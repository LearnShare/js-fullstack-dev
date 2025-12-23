# 4.10.1 中间件概述

## 1. 概述

中间件是 Web 框架中的核心概念，用于在请求和响应之间执行代码。中间件可以访问请求对象、响应对象和下一个中间件函数，实现请求处理、响应处理和错误处理等功能。

## 2. 核心概念

### 2.1 中间件的定义

中间件是一个函数，接收三个参数：
- **request**：请求对象
- **response**：响应对象
- **next**：下一个中间件函数

### 2.2 中间件的工作流程

```
请求 → 中间件1 → 中间件2 → 中间件3 → 路由处理 → 响应
```

### 2.3 中间件的执行顺序

中间件按照注册顺序执行，必须调用 `next()` 才能继续执行下一个中间件。

## 3. 中间件类型

### 3.1 应用级中间件

```ts
// 应用级中间件：绑定到 app 对象
app.use((req: Request, res: Response, next: NextFunction): void => {
  console.log('Request received');
  next();
});
```

### 3.2 路由级中间件

```ts
// 路由级中间件：绑定到特定路由
app.get('/users', authMiddleware, (req: Request, res: Response): void => {
  res.json({ users: [] });
});
```

### 3.3 错误处理中间件

```ts
// 错误处理中间件：四个参数
app.use((err: Error, req: Request, res: Response, next: NextFunction): void => {
  console.error(err);
  res.status(500).json({ error: 'Internal server error' });
});
```

## 4. 中间件功能

### 4.1 请求处理

- **日志记录**：记录请求信息
- **认证授权**：验证用户身份
- **数据解析**：解析请求体
- **请求验证**：验证请求数据

### 4.2 响应处理

- **响应格式化**：格式化响应数据
- **响应压缩**：压缩响应数据
- **CORS 处理**：处理跨域请求
- **缓存控制**：设置缓存头

### 4.3 错误处理

- **错误捕获**：捕获和处理错误
- **错误日志**：记录错误信息
- **错误响应**：返回错误响应

## 5. 中间件链

### 5.1 中间件执行

```ts
app.use(middleware1);
app.use(middleware2);
app.use(middleware3);

// 执行顺序：middleware1 → middleware2 → middleware3
```

### 5.2 条件执行

```ts
app.use((req: Request, res: Response, next: NextFunction): void => {
  if (req.path.startsWith('/api')) {
    // 只对 API 路由执行
    next();
  } else {
    next();
  }
});
```

## 6. 注意事项

- **next() 调用**：必须调用 next() 才能继续
- **执行顺序**：中间件按注册顺序执行
- **错误处理**：使用错误处理中间件处理错误
- **性能考虑**：注意中间件的性能影响

## 7. 常见问题

### 7.1 中间件和路由处理器的区别？

中间件在路由处理器之前执行，可以处理请求和响应；路由处理器处理具体的业务逻辑。

### 7.2 如何控制中间件执行顺序？

通过注册顺序控制，先注册的中间件先执行。

### 7.3 如何处理异步中间件？

使用 async/await 或返回 Promise。

## 8. 相关资源

- [Express 中间件文档](https://expressjs.com/en/guide/using-middleware.html)
- [中间件模式](https://en.wikipedia.org/wiki/Middleware)

---

**下一节**：[4.10.2 中间件模式](section-02-patterns.md)
