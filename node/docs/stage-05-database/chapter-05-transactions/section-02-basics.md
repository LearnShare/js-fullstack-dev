# 5.5.2 事务基础

## 1. 概述

事务基础包括事务的开始、提交、回滚等基本操作。掌握事务基础是使用事务的前提。

## 2. 事务控制语句

### 2.1 BEGIN/START TRANSACTION

```sql
-- 开始事务
BEGIN;
-- 或
START TRANSACTION;
```

### 2.2 COMMIT

```sql
-- 提交事务
COMMIT;
```

### 2.3 ROLLBACK

```sql
-- 回滚事务
ROLLBACK;
```

## 3. Node.js 实现

### 3.1 基本事务

```ts
import { Pool, PoolClient } from 'pg';

const pool = new Pool({ connectionString: process.env.DATABASE_URL });

async function executeTransaction(): Promise<void> {
  const client: PoolClient = await pool.connect();
  try {
    await client.query('BEGIN');
    
    // 执行操作
    await client.query('INSERT INTO users (name, email) VALUES ($1, $2)', ['John', 'john@example.com']);
    await client.query('INSERT INTO posts (title, content) VALUES ($1, $2)', ['Post 1', 'Content 1']);
    
    await client.query('COMMIT');
  } catch (error) {
    await client.query('ROLLBACK');
    throw error;
  } finally {
    client.release();
  }
}
```

### 3.2 事务辅助函数

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

// 使用
await withTransaction(async (client: PoolClient): Promise<void> => {
  await client.query('INSERT INTO users (name, email) VALUES ($1, $2)', ['John', 'john@example.com']);
  await client.query('INSERT INTO posts (title, content) VALUES ($1, $2)', ['Post 1', 'Content 1']);
});
```

## 4. ORM 事务

### 4.1 Prisma 事务

```ts
import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

await prisma.$transaction(async (tx) => {
  await tx.user.create({
    data: { name: 'John', email: 'john@example.com' }
  });
  await tx.post.create({
    data: { title: 'Post 1', content: 'Content 1', authorId: 1 }
  });
});
```

### 4.2 TypeORM 事务

```ts
import { AppDataSource } from './data-source';

await AppDataSource.transaction(async (manager) => {
  await manager.save(User, { name: 'John', email: 'john@example.com' });
  await manager.save(Post, { title: 'Post 1', content: 'Content 1' });
});
```

## 5. 保存点

### 5.1 保存点使用

```sql
-- 创建保存点
SAVEPOINT sp1;

-- 回滚到保存点
ROLLBACK TO SAVEPOINT sp1;

-- 释放保存点
RELEASE SAVEPOINT sp1;
```

### 5.2 Node.js 实现

```ts
async function useSavepoint(): Promise<void> {
  const client = await pool.connect();
  try {
    await client.query('BEGIN');
    
    await client.query('INSERT INTO users (name, email) VALUES ($1, $2)', ['John', 'john@example.com']);
    await client.query('SAVEPOINT sp1');
    
    try {
      await client.query('INSERT INTO posts (title, content) VALUES ($1, $2)', ['Post 1', 'Content 1']);
    } catch (error) {
      await client.query('ROLLBACK TO SAVEPOINT sp1');
    }
    
    await client.query('COMMIT');
  } catch (error) {
    await client.query('ROLLBACK');
    throw error;
  } finally {
    client.release();
  }
}
```

## 6. 最佳实践

### 6.1 事务范围

- 保持事务范围最小
- 避免长时间事务
- 合理控制事务粒度

### 6.2 错误处理

- 实现完善的错误处理
- 确保回滚操作
- 记录错误日志

## 7. 注意事项

- **事务范围**：合理控制事务范围
- **性能影响**：事务会影响性能
- **错误处理**：实现完善的错误处理
- **资源释放**：确保释放数据库连接

## 8. 常见问题

### 8.1 如何处理事务超时？

设置事务超时时间，超时后自动回滚。

### 8.2 如何避免长时间事务？

合理控制事务范围，避免在事务中执行耗时操作。

### 8.3 如何处理嵌套事务？

使用保存点实现嵌套事务效果。

## 9. 实践任务

1. **基本事务**：实现基本的事务操作
2. **事务辅助函数**：实现事务辅助函数
3. **ORM 事务**：使用 ORM 框架实现事务
4. **保存点**：使用保存点实现部分回滚
5. **错误处理**：实现完善的错误处理机制

---

**下一节**：[5.5.3 ACID 特性](section-03-acid.md)
