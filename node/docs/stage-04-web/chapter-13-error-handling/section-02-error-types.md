# 4.13.2 错误分类与自定义错误

## 1. 概述

错误分类和自定义错误类是错误处理的基础。通过定义不同类型的错误类，可以更好地分类和处理错误，提供清晰的错误信息和合适的 HTTP 状态码。

## 2. 错误分类

### 2.1 应用错误

- **验证错误**：数据验证失败
- **业务错误**：业务逻辑错误
- **权限错误**：权限不足

### 2.2 系统错误

- **数据库错误**：数据库操作失败
- **网络错误**：网络请求失败
- **系统错误**：系统级错误

## 3. 自定义错误类

### 3.1 基础错误类

```ts
class AppError extends Error {
  public statusCode: number;
  public isOperational: boolean;

  constructor(message: string, statusCode: number = 500) {
    super(message);
    this.statusCode = statusCode;
    this.isOperational = true;
    Error.captureStackTrace(this, this.constructor);
  }
}
```

### 3.2 验证错误

```ts
class ValidationError extends AppError {
  public errors: Array<{ field: string; message: string }>;

  constructor(errors: Array<{ field: string; message: string }>) {
    super('Validation failed', 400);
    this.errors = errors;
    this.name = 'ValidationError';
  }
}
```

### 3.3 认证错误

```ts
class AuthenticationError extends AppError {
  constructor(message: string = 'Authentication required') {
    super(message, 401);
    this.name = 'AuthenticationError';
  }
}

class AuthorizationError extends AppError {
  constructor(message: string = 'Insufficient permissions') {
    super(message, 403);
    this.name = 'AuthorizationError';
  }
}
```

### 3.4 资源错误

```ts
class NotFoundError extends AppError {
  constructor(resource: string = 'Resource') {
    super(`${resource} not found`, 404);
    this.name = 'NotFoundError';
  }
}

class ConflictError extends AppError {
  constructor(message: string = 'Resource conflict') {
    super(message, 409);
    this.name = 'ConflictError';
  }
}
```

### 3.5 业务错误

```ts
class BusinessError extends AppError {
  public code: string;

  constructor(message: string, code: string, statusCode: number = 400) {
    super(message, statusCode);
    this.code = code;
    this.name = 'BusinessError';
  }
}
```

## 4. 错误使用

### 4.1 抛出错误

```ts
// 验证错误
if (!email || !isValidEmail(email)) {
  throw new ValidationError([
    { field: 'email', message: 'Invalid email format' }
  ]);
}

// 认证错误
if (!token || !isValidToken(token)) {
  throw new AuthenticationError('Invalid token');
}

// 资源错误
const user = await getUserById(id);
if (!user) {
  throw new NotFoundError('User');
}
```

### 4.2 错误处理

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

## 5. 错误码系统

### 5.1 错误码定义

```ts
enum ErrorCode {
  // 验证错误 (40000-40099)
  VALIDATION_ERROR = 40000,
  INVALID_EMAIL = 40001,
  INVALID_PASSWORD = 40002,
  
  // 认证错误 (40100-40199)
  AUTHENTICATION_REQUIRED = 40100,
  INVALID_TOKEN = 40101,
  TOKEN_EXPIRED = 40102,
  
  // 权限错误 (40300-40399)
  INSUFFICIENT_PERMISSIONS = 40300,
  RESOURCE_ACCESS_DENIED = 40301,
  
  // 资源错误 (40400-40499)
  RESOURCE_NOT_FOUND = 40400,
  USER_NOT_FOUND = 40401,
  
  // 业务错误 (40900-40999)
  RESOURCE_CONFLICT = 40900,
  EMAIL_ALREADY_EXISTS = 40901,
  
  // 服务器错误 (50000-50099)
  INTERNAL_ERROR = 50000,
  DATABASE_ERROR = 50001,
  EXTERNAL_SERVICE_ERROR = 50002
}
```

### 5.2 使用错误码

```ts
class AppError extends Error {
  public statusCode: number;
  public code: number;
  public isOperational: boolean;

  constructor(message: string, statusCode: number, code: number) {
    super(message);
    this.statusCode = statusCode;
    this.code = code;
    this.isOperational = true;
    Error.captureStackTrace(this, this.constructor);
  }
}

class ValidationError extends AppError {
  constructor(message: string = 'Validation failed') {
    super(message, 400, ErrorCode.VALIDATION_ERROR);
    this.name = 'ValidationError';
  }
}
```

## 6. 最佳实践

### 6.1 错误分类

- 使用自定义错误类分类错误
- 使用错误码标识错误类型
- 提供清晰的错误信息

### 6.2 错误处理

- 区分可操作错误和系统错误
- 使用合适的 HTTP 状态码
- 记录详细错误日志

### 6.3 错误信息

- 提供用户友好的错误信息
- 不泄露敏感信息
- 包含错误上下文

## 7. 注意事项

- **错误分类**：合理分类错误类型
- **错误信息**：提供清晰的错误信息
- **安全性**：不泄露敏感信息
- **可维护性**：保持错误类清晰

## 8. 常见问题

### 8.1 如何设计错误类层次？

根据错误类型和业务需求设计错误类层次。

### 8.2 如何使用错误码？

使用错误码标识错误类型，便于错误处理和监控。

### 8.3 如何处理错误上下文？

在错误类中包含上下文信息，便于错误追踪。

## 9. 实践任务

1. **定义错误类**：定义各种自定义错误类
2. **实现错误码系统**：实现错误码定义和使用
3. **实现错误抛出**：在业务逻辑中抛出错误
4. **实现错误处理**：实现错误捕获和处理
5. **优化错误信息**：优化错误信息设计

---

**下一节**：[4.13.3 错误中间件](section-03-error-middleware.md)
