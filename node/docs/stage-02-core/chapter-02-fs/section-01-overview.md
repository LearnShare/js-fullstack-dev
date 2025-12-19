# 2.2.1 文件系统概述

## 1. 概述

Node.js 的文件系统模块（fs）提供了与文件系统交互的完整 API，包括文件读写、目录操作、文件监听等功能。fs 模块支持同步和异步两种操作方式，以及基于 Promise 的现代 API。理解文件系统模块的使用对于构建后端应用至关重要。

## 2. 特性说明

- **同步与异步 API**：提供同步和异步两种操作方式，满足不同场景需求。
- **Promise 支持**：提供基于 Promise 的现代 API，简化异步代码。
- **跨平台兼容**：自动处理不同操作系统的路径和权限差异。
- **流式处理**：支持大文件的流式读写，避免内存溢出。
- **文件监听**：支持监听文件变化，实现热重载等功能。

## 3. 模块导入方式

### CommonJS 方式

```ts
const fs = require('node:fs');
const fsPromises = require('node:fs/promises');
```

### ES Modules 方式

```ts
import fs from 'node:fs';
import fsPromises from 'node:fs/promises';
```

## 4. API 类型说明

fs 模块提供三种类型的 API：

| API 类型     | 命名规则             | 示例                           | 说明                                     |
|:-------------|:---------------------|:-------------------------------|:-----------------------------------------|
| **异步回调** | 无后缀               | `fs.readFile()`                | 使用回调函数处理结果。                   |
| **同步**     | `Sync` 后缀          | `fs.readFileSync()`            | 阻塞执行，返回结果。                     |
| **Promise**  | `fs/promises` 模块   | `fsPromises.readFile()`        | 返回 Promise，支持 async/await。         |

## 5. 参数说明：文件操作通用参数

大多数文件操作 API 接受以下通用参数：

| 参数名       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **path**     | String   | 文件或目录的路径。                       | `'./data.txt'`                 |
| **options**  | Object   | 操作选项（编码、标志等）。               | `{ encoding: 'utf8' }`          |
| **callback** | Function | 回调函数（异步 API）。                   | `(err, data) => {}`            |

## 6. 返回值与状态说明

不同 API 类型的返回值：

| API 类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **异步回调** | `undefined`  | 通过回调函数返回结果。                   |
| **同步**     | 直接返回值   | 返回操作结果或抛出异常。                 |
| **Promise**  | `Promise<T>` | 返回 Promise，resolve 时返回结果。        |

## 7. 代码示例：文件读取对比

以下示例对比了三种文件读取方式：

### 异步回调方式

```ts
// 文件: read-callback.ts
// 功能: 使用回调方式读取文件

import fs from 'node:fs';

fs.readFile('./data.txt', 'utf8', (err, data) => {
    if (err) {
        console.error('Error:', err);
        return;
    }
    console.log('Content:', data);
});
```

### 同步方式

```ts
// 文件: read-sync.ts
// 功能: 使用同步方式读取文件

import fs from 'node:fs';

try {
    const data = fs.readFileSync('./data.txt', 'utf8');
    console.log('Content:', data);
} catch (err) {
    console.error('Error:', err);
}
```

### Promise 方式

```ts
// 文件: read-promise.ts
// 功能: 使用 Promise 方式读取文件

import fsPromises from 'node:fs/promises';

async function readFile() {
    try {
        const data = await fsPromises.readFile('./data.txt', 'utf8');
        console.log('Content:', data);
    } catch (err) {
        console.error('Error:', err);
    }
}

readFile();
```

## 8. 输出结果说明

三种方式的输出结果相同：

```text
Content: Hello, Node.js!
```

**逻辑解析**：
- **异步回调**：非阻塞，通过回调处理结果
- **同步**：阻塞执行，直接返回结果
- **Promise**：非阻塞，使用 async/await 处理结果

## 9. 使用场景

### 1. 配置文件读取

读取应用配置文件：

```ts
// 读取 JSON 配置文件
import fsPromises from 'node:fs/promises';

async function loadConfig() {
    const configText = await fsPromises.readFile('./config.json', 'utf8');
    return JSON.parse(configText);
}
```

### 2. 日志文件写入

写入应用日志：

```ts
// 追加日志到文件
import fsPromises from 'node:fs/promises';

async function writeLog(message: string) {
    const logEntry = `${new Date().toISOString()} - ${message}\n`;
    await fsPromises.appendFile('./app.log', logEntry, 'utf8');
}
```

### 3. 文件复制

复制文件：

```ts
// 复制文件
import fsPromises from 'node:fs/promises';

async function copyFile(source: string, dest: string) {
    await fsPromises.copyFile(source, dest);
    console.log('File copied successfully');
}
```

## 10. 注意事项与常见错误

- **路径处理**：使用 `path` 模块处理路径，确保跨平台兼容
- **错误处理**：始终处理文件操作的错误，文件可能不存在或权限不足
- **同步 API 慎用**：同步 API 会阻塞事件循环，仅在启动阶段使用
- **大文件处理**：处理大文件时使用流式 API，避免内存溢出
- **权限问题**：注意文件权限，确保有读写权限

## 11. 常见问题 (FAQ)

**Q: 什么时候使用同步 API？**
A: 仅在应用启动阶段读取配置文件等场景使用。运行时应使用异步 API，避免阻塞事件循环。

**Q: Promise 版本和回调版本有什么区别？**
A: Promise 版本使用 `async/await` 语法更简洁，回调版本需要嵌套回调。推荐使用 Promise 版本。

**Q: 如何判断文件是否存在？**
A: 使用 `fsPromises.access()` 或 `fs.existsSync()`（已废弃，不推荐）。更好的方式是尝试读取文件并处理错误。

## 12. 最佳实践

- **优先使用 Promise API**：使用 `fs/promises` 模块，代码更简洁
- **避免同步 API**：运行时避免使用同步 API，保持事件循环畅通
- **错误处理**：始终处理文件操作的错误
- **路径处理**：使用 `path` 模块处理路径，确保跨平台兼容
- **流式处理**：处理大文件时使用流式 API

## 13. 对比分析：同步 vs 异步 vs Promise

| 维度             | 同步 API                                    | 异步回调 API                                | Promise API                                  |
|:-----------------|:--------------------------------------------|:--------------------------------------------|:---------------------------------------------|
| **执行方式**     | 阻塞执行                                    | 非阻塞执行                                  | 非阻塞执行                                    |
| **语法**         | 直接返回值                                   | 回调函数                                    | async/await                                   |
| **错误处理**     | try/catch                                   | 回调第一个参数                              | try/catch                                     |
| **性能影响**     | 阻塞事件循环                                | 不阻塞事件循环                              | 不阻塞事件循环                                |
| **适用场景**     | 启动阶段配置读取                            | 传统异步代码                                | 现代异步代码（推荐）                         |

## 14. 练习任务

1. **文件读取实践**：
   - 使用三种方式读取文件
   - 对比三种方式的差异
   - 理解异步操作的优势

2. **文件写入实践**：
   - 创建文件并写入内容
   - 追加内容到文件
   - 理解文件写入的不同模式

3. **错误处理实践**：
   - 处理文件不存在的错误
   - 处理权限不足的错误
   - 实现健壮的文件操作

4. **路径处理实践**：
   - 使用 `path` 模块处理文件路径
   - 实现跨平台兼容的路径处理
   - 理解路径处理的重要性

5. **实际应用**：
   - 实现配置文件读取功能
   - 实现日志文件写入功能
   - 在实际项目中应用文件系统操作

完成以上练习后，继续学习下一节：文件读写（同步与异步）。

## 总结

文件系统模块是 Node.js 的核心能力：

- **三种 API**：同步、异步回调、Promise
- **功能丰富**：文件读写、目录操作、文件监听
- **最佳实践**：优先使用 Promise API，避免同步 API
- **错误处理**：始终处理文件操作的错误

掌握文件系统模块有助于构建功能完整的后端应用。

---

**最后更新**：2025-01-XX
