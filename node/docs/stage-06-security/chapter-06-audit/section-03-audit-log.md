# 6.6.3 审计日志

## 1. 概述

审计日志是记录系统操作和变更的日志，用于追溯操作历史、分析系统行为、满足合规要求。审计日志是安全审计的核心组件。

## 2. 审计日志设计

### 2.1 日志结构

```ts
interface AuditLog {
  id: number;
  userId: number;
  username: string;
  action: string;
  resourceType: string;
  resourceId: number;
  oldValue?: any;
  newValue?: any;
  ip: string;
  userAgent: string;
  timestamp: Date;
  success: boolean;
  error?: string;
}
```

### 2.2 数据库表

```sql
CREATE TABLE audit_logs (
  id SERIAL PRIMARY KEY,
  user_id INT NOT NULL,
  username VARCHAR(100) NOT NULL,
  action VARCHAR(100) NOT NULL,
  resource_type VARCHAR(100) NOT NULL,
  resource_id INT,
  old_value JSONB,
  new_value JSONB,
  ip VARCHAR(45) NOT NULL,
  user_agent TEXT,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  success BOOLEAN NOT NULL,
  error TEXT,
  INDEX idx_user_id (user_id),
  INDEX idx_timestamp (timestamp),
  INDEX idx_resource (resource_type, resource_id)
);
```

## 3. 审计日志实现

### 3.1 日志记录函数

```ts
async function logAuditEvent(
  userId: number,
  username: string,
  action: string,
  resourceType: string,
  resourceId: number,
  oldValue: any,
  newValue: any,
  req: Request,
  success: boolean = true,
  error?: string
): Promise<void> {
  await db.query(
    `INSERT INTO audit_logs 
     (user_id, username, action, resource_type, resource_id, old_value, new_value, ip, user_agent, success, error)
     VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11)`,
    [
      userId,
      username,
      action,
      resourceType,
      resourceId,
      oldValue ? JSON.stringify(oldValue) : null,
      newValue ? JSON.stringify(newValue) : null,
      req.ip,
      req.headers['user-agent'] || '',
      success,
      error
    ]
  );
}
```

### 3.2 数据变更审计

```ts
app.put('/users/:id', async (req: Request, res: Response): Promise<void> => {
  const userId = parseInt(req.params.id);
  const user = (req as any).user;
  
  try {
    // 获取旧值
    const oldUser = await db.query('SELECT * FROM users WHERE id = $1', [userId]);
    
    // 更新数据
    await db.query(
      'UPDATE users SET name = $1, email = $2 WHERE id = $3',
      [req.body.name, req.body.email, userId]
    );
    
    // 获取新值
    const newUser = await db.query('SELECT * FROM users WHERE id = $1', [userId]);
    
    // 记录审计日志
    await logAuditEvent(
      user.id,
      user.username,
      'update',
      'user',
      userId,
      oldUser[0],
      newUser[0],
      req,
      true
    );
    
    res.json({ message: 'User updated' });
  } catch (error) {
    await logAuditEvent(
      user.id,
      user.username,
      'update',
      'user',
      userId,
      null,
      null,
      req,
      false,
      (error as Error).message
    );
    
    res.status(500).json({ message: 'Update failed' });
  }
});
```

## 4. 日志查询和分析

### 4.1 查询日志

```ts
async function getAuditLogs(
  filters: {
    userId?: number;
    resourceType?: string;
    action?: string;
    startDate?: Date;
    endDate?: Date;
  },
  limit: number = 100,
  offset: number = 0
): Promise<AuditLog[]> {
  let query = 'SELECT * FROM audit_logs WHERE 1=1';
  const params: any[] = [];
  
  if (filters.userId) {
    query += ' AND user_id = $' + (params.length + 1);
    params.push(filters.userId);
  }
  
  if (filters.resourceType) {
    query += ' AND resource_type = $' + (params.length + 1);
    params.push(filters.resourceType);
  }
  
  if (filters.action) {
    query += ' AND action = $' + (params.length + 1);
    params.push(filters.action);
  }
  
  if (filters.startDate) {
    query += ' AND timestamp >= $' + (params.length + 1);
    params.push(filters.startDate);
  }
  
  if (filters.endDate) {
    query += ' AND timestamp <= $' + (params.length + 1);
    params.push(filters.endDate);
  }
  
  query += ' ORDER BY timestamp DESC LIMIT $' + (params.length + 1) + ' OFFSET $' + (params.length + 2);
  params.push(limit, offset);
  
  const results = await db.query(query, params);
  return results.map((row: any) => ({
    ...row,
    oldValue: row.old_value ? JSON.parse(row.old_value) : null,
    newValue: row.new_value ? JSON.parse(row.new_value) : null
  }));
}
```

### 4.2 日志统计

```ts
async function getAuditStatistics(startDate: Date, endDate: Date): Promise<any> {
  const stats = await db.query(
    `SELECT 
       action,
       resource_type,
       COUNT(*) as count,
       COUNT(*) FILTER (WHERE success = false) as error_count
     FROM audit_logs
     WHERE timestamp BETWEEN $1 AND $2
     GROUP BY action, resource_type
     ORDER BY count DESC`,
    [startDate, endDate]
  );
  
  return stats;
}
```

## 5. 日志导出

### 5.1 CSV 导出

```ts
import { createWriteStream } from 'node:fs';
import { stringify } from 'csv-stringify';

async function exportAuditLogs(filters: any, filePath: string): Promise<void> {
  const logs = await getAuditLogs(filters, 10000, 0);
  
  const stringifier = stringify({
    header: true,
    columns: ['id', 'userId', 'username', 'action', 'resourceType', 'resourceId', 'ip', 'timestamp', 'success']
  });
  
  const writeStream = createWriteStream(filePath);
  stringifier.pipe(writeStream);
  
  for (const log of logs) {
    stringifier.write([
      log.id,
      log.userId,
      log.username,
      log.action,
      log.resourceType,
      log.resourceId,
      log.ip,
      log.timestamp,
      log.success
    ]);
  }
  
  stringifier.end();
}
```

## 6. 最佳实践

### 6.1 日志设计

- 结构化存储
- 包含完整信息
- 支持查询
- 定期归档

### 6.2 安全考虑

- 保护日志完整性
- 访问控制
- 加密敏感信息
- 备份恢复

## 7. 注意事项

- **性能影响**：注意日志记录性能
- **存储容量**：合理管理日志存储
- **隐私保护**：保护用户隐私
- **合规要求**：满足合规要求

## 8. 常见问题

### 8.1 如何优化日志性能？

异步记录、批量写入、使用消息队列、定期归档。

### 8.2 如何处理日志存储？

定期归档、压缩存储、删除过期日志、使用对象存储。

### 8.3 如何保护日志安全？

只追加存储、访问控制、加密存储、备份恢复。

## 9. 实践任务

1. **日志记录**：实现审计日志记录
2. **日志查询**：实现日志查询功能
3. **日志分析**：实现日志分析功能
4. **日志导出**：实现日志导出功能
5. **安全加固**：加固日志安全

---

**下一章**：[6.7 依赖安全](../chapter-07-dependency-security/readme.md)
