# 1.2.3 Libuv 异步调度与事件循环

## 1. 概述

Libuv 是用 C 语言编写的高性能异步非阻塞 I/O 库，是 Node.js 跨平台异步特性的底层支柱。它通过维护一套精密的“事件循环（Event Loop）”调度算法，并封装了不同操作系统的异步原语（如 Linux 的 epoll、Windows 的 IOCP），使得单线程的 JavaScript 能够高效处理数万个并发连接。

## 2. 特性说明

- **非阻塞 I/O**：通过操作系统内核的通知机制实现 I/O 多路复用，不挂起进程。
- **线程池分配**：对于无法直接异步化的任务（如文件 I/O、DNS 查询），由内置线程池接管。
- **高精度定时器**：提供毫秒级的任务调度能力。
- **跨平台一致性**：在所有支持的平台上提供统一的异步编程接口。

## 3. 事件循环阶段逻辑

Node.js 进程启动后，Libuv 会开启一个无限循环（Tick），其物理执行过程分为六个阶段。

| 阶段名称             | 逻辑任务                                                           |
|:---------------------|:-------------------------------------------------------------------|
| **1. Timers**        | 执行 `setTimeout()` 和 `setInterval()` 到期的回调。                |
| **2. Pending I/O**   | 执行被延迟到下一轮循环的 I/O 回调（如 TCP 错误）。                 |
| **3. Idle, Prepare** | 仅内部使用，用于准备后续的 I/O 轮询。                              |
| **4. Poll**          | 轮询新 I/O 事件。若无定时器且无 I/O，可能在此阻塞等待（Sleep）。   |
| **5. Check**         | 执行 `setImmediate()` 的回调。                                     |
| **6. Close**         | 执行所有 `close` 事件的回调（如 `socket.on('close')`）。           |

**优先级补充**：在阶段转换间隙，主线程会优先清空 **微任务队列**（`process.nextTick` 优先级高于 Promise）。

## 4. 参数说明：线程池配置

可以通过环境变量调整 Libuv 处理任务的并发能力。

| 环境变量              | 类型     | 默认值 | 最大值 | 说明                                             |
|:----------------------|:---------|:-------|:-------|:-------------------------------------------------|
| `UV_THREADPOOL_SIZE`  | Number   | 4      | 128    | 调整 Libuv 线程池中工作线程的数量。              |

## 5. 返回值与状态说明

通过 `perf_hooks` 等模块可以监控 Libuv 的调度状态。

| 属性/方法             | 类型     | 逻辑说明                                         |
|:----------------------|:---------|:-------------------------------------------------|
| `eventLoopDelay`      | Number   | 测量事件循环的一轮耗时，用于衡量主线程负载。     |
| `threadpoolUsage()`   | Object   | 返回线程池的活跃线程数及队列排队情况。           |

## 6. 代码示例：任务执行时序演示

```ts
// 文件: event-loop-demo.ts
// 功能: 演示在 I/O 回调内触发宏任务与微任务的确定性顺序

import { readFile } from 'node:fs';

import { readFile } from 'node:fs';

readFile('package.json', (): void => {
  console.log('--- 进入 Poll 阶段回调 ---');

  setTimeout((): void => console.log('1. Timers 阶段: setTimeout'), 0);
  setImmediate((): void => console.log('2. Check 阶段: setImmediate'));

  process.nextTick((): void => console.log('3. 微任务: nextTick'));
  Promise.resolve().then((): void => console.log('4. 微任务: Promise'));
});
```

## 7. 输出结果说明

```text
--- 进入 Poll 阶段回调 ---
3. 微任务: nextTick
4. 微任务: Promise
2. Check 阶段: setImmediate
1. Timers 阶段: setTimeout
```

**逻辑解析**：在 Poll 阶段的回调执行完毕后，主线程会立即清空微任务（3, 4），然后由于 Poll 阶段结束后紧跟 Check 阶段（5），所以 `setImmediate`（2）会优先于下一轮循环的 `setTimeout`（1）执行。

## 8. 注意事项与常见错误

- **阻塞 Poll 阶段**：如果在 Poll 阶段运行耗时的 JS 代码，会导致后续所有的 I/O 回调被积压。
- **线程池耗尽**：如果同时发起大量文件 I/O，而线程池较小，会导致新请求在队列中长时间排队。
- **nextTick 递归**：递归调用 `process.nextTick` 会导致事件循环永远无法进入下一个阶段，造成应用假死。

## 9. 常见问题 (FAQ)

**Q: 为什么在主脚本中运行 setImmediate 和 setTimeout(0) 的顺序不固定？**
A: 因为主脚本执行完后，由于系统性能波动，进入事件循环的时间点可能已经超过了定时器的 1ms 阈值，也可能没到。但在 I/O 回调中，顺序是 100% 固定的。

**Q: 既然 Node.js 是单线程的，如何利用多核 CPU 进行 I/O？**
A: 依靠 Libuv 的线程池。虽然处理结果的回调是单线程执行的，但读取文件、解密等实际计算是由多个 C++ 线程在底层并行完成的。

## 10. 最佳实践

- **环境变量前置**：必须在进程启动之初（如 Shell 中）设置 `UV_THREADPOOL_SIZE`，在 JS 代码运行中设置通常无效。
- **计算任务剥离**：不要在事件循环中处理大 JSON 解析或复杂正则。
- **监控 Lag**：使用 `perf_hooks` 定期上报 Event Loop Lag 指标。

## 11. 对比分析：setTimeout(0) vs setImmediate

| 特性项               | setTimeout(0)                     | setImmediate                      |
|:---------------------|:----------------------------------|:----------------------------------|
| **所属阶段**         | Timers (第一阶段)                 | Check (第五阶段)                  |
| **执行逻辑**         | 检查最小堆中的过期任务。          | 检查活跃的即时任务队列。          |
| **推荐场景**         | 需要逻辑上的“尽快执行”。          | 确保在当前 I/O 完成后立即执行。   |

## 12. 练习任务

1. **时序推演**：编写包含 `nextTick`、`Promise`、`setImmediate` 的复杂嵌套代码，并预测输出。
2. **性能基准**：设置 `UV_THREADPOOL_SIZE=1`，并发读取 10 个 1GB 的大文件，观察总耗时。
3. **延迟测量**：使用 `perf_hooks` 模块，测量在密集计算下事件循环的延迟增加。
