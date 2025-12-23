# 2.7.2 Buffer 基础

## 1. 概述

Buffer 是 Node.js 中用于处理二进制数据的类数组对象。在 JavaScript 中，字符串是 Unicode 编码，但在处理文件、网络数据、加密数据等场景时，需要直接操作字节数据。Buffer 提供了这种能力，是 Node.js 处理二进制数据的基础。

## 2. 特性说明

- **二进制数据**：直接操作字节数据，不受编码限制。
- **类数组接口**：提供类似数组的接口，支持索引访问。
- **固定大小**：Buffer 创建后大小固定，不能动态调整。
- **编码支持**：支持多种编码格式的转换（UTF-8、ASCII、Base64 等）。
- **内存效率**：在 V8 堆外分配内存，提高性能。

## 3. 语法与定义

### 创建 Buffer

```ts
// 从字符串创建
Buffer.from(string: string, encoding?: string): Buffer

// 从数组创建
Buffer.from(array: number[]): Buffer

// 创建指定大小的 Buffer
Buffer.alloc(size: number, fill?: number | string, encoding?: string): Buffer

// 创建未初始化的 Buffer（不推荐）
Buffer.allocUnsafe(size: number): Buffer
```

## 4. 基本用法

### 示例 1：创建 Buffer

```ts
// 文件: buffer-create.ts
// 功能: 创建 Buffer

import { Buffer } from 'node:buffer';

// 从字符串创建
const buf1 = Buffer.from('Hello', 'utf8');
console.log('Buffer from string:', buf1);

// 从数组创建
const buf2 = Buffer.from([0x48, 0x65, 0x6c, 0x6c, 0x6f]);
console.log('Buffer from array:', buf2);

// 创建指定大小的 Buffer
const buf3 = Buffer.alloc(10);
console.log('Allocated buffer:', buf3);

// 创建并填充
const buf4 = Buffer.alloc(10, 'a', 'utf8');
console.log('Filled buffer:', buf4.toString());
```

### 示例 2：Buffer 操作

```ts
// 文件: buffer-operations.ts
// 功能: Buffer 操作

import { Buffer } from 'node:buffer';

const buf = Buffer.from('Hello, Node.js!');

// 读取字节
console.log('First byte:', buf[0]); // 72 (H 的 ASCII 码)

// 修改字节
buf[0] = 104; // h 的 ASCII 码
console.log('Modified:', buf.toString());

// 切片
const slice = buf.slice(0, 5);
console.log('Slice:', slice.toString());

// 复制
const copy = Buffer.alloc(5);
buf.copy(copy, 0, 0, 5);
console.log('Copy:', copy.toString());
```

### 示例 3：编码转换

```ts
// 文件: buffer-encoding.ts
// 功能: Buffer 编码转换

import { Buffer } from 'node:buffer';

const text = 'Hello, 世界!';

// 转换为不同编码
const utf8 = Buffer.from(text, 'utf8');
const base64 = utf8.toString('base64');
const hex = utf8.toString('hex');

console.log('UTF-8:', utf8);
console.log('Base64:', base64);
console.log('Hex:', hex);

// 从不同编码恢复
const fromBase64 = Buffer.from(base64, 'base64').toString('utf8');
const fromHex = Buffer.from(hex, 'hex').toString('utf8');

console.log('From Base64:', fromBase64);
console.log('From Hex:', fromHex);
```

## 5. 参数说明：Buffer 创建方法

### from 方法参数

| 参数名       | 类型           | 说明                                     | 示例                           |
|:-------------|:---------------|:-----------------------------------------|:-------------------------------|
| **source**   | String/Array   | 数据源（字符串或数组）                   | `'Hello'` 或 `[72, 101, 108]`  |
| **encoding** | String         | 编码格式（字符串时）                     | `'utf8'`, `'base64'`, `'hex'`  |

### alloc 方法参数

| 参数名       | 类型           | 说明                                     | 示例                           |
|:-------------|:---------------|:-----------------------------------------|:-------------------------------|
| **size**     | Number         | Buffer 大小（字节）                      | `1024`                         |
| **fill**     | Number/String  | 填充值（可选）                           | `0` 或 `'a'`                    |
| **encoding** | String         | 编码格式（fill 是字符串时）              | `'utf8'`                        |

## 6. 返回值与状态说明

Buffer 操作的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **创建**     | Buffer       | 返回 Buffer 实例                         |
| **toString** | String       | 返回字符串表示                           |
| **slice**    | Buffer       | 返回新的 Buffer（共享内存）               |
| **copy**     | Number       | 返回复制的字节数                         |

## 7. 代码示例：Buffer 实用操作

以下示例演示了 Buffer 的实用操作：

```ts
// 文件: buffer-utilities.ts
// 功能: Buffer 实用操作

import { Buffer } from 'node:buffer';

// 1. 连接多个 Buffer
function concatBuffers(buffers: Buffer[]): Buffer {
    return Buffer.concat(buffers);
}

// 2. 比较 Buffer
function compareBuffers(buf1: Buffer, buf2: Buffer): number {
    return buf1.compare(buf2);
}

// 3. 查找 Buffer
function findInBuffer(buf: Buffer, search: Buffer | string): number {
    return buf.indexOf(search);
}

// 4. 填充 Buffer
function fillBuffer(buf: Buffer, value: number | string): Buffer {
    return buf.fill(value);
}

// 使用
const buf1 = Buffer.from('Hello');
const buf2 = Buffer.from('World');
const combined = concatBuffers([buf1, buf2]);
console.log('Combined:', combined.toString());

const index = findInBuffer(combined, 'World');
console.log('Found at index:', index);
```

## 8. 输出结果说明

Buffer 操作的输出结果：

```text
Combined: HelloWorld
Found at index: 5
```

**逻辑解析**：
- `concat()` 连接多个 Buffer
- `indexOf()` 查找子 Buffer 或字符串的位置
- Buffer 操作都是高效的字节级操作

## 9. 使用场景

### 1. 文件处理

处理二进制文件：

```ts
// 文件处理示例
import fsPromises from 'node:fs/promises';

async function processImage(filePath: string) {
    const buffer = await fsPromises.readFile(filePath);
    // 处理图片数据
    return buffer;
}
```

### 2. 网络通信

处理网络数据：

```ts
// 网络通信示例
import { createServer, IncomingMessage, ServerResponse } from 'node:http';

const server = createServer((req: IncomingMessage, res: ServerResponse): void => {
    let data = Buffer.alloc(0);
    
    req.on('data', (chunk: Buffer): void => {
        data = Buffer.concat([data, chunk]);
    });
    
    req.on('end', (): void => {
        // 处理完整数据
    });
});
```

### 3. 加密操作

处理加密数据：

```ts
// 加密操作示例
import crypto from 'node:crypto';

function encryptData(data: string, key: Buffer): Buffer {
    const iv = crypto.randomBytes(16);
    const cipher = crypto.createCipheriv('aes-256-cbc', key, iv);
    
    const encrypted = Buffer.concat([
        cipher.update(data, 'utf8'),
        cipher.final()
    ]);
    
    return Buffer.concat([iv, encrypted]);
}
```

## 10. 注意事项与常见错误

- **内存管理**：Buffer 会占用内存，注意大 Buffer 的内存使用
- **编码问题**：明确数据的编码格式，避免乱码
- **大小限制**：Buffer 有最大大小限制（约 2GB）
- **共享内存**：`slice()` 返回的 Buffer 共享内存，修改会影响原 Buffer
- **性能考虑**：大 Buffer 操作可能较慢，考虑使用 Stream

## 11. 常见问题 (FAQ)

**Q: Buffer 和数组有什么区别？**
A: Buffer 存储字节数据，数组存储任意类型。Buffer 大小固定，数组可以动态调整。

**Q: 如何安全地创建 Buffer？**
A: 使用 `Buffer.alloc()` 或 `Buffer.from()`，避免使用 `Buffer.allocUnsafe()`。

**Q: Buffer 可以动态调整大小吗？**
A: 不可以，Buffer 创建后大小固定。需要调整大小时创建新的 Buffer。

## 12. 最佳实践

- **使用 alloc/from**：使用 `Buffer.alloc()` 和 `Buffer.from()`，避免 `allocUnsafe()`
- **明确编码**：明确指定编码格式，避免默认编码问题
- **内存管理**：注意大 Buffer 的内存使用，考虑使用 Stream
- **错误处理**：处理 Buffer 操作的错误
- **性能优化**：合理使用 Buffer，避免不必要的复制

## 13. 对比分析：Buffer 创建方法

| 方法           | 特点                                     | 适用场景                       |
|:---------------|:-----------------------------------------|:-------------------------------|
| **Buffer.from()**| 从数据创建，安全                         | 从字符串、数组创建 Buffer      |
| **Buffer.alloc()**| 创建并初始化，安全                       | 创建指定大小的 Buffer          |
| **Buffer.allocUnsafe()**| 创建但不初始化，可能包含旧数据，不安全 | 性能要求极高的场景（不推荐）   |

## 14. 练习任务

1. **Buffer 创建实践**：
   - 使用不同方法创建 Buffer
   - 理解不同创建方法的区别
   - 实现 Buffer 转换

2. **Buffer 操作实践**：
   - 进行 Buffer 的读取、修改、切片、复制
   - 理解 Buffer 的类数组接口
   - 实现 Buffer 工具函数

3. **编码转换实践**：
   - 在不同编码格式间转换
   - 理解编码的作用
   - 实现编码转换功能

4. **实际应用**：
   - 在实际项目中应用 Buffer
   - 处理二进制数据
   - 实现数据转换功能

完成以上练习后，继续学习下一节：Stream 基础。

## 总结

Buffer 是 Node.js 处理二进制数据的基础：

- **核心功能**：处理二进制数据，支持多种编码
- **类数组接口**：提供类似数组的操作接口
- **固定大小**：创建后大小固定
- **最佳实践**：使用安全的创建方法，明确编码，注意内存管理

掌握 Buffer 有助于处理各种二进制数据。

---

**最后更新**：2025-01-XX
