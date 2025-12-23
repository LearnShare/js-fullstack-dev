# 4.8.3 bottleneck

## 1. 概述

bottleneck 是一个功能强大的限流和任务调度库，支持多种限流算法、优先级队列、任务重试等功能。bottleneck 不仅适用于 API 限流，还适用于任何需要控制执行速率的场景。

## 2. 特性说明

- **多种限流算法**：支持固定窗口、滑动窗口等
- **优先级队列**：支持任务优先级
- **任务重试**：支持自动重试
- **集群支持**：支持多进程/多服务器
- **TypeScript 支持**：提供类型定义

## 3. 安装与初始化

### 3.1 安装

```bash
npm install bottleneck
```

### 3.2 基本使用

```ts
import Bottleneck from 'bottleneck';

const limiter = new Bottleneck({
  maxConcurrent: 5, // 最大并发数
  minTime: 1000 // 最小间隔：1 秒
});

async function makeRequest(url: string): Promise<Response> {
  return await limiter.schedule(async (): Promise<Response> => {
    return await fetch(url);
  });
}
```

## 4. 限流配置

### 4.1 速率限制

```ts
const limiter = new Bottleneck({
  reservoir: 100, // 初始令牌数
  reservoirRefreshAmount: 100, // 每次刷新数量
  reservoirRefreshInterval: 60 * 1000, // 刷新间隔：1 分钟
  maxConcurrent: 5, // 最大并发数
  minTime: 100 // 最小间隔：100ms
});
```

### 4.2 并发限制

```ts
const limiter = new Bottleneck({
  maxConcurrent: 10, // 最多同时执行 10 个任务
  minTime: 0 // 无最小间隔限制
});
```

### 4.3 时间窗口限制

```ts
const limiter = new Bottleneck({
  reservoir: 100, // 窗口内允许的请求数
  reservoirRefreshAmount: 100,
  reservoirRefreshInterval: 15 * 60 * 1000 // 15 分钟窗口
});
```

## 5. 任务调度

### 5.1 基本调度

```ts
const limiter = new Bottleneck({
  maxConcurrent: 5,
  minTime: 1000
});

// 调度任务
const job = limiter.schedule(async (): Promise<string> => {
  return 'Task completed';
});

const result = await job;
console.log(result);
```

### 5.2 优先级调度

```ts
const limiter = new Bottleneck({
  maxConcurrent: 5,
  minTime: 1000
});

// 高优先级任务
limiter.schedule({ priority: 1 }, async (): Promise<void> => {
  console.log('High priority task');
});

// 低优先级任务
limiter.schedule({ priority: 5 }, async (): Promise<void> => {
  console.log('Low priority task');
});
```

### 5.3 任务取消

```ts
const job = limiter.schedule(async (): Promise<string> => {
  await new Promise((resolve) => setTimeout(resolve, 5000));
  return 'Task completed';
});

// 取消任务
job.cancel();
```

## 6. 事件监听

### 6.1 事件处理

```ts
const limiter = new Bottleneck({
  maxConcurrent: 5,
  minTime: 1000
});

limiter.on('error', (error: Error): void => {
  console.error('Limiter error:', error);
});

limiter.on('depleted', (): void => {
  console.log('Reservoir depleted');
});

limiter.on('empty', (): void => {
  console.log('Queue empty');
});

limiter.on('idle', (): void => {
  console.log('Limiter idle');
});
```

## 7. 集群支持

### 7.1 Redis 集群

```bash
npm install ioredis
```

```ts
import Bottleneck from 'bottleneck';
import Redis from 'ioredis';

const connection = new Redis({
  host: process.env.REDIS_HOST,
  port: parseInt(process.env.REDIS_PORT || '6379')
});

const limiter = new Bottleneck({
  id: 'my-limiter',
  datastore: 'ioredis',
  clearDatastore: false,
  connection,
  maxConcurrent: 5,
  minTime: 1000
});
```

## 8. 与 Express 集成

### 8.1 Express 中间件

```ts
import express, { Express, Request, Response, NextFunction } from 'express';
import Bottleneck from 'bottleneck';

const app: Express = express();

const limiter = new Bottleneck({
  maxConcurrent: 10,
  minTime: 100
});

function rateLimitMiddleware(limiter: Bottleneck) {
  return async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    try {
      await limiter.schedule(async (): Promise<void> => {
        next();
      });
    } catch (error) {
      res.status(429).json({ error: 'Too many requests' });
    }
  };
}

app.use('/api/', rateLimitMiddleware(limiter));
```

## 9. 最佳实践

### 9.1 不同场景的限流

```ts
// API 调用限流
const apiLimiter = new Bottleneck({
  maxConcurrent: 5,
  minTime: 200
});

// 数据库操作限流
const dbLimiter = new Bottleneck({
  maxConcurrent: 10,
  minTime: 100
});

// 外部服务调用限流
const externalLimiter = new Bottleneck({
  maxConcurrent: 3,
  minTime: 1000
});
```

### 9.2 任务重试

```ts
const limiter = new Bottleneck({
  maxConcurrent: 5,
  minTime: 1000
});

async function makeRequestWithRetry(url: string, retries: number = 3): Promise<Response> {
  for (let i = 0; i < retries; i++) {
    try {
      return await limiter.schedule(async (): Promise<Response> => {
        return await fetch(url);
      });
    } catch (error) {
      if (i === retries - 1) throw error;
      await new Promise((resolve) => setTimeout(resolve, 1000 * (i + 1)));
    }
  }
  throw new Error('Max retries exceeded');
}
```

## 10. 注意事项

- **内存使用**：注意任务队列的内存使用
- **错误处理**：实现完善的错误处理机制
- **监控**：监控限流效果和任务执行情况
- **性能**：优化限流配置以提升性能

## 11. 常见问题

### 11.1 bottleneck 和 express-rate-limit 的区别？

bottleneck 更灵活，支持更多功能；express-rate-limit 更简单，专为 Express 设计。

### 11.2 如何处理任务失败？

使用 try-catch 和重试机制处理任务失败。

### 11.3 如何实现动态限流？

使用事件监听和动态配置实现动态限流。

## 12. 实践任务

1. **实现基本限流**：使用 bottleneck 实现基本限流功能
2. **实现优先级调度**：实现任务优先级调度
3. **集成 Redis**：使用 Redis 实现集群限流
4. **实现任务重试**：实现任务自动重试机制
5. **监控限流**：实现限流监控和统计

---

**下一节**：[4.8.4 限流策略](section-04-strategies.md)
