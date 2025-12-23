# 6.7.2 npm audit

## 1. 概述

npm audit 是 npm 内置的依赖漏洞检测工具，可以扫描项目依赖中的已知安全漏洞，并提供修复建议。

## 2. 基本使用

### 2.1 检查漏洞

```bash
# 检查依赖漏洞
npm audit

# 检查并生成报告
npm audit --json > audit-report.json
```

### 2.2 自动修复

```bash
# 自动修复可修复的漏洞
npm audit fix

# 强制修复（可能破坏兼容性）
npm audit fix --force
```

### 2.3 查看详细信息

```bash
# 查看特定包的漏洞
npm audit <package-name>

# 查看漏洞详情
npm audit --audit-level=moderate
```

## 3. 输出解读

### 3.1 漏洞级别

- **Critical**：严重漏洞
- **High**：高危漏洞
- **Moderate**：中等漏洞
- **Low**：低危漏洞
- **Info**：信息

### 3.2 输出示例

```
=== npm audit security report ===

Critical: 2
High: 5
Moderate: 10
Low: 3

found 20 vulnerabilities in 150 packages
```

## 4. 配置选项

### 4.1 .npmrc 配置

```ini
# 设置审计级别
audit-level=moderate

# 禁用审计
audit=false

# 生产环境不审计开发依赖
audit-production=true
```

### 4.2 package.json 配置

```json
{
  "scripts": {
    "audit": "npm audit",
    "audit:fix": "npm audit fix",
    "audit:report": "npm audit --json > audit-report.json"
  }
}
```

## 5. CI/CD 集成

### 5.1 GitHub Actions

```yaml
name: Security Audit

on: [push, pull_request]

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: npm ci
      - run: npm audit --audit-level=moderate
```

### 5.2 失败处理

```bash
# 如果发现严重漏洞，退出码不为 0
npm audit --audit-level=high

# 在 CI 中使用
npm audit --audit-level=high || exit 1
```

## 6. 最佳实践

### 6.1 定期检查

- 每次安装依赖后检查
- CI/CD 中集成检查
- 定期手动检查
- 监控漏洞更新

### 6.2 修复策略

- 优先修复严重漏洞
- 测试修复后的应用
- 记录修复过程
- 更新依赖文档

## 7. 注意事项

- **自动修复**：谨慎使用 --force，可能破坏兼容性
- **测试验证**：修复后测试应用
- **版本兼容**：注意版本兼容性
- **持续监控**：持续监控依赖安全

## 8. 常见问题

### 8.1 如何修复间接依赖漏洞？

更新直接依赖，或使用 npm audit fix。

### 8.2 如何处理无法自动修复的漏洞？

手动更新依赖版本，或寻找替代方案。

### 8.3 如何在 CI 中集成？

在 CI 流程中添加 npm audit 检查，设置合理的审计级别。

## 9. 实践任务

1. **漏洞检查**：使用 npm audit 检查漏洞
2. **自动修复**：使用 npm audit fix 修复漏洞
3. **CI 集成**：在 CI/CD 中集成审计
4. **报告生成**：生成审计报告
5. **持续监控**：建立持续监控机制

---

**下一节**：[6.7.3 Snyk 与 Dependabot](section-03-snyk-dependabot.md)
