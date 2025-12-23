# 4.10.4 中间件最佳实践

## 1. 概述

中间件最佳实践包括中间件设计、错误处理、性能优化、安全性等方面。遵循最佳实践可以提升应用的稳定性、性能和可维护性。

## 2. 设计原则

### 2.1 单一职责

```ts
// ✅ 好的设计：单一职责
function loggerMiddleware(req: Request, res: Response, next: NextFunction): void {
  console.log(`${req.method} ${req.path}`);
  next();
}

function authMiddleware(req: Request, res: Response, next: NextFunction): void {
  // 认证逻辑
  next();
}

// ❌ 不好的设计：多个职责
function complexMiddleware(req: Request, res: Response, next: NextFunction): void {
  // 日志
  console.log(`${req.method} ${req.path}`);
  // 认证
  // 验证
  // 缓存
  next();
}
```

### 2.2 可配置性

```ts
// ✅ 好的设计：可配置
function createLoggerMiddleware(options: { format: string; level: string }) {
  return (req: Request, res: Response, next: NextFunction): void => {
    if (options.level === 'debug') {
      console.log(`[${options.format}] ${req.method} ${req.path}`);
    }
    next();
  };
}

// ❌ 不好的设计：硬编码
function loggerMiddleware(req: Request, res: Response, next: NextFunction): void {
  console.log(`${req.method} ${req.path}`); // 格式硬编码
  next();
}
```

## 3. 错误处理

### 3.1 异步错误处理

```ts
// ✅ 好的设计：正确处理异步错误
async function asyncMiddleware(req: Request, res: Response, next: NextFunction): Promise<void> {
  try {
    await someAsyncOperation();
    next();
  } catch (error) {
    next(error);
  }
}

// ❌ 不好的设计：未处理错误
async function badAsyncMiddleware(req: Request, res: Response, next: NextFunction): Promise<void> {
  await someAsyncOperation(); // 错误未处理
  next();
}
```

### 3.2 错误传播

```ts
// ✅ 好的设计：错误传播到错误处理中间件
function errorPropagatingMiddleware(req: Request, res: Response, next: NextFunction): void {
  try {
    // 某些操作
    if (someCondition) {
      throw new Error('Something went wrong');
    }
    next();
  } catch (error) {
    next(error); // 传播错误
  }
}
```

## 4. 性能优化

### 4.1 避免阻塞操作

```ts
// ✅ 好的设计：异步非阻塞
async function nonBlockingMiddleware(req: Request, res: Response, next: NextFunction): Promise<void> {
  await someAsyncOperation();
  next();
}

// ❌ 不好的设计：同步阻塞
function blockingMiddleware(req: Request, res: Response, next: NextFunction): void {
  // 同步阻塞操作
  const result = expensiveSyncOperation();
  next();
}
```

### 4.2 缓存优化

```ts
// ✅ 好的设计：使用缓存
const cache = new Map<string, unknown>();

function cachedMiddleware(req: Request, res: Response, next: NextFunction): void {
  const cacheKey = req.path;
  const cached = cache.get(cacheKey);
  
  if (cached) {
    return res.json(cached);
  }
  
  // 计算并缓存
  const result = computeResult();
  cache.set(cacheKey, result);
  res.json(result);
}
```

## 5. 安全性

### 5.1 输入验证

```ts
// ✅ 好的设计：验证输入
function validatedMiddleware(req: Request, res: Response, next: NextFunction): void {
  const { email } = req.body;
  
  if (!email || !isValidEmail(email)) {
    return res.status(400).json({ error: 'Invalid email' });
  }
  
  next();
}
```

### 5.2 敏感信息处理

```ts
// ✅ 好的设计：不记录敏感信息
function secureLoggerMiddleware(req: Request, res: Response, next: NextFunction): void {
  const sanitizedBody = { ...req.body };
  delete sanitizedBody.password;
  delete sanitizedBody.token;
  
  console.log('Request:', {
    method: req.method,
    path: req.path,
    body: sanitizedBody
  });
  
  next();
}
```

## 6. 可测试性

### 6.1 纯函数设计

```ts
// ✅ 好的设计：可测试的纯函数
function pureMiddleware(req: Request, res: Response, next: NextFunction): void {
  const result = processRequest(req);
  req.processed = result;
  next();
}

function processRequest(req: Request): unknown {
  // 纯函数，易于测试
  return { processed: true };
}
```

### 6.2 依赖注入

```ts
// ✅ 好的设计：依赖注入
function createAuthMiddleware(verifyToken: (token: string) => Promise<unknown>) {
  return async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    const token = req.headers.authorization;
    const user = await verifyToken(token || '');
    req.user = user;
    next();
  };
}

// 测试时可以注入 mock 函数
const testMiddleware = createAuthMiddleware(mockVerifyToken);
```

## 7. 中间件组织

### 7.1 按功能组织

```ts
// middleware/auth.ts
export function authMiddleware(req: Request, res: Response, next: NextFunction): void {
  // 认证逻辑
}

// middleware/logger.ts
export function loggerMiddleware(req: Request, res: Response, next: NextFunction): void {
  // 日志逻辑
}

// app.ts
import { authMiddleware } from './middleware/auth';
import { loggerMiddleware } from './middleware/logger';

app.use(loggerMiddleware);
app.use('/api', authMiddleware);
```

### 7.2 中间件组合

```ts
// middleware/index.ts
import { authMiddleware } from './auth';
import { loggerMiddleware } from './logger';
import { errorHandler } from './error';

export const commonMiddlewares = [
  loggerMiddleware,
  errorHandler
];

export const protectedMiddlewares = [
  ...commonMiddlewares,
  authMiddleware
];
```

## 8. 最佳实践总结

### 8.1 设计原则

- **单一职责**：每个中间件只做一件事
- **可配置性**：使用工厂函数创建可配置中间件
- **可测试性**：编写可测试的中间件

### 8.2 错误处理

- **异步错误**：正确处理异步错误
- **错误传播**：使用 next(error) 传播错误
- **错误日志**：记录错误信息

### 8.3 性能优化

- **避免阻塞**：避免同步阻塞操作
- **使用缓存**：合理使用缓存
- **优化顺序**：优化中间件执行顺序

### 8.4 安全性

- **输入验证**：验证所有输入
- **敏感信息**：不记录敏感信息
- **权限检查**：实现权限检查

## 9. 注意事项

- **next() 调用**：必须调用 next() 才能继续
- **错误处理**：正确处理错误
- **性能影响**：注意中间件的性能影响
- **可维护性**：保持代码清晰和文档化

## 10. 常见问题

### 10.1 如何组织中间件？

按功能模块组织，使用中间件组合。

### 10.2 如何优化中间件性能？

避免阻塞操作，使用缓存，优化执行顺序。

### 10.3 如何测试中间件？

使用依赖注入，编写纯函数，使用 mock 对象。

## 11. 实践任务

1. **重构中间件**：重构现有中间件遵循最佳实践
2. **实现错误处理**：实现完善的错误处理机制
3. **优化性能**：优化中间件性能
4. **提高安全性**：提高中间件安全性
5. **编写测试**：为中间件编写单元测试

---

**下一章**：[4.11 路由设计](../chapter-11-routing/readme.md)
