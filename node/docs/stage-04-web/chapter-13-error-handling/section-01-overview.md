# 4.13.1 错误处理概述

## 1. 概述

错误处理是 Web 应用开发中的重要环节，涉及错误的捕获、分类、处理和响应。良好的错误处理可以提高应用的稳定性、可维护性和用户体验。

## 2. 核心概念

### 2.1 错误处理的目的

- **稳定性**：防止应用崩溃
- **可调试性**：提供错误信息便于调试
- **用户体验**：提供友好的错误提示
- **安全性**：不泄露敏感信息

### 2.2 错误处理的层次

- **应用层错误**：业务逻辑错误
- **框架层错误**：框架相关错误
- **系统层错误**：系统级错误

## 3. 错误类型

### 3.1 客户端错误（4xx）

- **400 Bad Request**：请求参数错误
- **401 Unauthorized**：未认证
- **403 Forbidden**：无权限
- **404 Not Found**：资源不存在
- **409 Conflict**：资源冲突

### 3.2 服务器错误（5xx）

- **500 Internal Server Error**：服务器内部错误
- **502 Bad Gateway**：网关错误
- **503 Service Unavailable**：服务不可用
- **504 Gateway Timeout**：网关超时

## 4. 错误处理流程

### 4.1 错误捕获

```
请求 → 路由处理 → 错误发生 → 错误捕获 → 错误处理 → 错误响应
```

### 4.2 错误传播

```ts
try {
  // 某些操作
  await someOperation();
} catch (error) {
  // 捕获错误并传播
  next(error);
}
```

## 5. 错误处理方式

### 5.1 Try-Catch

```ts
try {
  await someOperation();
} catch (error) {
  console.error('Error:', error);
  res.status(500).json({ error: 'Internal server error' });
}
```

### 5.2 错误中间件

```ts
app.use((err: Error, req: Request, res: Response, next: NextFunction): void => {
  console.error('Error:', err);
  res.status(500).json({ error: 'Internal server error' });
});
```

### 5.3 Promise 错误处理

```ts
app.get('/api/users', async (req: Request, res: Response, next: NextFunction): Promise<void> => {
  try {
    const users = await fetchUsers();
    res.json({ users });
  } catch (error) {
    next(error);
  }
});
```

## 6. 错误处理原则

### 6.1 统一处理

- 使用统一的错误处理中间件
- 使用统一的错误响应格式
- 记录所有错误

### 6.2 错误分类

- 区分客户端错误和服务器错误
- 使用合适的 HTTP 状态码
- 提供清晰的错误信息

### 6.3 安全性

- 不泄露敏感信息
- 不暴露系统内部信息
- 记录详细错误日志

## 7. 注意事项

- **错误捕获**：捕获所有可能的错误
- **错误传播**：正确传播错误到错误处理中间件
- **错误日志**：记录详细错误日志
- **用户体验**：提供友好的错误提示

## 8. 常见问题

### 8.1 如何处理异步错误？

使用 try-catch 或 Promise.catch 处理异步错误。

### 8.2 如何区分不同类型的错误？

使用自定义错误类或错误码区分错误类型。

### 8.3 如何记录错误日志？

使用日志库记录错误，包含错误堆栈和上下文信息。

## 9. 相关资源

- [HTTP 状态码](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [错误处理最佳实践](https://expressjs.com/en/guide/error-handling.html)

---

**下一节**：[4.13.2 错误分类与自定义错误](section-02-error-types.md)
