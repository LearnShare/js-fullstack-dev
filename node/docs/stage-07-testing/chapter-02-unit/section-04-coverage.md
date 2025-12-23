# 7.2.4 测试覆盖率

## 1. 概述

测试覆盖率是衡量测试质量的重要指标，表示测试覆盖了多少代码。测试覆盖率包括语句覆盖率、分支覆盖率、函数覆盖率和行覆盖率。

## 2. 覆盖率类型

### 2.1 语句覆盖率（Statement Coverage）

**定义**：执行了多少条语句。

**示例**：
```ts
function example(a: number, b: number): number {
  if (a > 0) {
    return a + b;  // 如果 a <= 0，这行不会执行
  }
  return a - b;
}
```

### 2.2 分支覆盖率（Branch Coverage）

**定义**：执行了多少个分支。

**示例**：
```ts
function example(a: number): string {
  if (a > 0) {
    return 'positive';  // 分支 1
  } else {
    return 'non-positive';  // 分支 2
  }
}
```

### 2.3 函数覆盖率（Function Coverage）

**定义**：调用了多少个函数。

### 2.4 行覆盖率（Line Coverage）

**定义**：执行了多少行代码。

## 3. Vitest 覆盖率

### 3.1 配置

```ts
// vitest.config.ts
import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html'],
      exclude: [
        'node_modules/',
        'tests/',
        '*.config.*'
      ],
      thresholds: {
        lines: 80,
        functions: 80,
        branches: 80,
        statements: 80
      }
    }
  }
});
```

### 3.2 生成报告

```bash
# 生成覆盖率报告
npm run test:coverage

# 查看 HTML 报告
open coverage/index.html
```

## 4. Jest 覆盖率

### 4.1 配置

```ts
// jest.config.ts
const config: Config = {
  collectCoverageFrom: [
    'src/**/*.ts',
    '!src/**/*.d.ts',
    '!src/**/*.test.ts'
  ],
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80
    }
  },
  coverageReporters: ['text', 'json', 'html', 'lcov']
};
```

### 4.2 生成报告

```bash
# 生成覆盖率报告
npm run test:coverage

# 查看 HTML 报告
open coverage/lcov-report/index.html
```

## 5. 覆盖率分析

### 5.1 查看未覆盖代码

```ts
// 未覆盖的代码
function unusedFunction(): void {
  console.log('This function is never called');
}
```

### 5.2 提高覆盖率

```ts
// 添加测试
describe('unusedFunction', () => {
  it('should be called', (): void => {
    unusedFunction();
    // 验证行为
  });
});
```

## 6. 覆盖率阈值

### 6.1 设置阈值

```ts
coverageThreshold: {
  global: {
    branches: 80,
    functions: 80,
    lines: 80,
    statements: 80
  },
  './src/utils/': {
    branches: 90,
    functions: 90,
    lines: 90,
    statements: 90
  }
}
```

### 6.2 CI 集成

```yaml
# GitHub Actions
- name: Run tests with coverage
  run: npm run test:coverage

- name: Check coverage threshold
  run: npm run test:coverage -- --coverageThreshold
```

## 7. 最佳实践

### 7.1 覆盖率目标

- 设置合理的目标（80%+）
- 关键代码 100% 覆盖
- 逐步提高覆盖率
- 关注质量而非数量

### 7.2 覆盖率分析

- 分析未覆盖代码
- 识别测试盲点
- 优化测试策略
- 定期审查覆盖率

## 8. 注意事项

- **质量优先**：覆盖率不是唯一指标
- **合理目标**：设置合理的覆盖率目标
- **关键代码**：优先覆盖关键代码
- **持续改进**：逐步提高覆盖率

## 9. 常见问题

### 9.1 覆盖率多少合适？

通常 80%+ 是合理目标，关键代码应该 100% 覆盖。

### 9.2 如何提高覆盖率？

分析未覆盖代码，添加相应测试。

### 9.3 覆盖率是否越高越好？

不是，应该关注测试质量而非数量。

## 10. 实践任务

1. **配置覆盖率**：配置测试覆盖率
2. **生成报告**：生成覆盖率报告
3. **分析覆盖率**：分析覆盖率数据
4. **提高覆盖率**：提高测试覆盖率
5. **设置阈值**：设置覆盖率阈值

---

**下一章**：[7.3 集成测试](../chapter-03-integration/readme.md)
