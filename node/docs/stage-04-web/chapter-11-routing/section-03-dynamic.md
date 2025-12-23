# 4.11.3 动态路由与参数

## 1. 概述

动态路由允许在 URL 路径中使用参数，实现灵活的路由匹配。动态路由参数可以用于资源标识、过滤条件等场景。

## 2. 路径参数

### 2.1 基本路径参数

```ts
// Express
app.get('/users/:id', (req: Request, res: Response): void => {
  const { id } = req.params;
  res.json({ userId: id });
});

// Fastify
fastify.get('/users/:id', async (request: FastifyRequest<{ Params: { id: string } }>, reply: FastifyReply): Promise<void> => {
  const { id } = request.params;
  reply.send({ userId: id });
});
```

### 2.2 多个路径参数

```ts
app.get('/users/:userId/posts/:postId', (req: Request, res: Response): void => {
  const { userId, postId } = req.params;
  res.json({ userId, postId });
});
```

### 2.3 可选参数

```ts
// Express 不支持真正的可选参数，可以使用多个路由
app.get('/users/:id', getUserById);
app.get('/users', getUsers);

// 或使用查询参数
app.get('/users/:id?', (req: Request, res: Response): void => {
  const { id } = req.params;
  if (id) {
    return getUserById(req, res);
  }
  return getUsers(req, res);
});
```

## 3. 参数验证

### 3.1 基本验证

```ts
app.get('/users/:id', (req: Request, res: Response): void => {
  const { id } = req.params;
  
  // 验证 ID 格式
  if (!/^\d+$/.test(id)) {
    return res.status(400).json({ error: 'Invalid user ID' });
  }
  
  const userId = parseInt(id, 10);
  res.json({ userId });
});
```

### 3.2 使用验证中间件

```ts
import { param, validationResult } from 'express-validator';

app.get('/users/:id',
  param('id').isInt().withMessage('ID must be an integer'),
  (req: Request, res: Response): void => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }
    
    const { id } = req.params;
    res.json({ userId: parseInt(id, 10) });
  }
);
```

### 3.3 使用 Zod 验证

```ts
import { z } from 'zod';

const paramsSchema = z.object({
  id: z.string().transform((val) => parseInt(val, 10)).pipe(z.number().int().positive())
});

app.get('/users/:id', (req: Request, res: Response): void => {
  try {
    const { id } = paramsSchema.parse(req.params);
    res.json({ userId: id });
  } catch (error) {
    if (error instanceof z.ZodError) {
      return res.status(400).json({ errors: error.errors });
    }
    throw error;
  }
});
```

## 4. 查询参数

### 4.1 基本查询参数

```ts
app.get('/users', (req: Request, res: Response): void => {
  const { page, limit } = req.query;
  const pageNum = page ? parseInt(page as string, 10) : 1;
  const limitNum = limit ? parseInt(limit as string, 10) : 10;
  
  res.json({ page: pageNum, limit: limitNum });
});
```

### 4.2 查询参数验证

```ts
import { query } from 'express-validator';

app.get('/users',
  query('page').optional().isInt({ min: 1 }).withMessage('Page must be a positive integer'),
  query('limit').optional().isInt({ min: 1, max: 100 }).withMessage('Limit must be between 1 and 100'),
  (req: Request, res: Response): void => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }
    
    const { page, limit } = req.query;
    res.json({ page, limit });
  }
);
```

## 5. 通配符路由

### 5.1 通配符匹配

```ts
// 匹配所有路径
app.get('*', (req: Request, res: Response): void => {
  res.status(404).json({ error: 'Not Found' });
});

// 匹配特定前缀
app.get('/api/*', (req: Request, res: Response): void => {
  res.json({ message: 'API route' });
});
```

### 5.2 正则表达式路由

```ts
// 匹配数字 ID
app.get(/^\/users\/(\d+)$/, (req: Request, res: Response): void => {
  const id = req.params[0];
  res.json({ userId: id });
});
```

## 6. 路由优先级

### 6.1 具体路由优先

```ts
// 具体路由在前
app.get('/users/me', getCurrentUser);
app.get('/users/:id', getUserById);
```

### 6.2 路由顺序

```ts
// 路由按注册顺序匹配
app.get('/users/new', showNewUserForm); // 必须在 /users/:id 之前
app.get('/users/:id', getUserById);
```

## 7. 参数类型转换

### 7.1 数字转换

```ts
app.get('/users/:id', (req: Request, res: Response): void => {
  const { id } = req.params;
  const userId = parseInt(id, 10);
  
  if (isNaN(userId)) {
    return res.status(400).json({ error: 'Invalid user ID' });
  }
  
  res.json({ userId });
});
```

### 7.2 使用中间件转换

```ts
function parseIdParam(req: Request, res: Response, next: NextFunction): void {
  const { id } = req.params;
  const userId = parseInt(id, 10);
  
  if (isNaN(userId)) {
    return res.status(400).json({ error: 'Invalid user ID' });
  }
  
  req.params.id = userId.toString();
  next();
}

app.get('/users/:id', parseIdParam, getUserById);
```

## 8. 最佳实践

### 8.1 参数验证

- 验证所有路径参数
- 验证查询参数类型
- 提供清晰的错误信息

### 8.2 类型安全

- 使用 TypeScript 类型定义
- 实现参数类型转换
- 使用验证库

### 8.3 路由设计

- 使用有意义的参数名
- 保持路由简洁
- 避免过度嵌套

## 9. 注意事项

- **参数验证**：验证所有路径参数
- **类型转换**：正确转换参数类型
- **路由顺序**：注意路由匹配顺序
- **性能**：注意路由匹配性能

## 10. 常见问题

### 10.1 如何处理可选参数？

使用多个路由或查询参数实现可选参数。

### 10.2 如何验证路径参数？

使用验证中间件或验证库验证路径参数。

### 10.3 如何处理参数类型转换？

使用中间件或验证库实现参数类型转换。

## 11. 实践任务

1. **实现动态路由**：实现带参数的动态路由
2. **实现参数验证**：实现路径参数和查询参数验证
3. **实现类型转换**：实现参数类型转换
4. **实现嵌套路由**：实现嵌套资源路由
5. **优化路由匹配**：优化路由匹配性能

---

**下一节**：[4.11.4 路由守卫与权限控制](section-04-guards.md)
