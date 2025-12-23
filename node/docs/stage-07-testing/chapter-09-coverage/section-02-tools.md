# 7.9.2 Istanbul 与 c8

## 1. 概述

Istanbul 和 c8 是常用的代码覆盖率工具，用于收集和分析代码覆盖率。Istanbul 是传统的覆盖率工具，c8 是基于 V8 的现代覆盖率工具。

## 2. Istanbul

### 2.1 安装

```bash
npm install -D nyc
```

### 2.2 配置

```json
// package.json
{
  "scripts": {
    "test": "nyc --reporter=text --reporter=html --reporter=json npm run test:unit",
    "test:coverage": "nyc --reporter=html npm run test:unit"
  },
  "nyc": {
    "check-coverage": true,
    "lines": 80,
    "functions": 80,
    "branches": 80,
    "statements": 80,
    "exclude": [
      "**/*.test.ts",
      "**/*.spec.ts",
      "coverage/**"
    ]
  }
}
```

### 2.3 使用

```bash
# 运行测试并生成覆盖率
npm test

# 查看 HTML 报告
open coverage/index.html

# 检查覆盖率阈值
nyc check-coverage
```

## 3. c8

### 3.1 安装

```bash
npm install -D c8
```

### 3.2 配置

```json
// package.json
{
  "scripts": {
    "test": "c8 --reporter=text --reporter=html --reporter=json npm run test:unit",
    "test:coverage": "c8 --reporter=html npm run test:unit"
  },
  "c8": {
    "check-coverage": true,
    "lines": 80,
    "functions": 80,
    "branches": 80,
    "statements": 80,
    "exclude": [
      "**/*.test.ts",
      "**/*.spec.ts",
      "coverage/**"
    ]
  }
}
```

### 3.3 使用

```bash
# 运行测试并生成覆盖率
npm test

# 查看 HTML 报告
open coverage/index.html

# 检查覆盖率阈值
c8 check-coverage
```

## 4. 工具对比

### 4.1 Istanbul vs c8

| 特性 | Istanbul | c8 |
|------|----------|-----|
| 基于 | Babel | V8 |
| 性能 | 中等 | 高 |
| ESM 支持 | 需要配置 | 原生支持 |
| TypeScript | 需要配置 | 原生支持 |
| 维护状态 | 维护中 | 活跃 |

### 4.2 选择建议

- **现代项目**：使用 c8
- **ESM 项目**：使用 c8
- **TypeScript 项目**：使用 c8
- **传统项目**：使用 Istanbul

## 5. 覆盖率报告

### 5.1 HTML 报告

```bash
# 生成 HTML 报告
npm run test:coverage

# 查看报告
open coverage/index.html
```

### 5.2 文本报告

```bash
# 生成文本报告
npm test

# 输出示例
----------|---------|----------|---------|---------|-------------------
File      | % Stmts | % Branch | % Funcs | % Lines | Uncovered Line #s
----------|---------|----------|---------|---------|-------------------
All files |   85.23 |    80.45 |   90.12 |   85.23 |
 utils.ts |   90.00 |    85.00 |  100.00 |   90.00 | 15-16
 api.ts   |   80.00 |    75.00 |   80.00 |   80.00 | 25-30
----------|---------|----------|---------|---------|-------------------
```

## 6. 最佳实践

### 6.1 配置优化

- 设置合理的阈值
- 排除测试文件
- 排除配置文件
- 使用多种报告格式

### 6.2 覆盖率分析

- 分析未覆盖代码
- 识别测试盲点
- 优化测试策略
- 定期审查覆盖率

## 7. 注意事项

- **工具选择**：根据项目需求选择工具
- **配置优化**：优化覆盖率配置
- **报告分析**：深入分析覆盖率报告
- **持续改进**：逐步提高覆盖率

## 8. 常见问题

### 8.1 如何选择工具？

根据项目类型、ESM 支持、TypeScript 支持选择。

### 8.2 如何处理未覆盖代码？

分析未覆盖代码，添加相应测试。

### 8.3 如何优化覆盖率配置？

设置合理的阈值，排除不必要的文件。

## 9. 实践任务

1. **安装工具**：安装覆盖率工具
2. **配置工具**：配置覆盖率工具
3. **生成报告**：生成覆盖率报告
4. **分析报告**：分析覆盖率报告
5. **优化覆盖率**：优化测试覆盖率

---

**下一节**：[7.9.3 覆盖率报告与分析](section-03-reports.md)
