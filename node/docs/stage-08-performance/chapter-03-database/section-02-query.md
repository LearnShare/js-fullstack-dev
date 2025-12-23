# 8.3.2 查询优化

## 1. 概述

查询优化是数据库性能优化的核心，通过优化 SQL 查询语句，可以显著提高查询速度和减少资源使用。

## 2. 查询分析

### 2.1 EXPLAIN 使用

```sql
-- PostgreSQL
EXPLAIN ANALYZE 
SELECT u.*, p.title 
FROM users u 
JOIN posts p ON u.id = p.user_id 
WHERE u.email = 'user@example.com';

-- 输出示例
-- Seq Scan on users (cost=0.00..1000.00 rows=1 width=64) (actual time=0.123..5.456 rows=1 loops=1)
--   Filter: (email = 'user@example.com'::text)
--   Rows Removed by Filter: 9999
```

### 2.2 查询计划解读

- **Seq Scan**：顺序扫描（慢）
- **Index Scan**：索引扫描（快）
- **cost**：预估成本
- **rows**：预估行数
- **actual time**：实际执行时间

## 3. 查询优化技巧

### 3.1 避免 SELECT *

```sql
-- 不优化
SELECT * FROM users WHERE id = 1;

-- 优化：只查询需要的字段
SELECT id, name, email FROM users WHERE id = 1;
```

### 3.2 使用 LIMIT

```sql
-- 不优化
SELECT * FROM posts ORDER BY created_at DESC;

-- 优化：限制结果数量
SELECT * FROM posts ORDER BY created_at DESC LIMIT 20;
```

### 3.3 优化 WHERE 子句

```sql
-- 不优化：函数调用
SELECT * FROM users WHERE UPPER(email) = 'USER@EXAMPLE.COM';

-- 优化：使用索引字段
SELECT * FROM users WHERE email = 'user@example.com';
```

### 3.4 优化 JOIN

```sql
-- 不优化：笛卡尔积
SELECT * FROM users, posts WHERE users.id = posts.user_id;

-- 优化：使用 JOIN
SELECT u.*, p.title 
FROM users u 
INNER JOIN posts p ON u.id = p.user_id;
```

## 4. 子查询优化

### 4.1 EXISTS vs IN

```sql
-- 使用 EXISTS（通常更快）
SELECT * FROM users u 
WHERE EXISTS (
  SELECT 1 FROM posts p WHERE p.user_id = u.id
);

-- 使用 IN（小数据集）
SELECT * FROM users 
WHERE id IN (SELECT user_id FROM posts);
```

### 4.2 子查询转 JOIN

```sql
-- 不优化：子查询
SELECT * FROM users 
WHERE id IN (SELECT user_id FROM posts WHERE status = 'published');

-- 优化：JOIN
SELECT DISTINCT u.* 
FROM users u 
INNER JOIN posts p ON u.id = p.user_id 
WHERE p.status = 'published';
```

## 5. 分页优化

### 5.1 OFFSET 优化

```sql
-- 不优化：大 OFFSET
SELECT * FROM posts ORDER BY id LIMIT 20 OFFSET 10000;

-- 优化：使用游标
SELECT * FROM posts WHERE id > 10000 ORDER BY id LIMIT 20;
```

### 5.2 分页实现

```ts
interface PaginationOptions {
  page: number;
  pageSize: number;
  lastId?: number;
}

async function getPosts(options: PaginationOptions): Promise<Post[]> {
  const { page, pageSize, lastId } = options;
  
  if (lastId) {
    // 游标分页
    return await db.query(
      'SELECT * FROM posts WHERE id > $1 ORDER BY id LIMIT $2',
      [lastId, pageSize]
    );
  } else {
    // 偏移分页
    return await db.query(
      'SELECT * FROM posts ORDER BY id LIMIT $1 OFFSET $2',
      [pageSize, (page - 1) * pageSize]
    );
  }
}
```

## 6. 最佳实践

### 6.1 查询设计

- 使用 EXPLAIN 分析查询
- 只查询需要的字段
- 使用索引字段查询
- 优化 JOIN 操作

### 6.2 性能监控

- 监控慢查询
- 分析查询计划
- 优化热点查询
- 定期审查查询

## 7. 注意事项

- **查询分析**：使用 EXPLAIN 分析查询
- **索引使用**：确保使用索引
- **避免全表扫描**：优化 WHERE 子句
- **分页优化**：使用游标分页

## 8. 常见问题

### 8.1 如何优化慢查询？

使用 EXPLAIN 分析、添加索引、优化查询语句。

### 8.2 如何处理大量数据查询？

使用分页、游标、批量处理。

### 8.3 如何优化 JOIN 查询？

使用索引、优化 JOIN 顺序、使用子查询。

## 9. 实践任务

1. **查询分析**：使用 EXPLAIN 分析查询
2. **查询优化**：优化慢查询
3. **分页实现**：实现高效分页
4. **性能测试**：测试查询性能
5. **持续优化**：持续优化查询

---

**下一节**：[8.3.3 索引优化](section-03-indexes.md)
