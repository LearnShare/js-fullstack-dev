# 2.9.2 promisify 与回调转换

## 1. 概述

`promisify` 是 util 模块中最常用的工具函数之一，用于将遵循 Node.js 回调约定（错误优先）的回调函数转换为返回 Promise 的函数。这对于将旧的回调式 API 转换为现代的 Promise/async-await 风格非常有用。

## 2. 特性说明

- **回调转换**：将回调函数转换为 Promise。
- **错误优先**：只适用于遵循错误优先约定的回调函数。
- **自动处理**：自动处理错误和成功情况。
- **类型安全**：与 TypeScript 配合使用，提供类型安全。
- **自定义支持**：支持自定义 Promise 转换逻辑。

## 3. 语法与定义

### promisify 函数

```ts
// 基本用法
util.promisify(original: Function): Function

// 自定义 Promise
util.promisify.custom: symbol
```

## 4. 基本用法

### 示例 1：基本 promisify

```ts
// 文件: util-promisify-basic.ts
// 功能: 基本 promisify 使用

import util from 'node:util';
import fs from 'node:fs';

// 转换回调函数为 Promise
const readFile = util.promisify(fs.readFile);
const writeFile = util.promisify(fs.writeFile);

// 使用 async/await
async function fileOperations() {
    try {
        const data = await readFile('./input.txt', 'utf8');
        await writeFile('./output.txt', data.toUpperCase(), 'utf8');
        console.log('File processed successfully');
    } catch (error) {
        console.error('Error:', error);
    }
}

fileOperations();
```

### 示例 2：转换多个函数

```ts
// 文件: util-promisify-multiple.ts
// 功能: 转换多个函数

import util from 'node:util';
import fs from 'node:fs';

// 批量转换
const fsPromises = {
    readFile: util.promisify(fs.readFile),
    writeFile: util.promisify(fs.writeFile),
    readdir: util.promisify(fs.readdir),
    stat: util.promisify(fs.stat)
};

// 使用
async function processFiles() {
    const files = await fsPromises.readdir('./src');
    for (const file of files) {
        const stats = await fsPromises.stat(`./src/${file}`);
        console.log(`${file}: ${stats.size} bytes`);
    }
}

processFiles();
```

### 示例 3：自定义 promisify

```ts
// 文件: util-promisify-custom.ts
// 功能: 自定义 promisify

import util from 'node:util';

// 不遵循标准约定的函数
function customCallback(data: string, callback: (result: string) => void) {
    setTimeout(() => {
        callback(`Processed: ${data}`);
    }, 1000);
}

// 自定义转换
function promisifyCustom<T extends (...args: any[]) => void>(
    fn: T
): (...args: Parameters<T> extends [...infer A, infer C] ? A : never) => Promise<any> {
    return function(...args: any[]) {
        return new Promise((resolve, reject) => {
            fn(...args, (result: any) => {
                resolve(result);
            });
        });
    };
}

const customPromise = promisifyCustom(customCallback);

// 使用
async function useCustom() {
    const result = await customPromise('data');
    console.log(result);
}

useCustom();
```

## 5. 参数说明：promisify 参数

### promisify 参数

| 参数名       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **original** | Function | 要转换的回调函数（必须遵循错误优先约定） | `fs.readFile`                  |

## 6. 返回值与状态说明

promisify 操作的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **promisify**| Function     | 返回 Promise 版本的函数                  |

## 7. 代码示例：完整的 promisify 应用

以下示例演示了 promisify 的完整应用：

```ts
// 文件: util-promisify-complete.ts
// 功能: 完整的 promisify 应用

import util from 'node:util';
import fs from 'node:fs';
import crypto from 'node:crypto';

// 转换多个函数
const fsAsync = {
    readFile: util.promisify(fs.readFile),
    writeFile: util.promisify(fs.writeFile),
    readdir: util.promisify(fs.readdir),
    stat: util.promisify(fs.stat)
};

const cryptoAsync = {
    randomBytes: util.promisify(crypto.randomBytes),
    pbkdf2: util.promisify(crypto.pbkdf2)
};

// 使用转换后的函数
async function processData() {
    try {
        // 读取文件
        const data = await fsAsync.readFile('./data.txt', 'utf8');
        
        // 生成随机盐值
        const salt = await cryptoAsync.randomBytes(16);
        
        // 哈希密码
        const hash = await cryptoAsync.pbkdf2('password', salt, 10000, 64, 'sha512');
        
        // 写入结果
        await fsAsync.writeFile('./result.txt', hash.toString('hex'), 'utf8');
        
        console.log('Processing completed');
    } catch (error) {
        console.error('Error:', error);
    }
}

processData();
```

## 8. 输出结果说明

promisify 应用的输出结果：

```text
Processing completed
```

**逻辑解析**：
- 所有回调函数都转换为 Promise
- 使用 async/await 处理异步操作
- 错误通过 try/catch 统一处理

## 9. 使用场景

### 1. 文件操作转换

转换文件操作的回调 API：

```ts
// 文件操作转换示例
import util from 'node:util';
import fs from 'node:fs';

const readFile = util.promisify(fs.readFile);
const writeFile = util.promisify(fs.writeFile);

async function copyFile(source: string, dest: string) {
    const data = await readFile(source);
    await writeFile(dest, data);
}
```

### 2. 数据库操作转换

转换数据库操作的回调 API：

```ts
// 数据库操作转换示例
import util from 'node:util';

class Database {
    query(sql: string, callback: (error: Error | null, results: any) => void) {
        // 数据库查询逻辑
    }
}

const db = new Database();
const queryAsync = util.promisify(db.query.bind(db));

async function getUsers() {
    const results = await queryAsync('SELECT * FROM users');
    return results;
}
```

### 3. 第三方库转换

转换第三方库的回调 API：

```ts
// 第三方库转换示例
import util from 'node:util';
import someLibrary from 'some-library';

const libraryAsync = {
    method1: util.promisify(someLibrary.method1),
    method2: util.promisify(someLibrary.method2)
};
```

## 10. 注意事项与常见错误

- **回调约定**：只适用于遵循错误优先约定的函数
- **this 绑定**：注意函数的 this 绑定，可能需要使用 `bind()`
- **参数顺序**：回调必须是最后一个参数
- **错误处理**：Promise 版本的错误通过 reject 传递
- **现代替代**：优先使用原生 Promise API（如 `fs/promises`）

## 11. 常见问题 (FAQ)

**Q: promisify 适用于所有回调函数吗？**
A: 不，只适用于遵循 Node.js 回调约定（错误优先，回调是最后一个参数）的函数。

**Q: 如何处理 this 绑定问题？**
A: 使用 `bind()` 绑定 this，如 `util.promisify(obj.method.bind(obj))`。

**Q: 为什么不直接使用 fs/promises？**
A: `fs/promises` 是更好的选择，但 promisify 适用于其他回调式 API。

## 12. 最佳实践

- **优先使用原生 Promise API**：如 `fs/promises` 而非 `promisify(fs.readFile)`
- **this 绑定**：注意函数的 this 绑定
- **错误处理**：使用 try/catch 处理 Promise 错误
- **类型安全**：与 TypeScript 配合使用，提供类型定义
- **代码简化**：使用 promisify 简化回调代码

## 13. 对比分析：promisify vs 原生 Promise API

| 维度             | promisify                                  | 原生 Promise API（如 fs/promises）        |
|:-----------------|:------------------------------------------|:------------------------------------------|
| **适用场景**     | 转换回调式 API                             | 原生支持 Promise 的 API                   |
| **性能**         | 有转换开销                                 | 无转换开销                                 |
| **类型支持**     | 需要手动定义类型                           | 更好的类型支持                             |
| **推荐使用**     | 转换旧 API 时使用                          | 新 API 优先使用原生 Promise               |

## 14. 练习任务

1. **promisify 实践**：
   - 转换不同的回调函数
   - 理解 promisify 的限制
   - 处理 this 绑定问题

2. **批量转换实践**：
   - 批量转换多个函数
   - 创建 Promise 版本的模块
   - 实现工具函数封装

3. **实际应用**：
   - 在实际项目中应用 promisify
   - 转换旧的回调式 API
   - 简化异步代码

完成以上练习后，继续学习下一节：类型检查与调试工具。

## 总结

promisify 是转换回调函数为 Promise 的工具：

- **核心功能**：将回调函数转换为 Promise
- **适用场景**：转换遵循错误优先约定的回调函数
- **最佳实践**：优先使用原生 Promise API，注意 this 绑定

掌握 promisify 有助于将旧代码转换为现代 Promise 风格。

---

**最后更新**：2025-01-XX
