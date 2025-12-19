# 2.10.3 进程信息与控制（process）

## 1. 概述

process 模块提供了访问和控制当前 Node.js 进程的能力，包括进程 ID、环境变量、命令行参数、工作目录、进程退出等。理解 process 模块的使用对于进程管理、环境配置、信号处理等场景非常重要。

## 2. 特性说明

- **进程信息**：访问进程 ID、版本、平台等信息。
- **环境变量**：访问和设置环境变量。
- **命令行参数**：访问命令行参数。
- **工作目录**：获取和设置工作目录。
- **进程控制**：控制进程退出、信号处理等。

## 3. 语法与定义

### process 模块常用属性和方法

```ts
// 进程信息
process.pid: number
process.version: string
process.platform: string
process.cwd(): string
process.chdir(directory: string): void

// 环境变量
process.env: object

// 命令行参数
process.argv: string[]

// 进程退出
process.exit(code?: number): void
process.on(event: string, listener: Function): void
```

## 4. 基本用法

### 示例 1：进程信息

```ts
// 文件: process-info.ts
// 功能: 获取进程信息

import process from 'node:process';

console.log('Process ID:', process.pid);
console.log('Node Version:', process.version);
console.log('Platform:', process.platform);
console.log('Working Directory:', process.cwd());
console.log('Command Line Args:', process.argv);
```

### 示例 2：环境变量

```ts
// 文件: process-env.ts
// 功能: 环境变量处理

import process from 'node:process';

// 读取环境变量
const nodeEnv = process.env.NODE_ENV || 'development';
const port = parseInt(process.env.PORT || '3000', 10);

console.log('NODE_ENV:', nodeEnv);
console.log('PORT:', port);

// 设置环境变量（仅当前进程）
process.env.CUSTOM_VAR = 'value';
console.log('CUSTOM_VAR:', process.env.CUSTOM_VAR);
```

### 示例 3：进程控制

```ts
// 文件: process-control.ts
// 功能: 进程控制

import process from 'node:process';

// 优雅退出
process.on('SIGTERM', () => {
    console.log('Received SIGTERM, shutting down gracefully');
    // 清理资源
    process.exit(0);
});

process.on('SIGINT', () => {
    console.log('Received SIGINT (Ctrl+C), shutting down');
    process.exit(0);
});

// 未捕获异常处理
process.on('uncaughtException', (error) => {
    console.error('Uncaught Exception:', error);
    process.exit(1);
});

// 未处理的 Promise 拒绝
process.on('unhandledRejection', (reason, promise) => {
    console.error('Unhandled Rejection:', reason);
    process.exit(1);
});
```

## 5. 参数说明：process 模块方法

| 方法/属性      | 类型     | 说明                                     | 示例                           |
|:---------------|:---------|:-----------------------------------------|:-------------------------------|
| **pid**        | Number   | 进程 ID                                  | `12345`                        |
| **version**    | String   | Node.js 版本                             | `'v22.0.0'`                    |
| **platform**   | String   | 平台                                     | `'win32'`, `'linux'`           |
| **cwd()**      | String   | 当前工作目录                             | `'/path/to/dir'`               |
| **chdir()**    | Void     | 更改工作目录                             | `process.chdir('/new/path')`   |
| **exit()**     | Void     | 退出进程                                 | `process.exit(0)`              |
| **env**        | Object   | 环境变量对象                             | `{ NODE_ENV: 'production' }`   |
| **argv**       | Array    | 命令行参数数组                           | `['node', 'script.js', 'arg1']`|

## 6. 返回值与状态说明

process 模块操作的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **进程信息** | 各种类型     | 根据属性返回不同类型                     |
| **exit**     | Void         | 退出进程，不返回                         |

## 7. 代码示例：进程管理工具

以下示例演示了如何构建进程管理工具：

```ts
// 文件: process-manager.ts
// 功能: 进程管理工具

import process from 'node:process';

class ProcessManager {
    private shutdownHandlers: Array<() => Promise<void>> = [];
    
    getInfo() {
        return {
            pid: process.pid,
            version: process.version,
            platform: process.platform,
            cwd: process.cwd(),
            env: process.env.NODE_ENV || 'development',
            memoryUsage: process.memoryUsage()
        };
    }
    
    registerShutdownHandler(handler: () => Promise<void>) {
        this.shutdownHandlers.push(handler);
    }
    
    async gracefulShutdown(signal: string) {
        console.log(`Received ${signal}, shutting down gracefully...`);
        
        // 执行关闭处理程序
        for (const handler of this.shutdownHandlers) {
            try {
                await handler();
            } catch (error) {
                console.error('Shutdown handler error:', error);
            }
        }
        
        process.exit(0);
    }
    
    setupSignalHandlers() {
        process.on('SIGTERM', () => this.gracefulShutdown('SIGTERM'));
        process.on('SIGINT', () => this.gracefulShutdown('SIGINT'));
        
        process.on('uncaughtException', (error) => {
            console.error('Uncaught Exception:', error);
            this.gracefulShutdown('uncaughtException');
        });
        
        process.on('unhandledRejection', (reason, promise) => {
            console.error('Unhandled Rejection:', reason);
            this.gracefulShutdown('unhandledRejection');
        });
    }
}

// 使用
const manager = new ProcessManager();

manager.registerShutdownHandler(async () => {
    console.log('Closing database connections...');
    // 关闭数据库连接
});

manager.registerShutdownHandler(async () => {
    console.log('Saving state...');
    // 保存状态
});

manager.setupSignalHandlers();
console.log('Process Info:', manager.getInfo());
```

## 8. 输出结果说明

进程管理的输出结果：

```text
Process Info: {
  pid: 12345,
  version: 'v22.0.0',
  platform: 'win32',
  cwd: 'C:\\works',
  env: 'development',
  memoryUsage: { rss: ..., heapTotal: ..., heapUsed: ... }
}
```

**逻辑解析**：
- 获取进程的基本信息
- 注册关闭处理程序
- 设置信号处理，实现优雅退出

## 9. 使用场景

### 1. 环境配置

根据环境变量配置应用：

```ts
// 环境配置示例
import process from 'node:process';

const config = {
    env: process.env.NODE_ENV || 'development',
    port: parseInt(process.env.PORT || '3000', 10),
    database: {
        host: process.env.DB_HOST || 'localhost',
        port: parseInt(process.env.DB_PORT || '5432', 10)
    }
};
```

### 2. 优雅退出

实现应用的优雅退出：

```ts
// 优雅退出示例
import process from 'node:process';

let isShuttingDown = false;

async function gracefulShutdown() {
    if (isShuttingDown) return;
    isShuttingDown = true;
    
    console.log('Shutting down...');
    // 清理资源
    process.exit(0);
}

process.on('SIGTERM', gracefulShutdown);
process.on('SIGINT', gracefulShutdown);
```

### 3. 错误处理

处理未捕获的异常：

```ts
// 错误处理示例
import process from 'node:process';

process.on('uncaughtException', (error) => {
    console.error('Uncaught Exception:', error);
    // 记录错误
    // 清理资源
    process.exit(1);
});

process.on('unhandledRejection', (reason, promise) => {
    console.error('Unhandled Rejection:', reason);
    // 记录错误
    process.exit(1);
});
```

## 10. 注意事项与常见错误

- **环境变量类型**：环境变量都是字符串，需要类型转换
- **进程退出**：正确使用进程退出，避免资源泄漏
- **信号处理**：理解不同信号的含义
- **工作目录**：注意工作目录的变化
- **内存使用**：`memoryUsage()` 返回的是快照，不是实时值

## 11. 常见问题 (FAQ)

**Q: 环境变量都是字符串吗？**
A: 是的，环境变量都是字符串，需要手动转换为其他类型。

**Q: 如何实现优雅退出？**
A: 监听 SIGTERM 和 SIGINT 信号，执行清理操作后调用 `process.exit()`。

**Q: uncaughtException 和 unhandledRejection 有什么区别？**
A: `uncaughtException` 处理同步异常，`unhandledRejection` 处理 Promise 拒绝。

## 12. 最佳实践

- **环境配置**：使用 process.env 进行环境配置
- **优雅退出**：实现优雅退出，清理资源
- **错误处理**：处理未捕获的异常和未处理的 Promise 拒绝
- **信号处理**：正确处理进程信号
- **类型转换**：环境变量需要类型转换

## 13. 对比分析：不同退出方式

| 方式             | 说明                                     | 适用场景                       |
|:-----------------|:-----------------------------------------|:-------------------------------|
| **process.exit(0)**| 正常退出                                | 正常结束                       |
| **process.exit(1)**| 异常退出                                | 发生错误时退出                 |
| **SIGTERM**      | 终止信号（可捕获）                        | 优雅退出                       |
| **SIGINT**       | 中断信号（Ctrl+C，可捕获）                | 用户中断                       |

## 14. 练习任务

1. **进程信息实践**：
   - 获取进程信息
   - 处理环境变量
   - 实现配置管理

2. **进程控制实践**：
   - 实现优雅退出
   - 处理进程信号
   - 实现错误处理

3. **实际应用**：
   - 在实际项目中应用 process 模块
   - 实现进程管理功能
   - 实现环境配置管理

完成以上练习后，继续学习下一章：子进程与集群。

## 总结

process 模块提供了进程信息和控制能力：

- **核心功能**：进程信息、环境变量、进程控制
- **使用场景**：环境配置、优雅退出、错误处理
- **最佳实践**：环境配置、优雅退出、错误处理

掌握 process 模块有助于进行进程管理和应用配置。

---

**最后更新**：2025-01-XX
