# 6.7.3 Snyk 与 Dependabot

## 1. 概述

Snyk 和 Dependabot 是第三方依赖安全工具，提供更全面的漏洞检测、自动修复建议和持续监控功能。

## 2. Snyk

### 2.1 安装与配置

```bash
# 安装 Snyk CLI
npm install -g snyk

# 登录 Snyk
snyk auth

# 测试连接
snyk test
```

### 2.2 基本使用

```bash
# 测试项目漏洞
snyk test

# 监控项目
snyk monitor

# 修复漏洞
snyk wizard
```

### 2.3 配置文件

```json
{
  "$schema": "https://snyk.io/schema/project",
  "language": "node",
  "packageManager": "npm",
  "ignore": {
    "SNYK-JS-LODASH-567746": {
      "reason": "Not used in production",
      "expires": "2024-12-31T23:59:59.999Z"
    }
  }
}
```

### 2.4 Node.js 集成

```ts
import snyk from 'snyk';

async function testDependencies(): Promise<void> {
  try {
    const result = await snyk.test();
    console.log('Vulnerabilities:', result.vulnerabilities);
  } catch (error) {
    console.error('Snyk test failed:', error);
  }
}
```

## 3. Dependabot

### 3.1 GitHub 配置

在 `.github/dependabot.yml` 中配置：

```yaml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 10
    reviewers:
      - "team-security"
    labels:
      - "dependencies"
      - "security"
    commit-message:
      prefix: "chore"
      include: "scope"
```

### 3.2 安全更新

```yaml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "daily"
    open-pull-requests-limit: 5
    # 只创建安全更新 PR
    only-security-updates: true
```

### 3.3 版本策略

```yaml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    versioning-strategy: increase
    # 忽略特定包
    ignore:
      - dependency-name: "package-name"
        update-types: ["version-update:semver-major"]
```

## 4. 工具对比

### 4.1 Snyk vs Dependabot

| 特性 | Snyk | Dependabot |
|------|------|------------|
| 漏洞检测 | 全面 | 基础 |
| 自动修复 | 支持 | 支持 |
| CI 集成 | 支持 | GitHub Actions |
| 许可证检查 | 支持 | 不支持 |
| 成本 | 免费/付费 | 免费 |

### 4.2 选择建议

- **GitHub 项目**：使用 Dependabot
- **企业项目**：使用 Snyk
- **全面检测**：使用 Snyk
- **简单需求**：使用 Dependabot

## 5. 最佳实践

### 5.1 工具配置

- 配置合理的更新频率
- 设置 PR 限制
- 配置审查流程
- 设置告警规则

### 5.2 更新管理

- 及时审查 PR
- 测试更新
- 记录更新历史
- 监控更新影响

## 6. 注意事项

- **更新测试**：更新后测试应用
- **版本兼容**：注意版本兼容性
- **PR 审查**：审查自动生成的 PR
- **持续监控**：持续监控依赖安全

## 7. 常见问题

### 7.1 如何选择工具？

根据项目需求、平台、预算选择。

### 7.2 如何处理大量 PR？

设置合理的 PR 限制，批量处理更新。

### 7.3 如何防止破坏性更新？

配置版本策略，审查重大更新。

## 8. 实践任务

1. **Snyk 配置**：配置和使用 Snyk
2. **Dependabot 配置**：配置 Dependabot
3. **工具对比**：对比不同工具
4. **更新管理**：管理依赖更新
5. **持续监控**：建立持续监控机制

---

**下一节**：[6.7.4 漏洞扫描与修复](section-04-vulnerability.md)
