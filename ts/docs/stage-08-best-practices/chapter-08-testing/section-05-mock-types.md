# 8.8.5 Mock 类型

## 概述

在 TypeScript 测试中使用类型安全的 Mock 可以提高测试的可靠性和可维护性。本节介绍如何创建和使用类型安全的 Mock。

## Mock 类型定义

### 1. 基础 Mock 类型

定义基础的 Mock 类型：

```ts
// Mock 类型定义
interface MockUserRepository {
    findById: jest.Mock<Promise<User>, [number]>;
    create: jest.Mock<Promise<User>, [CreateUserRequest]>;
    update: jest.Mock<Promise<User>, [number, UpdateUserRequest]>;
    delete: jest.Mock<Promise<void>, [number]>;
}
```

### 2. 使用 Mock 类型

使用类型安全的 Mock：

```ts
// 使用 Mock 类型
const mockRepository: MockUserRepository = {
    findById: jest.fn(),
    create: jest.fn(),
    update: jest.fn(),
    delete: jest.fn(),
};

// 类型安全的 Mock 调用
mockRepository.findById.mockResolvedValue({
    id: 1,
    name: 'John',
    email: 'john@example.com'
});
```

## Jest Mock 类型

### 1. jest.Mock

使用 `jest.Mock` 定义 Mock 类型：

```ts
import { jest } from '@jest/globals';

// Mock 函数类型
const mockFn: jest.Mock<number, [number, number]> = jest.fn();

// 设置返回值
mockFn.mockReturnValue(10);

// 调用 Mock
const result: number = mockFn(1, 2);
expect(result).toBe(10);
```

### 2. jest.Mocked

使用 `jest.Mocked` 转换类型：

```ts
import { jest } from '@jest/globals';

class UserRepository {
    findById(id: number): Promise<User> {
        // ...
    }
}

// 转换为 Mock 类型
const mockRepository = jest.mocked(UserRepository);

// 类型安全的 Mock
mockRepository.prototype.findById.mockResolvedValue({
    id: 1,
    name: 'John',
    email: 'john@example.com'
});
```

## Vitest Mock 类型

### 1. vi.fn

使用 `vi.fn` 创建类型安全的 Mock：

```ts
import { vi } from 'vitest';

// Mock 函数类型
const mockFn = vi.fn<number, [number, number]>();

// 设置返回值
mockFn.mockReturnValue(10);

// 调用 Mock
const result: number = mockFn(1, 2);
expect(result).toBe(10);
```

### 2. vi.mocked

使用 `vi.mocked` 转换类型：

```ts
import { vi } from 'vitest';

class UserRepository {
    findById(id: number): Promise<User> {
        // ...
    }
}

// 转换为 Mock 类型
const mockRepository = vi.mocked(UserRepository);

// 类型安全的 Mock
mockRepository.prototype.findById.mockResolvedValue({
    id: 1,
    name: 'John',
    email: 'john@example.com'
});
```

## Mock 类型实践

### 1. API Mock

创建类型安全的 API Mock：

```ts
// API Mock 类型
interface MockApiClient {
    get: jest.Mock<Promise<any>, [string]>;
    post: jest.Mock<Promise<any>, [string, any]>;
    put: jest.Mock<Promise<any>, [string, any]>;
    delete: jest.Mock<Promise<void>, [string]>;
}

const mockApi: MockApiClient = {
    get: jest.fn(),
    post: jest.fn(),
    put: jest.fn(),
    delete: jest.fn(),
};
```

### 2. 服务 Mock

创建类型安全的服务 Mock：

```ts
// 服务 Mock 类型
interface MockUserService {
    getUser: jest.Mock<Promise<User>, [number]>;
    createUser: jest.Mock<Promise<User>, [CreateUserRequest]>;
    updateUser: jest.Mock<Promise<User>, [number, UpdateUserRequest]>;
}

const mockService: MockUserService = {
    getUser: jest.fn(),
    createUser: jest.fn(),
    updateUser: jest.fn(),
};
```

## 注意事项

1. **类型定义**：为 Mock 添加明确的类型定义
2. **类型安全**：使用类型安全的 Mock 方法
3. **Mock 清理**：在测试后清理 Mock
4. **类型推断**：利用 TypeScript 的类型推断
5. **工具支持**：确保测试框架支持类型安全的 Mock

## 最佳实践

1. **类型定义**：为所有 Mock 添加类型定义
2. **类型安全**：使用类型安全的 Mock 方法
3. **Mock 组织**：合理组织 Mock 类型
4. **文档说明**：为 Mock 类型添加文档
5. **持续维护**：持续维护 Mock 类型定义

## 练习任务

1. **创建 Mock 类型**：
   - 定义 Mock 类型
   - 创建类型安全的 Mock
   - 理解 Mock 类型的作用

2. **使用 Mock**：
   - 在测试中使用类型安全的 Mock
   - 设置 Mock 返回值
   - 验证 Mock 调用

3. **Mock 组织**：
   - 组织 Mock 类型定义
   - 创建 Mock 工厂函数
   - 理解 Mock 组织的重要性

4. **类型安全**：
   - 确保 Mock 的类型安全
   - 使用类型推断
   - 理解类型安全的价值

5. **实际应用**：
   - 在实际项目中创建 Mock 类型
   - 使用类型安全的 Mock
   - 总结使用经验

完成以上练习后，你已经掌握了 TypeScript 与测试框架的集成。

## 总结

Mock 类型是 TypeScript 测试的重要组成部分：

- **类型定义**：为 Mock 添加类型定义
- **类型安全**：使用类型安全的 Mock 方法
- **最佳实践**：遵循 Mock 类型的最佳实践
- **持续维护**：持续维护 Mock 类型定义

掌握 Mock 类型有助于编写更安全、更可靠的测试代码。

---

**最后更新**：2025-01-XX
