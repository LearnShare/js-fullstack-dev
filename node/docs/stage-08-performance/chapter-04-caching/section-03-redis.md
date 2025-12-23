# 8.4.3 Redis 缓存实现

## 1. 概述

Redis 是高性能的内存数据库，广泛用于缓存实现。本章介绍如何使用 Redis 在 Node.js 中实现缓存功能。

## 2. Redis 安装与配置

### 2.1 安装

```bash
npm install ioredis
npm install -D @types/ioredis
```

### 2.2 基本配置

```ts
import Redis from 'ioredis';

const redis = new Redis({
  host: 'localhost',
  port: 6379,
  password: 'password',
  db: 0,
  retryStrategy: (times: number): number => {
    const delay = Math.min(times * 50, 2000);
    return delay;
  }
});
```

## 3. 基本操作

### 3.1 字符串操作

```ts
// 设置值
await redis.set('key', 'value');
await redis.setex('key', 3600, 'value'); // 带过期时间

// 获取值
const value = await redis.get('key');

// 删除值
await redis.del('key');

// 检查存在
const exists = await redis.exists('key');
```

### 3.2 哈希操作

```ts
// 设置哈希
await redis.hset('user:1', 'name', 'John');
await redis.hset('user:1', 'email', 'john@example.com');

// 获取哈希
const name = await redis.hget('user:1', 'name');
const user = await redis.hgetall('user:1');

// 删除哈希字段
await redis.hdel('user:1', 'email');
```

### 3.3 列表操作

```ts
// 添加元素
await redis.lpush('list', 'item1');
await redis.rpush('list', 'item2');

// 获取元素
const items = await redis.lrange('list', 0, -1);

// 删除元素
await redis.lrem('list', 1, 'item1');
```

## 4. 缓存实现

### 4.1 简单缓存

```ts
class SimpleCache {
  constructor(private redis: Redis) {}
  
  async get<T>(key: string): Promise<T | null> {
    const value = await this.redis.get(key);
    return value ? JSON.parse(value) : null;
  }
  
  async set(key: string, value: any, ttl: number = 3600): Promise<void> {
    await this.redis.setex(key, ttl, JSON.stringify(value));
  }
  
  async del(key: string): Promise<void> {
    await this.redis.del(key);
  }
  
  async exists(key: string): Promise<boolean> {
    return (await this.redis.exists(key)) === 1;
  }
}
```

### 4.2 缓存装饰器

```ts
function cached(ttl: number = 3600) {
  return function (target: any, propertyName: string, descriptor: PropertyDescriptor): void {
    const method = descriptor.value;
    const cache = new SimpleCache(redis);
    
    descriptor.value = async function (...args: any[]): Promise<any> {
      const cacheKey = `${target.constructor.name}:${propertyName}:${JSON.stringify(args)}`;
      
      // 先查缓存
      const cached = await cache.get(cacheKey);
      if (cached !== null) {
        return cached;
      }
      
      // 执行方法
      const result = await method.apply(this, args);
      
      // 写入缓存
      await cache.set(cacheKey, result, ttl);
      
      return result;
    };
  };
}

// 使用
class UserService {
  @cached(3600)
  async getUser(id: number): Promise<User> {
    return await db.query('SELECT * FROM users WHERE id = $1', [id]);
  }
}
```

## 5. 缓存策略实现

### 5.1 Cache-Aside 实现

```ts
class CacheAsideService {
  constructor(
    private cache: SimpleCache,
    private db: Database
  ) {}
  
  async getUser(id: number): Promise<User | null> {
    const cacheKey = `user:${id}`;
    
    // 1. 查缓存
    const cached = await this.cache.get<User>(cacheKey);
    if (cached) {
      return cached;
    }
    
    // 2. 查数据库
    const user = await this.db.query('SELECT * FROM users WHERE id = $1', [id]);
    
    if (user.length > 0) {
      // 3. 写入缓存
      await this.cache.set(cacheKey, user[0], 3600);
      return user[0];
    }
    
    return null;
  }
  
  async updateUser(id: number, data: Partial<User>): Promise<void> {
    // 1. 更新数据库
    await this.db.query('UPDATE users SET ... WHERE id = $1', [id]);
    
    // 2. 删除缓存
    await this.cache.del(`user:${id}`);
  }
}
```

## 6. 缓存优化

### 6.1 批量操作

```ts
class BatchCache {
  constructor(private redis: Redis) {}
  
  async mget(keys: string[]): Promise<(string | null)[]> {
    return await this.redis.mget(...keys);
  }
  
  async mset(keyValues: Record<string, any>, ttl: number = 3600): Promise<void> {
    const pipeline = this.redis.pipeline();
    for (const [key, value] of Object.entries(keyValues)) {
      pipeline.setex(key, ttl, JSON.stringify(value));
    }
    await pipeline.exec();
  }
}
```

### 6.2 缓存预热

```ts
async function warmupCache(): Promise<void> {
  const cache = new SimpleCache(redis);
  const db = new Database();
  
  // 加载热点数据
  const hotUsers = await db.query('SELECT * FROM users WHERE active = true LIMIT 100');
  
  for (const user of hotUsers) {
    await cache.set(`user:${user.id}`, user, 3600);
  }
}
```

## 7. 最佳实践

### 7.1 键设计

- 使用有意义的键名
- 使用命名空间
- 包含版本信息
- 保持键简洁

### 7.2 过期时间

- 设置合理过期时间
- 根据数据特性设置
- 使用随机过期时间避免雪崩

## 8. 注意事项

- **内存管理**：监控 Redis 内存使用
- **连接管理**：使用连接池
- **错误处理**：处理 Redis 错误
- **性能监控**：监控缓存命中率

## 9. 常见问题

### 9.1 如何处理缓存穿透？

使用布隆过滤器、缓存空值、限制查询。

### 9.2 如何处理缓存雪崩？

使用随机过期时间、多级缓存、限流。

### 9.3 如何优化 Redis 性能？

使用管道、批量操作、合理数据结构。

## 10. 实践任务

1. **Redis 配置**：配置 Redis 连接
2. **缓存实现**：实现缓存功能
3. **缓存策略**：实现缓存策略
4. **性能优化**：优化缓存性能
5. **监控告警**：监控缓存使用

---

**下一节**：[8.4.4 CDN 与静态资源缓存](section-04-cdn.md)
