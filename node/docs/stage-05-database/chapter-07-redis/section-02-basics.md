# 5.7.2 Redis 基础

## 1. 概述

Redis 支持多种数据结构，包括字符串、列表、集合、有序集合、哈希等。理解这些数据结构是使用 Redis 的基础。

## 2. 数据结构

### 2.1 字符串（String）

```ts
import Redis from 'ioredis';

const redis = new Redis();

// 设置
await redis.set('key', 'value');
await redis.set('key', 'value', 'EX', 3600); // 设置过期时间

// 获取
const value = await redis.get('key');

// 递增
await redis.incr('counter');
await redis.incrby('counter', 10);
```

### 2.2 列表（List）

```ts
// 添加
await redis.lpush('list', 'item1', 'item2');
await redis.rpush('list', 'item3');

// 获取
const items = await redis.lrange('list', 0, -1);

// 弹出
const item = await redis.lpop('list');
```

### 2.3 集合（Set）

```ts
// 添加
await redis.sadd('set', 'member1', 'member2');

// 获取
const members = await redis.smembers('set');

// 检查成员
const exists = await redis.sismember('set', 'member1');
```

### 2.4 有序集合（Sorted Set）

```ts
// 添加
await redis.zadd('sorted-set', 100, 'member1', 200, 'member2');

// 获取
const members = await redis.zrange('sorted-set', 0, -1, 'WITHSCORES');

// 获取排名
const rank = await redis.zrank('sorted-set', 'member1');
```

### 2.5 哈希（Hash）

```ts
// 设置
await redis.hset('hash', 'field1', 'value1', 'field2', 'value2');

// 获取
const value = await redis.hget('hash', 'field1');
const all = await redis.hgetall('hash');
```

## 3. 过期和删除

### 3.1 过期时间

```ts
// 设置过期时间
await redis.expire('key', 3600);
await redis.setex('key', 3600, 'value');

// 获取剩余时间
const ttl = await redis.ttl('key');
```

### 3.2 删除

```ts
// 删除键
await redis.del('key');

// 批量删除
await redis.del('key1', 'key2', 'key3');
```

## 4. 管道和事务

### 4.1 管道

```ts
const pipeline = redis.pipeline();
pipeline.set('key1', 'value1');
pipeline.set('key2', 'value2');
pipeline.get('key1');
const results = await pipeline.exec();
```

### 4.2 事务

```ts
const multi = redis.multi();
multi.set('key1', 'value1');
multi.set('key2', 'value2');
const results = await multi.exec();
```

## 5. 最佳实践

### 5.1 连接管理

- 使用连接池
- 合理设置连接数
- 处理连接错误
- 关闭连接

### 5.2 性能优化

- 使用管道批量操作
- 使用合适的数据结构
- 设置合理的过期时间
- 避免大键

## 6. 注意事项

- **内存管理**：合理管理内存使用
- **过期时间**：设置合理的过期时间
- **数据结构选择**：根据场景选择合适的数据结构
- **错误处理**：实现完善的错误处理

## 7. 常见问题

### 7.1 如何选择数据结构？

根据数据特点和操作需求选择。

### 7.2 如何处理过期数据？

设置合理的过期时间，使用定期清理。

### 7.3 如何优化性能？

使用管道、批量操作、合适的数据结构。

## 8. 实践任务

1. **基本操作**：实现 Redis 基本操作
2. **数据结构**：使用不同的数据结构
3. **过期管理**：实现过期时间管理
4. **管道事务**：使用管道和事务
5. **性能优化**：优化 Redis 操作性能

---

**下一节**：[5.7.3 缓存策略](section-03-strategies.md)
