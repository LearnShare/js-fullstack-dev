# 2.7.5 管道（pipe）与背压（backpressure）

## 1. 概述

管道（pipe）是连接多个 Stream 的便捷方式，可以自动处理数据流转。背压（backpressure）是当数据生产速度大于消费速度时，系统自动暂停生产以平衡速度的机制。理解管道和背压对于高效使用 Stream 至关重要。

## 2. 特性说明

- **自动流转**：管道自动处理数据从源流到目标流的传输。
- **背压处理**：自动处理数据生产速度与消费速度不匹配的情况。
- **错误传播**：管道中的错误会自动传播。
- **链式调用**：支持链式调用，连接多个 Stream。
- **资源管理**：自动管理流的生命周期。

## 3. 语法与定义

### 管道操作

```ts
// 基本管道
readable.pipe(writable): Writable

// 链式管道
readable.pipe(transform1).pipe(transform2).pipe(writable)

// 取消管道
readable.unpipe(writable): Readable
```

### 背压处理

```ts
// 监听 drain 事件（可写流）
writable.on('drain', () => {
    // 可以继续写入
});

// 检查写入状态
const canWrite = writable.write(chunk);
if (!canWrite) {
    // 等待 drain 事件
}
```

## 4. 基本用法

### 示例 1：基本管道

```ts
// 文件: stream-pipe-basic.ts
// 功能: 基本管道操作

import fs from 'node:fs';

const readStream = fs.createReadStream('./input.txt');
const writeStream = fs.createWriteStream('./output.txt');

// 使用管道连接
readStream.pipe(writeStream);

writeStream.on('finish', () => {
    console.log('File copied');
});

// 错误处理
readStream.on('error', (error) => {
    console.error('Read error:', error);
});

writeStream.on('error', (error) => {
    console.error('Write error:', error);
});
```

### 示例 2：链式管道

```ts
// 文件: stream-pipe-chain.ts
// 功能: 链式管道

import fs from 'node:fs';
import { Transform } from 'node:stream';
import zlib from 'node:zlib';

// 转换流：转换为大写
const upperTransform = new Transform({
    transform(chunk, encoding, callback) {
        this.push(chunk.toString().toUpperCase());
        callback();
    }
});

// 管道链：读取 -> 转换 -> 压缩 -> 写入
fs.createReadStream('./input.txt')
    .pipe(upperTransform)
    .pipe(zlib.createGzip())
    .pipe(fs.createWriteStream('./output.txt.gz'))
    .on('finish', () => {
        console.log('Processing completed');
    });
```

### 示例 3：背压处理

```ts
// 文件: stream-backpressure.ts
// 功能: 背压处理

import { Readable, Writable } from 'node:stream';

// 快速生产数据的可读流
const readable = new Readable({
    read() {
        for (let i = 0; i < 1000; i++) {
            if (!this.push(`Data ${i}\n`)) {
                // push 返回 false，表示应该暂停
                console.log('Paused due to backpressure');
                return;
            }
        }
    }
});

// 慢速消费数据的可写流
const writable = new Writable({
    write(chunk, encoding, callback) {
        // 模拟慢速处理
        setTimeout(() => {
            console.log('Processed:', chunk.toString().trim());
            callback();
        }, 100);
    }
});

// 使用管道，自动处理背压
readable.pipe(writable);

writable.on('drain', () => {
    console.log('Drain event: can continue writing');
});
```

## 5. 参数说明：管道方法参数

### pipe 方法参数

| 参数名       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **destination**| Writable| 目标可写流                                | `writeStream`                  |
| **options**  | Object   | 管道选项（可选）                         | `{ end: false }`               |
| **end**      | Boolean  | 是否在源流结束时结束目标流（默认 true）   | `false`                        |

## 6. 返回值与状态说明

管道操作的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **pipe**     | Writable     | 返回目标流，支持链式调用                  |
| **unpipe**   | Readable     | 返回源流                                 |
| **write**    | Boolean      | 返回是否应该暂停写入（false 表示背压）   |

## 7. 代码示例：完整的管道应用

以下示例演示了如何构建完整的管道应用：

```ts
// 文件: stream-pipe-complete.ts
// 功能: 完整的管道应用

import fs from 'node:fs';
import { Transform } from 'node:stream';
import zlib from 'node:zlib';

// 1. 数据过滤转换流
class FilterTransform extends Transform {
    private filter: (chunk: Buffer) => boolean;
    
    constructor(filter: (chunk: Buffer) => boolean) {
        super();
        this.filter = filter;
    }
    
    _transform(chunk: Buffer, encoding: string, callback: () => void) {
        if (this.filter(chunk)) {
            this.push(chunk);
        }
        callback();
    }
}

// 2. 数据统计转换流
class StatsTransform extends Transform {
    private count = 0;
    private size = 0;
    
    _transform(chunk: Buffer, encoding: string, callback: () => void) {
        this.count++;
        this.size += chunk.length;
        this.push(chunk);
        callback();
    }
    
    _flush(callback: () => void) {
        this.push(`\nStats: ${this.count} chunks, ${this.size} bytes\n`);
        callback();
    }
}

// 3. 构建管道
const pipeline = fs.createReadStream('./input.txt')
    .pipe(new FilterTransform(chunk => chunk.length > 0))
    .pipe(new StatsTransform())
    .pipe(zlib.createGzip())
    .pipe(fs.createWriteStream('./output.txt.gz'));

pipeline.on('finish', () => {
    console.log('Pipeline completed');
});
```

## 8. 输出结果说明

管道处理的输出结果：

```text
Processed: Data 0
Processed: Data 1
...
Drain event: can continue writing
Pipeline completed
```

**逻辑解析**：
- 管道自动处理数据流转
- 背压自动暂停和恢复数据生产
- `drain` 事件表示可以继续写入

## 9. 使用场景

### 1. 文件处理管道

处理文件的多个步骤：

```ts
// 文件处理管道示例
fs.createReadStream('./input.txt')
    .pipe(transform1)
    .pipe(transform2)
    .pipe(fs.createWriteStream('./output.txt'));
```

### 2. 数据转换链

实现数据转换链：

```ts
// 数据转换链示例
readable
    .pipe(parseTransform)
    .pipe(validateTransform)
    .pipe(processTransform)
    .pipe(writable);
```

### 3. 网络代理

实现网络代理：

```ts
// 网络代理示例
req.pipe(proxyReq);
proxyRes.pipe(res);
```

## 10. 注意事项与常见错误

- **错误处理**：管道中的错误需要分别处理每个流的错误
- **背压理解**：理解背压机制，避免手动处理背压
- **管道断开**：处理管道断开的情况
- **资源清理**：确保管道正确结束，清理资源
- **选项设置**：使用 `{ end: false }` 保持目标流打开

## 11. 常见问题 (FAQ)

**Q: 管道会自动处理背压吗？**
A: 是的，管道会自动处理背压，当目标流缓冲区满时，源流会自动暂停。

**Q: 如何手动处理背压？**
A: 监听 `drain` 事件，当 `write()` 返回 false 时暂停写入，`drain` 事件触发后继续。

**Q: 管道断开后如何重新连接？**
A: 使用 `unpipe()` 断开，然后重新调用 `pipe()` 连接。

## 12. 最佳实践

- **使用管道**：优先使用管道，简化代码
- **错误处理**：为管道中的每个流处理错误
- **背压理解**：理解背压机制，让管道自动处理
- **链式调用**：使用链式调用提高代码可读性
- **资源管理**：确保管道正确结束，清理资源

## 13. 对比分析：管道 vs 手动处理

| 维度             | 管道（pipe）                              | 手动处理                                  |
|:-----------------|:------------------------------------------|:------------------------------------------|
| **代码复杂度**   | 简单                                      | 复杂                                      |
| **背压处理**     | 自动处理                                  | 需要手动处理                              |
| **错误处理**     | 需要分别处理                              | 可以统一处理                              |
| **灵活性**       | 较灵活                                    | 更灵活                                    |
| **推荐使用**     | ✅ 推荐                                   | 特殊场景使用                              |

## 14. 练习任务

1. **管道实践**：
   - 使用管道连接多个流
   - 实现链式管道
   - 处理管道错误

2. **背压实践**：
   - 理解背压机制
   - 观察背压的行为
   - 手动处理背压（如果需要）

3. **实际应用**：
   - 在实际项目中应用管道
   - 实现数据转换管道
   - 处理复杂的数据流

完成以上练习后，继续学习下一章：URL 与查询字符串处理。

## 总结

管道和背压是 Stream 的高级用法：

- **管道**：自动处理数据流转，简化代码
- **背压**：自动处理速度不匹配，避免内存问题
- **最佳实践**：使用管道，理解背压，错误处理

掌握管道和背压有助于高效使用 Stream。

---

**最后更新**：2025-01-XX
