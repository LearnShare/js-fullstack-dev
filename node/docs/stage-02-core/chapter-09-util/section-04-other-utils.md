# 2.9.4 其他工具函数

## 1. 概述

util 模块还提供了其他有用的工具函数，包括继承工具、文本编码、错误处理等。虽然这些函数的使用频率不如 promisify 和类型检查高，但在特定场景下仍然很有用。理解这些工具函数有助于充分利用 util 模块的功能。

## 2. 特性说明

- **继承工具**：提供继承相关的工具函数。
- **文本编码**：提供文本编码转换工具。
- **错误处理**：提供错误处理相关的工具。
- **文本处理**：提供文本处理相关的工具。
- **兼容性工具**：提供兼容性相关的工具。

## 3. 语法与定义

### 继承工具

```ts
// 继承工具（已废弃，不推荐使用）
util.inherits(constructor: Function, superConstructor: Function): void
```

### 文本编码

```ts
// 文本编码转换
util.TextEncoder
util.TextDecoder
```

### 错误处理

```ts
// 错误处理
util.callbackify(asyncFn: Function): Function
```

## 4. 基本用法

### 示例 1：TextEncoder/TextDecoder

```ts
// 文件: util-text-encoding.ts
// 功能: 文本编码

import { TextEncoder, TextDecoder } from 'node:util';

// 编码文本为 UTF-8 字节
const encoder = new TextEncoder();
const encoded = encoder.encode('Hello, 世界!');
console.log('Encoded:', encoded);
// Uint8Array [72, 101, 108, 108, 111, ...]

// 解码字节为文本
const decoder = new TextDecoder('utf-8');
const decoded = decoder.decode(encoded);
console.log('Decoded:', decoded);
// Hello, 世界!
```

### 示例 2：callbackify

```ts
// 文件: util-callbackify.ts
// 功能: callbackify 使用

import util from 'node:util';

// Promise 函数
async function asyncFunction(input: string): Promise<string> {
    return `Processed: ${input}`;
}

// 转换为回调函数
const callbackFunction = util.callbackify(asyncFunction);

// 使用回调方式
callbackFunction('data', (error: Error | null, result?: string) => {
    if (error) {
        console.error('Error:', error);
    } else {
        console.log('Result:', result);
    }
});
```

### 示例 3：其他实用工具

```ts
// 文件: util-other.ts
// 功能: 其他实用工具

import util from 'node:util';

// 1. 深度相等比较（需要手动实现或使用库）
function deepEqual(a: any, b: any): boolean {
    return JSON.stringify(a) === JSON.stringify(b);
}

// 2. 获取系统错误信息
function getSystemError(errno: number): string {
    return util.getSystemErrorName(errno) || 'Unknown error';
}

// 3. 格式化错误堆栈
function formatError(error: Error): string {
    return util.inspect(error, { depth: null });
}
```

## 5. 参数说明：其他工具函数参数

### callbackify 参数

| 参数名       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **asyncFn**  | Function | 返回 Promise 的异步函数                  | `async () => {}`               |

### TextEncoder/TextDecoder 参数

| 参数名       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **encoding** | String   | 编码格式（TextDecoder，默认 'utf-8'）     | `'utf-8'`, `'utf-16'`          |

## 6. 返回值与状态说明

其他工具函数的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **callbackify**| Function   | 返回回调版本的函数                       |
| **encode**    | Uint8Array  | 返回编码后的字节数组                     |
| **decode**    | String      | 返回解码后的字符串                       |

## 7. 代码示例：完整的工具函数应用

以下示例演示了其他工具函数的应用：

```ts
// 文件: util-other-complete.ts
// 功能: 其他工具函数完整应用

import { TextEncoder, TextDecoder } from 'node:util';
import util from 'node:util';

// 1. 文本编码工具类
class TextEncoding {
    private encoder = new TextEncoder();
    private decoder = new TextDecoder('utf-8');
    
    encode(text: string): Uint8Array {
        return this.encoder.encode(text);
    }
    
    decode(bytes: Uint8Array): string {
        return this.decoder.decode(bytes);
    }
    
    encodeBase64(text: string): string {
        const bytes = this.encode(text);
        return Buffer.from(bytes).toString('base64');
    }
    
    decodeBase64(base64: string): string {
        const bytes = Buffer.from(base64, 'base64');
        return this.decode(bytes);
    }
}

// 2. 错误格式化工具
class ErrorFormatter {
    static format(error: Error, options?: { depth?: number }): string {
        return util.inspect(error, {
            depth: options?.depth ?? null,
            colors: true
        });
    }
    
    static getSystemError(errno: number): string {
        return util.getSystemErrorName(errno) || 'Unknown error';
    }
}

// 使用
const encoding = new TextEncoding();
const encoded = encoding.encodeBase64('Hello, World!');
console.log('Base64:', encoded);

const decoded = encoding.decodeBase64(encoded);
console.log('Decoded:', decoded);
```

## 8. 输出结果说明

工具函数的输出结果：

```text
Base64: SGVsbG8sIFdvcmxkIQ==
Decoded: Hello, World!
```

**逻辑解析**：
- TextEncoder/TextDecoder 处理文本编码
- 可以配合 Buffer 进行 Base64 编码
- 工具函数简化了编码转换操作

## 9. 使用场景

### 1. 文本编码转换

处理不同编码格式的文本：

```ts
// 文本编码转换示例
import { TextEncoder, TextDecoder } from 'node:util';

function convertEncoding(text: string, from: string, to: string): string {
    const decoder = new TextDecoder(from);
    const encoder = new TextEncoder();
    const bytes = encoder.encode(text);
    return decoder.decode(bytes);
}
```

### 2. 兼容旧代码

将 Promise 函数转换为回调函数：

```ts
// 兼容旧代码示例
import util from 'node:util';

async function modernFunction(input: string): Promise<string> {
    return `Result: ${input}`;
}

// 转换为回调函数以兼容旧代码
const legacyFunction = util.callbackify(modernFunction);
```

### 3. 错误处理

格式化错误信息：

```ts
// 错误处理示例
import util from 'node:util';

function formatError(error: Error): string {
    return util.inspect(error, { depth: null, colors: true });
}
```

## 10. 注意事项与常见错误

- **inherits 已废弃**：`util.inherits()` 已废弃，使用 ES6 class extends
- **callbackify 限制**：只适用于返回 Promise 的函数
- **编码格式**：注意文本编码格式，避免乱码
- **性能考虑**：某些工具函数可能有性能开销
- **现代替代**：优先使用现代 JavaScript 特性

## 11. 常见问题 (FAQ)

**Q: 为什么不使用 util.inherits()？**
A: `util.inherits()` 已废弃，应该使用 ES6 的 `class extends` 语法。

**Q: TextEncoder/TextDecoder 和 Buffer 有什么区别？**
A: TextEncoder/TextDecoder 专门处理文本编码，Buffer 更通用，可以处理任意二进制数据。

**Q: 什么时候使用 callbackify？**
A: 需要将 Promise 函数转换为回调函数以兼容旧代码时使用。

## 12. 最佳实践

- **避免 inherits**：不使用已废弃的 `inherits()`，使用 ES6 class
- **文本编码**：使用 TextEncoder/TextDecoder 处理文本编码
- **错误处理**：使用 `inspect()` 格式化错误信息
- **现代替代**：优先使用现代 JavaScript 特性
- **代码简化**：使用工具函数简化代码

## 13. 对比分析：util 工具 vs 现代 JavaScript

| 功能             | util 工具                                  | 现代 JavaScript                            |
|:-----------------|:-------------------------------------------|:-------------------------------------------|
| **继承**         | `util.inherits()`（已废弃）                | `class extends`                            |
| **文本编码**     | `TextEncoder/TextDecoder`                  | 原生支持（浏览器和 Node.js）               |
| **错误处理**     | `util.inspect()`                           | `JSON.stringify()`, 模板字符串             |
| **推荐使用**     | 特殊场景使用                               | 优先使用现代特性                           |

## 14. 练习任务

1. **文本编码实践**：
   - 使用 TextEncoder/TextDecoder
   - 实现编码转换功能
   - 处理不同编码格式

2. **callbackify 实践**：
   - 使用 callbackify 转换函数
   - 理解 callbackify 的用途
   - 实现兼容性转换

3. **实际应用**：
   - 在实际项目中应用工具函数
   - 实现文本编码转换
   - 实现错误格式化

完成以上练习后，继续学习下一章：操作系统与进程信息。

## 总结

util 模块提供了多种实用工具函数：

- **核心功能**：promisify、类型检查、调试工具、文本编码
- **实用价值**：简化代码，提高开发效率
- **最佳实践**：合理使用工具函数，优先使用现代特性

掌握 util 模块有助于编写更简洁高效的 Node.js 代码。

---

**最后更新**：2025-01-XX
