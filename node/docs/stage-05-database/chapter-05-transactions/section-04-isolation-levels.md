# 5.5.4 隔离级别

## 1. 概述

隔离级别控制并发事务之间的隔离程度，不同的隔离级别提供不同的并发控制能力和性能。理解隔离级别对于处理并发访问至关重要。

## 2. 隔离级别

### 2.1 READ UNCOMMITTED（读未提交）

**特点**：
- 最低隔离级别
- 允许脏读
- 性能最高
- 数据一致性最差

**问题**：
- 脏读（Dirty Read）
- 不可重复读（Non-repeatable Read）
- 幻读（Phantom Read）

### 2.2 READ COMMITTED（读已提交）

**特点**：
- 防止脏读
- 允许不可重复读
- 允许幻读
- 默认隔离级别（PostgreSQL）

**问题**：
- 不可重复读
- 幻读

### 2.3 REPEATABLE READ（可重复读）

**特点**：
- 防止脏读和不可重复读
- 允许幻读
- 默认隔离级别（MySQL）

**问题**：
- 幻读

### 2.4 SERIALIZABLE（串行化）

**特点**：
- 最高隔离级别
- 防止所有并发问题
- 性能最低
- 数据一致性最好

**问题**：
- 性能开销大
- 可能产生死锁

## 3. 并发问题

### 3.1 脏读（Dirty Read）

**定义**：读取到未提交的数据。

**示例**：
```sql
-- 事务 A
BEGIN;
UPDATE accounts SET balance = 1000 WHERE id = 1;
-- 未提交

-- 事务 B（READ UNCOMMITTED）
SELECT balance FROM accounts WHERE id = 1; -- 读取到 1000

-- 事务 A
ROLLBACK; -- 回滚

-- 事务 B 读取到的是无效数据
```

### 3.2 不可重复读（Non-repeatable Read）

**定义**：同一事务中多次读取同一数据，结果不一致。

**示例**：
```sql
-- 事务 A
BEGIN;
SELECT balance FROM accounts WHERE id = 1; -- 读取到 100

-- 事务 B
UPDATE accounts SET balance = 200 WHERE id = 1;
COMMIT;

-- 事务 A
SELECT balance FROM accounts WHERE id = 1; -- 读取到 200（不一致）
```

### 3.3 幻读（Phantom Read）

**定义**：同一事务中多次查询，结果集不一致。

**示例**：
```sql
-- 事务 A
BEGIN;
SELECT * FROM accounts WHERE balance > 100; -- 返回 2 条记录

-- 事务 B
INSERT INTO accounts (balance) VALUES (200);
COMMIT;

-- 事务 A
SELECT * FROM accounts WHERE balance > 100; -- 返回 3 条记录（不一致）
```

## 4. 隔离级别设置

### 4.1 PostgreSQL

```sql
-- 设置隔离级别
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
BEGIN;
-- 事务操作
COMMIT;
```

### 4.2 MySQL

```sql
-- 设置隔离级别
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
BEGIN;
-- 事务操作
COMMIT;
```

### 4.3 Node.js 实现

```ts
async function setIsolationLevel(): Promise<void> {
  const client = await pool.connect();
  try {
    await client.query('SET TRANSACTION ISOLATION LEVEL READ COMMITTED');
    await client.query('BEGIN');
    
    // 事务操作
    
    await client.query('COMMIT');
  } catch (error) {
    await client.query('ROLLBACK');
    throw error;
  } finally {
    client.release();
  }
}
```

## 5. 选择隔离级别

### 5.1 选择原则

- **数据一致性要求高**：使用 SERIALIZABLE
- **性能要求高**：使用 READ COMMITTED
- **平衡考虑**：使用 REPEATABLE READ

### 5.2 应用场景

- **只读查询**：READ COMMITTED
- **读写混合**：REPEATABLE READ
- **关键业务**：SERIALIZABLE

## 6. 最佳实践

### 6.1 隔离级别选择

- 根据业务需求选择
- 平衡一致性和性能
- 测试不同隔离级别
- 监控并发问题

### 6.2 并发控制

- 使用锁机制
- 处理死锁
- 优化事务范围
- 监控性能

## 7. 注意事项

- **性能影响**：隔离级别越高，性能越低
- **死锁风险**：高隔离级别可能产生死锁
- **业务需求**：根据业务需求选择隔离级别
- **测试验证**：测试不同隔离级别的效果

## 8. 常见问题

### 8.1 如何选择隔离级别？

根据数据一致性要求和性能需求选择。

### 8.2 如何处理死锁？

实现死锁检测和重试机制。

### 8.3 如何优化并发性能？

选择合适的隔离级别，优化事务范围，使用索引。

## 9. 实践任务

1. **理解隔离级别**：深入理解不同隔离级别
2. **设置隔离级别**：在应用中设置隔离级别
3. **测试并发问题**：测试不同隔离级别的并发问题
4. **优化性能**：优化隔离级别和事务范围
5. **最佳实践**：遵循隔离级别使用最佳实践

---

**下一章**：[5.6 NoSQL 数据库](../chapter-06-nosql/readme.md)
