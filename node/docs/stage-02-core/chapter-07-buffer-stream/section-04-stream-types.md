# 2.7.4 可读流、可写流、双工流

## 1. 概述

Node.js 提供了四种类型的 Stream：可读流（Readable）、可写流（Writable）、双工流（Duplex）和转换流（Transform）。每种类型都有其特定的用途和特点。理解不同类型的 Stream 对于正确使用 Stream 至关重要。

## 2. 特性说明

- **可读流**：数据来源，只能读取数据。
- **可写流**：数据目标，只能写入数据。
- **双工流**：既可读又可写，如 TCP Socket。
- **转换流**：在传输过程中转换数据，如压缩、加密。

## 3. 语法与定义

### 可读流（Readable）

```ts
import { Readable } from 'node:stream';

const readable = new Readable({
    read() {
        // 读取逻辑
    }
});
```

### 可写流（Writable）

```ts
import { Writable } from 'node:stream';

const writable = new Writable({
    write(chunk, encoding, callback) {
        // 写入逻辑
        callback();
    }
});
```

### 双工流（Duplex）

```ts
import { Duplex } from 'node:stream';

const duplex = new Duplex({
    read() {
        // 读取逻辑
    },
    write(chunk, encoding, callback) {
        // 写入逻辑
        callback();
    }
});
```

### 转换流（Transform）

```ts
import { Transform } from 'node:stream';

const transform = new Transform({
    transform(chunk, encoding, callback) {
        // 转换逻辑
        this.push(transformed);
        callback();
    }
});
```

## 4. 基本用法

### 示例 1：可读流

```ts
// 文件: stream-readable-detail.ts
// 功能: 可读流详细示例

import { Readable } from 'node:stream';

class NumberStream extends Readable {
    private count = 0;
    private max = 10;
    
    _read() {
        if (this.count < this.max) {
            this.push(`${this.count}\n`);
            this.count++;
        } else {
            this.push(null); // 结束流
        }
    }
}

const numberStream = new NumberStream();

numberStream.on('data', (chunk) => {
    console.log('Number:', chunk.toString().trim());
});

numberStream.on('end', () => {
    console.log('Stream ended');
});
```

### 示例 2：可写流

```ts
// 文件: stream-writable-detail.ts
// 功能: 可写流详细示例

import { Writable } from 'node:stream';

class LoggerStream extends Writable {
    _write(chunk: Buffer, encoding: string, callback: () => void) {
        console.log(`[LOG] ${chunk.toString()}`);
        callback();
    }
}

const logger = new LoggerStream();

logger.write('Message 1\n');
logger.write('Message 2\n');
logger.end('Final message\n');
```

### 示例 3：转换流

```ts
// 文件: stream-transform-detail.ts
// 功能: 转换流详细示例

import { Transform } from 'node:stream';

class UpperCaseTransform extends Transform {
    _transform(chunk: Buffer, encoding: string, callback: () => void) {
        const upper = chunk.toString().toUpperCase();
        this.push(upper);
        callback();
    }
}

const transform = new UpperCaseTransform();

transform.on('data', (chunk) => {
    console.log('Transformed:', chunk.toString());
});

transform.write('hello\n');
transform.write('world\n');
transform.end();
```

### 示例 4：双工流

```ts
// 文件: stream-duplex-detail.ts
// 功能: 双工流详细示例

import { Duplex } from 'node:stream';

class EchoStream extends Duplex {
    private buffer: Buffer[] = [];
    
    _read() {
        // 从缓冲区读取数据
        while (this.buffer.length > 0) {
            const chunk = this.buffer.shift();
            if (chunk) {
                this.push(chunk);
            }
        }
    }
    
    _write(chunk: Buffer, encoding: string, callback: () => void) {
        // 写入数据到缓冲区
        this.buffer.push(chunk);
        // 触发读取
        this._read();
        callback();
    }
}

const echo = new EchoStream();

echo.on('data', (chunk) => {
    console.log('Echoed:', chunk.toString());
});

echo.write('Hello\n');
echo.write('World\n');
echo.end();
```

## 5. 参数说明：Stream 类型参数

### Readable 参数

| 参数名       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **read**     | Function | 读取数据的函数（可选，可重写 `_read()`） | `function() { this.push(data) }`|
| **objectMode**| Boolean | 对象模式                                 | `true`                         |
| **highWaterMark**| Number | 缓冲区大小                             | `16384`                        |

### Writable 参数

| 参数名       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **write**    | Function | 写入数据的函数（可选，可重写 `_write()`）| `function(chunk, enc, cb) {}`  |
| **objectMode**| Boolean | 对象模式                                 | `true`                         |
| **highWaterMark**| Number | 缓冲区大小                             | `16384`                        |

## 6. 返回值与状态说明

Stream 操作的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **创建**     | Stream       | 返回对应类型的 Stream 实例               |
| **write**    | Boolean      | 返回是否应该暂停写入（背压）             |
| **push**     | Boolean      | 返回是否应该暂停读取（背压）             |

## 7. 代码示例：完整的 Stream 应用

以下示例演示了如何组合使用不同类型的 Stream：

```ts
// 文件: stream-complete.ts
// 功能: 完整的 Stream 应用

import { Readable, Writable, Transform } from 'node:stream';
import fs from 'node:fs';

// 1. 可读流：读取数据
const readable = new Readable({
    read() {
        this.push('Line 1\n');
        this.push('Line 2\n');
        this.push('Line 3\n');
        this.push(null);
    }
});

// 2. 转换流：转换为大写
const upperTransform = new Transform({
    transform(chunk, encoding, callback) {
        this.push(chunk.toString().toUpperCase());
        callback();
    }
});

// 3. 转换流：添加行号
let lineNumber = 1;
const lineNumberTransform = new Transform({
    transform(chunk, encoding, callback) {
        const lines = chunk.toString().split('\n').filter(Boolean);
        const numbered = lines.map(line => `${lineNumber++}: ${line}\n`).join('');
        this.push(numbered);
        callback();
    }
});

// 4. 可写流：写入文件
const writable = fs.createWriteStream('./output.txt');

// 5. 管道连接
readable
    .pipe(upperTransform)
    .pipe(lineNumberTransform)
    .pipe(writable);

writable.on('finish', () => {
    console.log('Processing completed');
});
```

## 8. 输出结果说明

Stream 处理的输出结果（output.txt）：

```text
1: LINE 1
2: LINE 2
3: LINE 3
```

**逻辑解析**：
- 可读流提供原始数据
- 转换流1：转换为大写
- 转换流2：添加行号
- 可写流：写入文件
- 数据通过管道自动流转

## 9. 使用场景

### 1. 文件处理管道

处理文件的多个步骤：

```ts
// 文件处理管道示例
import fs from 'node:fs';
import { Transform } from 'node:stream';
import zlib from 'node:zlib';

fs.createReadStream('./input.txt')
    .pipe(new Transform({ /* 转换逻辑 */ }))
    .pipe(zlib.createGzip())
    .pipe(fs.createWriteStream('./output.txt.gz'));
```

### 2. 数据转换链

实现数据转换链：

```ts
// 数据转换链示例
readable
    .pipe(transform1)
    .pipe(transform2)
    .pipe(transform3)
    .pipe(writable);
```

### 3. 网络代理

实现网络代理：

```ts
// 网络代理示例
import http from 'node:http';

const server = http.createServer((req, res) => {
    const proxyReq = http.request({
        hostname: 'target-server.com',
        path: req.url,
        method: req.method
    }, (proxyRes) => {
        res.writeHead(proxyRes.statusCode!, proxyRes.headers);
        proxyRes.pipe(res);
    });
    
    req.pipe(proxyReq);
});
```

## 10. 注意事项与常见错误

- **错误处理**：每种 Stream 类型都需要处理 `error` 事件
- **背压处理**：注意可写流的背压，监听 `drain` 事件
- **流结束**：确保流正确结束，调用 `end()` 或 `push(null)`
- **管道断开**：处理管道断开的情况
- **内存管理**：注意缓冲区大小，避免内存问题

## 11. 常见问题 (FAQ)

**Q: 可读流和可写流可以互相转换吗？**
A: 不可以直接转换，但可以通过双工流或转换流实现。

**Q: 如何实现自定义的 Stream？**
A: 继承对应的 Stream 类（Readable、Writable、Duplex、Transform），实现相应的方法。

**Q: 转换流和双工流有什么区别？**
A: 转换流是特殊的双工流，输入和输出有明确的转换关系；双工流可以独立处理输入和输出。

## 12. 最佳实践

- **类型选择**：根据需求选择合适的 Stream 类型
- **错误处理**：为每种 Stream 类型处理错误
- **管道使用**：使用管道简化数据流转
- **背压处理**：正确处理背压，避免内存问题
- **资源清理**：确保流正确结束，清理资源

## 13. 对比分析：Stream 类型选择

| 类型           | 特点                                     | 适用场景                       |
|:---------------|:-----------------------------------------|:-------------------------------|
| **Readable**   | 只能读取数据                              | 文件读取、数据生成             |
| **Writable**   | 只能写入数据                              | 文件写入、数据输出             |
| **Duplex**     | 既可读又可写，输入输出独立                 | TCP Socket、WebSocket          |
| **Transform**  | 既可读又可写，输入输出有转换关系           | 数据转换、压缩、加密           |

## 14. 练习任务

1. **可读流实践**：
   - 创建自定义可读流
   - 实现数据生成逻辑
   - 处理流结束

2. **可写流实践**：
   - 创建自定义可写流
   - 实现数据写入逻辑
   - 处理背压

3. **转换流实践**：
   - 创建自定义转换流
   - 实现数据转换逻辑
   - 组合多个转换流

4. **实际应用**：
   - 在实际项目中应用不同类型的 Stream
   - 实现数据转换管道
   - 处理复杂的数据流

完成以上练习后，继续学习下一节：管道（pipe）与背压（backpressure）。

## 总结

不同类型的 Stream 有不同的用途：

- **可读流**：数据来源，只能读取
- **可写流**：数据目标，只能写入
- **双工流**：既可读又可写，输入输出独立
- **转换流**：既可读又可写，输入输出有转换关系

理解不同类型的 Stream 有助于正确使用 Stream。

---

**最后更新**：2025-01-XX
