# 4.3.2 RESTful API

## 1. 概述

RESTful API 是基于 REST（Representational State Transfer）架构风格的 API 设计方式。RESTful API 使用标准 HTTP 方法操作资源，是 Web API 设计的主流范式。

## 2. 特性说明

- **资源导向**：将数据视为资源，使用 URL 标识资源
- **标准 HTTP 方法**：使用 GET、POST、PUT、DELETE 等标准方法
- **无状态**：每个请求包含所有必要信息
- **统一接口**：使用标准的 HTTP 方法和状态码
- **可缓存**：支持 HTTP 缓存机制

## 3. RESTful 设计原则

### 3.1 资源设计

资源应该使用名词，使用复数形式：

```ts
// ✅ 正确
GET /api/users
GET /api/users/123
POST /api/users

// ❌ 错误
GET /api/getUsers
GET /api/user/123
POST /api/createUser
```

### 3.2 HTTP 方法使用

| 方法     | 用途           | 幂等性 | 安全性 |
|:---------|:---------------|:-------|:-------|
| **GET**  | 获取资源       | 是     | 是     |
| **POST** | 创建资源       | 否     | 否     |
| **PUT**  | 完整更新资源   | 是     | 否     |
| **PATCH** | 部分更新资源 | 是     | 否     |
| **DELETE** | 删除资源     | 是     | 否     |

### 3.3 状态码使用

使用标准 HTTP 状态码：

| 状态码 | 含义           | 使用场景                     |
|:-------|:---------------|:-----------------------------|
| **200** | OK             | 成功获取资源                 |
| **201** | Created        | 成功创建资源                 |
| **204** | No Content     | 成功删除资源                 |
| **400** | Bad Request    | 请求参数错误                 |
| **401** | Unauthorized   | 未认证                       |
| **403** | Forbidden      | 无权限                       |
| **404** | Not Found      | 资源不存在                   |
| **500** | Internal Error | 服务器内部错误               |

## 4. 实现示例

### 4.1 Express.js 实现

```ts
import express, { Request, Response, Router } from 'express';

const router: Router = express.Router();

interface User {
  id: number;
  name: string;
  email: string;
}

const users: User[] = [
  { id: 1, name: 'John', email: 'john@example.com' },
  { id: 2, name: 'Jane', email: 'jane@example.com' }
];

// GET /api/users - 获取所有用户
router.get('/users', (req: Request, res: Response): void => {
  res.json({ data: users });
});

// GET /api/users/:id - 获取单个用户
router.get('/users/:id', (req: Request, res: Response): void => {
  const id: number = parseInt(req.params.id);
  const user: User | undefined = users.find((u: User) => u.id === id);
  
  if (!user) {
    res.status(404).json({ error: 'User not found' });
    return;
  }
  
  res.json({ data: user });
});

// POST /api/users - 创建用户
router.post('/users', (req: Request, res: Response): void => {
  const { name, email }: { name: string; email: string } = req.body;
  
  if (!name || !email) {
    res.status(400).json({ error: 'Name and email are required' });
    return;
  }
  
  const newUser: User = {
    id: users.length + 1,
    name,
    email
  };
  
  users.push(newUser);
  res.status(201).json({ data: newUser });
});

// PUT /api/users/:id - 完整更新用户
router.put('/users/:id', (req: Request, res: Response): void => {
  const id: number = parseInt(req.params.id);
  const userIndex: number = users.findIndex((u: User) => u.id === id);
  
  if (userIndex === -1) {
    res.status(404).json({ error: 'User not found' });
    return;
  }
  
  const { name, email }: { name: string; email: string } = req.body;
  users[userIndex] = { id, name, email };
  
  res.json({ data: users[userIndex] });
});

// PATCH /api/users/:id - 部分更新用户
router.patch('/users/:id', (req: Request, res: Response): void => {
  const id: number = parseInt(req.params.id);
  const userIndex: number = users.findIndex((u: User) => u.id === id);
  
  if (userIndex === -1) {
    res.status(404).json({ error: 'User not found' });
    return;
  }
  
  const updates: Partial<User> = req.body;
  users[userIndex] = { ...users[userIndex], ...updates };
  
  res.json({ data: users[userIndex] });
});

// DELETE /api/users/:id - 删除用户
router.delete('/users/:id', (req: Request, res: Response): void => {
  const id: number = parseInt(req.params.id);
  const userIndex: number = users.findIndex((u: User) => u.id === id);
  
  if (userIndex === -1) {
    res.status(404).json({ error: 'User not found' });
    return;
  }
  
  users.splice(userIndex, 1);
  res.status(204).send();
});

export default router;
```

### 4.2 Fastify 实现

```ts
import { FastifyInstance, FastifyRequest, FastifyReply } from 'fastify';

interface User {
  id: number;
  name: string;
  email: string;
}

const users: User[] = [
  { id: 1, name: 'John', email: 'john@example.com' },
  { id: 2, name: 'Jane', email: 'jane@example.com' }
];

export default async function userRoutes(fastify: FastifyInstance): Promise<void> {
  // GET /api/users
  fastify.get('/users', async (request: FastifyRequest, reply: FastifyReply): Promise<void> => {
    reply.send({ data: users });
  });

  // GET /api/users/:id
  fastify.get('/users/:id', async (request: FastifyRequest<{ Params: { id: string } }>, reply: FastifyReply): Promise<void> => {
    const id: number = parseInt(request.params.id);
    const user: User | undefined = users.find((u: User) => u.id === id);
    
    if (!user) {
      reply.code(404).send({ error: 'User not found' });
      return;
    }
    
    reply.send({ data: user });
  });

  // POST /api/users
  fastify.post('/users', async (request: FastifyRequest<{ Body: { name: string; email: string } }>, reply: FastifyReply): Promise<void> => {
    const { name, email } = request.body;
    
    if (!name || !email) {
      reply.code(400).send({ error: 'Name and email are required' });
      return;
    }
    
    const newUser: User = {
      id: users.length + 1,
      name,
      email
    };
    
    users.push(newUser);
    reply.code(201).send({ data: newUser });
  });

  // PUT /api/users/:id
  fastify.put('/users/:id', async (request: FastifyRequest<{ Params: { id: string }; Body: { name: string; email: string } }>, reply: FastifyReply): Promise<void> => {
    const id: number = parseInt(request.params.id);
    const userIndex: number = users.findIndex((u: User) => u.id === id);
    
    if (userIndex === -1) {
      reply.code(404).send({ error: 'User not found' });
      return;
    }
    
    const { name, email } = request.body;
    users[userIndex] = { id, name, email };
    
    reply.send({ data: users[userIndex] });
  });

  // DELETE /api/users/:id
  fastify.delete('/users/:id', async (request: FastifyRequest<{ Params: { id: string } }>, reply: FastifyReply): Promise<void> => {
    const id: number = parseInt(request.params.id);
    const userIndex: number = users.findIndex((u: User) => u.id === id);
    
    if (userIndex === -1) {
      reply.code(404).send({ error: 'User not found' });
      return;
    }
    
    users.splice(userIndex, 1);
    reply.code(204).send();
  });
}
```

## 5. 查询参数

### 5.1 分页

```ts
// GET /api/users?page=1&limit=10
router.get('/users', (req: Request, res: Response): void => {
  const page: number = parseInt(req.query.page as string) || 1;
  const limit: number = parseInt(req.query.limit as string) || 10;
  const start: number = (page - 1) * limit;
  const end: number = start + limit;
  
  const paginatedUsers: User[] = users.slice(start, end);
  
  res.json({
    data: paginatedUsers,
    pagination: {
      page,
      limit,
      total: users.length,
      totalPages: Math.ceil(users.length / limit)
    }
  });
});
```

### 5.2 过滤

```ts
// GET /api/users?status=active&role=admin
router.get('/users', (req: Request, res: Response): void => {
  let filteredUsers: User[] = [...users];
  
  if (req.query.status) {
    filteredUsers = filteredUsers.filter((u: User) => u.status === req.query.status);
  }
  
  if (req.query.role) {
    filteredUsers = filteredUsers.filter((u: User) => u.role === req.query.role);
  }
  
  res.json({ data: filteredUsers });
});
```

### 5.3 排序

```ts
// GET /api/users?sort=name&order=asc
router.get('/users', (req: Request, res: Response): void => {
  const sort: string = (req.query.sort as string) || 'id';
  const order: string = (req.query.order as string) || 'asc';
  
  const sortedUsers: User[] = [...users].sort((a: User, b: User): number => {
    const aValue: string | number = a[sort as keyof User] as string | number;
    const bValue: string | number = b[sort as keyof User] as string | number;
    
    if (order === 'desc') {
      return aValue > bValue ? -1 : 1;
    }
    
    return aValue < bValue ? -1 : 1;
  });
  
  res.json({ data: sortedUsers });
});
```

## 6. 响应格式

### 6.1 统一响应格式

```ts
interface ApiResponse<T> {
  data?: T;
  error?: {
    code: string;
    message: string;
  };
  meta?: {
    page?: number;
    limit?: number;
    total?: number;
  };
}

// 成功响应
res.json({ data: user } as ApiResponse<User>);

// 错误响应
res.status(400).json({
  error: {
    code: 'VALIDATION_ERROR',
    message: 'Name and email are required'
  }
} as ApiResponse<never>);
```

## 7. 最佳实践

### 7.1 资源命名

- 使用名词，不使用动词
- 使用复数形式
- 使用小写字母和连字符

### 7.2 版本控制

```ts
// 使用 URL 版本控制
router.use('/v1', v1Routes);
router.use('/v2', v2Routes);
```

### 7.3 错误处理

```ts
router.use((err: Error, req: Request, res: Response, next: express.NextFunction): void => {
  console.error(err);
  res.status(500).json({
    error: {
      code: 'INTERNAL_ERROR',
      message: 'An internal error occurred'
    }
  });
});
```

## 8. 注意事项

- **幂等性**：GET、PUT、DELETE 应该是幂等的
- **安全性**：GET 请求不应该修改数据
- **状态码**：正确使用 HTTP 状态码
- **响应格式**：保持响应格式一致

## 9. 常见问题

### 9.1 PUT 和 PATCH 的区别？

PUT 用于完整更新资源，PATCH 用于部分更新资源。

### 9.2 如何处理嵌套资源？

使用嵌套 URL：`/api/users/123/posts`

### 9.3 如何实现批量操作？

使用 POST 方法，在请求体中包含多个资源。

## 10. 实践任务

1. **实现用户 CRUD API**：使用 Express 或 Fastify 实现完整的用户 CRUD API
2. **实现分页查询**：实现支持分页、过滤、排序的用户列表 API
3. **实现错误处理**：实现统一的错误处理中间件
4. **实现版本控制**：实现 API 版本控制机制
5. **实现响应格式**：实现统一的响应格式

---

**下一节**：[4.3.3 GraphQL API](section-03-graphql.md)
