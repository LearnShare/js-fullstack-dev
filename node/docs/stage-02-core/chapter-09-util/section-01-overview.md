# 2.9.1 util 模块概述

## 1. 概述

util 模块提供了 Node.js 中常用的工具函数，包括回调函数转 Promise、类型检查、调试工具、格式化输出等。这些工具函数可以简化代码，提高开发效率。虽然许多功能在现代 JavaScript 中已有替代方案，但理解 util 模块的使用仍然很有价值。

## 2. 特性说明

- **回调转换**：将回调式函数转换为 Promise。
- **类型检查**：提供类型检查工具函数。
- **调试工具**：提供调试和格式化工具。
- **继承工具**：提供继承相关的工具函数。
- **格式化输出**：提供格式化输出的工具。

## 3. 模块导入方式

### ES Modules 方式

```ts
import util from 'node:util';
```

### CommonJS 方式

```ts
const util = require('node:util');
```

## 4. 主要功能概览

| 功能类别     | 主要函数                                     | 用途                           |
|:-------------|:---------------------------------------------|:-------------------------------|
| **Promise 转换**| `promisify()`, `promisify.custom`            | 回调函数转 Promise             |
| **类型检查** | `types.isDate()`, `types.isPromise()`        | 类型检查                       |
| **调试工具** | `debuglog()`, `inspect()`                    | 调试和格式化输出               |
| **继承工具** | `inherits()`, `inspect.custom`               | 继承和自定义                   |
| **格式化**   | `format()`, `inspect()`                      | 格式化输出                     |

## 5. 参数说明：util 模块常用 API

| API 名称      | 说明                                     | 示例                           |
|:--------------|:-----------------------------------------|:-------------------------------|
| **promisify** | 将回调函数转换为 Promise                 | `util.promisify(fs.readFile)`  |
| **inspect**   | 格式化对象输出                           | `util.inspect(obj)`            |
| **format**    | 格式化字符串（类似 printf）               | `util.format('%s %d', 'a', 1)` |
| **types**     | 类型检查工具                              | `util.types.isDate(obj)`       |

## 6. 返回值与状态说明

util 模块操作的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **promisify**| Function     | 返回 Promise 版本的函数                  |
| **inspect**  | String       | 返回格式化的字符串表示                   |
| **format**   | String       | 返回格式化后的字符串                     |

## 7. 代码示例：util 模块基本使用

以下示例演示了 util 模块的基本使用：

```ts
// 文件: util-basic.ts
// 功能: util 模块基本使用

import util from 'node:util';

// 1. 格式化输出
const formatted = util.format('Hello, %s! You have %d messages.', 'Alice', 5);
console.log(formatted);
// Hello, Alice! You have 5 messages.

// 2. 对象检查
const obj = { name: 'Alice', age: 25, nested: { key: 'value' } };
const inspected = util.inspect(obj, { depth: 2, colors: true });
console.log(inspected);

// 3. 类型检查
console.log('Is Date:', util.types.isDate(new Date()));        // true
console.log('Is Promise:', util.types.isPromise(Promise.resolve())); // true
```

## 8. 输出结果说明

util 模块的输出结果：

```text
Hello, Alice! You have 5 messages.
{ name: 'Alice', age: 25, nested: { key: 'value' } }
Is Date: true
Is Promise: true
```

**逻辑解析**：
- `format()` 格式化字符串，支持占位符
- `inspect()` 格式化对象，支持深度和颜色选项
- `types` 提供类型检查功能

## 9. 使用场景

### 1. 回调转 Promise

将回调式 API 转换为 Promise：

```ts
// 回调转 Promise 示例
import util from 'node:util';
import fs from 'node:fs';

const readFile = util.promisify(fs.readFile);

async function readConfig() {
    const data = await readFile('./config.json', 'utf8');
    return JSON.parse(data);
}
```

### 2. 调试输出

格式化调试输出：

```ts
// 调试输出示例
import util from 'node:util';

function debugLog(obj: any) {
    console.log(util.inspect(obj, { depth: null, colors: true }));
}
```

### 3. 类型检查

进行类型检查：

```ts
// 类型检查示例
import util from 'node:util';

function validateInput(input: any) {
    if (!util.types.isString(input)) {
        throw new Error('Input must be a string');
    }
}
```

## 10. 注意事项与常见错误

- **promisify 限制**：promisify 只适用于遵循 Node.js 回调约定的函数
- **类型检查**：类型检查函数可能不如 TypeScript 类型系统准确
- **性能考虑**：某些工具函数可能有性能开销
- **现代替代**：许多功能在现代 JavaScript 中已有替代方案

## 11. 常见问题 (FAQ)

**Q: promisify 适用于所有回调函数吗？**
A: 不，只适用于遵循 Node.js 回调约定（错误优先）的函数。

**Q: inspect 和 JSON.stringify 有什么区别？**
A: `inspect()` 更适合调试，支持循环引用、函数等；`JSON.stringify()` 只处理 JSON 兼容的数据。

**Q: 什么时候使用 util 模块？**
A: 处理回调转 Promise、调试输出、类型检查等场景时使用。

## 12. 最佳实践

- **使用 promisify**：将回调式 API 转换为 Promise，使用 async/await
- **调试工具**：使用 `inspect()` 进行调试输出
- **类型检查**：在运行时进行类型检查时使用 `types`
- **代码简化**：使用工具函数简化代码
- **现代替代**：优先使用现代 JavaScript 特性（如原生 Promise）

## 13. 对比分析：util vs 现代 JavaScript

| 功能             | util 模块                                  | 现代 JavaScript                            |
|:-----------------|:-------------------------------------------|:-------------------------------------------|
| **Promise 转换**| `util.promisify()`                         | 原生 Promise、async/await                  |
| **类型检查**     | `util.types.*`                             | TypeScript 类型系统                        |
| **格式化**       | `util.format()`, `util.inspect()`          | 模板字符串、JSON.stringify()               |
| **推荐使用**     | 处理旧代码、特殊场景                       | 新项目优先使用现代特性                     |

## 14. 练习任务

1. **util 模块实践**：
   - 使用不同的工具函数
   - 理解每个工具函数的用途
   - 实现工具函数封装

2. **回调转换实践**：
   - 使用 promisify 转换回调函数
   - 理解 promisify 的限制
   - 实现自定义 promisify

3. **调试工具实践**：
   - 使用 inspect 格式化输出
   - 使用 format 格式化字符串
   - 实现调试工具函数

4. **实际应用**：
   - 在实际项目中应用 util 模块
   - 简化代码逻辑
   - 提高开发效率

完成以上练习后，继续学习下一节：promisify 与回调转换。

## 总结

util 模块提供了常用的工具函数：

- **核心功能**：回调转换、类型检查、调试工具、格式化输出
- **实用价值**：简化代码，提高开发效率
- **最佳实践**：合理使用工具函数，优先使用现代特性

掌握 util 模块有助于编写更简洁的 Node.js 代码。

---

**最后更新**：2025-01-XX
