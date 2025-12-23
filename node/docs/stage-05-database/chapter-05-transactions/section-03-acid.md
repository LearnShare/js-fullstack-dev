# 5.5.3 ACID 特性

## 1. 概述

ACID 是事务的四个基本特性，保证数据库操作的可靠性和一致性。理解 ACID 特性对于正确使用事务至关重要。

## 2. ACID 特性

### 2.1 原子性（Atomicity）

**定义**：事务中的所有操作要么全部执行成功，要么全部不执行。

**实现**：
- 使用事务控制语句
- 实现回滚机制
- 保证操作原子性

**示例**：
```ts
async function atomicOperation(): Promise<void> {
  const client = await pool.connect();
  try {
    await client.query('BEGIN');
    
    await client.query('UPDATE accounts SET balance = balance - 100 WHERE id = 1');
    await client.query('UPDATE accounts SET balance = balance + 100 WHERE id = 2');
    
    await client.query('COMMIT');
  } catch (error) {
    await client.query('ROLLBACK'); // 全部回滚
    throw error;
  } finally {
    client.release();
  }
}
```

### 2.2 一致性（Consistency）

**定义**：事务执行前后数据库保持一致状态。

**实现**：
- 使用约束保证数据完整性
- 验证业务规则
- 保证数据一致性

**示例**：
```ts
async function consistentOperation(): Promise<void> {
  const client = await pool.connect();
  try {
    await client.query('BEGIN');
    
    // 检查约束
    const result = await client.query('SELECT balance FROM accounts WHERE id = 1');
    if (result.rows[0].balance < 100) {
      throw new Error('Insufficient balance');
    }
    
    await client.query('UPDATE accounts SET balance = balance - 100 WHERE id = 1');
    await client.query('UPDATE accounts SET balance = balance + 100 WHERE id = 2');
    
    await client.query('COMMIT');
  } catch (error) {
    await client.query('ROLLBACK');
    throw error;
  } finally {
    client.release();
  }
}
```

### 2.3 隔离性（Isolation）

**定义**：并发事务相互隔离，互不干扰。

**实现**：
- 使用隔离级别控制
- 实现锁机制
- 处理并发冲突

**示例**：
```sql
-- 设置隔离级别
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
BEGIN;
-- 事务操作
COMMIT;
```

### 2.4 持久性（Durability）

**定义**：事务提交后，数据永久保存。

**实现**：
- 使用事务日志
- 实现数据持久化
- 保证数据可靠性

## 3. ACID 保证

### 3.1 数据库保证

- 数据库系统保证 ACID 特性
- 使用日志和锁机制
- 实现恢复机制

### 3.2 应用层保证

- 正确使用事务
- 实现错误处理
- 验证业务规则

## 4. 注意事项

- **性能影响**：ACID 特性可能影响性能
- **隔离级别**：选择合适的隔离级别
- **并发控制**：处理并发访问
- **数据一致性**：保证数据一致性

## 5. 常见问题

### 5.1 ACID 特性如何保证？

数据库系统通过日志、锁、恢复机制保证 ACID 特性。

### 5.2 如何平衡 ACID 和性能？

选择合适的隔离级别，优化事务范围。

### 5.3 何时可以放宽 ACID 要求？

某些场景可以放宽一致性要求，如最终一致性。

## 6. 实践任务

1. **理解 ACID**：深入理解 ACID 特性
2. **实现原子性**：实现原子性操作
3. **保证一致性**：保证数据一致性
4. **控制隔离性**：选择合适的隔离级别
5. **确保持久性**：确保数据持久化

---

**下一节**：[5.5.4 隔离级别](section-04-isolation-levels.md)
