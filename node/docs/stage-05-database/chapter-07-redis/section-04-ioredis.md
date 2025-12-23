# 5.7.4 ioredis 客户端

## 1. 概述

ioredis 是 Node.js 的 Redis 客户端，提供了完整的 Redis 功能支持、连接池、集群支持等特性。ioredis 是 Node.js 中最流行的 Redis 客户端。

## 2. 安装与初始化

### 2.1 安装

```bash
npm install ioredis
```

### 2.2 基本连接

```ts
import Redis from 'ioredis';

const redis = new Redis({
  host: 'localhost',
  port: 6379,
  password: 'password',
  db: 0
});

redis.on('connect', (): void => {
  console.log('Connected to Redis');
});

redis.on('error', (error: Error): void => {
  console.error('Redis error:', error);
});
```

### 2.3 连接池

```ts
const redis = new Redis({
  host: 'localhost',
  port: 6379,
  maxRetriesPerRequest: 3,
  retryStrategy: (times: number): number => {
    const delay = Math.min(times * 50, 2000);
    return delay;
  }
});
```

## 3. 基本操作

### 3.1 字符串操作

```ts
// 设置
await redis.set('key', 'value');
await redis.setex('key', 3600, 'value');

// 获取
const value = await redis.get('key');

// 批量操作
await redis.mset('key1', 'value1', 'key2', 'value2');
const values = await redis.mget('key1', 'key2');
```

### 3.2 哈希操作

```ts
// 设置
await redis.hset('hash', 'field1', 'value1', 'field2', 'value2');

// 获取
const value = await redis.hget('hash', 'field1');
const all = await redis.hgetall('hash');

// 批量操作
await redis.hmget('hash', 'field1', 'field2');
```

### 3.3 列表操作

```ts
// 添加
await redis.lpush('list', 'item1', 'item2');
await redis.rpush('list', 'item3');

// 获取
const items = await redis.lrange('list', 0, -1);

// 弹出
const item = await redis.lpop('list');
```

## 4. 发布订阅

### 4.1 发布

```ts
const publisher = new Redis();
await publisher.publish('channel', 'message');
```

### 4.2 订阅

```ts
const subscriber = new Redis();

subscriber.subscribe('channel', (err: Error | null, count: number): void => {
  if (err) {
    console.error('Subscribe error:', err);
  } else {
    console.log(`Subscribed to ${count} channels`);
  }
});

subscriber.on('message', (channel: string, message: string): void => {
  console.log(`Received message from ${channel}: ${message}`);
});
```

## 5. 管道和事务

### 5.1 管道

```ts
const pipeline = redis.pipeline();
pipeline.set('key1', 'value1');
pipeline.set('key2', 'value2');
pipeline.get('key1');
const results = await pipeline.exec();
```

### 5.2 事务

```ts
const multi = redis.multi();
multi.set('key1', 'value1');
multi.set('key2', 'value2');
const results = await multi.exec();
```

## 6. 集群支持

```ts
import { Cluster } from 'ioredis';

const cluster = new Cluster([
  { host: '127.0.0.1', port: 7000 },
  { host: '127.0.0.1', port: 7001 },
  { host: '127.0.0.1', port: 7002 }
]);
```

## 7. 最佳实践

### 7.1 连接管理

- 使用单例模式
- 合理设置连接池
- 处理连接错误
- 正确关闭连接

### 7.2 性能优化

- 使用管道批量操作
- 使用合适的数据结构
- 设置合理的过期时间
- 避免大键

## 8. 注意事项

- **连接管理**：合理管理 Redis 连接
- **错误处理**：实现完善的错误处理
- **性能优化**：优化 Redis 操作性能
- **内存管理**：合理管理内存使用

## 9. 常见问题

### 9.1 如何处理连接错误？

实现重连机制和错误处理。

### 9.2 如何优化性能？

使用管道、批量操作、合适的数据结构。

### 9.3 如何实现高可用？

使用集群模式、哨兵模式。

## 10. 实践任务

1. **连接 Redis**：建立 Redis 连接
2. **基本操作**：实现 Redis 基本操作
3. **发布订阅**：实现发布订阅功能
4. **管道事务**：使用管道和事务
5. **性能优化**：优化 Redis 操作性能

---

**下一章**：[5.8 消息队列](../chapter-08-queue/readme.md)
