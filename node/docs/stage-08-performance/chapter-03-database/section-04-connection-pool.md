# 8.3.4 连接池优化

## 1. 概述

连接池是管理数据库连接的重要机制，通过复用连接、限制连接数、管理连接生命周期等方式，可以提高数据库性能和资源利用率。

## 2. 连接池配置

### 2.1 基本配置

```ts
import { Pool } from 'pg';

const pool = new Pool({
  host: 'localhost',
  port: 5432,
  database: 'mydb',
  user: 'user',
  password: 'password',
  max: 20,              // 最大连接数
  min: 5,               // 最小连接数
  idleTimeoutMillis: 30000,  // 空闲连接超时
  connectionTimeoutMillis: 2000, // 连接超时
});
```

### 2.2 连接池大小

```ts
// 计算连接池大小
// 公式：连接数 = ((核心数 * 2) + 有效磁盘数)
function calculatePoolSize(): number {
  const cores = require('os').cpus().length;
  const diskCount = 1; // 假设单磁盘
  return (cores * 2) + diskCount;
}

const poolSize = calculatePoolSize();
console.log(`Recommended pool size: ${poolSize}`);
```

## 3. 连接池管理

### 3.1 连接获取

```ts
async function queryWithPool(sql: string, params: any[]): Promise<any> {
  const client = await pool.connect();
  try {
    const result = await client.query(sql, params);
    return result.rows;
  } finally {
    client.release(); // 释放连接
  }
}
```

### 3.2 连接池监控

```ts
class PoolMonitor {
  constructor(private pool: Pool) {}
  
  getStats(): {
    total: number;
    idle: number;
    waiting: number;
  } {
    return {
      total: this.pool.totalCount,
      idle: this.pool.idleCount,
      waiting: this.pool.waitingCount
    };
  }
  
  logStats(): void {
    const stats = this.getStats();
    console.log(`Pool stats: total=${stats.total}, idle=${stats.idle}, waiting=${stats.waiting}`);
  }
}

// 使用
const monitor = new PoolMonitor(pool);
setInterval(() => monitor.logStats(), 5000);
```

## 4. 连接池优化

### 4.1 连接复用

```ts
// 使用连接池复用连接
class DatabaseService {
  constructor(private pool: Pool) {}
  
  async executeQuery<T>(sql: string, params: any[]): Promise<T[]> {
    const client = await this.pool.connect();
    try {
      const result = await client.query(sql, params);
      return result.rows as T[];
    } finally {
      client.release();
    }
  }
}
```

### 4.2 连接超时

```ts
const pool = new Pool({
  // ... 其他配置
  connectionTimeoutMillis: 2000, // 2 秒超时
  idleTimeoutMillis: 30000,       // 30 秒空闲超时
});
```

### 4.3 连接健康检查

```ts
async function checkConnectionHealth(pool: Pool): Promise<boolean> {
  try {
    const client = await pool.connect();
    await client.query('SELECT 1');
    client.release();
    return true;
  } catch (error) {
    return false;
  }
}

// 定期检查
setInterval(async () => {
  const healthy = await checkConnectionHealth(pool);
  if (!healthy) {
    console.error('Database connection unhealthy');
  }
}, 30000);
```

## 5. 最佳实践

### 5.1 连接池配置

- 根据并发量配置大小
- 设置合理的超时时间
- 监控连接使用情况
- 及时释放连接

### 5.2 连接管理

- 使用 try-finally 确保释放
- 避免连接泄漏
- 监控连接池状态
- 处理连接错误

## 6. 注意事项

- **连接泄漏**：确保释放连接
- **连接数限制**：避免过多连接
- **超时设置**：设置合理超时
- **健康检查**：定期检查连接健康

## 7. 常见问题

### 7.1 如何确定连接池大小？

根据并发量、数据库性能、应用需求确定。

### 7.2 如何处理连接泄漏？

使用 try-finally、监控连接数、定期检查。

### 7.3 如何优化连接池性能？

合理配置大小、复用连接、监控使用情况。

## 8. 实践任务

1. **连接池配置**：配置连接池
2. **连接管理**：管理数据库连接
3. **连接监控**：监控连接使用
4. **性能优化**：优化连接池性能
5. **持续维护**：持续维护连接池

---

**下一章**：[8.4 缓存策略](../chapter-04-caching/readme.md)
