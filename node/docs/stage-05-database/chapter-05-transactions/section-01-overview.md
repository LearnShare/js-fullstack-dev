# 5.5.1 事务处理概述

## 1. 概述

事务是数据库操作的基本单位，是一系列数据库操作的集合，要么全部执行成功，要么全部不执行。事务保证了数据的一致性和完整性。

## 2. 核心概念

### 2.1 事务的定义

事务是一组数据库操作，满足 ACID 特性：
- **原子性（Atomicity）**：全部成功或全部失败
- **一致性（Consistency）**：数据保持一致
- **隔离性（Isolation）**：并发事务相互隔离
- **持久性（Durability）**：提交后持久化

### 2.2 事务的状态

- **活动（Active）**：事务正在执行
- **部分提交（Partially Committed）**：最后一条语句执行完成
- **提交（Committed）**：事务成功提交
- **失败（Failed）**：事务执行失败
- **中止（Aborted）**：事务回滚

## 3. 事务操作

### 3.1 基本操作

```sql
-- 开始事务
BEGIN;

-- 执行操作
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

-- 提交事务
COMMIT;

-- 或回滚事务
ROLLBACK;
```

### 3.2 Node.js 实现

```ts
import { Pool } from 'pg';

const pool = new Pool({ connectionString: process.env.DATABASE_URL });

async function transferFunds(fromId: number, toId: number, amount: number): Promise<void> {
  const client = await pool.connect();
  try {
    await client.query('BEGIN');
    
    await client.query(
      'UPDATE accounts SET balance = balance - $1 WHERE id = $2',
      [amount, fromId]
    );
    
    await client.query(
      'UPDATE accounts SET balance = balance + $1 WHERE id = $2',
      [amount, toId]
    );
    
    await client.query('COMMIT');
  } catch (error) {
    await client.query('ROLLBACK');
    throw error;
  } finally {
    client.release();
  }
}
```

## 4. 事务的重要性

### 4.1 数据一致性

- 保证数据操作的原子性
- 防止部分更新导致的数据不一致
- 保证业务逻辑的正确性

### 4.2 并发控制

- 处理并发访问
- 防止数据竞争
- 保证数据完整性

## 5. 注意事项

- **事务范围**：合理控制事务范围
- **性能影响**：事务会影响性能
- **死锁**：注意避免死锁
- **隔离级别**：选择合适的隔离级别

## 6. 常见问题

### 6.1 何时使用事务？

需要保证多个操作原子性时使用事务。

### 6.2 事务会影响性能吗？

会，需要合理控制事务范围和隔离级别。

### 6.3 如何处理事务失败？

实现错误处理和回滚机制。

## 7. 相关资源

- [事务处理](https://en.wikipedia.org/wiki/Database_transaction)
- [ACID 特性](https://en.wikipedia.org/wiki/ACID)

---

**下一节**：[5.5.2 事务基础](section-02-basics.md)
