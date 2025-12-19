# 2.11.1 子进程与集群概述

## 1. 概述

子进程和集群是 Node.js 实现并行处理和充分利用多核 CPU 的重要机制。child_process 模块用于创建子进程执行外部命令或脚本，cluster 模块用于创建进程集群以充分利用多核 CPU。理解子进程和集群的使用对于并行处理、任务分发、性能优化等场景非常重要。

## 2. 特性说明

- **子进程创建**：可以创建子进程执行外部命令或脚本。
- **进程通信**：支持父子进程之间的通信。
- **进程集群**：可以创建进程集群充分利用多核 CPU。
- **负载均衡**：cluster 模块提供负载均衡功能。
- **进程管理**：可以管理和监控子进程。

## 3. 模块导入方式

### ES Modules 方式

```ts
import { spawn, exec, fork } from 'node:child_process';
import cluster from 'node:cluster';
```

### CommonJS 方式

```ts
const { spawn, exec, fork } = require('node:child_process');
const cluster = require('node:cluster');
```

## 4. child_process vs cluster

| 特性         | child_process                              | cluster                                    |
|:-------------|:-------------------------------------------|:-------------------------------------------|
| **用途**     | 执行外部命令或脚本                         | 创建进程集群充分利用多核 CPU               |
| **进程类型** | 任意子进程                                 | Node.js 进程                               |
| **通信方式** | 标准输入输出、IPC                          | IPC（进程间通信）                          |
| **适用场景** | 执行外部命令、调用其他程序                 | Web 服务器、CPU 密集型任务                 |

## 5. 参数说明：子进程和集群常用 API

| API 名称      | 说明                                     | 示例                           |
|:--------------|:-----------------------------------------|:-------------------------------|
| **spawn**     | 创建子进程（流式输出）                    | `spawn('node', ['script.js'])` |
| **exec**      | 执行命令（缓冲输出）                      | `exec('ls -la', callback)`     |
| **fork**      | 创建 Node.js 子进程（IPC 通信）           | `fork('./worker.js')`          |
| **cluster.fork()**| 创建工作进程                            | `cluster.fork()`               |

## 6. 返回值与状态说明

子进程和集群操作的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **spawn/exec/fork**| ChildProcess | 返回子进程对象                           |
| **cluster.fork()**| Worker     | 返回工作进程对象                         |

## 7. 代码示例：基本使用

以下示例演示了子进程和集群的基本使用：

```ts
// 文件: child-cluster-basic.ts
// 功能: 子进程和集群基本使用

import { spawn, exec } from 'node:child_process';
import cluster from 'node:cluster';

// 1. 使用 spawn 创建子进程
const child = spawn('node', ['--version']);
child.stdout.on('data', (data) => {
    console.log('Node version:', data.toString());
});

// 2. 使用 exec 执行命令
exec('ls -la', (error, stdout, stderr) => {
    if (error) {
        console.error('Error:', error);
        return;
    }
    console.log('Output:', stdout);
});

// 3. 使用 cluster 创建进程集群
if (cluster.isPrimary) {
    console.log('Primary process:', process.pid);
    // 创建工作进程
    const worker = cluster.fork();
    worker.on('message', (msg) => {
        console.log('Message from worker:', msg);
    });
} else {
    console.log('Worker process:', process.pid);
    process.send({ type: 'ready' });
}
```

## 8. 输出结果说明

子进程和集群的输出结果：

```text
Node version: v22.0.0
Output: total 100
drwxr-xr-x  ...
Primary process: 12345
Worker process: 12346
Message from worker: { type: 'ready' }
```

**逻辑解析**：
- spawn 用于流式处理子进程输出
- exec 用于执行命令并获取完整输出
- cluster 用于创建进程集群

## 9. 使用场景

### 1. 执行外部命令

执行系统命令或外部程序：

```ts
// 执行外部命令示例
import { exec } from 'node:child_process';

exec('git status', (error, stdout, stderr) => {
    if (error) {
        console.error('Error:', error);
        return;
    }
    console.log(stdout);
});
```

### 2. 并行处理

使用子进程进行并行处理：

```ts
// 并行处理示例
import { fork } from 'node:child_process';

const workers = [];
for (let i = 0; i < 4; i++) {
    const worker = fork('./worker.js');
    workers.push(worker);
}
```

### 3. 进程集群

创建进程集群提高性能：

```ts
// 进程集群示例
import cluster from 'node:cluster';
import os from 'node:os';

if (cluster.isPrimary) {
    const cpuCount = os.cpus().length;
    for (let i = 0; i < cpuCount; i++) {
        cluster.fork();
    }
} else {
    // 工作进程代码
    require('./app.js');
}
```

## 10. 注意事项与常见错误

- **进程通信**：注意父子进程之间的通信方式
- **错误处理**：处理子进程的错误和退出
- **资源管理**：注意子进程的资源管理
- **性能考虑**：子进程创建有开销，不要过度使用
- **安全性**：注意命令注入风险，验证输入

## 11. 常见问题 (FAQ)

**Q: spawn、exec、fork 有什么区别？**
A: spawn 流式输出，exec 缓冲输出，fork 专门用于 Node.js 进程且支持 IPC。

**Q: 什么时候使用 cluster？**
A: 需要充分利用多核 CPU 时使用，如 Web 服务器、CPU 密集型任务。

**Q: 子进程如何与父进程通信？**
A: 使用标准输入输出、IPC（fork）或消息传递。

## 12. 最佳实践

- **选择合适的方法**：根据需求选择 spawn、exec 或 fork
- **错误处理**：完善的错误处理和进程监控
- **资源管理**：注意子进程的资源管理和清理
- **安全性**：验证输入，防止命令注入
- **性能优化**：合理使用子进程和集群，避免过度使用

## 13. 对比分析：spawn vs exec vs fork

| 维度             | spawn                                    | exec                                    | fork                                    |
|:-----------------|:------------------------------------------|:----------------------------------------|:----------------------------------------|
| **输出方式**     | 流式                                      | 缓冲                                    | 流式                                    |
| **适用场景**     | 长时间运行、大量输出                      | 短命令、小输出                           | Node.js 进程、IPC 通信                  |
| **内存使用**     | 低（流式）                                | 高（缓冲）                              | 低（流式）                              |
| **通信方式**     | 标准输入输出                              | 标准输入输出                             | IPC（进程间通信）                        |

## 14. 练习任务

1. **子进程实践**：
   - 使用 spawn、exec、fork 创建子进程
   - 处理子进程的输出和错误
   - 实现进程通信

2. **集群实践**：
   - 使用 cluster 创建进程集群
   - 实现负载均衡
   - 处理进程间通信

3. **实际应用**：
   - 在实际项目中应用子进程和集群
   - 实现并行处理功能
   - 实现进程集群

完成以上练习后，继续学习下一节：child_process 模块。

## 总结

子进程和集群是 Node.js 并行处理的重要机制：

- **child_process**：创建子进程执行外部命令或脚本
- **cluster**：创建进程集群充分利用多核 CPU
- **使用场景**：并行处理、任务分发、性能优化

掌握子进程和集群有助于实现高性能的 Node.js 应用。

---

**最后更新**：2025-01-XX
