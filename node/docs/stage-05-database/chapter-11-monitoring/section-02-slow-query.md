# 5.11.2 慢查询分析

## 1. 概述

慢查询是影响数据库性能的主要因素，通过分析慢查询可以识别性能瓶颈、优化查询语句、提高数据库性能。

## 2. 慢查询识别

### 2.1 慢查询定义

- **时间阈值**：超过设定时间的查询
- **资源消耗**：消耗大量资源的查询
- **频率影响**：频繁执行的慢查询

### 2.2 PostgreSQL 慢查询

```sql
-- 启用慢查询日志
SET log_min_duration_statement = 1000; -- 记录超过 1 秒的查询

-- 查看慢查询
SELECT query, calls, total_time, mean_time
FROM pg_stat_statements
WHERE mean_time > 1000
ORDER BY mean_time DESC;
```

### 2.3 MySQL 慢查询

```sql
-- 启用慢查询日志
SET GLOBAL slow_query_log = 'ON';
SET GLOBAL long_query_time = 1; -- 记录超过 1 秒的查询

-- 查看慢查询
SELECT * FROM mysql.slow_log
WHERE query_time > 1
ORDER BY query_time DESC;
```

## 3. 查询分析

### 3.1 EXPLAIN 分析

```sql
-- PostgreSQL
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'user@example.com';

-- MySQL
EXPLAIN SELECT * FROM users WHERE email = 'user@example.com';
```

### 3.2 查询计划解读

```ts
interface QueryPlan {
  plan: string;
  executionTime: number;
  rows: number;
  cost: number;
}

async function analyzeQuery(query: string): Promise<QueryPlan> {
  const result = await db.query(`EXPLAIN ANALYZE ${query}`);
  // 解析查询计划
  return parseQueryPlan(result);
}
```

## 4. 慢查询优化

### 4.1 索引优化

```ts
// 识别缺失索引
async function findMissingIndexes(): Promise<void> {
  const queries = await db.query(`
    SELECT schemaname, tablename, attname, n_distinct
    FROM pg_stats
    WHERE n_distinct > 100
    AND schemaname = 'public'
  `);
  
  // 分析是否需要创建索引
  for (const query of queries) {
    console.log(`Consider index on ${query.tablename}.${query.attname}`);
  }
}
```

### 4.2 查询重写

```ts
// 优化前
async function slowQuery(): Promise<void> {
  await db.query(`
    SELECT * FROM users
    WHERE email LIKE '%@example.com'
    ORDER BY created_at DESC
  `);
}

// 优化后
async function optimizedQuery(): Promise<void> {
  await db.query(`
    SELECT * FROM users
    WHERE email LIKE '@example.com%'
    ORDER BY created_at DESC
    LIMIT 100
  `);
}
```

## 5. 慢查询监控

### 5.1 自动监控

```ts
import cron from 'node-cron';

cron.schedule('*/5 * * * *', async (): Promise<void> => {
  const slowQueries = await db.query(`
    SELECT query, calls, mean_time
    FROM pg_stat_statements
    WHERE mean_time > 1000
    ORDER BY mean_time DESC
    LIMIT 10
  `);
  
  if (slowQueries.length > 0) {
    console.warn('Slow queries detected:', slowQueries);
    // 发送告警
  }
});
```

## 6. 最佳实践

### 6.1 慢查询处理

- 定期分析慢查询
- 优化慢查询语句
- 创建必要索引
- 监控查询性能

### 6.2 预防措施

- 使用索引
- 优化查询语句
- 避免全表扫描
- 使用分页

## 7. 注意事项

- **监控开销**：注意慢查询日志对性能的影响
- **索引平衡**：平衡索引数量和写入性能
- **查询优化**：优化查询语句和索引
- **定期审查**：定期审查慢查询

## 8. 常见问题

### 8.1 如何识别慢查询？

使用慢查询日志、查询统计、性能监控工具。

### 8.2 如何优化慢查询？

使用索引、优化查询语句、使用 EXPLAIN 分析。

### 8.3 如何预防慢查询？

合理设计表结构、使用索引、优化查询语句。

## 9. 实践任务

1. **识别慢查询**：识别数据库中的慢查询
2. **分析查询**：使用 EXPLAIN 分析查询
3. **优化查询**：优化慢查询语句
4. **监控慢查询**：实现慢查询监控
5. **性能优化**：根据分析结果优化性能

---

**下一节**：[5.11.3 性能指标监控](section-03-metrics.md)
