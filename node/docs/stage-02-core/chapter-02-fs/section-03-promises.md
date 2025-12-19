# 2.2.3 Promise 版本（fs/promises）

## 1. 概述

`fs/promises` 模块提供了基于 Promise 的文件系统 API，是现代 Node.js 开发的首选方式。它提供了与回调版本相同的功能，但使用 Promise 和 async/await 语法，使代码更简洁、更易读。在 Node.js 22+ 环境下，Promise 版本的 API 已经非常成熟和稳定。

## 2. 特性说明

- **Promise 支持**：所有 API 都返回 Promise，支持 async/await 语法。
- **代码简洁**：使用 async/await 语法，避免回调地狱。
- **错误处理**：使用 try/catch 处理错误，更符合现代 JavaScript 习惯。
- **类型安全**：与 TypeScript 完美集成，提供完整的类型定义。
- **功能完整**：提供与回调版本相同的所有功能。

## 3. 语法与定义

### 模块导入

```ts
// ES Modules
import fsPromises from 'node:fs/promises';

// CommonJS
const fsPromises = require('node:fs/promises');
```

### 常用 API

```ts
// 读取文件
fsPromises.readFile(path: string, options?: string | object): Promise<Buffer | string>

// 写入文件
fsPromises.writeFile(path: string, data: string | Buffer, options?: object): Promise<void>

// 追加文件
fsPromises.appendFile(path: string, data: string | Buffer, options?: object): Promise<void>

// 复制文件
fsPromises.copyFile(src: string, dest: string, flags?: number): Promise<void>

// 删除文件
fsPromises.unlink(path: string): Promise<void>

// 重命名文件
fsPromises.rename(oldPath: string, newPath: string): Promise<void>
```

## 4. 基本用法

### 示例 1：读取文件

```ts
// 文件: read-promise.ts
// 功能: 使用 Promise 读取文件

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

### 示例 2：写入文件

```ts
// 文件: write-promise.ts
// 功能: 使用 Promise 写入文件

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

### 示例 3：文件操作组合

```ts
// 文件: file-operations.ts
// 功能: 组合多个文件操作

import fsPromises from 'node:fs/promises';

async function processFile() {
    try {
        // 1. 读取文件
        const content = await fsPromises.readFile('./input.txt', 'utf8');
        
        // 2. 处理内容
        const processed = content.toUpperCase();
        
        // 3. 写入文件
        await fsPromises.writeFile('./output.txt', processed, 'utf8');
        
        // 4. 复制文件
        await fsPromises.copyFile('./output.txt', './backup.txt');
        
        console.log('File processed successfully');
    } catch (err) {
        console.error('Error processing file:', err);
    }
}

processFile();
```

## 5. 参数说明：Promise API 参数

Promise 版本的 API 参数与回调版本相同，但不包含回调函数：

| API 名称      | 参数说明                                     | 示例                           |
|:--------------|:---------------------------------------------|:-------------------------------|
| **readFile**  | `(path, options?)`                          | `readFile('./data.txt', 'utf8')`|
| **writeFile** | `(path, data, options?)`                     | `writeFile('./out.txt', 'data', 'utf8')`|
| **appendFile**| `(path, data, options?)`                     | `appendFile('./log.txt', 'entry', 'utf8')`|
| **copyFile**  | `(src, dest, flags?)`                       | `copyFile('./src.txt', './dest.txt')`|
| **unlink**    | `(path)`                                     | `unlink('./file.txt')`         |
| **rename**    | `(oldPath, newPath)`                         | `rename('./old.txt', './new.txt')`|

## 6. 返回值与状态说明

所有 Promise API 都返回 Promise：

| API 名称      | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **readFile** | `Promise<Buffer/string>`| 读取成功时返回文件内容。                 |
| **writeFile**| `Promise<void>`| 写入成功时 resolve。                    |
| **appendFile**| `Promise<void>`| 追加成功时 resolve。                    |
| **copyFile** | `Promise<void>`| 复制成功时 resolve。                    |
| **unlink**   | `Promise<void>`| 删除成功时 resolve。                    |
| **rename**   | `Promise<void>`| 重命名成功时 resolve。                  |

## 7. 代码示例：并发文件操作

Promise API 支持并发操作：

```ts
// 文件: concurrent-operations.ts
// 功能: 并发执行多个文件操作

import fsPromises from 'node:fs/promises';

async function concurrentOperations() {
    try {
        // 并发读取多个文件
        const [file1, file2, file3] = await Promise.all([
            fsPromises.readFile('./file1.txt', 'utf8'),
            fsPromises.readFile('./file2.txt', 'utf8'),
            fsPromises.readFile('./file3.txt', 'utf8')
        ]);
        
        console.log('File 1:', file1);
        console.log('File 2:', file2);
        console.log('File 3:', file3);
    } catch (err) {
        console.error('Error reading files:', err);
    }
}

concurrentOperations();
```

## 8. 输出结果说明

并发操作的输出结果：

```text
File 1: Content 1
File 2: Content 2
File 3: Content 3
```

**逻辑解析**：
- `Promise.all()` 并发执行多个文件操作
- 所有操作完成后返回结果数组
- 任何一个操作失败，整个 Promise.all 会 reject

## 9. 使用场景

### 1. 配置文件管理

读取和更新配置文件：

```ts
// 配置文件管理
import fsPromises from 'node:fs/promises';

async function updateConfig(key: string, value: any) {
    const config = JSON.parse(
        await fsPromises.readFile('./config.json', 'utf8')
    );
    config[key] = value;
    await fsPromises.writeFile('./config.json', JSON.stringify(config, null, 2), 'utf8');
}
```

### 2. 日志系统

实现日志系统：

```ts
// 日志系统
import fsPromises from 'node:fs/promises';

async function log(level: string, message: string) {
    const logEntry = `${new Date().toISOString()} [${level}] ${message}\n`;
    await fsPromises.appendFile('./app.log', logEntry, 'utf8');
}
```

### 3. 文件备份

实现文件备份功能：

```ts
// 文件备份
import fsPromises from 'node:fs/promises';

async function backupFile(filePath: string) {
    const backupPath = `${filePath}.backup`;
    await fsPromises.copyFile(filePath, backupPath);
    console.log(`File backed up to ${backupPath}`);
}
```

## 10. 注意事项与常见错误

- **错误处理**：始终使用 try/catch 处理 Promise 错误
- **路径处理**：使用 `path` 模块处理路径，确保跨平台兼容
- **并发控制**：大量并发文件操作时注意系统资源限制
- **权限问题**：确保有文件读写权限
- **文件锁定**：注意文件锁定问题，避免并发写入冲突

## 11. 常见问题 (FAQ)

**Q: Promise API 和回调 API 有什么区别？**
A: Promise API 使用 async/await 语法更简洁，错误处理更统一。功能完全相同，只是语法不同。

**Q: 可以混用 Promise API 和回调 API 吗？**
A: 可以，但不推荐。建议在同一项目中统一使用一种 API。

**Q: Promise API 的性能如何？**
A: 性能与回调 API 相同，只是语法更现代。

## 12. 最佳实践

- **优先使用 Promise API**：新项目优先使用 Promise API
- **统一 API 风格**：在同一项目中统一使用 Promise API
- **错误处理**：使用 try/catch 处理所有文件操作错误
- **并发操作**：使用 Promise.all 实现并发文件操作
- **路径处理**：使用 `path` 模块处理路径

## 13. 对比分析：回调 vs Promise

| 维度             | 回调 API                                    | Promise API                                  |
|:-----------------|:--------------------------------------------|:---------------------------------------------|
| **语法**         | 回调函数                                    | async/await                                  |
| **错误处理**     | 回调第一个参数                              | try/catch                                    |
| **代码可读性**   | 回调嵌套，可读性较差                        | 线性代码，可读性好                            |
| **并发处理**     | 需要手动管理                                | 使用 Promise.all 等工具                     |
| **类型安全**     | 需要额外配置                                | 与 TypeScript 完美集成                       |

## 14. 练习任务

1. **Promise API 实践**：
   - 使用 Promise API 读取和写入文件
   - 对比 Promise API 和回调 API 的差异
   - 理解 Promise API 的优势

2. **错误处理实践**：
   - 使用 try/catch 处理文件操作错误
   - 实现健壮的文件操作函数
   - 理解错误处理的重要性

3. **并发操作实践**：
   - 使用 Promise.all 并发读取多个文件
   - 实现文件批量处理功能
   - 理解并发操作的优势

4. **实际应用**：
   - 实现配置文件管理功能
   - 实现日志系统
   - 在实际项目中应用 Promise API

5. **性能优化**：
   - 优化文件操作的性能
   - 实现文件操作缓存
   - 理解性能优化的方法

完成以上练习后，继续学习下一节：目录操作。

## 总结

Promise 版本的文件系统 API 是现代 Node.js 开发的首选：

- **语法简洁**：使用 async/await 语法，代码更易读
- **错误处理**：使用 try/catch 处理错误，更符合现代习惯
- **功能完整**：提供与回调版本相同的所有功能
- **最佳实践**：优先使用 Promise API，统一 API 风格

掌握 Promise API 有助于编写现代化的 Node.js 代码。

---

**最后更新**：2025-01-XX
