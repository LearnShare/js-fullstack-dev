# 4.1.3 RESTful API 设计原则

## 1. 概述

RESTful API 是一种基于 REST（Representational State Transfer，表述性状态转移）架构风格的 API 设计方法。RESTful API 设计遵循统一的规范和原则，使 API 易于理解、使用和维护。本节介绍 RESTful API 的核心设计原则和最佳实践。

## 2. REST 架构原则

### 2.1 REST 核心原则

- **资源导向**：以资源为中心设计 API，而非操作
- **统一接口**：使用标准 HTTP 方法和状态码
- **无状态**：每个请求包含所有必要信息
- **可缓存**：支持 HTTP 缓存机制
- **分层系统**：支持中间层（如代理、网关）
- **按需编码**：客户端可以扩展功能

### 2.2 RESTful API 特点

- **资源识别**：通过 URL 识别资源
- **标准方法**：使用标准 HTTP 方法操作资源
- **状态码**：使用标准 HTTP 状态码表示结果
- **HATEOAS**：超媒体作为应用状态引擎（可选）

## 3. 资源设计

### 3.1 资源命名

**好的资源命名**：

- 使用名词，而非动词：`/users` 而非 `/getUsers`
- 使用复数形式：`/users` 而非 `/user`
- 使用小写字母和连字符：`/user-profiles` 而非 `/userProfiles`
- 避免文件扩展名：`/users` 而非 `/users.json`

**示例**：

```
GET    /users              # 获取用户列表
GET    /users/123          # 获取用户 123
POST   /users              # 创建新用户
PUT    /users/123          # 更新用户 123
DELETE /users/123          # 删除用户 123
```

### 3.2 资源层级

使用层级结构表示资源关系：

```
/users/123/posts           # 用户 123 的帖子
/users/123/posts/456       # 用户 123 的帖子 456
/users/123/posts/456/comments # 帖子 456 的评论
```

### 3.3 资源过滤和分页

使用查询参数进行过滤和分页：

```
GET /users?status=active&page=1&limit=20
GET /users?role=admin&sort=created_at&order=desc
```

## 4. HTTP 方法使用

### 4.1 标准方法映射

| HTTP 方法 | 用途           | 幂等性 | 安全性 | 示例                     |
|:----------|:---------------|:-------|:-------|:-------------------------|
| **GET**   | 获取资源       | 是     | 是     | `GET /users/123`         |
| **POST**  | 创建资源       | 否     | 否     | `POST /users`            |
| **PUT**   | 完整更新资源   | 是     | 否     | `PUT /users/123`         |
| **PATCH** | 部分更新资源   | 否     | 否     | `PATCH /users/123`       |
| **DELETE**| 删除资源       | 是     | 否     | `DELETE /users/123`      |

### 4.2 方法选择原则

- **GET**：用于查询操作，不应有副作用
- **POST**：用于创建资源或执行非幂等操作
- **PUT**：用于完整更新资源（替换整个资源）
- **PATCH**：用于部分更新资源（只更新指定字段）
- **DELETE**：用于删除资源

### 4.3 方法使用示例

```ts
// GET - 获取资源
GET /api/users/123

// POST - 创建资源
POST /api/users
Content-Type: application/json
{
  "name": "John",
  "email": "john@example.com"
}

// PUT - 完整更新资源
PUT /api/users/123
Content-Type: application/json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}

// PATCH - 部分更新资源
PATCH /api/users/123
Content-Type: application/json
{
  "name": "John Doe"
}

// DELETE - 删除资源
DELETE /api/users/123
```

## 5. 状态码使用

### 5.1 成功状态码

| 状态码 | 使用场景                     | 示例                           |
|:-------|:-----------------------------|:-------------------------------|
| **200**| 请求成功                     | GET、PUT、PATCH 成功           |
| **201**| 资源创建成功                 | POST 创建资源成功              |
| **204**| 请求成功，无返回内容         | DELETE 成功                    |

### 5.2 客户端错误状态码

| 状态码 | 使用场景                     | 示例                           |
|:-------|:-----------------------------|:-------------------------------|
| **400**| 请求参数错误                 | 请求体格式错误                 |
| **401**| 未授权                       | 缺少或无效的认证信息           |
| **403**| 禁止访问                     | 无权限访问资源                 |
| **404**| 资源不存在                   | 请求的资源不存在               |
| **409**| 资源冲突                     | 创建资源时发生冲突             |
| **422**| 请求格式正确但语义错误       | 验证失败                       |
| **429**| 请求过多                     | 超过限流阈值                   |

### 5.3 服务器错误状态码

| 状态码 | 使用场景                     | 示例                           |
|:-------|:-----------------------------|:-------------------------------|
| **500**| 服务器内部错误               | 未处理的异常                   |
| **502**| 网关错误                     | 上游服务器错误                 |
| **503**| 服务不可用                   | 服务维护或过载                 |

## 6. 请求和响应格式

### 6.1 请求格式

**Content-Type 头部**：

- JSON：`Content-Type: application/json`
- 表单：`Content-Type: application/x-www-form-urlencoded`
- 文件上传：`Content-Type: multipart/form-data`

**请求体示例**：

```json
{
  "name": "John",
  "email": "john@example.com",
  "age": 30
}
```

### 6.2 响应格式

**统一响应格式**：

```json
{
  "data": {
    "id": 123,
    "name": "John",
    "email": "john@example.com"
  },
  "meta": {
    "timestamp": "2025-01-01T00:00:00Z"
  }
}
```

**错误响应格式**：

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Validation failed",
    "details": [
      {
        "field": "email",
        "message": "Invalid email format"
      }
    ]
  }
}
```

### 6.3 分页响应格式

```json
{
  "data": [...],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 100,
    "totalPages": 5
  }
}
```

## 7. 版本控制

### 7.1 版本控制策略

**URL 路径版本控制**：

```
/api/v1/users
/api/v2/users
```

**请求头版本控制**：

```
Accept: application/vnd.api+json;version=1
```

**查询参数版本控制**（不推荐）：

```
/api/users?version=1
```

### 7.2 版本控制最佳实践

- **URL 路径版本控制**：最常用，清晰明确
- **向后兼容**：尽量保持向后兼容，避免破坏性变更
- **版本文档**：为每个版本维护文档
- **弃用策略**：明确弃用旧版本的策略和时间表

## 8. 代码示例

### 8.1 RESTful API 实现示例

```ts
import { createServer, IncomingMessage, ServerResponse } from 'node:http';
import { parse } from 'node:url';

interface User {
  id: number;
  name: string;
  email: string;
}

const users: User[] = [
  { id: 1, name: 'John', email: 'john@example.com' },
  { id: 2, name: 'Jane', email: 'jane@example.com' }
];

const server = createServer((req: IncomingMessage, res: ServerResponse) => {
  const { pathname, query } = parse(req.url || '', true);
  const method = req.method;

  // 设置响应头
  res.setHeader('Content-Type', 'application/json');

  // 路由处理
  if (pathname === '/api/users') {
    if (method === 'GET') {
      // GET /api/users - 获取用户列表
      const page = parseInt(query.page as string) || 1;
      const limit = parseInt(query.limit as string) || 20;
      const start = (page - 1) * limit;
      const end = start + limit;

      res.statusCode = 200;
      res.end(JSON.stringify({
        data: users.slice(start, end),
        pagination: {
          page,
          limit,
          total: users.length,
          totalPages: Math.ceil(users.length / limit)
        }
      }));
    } else if (method === 'POST') {
      // POST /api/users - 创建用户
      let body = '';
      req.on('data', (chunk: Buffer): void => {
        body += chunk.toString();
      });
      req.on('end', (): void => {
        try {
          const userData = JSON.parse(body);
          const newUser: User = {
            id: users.length + 1,
            ...userData
          };
          users.push(newUser);
          res.statusCode = 201;
          res.end(JSON.stringify({ data: newUser }));
        } catch (error: unknown) {
          res.statusCode = 400;
          res.end(JSON.stringify({ error: { message: 'Invalid JSON' } }));
        }
      });
    } else {
      res.statusCode = 405;
      res.end(JSON.stringify({ error: { message: 'Method Not Allowed' } }));
    }
  } else if (pathname?.startsWith('/api/users/')) {
    const userId = parseInt(pathname.split('/')[3]);
    const user = users.find((u: User) => u.id === userId);

    if (!user) {
      res.statusCode = 404;
      res.end(JSON.stringify({ error: { message: 'User not found' } }));
      return;
    }

    if (method === 'GET') {
      // GET /api/users/:id - 获取用户
      res.statusCode = 200;
      res.end(JSON.stringify({ data: user }));
    } else if (method === 'PUT') {
      // PUT /api/users/:id - 完整更新用户
      let body = '';
      req.on('data', (chunk: Buffer): void => {
        body += chunk.toString();
      });
      req.on('end', (): void => {
        try {
          const userData = JSON.parse(body);
          Object.assign(user, userData);
          res.statusCode = 200;
          res.end(JSON.stringify({ data: user }));
        } catch (error: unknown) {
          res.statusCode = 400;
          res.end(JSON.stringify({ error: { message: 'Invalid JSON' } }));
        }
      });
    } else if (method === 'DELETE') {
      // DELETE /api/users/:id - 删除用户
      const index = users.findIndex((u: User) => u.id === userId);
      users.splice(index, 1);
      res.statusCode = 204;
      res.end();
    } else {
      res.statusCode = 405;
      res.end(JSON.stringify({ error: { message: 'Method Not Allowed' } }));
    }
  } else {
    res.statusCode = 404;
    res.end(JSON.stringify({ error: { message: 'Not Found' } }));
  }
});

server.listen(3000, (): void => {
  console.log('Server running on http://localhost:3000');
});
```

## 9. 最佳实践

### 9.1 设计原则

- **资源导向**：以资源为中心，而非操作
- **统一接口**：使用标准 HTTP 方法和状态码
- **无状态**：每个请求独立，不依赖服务器状态
- **可缓存**：合理使用 HTTP 缓存机制
- **版本控制**：明确管理 API 版本

### 9.2 命名规范

- 使用名词，避免动词
- 使用复数形式
- 使用小写字母和连字符
- 避免文件扩展名

### 9.3 错误处理

- 使用标准状态码
- 提供清晰的错误信息
- 统一错误响应格式
- 记录错误日志

### 9.4 性能优化

- 使用分页限制返回数据量
- 使用过滤减少数据传输
- 合理使用缓存
- 支持字段选择（如 GraphQL 的字段选择）

## 10. 注意事项

- **安全性**：注意认证、授权、输入验证、SQL 注入等安全问题
- **性能**：注意查询性能，合理使用索引和缓存
- **文档**：保持 API 文档的及时更新
- **测试**：编写完整的 API 测试用例

## 11. 常见问题

### 11.1 何时使用 PUT 和 PATCH？

- **PUT**：用于完整更新资源，替换整个资源
- **PATCH**：用于部分更新资源，只更新指定字段

### 11.2 如何处理嵌套资源？

使用层级 URL 结构：

```
/users/123/posts          # 用户 123 的帖子
/users/123/posts/456      # 用户 123 的帖子 456
```

### 11.3 如何处理批量操作？

使用 POST 方法，在请求体中包含多个资源：

```json
POST /api/users/batch
{
  "users": [
    { "name": "John", "email": "john@example.com" },
    { "name": "Jane", "email": "jane@example.com" }
  ]
}
```

---

**下一节**：[4.1.4 API 版本控制](section-04-versioning.md)
