# 8.2.3 内存管理

## 1. 概述

内存管理是 Node.js 性能优化的重要方面，通过合理管理内存使用，可以减少内存泄漏、提高应用性能。理解 V8 引擎的内存管理机制对于优化至关重要。

## 2. V8 内存结构

### 2.1 堆内存

```ts
import { memoryUsage } from 'node:process';

interface MemoryInfo {
  rss: number;        // 常驻集大小
  heapTotal: number;  // 堆总大小
  heapUsed: number;   // 堆已使用
  external: number;   // 外部内存
}

function getMemoryInfo(): MemoryInfo {
  return memoryUsage();
}

// 使用
const mem = getMemoryInfo();
console.log(`Heap Used: ${(mem.heapUsed / 1024 / 1024).toFixed(2)} MB`);
```

### 2.2 内存限制

```ts
// 获取内存限制
const v8 = require('v8');
const heapStats = v8.getHeapStatistics();

console.log(`Heap Size Limit: ${(heapStats.heap_size_limit / 1024 / 1024).toFixed(2)} MB`);
```

## 3. 内存优化技巧

### 3.1 及时释放引用

```ts
// 不优化：保持引用
class DataProcessor {
  private cache: Map<string, any> = new Map();
  
  process(data: any): void {
    // 处理数据
    this.cache.set(data.id, data); // 可能造成内存泄漏
  }
}

// 优化：及时清理
class DataProcessorOptimized {
  private cache: Map<string, any> = new Map();
  private maxSize: number = 1000;
  
  process(data: any): void {
    // 处理数据
    this.cache.set(data.id, data);
    
    // 限制缓存大小
    if (this.cache.size > this.maxSize) {
      const firstKey = this.cache.keys().next().value;
      this.cache.delete(firstKey);
    }
  }
  
  clear(): void {
    this.cache.clear();
  }
}
```

### 3.2 使用对象池

```ts
class ObjectPool<T> {
  private pool: T[] = [];
  private createFn: () => T;
  
  constructor(createFn: () => T, initialSize: number = 10) {
    this.createFn = createFn;
    for (let i = 0; i < initialSize; i++) {
      this.pool.push(createFn());
    }
  }
  
  acquire(): T {
    return this.pool.pop() || this.createFn();
  }
  
  release(obj: T): void {
    // 重置对象状态
    this.pool.push(obj);
  }
}

// 使用
const bufferPool = new ObjectPool(() => Buffer.alloc(1024), 10);
const buffer = bufferPool.acquire();
// 使用 buffer
bufferPool.release(buffer);
```

### 3.3 流处理大文件

```ts
import { createReadStream, createWriteStream } from 'node:fs';
import { pipeline } from 'node:stream/promises';

// 不优化：一次性加载
async function processFileBad(filePath: string): Promise<void> {
  const data = await readFile(filePath, 'utf8');
  // 处理数据 - 可能内存溢出
  const processed = processData(data);
  await writeFile('output.txt', processed);
}

// 优化：使用流
async function processFileGood(filePath: string): Promise<void> {
  const readStream = createReadStream(filePath);
  const writeStream = createWriteStream('output.txt');
  
  // 流式处理
  await pipeline(
    readStream,
    transformStream, // 转换流
    writeStream
  );
}
```

## 4. 内存泄漏检测

### 4.1 监控内存使用

```ts
class MemoryMonitor {
  private baseline: NodeJS.MemoryUsage;
  private interval: NodeJS.Timeout | null = null;
  
  constructor() {
    this.baseline = memoryUsage();
  }
  
  start(intervalMs: number = 5000): void {
    this.interval = setInterval(() => {
      const current = memoryUsage();
      const heapUsedDiff = current.heapUsed - this.baseline.heapUsed;
      const heapUsedDiffMB = heapUsedDiff / 1024 / 1024;
      
      if (heapUsedDiffMB > 100) {
        console.warn(`Memory increase: ${heapUsedDiffMB.toFixed(2)} MB`);
      }
    }, intervalMs);
  }
  
  stop(): void {
    if (this.interval) {
      clearInterval(this.interval);
      this.interval = null;
    }
  }
}
```

### 4.2 堆快照

```ts
import { writeHeapSnapshot } from 'node:v8';

function takeHeapSnapshot(prefix: string = 'heap'): string {
  const filename = writeHeapSnapshot(`${prefix}-${Date.now()}.heapsnapshot`);
  console.log(`Heap snapshot written to ${filename}`);
  return filename;
}

// 定期生成快照
setInterval(() => {
  takeHeapSnapshot('periodic');
}, 60000);
```

## 5. 最佳实践

### 5.1 内存管理

- 及时释放不需要的对象
- 使用对象池复用对象
- 使用流处理大文件
- 限制缓存大小

### 5.2 内存监控

- 监控内存使用
- 检测内存泄漏
- 定期生成堆快照
- 分析内存增长

## 6. 注意事项

- **内存泄漏**：避免循环引用、未清理的监听器
- **大对象**：避免创建过大的对象
- **缓存大小**：限制缓存大小
- **流处理**：使用流处理大文件

## 7. 常见问题

### 7.1 如何检测内存泄漏？

使用内存监控、堆快照对比、分析工具。

### 7.2 如何处理大文件？

使用流处理，避免一次性加载。

### 7.3 如何优化内存使用？

及时释放引用、使用对象池、限制缓存大小。

## 8. 实践任务

1. **内存监控**：实现内存监控
2. **内存优化**：优化内存使用
3. **泄漏检测**：检测内存泄漏
4. **流处理**：使用流处理大文件
5. **持续优化**：持续优化内存使用

---

**下一节**：[8.2.4 异步优化](section-04-async.md)
