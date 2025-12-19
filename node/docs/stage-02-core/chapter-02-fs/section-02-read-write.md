# 2.2.2 文件读写（同步与异步）

## 1. 概述

文件读写是文件系统操作的基础。Node.js 提供了同步和异步两种文件读写方式，每种方式都有其适用场景。理解同步与异步 API 的区别，以及如何正确使用它们，是掌握文件系统操作的关键。

## 2. 特性说明

- **异步非阻塞**：异步 API 不阻塞事件循环，适合高并发场景。
- **同步阻塞**：同步 API 阻塞执行，仅在特定场景使用。
- **多种编码**：支持 UTF-8、ASCII、Buffer 等多种编码格式。
- **文件标志**：支持多种文件打开标志（读、写、追加等）。
- **错误处理**：提供完善的错误处理机制。

## 3. 语法与定义

### 异步读取文件

```ts
// 异步读取文件（回调方式）
fs.readFile(path: string, options: string | object, callback: Function): void

// 异步读取文件（Promise 方式）
fsPromises.readFile(path: string, options?: string | object): Promise<Buffer | string>
```

### 同步读取文件

```ts
// 同步读取文件
fs.readFileSync(path: string, options?: string | object): Buffer | string
```

### 异步写入文件

```ts
// 异步写入文件（回调方式）
fs.writeFile(path: string, data: string | Buffer, options: object, callback: Function): void

// 异步写入文件（Promise 方式）
fsPromises.writeFile(path: string, data: string | Buffer, options?: object): Promise<void>
```

### 同步写入文件

```ts
// 同步写入文件
fs.writeFileSync(path: string, data: string | Buffer, options?: object): void
```

## 4. 基本用法

### 示例 1：异步读取文件

```ts
// 文件: read-async.ts
// 功能: 异步读取文件

import fs from 'node:fs';

// 回调方式
fs.readFile('./data.txt', 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading file:', err);
        return;
    }
    console.log('File content:', data);
});

// Promise 方式
import fsPromises from 'node:fs/promises';

async function readFile() {
    try {
        const data = await fsPromises.readFile('./data.txt', 'utf8');
        console.log('File content:', data);
    } catch (err) {
        console.error('Error reading file:', err);
    }
}

readFile();
```

### 示例 2：同步读取文件

```ts
// 文件: read-sync.ts
// 功能: 同步读取文件

import fs from 'node:fs';

try {
    const data = fs.readFileSync('./data.txt', 'utf8');
    console.log('File content:', data);
} catch (err) {
    console.error('Error reading file:', err);
}
```

### 示例 3：异步写入文件

```ts
// 文件: write-async.ts
// 功能: 异步写入文件

import fsPromises from 'node:fs/promises';

async function writeFile() {
    try {
        await fsPromises.writeFile('./output.txt', 'Hello, Node.js!', 'utf8');
        console.log('File written successfully');
    } catch (err) {
        console.error('Error writing file:', err);
    }
}

writeFile();
```

### 示例 4：同步写入文件

```ts
// 文件: write-sync.ts
// 功能: 同步写入文件

import fs from 'node:fs';

try {
    fs.writeFileSync('./output.txt', 'Hello, Node.js!', 'utf8');
    console.log('File written successfully');
} catch (err) {
    console.error('Error writing file:', err);
}
```

## 5. 参数说明：readFile 和 writeFile

### readFile 参数

| 参数名       | 类型           | 说明                                     | 示例                           |
|:-------------|:---------------|:-----------------------------------------|:-------------------------------|
| **path**     | String         | 文件路径。                               | `'./data.txt'`                 |
| **options**  | String/Object  | 编码或选项对象。                         | `'utf8'` 或 `{ encoding: 'utf8' }`|
| **callback** | Function       | 回调函数（异步回调方式）。               | `(err, data) => {}`            |

### writeFile 参数

| 参数名       | 类型           | 说明                                     | 示例                           |
|:-------------|:---------------|:-----------------------------------------|:-------------------------------|
| **path**     | String         | 文件路径。                               | `'./output.txt'`               |
| **data**     | String/Buffer  | 要写入的数据。                           | `'Hello'` 或 `Buffer.from('Hello')`|
| **options**  | String/Object  | 编码或选项对象。                         | `'utf8'` 或 `{ encoding: 'utf8', flag: 'w' }`|
| **callback** | Function       | 回调函数（异步回调方式）。               | `(err) => {}`                  |

## 6. 返回值与状态说明

### readFile 返回值

| API 类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **异步回调** | `undefined`  | 通过回调函数返回数据。                   |
| **同步**     | `Buffer/string`| 返回文件内容。                         |
| **Promise**  | `Promise<Buffer/string>`| 返回 Promise，resolve 时返回文件内容。|

### writeFile 返回值

| API 类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **异步回调** | `undefined`  | 通过回调函数返回结果。                   |
| **同步**     | `undefined`  | 写入成功返回 undefined。                 |
| **Promise**  | `Promise<void>`| 返回 Promise，写入成功时 resolve。      |

## 7. 代码示例：文件操作选项

文件操作支持多种选项：

```ts
// 文件: file-options.ts
// 功能: 文件操作选项示例

import fsPromises from 'node:fs/promises';

async function fileOperations() {
    // 1. 读取文件（指定编码）
    const text = await fsPromises.readFile('./data.txt', { encoding: 'utf8' });
    
    // 2. 读取文件（Buffer）
    const buffer = await fsPromises.readFile('./data.txt');
    
    // 3. 写入文件（覆盖模式）
    await fsPromises.writeFile('./output.txt', 'Hello', { 
        encoding: 'utf8',
        flag: 'w' // 写入模式（覆盖）
    });
    
    // 4. 追加文件
    await fsPromises.writeFile('./output.txt', '\nWorld', { 
        encoding: 'utf8',
        flag: 'a' // 追加模式
    });
    
    // 5. 读取 JSON 文件
    const config = JSON.parse(
        await fsPromises.readFile('./config.json', 'utf8')
    );
}
```

## 8. 输出结果说明

文件操作的输出结果：

```text
File content: Hello, Node.js!
File written successfully
```

**逻辑解析**：
- 读取操作返回文件内容（字符串或 Buffer）
- 写入操作成功时不返回内容，失败时抛出错误
- 使用选项对象可以控制文件操作的详细行为

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
// 追加日志
import fsPromises from 'node:fs/promises';

async function log(message: string) {
    const logEntry = `${new Date().toISOString()} - ${message}\n`;
    await fsPromises.writeFile('./app.log', logEntry, { 
        encoding: 'utf8',
        flag: 'a' // 追加模式
    });
}
```

### 3. 数据持久化

将数据保存到文件：

```ts
// 保存数据到文件
import fsPromises from 'node:fs/promises';

async function saveData(data: object) {
    const json = JSON.stringify(data, null, 2);
    await fsPromises.writeFile('./data.json', json, 'utf8');
}
```

## 10. 注意事项与常见错误

- **编码问题**：明确指定文件编码，避免乱码
- **路径问题**：使用相对路径时注意当前工作目录
- **权限问题**：确保有文件读写权限
- **同步 API 慎用**：同步 API 会阻塞事件循环
- **错误处理**：始终处理文件操作的错误
- **文件覆盖**：写入文件会覆盖原有内容，注意数据安全

## 11. 常见问题 (FAQ)

**Q: 什么时候使用同步 API？**
A: 仅在应用启动阶段读取配置文件等场景使用。运行时应使用异步 API。

**Q: 如何追加内容到文件？**
A: 使用 `flag: 'a'` 选项，或使用 `fsPromises.appendFile()` 方法。

**Q: 如何读取二进制文件？**
A: 不指定编码或使用 `{ encoding: null }`，返回 Buffer 对象。

**Q: 写入文件会覆盖原有内容吗？**
A: 默认会覆盖。使用 `flag: 'a'` 可以追加内容。

## 12. 最佳实践

- **优先使用 Promise API**：使用 `fs/promises` 模块，代码更简洁
- **避免同步 API**：运行时避免使用同步 API
- **明确编码**：明确指定文件编码，避免乱码
- **错误处理**：始终处理文件操作的错误
- **路径处理**：使用 `path` 模块处理路径
- **大文件处理**：处理大文件时使用流式 API

## 13. 对比分析：同步 vs 异步

| 维度             | 同步 API                                    | 异步 API                                    |
|:-----------------|:--------------------------------------------|:--------------------------------------------|
| **执行方式**     | 阻塞执行                                    | 非阻塞执行                                  |
| **性能影响**     | 阻塞事件循环                                | 不阻塞事件循环                              |
| **错误处理**     | try/catch                                   | 回调或 Promise                               |
| **适用场景**     | 启动阶段配置读取                            | 运行时文件操作（推荐）                     |
| **代码复杂度**   | 简单                                        | 需要处理异步                                |

## 14. 练习任务

1. **文件读取实践**：
   - 使用异步和同步方式读取文件
   - 对比两种方式的差异
   - 理解异步操作的优势

2. **文件写入实践**：
   - 创建文件并写入内容
   - 追加内容到文件
   - 理解不同的写入模式

3. **编码处理实践**：
   - 读取不同编码的文件
   - 写入不同编码的文件
   - 理解编码的重要性

4. **错误处理实践**：
   - 处理文件不存在的错误
   - 处理权限不足的错误
   - 实现健壮的文件操作

5. **实际应用**：
   - 实现配置文件读取功能
   - 实现日志文件写入功能
   - 在实际项目中应用文件读写操作

完成以上练习后，继续学习下一节：Promise 版本（fs/promises）。

## 总结

文件读写是文件系统操作的基础：

- **两种方式**：同步和异步，各有适用场景
- **多种编码**：支持多种编码格式
- **错误处理**：完善的错误处理机制
- **最佳实践**：优先使用异步 API，明确编码，处理错误

掌握文件读写操作有助于构建功能完整的后端应用。

---

**最后更新**：2025-01-XX
