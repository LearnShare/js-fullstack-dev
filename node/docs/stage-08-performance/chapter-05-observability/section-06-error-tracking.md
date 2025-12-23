# 8.5.6 错误追踪（Sentry）

## 1. 概述

错误追踪是监控和追踪应用错误的重要工具，通过自动捕获、记录和分析错误，可以帮助开发者快速定位和修复问题。Sentry 是广泛使用的错误追踪服务。

## 2. Sentry 安装与配置

### 2.1 安装

```bash
npm install @sentry/node
```

### 2.2 初始化

```ts
import * as Sentry from '@sentry/node';

Sentry.init({
  dsn: process.env.SENTRY_DSN,
  environment: process.env.NODE_ENV,
  tracesSampleRate: 1.0,
  integrations: [
    new Sentry.Integrations.Http({ tracing: true }),
    new Sentry.Integrations.Express({ app })
  ]
});
```

## 3. Express 集成

### 3.1 错误处理

```ts
import express, { Express, Request, Response, NextFunction } from 'express';
import * as Sentry from '@sentry/node';

const app: Express = express();

// 请求追踪
app.use(Sentry.Handlers.requestHandler());
app.use(Sentry.Handlers.tracingHandler());

// 路由
app.get('/api/users', async (req: Request, res: Response): Promise<void> => {
  // 业务逻辑
});

// 错误处理
app.use(Sentry.Handlers.errorHandler());

// 自定义错误处理
app.use((err: Error, req: Request, res: Response, next: NextFunction): void => {
  Sentry.captureException(err);
  res.status(500).json({ error: 'Internal server error' });
});
```

## 4. 手动捕获错误

### 4.1 捕获异常

```ts
try {
  await processData();
} catch (error) {
  Sentry.captureException(error);
  throw error;
}
```

### 4.2 捕获消息

```ts
Sentry.captureMessage('Something went wrong', 'warning');
```

### 4.3 添加上下文

```ts
Sentry.withScope((scope) => {
  scope.setTag('user.id', userId);
  scope.setLevel('error');
  scope.setContext('user', {
    id: userId,
    email: userEmail
  });
  Sentry.captureException(error);
});
```

## 5. 性能监控

### 5.1 事务追踪

```ts
const transaction = Sentry.startTransaction({
  op: 'http.server',
  name: 'GET /api/users'
});

try {
  const span = transaction.startChild({
    op: 'db.query',
    description: 'SELECT * FROM users'
  });
  
  const users = await db.query('SELECT * FROM users');
  span.finish();
  
  transaction.setStatus('ok');
} catch (error) {
  transaction.setStatus('internal_error');
  throw error;
} finally {
  transaction.finish();
}
```

## 6. 最佳实践

### 6.1 错误追踪

- 自动捕获未处理错误
- 手动捕获关键错误
- 添加上下文信息
- 设置错误级别

### 6.2 性能监控

- 追踪关键操作
- 监控慢请求
- 分析性能瓶颈
- 优化性能问题

## 7. 注意事项

- **敏感信息**：避免发送敏感信息
- **采样率**：设置合理的采样率
- **性能影响**：注意性能开销
- **告警配置**：配置合理的告警规则

## 8. 常见问题

### 8.1 如何处理敏感信息？

使用数据清理、过滤敏感字段、脱敏处理。

### 8.2 如何优化性能？

使用采样、异步发送、批量发送。

### 8.3 如何配置告警？

根据错误频率、严重程度、业务影响配置。

## 9. 实践任务

1. **配置 Sentry**：配置错误追踪
2. **集成应用**：集成到应用中
3. **错误处理**：实现错误处理
4. **性能监控**：配置性能监控
5. **持续优化**：持续优化错误追踪

---

**下一章**：[8.6 负载均衡](../chapter-06-load-balancing/readme.md)
