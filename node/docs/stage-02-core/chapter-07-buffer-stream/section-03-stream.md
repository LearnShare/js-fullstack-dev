# 2.7.3 Stream 基础

## 1. 概述

Stream 是 Node.js 中处理数据流的抽象接口。Stream 允许数据以流的形式传输，而不是一次性加载到内存中。这对于处理大文件、网络通信、实时数据等场景非常重要。理解 Stream 的使用是掌握 Node.js 高效数据处理的关键。

## 2. 特性说明

- **流式处理**：数据以流的形式传输，不需要全部加载到内存。
- **事件驱动**：基于事件系统，通过事件处理数据。
- **内存效率**：只占用缓冲区大小的内存，可以处理大于内存的数据。
- **管道操作**：支持通过管道连接多个 Stream。
- **背压处理**：自动处理数据生产速度与消费速度不匹配的情况。

## 3. Stream 类型

Node.js 提供了四种类型的 Stream：

| Stream 类型   | 说明                                     | 示例                           |
|:--------------|:-----------------------------------------|:-------------------------------|
| **Readable**  | 可读流，数据来源                          | 文件读取、HTTP 请求            |
| **Writable**  | 可写流，数据目标                          | 文件写入、HTTP 响应            |
| **Duplex**    | 双工流，既可读又可写                      | TCP Socket、WebSocket          |
| **Transform** | 转换流，在传输过程中转换数据              | 压缩、加密、数据转换           |

## 4. 基本用法

### 示例 1：可读流（Readable）

```ts
// 文件: stream-readable.ts
// 功能: 可读流示例

import { Readable } from 'node:stream';

// 创建可读流
const readable = new Readable({
    read() {
        // 推送数据
        this.push('Chunk 1\n');
        this.push('Chunk 2\n');
        this.push(null); // 结束流
    }
});

// 监听数据事件
readable.on('data', (chunk) => {
    console.log('Received:', chunk.toString());
});

readable.on('end', () => {
    console.log('Stream ended');
});
```

### 示例 2：可写流（Writable）

```ts
// 文件: stream-writable.ts
// 功能: 可写流示例

import { Writable } from 'node:stream';

// 创建可写流
const writable = new Writable({
    write(chunk, encoding, callback) {
        console.log('Writing:', chunk.toString());
        callback(); // 通知写入完成
    }
});

// 写入数据
writable.write('Hello\n');
writable.write('World\n');
writable.end(); // 结束流
```

### 示例 3：管道操作

```ts
// 文件: stream-pipe.ts
// 功能: 管道操作示例

import { Readable, Writable } from 'node:stream';

const readable = new Readable({
    read() {
        this.push('Data chunk\n');
        this.push(null);
    }
});

const writable = new Writable({
    write(chunk, encoding, callback) {
        console.log('Received:', chunk.toString());
        callback();
    }
});

// 使用管道连接
readable.pipe(writable);
```

## 5. 参数说明：Stream 创建参数

### Readable 参数

| 参数名       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **read**     | Function | 读取数据的函数                            | `function() { this.push(data) }`|
| **objectMode**| Boolean | 对象模式（传输对象而非 Buffer）          | `true`                         |
| **highWaterMark**| Number | 缓冲区大小（字节）                    | `16384`                        |

### Writable 参数

| 参数名       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **write**    | Function | 写入数据的函数                            | `function(chunk, enc, cb) {}`  |
| **objectMode**| Boolean | 对象模式                                 | `true`                         |
| **highWaterMark**| Number | 缓冲区大小（字节）                    | `16384`                        |

## 6. 返回值与状态说明

Stream 操作的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **创建**     | Stream       | 返回 Stream 实例                         |
| **pipe**     | Stream       | 返回目标 Stream，支持链式调用            |
| **write**    | Boolean      | 返回是否应该暂停写入（背压）             |

## 7. 代码示例：文件流操作

以下示例演示了如何使用 Stream 处理文件：

```ts
// 文件: stream-file.ts
// 功能: 文件流操作

import fs from 'node:fs';
import { Transform } from 'node:stream';

// 1. 读取文件流
const readStream = fs.createReadStream('./input.txt');

// 2. 写入文件流
const writeStream = fs.createWriteStream('./output.txt');

// 3. 转换流（转换为大写）
const transform = new Transform({
    transform(chunk, encoding, callback) {
        this.push(chunk.toString().toUpperCase());
        callback();
    }
});

// 4. 管道连接
readStream
    .pipe(transform)
    .pipe(writeStream);

// 5. 监听事件
writeStream.on('finish', () => {
    console.log('File processed');
});
```

## 8. 输出结果说明

Stream 操作的输出结果：

```text
Received: Chunk 1
Received: Chunk 2
Stream ended
Writing: Hello
Writing: World
File processed
```

**逻辑解析**：
- 可读流通过 `data` 事件提供数据
- 可写流通过 `write()` 方法接收数据
- 管道自动处理数据流转和背压

## 9. 使用场景

### 1. 大文件处理

处理大文件而不占用大量内存：

```ts
// 大文件处理示例
import fs from 'node:fs';

const readStream = fs.createReadStream('./large-file.txt');
const writeStream = fs.createWriteStream('./output.txt');

readStream.pipe(writeStream);
```

### 2. 数据转换

在传输过程中转换数据：

```ts
// 数据转换示例
import { Transform } from 'node:stream';

const jsonTransform = new Transform({
    objectMode: true,
    transform(chunk, encoding, callback) {
        try {
            const json = JSON.parse(chunk.toString());
            this.push(JSON.stringify(json, null, 2));
        } catch (error) {
            callback(error);
            return;
        }
        callback();
    }
});
```

### 3. 网络通信

处理网络数据流：

```ts
// 网络通信示例
import http from 'node:http';

const server = http.createServer((req, res) => {
    // req 和 res 都是 Stream
    req.pipe(res); // 回显请求数据
});
```

## 10. 注意事项与常见错误

- **错误处理**：必须处理 Stream 的 `error` 事件
- **背压处理**：注意数据生产速度与消费速度的匹配
- **流结束**：确保流正确结束，避免资源泄漏
- **内存管理**：虽然 Stream 内存效率高，但仍需注意缓冲区大小
- **管道断开**：处理管道断开的情况

## 11. 常见问题 (FAQ)

**Q: Stream 是同步还是异步的？**
A: Stream 是异步的，基于事件系统，数据以事件形式传输。

**Q: 如何暂停和恢复 Stream？**
A: 使用 `pause()` 和 `resume()` 方法，或监听 `drain` 事件处理背压。

**Q: 管道断开后如何处理？**
A: 监听 `error` 和 `close` 事件，清理资源。

## 12. 最佳实践

- **错误处理**：始终处理 `error` 事件
- **背压处理**：监听 `drain` 事件处理背压
- **资源清理**：确保流正确结束，清理资源
- **管道使用**：使用管道简化数据流转
- **性能优化**：合理设置缓冲区大小

## 13. 对比分析：Stream vs Buffer

| 维度             | Stream                                    | Buffer                                    |
|:-----------------|:------------------------------------------|:------------------------------------------|
| **内存占用**     | 只占用缓冲区大小的内存                    | 占用完整数据大小的内存                    |
| **处理方式**     | 流式分块处理                              | 一次性处理                                |
| **适用场景**     | 大文件、网络通信、实时数据                 | 小文件、需要完整数据                       |
| **性能**         | 大数据时性能好，避免内存溢出               | 小数据时性能好                             |

## 14. 练习任务

1. **可读流实践**：
   - 创建可读流
   - 监听数据事件
   - 理解流的生命周期

2. **可写流实践**：
   - 创建可写流
   - 写入数据
   - 处理背压

3. **管道实践**：
   - 使用管道连接流
   - 实现数据流转
   - 处理管道错误

4. **实际应用**：
   - 使用 Stream 处理大文件
   - 实现数据转换功能
   - 处理网络数据流

完成以上练习后，继续学习下一节：可读流、可写流、双工流。

## 总结

Stream 是 Node.js 流式数据处理的基础：

- **流式处理**：数据以流的形式传输
- **内存效率**：只占用缓冲区大小的内存
- **事件驱动**：基于事件系统处理数据
- **最佳实践**：错误处理、背压处理、资源清理

掌握 Stream 有助于高效处理大量数据。

---

**最后更新**：2025-01-XX
