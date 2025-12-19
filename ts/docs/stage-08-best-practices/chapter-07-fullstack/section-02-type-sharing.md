# 8.7.2 前后端类型共享

## 概述

前后端类型共享是全栈 TypeScript 开发的核心。本节介绍如何实现前后端类型共享，包括共享类型定义文件、类型生成工具等方法。

## 类型共享方法

### 1. 共享类型定义文件

创建共享的类型定义文件，前后端共同使用：

```ts
// shared/types.ts
export interface User {
    id: number;
    name: string;
    email: string;
}

export interface CreateUserRequest {
    name: string;
    email: string;
}

export interface CreateUserResponse {
    user: User;
}
```

### 2. 项目结构

组织项目结构以支持类型共享：

```
project/
├── shared/
│   └── types/
│       ├── user.ts
│       ├── api.ts
│       └── index.ts
├── frontend/
│   └── src/
│       └── api/
│           └── user.ts
└── backend/
    └── src/
        └── api/
            └── user.ts
```

### 3. 使用共享类型

前后端都使用共享类型：

```ts
// frontend/src/api/user.ts
import { User, CreateUserRequest, CreateUserResponse } from '../../../shared/types';

async function createUser(data: CreateUserRequest): Promise<CreateUserResponse> {
    const response = await fetch('/api/users', {
        method: 'POST',
        body: JSON.stringify(data)
    });
    return response.json();
}
```

```ts
// backend/src/api/user.ts
import { User, CreateUserRequest, CreateUserResponse } from '../../../shared/types';

function createUser(data: CreateUserRequest): CreateUserResponse {
    const user: User = {
        id: generateId(),
        name: data.name,
        email: data.email
    };
    return { user };
}
```

## 类型生成工具

### 1. 从 API 定义生成类型

使用工具从 API 定义（如 OpenAPI）生成类型：

```bash
# 安装 openapi-typescript
npm install --save-dev openapi-typescript

# 从 OpenAPI 定义生成类型
npx openapi-typescript api.yaml -o shared/types/api.ts
```

### 2. 从 JSON Schema 生成类型

从 JSON Schema 生成类型：

```bash
# 安装 json-schema-to-typescript
npm install --save-dev json-schema-to-typescript

# 从 JSON Schema 生成类型
npx json2ts schema.json -o shared/types/schema.ts
```

### 3. 从 GraphQL 生成类型

从 GraphQL Schema 生成类型：

```bash
# 安装 graphql-codegen
npm install --save-dev @graphql-codegen/cli

# 从 GraphQL Schema 生成类型
npx graphql-codegen
```

## 类型共享最佳实践

### 1. 统一类型定义

使用统一的类型定义文件：

```ts
// shared/types/index.ts
export * from './user';
export * from './api';
export * from './common';
```

### 2. 版本管理

管理类型定义的版本：

```ts
// shared/types/v1/user.ts
export interface UserV1 {
    id: number;
    name: string;
}

// shared/types/v2/user.ts
export interface UserV2 {
    id: number;
    name: string;
    email: string;
}
```

### 3. 类型验证

在运行时验证类型：

```ts
import { User } from '../shared/types';

function validateUser(data: unknown): data is User {
    return (
        typeof data === 'object' &&
        data !== null &&
        'id' in data &&
        'name' in data &&
        'email' in data
    );
}

function handleUser(data: unknown): void {
    if (validateUser(data)) {
        // data 是 User 类型
        console.log(data.name);
    }
}
```

## 使用场景

### 1. REST API

在 REST API 项目中使用类型共享：

```ts
// shared/types/api.ts
export interface ApiResponse<T> {
    data: T;
    error?: string;
    status: number;
}

export interface GetUsersResponse extends ApiResponse<User[]> {}
export interface GetUserResponse extends ApiResponse<User> {}
```

### 2. GraphQL

在 GraphQL 项目中使用类型共享：

```ts
// shared/types/graphql.ts
export interface GraphQLResponse<T> {
    data: T;
    errors?: Array<{ message: string }>;
}
```

### 3. WebSocket

在 WebSocket 项目中使用类型共享：

```ts
// shared/types/websocket.ts
export interface WebSocketMessage<T> {
    type: string;
    payload: T;
}
```

## 注意事项

1. **类型同步**：确保前后端类型定义同步
2. **版本管理**：管理类型定义的版本
3. **工具支持**：确保工具链支持类型共享
4. **团队协作**：团队需要统一类型定义规范
5. **持续维护**：需要持续维护类型定义

## 最佳实践

1. **共享文件**：使用共享类型定义文件
2. **类型生成**：使用工具自动生成类型
3. **版本控制**：将类型定义纳入版本控制
4. **类型验证**：在运行时验证类型
5. **文档说明**：为类型定义添加文档

## 练习任务

1. **创建共享类型**：
   - 创建共享类型定义文件
   - 在前端和后端中使用共享类型
   - 理解类型共享的作用

2. **类型生成**：
   - 使用工具从 API 定义生成类型
   - 配置类型生成工具
   - 理解类型生成的作用

3. **类型验证**：
   - 实现运行时类型验证
   - 使用类型守卫验证类型
   - 理解类型验证的作用

4. **项目结构**：
   - 组织项目结构以支持类型共享
   - 配置构建工具支持类型共享
   - 理解项目结构的重要性

5. **实际应用**：
   - 在实际项目中实现类型共享
   - 评估类型共享的效果
   - 总结使用经验

完成以上练习后，继续学习下一节：API 类型定义。

## 总结

前后端类型共享是全栈 TypeScript 开发的核心：

- **共享文件**：使用共享类型定义文件
- **类型生成**：使用工具自动生成类型
- **类型验证**：在运行时验证类型
- **最佳实践**：遵循类型共享的最佳实践

掌握前后端类型共享有助于构建类型安全的全栈应用。

---

**最后更新**：2025-01-XX
