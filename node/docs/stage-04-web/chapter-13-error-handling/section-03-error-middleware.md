# 4.13.3 错误中间件

## 1. 概述

错误处理中间件是统一处理错误的机制，可以捕获应用中所有未处理的错误，提供统一的错误响应格式和错误日志记录。

## 2. 基本错误中间件

### 2.1 Express 错误中间件

```ts
import { Request, Response, NextFunction } from 'express';

app.use((err: Error, req: Request, res: Response, next: NextFunction): void => {
  console.error('Error:', err);
  res.status(500).json({ error: 'Internal server error' });
});
```

### 2.2 错误分类处理

```ts
app.use((err: Error, req: Request, res: Response, next: NextFunction): void => {
  if (err instanceof ValidationError) {
    return res.status(400).json({
      error: 'Validation failed',
      details: err.errors
    });
  }
  
  if (err instanceof AuthenticationError) {
    return res.status(401).json({
      error: 'Authentication required',
      message: err.message
    });
  }
  
  if (err instanceof NotFoundError) {
    return res.status(404).json({
      error: 'Resource not found',
      message: err.message
    });
  }
  
  // 默认服务器错误
  console.error('Unexpected error:', err);
  res.status(500).json({ error: 'Internal server error' });
});
```

## 3. 错误日志记录

### 3.1 结构化日志

```ts
import { Request, Response, NextFunction } from 'express';

interface ErrorLog {
  timestamp: string;
  method: string;
  path: string;
  error: {
    name: string;
    message: string;
    stack?: string;
  };
  user?: string;
  ip: string;
}

app.use((err: Error, req: Request, res: Response, next: NextFunction): void => {
  const errorLog: ErrorLog = {
    timestamp: new Date().toISOString(),
    method: req.method,
    path: req.path,
    error: {
      name: err.name,
      message: err.message,
      stack: process.env.NODE_ENV === 'development' ? err.stack : undefined
    },
    user: (req as any).user?.id,
    ip: req.ip
  };
  
  console.error(JSON.stringify(errorLog));
  
  // 发送到日志服务
  // sendToLogService(errorLog);
  
  next(err);
});
```

### 3.2 错误分类记录

```ts
app.use((err: Error, req: Request, res: Response, next: NextFunction): void => {
  if (err instanceof AppError && err.isOperational) {
    // 可操作错误：记录但不发送警报
    console.warn('Operational error:', err.message);
  } else {
    // 系统错误：记录并发送警报
    console.error('System error:', err);
    // sendAlert(err);
  }
  
  next(err);
});
```

## 4. 错误响应格式化

### 4.1 统一错误响应

```ts
interface ErrorResponse {
  error: {
    code: string;
    message: string;
    details?: unknown;
  };
  timestamp: string;
  path: string;
}

function formatErrorResponse(err: Error, req: Request): ErrorResponse {
  if (err instanceof AppError) {
    return {
      error: {
        code: err.code?.toString() || 'UNKNOWN_ERROR',
        message: err.message,
        details: err instanceof ValidationError ? err.errors : undefined
      },
      timestamp: new Date().toISOString(),
      path: req.path
    };
  }
  
  return {
    error: {
      code: 'INTERNAL_ERROR',
      message: process.env.NODE_ENV === 'production' ? 'Internal server error' : err.message
    },
    timestamp: new Date().toISOString(),
    path: req.path
  };
}

app.use((err: Error, req: Request, res: Response, next: NextFunction): void => {
  const errorResponse = formatErrorResponse(err, req);
  const statusCode = err instanceof AppError ? err.statusCode : 500;
  
  res.status(statusCode).json(errorResponse);
});
```

## 5. 异步错误处理

### 5.1 异步错误包装

```ts
function asyncHandler(fn: (req: Request, res: Response, next: NextFunction) => Promise<void>) {
  return (req: Request, res: Response, next: NextFunction): void => {
    Promise.resolve(fn(req, res, next)).catch(next);
  };
}

app.get('/api/users', asyncHandler(async (req: Request, res: Response): Promise<void> => {
  const users = await fetchUsers();
  res.json({ users });
}));
```

### 5.2 路由级错误处理

```ts
app.get('/api/users/:id', async (req: Request, res: Response, next: NextFunction): Promise<void> => {
  try {
    const { id } = req.params;
    const user = await getUserById(id);
    
    if (!user) {
      throw new NotFoundError('User');
    }
    
    res.json({ user });
  } catch (error) {
    next(error);
  }
});
```

## 6. 错误监控

### 6.1 错误统计

```ts
interface ErrorStats {
  total: number;
  byType: Record<string, number>;
  byEndpoint: Record<string, number>;
}

const errorStats: ErrorStats = {
  total: 0,
  byType: {},
  byEndpoint: {}
};

app.use((err: Error, req: Request, res: Response, next: NextFunction): void => {
  errorStats.total++;
  errorStats.byType[err.name] = (errorStats.byType[err.name] || 0) + 1;
  errorStats.byEndpoint[req.path] = (errorStats.byEndpoint[req.path] || 0) + 1;
  
  next(err);
});

app.get('/api/stats/errors', (req: Request, res: Response): void => {
  res.json(errorStats);
});
```

## 7. 最佳实践

### 7.1 错误处理

- 使用统一的错误处理中间件
- 分类处理不同类型的错误
- 记录详细错误日志

### 7.2 错误响应

- 使用统一的错误响应格式
- 提供清晰的错误信息
- 不泄露敏感信息

### 7.3 错误监控

- 监控错误统计
- 设置错误警报
- 分析错误趋势

## 8. 注意事项

- **错误捕获**：确保所有错误都被捕获
- **错误日志**：记录详细错误信息
- **安全性**：不泄露敏感信息
- **性能**：注意错误处理的性能影响

## 9. 常见问题

### 9.1 如何处理异步错误？

使用 asyncHandler 包装异步函数或使用 try-catch。

### 9.2 如何记录错误日志？

使用结构化日志记录错误，包含错误堆栈和上下文。

### 9.3 如何实现错误监控？

使用错误统计和监控服务实现错误监控。

## 10. 实践任务

1. **实现错误中间件**：实现统一的错误处理中间件
2. **实现错误日志**：实现错误日志记录功能
3. **实现错误响应**：实现统一的错误响应格式
4. **实现错误监控**：实现错误统计和监控
5. **优化错误处理**：优化错误处理性能和可维护性

---

**下一节**：[4.13.4 错误响应格式](section-04-response-format.md)
