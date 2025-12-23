# 4.10.3 编写自定义中间件

## 1. 概述

编写自定义中间件是 Web 开发中的常见需求。自定义中间件可以根据项目需求实现特定的功能，如认证、日志、数据验证等。

## 2. 基本中间件

### 2.1 简单中间件

```ts
import { Request, Response, NextFunction } from 'express';

function simpleMiddleware(req: Request, res: Response, next: NextFunction): void {
  console.log('Simple middleware executed');
  next();
}

app.use(simpleMiddleware);
```

### 2.2 带配置的中间件

```ts
function configurableMiddleware(options: { prefix: string }) {
  return (req: Request, res: Response, next: NextFunction): void => {
    console.log(`[${options.prefix}] ${req.method} ${req.path}`);
    next();
  };
}

app.use(configurableMiddleware({ prefix: 'API' }));
```

## 3. 认证中间件

### 3.1 JWT 认证

```ts
import { verify } from 'jsonwebtoken';

interface AuthRequest extends Request {
  user?: { id: string; email: string };
}

function jwtAuthMiddleware(req: AuthRequest, res: Response, next: NextFunction): void {
  const token = req.headers.authorization?.replace('Bearer ', '');
  
  if (!token) {
    return res.status(401).json({ error: 'No token provided' });
  }
  
  try {
    const decoded = verify(token, process.env.JWT_SECRET!) as { id: string; email: string };
    req.user = decoded;
    next();
  } catch (error) {
    res.status(401).json({ error: 'Invalid token' });
  }
}

app.use('/api/protected', jwtAuthMiddleware);
```

### 3.2 角色验证中间件

```ts
function roleMiddleware(allowedRoles: string[]) {
  return (req: AuthRequest, res: Response, next: NextFunction): void => {
    if (!req.user) {
      return res.status(401).json({ error: 'Unauthorized' });
    }
    
    if (!allowedRoles.includes(req.user.role)) {
      return res.status(403).json({ error: 'Forbidden' });
    }
    
    next();
  };
}

app.get('/api/admin', jwtAuthMiddleware, roleMiddleware(['admin']), (req: Request, res: Response): void => {
  res.json({ message: 'Admin access granted' });
});
```

## 4. 日志中间件

### 4.1 请求日志

```ts
function requestLoggerMiddleware(req: Request, res: Response, next: NextFunction): void {
  const start = Date.now();
  const { method, path, ip } = req;
  
  res.on('finish', (): void => {
    const duration = Date.now() - start;
    const { statusCode } = res;
    console.log(`${method} ${path} ${statusCode} ${duration}ms - ${ip}`);
  });
  
  next();
}

app.use(requestLoggerMiddleware);
```

### 4.2 结构化日志

```ts
interface LogEntry {
  timestamp: string;
  method: string;
  path: string;
  statusCode: number;
  duration: number;
  ip: string;
}

function structuredLoggerMiddleware(req: Request, res: Response, next: NextFunction): void {
  const start = Date.now();
  
  res.on('finish', (): void => {
    const logEntry: LogEntry = {
      timestamp: new Date().toISOString(),
      method: req.method,
      path: req.path,
      statusCode: res.statusCode,
      duration: Date.now() - start,
      ip: req.ip
    };
    
    console.log(JSON.stringify(logEntry));
  });
  
  next();
}
```

## 5. 数据验证中间件

### 5.1 请求体验证

```ts
import { z } from 'zod';

function validateBodyMiddleware(schema: z.ZodSchema) {
  return (req: Request, res: Response, next: NextFunction): void => {
    try {
      req.body = schema.parse(req.body);
      next();
    } catch (error) {
      if (error instanceof z.ZodError) {
        return res.status(400).json({
          error: 'Validation failed',
          details: error.errors
        });
      }
      next(error);
    }
  };
}

const createUserSchema = z.object({
  name: z.string().min(1),
  email: z.string().email()
});

app.post('/api/users', validateBodyMiddleware(createUserSchema), (req: Request, res: Response): void => {
  // req.body 已经验证
  res.json({ message: 'User created' });
});
```

### 5.2 查询参数验证

```ts
function validateQueryMiddleware(schema: z.ZodSchema) {
  return (req: Request, res: Response, next: NextFunction): void => {
    try {
      req.query = schema.parse(req.query);
      next();
    } catch (error) {
      if (error instanceof z.ZodError) {
        return res.status(400).json({
          error: 'Invalid query parameters',
          details: error.errors
        });
      }
      next(error);
    }
  };
}

const paginationSchema = z.object({
  page: z.string().transform((val) => parseInt(val, 10)).pipe(z.number().int().positive()),
  limit: z.string().transform((val) => parseInt(val, 10)).pipe(z.number().int().positive().max(100))
});

app.get('/api/users', validateQueryMiddleware(paginationSchema), (req: Request, res: Response): void => {
  const { page, limit } = req.query as { page: number; limit: number };
  res.json({ page, limit });
});
```

## 6. 缓存中间件

### 6.1 响应缓存

```ts
const cache = new Map<string, { data: unknown; expires: number }>();

function cacheMiddleware(ttl: number = 60000) {
  return (req: Request, res: Response, next: NextFunction): void => {
    const cacheKey = `${req.method}:${req.path}`;
    const cached = cache.get(cacheKey);
    
    if (cached && cached.expires > Date.now()) {
      return res.json(cached.data);
    }
    
    const originalJson = res.json.bind(res);
    res.json = function (data: unknown): Response {
      cache.set(cacheKey, {
        data,
        expires: Date.now() + ttl
      });
      return originalJson(data);
    };
    
    next();
  };
}

app.get('/api/users', cacheMiddleware(60000), (req: Request, res: Response): void => {
  res.json({ users: [] });
});
```

## 7. 性能监控中间件

### 7.1 响应时间监控

```ts
function performanceMiddleware(req: Request, res: Response, next: NextFunction): void {
  const start = process.hrtime.bigint();
  
  res.on('finish', (): void => {
    const duration = Number(process.hrtime.bigint() - start) / 1e6; // 转换为毫秒
    const { method, path } = req;
    const { statusCode } = res;
    
    if (duration > 1000) {
      console.warn(`Slow request: ${method} ${path} took ${duration.toFixed(2)}ms`);
    }
    
    // 记录性能指标
    recordMetric('request.duration', duration, { method, path, statusCode });
  });
  
  next();
}
```

## 8. 最佳实践

### 8.1 中间件设计

- 保持单一职责
- 使用类型定义
- 实现错误处理
- 提供配置选项

### 8.2 错误处理

- 使用 try-catch 处理异步错误
- 提供清晰的错误信息
- 记录错误日志

### 8.3 性能优化

- 避免阻塞操作
- 使用缓存
- 优化资源清理

## 9. 注意事项

- **next() 调用**：必须调用 next() 才能继续
- **错误处理**：正确处理错误
- **类型安全**：使用 TypeScript 类型定义
- **可测试性**：编写可测试的中间件

## 10. 常见问题

### 10.1 如何处理异步操作？

使用 async/await 或返回 Promise。

### 10.2 如何传递数据到下一个中间件？

使用 req 对象添加属性。

### 10.3 如何实现条件中间件？

使用中间件工厂函数，根据条件返回不同的中间件。

## 11. 实践任务

1. **实现认证中间件**：实现 JWT 认证中间件
2. **实现日志中间件**：实现请求日志记录中间件
3. **实现验证中间件**：实现请求数据验证中间件
4. **实现缓存中间件**：实现响应缓存中间件
5. **实现性能监控中间件**：实现性能监控中间件

---

**下一节**：[4.10.4 中间件最佳实践](section-04-best-practices.md)
