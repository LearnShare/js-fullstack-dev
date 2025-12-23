# 4.13.4 错误响应格式

## 1. 概述

统一的错误响应格式可以提高 API 的一致性和可维护性。良好的错误响应格式应该包含错误信息、错误码、详细信息等，便于客户端处理和用户理解。

## 2. 错误响应结构

### 2.1 基本结构

```ts
interface ErrorResponse {
  error: {
    code: string;
    message: string;
    details?: unknown;
  };
  timestamp: string;
  path: string;
  requestId?: string;
}
```

### 2.2 详细结构

```ts
interface DetailedErrorResponse {
  error: {
    code: string;
    message: string;
    type: string;
    details?: Array<{
      field?: string;
      message: string;
    }>;
  };
  timestamp: string;
  path: string;
  method: string;
  requestId: string;
  stack?: string; // 仅开发环境
}
```

## 3. 错误响应实现

### 3.1 统一错误响应

```ts
function createErrorResponse(err: Error, req: Request): ErrorResponse {
  const requestId = req.headers['x-request-id'] as string || generateRequestId();
  
  if (err instanceof ValidationError) {
    return {
      error: {
        code: 'VALIDATION_ERROR',
        message: 'Validation failed',
        details: err.errors
      },
      timestamp: new Date().toISOString(),
      path: req.path,
      requestId
    };
  }
  
  if (err instanceof AuthenticationError) {
    return {
      error: {
        code: 'AUTHENTICATION_ERROR',
        message: err.message
      },
      timestamp: new Date().toISOString(),
      path: req.path,
      requestId
    };
  }
  
  if (err instanceof NotFoundError) {
    return {
      error: {
        code: 'NOT_FOUND',
        message: err.message
      },
      timestamp: new Date().toISOString(),
      path: req.path,
      requestId
    };
  }
  
  // 默认错误
  return {
    error: {
      code: 'INTERNAL_ERROR',
      message: process.env.NODE_ENV === 'production' ? 'Internal server error' : err.message
    },
    timestamp: new Date().toISOString(),
    path: req.path,
    requestId
  };
}
```

### 3.2 错误中间件

```ts
app.use((err: Error, req: Request, res: Response, next: NextFunction): void => {
  const errorResponse = createErrorResponse(err, req);
  const statusCode = err instanceof AppError ? err.statusCode : 500;
  
  res.status(statusCode).json(errorResponse);
});
```

## 4. 不同错误的响应

### 4.1 验证错误

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Validation failed",
    "details": [
      {
        "field": "email",
        "message": "Invalid email format"
      },
      {
        "field": "password",
        "message": "Password must be at least 8 characters"
      }
    ]
  },
  "timestamp": "2025-12-22T10:00:00.000Z",
  "path": "/api/users",
  "requestId": "req-123"
}
```

### 4.2 认证错误

```json
{
  "error": {
    "code": "AUTHENTICATION_ERROR",
    "message": "Invalid token"
  },
  "timestamp": "2025-12-22T10:00:00.000Z",
  "path": "/api/protected",
  "requestId": "req-124"
}
```

### 4.3 资源错误

```json
{
  "error": {
    "code": "NOT_FOUND",
    "message": "User not found"
  },
  "timestamp": "2025-12-22T10:00:00.000Z",
  "path": "/api/users/123",
  "requestId": "req-125"
}
```

## 5. 错误响应头

### 5.1 标准响应头

```ts
function setErrorHeaders(res: Response, err: Error): void {
  res.setHeader('X-Error-Code', err instanceof AppError ? err.code?.toString() || 'UNKNOWN' : 'INTERNAL_ERROR');
  res.setHeader('X-Request-ID', res.locals.requestId || generateRequestId());
  
  if (err instanceof RateLimitError) {
    res.setHeader('Retry-After', '60');
  }
}
```

## 6. 最佳实践

### 6.1 响应格式

- 使用统一的错误响应格式
- 包含错误码和错误信息
- 提供错误详情（如验证错误）

### 6.2 错误信息

- 提供用户友好的错误信息
- 不泄露敏感信息
- 包含错误上下文

### 6.3 错误码

- 使用有意义的错误码
- 错误码与 HTTP 状态码对应
- 文档化错误码

## 7. 注意事项

- **一致性**：保持错误响应格式一致
- **安全性**：不泄露敏感信息
- **可维护性**：保持错误响应清晰
- **文档化**：文档化错误响应格式

## 8. 常见问题

### 8.1 如何设计错误响应格式？

根据 API 需求和客户端需求设计统一的错误响应格式。

### 8.2 如何处理错误详情？

根据错误类型提供不同的错误详情，如验证错误提供字段级错误。

### 8.3 如何实现错误码系统？

使用枚举或常量定义错误码，与 HTTP 状态码对应。

## 9. 实践任务

1. **设计错误响应格式**：设计统一的错误响应格式
2. **实现错误响应**：实现错误响应生成函数
3. **实现错误码系统**：实现错误码定义和使用
4. **实现错误文档**：文档化错误响应格式
5. **优化错误响应**：优化错误响应设计和实现

---

**下一章**：[4.14 API 测试工具](../chapter-14-api-testing/readme.md)
