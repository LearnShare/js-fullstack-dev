# 8.3.3 索引优化

## 1. 概述

索引是提高数据库查询性能的关键，通过合理设计和优化索引，可以显著提高查询速度。理解索引的工作原理对于优化至关重要。

## 2. 索引类型

### 2.1 B-Tree 索引

**特点**：
- 最常用的索引类型
- 支持等值查询和范围查询
- 适合大多数场景

**创建**：
```sql
-- 单列索引
CREATE INDEX idx_email ON users(email);

-- 复合索引
CREATE INDEX idx_user_status ON posts(user_id, status);
```

### 2.2 唯一索引

```sql
CREATE UNIQUE INDEX idx_email_unique ON users(email);
```

### 2.3 部分索引

```sql
-- PostgreSQL：只索引活跃用户
CREATE INDEX idx_active_users ON users(email) WHERE active = true;
```

## 3. 索引设计原则

### 3.1 选择索引字段

- **WHERE 子句**：为 WHERE 子句中的字段创建索引
- **JOIN 字段**：为 JOIN 字段创建索引
- **ORDER BY**：为 ORDER BY 字段创建索引
- **高选择性**：选择高选择性的字段

### 3.2 复合索引

```sql
-- 复合索引顺序很重要
CREATE INDEX idx_user_status_created ON posts(user_id, status, created_at);

-- 查询可以使用索引
SELECT * FROM posts WHERE user_id = 1 AND status = 'published' ORDER BY created_at;
```

### 3.3 索引选择性

```sql
-- 高选择性：适合索引
CREATE INDEX idx_email ON users(email); -- email 唯一或接近唯一

-- 低选择性：不适合索引
-- CREATE INDEX idx_gender ON users(gender); -- 只有几个值
```

## 4. 索引优化

### 4.1 监控索引使用

```sql
-- PostgreSQL：查看索引使用情况
SELECT 
  schemaname,
  tablename,
  indexname,
  idx_scan,
  idx_tup_read,
  idx_tup_fetch
FROM pg_stat_user_indexes
ORDER BY idx_scan;

-- MySQL：查看索引使用情况
SHOW INDEX FROM users;
```

### 4.2 删除未使用索引

```sql
-- 删除未使用的索引
DROP INDEX idx_unused_index;
```

### 4.3 索引维护

```sql
-- PostgreSQL：重建索引
REINDEX INDEX idx_email;

-- MySQL：优化表
OPTIMIZE TABLE users;
```

## 5. 索引最佳实践

### 5.1 索引设计

- 为常用查询创建索引
- 使用复合索引优化多字段查询
- 避免过多索引
- 定期维护索引

### 5.2 索引使用

- 确保查询使用索引
- 避免在索引字段上使用函数
- 使用 EXPLAIN 验证索引使用
- 监控索引性能

## 6. 注意事项

- **索引开销**：索引会增加写入开销
- **索引维护**：定期维护索引
- **过度索引**：避免创建过多索引
- **索引选择**：选择高选择性字段

## 7. 常见问题

### 7.1 如何选择索引字段？

为 WHERE、JOIN、ORDER BY 中的字段创建索引。

### 7.2 如何优化复合索引？

根据查询模式确定字段顺序。

### 7.3 如何处理索引过多？

删除未使用的索引，合并相关索引。

## 8. 实践任务

1. **索引设计**：设计合适的索引
2. **索引创建**：创建索引
3. **索引监控**：监控索引使用
4. **索引优化**：优化索引性能
5. **持续维护**：定期维护索引

---

**下一节**：[8.3.4 连接池优化](section-04-connection-pool.md)
