# 2.2.4 目录操作

## 1. 概述

目录操作是文件系统操作的重要组成部分，包括目录的创建、删除、遍历、重命名等操作。Node.js 的 fs 模块提供了完整的目录操作 API，支持同步和异步两种方式，以及基于 Promise 的现代 API。

## 2. 特性说明

- **目录创建**：支持创建单个目录和递归创建多级目录。
- **目录删除**：支持删除空目录和递归删除非空目录。
- **目录遍历**：支持读取目录内容、递归遍历目录树。
- **目录信息**：支持获取目录状态、权限等信息。
- **跨平台兼容**：自动处理不同操作系统的路径和权限差异。

## 3. 语法与定义

### 创建目录

```ts
// 创建目录（Promise）
fsPromises.mkdir(path: string, options?: object): Promise<void>

// 创建目录（同步）
fs.mkdirSync(path: string, options?: object): void
```

### 删除目录

```ts
// 删除目录（Promise）
fsPromises.rmdir(path: string, options?: object): Promise<void>

// 删除目录（同步）
fs.rmdirSync(path: string, options?: object): void

// 递归删除目录（Promise，Node.js 14.14+）
fsPromises.rm(path: string, options?: object): Promise<void>
```

### 读取目录

```ts
// 读取目录（Promise）
fsPromises.readdir(path: string, options?: object): Promise<string[] | Dirent[]>

// 读取目录（同步）
fs.readdirSync(path: string, options?: object): string[] | Dirent[]
```

## 4. 基本用法

### 示例 1：创建目录

```ts
// 文件: create-dir.ts
// 功能: 创建目录

import fsPromises from 'node:fs/promises';

async function createDirectory() {
    try {
        // 创建单个目录
        await fsPromises.mkdir('./new-dir');
        console.log('Directory created');
        
        // 递归创建多级目录
        await fsPromises.mkdir('./parent/child/grandchild', { recursive: true });
        console.log('Nested directories created');
    } catch (err) {
        console.error('Error creating directory:', err);
    }
}

createDirectory();
```

### 示例 2：删除目录

```ts
// 文件: delete-dir.ts
// 功能: 删除目录

import fsPromises from 'node:fs/promises';

async function deleteDirectory() {
    try {
        // 删除空目录
        await fsPromises.rmdir('./empty-dir');
        console.log('Directory deleted');
        
        // 递归删除非空目录（Node.js 14.14+）
        await fsPromises.rm('./non-empty-dir', { recursive: true, force: true });
        console.log('Directory and contents deleted');
    } catch (err) {
        console.error('Error deleting directory:', err);
    }
}

deleteDirectory();
```

### 示例 3：读取目录

```ts
// 文件: read-dir.ts
// 功能: 读取目录内容

import fsPromises from 'node:fs/promises';

async function readDirectory() {
    try {
        // 读取目录内容（文件名）
        const files = await fsPromises.readdir('./src');
        console.log('Files:', files);
        
        // 读取目录内容（包含详细信息）
        const entries = await fsPromises.readdir('./src', { withFileTypes: true });
        for (const entry of entries) {
            if (entry.isFile()) {
                console.log(`File: ${entry.name}`);
            } else if (entry.isDirectory()) {
                console.log(`Directory: ${entry.name}`);
            }
        }
    } catch (err) {
        console.error('Error reading directory:', err);
    }
}

readDirectory();
```

## 5. 参数说明：目录操作参数

### mkdir 参数

| 参数名       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **path**     | String   | 目录路径。                               | `'./new-dir'`                  |
| **options**  | Object   | 选项对象。                               | `{ recursive: true }`          |
| **recursive**| Boolean  | 是否递归创建父目录。                     | `true`                         |
| **mode**     | Number   | 目录权限（八进制）。                     | `0o755`                        |

### readdir 参数

| 参数名           | 类型     | 说明                                     | 示例                           |
|:-----------------|:---------|:-----------------------------------------|:-------------------------------|
| **path**         | String   | 目录路径。                               | `'./src'`                      |
| **options**      | Object   | 选项对象。                               | `{ withFileTypes: true }`      |
| **withFileTypes**| Boolean  | 是否返回 Dirent 对象而非字符串。         | `true`                         |
| **encoding**     | String   | 文件名编码。                             | `'utf8'`                       |

## 6. 返回值与状态说明

### mkdir 返回值

| API 类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **Promise**  | `Promise<void>`| 创建成功时 resolve。                    |
| **同步**     | `void`       | 创建成功返回 undefined。                |

### readdir 返回值

| API 类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **Promise**  | `Promise<string[]/Dirent[]>`| 返回目录内容数组。                      |
| **同步**     | `string[]/Dirent[]`| 返回目录内容数组。                      |

## 7. 代码示例：递归遍历目录

以下示例演示了如何递归遍历目录树：

```ts
// 文件: traverse-dir.ts
// 功能: 递归遍历目录

import fsPromises from 'node:fs/promises';
import path from 'node:path';

async function traverseDirectory(dirPath: string): Promise<void> {
    try {
        const entries = await fsPromises.readdir(dirPath, { withFileTypes: true });
        
        for (const entry of entries) {
            const fullPath = path.join(dirPath, entry.name);
            
            if (entry.isDirectory()) {
                console.log(`Directory: ${fullPath}`);
                await traverseDirectory(fullPath); // 递归遍历
            } else if (entry.isFile()) {
                console.log(`File: ${fullPath}`);
            }
        }
    } catch (err) {
        console.error('Error traversing directory:', err);
    }
}

traverseDirectory('./src');
```

## 8. 输出结果说明

目录遍历的输出结果：

```text
Directory: ./src
File: ./src/index.ts
Directory: ./src/utils
File: ./src/utils/helper.ts
File: ./src/utils/validator.ts
```

**逻辑解析**：
- 递归遍历目录树
- 区分文件和目录
- 输出完整的文件路径

## 9. 使用场景

### 1. 项目初始化

创建项目目录结构：

```ts
// 创建项目目录结构
import fsPromises from 'node:fs/promises';

async function initProject() {
    const dirs = ['src', 'tests', 'docs', 'dist'];
    for (const dir of dirs) {
        await fsPromises.mkdir(dir, { recursive: true });
    }
}
```

### 2. 文件清理

清理临时文件和目录：

```ts
// 清理临时目录
import fsPromises from 'node:fs/promises';

async function cleanTemp() {
    await fsPromises.rm('./temp', { recursive: true, force: true });
    console.log('Temp directory cleaned');
}
```

### 3. 文件统计

统计目录中的文件数量：

```ts
// 统计文件数量
import fsPromises from 'node:fs/promises';

async function countFiles(dirPath: string): Promise<number> {
    const entries = await fsPromises.readdir(dirPath, { withFileTypes: true });
    let count = 0;
    
    for (const entry of entries) {
        if (entry.isFile()) {
            count++;
        } else if (entry.isDirectory()) {
            count += await countFiles(path.join(dirPath, entry.name));
        }
    }
    
    return count;
}
```

## 10. 注意事项与常见错误

- **递归创建**：创建多级目录时使用 `{ recursive: true }`
- **递归删除**：删除非空目录时使用 `fsPromises.rm()` 而非 `rmdir()`
- **路径处理**：使用 `path` 模块处理路径，确保跨平台兼容
- **权限问题**：确保有目录创建和删除权限
- **目录存在**：创建目录前检查目录是否已存在，避免错误

## 11. 常见问题 (FAQ)

**Q: 如何检查目录是否存在？**
A: 使用 `fsPromises.access()` 或 `fs.existsSync()`（已废弃）。更好的方式是尝试操作并处理错误。

**Q: 如何删除非空目录？**
A: 使用 `fsPromises.rm(path, { recursive: true, force: true })`（Node.js 14.14+）。

**Q: readdir 返回的是什么？**
A: 默认返回文件名数组。使用 `{ withFileTypes: true }` 返回 Dirent 对象数组，包含更多信息。

## 12. 最佳实践

- **使用 Promise API**：优先使用 `fs/promises` 模块
- **递归选项**：创建多级目录时使用 `recursive: true`
- **路径处理**：使用 `path` 模块处理路径
- **错误处理**：始终处理目录操作的错误
- **权限管理**：注意目录权限，确保有操作权限

## 13. 对比分析：mkdir vs mkdirSync

| 维度             | mkdir (异步)                                | mkdirSync (同步)                            |
|:-----------------|:--------------------------------------------|:--------------------------------------------|
| **执行方式**     | 非阻塞执行                                  | 阻塞执行                                    |
| **性能影响**     | 不阻塞事件循环                              | 阻塞事件循环                                |
| **错误处理**     | Promise 或回调                              | try/catch                                   |
| **适用场景**     | 运行时目录操作（推荐）                     | 启动阶段目录创建                            |

## 14. 练习任务

1. **目录创建实践**：
   - 创建单个目录和多级目录
   - 理解递归创建的作用
   - 处理目录已存在的情况

2. **目录删除实践**：
   - 删除空目录和非空目录
   - 理解递归删除的作用
   - 处理目录不存在的情况

3. **目录遍历实践**：
   - 读取目录内容
   - 递归遍历目录树
   - 实现文件统计功能

4. **路径处理实践**：
   - 使用 `path` 模块处理目录路径
   - 实现跨平台兼容的路径处理
   - 理解路径处理的重要性

5. **实际应用**：
   - 实现项目初始化功能
   - 实现文件清理功能
   - 在实际项目中应用目录操作

完成以上练习后，继续学习下一节：文件监听（watch）。

## 总结

目录操作是文件系统操作的重要组成部分：

- **创建删除**：支持创建和删除目录（包括递归操作）
- **目录遍历**：支持读取和遍历目录内容
- **最佳实践**：使用 Promise API，处理错误，使用路径模块

掌握目录操作有助于构建功能完整的文件管理系统。

---

**最后更新**：2025-01-XX
