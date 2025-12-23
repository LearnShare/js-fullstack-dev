# 5.9.2 连接池配置

## 1. 概述

连接池配置决定了连接池的行为和性能。合理的配置可以提高应用性能和稳定性。

## 2. PostgreSQL 连接池配置

### 2.1 基本配置

```ts
import { Pool, PoolConfig } from 'pg';

const config: PoolConfig = {
  host: 'localhost',
  port: 5432,
  database: 'mydb',
  user: 'postgres',
  password: 'password',
  max: 20,                    // 最大连接数
  min: 5,                     // 最小连接数
  idleTimeoutMillis: 30000,   // 空闲连接超时（30秒）
  connectionTimeoutMillis: 2000, // 获取连接超时（2秒）
  statement_timeout: 5000,     // 语句超时（5秒）
  query_timeout: 10000        // 查询超时（10秒）
};

const pool = new Pool(config);
```

### 2.2 高级配置

```ts
const config: PoolConfig = {
  // ... 基本配置
  allowExitOnIdle: true,      // 空闲时允许退出
  application_name: 'my-app', // 应用名称
  keepAlive: true,            // 保持连接活跃
  keepAliveInitialDelayMillis: 10000
};
```

## 3. MySQL 连接池配置

### 3.1 基本配置

```ts
import { createPool, PoolOptions } from 'mysql2/promise';

const config: PoolOptions = {
  host: 'localhost',
  port: 3306,
  database: 'mydb',
  user: 'root',
  password: 'password',
  connectionLimit: 10,         // 最大连接数
  queueLimit: 0,              // 队列限制（0表示无限制）
  acquireTimeout: 60000,       // 获取连接超时（60秒）
  timeout: 60000,              // 查询超时（60秒）
  reconnect: true              // 自动重连
};

const pool = createPool(config);
```

## 4. 连接池监控

### 4.1 监控连接状态

```ts
// PostgreSQL
pool.on('connect', (client): void => {
  console.log('New client connected');
});

pool.on('error', (err: Error, client): void => {
  console.error('Unexpected error on idle client', err);
});

// 获取连接池统计
console.log('Total clients:', pool.totalCount);
console.log('Idle clients:', pool.idleCount);
console.log('Waiting clients:', pool.waitingCount);
```

### 4.2 监控连接使用

```ts
function monitorPool(): void {
  setInterval((): void => {
    console.log({
      total: pool.totalCount,
      idle: pool.idleCount,
      waiting: pool.waitingCount
    });
  }, 5000);
}
```

## 5. 配置优化

### 5.1 连接数计算

```ts
// 根据 CPU 核心数和应用负载计算
const maxConnections = Math.min(
  os.cpus().length * 2 + 1,  // CPU 核心数 * 2 + 1
  20                          // 最大不超过 20
);
```

### 5.2 超时设置

```ts
// 根据业务需求设置超时
const config = {
  connectionTimeoutMillis: 2000,  // 快速失败
  idleTimeoutMillis: 30000,       // 合理回收空闲连接
  statement_timeout: 5000         // 防止长时间查询
};
```

## 6. 最佳实践

### 6.1 配置原则

- 根据应用负载设置连接数
- 设置合理的超时时间
- 监控连接池状态
- 处理连接错误

### 6.2 性能优化

- 合理设置连接数
- 使用连接复用
- 避免连接泄漏
- 监控连接使用

## 7. 注意事项

- **连接数限制**：注意数据库服务器的最大连接数
- **资源消耗**：每个连接消耗资源
- **超时设置**：设置合理的超时时间
- **监控**：监控连接池状态

## 8. 常见问题

### 8.1 如何设置最大连接数？

根据应用负载、数据库性能、服务器资源设置。

### 8.2 如何处理连接超时？

设置合理的超时时间，实现重试机制。

### 8.3 如何优化连接池？

合理设置连接数，使用连接复用，监控连接使用。

## 9. 实践任务

1. **配置连接池**：配置数据库连接池
2. **监控连接**：实现连接池监控
3. **优化配置**：优化连接池配置
4. **错误处理**：实现连接错误处理
5. **性能测试**：测试连接池性能

---

**下一节**：[5.9.3 连接泄漏检测](section-03-leak-detection.md)
