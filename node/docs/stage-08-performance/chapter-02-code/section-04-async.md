# 8.2.4 异步优化

## 1. 概述

异步优化是 Node.js 性能优化的关键，通过合理使用异步操作、并行处理、避免阻塞等方式，可以显著提高应用性能和并发能力。

## 2. 并行处理

### 2.1 Promise.all

```ts
// 不优化：串行处理
async function fetchDataSerial(urls: string[]): Promise<any[]> {
  const results: any[] = [];
  for (const url of urls) {
    const data = await fetch(url);
    results.push(await data.json());
  }
  return results;
}

// 优化：并行处理
async function fetchDataParallel(urls: string[]): Promise<any[]> {
  const promises = urls.map(async (url) => {
    const response = await fetch(url);
    return response.json();
  });
  return Promise.all(promises);
}
```

### 2.2 Promise.allSettled

```ts
// 处理多个异步操作，即使部分失败
async function fetchMultiple(urls: string[]): Promise<any[]> {
  const promises = urls.map(url => fetch(url).then(r => r.json()).catch(err => ({ error: err.message })));
  const results = await Promise.allSettled(promises);
  return results.map(r => r.status === 'fulfilled' ? r.value : { error: 'Failed' });
}
```

### 2.3 并发控制

```ts
class ConcurrencyLimiter {
  private running: number = 0;
  private queue: Array<() => Promise<any>> = [];
  
  constructor(private limit: number) {}
  
  async execute<T>(fn: () => Promise<T>): Promise<T> {
    return new Promise((resolve, reject) => {
      this.queue.push(async () => {
        try {
          const result = await fn();
          resolve(result);
        } catch (error) {
          reject(error);
        }
      });
      this.process();
    });
  }
  
  private async process(): void {
    if (this.running >= this.limit || this.queue.length === 0) {
      return;
    }
    
    this.running++;
    const task = this.queue.shift()!;
    
    try {
      await task();
    } finally {
      this.running--;
      this.process();
    }
  }
}

// 使用
const limiter = new ConcurrencyLimiter(5);
const results = await Promise.all(
  urls.map(url => limiter.execute(() => fetch(url)))
);
```

## 3. 避免阻塞

### 3.1 使用异步 I/O

```ts
// 不优化：同步 I/O
import { readFileSync } from 'node:fs';

function processFileSync(filePath: string): string {
  const data = readFileSync(filePath, 'utf8');
  return processData(data); // 阻塞
}

// 优化：异步 I/O
import { readFile } from 'node:fs/promises';

async function processFileAsync(filePath: string): Promise<string> {
  const data = await readFile(filePath, 'utf8');
  return processData(data); // 非阻塞
}
```

### 3.2 使用 Worker Threads

```ts
import { Worker } from 'node:worker_threads';

function runInWorker(code: string): Promise<any> {
  return new Promise((resolve, reject) => {
    const worker = new Worker(code, { eval: true });
    worker.on('message', resolve);
    worker.on('error', reject);
  });
}

// 使用
const result = await runInWorker(`
  const { parentPort } = require('worker_threads');
  // 执行 CPU 密集型任务
  const result = heavyComputation();
  parentPort.postMessage(result);
`);
```

## 4. 缓存异步结果

### 4.1 异步缓存

```ts
class AsyncCache<K, V> {
  private cache: Map<K, Promise<V>> = new Map();
  
  async get(key: K, fetcher: () => Promise<V>): Promise<V> {
    if (this.cache.has(key)) {
      return this.cache.get(key)!;
    }
    
    const promise = fetcher();
    this.cache.set(key, promise);
    
    // 错误时移除
    promise.catch(() => {
      this.cache.delete(key);
    });
    
    return promise;
  }
  
  clear(): void {
    this.cache.clear();
  }
}

// 使用
const cache = new AsyncCache<string, any>();

const data = await cache.get('key', async () => {
  return await fetchData();
});
```

## 5. 最佳实践

### 5.1 异步优化

- 使用并行处理
- 避免阻塞操作
- 控制并发数量
- 缓存异步结果

### 5.2 错误处理

- 正确处理异步错误
- 使用 Promise.allSettled
- 实现重试机制
- 记录错误日志

## 6. 注意事项

- **并发控制**：避免过多并发
- **错误处理**：正确处理异步错误
- **资源清理**：及时清理资源
- **性能监控**：监控异步操作性能

## 7. 常见问题

### 7.1 如何处理大量并发请求？

使用并发限制器、分批处理、使用队列。

### 7.2 如何优化异步操作？

使用并行处理、避免阻塞、缓存结果。

### 7.3 如何处理异步错误？

使用 try-catch、Promise.catch、错误边界。

## 8. 实践任务

1. **并行处理**：实现并行处理
2. **并发控制**：实现并发控制
3. **异步缓存**：实现异步缓存
4. **错误处理**：处理异步错误
5. **性能优化**：优化异步操作

---

**下一章**：[8.3 数据库优化](../chapter-03-database/readme.md)
