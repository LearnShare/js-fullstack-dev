# 2.11.3 cluster 模块

## 1. 概述

cluster 模块用于创建进程集群，充分利用多核 CPU 提高应用性能。通过创建多个工作进程，cluster 模块可以实现负载均衡，将请求分发到不同的工作进程处理。理解 cluster 模块的使用对于构建高性能的 Node.js 应用非常重要。

## 2. 特性说明

- **进程集群**：创建多个工作进程充分利用多核 CPU。
- **负载均衡**：自动将请求分发到不同的工作进程。
- **进程管理**：可以管理和监控工作进程。
- **进程通信**：支持主进程和工作进程之间的通信。
- **自动重启**：工作进程崩溃时自动重启。

## 3. 语法与定义

### cluster 模块

```ts
// 判断是否为主进程
cluster.isPrimary: boolean
cluster.isWorker: boolean

// 创建工作进程
cluster.fork(env?: object): Worker

// 事件监听
cluster.on(event: string, listener: Function): void
```

## 4. 基本用法

### 示例 1：基本集群

```ts
// 文件: cluster-basic.ts
// 功能: 基本集群

import cluster from 'node:cluster';
import os from 'node:os';
import http from 'node:http';

if (cluster.isPrimary) {
    console.log('Primary process:', process.pid);
    
    const cpuCount = os.cpus().length;
    console.log(`Starting ${cpuCount} workers...`);
    
    // 创建工作进程
    for (let i = 0; i < cpuCount; i++) {
        cluster.fork();
    }
    
    // 监听工作进程退出
    cluster.on('exit', (worker, code, signal) => {
        console.log(`Worker ${worker.process.pid} died. Restarting...`);
        cluster.fork();
    });
} else {
    // 工作进程代码
    http.createServer((req, res) => {
        res.writeHead(200);
        res.end(`Hello from worker ${process.pid}`);
    }).listen(3000);
    
    console.log(`Worker ${process.pid} started`);
}
```

### 示例 2：进程通信

```ts
// 文件: cluster-communication.ts
// 功能: 进程通信

import cluster from 'node:cluster';

if (cluster.isPrimary) {
    const worker = cluster.fork();
    
    // 接收工作进程消息
    worker.on('message', (msg) => {
        console.log('Message from worker:', msg);
    });
    
    // 向工作进程发送消息
    worker.send({ type: 'task', data: 'Hello' });
} else {
    // 接收主进程消息
    process.on('message', (msg) => {
        console.log('Message from primary:', msg);
        // 向主进程发送响应
        process.send({ type: 'response', data: 'World' });
    });
}
```

### 示例 3：完整集群应用

```ts
// 文件: cluster-complete.ts
// 功能: 完整集群应用

import cluster from 'node:cluster';
import os from 'node:os';
import http from 'node:http';

if (cluster.isPrimary) {
    const cpuCount = os.cpus().length;
    console.log(`Primary ${process.pid} is running`);
    console.log(`Starting ${cpuCount} workers...`);
    
    // 创建工作进程
    for (let i = 0; i < cpuCount; i++) {
        const worker = cluster.fork();
        console.log(`Worker ${worker.process.pid} started`);
    }
    
    // 监听工作进程退出
    cluster.on('exit', (worker, code, signal) => {
        console.log(`Worker ${worker.process.pid} died (${signal || code}). Restarting...`);
        cluster.fork();
    });
    
    // 监听工作进程在线
    cluster.on('online', (worker) => {
        console.log(`Worker ${worker.process.pid} is online`);
    });
} else {
    // 工作进程：创建 HTTP 服务器
    http.createServer((req, res) => {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end(`Response from worker ${process.pid}\n`);
    }).listen(3000);
    
    console.log(`Worker ${process.pid} started server on port 3000`);
}
```

## 5. 参数说明：cluster 模块方法

| 方法/属性      | 类型     | 说明                                     | 示例                           |
|:---------------|:---------|:-----------------------------------------|:-------------------------------|
| **isPrimary**  | Boolean  | 是否为主进程                             | `cluster.isPrimary`            |
| **isWorker**   | Boolean  | 是否为工作进程                           | `cluster.isWorker`             |
| **fork()**     | Worker   | 创建工作进程                             | `cluster.fork()`               |
| **on()**       | Void     | 监听集群事件                             | `cluster.on('exit', ...)`      |

## 6. 返回值与状态说明

cluster 操作的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **fork()**   | Worker       | 返回工作进程对象                         |
| **事件**     | 各种类型     | 根据事件返回不同类型                     |

## 7. 代码示例：集群管理器

以下示例演示了如何构建集群管理器：

```ts
// 文件: cluster-manager.ts
// 功能: 集群管理器

import cluster from 'node:cluster';
import os from 'node:os';

class ClusterManager {
    private workers: Map<number, cluster.Worker> = new Map();
    private workerCount: number;
    
    constructor(workerCount?: number) {
        this.workerCount = workerCount || os.cpus().length;
    }
    
    start() {
        if (!cluster.isPrimary) {
            return;
        }
        
        console.log(`Primary ${process.pid} starting ${this.workerCount} workers...`);
        
        // 创建工作进程
        for (let i = 0; i < this.workerCount; i++) {
            this.createWorker();
        }
        
        // 监听事件
        cluster.on('exit', (worker, code, signal) => {
            console.log(`Worker ${worker.process.pid} died. Restarting...`);
            this.workers.delete(worker.process.pid!);
            this.createWorker();
        });
        
        cluster.on('online', (worker) => {
            console.log(`Worker ${worker.process.pid} is online`);
            this.workers.set(worker.process.pid!, worker);
        });
    }
    
    private createWorker() {
        const worker = cluster.fork();
        this.workers.set(worker.process.pid!, worker);
    }
    
    getWorkerCount(): number {
        return this.workers.size;
    }
    
    broadcast(message: any) {
        for (const worker of this.workers.values()) {
            worker.send(message);
        }
    }
}

// 使用
if (cluster.isPrimary) {
    const manager = new ClusterManager();
    manager.start();
} else {
    // 工作进程代码
    require('./app.js');
}
```

## 8. 输出结果说明

集群应用的输出结果：

```text
Primary 12345 starting 8 workers...
Worker 12346 is online
Worker 12347 is online
...
Worker 12346 started server on port 3000
Worker 12347 started server on port 3000
...
```

**逻辑解析**：
- 主进程创建工作进程
- 工作进程创建 HTTP 服务器
- 负载均衡自动分发请求

## 9. 使用场景

### 1. Web 服务器集群

创建 Web 服务器集群：

```ts
// Web 服务器集群示例
import cluster from 'node:cluster';
import os from 'node:os';

if (cluster.isPrimary) {
    for (let i = 0; i < os.cpus().length; i++) {
        cluster.fork();
    }
} else {
    require('./server.js');
}
```

### 2. CPU 密集型任务

并行处理 CPU 密集型任务：

```ts
// CPU 密集型任务示例
import cluster from 'node:cluster';

if (cluster.isPrimary) {
    // 分发任务到工作进程
    const tasks = [1, 2, 3, 4];
    let taskIndex = 0;
    
    cluster.on('online', (worker) => {
        if (taskIndex < tasks.length) {
            worker.send({ task: tasks[taskIndex++] });
        }
    });
} else {
    process.on('message', ({ task }) => {
        // 处理任务
        const result = processTask(task);
        process.send({ result });
    });
}
```

### 3. 高可用性

实现高可用性：

```ts
// 高可用性示例
import cluster from 'node:cluster';

if (cluster.isPrimary) {
    // 创建工作进程
    cluster.fork();
    
    // 自动重启
    cluster.on('exit', (worker) => {
        console.log('Worker died, restarting...');
        cluster.fork();
    });
}
```

## 10. 注意事项与常见错误

- **端口共享**：工作进程可以共享同一个端口
- **进程通信**：使用 IPC 进行进程间通信
- **状态共享**：工作进程之间不共享状态
- **资源管理**：注意工作进程的资源管理
- **性能考虑**：合理设置工作进程数量

## 11. 常见问题 (FAQ)

**Q: 工作进程可以共享端口吗？**
A: 可以，cluster 模块支持工作进程共享同一个端口。

**Q: 如何设置工作进程数量？**
A: 通常设置为 CPU 核心数，也可以根据需求调整。

**Q: 工作进程之间如何共享状态？**
A: 工作进程之间不共享状态，需要通过主进程或外部存储（如 Redis）共享。

## 12. 最佳实践

- **工作进程数量**：设置为 CPU 核心数
- **自动重启**：工作进程崩溃时自动重启
- **进程通信**：使用 IPC 进行进程间通信
- **负载均衡**：利用 cluster 的负载均衡功能
- **监控管理**：监控和管理工作进程

## 13. 对比分析：cluster vs child_process

| 维度             | cluster                                    | child_process                              |
|:-----------------|:--------------------------------------------|:--------------------------------------------|
| **用途**         | 创建进程集群充分利用多核 CPU                 | 执行外部命令或脚本                           |
| **进程类型**     | Node.js 进程                                | 任意子进程                                  |
| **通信方式**     | IPC（进程间通信）                            | 标准输入输出、IPC                            |
| **适用场景**     | Web 服务器、CPU 密集型任务                   | 执行外部命令、调用其他程序                   |

## 14. 练习任务

1. **集群实践**：
   - 创建进程集群
   - 实现负载均衡
   - 处理进程通信

2. **进程管理实践**：
   - 实现进程监控
   - 实现自动重启
   - 实现进程通信

3. **实际应用**：
   - 在实际项目中应用 cluster
   - 实现 Web 服务器集群
   - 实现高可用性

完成以上练习后，阶段二的学习就完成了。可以继续学习阶段三：工具链。

## 总结

cluster 模块用于创建进程集群：

- **核心功能**：创建进程集群、负载均衡、进程管理
- **使用场景**：Web 服务器、CPU 密集型任务、高可用性
- **最佳实践**：合理设置工作进程数量、自动重启、进程通信

掌握 cluster 模块有助于构建高性能的 Node.js 应用。

---

**最后更新**：2025-01-XX
