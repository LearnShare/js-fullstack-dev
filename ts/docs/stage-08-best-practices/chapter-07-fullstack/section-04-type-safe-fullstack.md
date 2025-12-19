# 8.7.4 类型安全的全栈开发

## 概述

类型安全的全栈开发是 TypeScript 的核心优势。本节介绍如何构建类型安全的全栈应用，包括前后端类型共享、API 类型定义、类型验证等实践。

## 类型安全的全栈架构

### 1. 项目结构

组织项目结构以支持类型安全：

```
fullstack-project/
├── shared/
│   └── types/
│       ├── user.ts
│       ├── api.ts
│       └── index.ts
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   │   └── client.ts
│   │   └── components/
│   └── tsconfig.json
├── backend/
│   ├── src/
│   │   ├── api/
│   │   │   └── routes.ts
│   │   └── services/
│   └── tsconfig.json
└── package.json
```

### 2. 共享类型定义

创建共享的类型定义：

```ts
// shared/types/user.ts
export interface User {
    id: number;
    name: string;
    email: string;
    createdAt: Date;
}

export interface CreateUserRequest {
    name: string;
    email: string;
}

export interface CreateUserResponse {
    user: User;
}
```

### 3. 类型安全的 API 客户端

创建类型安全的 API 客户端：

```ts
// frontend/src/api/client.ts
import { CreateUserRequest, CreateUserResponse } from '../../../shared/types';

class ApiClient {
    private baseUrl: string;

    constructor(baseUrl: string) {
        this.baseUrl = baseUrl;
    }

    async createUser(data: CreateUserRequest): Promise<CreateUserResponse> {
        const response = await fetch(`${this.baseUrl}/api/users`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error(`API error: ${response.status}`);
        }

        return response.json();
    }
}

export const apiClient = new ApiClient(process.env.API_URL || 'http://localhost:3000');
```

## 类型验证

### 1. 运行时类型验证

在运行时验证类型：

```ts
// shared/validation.ts
import { User, CreateUserRequest } from './types';

export function isUser(data: unknown): data is User {
    return (
        typeof data === 'object' &&
        data !== null &&
        'id' in data &&
        typeof (data as any).id === 'number' &&
        'name' in data &&
        typeof (data as any).name === 'string' &&
        'email' in data &&
        typeof (data as any).email === 'string'
    );
}

export function isCreateUserRequest(data: unknown): data is CreateUserRequest {
    return (
        typeof data === 'object' &&
        data !== null &&
        'name' in data &&
        typeof (data as any).name === 'string' &&
        'email' in data &&
        typeof (data as any).email === 'string'
    );
}
```

### 2. API 验证中间件

在后端使用验证中间件：

```ts
// backend/src/middleware/validation.ts
import { Request, Response, NextFunction } from 'express';
import { isCreateUserRequest } from '../../../shared/validation';

export function validateCreateUser(
    req: Request,
    res: Response,
    next: NextFunction
): void {
    if (!isCreateUserRequest(req.body)) {
        res.status(400).json({ error: 'Invalid request data' });
        return;
    }
    next();
}
```

## 类型安全的路由

### 1. 类型安全的路由定义

定义类型安全的路由：

```ts
// backend/src/api/routes.ts
import { Router } from 'express';
import { CreateUserRequest, CreateUserResponse } from '../../../shared/types';
import { validateCreateUser } from '../middleware/validation';

const router = Router();

router.post(
    '/users',
    validateCreateUser,
    (req: Request<{}, CreateUserResponse, CreateUserRequest>, res) => {
        const user = createUserService(req.body);
        const response: CreateUserResponse = { user };
        res.json(response);
    }
);

export default router;
```

### 2. 类型安全的服务层

创建类型安全的服务层：

```ts
// backend/src/services/user.ts
import { User, CreateUserRequest } from '../../../shared/types';

export function createUser(data: CreateUserRequest): User {
    return {
        id: generateId(),
        name: data.name,
        email: data.email,
        createdAt: new Date()
    };
}
```

## 全栈类型安全实践

### 1. 端到端类型安全

实现端到端的类型安全：

```ts
// 前端调用
const user = await apiClient.createUser({
    name: "John",
    email: "john@example.com"
});
// user 的类型是 CreateUserResponse

// 后端处理
app.post('/api/users', validateCreateUser, (req, res) => {
    const user = createUser(req.body);
    // req.body 的类型是 CreateUserRequest
    // user 的类型是 User
    res.json({ user });
});
```

### 2. 类型生成工作流

建立类型生成工作流：

```bash
# 1. 定义 API（OpenAPI、GraphQL Schema）
# 2. 生成类型定义
npx openapi-typescript api.yaml -o shared/types/api.ts

# 3. 前后端使用生成的类型
# 4. 类型检查确保一致性
```

## 注意事项

1. **类型同步**：确保前后端类型定义同步
2. **版本管理**：管理类型定义的版本
3. **类型验证**：在运行时验证类型
4. **错误处理**：定义并处理错误类型
5. **持续维护**：需要持续维护类型定义

## 最佳实践

1. **共享类型**：使用共享类型定义文件
2. **类型生成**：使用工具自动生成类型
3. **类型验证**：在运行时验证类型
4. **错误处理**：定义并处理错误类型
5. **文档说明**：为类型定义添加文档

## 练习任务

1. **构建全栈应用**：
   - 创建类型安全的全栈应用
   - 实现前后端类型共享
   - 理解类型安全的价值

2. **类型验证**：
   - 实现运行时类型验证
   - 创建验证中间件
   - 理解类型验证的作用

3. **类型生成**：
   - 建立类型生成工作流
   - 使用工具自动生成类型
   - 理解类型生成的价值

4. **错误处理**：
   - 定义错误类型
   - 实现错误处理
   - 理解错误处理的重要性

5. **实际应用**：
   - 在实际项目中应用全栈 TypeScript
   - 评估类型安全的效果
   - 总结使用经验

完成以上练习后，继续学习下一章：TypeScript 与测试框架集成。

## 总结

类型安全的全栈开发是 TypeScript 的核心优势：

- **类型共享**：前后端共享类型定义
- **类型验证**：运行时类型验证
- **类型安全**：端到端的类型安全
- **最佳实践**：遵循类型安全的最佳实践

掌握类型安全的全栈开发有助于构建更安全、更可靠的应用。

---

**最后更新**：2025-01-XX
