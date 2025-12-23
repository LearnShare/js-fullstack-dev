# 8.4.2 缓存模式（Cache-Aside、Write-Through）

## 1. 概述

缓存模式定义了缓存和数据库之间的交互方式，不同的缓存模式适用于不同的场景。理解各种缓存模式对于设计高效的缓存系统至关重要。

## 2. Cache-Aside（旁路缓存）

### 2.1 工作原理

```
读取：
1. 先查缓存
2. 缓存未命中，查数据库
3. 将结果写入缓存
4. 返回结果

写入：
1. 写入数据库
2. 删除缓存（或更新缓存）
```

### 2.2 实现

```ts
class CacheAsideService {
  constructor(
    private cache: Redis,
    private db: Database
  ) {}
  
  async get(key: string): Promise<any> {
    // 1. 先查缓存
    const cached = await this.cache.get(key);
    if (cached) {
      return JSON.parse(cached);
    }
    
    // 2. 缓存未命中，查数据库
    const data = await this.db.query('SELECT * FROM users WHERE id = $1', [key]);
    
    if (data.length > 0) {
      // 3. 写入缓存
      await this.cache.setex(key, 3600, JSON.stringify(data[0]));
      return data[0];
    }
    
    return null;
  }
  
  async set(key: string, value: any): Promise<void> {
    // 1. 写入数据库
    await this.db.query('UPDATE users SET ... WHERE id = $1', [key]);
    
    // 2. 删除缓存
    await this.cache.del(key);
  }
}
```

### 2.3 优缺点

**优点**：
- 实现简单
- 缓存未命中不影响数据库
- 灵活控制缓存

**缺点**：
- 可能出现缓存不一致
- 需要处理缓存失效

## 3. Write-Through（写透）

### 3.1 工作原理

```
写入：
1. 写入缓存
2. 写入数据库
3. 返回结果

读取：
1. 从缓存读取
2. 缓存未命中，查数据库并写入缓存
```

### 3.2 实现

```ts
class WriteThroughService {
  constructor(
    private cache: Redis,
    private db: Database
  ) {}
  
  async set(key: string, value: any): Promise<void> {
    // 1. 写入缓存
    await this.cache.setex(key, 3600, JSON.stringify(value));
    
    // 2. 写入数据库
    await this.db.query('UPDATE users SET ... WHERE id = $1', [key]);
  }
  
  async get(key: string): Promise<any> {
    // 从缓存读取
    const cached = await this.cache.get(key);
    if (cached) {
      return JSON.parse(cached);
    }
    
    // 缓存未命中，查数据库
    const data = await this.db.query('SELECT * FROM users WHERE id = $1', [key]);
    if (data.length > 0) {
      await this.cache.setex(key, 3600, JSON.stringify(data[0]));
      return data[0];
    }
    
    return null;
  }
}
```

### 3.3 优缺点

**优点**：
- 数据一致性高
- 缓存总是最新

**缺点**：
- 写入延迟较高
- 缓存和数据库都要写入

## 4. Write-Back（写回）

### 4.1 工作原理

```
写入：
1. 只写入缓存
2. 异步批量写入数据库

读取：
1. 从缓存读取
```

### 4.2 实现

```ts
class WriteBackService {
  private writeQueue: Array<{ key: string; value: any }> = [];
  
  constructor(
    private cache: Redis,
    private db: Database
  ) {
    // 定期批量写入数据库
    setInterval(() => this.flush(), 5000);
  }
  
  async set(key: string, value: any): Promise<void> {
    // 只写入缓存
    await this.cache.setex(key, 3600, JSON.stringify(value));
    
    // 加入写入队列
    this.writeQueue.push({ key, value });
  }
  
  private async flush(): Promise<void> {
    if (this.writeQueue.length === 0) return;
    
    const batch = this.writeQueue.splice(0, 100);
    await Promise.all(
      batch.map(({ key, value }) => 
        this.db.query('UPDATE users SET ... WHERE id = $1', [key])
      )
    );
  }
}
```

## 5. 模式选择

### 5.1 选择建议

- **读多写少**：使用 Cache-Aside
- **写多读少**：使用 Write-Through
- **高一致性要求**：使用 Write-Through
- **高写入性能要求**：使用 Write-Back

## 6. 最佳实践

### 6.1 模式设计

- 根据场景选择模式
- 处理缓存失效
- 保证数据一致性
- 监控缓存性能

### 6.2 实现技巧

- 使用事务保证一致性
- 实现重试机制
- 处理并发更新
- 优化缓存键设计

## 7. 注意事项

- **数据一致性**：保证缓存和数据库一致
- **缓存失效**：处理缓存失效场景
- **并发控制**：处理并发读写
- **错误处理**：处理缓存和数据库错误

## 8. 常见问题

### 8.1 如何选择缓存模式？

根据读写比例、一致性要求、性能要求选择。

### 8.2 如何处理缓存不一致？

使用 Write-Through、版本控制、定期刷新。

### 8.3 如何优化缓存性能？

选择合适的模式、优化缓存键、提高命中率。

## 9. 实践任务

1. **实现模式**：实现不同的缓存模式
2. **性能测试**：测试不同模式的性能
3. **一致性保证**：保证数据一致性
4. **错误处理**：处理各种错误场景
5. **持续优化**：持续优化缓存性能

---

**下一节**：[8.4.3 Redis 缓存实现](section-03-redis.md)
