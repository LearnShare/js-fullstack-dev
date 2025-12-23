# 6.6.2 安全事件记录

## 1. 概述

安全事件记录是记录安全相关事件的过程，包括认证事件、授权事件、数据访问事件等。安全事件记录是安全审计的基础。

## 2. 事件类型

### 2.1 认证事件

```ts
interface AuthEvent {
  type: 'login' | 'logout' | 'login_failed' | 'password_change';
  userId?: number;
  username?: string;
  ip: string;
  userAgent: string;
  timestamp: Date;
  success: boolean;
  reason?: string;
}

async function logAuthEvent(event: AuthEvent): Promise<void> {
  await db.query(
    `INSERT INTO auth_events (type, user_id, username, ip, user_agent, timestamp, success, reason)
     VALUES ($1, $2, $3, $4, $5, $6, $7, $8)`,
    [event.type, event.userId, event.username, event.ip, event.userAgent, event.timestamp, event.success, event.reason]
  );
}
```

### 2.2 授权事件

```ts
interface AuthorizationEvent {
  type: 'permission_check' | 'permission_granted' | 'permission_denied';
  userId: number;
  resource: string;
  action: string;
  result: 'allowed' | 'denied';
  ip: string;
  timestamp: Date;
}

async function logAuthorizationEvent(event: AuthorizationEvent): Promise<void> {
  await db.query(
    `INSERT INTO authorization_events (type, user_id, resource, action, result, ip, timestamp)
     VALUES ($1, $2, $3, $4, $5, $6, $7)`,
    [event.type, event.userId, event.resource, event.action, event.result, event.ip, event.timestamp]
  );
}
```

### 2.3 数据访问事件

```ts
interface DataAccessEvent {
  type: 'read' | 'write' | 'delete';
  userId: number;
  resourceType: string;
  resourceId: number;
  ip: string;
  timestamp: Date;
}

async function logDataAccessEvent(event: DataAccessEvent): Promise<void> {
  await db.query(
    `INSERT INTO data_access_events (type, user_id, resource_type, resource_id, ip, timestamp)
     VALUES ($1, $2, $3, $4, $5, $6)`,
    [event.type, event.userId, event.resourceType, event.resourceId, event.ip, event.timestamp]
  );
}
```

## 3. 事件记录中间件

### 3.1 认证事件记录

```ts
import { Request, Response, NextFunction } from 'express';

function logAuthMiddleware(req: Request, res: Response, next: NextFunction): void {
  const originalSend = res.send;
  
  res.send = function (body: any): Response {
    if (req.path === '/login' && req.method === 'POST') {
      const event: AuthEvent = {
        type: res.statusCode === 200 ? 'login' : 'login_failed',
        userId: (req as any).user?.id,
        username: req.body.username,
        ip: req.ip,
        userAgent: req.headers['user-agent'] || '',
        timestamp: new Date(),
        success: res.statusCode === 200,
        reason: res.statusCode !== 200 ? body : undefined
      };
      
      logAuthEvent(event).catch(console.error);
    }
    
    return originalSend.call(this, body);
  };
  
  next();
}

app.use(logAuthMiddleware);
```

### 3.2 授权事件记录

```ts
function logAuthorizationMiddleware(resource: string, action: string) {
  return async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    const userId = (req as any).user?.id;
    
    const originalSend = res.send;
    res.send = function (body: any): Response {
      const event: AuthorizationEvent = {
        type: 'permission_check',
        userId: userId || 0,
        resource,
        action,
        result: res.statusCode === 200 ? 'allowed' : 'denied',
        ip: req.ip,
        timestamp: new Date()
      };
      
      logAuthorizationEvent(event).catch(console.error);
      
      return originalSend.call(this, body);
    };
    
    next();
  };
}

// 使用
app.delete('/users/:id', logAuthorizationMiddleware('users', 'delete'), (req: Request, res: Response): void => {
  // 删除用户
});
```

## 4. 事件查询

### 4.1 查询认证事件

```ts
async function getAuthEvents(userId?: number, startDate?: Date, endDate?: Date): Promise<AuthEvent[]> {
  let query = 'SELECT * FROM auth_events WHERE 1=1';
  const params: any[] = [];
  
  if (userId) {
    query += ' AND user_id = $' + (params.length + 1);
    params.push(userId);
  }
  
  if (startDate) {
    query += ' AND timestamp >= $' + (params.length + 1);
    params.push(startDate);
  }
  
  if (endDate) {
    query += ' AND timestamp <= $' + (params.length + 1);
    params.push(endDate);
  }
  
  query += ' ORDER BY timestamp DESC LIMIT 100';
  
  return await db.query(query, params);
}
```

### 4.2 异常检测

```ts
async function detectSuspiciousActivity(userId: number, hours: number = 24): Promise<boolean> {
  const startDate = new Date(Date.now() - hours * 60 * 60 * 1000);
  
  const failedLogins = await db.query(
    `SELECT COUNT(*) as count 
     FROM auth_events 
     WHERE user_id = $1 AND type = 'login_failed' AND timestamp >= $2`,
    [userId, startDate]
  );
  
  return failedLogins[0].count > 5; // 24 小时内失败超过 5 次
}
```

## 5. 最佳实践

### 5.1 事件设计

- 结构化事件
- 包含关键信息
- 统一格式
- 支持查询

### 5.2 性能考虑

- 异步记录
- 批量写入
- 索引优化
- 定期归档

## 6. 注意事项

- **性能影响**：注意日志记录性能
- **存储容量**：合理管理日志存储
- **隐私保护**：保护用户隐私
- **日志安全**：保护日志不被篡改

## 7. 常见问题

### 7.1 如何优化日志性能？

异步记录、批量写入、使用消息队列。

### 7.2 如何处理日志存储？

定期归档、压缩存储、删除过期日志。

### 7.3 如何保护日志隐私？

加密敏感信息、访问控制、匿名化处理。

## 8. 实践任务

1. **事件记录**：实现安全事件记录
2. **中间件**：实现事件记录中间件
3. **事件查询**：实现事件查询功能
4. **异常检测**：实现异常检测功能
5. **日志分析**：实现日志分析功能

---

**下一节**：[6.6.3 审计日志](section-03-audit-log.md)
