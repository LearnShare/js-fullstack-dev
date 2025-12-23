# 5.7.3 缓存策略

## 1. 概述

缓存策略决定了何时缓存数据、何时更新缓存、如何处理缓存失效等。合理的缓存策略可以提高应用性能和数据一致性。

## 2. 缓存模式

### 2.1 Cache-Aside（旁路缓存）

**流程**：
1. 查询缓存
2. 缓存未命中，查询数据库
3. 将结果写入缓存
4. 返回结果

**实现**：
```ts
async function getUserById(id: number): Promise<User | null> {
  // 1. 查询缓存
  const cached = await redis.get(`user:${id}`);
  if (cached) {
    return JSON.parse(cached);
  }
  
  // 2. 查询数据库
  const user = await db.query('SELECT * FROM users WHERE id = $1', [id]);
  
  // 3. 写入缓存
  if (user) {
    await redis.setex(`user:${id}`, 3600, JSON.stringify(user));
  }
  
  return user;
}
```

### 2.2 Read-Through（读穿透）

**流程**：
1. 查询缓存
2. 缓存未命中，缓存层查询数据库
3. 将结果写入缓存
4. 返回结果

### 2.3 Write-Through（写穿透）

**流程**：
1. 写入数据库
2. 同时写入缓存
3. 返回结果

**实现**：
```ts
async function updateUser(id: number, data: Partial<User>): Promise<void> {
  // 1. 更新数据库
  await db.query('UPDATE users SET ... WHERE id = $1', [id]);
  
  // 2. 更新缓存
  const user = await getUserById(id);
  if (user) {
    await redis.setex(`user:${id}`, 3600, JSON.stringify(user));
  }
}
```

### 2.4 Write-Back（写回）

**流程**：
1. 写入缓存
2. 异步写入数据库
3. 返回结果

## 3. 缓存更新策略

### 3.1 失效策略

```ts
async function invalidateCache(id: number): Promise<void> {
  await redis.del(`user:${id}`);
}

async function invalidateUserCache(id: number): Promise<void> {
  await redis.del(`user:${id}`);
  await redis.del('users:list'); // 失效列表缓存
}
```

### 3.2 更新策略

```ts
async function updateUserWithCache(id: number, data: Partial<User>): Promise<void> {
  // 更新数据库
  await db.query('UPDATE users SET ... WHERE id = $1', [id]);
  
  // 更新缓存
  const user = await getUserById(id);
  if (user) {
    await redis.setex(`user:${id}`, 3600, JSON.stringify(user));
  }
}
```

## 4. 缓存失效

### 4.1 TTL（Time To Live）

```ts
// 设置过期时间
await redis.setex('key', 3600, 'value');

// 自动过期
await redis.expire('key', 3600);
```

### 4.2 主动失效

```ts
// 数据更新时失效缓存
async function updateUser(id: number, data: Partial<User>): Promise<void> {
  await db.query('UPDATE users SET ... WHERE id = $1', [id]);
  await redis.del(`user:${id}`); // 失效缓存
}
```

## 5. 缓存预热

```ts
async function warmupCache(): Promise<void> {
  const users = await db.query('SELECT * FROM users LIMIT 100');
  for (const user of users) {
    await redis.setex(`user:${user.id}`, 3600, JSON.stringify(user));
  }
}
```

## 6. 最佳实践

### 6.1 策略选择

- **读多写少**：Cache-Aside
- **写多读少**：Write-Through
- **一致性要求高**：Write-Through
- **性能要求高**：Write-Back

### 6.2 缓存设计

- 合理设置过期时间
- 实现缓存失效机制
- 处理缓存穿透
- 处理缓存雪崩

## 7. 注意事项

- **数据一致性**：保证缓存和数据库一致性
- **缓存穿透**：处理缓存未命中
- **缓存雪崩**：避免大量缓存同时失效
- **内存管理**：合理管理缓存内存

## 8. 常见问题

### 8.1 如何选择缓存策略？

根据读写比例、一致性要求、性能需求选择。

### 8.2 如何处理缓存失效？

使用 TTL、主动失效、版本控制。

### 8.3 如何处理缓存穿透？

使用布隆过滤器、缓存空值。

## 9. 实践任务

1. **实现缓存策略**：实现不同的缓存策略
2. **缓存更新**：实现缓存更新机制
3. **缓存失效**：实现缓存失效机制
4. **缓存预热**：实现缓存预热
5. **性能优化**：优化缓存性能

---

**下一节**：[5.7.4 ioredis 客户端](section-04-ioredis.md)
