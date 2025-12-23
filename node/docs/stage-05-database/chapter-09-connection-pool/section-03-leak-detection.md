# 5.9.3 连接泄漏检测

## 1. 概述

连接泄漏是指数据库连接在使用后没有正确释放，导致连接池中的连接被耗尽。连接泄漏会导致应用性能下降甚至崩溃。

## 2. 连接泄漏的原因

### 2.1 常见原因

- **忘记释放连接**：使用连接后忘记释放
- **异常未处理**：异常发生时未释放连接
- **异步操作**：异步操作中连接未正确释放
- **长时间事务**：事务未提交或回滚

### 2.2 泄漏示例

```ts
// ❌ 错误：忘记释放连接
async function badExample(): Promise<void> {
  const client = await pool.connect();
  await client.query('SELECT * FROM users');
  // 忘记 client.release()
}

// ❌ 错误：异常未处理
async function badExample2(): Promise<void> {
  const client = await pool.connect();
  try {
    await client.query('SELECT * FROM users');
  } catch (error) {
    // 异常时未释放连接
    throw error;
  }
}
```

## 3. 连接泄漏检测

### 3.1 监控连接数

```ts
function detectLeaks(): void {
  setInterval((): void => {
    const total = pool.totalCount;
    const idle = pool.idleCount;
    const waiting = pool.waitingCount;
    
    if (total > pool.options.max! * 0.9) {
      console.warn('High connection usage:', { total, idle, waiting });
    }
    
    if (waiting > 0) {
      console.warn('Connections waiting:', waiting);
    }
  }, 5000);
}
```

### 3.2 连接追踪

```ts
import { PoolClient } from 'pg';

const activeConnections = new Map<string, { client: PoolClient; timestamp: number }>();

async function trackedConnect(): Promise<PoolClient> {
  const client = await pool.connect();
  const id = `${Date.now()}-${Math.random()}`;
  
  activeConnections.set(id, {
    client,
    timestamp: Date.now()
  });
  
  // 包装 release 方法
  const originalRelease = client.release.bind(client);
  client.release = (): void => {
    activeConnections.delete(id);
    originalRelease();
  };
  
  return client;
}

function checkLeaks(): void {
  const now = Date.now();
  const timeout = 60000; // 1 分钟
  
  for (const [id, { timestamp }] of activeConnections.entries()) {
    if (now - timestamp > timeout) {
      console.error(`Potential leak detected: connection ${id} active for ${now - timestamp}ms`);
    }
  }
}
```

## 4. 预防连接泄漏

### 4.1 使用 try-finally

```ts
async function safeExample(): Promise<void> {
  const client = await pool.connect();
  try {
    await client.query('SELECT * FROM users');
  } finally {
    client.release(); // 确保释放
  }
}
```

### 4.2 使用辅助函数

```ts
async function withConnection<T>(
  callback: (client: PoolClient) => Promise<T>
): Promise<T> {
  const client = await pool.connect();
  try {
    return await callback(client);
  } finally {
    client.release();
  }
}

// 使用
await withConnection(async (client: PoolClient): Promise<void> => {
  await client.query('SELECT * FROM users');
});
```

### 4.3 使用事务辅助函数

```ts
async function withTransaction<T>(
  callback: (client: PoolClient) => Promise<T>
): Promise<T> {
  const client = await pool.connect();
  try {
    await client.query('BEGIN');
    const result = await callback(client);
    await client.query('COMMIT');
    return result;
  } catch (error) {
    await client.query('ROLLBACK');
    throw error;
  } finally {
    client.release();
  }
}
```

## 5. 自动检测工具

### 5.1 连接池包装

```ts
class MonitoredPool {
  private pool: Pool;
  private activeConnections: Map<string, number> = new Map();
  
  constructor(pool: Pool) {
    this.pool = pool;
    this.startMonitoring();
  }
  
  async connect(): Promise<PoolClient> {
    const client = await this.pool.connect();
    const id = `${Date.now()}-${Math.random()}`;
    this.activeConnections.set(id, Date.now());
    
    const originalRelease = client.release.bind(client);
    client.release = (): void => {
      this.activeConnections.delete(id);
      originalRelease();
    };
    
    return client;
  }
  
  private startMonitoring(): void {
    setInterval((): void => {
      const now = Date.now();
      for (const [id, timestamp] of this.activeConnections.entries()) {
        if (now - timestamp > 60000) {
          console.error(`Leak detected: connection ${id} active for ${now - timestamp}ms`);
        }
      }
    }, 10000);
  }
}
```

## 6. 最佳实践

### 6.1 预防措施

- 使用 try-finally 确保释放
- 使用辅助函数封装连接使用
- 实现连接追踪
- 监控连接使用

### 6.2 检测措施

- 监控连接池状态
- 实现连接泄漏检测
- 记录长时间连接
- 告警机制

## 7. 注意事项

- **及时释放**：使用完连接立即释放
- **异常处理**：确保异常时也释放连接
- **监控**：监控连接使用情况
- **告警**：实现连接泄漏告警

## 8. 常见问题

### 8.1 如何检测连接泄漏？

监控连接池状态，追踪连接使用时间。

### 8.2 如何预防连接泄漏？

使用 try-finally、辅助函数、连接追踪。

### 8.3 如何处理已泄漏的连接？

实现连接超时自动释放，重启应用。

## 9. 实践任务

1. **检测泄漏**：实现连接泄漏检测
2. **预防泄漏**：使用辅助函数预防泄漏
3. **监控连接**：实现连接使用监控
4. **告警机制**：实现连接泄漏告警
5. **最佳实践**：遵循连接管理最佳实践

---

**下一章**：[5.10 数据库备份与恢复](../chapter-10-backup/readme.md)
