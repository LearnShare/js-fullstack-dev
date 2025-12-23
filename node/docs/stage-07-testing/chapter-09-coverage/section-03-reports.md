# 7.9.3 覆盖率报告与分析

## 1. 概述

覆盖率报告是分析测试覆盖率的重要工具，通过分析覆盖率报告可以识别未覆盖的代码、优化测试策略、提高测试质量。

## 2. 报告类型

### 2.1 HTML 报告

**特点**：
- 可视化展示
- 交互式界面
- 详细代码视图
- 未覆盖代码高亮

**使用**：
```bash
npm run test:coverage
open coverage/index.html
```

### 2.2 文本报告

**特点**：
- 命令行输出
- 快速查看
- 适合 CI/CD
- 简洁明了

**使用**：
```bash
npm test
```

### 2.3 JSON 报告

**特点**：
- 结构化数据
- 适合自动化处理
- 可以集成到工具
- 支持数据分析

**使用**：
```bash
npm test -- --coverage --reporter=json
```

## 3. 报告分析

### 3.1 覆盖率指标

```ts
interface CoverageReport {
  total: {
    statements: { total: number; covered: number; pct: number };
    branches: { total: number; covered: number; pct: number };
    functions: { total: number; covered: number; pct: number };
    lines: { total: number; covered: number; pct: number };
  };
  files: Array<{
    path: string;
    statements: { total: number; covered: number; pct: number };
    branches: { total: number; covered: number; pct: number };
    functions: { total: number; covered: number; pct: number };
    lines: { total: number; covered: number; pct: number };
    uncoveredLines: number[];
  }>;
}
```

### 3.2 未覆盖代码分析

```ts
function analyzeUncoveredCode(report: CoverageReport): void {
  for (const file of report.files) {
    if (file.statements.pct < 80) {
      console.warn(`Low coverage in ${file.path}: ${file.statements.pct}%`);
      console.warn(`Uncovered lines: ${file.uncoveredLines.join(', ')}`);
    }
  }
}
```

## 4. 覆盖率优化

### 4.1 识别盲点

```ts
// 未覆盖的代码
function processPayment(amount: number): void {
  if (amount < 0) {
    throw new Error('Invalid amount'); // 未覆盖
  }
  
  if (amount > 10000) {
    requireApproval(); // 未覆盖
  }
  
  // 正常流程已覆盖
  executePayment(amount);
}
```

### 4.2 添加测试

```ts
describe('processPayment', () => {
  it('should throw error for negative amount', (): void => {
    expect(() => processPayment(-100)).toThrow('Invalid amount');
  });
  
  it('should require approval for large amount', (): void => {
    const requireApprovalSpy = vi.spyOn(approvalService, 'requireApproval');
    processPayment(15000);
    expect(requireApprovalSpy).toHaveBeenCalled();
  });
});
```

## 5. CI/CD 集成

### 5.1 GitHub Actions

```yaml
name: Test Coverage

on: [push, pull_request]

jobs:
  coverage:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
      - run: npm ci
      - run: npm run test:coverage
      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage/coverage-final.json
```

### 5.2 覆盖率检查

```ts
// coverage-check.ts
import { readFileSync } from 'node:fs';

const report = JSON.parse(readFileSync('coverage/coverage-final.json', 'utf8'));

const thresholds = {
  statements: 80,
  branches: 80,
  functions: 80,
  lines: 80
};

let failed = false;

for (const [file, data] of Object.entries(report)) {
  const coverage = (data as any).s;
  const statements = Object.values(coverage).filter((v: any) => v > 0).length;
  const total = Object.keys(coverage).length;
  const pct = (statements / total) * 100;
  
  if (pct < thresholds.statements) {
    console.error(`Coverage below threshold in ${file}: ${pct}%`);
    failed = true;
  }
}

if (failed) {
  process.exit(1);
}
```

## 6. 最佳实践

### 6.1 报告使用

- 定期查看报告
- 分析未覆盖代码
- 识别测试盲点
- 优化测试策略

### 6.2 覆盖率管理

- 设置合理阈值
- 关键代码 100% 覆盖
- 逐步提高覆盖率
- 关注质量而非数量

## 7. 注意事项

- **质量优先**：覆盖率不是唯一指标
- **合理目标**：设置合理的覆盖率目标
- **关键代码**：优先覆盖关键代码
- **持续改进**：逐步提高覆盖率

## 8. 常见问题

### 8.1 如何分析覆盖率报告？

查看 HTML 报告，分析未覆盖代码，识别测试盲点。

### 8.2 如何提高覆盖率？

分析未覆盖代码，添加相应测试。

### 8.3 如何在 CI 中集成？

在 CI 流程中生成覆盖率报告，设置覆盖率阈值。

## 9. 实践任务

1. **生成报告**：生成覆盖率报告
2. **分析报告**：分析覆盖率报告
3. **识别盲点**：识别测试盲点
4. **优化覆盖率**：优化测试覆盖率
5. **CI 集成**：在 CI 中集成覆盖率检查

---

**阶段七完成**：恭喜完成阶段七的学习！可以继续学习阶段八：性能优化与可观测性。
