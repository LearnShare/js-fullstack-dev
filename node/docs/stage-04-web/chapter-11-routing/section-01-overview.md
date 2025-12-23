# 4.11.1 路由设计概述

## 1. 概述

路由设计是 Web 应用架构的重要组成部分，定义了请求 URL 与处理函数之间的映射关系。良好的路由设计可以提高应用的可维护性、可扩展性和用户体验。

## 2. 核心概念

### 2.1 路由的定义

路由是 URL 路径与处理函数之间的映射关系：

```
GET  /api/users      → getUsers()
POST /api/users      → createUser()
GET  /api/users/:id  → getUserById()
```

### 2.2 路由的组成

- **HTTP 方法**：GET、POST、PUT、DELETE 等
- **路径**：URL 路径，可能包含参数
- **处理函数**：处理请求的函数
- **中间件**：路由级别的中间件

## 3. 路由设计原则

### 3.1 RESTful 原则

- 使用资源名词
- 使用标准 HTTP 方法
- 使用合理的状态码

### 3.2 清晰性原则

- 使用有意义的路径
- 保持路径简洁
- 使用一致的命名

### 3.3 模块化原则

- 按功能模块组织路由
- 使用路由前缀
- 实现路由复用

## 4. 路由模式

### 4.1 扁平路由

```
/api/users
/api/posts
/api/comments
```

### 4.2 嵌套路由

```
/api/users
/api/users/:id
/api/users/:id/posts
/api/users/:id/posts/:postId
```

### 4.3 资源路由

```
GET    /api/users        → 获取用户列表
POST   /api/users        → 创建用户
GET    /api/users/:id    → 获取用户
PUT    /api/users/:id    → 更新用户
DELETE /api/users/:id    → 删除用户
```

## 5. 路由参数

### 5.1 路径参数

```
/api/users/:id
/api/posts/:postId/comments/:commentId
```

### 5.2 查询参数

```
/api/users?page=1&limit=10
/api/search?q=keyword&type=all
```

### 5.3 请求体参数

```
POST /api/users
Body: { name: "John", email: "john@example.com" }
```

## 6. 路由组织

### 6.1 按功能组织

```
routes/
├── users.ts
├── posts.ts
└── comments.ts
```

### 6.2 按模块组织

```
routes/
├── api/
│   ├── users.ts
│   └── posts.ts
└── admin/
    ├── users.ts
    └── settings.ts
```

## 7. 注意事项

- **RESTful 设计**：遵循 RESTful 设计原则
- **路径清晰**：使用清晰有意义的路径
- **模块化**：按功能模块组织路由
- **安全性**：实现路由级别的权限控制

## 8. 常见问题

### 8.1 如何设计 RESTful 路由？

使用资源名词和标准 HTTP 方法，遵循 RESTful 设计原则。

### 8.2 如何处理嵌套资源？

使用嵌套路径，如 `/api/users/:id/posts`。

### 8.3 如何组织大量路由？

按功能模块组织，使用路由前缀和模块化。

## 9. 相关资源

- [RESTful API 设计指南](https://restfulapi.net/)
- [路由设计最佳实践](https://expressjs.com/en/guide/routing.html)

---

**下一节**：[4.11.2 路由组织与模块化](section-02-organization.md)
