# 7.2.3 Jest（传统测试框架）

## 1. 概述

Jest 是 Facebook 开发的 JavaScript 测试框架，提供了完整的测试解决方案，包括断言、Mock、覆盖率等功能。Jest 是 Node.js 社区最流行的测试框架之一。

## 2. 特性说明

- **零配置**：开箱即用
- **快照测试**：支持快照测试
- **Mock 功能**：强大的 Mock 功能
- **覆盖率**：内置覆盖率工具

## 3. 安装与配置

### 3.1 安装

```bash
npm install -D jest @types/jest ts-jest
```

### 3.2 配置文件

```ts
// jest.config.ts
import type { Config } from 'jest';

const config: Config = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  roots: ['<rootDir>/src', '<rootDir>/tests'],
  testMatch: ['**/__tests__/**/*.ts', '**/?(*.)+(spec|test).ts'],
  collectCoverageFrom: [
    'src/**/*.ts',
    '!src/**/*.d.ts'
  ],
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80
    }
  }
};

export default config;
```

### 3.3 package.json

```json
{
  "scripts": {
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage"
  }
}
```

## 4. 基本使用

### 4.1 测试文件

```ts
// math.test.ts
describe('add', () => {
  it('should add two numbers', (): void => {
    expect(add(1, 2)).toBe(3);
  });
  
  it('should handle negative numbers', (): void => {
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
describe('UserService', () => {
  beforeAll(async (): Promise<void> => {
    await setupDatabase();
  });
  
  afterAll(async (): Promise<void> => {
    await cleanupDatabase();
  });
  
  beforeEach(async (): Promise<void> => {
    await clearTestData();
  });
  
  afterEach(async (): Promise<void> => {
    await resetState();
  });
});
```

### 5.2 Mock 功能

```ts
// Mock 函数
const mockFn = jest.fn();
mockFn.mockReturnValue(42);
expect(mockFn()).toBe(42);

// Mock 模块
jest.mock('./api');
import { fetchUser } from './api';
(fetchUser as jest.Mock).mockResolvedValue({ id: 1, name: 'John' });

// Mock 实现
jest.spyOn(console, 'log').mockImplementation(() => {});
```

### 5.3 快照测试

```ts
it('should render component', (): void => {
  const component = render(<Button>Click me</Button>);
  expect(component).toMatchSnapshot();
});
```

## 6. 最佳实践

### 6.1 测试组织

- 使用 describe 组织测试
- 使用清晰的测试名称
- 保持测试独立
- 使用测试钩子

### 6.2 Mock 使用

- 合理使用 Mock
- 避免过度 Mock
- 使用真实实现
- 测试边界情况

## 7. 注意事项

- **配置优化**：根据项目需求配置
- **性能考虑**：注意测试执行性能
- **Mock 使用**：合理使用 Mock
- **测试维护**：及时维护测试代码

## 8. 常见问题

### 8.1 如何处理 TypeScript？

使用 ts-jest 或 @jest/globals。

### 8.2 如何优化测试性能？

使用并行执行、测试缓存、优化慢速测试。

### 8.3 如何处理异步测试？

使用 async/await 或返回 Promise。

## 9. 实践任务

1. **安装配置**：安装和配置 Jest
2. **编写测试**：编写单元测试
3. **Mock 使用**：使用 Mock 功能
4. **快照测试**：使用快照测试
5. **性能优化**：优化测试性能

---

**下一节**：[7.2.4 测试覆盖率](section-04-coverage.md)
