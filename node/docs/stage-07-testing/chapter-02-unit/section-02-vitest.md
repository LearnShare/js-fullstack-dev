# 7.2.2 Vitest（现代测试框架）

## 1. 概述

Vitest 是一个基于 Vite 的现代测试框架，提供了快速的执行速度、原生 ESM 支持和优秀的 TypeScript 支持。Vitest 适合现代 Node.js 和前端项目。

## 2. 特性说明

- **快速**：基于 Vite，执行速度快
- **ESM 支持**：原生 ESM 支持
- **TypeScript**：优秀的 TypeScript 支持
- **兼容 Jest**：兼容 Jest API

## 3. 安装与配置

### 3.1 安装

```bash
npm install -D vitest
```

### 3.2 配置文件

```ts
// vitest.config.ts
import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    globals: true,
    environment: 'node',
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html']
    }
  }
});
```

### 3.3 package.json

```json
{
  "scripts": {
    "test": "vitest",
    "test:watch": "vitest --watch",
    "test:coverage": "vitest --coverage"
  }
}
```

## 4. 基本使用

### 4.1 测试文件

```ts
// math.test.ts
import { describe, it, expect } from 'vitest';

function add(a: number, b: number): number {
  return a + b;
}

describe('add', () => {
  it('should add two numbers', () => {
    expect(add(1, 2)).toBe(3);
  });
  
  it('should handle negative numbers', () => {
    expect(add(-1, 2)).toBe(1);
  });
});
```

### 4.2 运行测试

```bash
# 运行所有测试
npm test

# 监视模式
npm run test:watch

# 生成覆盖率报告
npm run test:coverage
```

## 5. 高级特性

### 5.1 测试钩子

```ts
import { describe, it, expect, beforeAll, afterAll, beforeEach, afterEach } from 'vitest';

describe('UserService', () => {
  beforeAll(async (): Promise<void> => {
    // 在所有测试前执行一次
    await setupDatabase();
  });
  
  afterAll(async (): Promise<void> => {
    // 在所有测试后执行一次
    await cleanupDatabase();
  });
  
  beforeEach(async (): Promise<void> => {
    // 在每个测试前执行
    await clearTestData();
  });
  
  afterEach(async (): Promise<void> => {
    // 在每个测试后执行
    await resetState();
  });
  
  it('should create a user', async (): Promise<void> => {
    // 测试代码
  });
});
```

### 5.2 参数化测试

```ts
describe('isEven', () => {
  it.each([
    [2, true],
    [3, false],
    [4, true],
    [5, false]
  ])('should return %s for %d', (input: number, expected: boolean): void => {
    expect(isEven(input)).toBe(expected);
  });
});
```

### 5.3 异步测试

```ts
describe('fetchUser', () => {
  it('should fetch user data', async (): Promise<void> => {
    const user = await fetchUser(1);
    expect(user).toBeDefined();
    expect(user.id).toBe(1);
  });
  
  it('should handle errors', async (): Promise<void> => {
    await expect(fetchUser(999)).rejects.toThrow('User not found');
  });
});
```

### 5.4 Mock 功能

```ts
import { describe, it, expect, vi } from 'vitest';

describe('UserService', () => {
  it('should call API', async (): Promise<void> => {
    const mockFetch = vi.fn().mockResolvedValue({ id: 1, name: 'John' });
    vi.stubGlobal('fetch', mockFetch);
    
    await fetchUser(1);
    
    expect(mockFetch).toHaveBeenCalledWith('/api/users/1');
  });
});
```

## 6. 最佳实践

### 6.1 测试组织

- 使用 describe 组织测试
- 使用清晰的测试名称
- 保持测试独立
- 使用测试钩子

### 6.2 性能优化

- 使用并行执行
- 优化慢速测试
- 使用测试缓存
- 合理使用 Mock

## 7. 注意事项

- **ESM 支持**：确保项目支持 ESM
- **配置优化**：根据项目需求配置
- **性能考虑**：注意测试执行性能
- **兼容性**：注意与 Jest 的兼容性

## 8. 常见问题

### 8.1 如何迁移 Jest 到 Vitest？

大部分 Jest API 兼容，可以逐步迁移。

### 8.2 如何处理 CommonJS 模块？

使用 Vitest 的 CommonJS 支持或转换为 ESM。

### 8.3 如何优化测试性能？

使用并行执行、测试缓存、优化慢速测试。

## 9. 实践任务

1. **安装配置**：安装和配置 Vitest
2. **编写测试**：编写单元测试
3. **测试钩子**：使用测试钩子
4. **Mock 使用**：使用 Mock 功能
5. **性能优化**：优化测试性能

---

**下一节**：[7.2.3 Jest（传统测试框架）](section-03-jest.md)
