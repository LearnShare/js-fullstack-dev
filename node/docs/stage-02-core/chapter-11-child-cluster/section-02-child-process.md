# 2.11.2 child_process 模块

## 1. 概述

child_process 模块提供了创建和管理子进程的能力，可以执行外部命令、调用其他程序、并行处理任务等。理解 child_process 的使用对于系统集成、任务并行化、性能优化等场景非常重要。

## 2. 特性说明

- **多种创建方式**：提供 spawn、exec、execFile、fork 等多种方式。
- **进程通信**：支持标准输入输出、IPC 通信。
- **进程管理**：可以监控和管理子进程。
- **错误处理**：完善的错误处理机制。
- **跨平台支持**：提供跨平台的一致性 API。

## 3. 语法与定义

### spawn

```ts
spawn(command: string, args?: string[], options?: SpawnOptions): ChildProcess
```

### exec

```ts
exec(command: string, options?: ExecOptions, callback?: (error, stdout, stderr) => void): ChildProcess
```

### fork

```ts
fork(modulePath: string, args?: string[], options?: ForkOptions): ChildProcess
```

## 4. 基本用法

### 示例 1：spawn（流式输出）

```ts
// 文件: child-spawn.ts
// 功能: 使用 spawn 创建子进程

import { spawn } from 'node:child_process';

const child = spawn('node', ['--version']);

child.stdout.on('data', (data) => {
    console.log('stdout:', data.toString());
});

child.stderr.on('data', (data) => {
    console.error('stderr:', data.toString());
});

child.on('close', (code) => {
    console.log('Child process exited with code', code);
});
```

### 示例 2：exec（缓冲输出）

```ts
// 文件: child-exec.ts
// 功能: 使用 exec 执行命令

import { exec } from 'node:child_process';

exec('ls -la', (error, stdout, stderr) => {
    if (error) {
        console.error('Error:', error);
        return;
    }
    if (stderr) {
        console.error('Stderr:', stderr);
        return;
    }
    console.log('Output:', stdout);
});
```

### 示例 3：fork（IPC 通信）

```ts
// 文件: child-fork.ts
// 功能: 使用 fork 创建子进程

import { fork } from 'node:child_process';

const child = fork('./worker.js');

child.on('message', (msg) => {
    console.log('Message from child:', msg);
});

child.send({ type: 'start', data: 'Hello' });

// worker.js
process.on('message', (msg) => {
    console.log('Message from parent:', msg);
    process.send({ type: 'response', data: 'World' });
});
```

## 5. 参数说明：child_process 方法参数

### spawn 参数

| 参数名       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **command**  | String   | 要执行的命令                             | `'node'`                       |
| **args**     | Array    | 命令参数（可选）                         | `['--version']`                |
| **options**  | Object   | 选项（可选）                             | `{ cwd: '/path', env: {...} }`|

### exec 参数

| 参数名       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **command**  | String   | 要执行的命令（完整命令）                 | `'ls -la'`                     |
| **options**  | Object   | 选项（可选）                             | `{ timeout: 5000 }`            |
| **callback** | Function | 回调函数（可选）                         | `(error, stdout, stderr) => {}`|

## 6. 返回值与状态说明

child_process 操作的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **spawn/exec/fork**| ChildProcess | 返回子进程对象                           |
| **子进程事件** | 各种类型     | 根据事件返回不同类型                     |

## 7. 代码示例：完整的子进程管理

以下示例演示了如何构建完整的子进程管理系统：

```ts
// 文件: child-complete.ts
// 功能: 完整的子进程管理

import { spawn, exec } from 'node:child_process';
import { promisify } from 'node:util';

const execAsync = promisify(exec);

class ProcessManager {
    async executeCommand(command: string, args: string[] = []): Promise<string> {
        return new Promise((resolve, reject) => {
            const child = spawn(command, args, {
                stdio: 'pipe'
            });
            
            let stdout = '';
            let stderr = '';
            
            child.stdout.on('data', (data) => {
                stdout += data.toString();
            });
            
            child.stderr.on('data', (data) => {
                stderr += data.toString();
            });
            
            child.on('close', (code) => {
                if (code === 0) {
                    resolve(stdout);
                } else {
                    reject(new Error(`Process exited with code ${code}: ${stderr}`));
                }
            });
            
            child.on('error', (error) => {
                reject(error);
            });
        });
    }
    
    async executeCommandSimple(command: string): Promise<string> {
        try {
            const { stdout } = await execAsync(command);
            return stdout;
        } catch (error: any) {
            throw new Error(`Command failed: ${error.message}`);
        }
    }
}

// 使用
const manager = new ProcessManager();

async function example() {
    try {
        const version = await manager.executeCommand('node', ['--version']);
        console.log('Node version:', version);
        
        const files = await manager.executeCommandSimple('ls -la');
        console.log('Files:', files);
    } catch (error) {
        console.error('Error:', error);
    }
}

example();
```

## 8. 输出结果说明

子进程管理的输出结果：

```text
Node version: v22.0.0
Files: total 100
drwxr-xr-x  ...
```

**逻辑解析**：
- 使用 Promise 封装子进程操作
- 处理标准输出和错误输出
- 处理进程退出码和错误

## 9. 使用场景

### 1. 执行系统命令

执行系统命令或外部程序：

```ts
// 执行系统命令示例
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

const tasks = [1, 2, 3, 4];
const workers = tasks.map(task => {
    const worker = fork('./worker.js');
    worker.send({ task });
    return worker;
});
```

### 3. 系统集成

集成外部系统或工具：

```ts
// 系统集成示例
import { spawn } from 'node:child_process';

function runScript(scriptPath: string) {
    const child = spawn('node', [scriptPath]);
    child.stdout.pipe(process.stdout);
    child.stderr.pipe(process.stderr);
}
```

## 10. 注意事项与常见错误

- **命令注入**：注意命令注入风险，验证和清理输入
- **错误处理**：完善的错误处理和进程监控
- **资源管理**：注意子进程的资源管理和清理
- **性能考虑**：子进程创建有开销，不要过度使用
- **跨平台**：注意不同平台的命令差异

## 11. 常见问题 (FAQ)

**Q: spawn、exec、fork 如何选择？**
A: spawn 用于流式输出，exec 用于短命令，fork 用于 Node.js 进程和 IPC 通信。

**Q: 如何实现进程间通信？**
A: 使用 fork 创建子进程，通过 `send()` 和 `message` 事件通信。

**Q: 如何处理子进程的错误？**
A: 监听 `error` 事件和检查退出码。

## 12. 最佳实践

- **选择合适的方法**：根据需求选择 spawn、exec 或 fork
- **错误处理**：完善的错误处理和进程监控
- **安全性**：验证输入，防止命令注入
- **资源管理**：注意子进程的资源管理和清理
- **性能优化**：合理使用子进程，避免过度使用

## 13. 对比分析：spawn vs exec vs fork

| 维度             | spawn                                    | exec                                    | fork                                    |
|:-----------------|:------------------------------------------|:----------------------------------------|:----------------------------------------|
| **输出方式**     | 流式                                      | 缓冲                                    | 流式                                    |
| **适用场景**     | 长时间运行、大量输出                      | 短命令、小输出                           | Node.js 进程、IPC 通信                  |
| **内存使用**     | 低（流式）                                | 高（缓冲）                              | 低（流式）                              |
| **通信方式**     | 标准输入输出                              | 标准输入输出                             | IPC（进程间通信）                        |

## 14. 练习任务

1. **spawn 实践**：
   - 使用 spawn 创建子进程
   - 处理流式输出
   - 实现进程通信

2. **exec 实践**：
   - 使用 exec 执行命令
   - 处理缓冲输出
   - 实现错误处理

3. **fork 实践**：
   - 使用 fork 创建子进程
   - 实现 IPC 通信
   - 实现任务分发

4. **实际应用**：
   - 在实际项目中应用 child_process
   - 实现并行处理功能
   - 实现系统集成

完成以上练习后，继续学习下一节：cluster 模块。

## 总结

child_process 模块提供了创建和管理子进程的能力：

- **核心功能**：spawn、exec、fork 等多种创建方式
- **使用场景**：执行外部命令、并行处理、系统集成
- **最佳实践**：选择合适的方法、错误处理、安全性

掌握 child_process 模块有助于实现并行处理和系统集成。

---

**最后更新**：2025-01-XX
