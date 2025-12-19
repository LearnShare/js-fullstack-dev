# 8.8.2 Jest + TypeScript

## 概述

Jest 是流行的 JavaScript 测试框架，通过配置可以很好地支持 TypeScript。本节介绍如何配置和使用 Jest 进行 TypeScript 测试。

## 安装和配置

### 1. 安装依赖

安装 Jest 和 TypeScript 相关依赖：

```bash
npm install --save-dev jest @types/jest ts-jest typescript
```

### 2. 配置 Jest

创建 `jest.config.js` 或 `jest.config.ts`：

```ts
// jest.config.ts
import type { Config } from 'jest';

const config: Config = {
    preset: 'ts-jest',
    testEnvironment: 'node',
    roots: ['<rootDir>/src'],
    testMatch: ['**/__tests__/**/*.ts', '**/?(*.)+(spec|test).ts'],
    transform: {
        '^.+\\.ts$': 'ts-jest',
    },
    collectCoverageFrom: [
        'src/**/*.ts',
        '!src/**/*.d.ts',
    ],
};

export default config;
```

### 3. 配置 ts-jest

在 `tsconfig.json` 中配置 TypeScript：

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "esModuleInterop": true,
    "skipLibCheck": true
  },
  "ts-jest": {
    "tsconfig": {
      "compilerOptions": {
        "module": "commonjs"
      }
    }
  }
}
```

## 编写测试

### 1. 基础测试

编写类型安全的测试：

```ts
// src/math.test.ts
import { add, subtract } from './math';

describe('math functions', () => {
    it('should add two numbers', () => {
        const result: number = add(1, 2);
        expect(result).toBe(3);
    });

    it('should subtract two numbers', () => {
        const result: number = subtract(5, 2);
        expect(result).toBe(3);
    });
});
```

### 2. 异步测试

编写异步测试：

```ts
// src/api.test.ts
import { fetchUser } from './api';

describe('API functions', () => {
    it('should fetch user', async () => {
        const user = await fetchUser(1);
        expect(user).toHaveProperty('id');
        expect(user).toHaveProperty('name');
    });
});
```

### 3. Mock 测试

使用类型安全的 Mock：

```ts
// src/service.test.ts
import { UserService } from './service';
import { UserRepository } from './repository';

jest.mock('./repository');

describe('UserService', () => {
    it('should get user', async () => {
        const mockRepository = UserRepository as jest.Mocked<typeof UserRepository>;
        mockRepository.findById.mockResolvedValue({
            id: 1,
            name: 'John',
            email: 'john@example.com'
        });

        const service = new UserService();
        const user = await service.getUser(1);
        expect(user).toHaveProperty('name');
    });
});
```

## 类型定义

### 1. 测试类型

为测试代码添加类型定义：

```ts
// 测试类型
interface TestUser {
    id: number;
    name: string;
    email: string;
}

describe('User', () => {
    it('should create user', () => {
        const user: TestUser = {
            id: 1,
            name: 'John',
            email: 'john@example.com'
        };
        expect(user).toHaveProperty('name');
    });
});
```

### 2. Mock 类型

使用类型安全的 Mock：

```ts
// Mock 类型
interface MockUserRepository {
    findById: jest.Mock<Promise<User>, [number]>;
    create: jest.Mock<Promise<User>, [CreateUserRequest]>;
}

const mockRepository: MockUserRepository = {
    findById: jest.fn(),
    create: jest.fn()
};
```

## 配置选项

### 1. 使用 @swc/jest

使用 @swc/jest 提高性能：

```bash
npm install --save-dev @swc/jest @swc/core
```

```ts
// jest.config.ts
import type { Config } from 'jest';

const config: Config = {
    transform: {
        '^.+\\.ts$': ['@swc/jest', {
            jsc: {
                parser: {
                    syntax: 'typescript',
                },
            },
        }],
    },
};

export default config;
```

### 2. 环境配置

配置测试环境：

```ts
// jest.config.ts
const config: Config = {
    testEnvironment: 'node',  // 或 'jsdom' 用于浏览器环境
    setupFilesAfterEnv: ['<rootDir>/src/setupTests.ts'],
};
```

## 注意事项

1. **类型定义**：需要安装 `@types/jest`
2. **编译选项**：测试环境的编译选项可能与生产环境不同
3. **性能考虑**：使用 @swc/jest 可以提高性能
4. **Mock 类型**：使用类型安全的 Mock
5. **配置管理**：合理配置 Jest 选项

## 最佳实践

1. **类型安全**：为测试代码添加类型定义
2. **Mock 类型**：使用类型安全的 Mock
3. **配置优化**：优化 Jest 配置提高性能
4. **测试组织**：合理组织测试文件
5. **持续集成**：在 CI/CD 中运行测试

## 练习任务

1. **配置 Jest**：
   - 安装和配置 Jest
   - 配置 TypeScript 支持
   - 理解配置选项

2. **编写测试**：
   - 编写类型安全的测试
   - 使用类型定义
   - 理解类型安全的价值

3. **Mock 测试**：
   - 使用类型安全的 Mock
   - 创建 Mock 类型
   - 理解 Mock 的作用

4. **配置优化**：
   - 优化 Jest 配置
   - 使用 @swc/jest 提高性能
   - 理解配置选项

5. **实际应用**：
   - 在实际项目中配置 Jest
   - 编写类型安全的测试
   - 总结使用经验

完成以上练习后，继续学习下一节：Vitest + TypeScript。

## 总结

Jest + TypeScript 集成提供：

- **类型安全**：测试代码也有类型安全
- **配置灵活**：可以灵活配置 Jest
- **工具支持**：丰富的工具和插件支持
- **最佳实践**：遵循 Jest + TypeScript 的最佳实践

掌握 Jest + TypeScript 集成有助于编写更安全、更可靠的测试代码。

---

**最后更新**：2025-01-XX
