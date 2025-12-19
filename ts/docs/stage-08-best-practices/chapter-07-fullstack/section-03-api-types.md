# 8.7.3 API 类型定义

## 概述

API 类型定义是全栈 TypeScript 开发的重要组成部分。本节介绍如何定义 API 请求和响应的类型，实现类型安全的 API 调用。

## API 类型定义方法

### 1. 请求类型定义

定义 API 请求的类型：

```ts
// API 请求类型
interface GetUserRequest {
    id: number;
}

interface CreateUserRequest {
    name: string;
    email: string;
    age?: number;
}

interface UpdateUserRequest {
    id: number;
    name?: string;
    email?: string;
    age?: number;
}

interface DeleteUserRequest {
    id: number;
}
```

### 2. 响应类型定义

定义 API 响应的类型：

```ts
// API 响应类型
interface GetUserResponse {
    user: User;
}

interface CreateUserResponse {
    user: User;
}

interface UpdateUserResponse {
    user: User;
}

interface DeleteUserResponse {
    success: boolean;
}

// 通用响应类型
interface ApiResponse<T> {
    data: T;
    error?: string;
    status: number;
}
```

### 3. 错误类型定义

定义 API 错误的类型：

```ts
// API 错误类型
interface ApiError {
    message: string;
    code: string;
    status: number;
}

interface ValidationError extends ApiError {
    fields: Array<{
        field: string;
        message: string;
    }>;
}
```

## API 客户端类型定义

### 1. 基础 API 客户端

定义类型安全的 API 客户端：

```ts
// API 客户端类型
class ApiClient {
    async get<T>(url: string): Promise<T> {
        const response = await fetch(url);
        return response.json();
    }

    async post<TRequest, TResponse>(
        url: string,
        data: TRequest
    ): Promise<TResponse> {
        const response = await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        return response.json();
    }
}
```

### 2. 类型安全的 API 调用

使用类型定义实现类型安全的 API 调用：

```ts
// 类型安全的 API 调用
const api = new ApiClient();

// GET 请求
async function getUser(id: number): Promise<GetUserResponse> {
    return api.get<GetUserResponse>(`/api/users/${id}`);
}

// POST 请求
async function createUser(data: CreateUserRequest): Promise<CreateUserResponse> {
    return api.post<CreateUserRequest, CreateUserResponse>('/api/users', data);
}
```

## REST API 类型定义

### 1. 资源类型

定义 REST API 资源类型：

```ts
// 资源类型
interface Resource<T> {
    data: T;
    links?: {
        self: string;
        related?: string;
    };
}

interface Collection<T> {
    data: T[];
    meta?: {
        total: number;
        page: number;
        pageSize: number;
    };
}
```

### 2. 端点类型

定义 API 端点类型：

```ts
// API 端点类型
type UserEndpoint = 
    | { method: 'GET'; path: '/api/users'; response: Collection<User> }
    | { method: 'GET'; path: '/api/users/:id'; response: Resource<User> }
    | { method: 'POST'; path: '/api/users'; request: CreateUserRequest; response: Resource<User> }
    | { method: 'PUT'; path: '/api/users/:id'; request: UpdateUserRequest; response: Resource<User> }
    | { method: 'DELETE'; path: '/api/users/:id'; response: { success: boolean } };
```

## GraphQL 类型定义

### 1. Query 类型

定义 GraphQL Query 类型：

```ts
// GraphQL Query 类型
interface GraphQLQuery {
    query: string;
    variables?: Record<string, any>;
}

interface GraphQLResponse<T> {
    data: T;
    errors?: Array<{ message: string }>;
}
```

### 2. Mutation 类型

定义 GraphQL Mutation 类型：

```ts
// GraphQL Mutation 类型
interface CreateUserMutation {
    createUser(input: CreateUserInput): User;
}

interface CreateUserInput {
    name: string;
    email: string;
}
```

## 类型生成

### 1. 从 OpenAPI 生成

从 OpenAPI 定义生成类型：

```bash
# 安装工具
npm install --save-dev openapi-typescript

# 生成类型
npx openapi-typescript api.yaml -o src/types/api.ts
```

### 2. 从 GraphQL Schema 生成

从 GraphQL Schema 生成类型：

```bash
# 安装工具
npm install --save-dev @graphql-codegen/cli @graphql-codegen/typescript

# 配置 codegen.yml
# 生成类型
npx graphql-codegen
```

## 使用场景

### 1. 前端 API 调用

在前端使用类型安全的 API 调用：

```ts
// 前端 API 调用
async function fetchUsers(): Promise<User[]> {
    const response = await fetch('/api/users');
    const data: Collection<User> = await response.json();
    return data.data;
}
```

### 2. 后端 API 处理

在后端使用类型安全的 API 处理：

```ts
// 后端 API 处理
app.get('/api/users/:id', (req, res) => {
    const id = parseInt(req.params.id);
    const user = getUserById(id);
    const response: GetUserResponse = { user };
    res.json(response);
});
```

## 注意事项

1. **类型同步**：确保前后端类型定义同步
2. **版本管理**：管理 API 类型定义的版本
3. **错误处理**：定义错误类型并处理错误
4. **类型验证**：在运行时验证类型
5. **文档说明**：为 API 类型添加文档

## 最佳实践

1. **统一定义**：使用统一的 API 类型定义
2. **类型生成**：使用工具自动生成类型
3. **错误处理**：定义并处理错误类型
4. **类型验证**：在运行时验证类型
5. **文档说明**：为 API 类型添加文档

## 练习任务

1. **API 类型定义**：
   - 为 API 定义请求和响应类型
   - 定义错误类型
   - 理解 API 类型定义的作用

2. **类型安全调用**：
   - 创建类型安全的 API 客户端
   - 实现类型安全的 API 调用
   - 理解类型安全的价值

3. **类型生成**：
   - 使用工具从 API 定义生成类型
   - 配置类型生成工具
   - 理解类型生成的作用

4. **错误处理**：
   - 定义错误类型
   - 实现错误处理
   - 理解错误处理的重要性

5. **实际应用**：
   - 在实际项目中定义 API 类型
   - 实现类型安全的 API 调用
   - 总结使用经验

完成以上练习后，继续学习下一节：类型安全的全栈开发。

## 总结

API 类型定义是全栈 TypeScript 开发的重要组成部分：

- **请求类型**：定义 API 请求的类型
- **响应类型**：定义 API 响应的类型
- **类型生成**：使用工具自动生成类型
- **类型安全**：实现类型安全的 API 调用

掌握 API 类型定义有助于构建类型安全的全栈应用。

---

**最后更新**：2025-01-XX
