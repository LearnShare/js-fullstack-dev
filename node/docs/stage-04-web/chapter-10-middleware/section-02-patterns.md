# 4.10.2 中间件模式

## 1. 概述

中间件模式是中间件设计和实现的方式。不同的中间件模式适用于不同的场景，理解这些模式有助于编写更好的中间件。

## 2. 基本模式

### 2.1 同步中间件

```ts
function loggerMiddleware(req: Request, res: Response, next: NextFunction): void {
  console.log(`${req.method} ${req.path}`);
  next();
}

app.use(loggerMiddleware);
```

### 2.2 异步中间件

```ts
async function authMiddleware(req: Request, res: Response, next: NextFunction): Promise<void> {
  try {
    const token = req.headers.authorization;
    const user = await verifyToken(token);
    req.user = user;
    next();
  } catch (error) {
    res.status(401).json({ error: 'Unauthorized' });
  }
}

app.use(authMiddleware);
```

### 2.3 条件中间件

```ts
function conditionalMiddleware(condition: (req: Request) => boolean) {
  return (req: Request, res: Response, next: NextFunction): void => {
    if (condition(req)) {
      // 执行某些逻辑
    }
    next();
  };
}

app.use(conditionalMiddleware((req: Request) => req.path.startsWith('/api')));
```

## 3. 功能模式

### 3.1 日志中间件

```ts
function loggerMiddleware(req: Request, res: Response, next: NextFunction): void {
  const start = Date.now();
  
  res.on('finish', (): void => {
    const duration = Date.now() - start;
    console.log(`${req.method} ${req.path} ${res.statusCode} ${duration}ms`);
  });
  
  next();
}

app.use(loggerMiddleware);
```

### 3.2 认证中间件

```ts
async function authMiddleware(req: Request, res: Response, next: NextFunction): Promise<void> {
  const token = req.headers.authorization?.replace('Bearer ', '');
  
  if (!token) {
    return res.status(401).json({ error: 'No token provided' });
  }
  
  try {
    const decoded = await verifyToken(token);
    req.user = decoded;
    next();
  } catch (error) {
    res.status(401).json({ error: 'Invalid token' });
  }
}

app.use('/api/protected', authMiddleware);
```

### 3.3 错误处理中间件

```ts
function errorHandler(err: Error, req: Request, res: Response, next: NextFunction): void {
  console.error('Error:', err);
  
  if (err instanceof ValidationError) {
    return res.status(400).json({ error: err.message });
  }
  
  if (err instanceof AuthenticationError) {
    return res.status(401).json({ error: err.message });
  }
  
  res.status(500).json({ error: 'Internal server error' });
}

app.use(errorHandler);
```

## 4. 组合模式

### 4.1 中间件组合

```ts
function combineMiddlewares(...middlewares: Array<(req: Request, res: Response, next: NextFunction) => void>) {
  return (req: Request, res: Response, next: NextFunction): void => {
    let index = 0;
    
    function runNext(): void {
      if (index < middlewares.length) {
        middlewares[index++](req, res, runNext);
      } else {
        next();
      }
    }
    
    runNext();
  };
}

app.use(combineMiddlewares(middleware1, middleware2, middleware3));
```

### 4.2 中间件工厂

```ts
function createAuthMiddleware(options: { required: boolean }) {
  return async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    const token = req.headers.authorization?.replace('Bearer ', '');
    
    if (!token) {
      if (options.required) {
        return res.status(401).json({ error: 'Authentication required' });
      } else {
        return next();
      }
    }
    
    try {
      const user = await verifyToken(token);
      req.user = user;
      next();
    } catch (error) {
      if (options.required) {
        return res.status(401).json({ error: 'Invalid token' });
      } else {
        next();
      }
    }
  };
}

app.use(createAuthMiddleware({ required: true }));
```

## 5. 高级模式

### 5.1 中间件链

```ts
class MiddlewareChain {
  private middlewares: Array<(req: Request, res: Response, next: NextFunction) => void> = [];

  use(middleware: (req: Request, res: Response, next: NextFunction) => void): this {
    this.middlewares.push(middleware);
    return this;
  }

  execute(req: Request, res: Response, finalHandler: (req: Request, res: Response) => void): void {
    let index = 0;
    
    const next = (): void => {
      if (index < this.middlewares.length) {
        this.middlewares[index++](req, res, next);
      } else {
        finalHandler(req, res);
      }
    };
    
    next();
  }
}

const chain = new MiddlewareChain();
chain.use(middleware1).use(middleware2).use(middleware3);
```

### 5.2 中间件装饰器

```ts
function middlewareDecorator(middleware: (req: Request, res: Response, next: NextFunction) => void) {
  return function (target: any, propertyKey: string, descriptor: PropertyDescriptor): void {
    const originalMethod = descriptor.value;
    
    descriptor.value = function (req: Request, res: Response): void {
      middleware(req, res, (): void => {
        originalMethod.call(this, req, res);
      });
    };
  };
}

class UserController {
  @middlewareDecorator(authMiddleware)
  getUsers(req: Request, res: Response): void {
    res.json({ users: [] });
  }
}
```

## 6. 最佳实践

### 6.1 中间件设计

- 保持中间件单一职责
- 使用中间件工厂创建可配置中间件
- 实现错误处理

### 6.2 性能优化

- 避免在中间件中执行耗时操作
- 使用缓存减少重复计算
- 优化中间件执行顺序

### 6.3 可维护性

- 提供清晰的文档
- 使用类型定义
- 实现错误处理

## 7. 注意事项

- **next() 调用**：必须调用 next() 才能继续
- **错误处理**：正确处理错误
- **性能**：注意中间件的性能影响
- **可测试性**：编写可测试的中间件

## 8. 常见问题

### 8.1 如何实现条件中间件？

使用中间件工厂函数，根据条件返回不同的中间件。

### 8.2 如何处理异步中间件？

使用 async/await 或返回 Promise。

### 8.3 如何组合多个中间件？

使用中间件组合函数或中间件链。

## 9. 实践任务

1. **实现日志中间件**：实现请求日志记录中间件
2. **实现认证中间件**：实现用户认证中间件
3. **实现错误处理中间件**：实现统一的错误处理中间件
4. **实现中间件工厂**：实现可配置的中间件工厂
5. **优化中间件性能**：优化中间件执行性能

---

**下一节**：[4.10.3 编写自定义中间件](section-03-custom.md)
