# 8.8.3 Vitest + TypeScript

## 概述

Vitest 是快速的测试框架，原生支持 TypeScript，与 Vite 深度集成。本节介绍如何配置和使用 Vitest 进行 TypeScript 测试。

## 安装和配置

### 1. 安装依赖

安装 Vitest：

```bash
npm install --save-dev vitest @vitest/ui
```

### 2. 配置 Vitest

创建 `vitest.config.ts`：

```ts
// vitest.config.ts
import { defineConfig } from 'vitest/config';

export default defineConfig({
    test: {
        globals: true,
        environment: 'node',
        include: ['src/**/*.{test,spec}.{ts,tsx}'],
        coverage: {
            provider: 'v8',
            reporter: ['text', 'json', 'html'],
        },
    },
});
```

### 3. 配置 TypeScript

Vitest 原生支持 TypeScript，无需额外配置：

```ts
// tsconfig.json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "types": ["vitest/globals"]
  }
}
```

## 编写测试

### 1. 基础测试

编写类型安全的测试：

```ts
// src/math.test.ts
import { describe, it, expect } from 'vitest';
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
import { describe, it, expect } from 'vitest';
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
import { describe, it, expect, vi } from 'vitest';
import { UserService } from './service';
import { UserRepository } from './repository';

vi.mock('./repository');

describe('UserService', () => {
    it('should get user', async () => {
        const mockRepository = vi.mocked(UserRepository);
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

### 1. 全局类型

使用全局类型（需要配置 `globals: true`）：

```ts
// 无需导入 describe、it、expect
describe('User', () => {
    it('should create user', () => {
        const user: User = {
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
    findById: ReturnType<typeof vi.fn<Promise<User>, [number]>>;
    create: ReturnType<typeof vi.fn<Promise<User>, [CreateUserRequest]>>;
}

const mockRepository: MockUserRepository = {
    findById: vi.fn(),
    create: vi.fn()
};
```

## 配置选项

### 1. 环境配置

配置测试环境：

```ts
// vitest.config.ts
export default defineConfig({
    test: {
        environment: 'node',  // 或 'jsdom' 用于浏览器环境
        setupFiles: ['./src/test/setup.ts'],
    },
});
```

### 2. 覆盖率配置

配置代码覆盖率：

```ts
// vitest.config.ts
export default defineConfig({
    test: {
        coverage: {
            provider: 'v8',
            reporter: ['text', 'json', 'html'],
            include: ['src/**/*.ts'],
            exclude: ['src/**/*.test.ts'],
        },
    },
});
```

## Vitest 的优势

### 1. 原生 TypeScript 支持

Vitest 原生支持 TypeScript，无需额外配置：

```ts
// 直接使用 TypeScript，无需编译步骤
import { add } from './math';

describe('math', () => {
    it('should work', () => {
        const result: number = add(1, 2);
        expect(result).toBe(3);
    });
});
```

### 2. 快速执行

Vitest 使用 Vite 的转换管道，执行速度很快：

```bash
# 快速执行测试
npm run test
```

### 3. 与 Vite 集成

与 Vite 深度集成，共享配置：

```ts
// vitest.config.ts
import { defineConfig } from 'vitest/config';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
    plugins: [vue()],
    test: {
        // 测试配置
    },
});
```

## 注意事项

1. **全局类型**：需要配置 `globals: true` 才能使用全局类型
2. **环境配置**：根据测试需求配置测试环境
3. **Mock 类型**：使用类型安全的 Mock
4. **性能优化**：利用 Vitest 的性能优势
5. **工具支持**：确保工具链支持 Vitest

## 最佳实践

1. **类型安全**：为测试代码添加类型定义
2. **Mock 类型**：使用类型安全的 Mock
3. **配置优化**：优化 Vitest 配置
4. **测试组织**：合理组织测试文件
5. **持续集成**：在 CI/CD 中运行测试

## 练习任务

1. **配置 Vitest**：
   - 安装和配置 Vitest
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

4. **性能优化**：
   - 优化 Vitest 配置
   - 利用 Vitest 的性能优势
   - 理解性能优化

5. **实际应用**：
   - 在实际项目中配置 Vitest
   - 编写类型安全的测试
   - 总结使用经验

完成以上练习后，继续学习下一节：类型测试。

## 总结

Vitest + TypeScript 集成提供：

- **原生支持**：原生支持 TypeScript
- **快速执行**：快速的测试执行速度
- **Vite 集成**：与 Vite 深度集成
- **最佳实践**：遵循 Vitest + TypeScript 的最佳实践

掌握 Vitest + TypeScript 集成有助于编写更快速、更安全的测试代码。

---

**最后更新**：2025-01-XX
