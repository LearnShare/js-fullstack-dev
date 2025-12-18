# 1.2.5 Worker Threads 并行计算机制

## 1. 概述

虽然 Node.js 的 JavaScript 执行是单线程的，但自 Node.js 10.5.0 起，官方引入了 `worker_threads` 模块，提供了真正的操作系统级多线程能力。与子进程（Child Process）完全隔离的内存空间不同，工作线程（Worker Threads）可以通过 `SharedArrayBuffer` 共享内存，且通信开销极低。它是 Node.js 应对计算密集型任务（如图像处理、科学计算、加密运算）的终极解决方案。

## 2. 特性说明

- **独立隔离性**：每个 Worker 拥有独立的 V8 实例、Libuv 事件循环及 Node.js 运行环境。
- **物理并行性**：不同于异步 I/O，多个 Worker 可以同时利用多个 CPU 核心进行计算。
- **轻量高效**：相比于子进程，Worker 的内存占用和启动耗时显著降低。
- **零拷贝通信**：通过转移（Transferable）或共享（Shared）缓冲区实现大规模数据的高效交换。

## 3. 线程隔离与共享逻辑

Worker Threads 的底层模型如下。

| 逻辑组件         | 隔离/共享状态                                                      | 说明                                         |
|:-----------------|:-------------------------------------------------------------------|:---------------------------------------------|
| **V8 Isolate**   | 严格隔离                                                           | 每个线程有自己的堆栈和垃圾回收机制。         |
| **Global 变量**  | 严格隔离                                                           | 主线程的全局变量对 Worker 不可见。           |
| **共享内存**     | 显式共享                                                           | 需使用 `SharedArrayBuffer` 才能实现引用共享。|
| **文件描述符**   | 部分共享                                                           | 多个线程可以同时操作同一个 Socket 或文件。   |

## 4. 参数说明：Worker 构造选项

在使用 `new Worker(path, options)` 创建线程时，常用的配置选项如下。

| 选项名           | 类型     | 逻辑说明                                         | 默认值 |
|:-----------------|:---------|:-------------------------------------------------|:-------|
| **workerData**   | Any      | 传递给 Worker 的初始数据。执行结构化克隆。       | null   |
| **eval**         | Boolean  | 为 true 时，第一个参数被视为脚本内容而非路径。   | false  |
| **resourceLimits**| Object   | 限制该线程的堆内存、栈深度等资源占用。           | null   |

## 5. 返回值与状态说明

创建 Worker 实例后，可以通过以下属性和事件获取状态。

| 属性/事件        | 类型     | 逻辑说明                                         |
|:-----------------|:---------|:-------------------------------------------------|
| `threadId`       | Number   | 该线程在当前进程内的唯一编号。                   |
| `on('message')`  | Event    | 监听 Worker 通过 `postMessage` 发回的数据。      |
| `on('exit')`     | Event    | 监听 Worker 退出事件，返回退出码。               |

## 6. 代码示例：计算密集型任务并行化

```ts
// 文件: worker-prime-calc.ts
// 功能: 演示如何利用多线程进行质数计算

import { Worker, isMainThread, parentPort, workerData } from 'node:worker_threads';

if (isMainThread) {
  // --- 主线程逻辑 ---
  console.log('[Main] 准备发起高耗时质数计算...');

  const worker = new Worker(__filename, {
    workerData: { limit: 10000000 }
  });

  worker.on('message', (count) => {
    console.log(`[Main] 计算完成！1000万以内的质数共有: ${count} 个`);
  });

  console.log('[Main] 我现在依然可以响应用户的其它 HTTP 请求');
} else {
  // --- Worker 线程逻辑 ---
  const { limit } = workerData;
  let count = 0;

  // 模拟极度耗时的同步计算
  for (let i = 2; i <= limit; i++) {
    let isPrime = true;
    for (let j = 2; j <= Math.sqrt(i); j++) {
      if (i % j === 0) { isPrime = false; break; }
    }
    if (isPrime) count++;
  }

  parentPort?.postMessage(count);
}
```

## 7. 输出结果说明

```text
[Main] 准备发起高耗时质数计算...
[Main] 我现在依然可以响应用户的其它 HTTP 请求
[Main] 计算完成！1000万以内的质数共有: 664579 个
```

**逻辑解析**：虽然质数计算循环占满了 CPU，但它发生在 Worker 线程中。主线程在创建 Worker 后立即恢复了对事件循环的监听，保证了应用的整体可用性。

## 8. 注意事项与常见错误

- **滥用成本**：创建 Worker 的开销约需 10ms-30ms，如果任务本身只需 1ms，使用多线程反而会变慢。
- **变量无法直接引用**：在 Worker 中尝试使用主线程定义的全局变量会报 `ReferenceError`。
- **内存竞争**：在使用 `SharedArrayBuffer` 时，必须结合 `Atomics` 模块进行原子操作，防止数据竞争。

## 9. 常见问题 (FAQ)

**Q: Worker Threads 和子进程 (Child Process) 的区别是什么？**
A: Worker 共享同一个操作系统进程的资源，通信更快且支持共享内存。子进程是完全独立的进程，启动更慢且内存占用大。

**Q: 既然有了 Worker，是不是 Node.js 就不怕阻塞了？**
A: 理论上是。但业务中 90% 的阻塞源于 I/O 逻辑不当（如使用了 Sync 方法），这些应通过异步解决。Worker 应仅用于计算密集型场景。

## 10. 最佳实践

- **线程池池化**：在生产环境中使用 `piscina` 等第三方库管理 Worker 线程池，避免频繁创建/销毁的性能损耗。
- **计算逻辑解耦**：将计算逻辑抽取到独立的 `.worker.ts` 文件中，方便维护与单元测试。
- **最小化通信**：尽量通过 `workerData` 传入小数据，大数据推荐使用 `SharedArrayBuffer` 或 `Transferable Objects`。

## 11. 对比分析：Worker vs Cluster

| 维度             | Worker Threads                                   | Cluster (集群模块)                               |
|:-----------------|:-------------------------------------------------|:-------------------------------------------------|
| **资源层级**     | 线程级。多个线程共用一个进程。                   | 进程级。每个 Worker 都是完整独立的进程。         |
| **适用场景**     | 并行处理复杂计算逻辑。                           | 并行处理网络连接，提升单机并发上限。             |
| **端口共享**     | 不支持。                                         | 支持。多个进程可以共用同一个 TCP 端口。          |

## 12. 练习任务

1. **性能实测**：编写代码对比“单线程循环 1 亿次”与“拆分为 4 个 Worker 各循环 2500 万次”的总耗时。
2. **原子操作练习**：使用 `SharedArrayBuffer` 和 `Atomics` 在两个 Worker 之间实现一个共享的“点赞计数器”。
3. **架构优化**：将之前阻塞示例中的 `/block` 逻辑改用 Worker 实现，并验证并发访问的响应情况。
