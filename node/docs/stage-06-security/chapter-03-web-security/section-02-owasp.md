# 6.3.2 OWASP Top 10（2025）

## 1. 概述

OWASP Top 10 是最常见的 Web 应用安全风险列表，帮助开发者和组织了解并防护主要的安全威胁。了解 OWASP Top 10 是 Web 安全的基础。

## 2. OWASP Top 10（2025）

### 2.1 A01:2021 – 失效的访问控制

**描述**：访问控制失效导致未授权访问。

**防护措施**：
- 实施最小权限原则
- 服务器端验证权限
- 防止权限提升
- 记录权限操作

### 2.2 A02:2021 – 加密失败

**描述**：敏感数据未加密或加密不当。

**防护措施**：
- 使用强加密算法
- 保护加密密钥
- 使用 HTTPS
- 加密敏感数据

### 2.3 A03:2021 – 注入

**描述**：SQL、NoSQL、命令注入等。

**防护措施**：
- 使用参数化查询
- 输入验证和清理
- 使用 ORM 框架
- 最小权限原则

### 2.4 A04:2021 – 不安全设计

**描述**：设计阶段的安全缺陷。

**防护措施**：
- 威胁建模
- 安全设计模式
- 安全架构审查
- 安全需求分析

### 2.5 A05:2021 – 安全配置错误

**描述**：不安全或不完整的配置。

**防护措施**：
- 安全默认配置
- 最小化功能
- 定期安全审查
- 自动化配置检查

### 2.6 A06:2021 – 易受攻击和过时的组件

**描述**：使用含有已知漏洞的组件。

**防护措施**：
- 依赖管理
- 定期更新组件
- 漏洞扫描
- 组件审查

### 2.7 A07:2021 – 身份认证和会话管理失效

**描述**：身份认证和会话管理缺陷。

**防护措施**：
- 强密码策略
- 多因素认证
- 安全会话管理
- 密码加密

### 2.8 A08:2021 – 软件和数据完整性失效

**描述**：软件和数据完整性验证不足。

**防护措施**：
- 代码签名
- 依赖验证
- CI/CD 安全
- 数据完整性检查

### 2.9 A09:2021 – 安全日志和监控失效

**描述**：安全日志和监控不足。

**防护措施**：
- 记录安全事件
- 实时监控
- 告警机制
- 日志分析

### 2.10 A10:2021 – 服务端请求伪造（SSRF）

**描述**：服务端请求伪造漏洞。

**防护措施**：
- 验证 URL
- 白名单验证
- 网络隔离
- 输入验证

## 3. 防护实施

### 3.1 安全编码

```ts
// ❌ 不安全：SQL 注入
app.get('/users', (req: Request, res: Response): void => {
  const query = `SELECT * FROM users WHERE name = '${req.query.name}'`;
  db.query(query);
});

// ✅ 安全：参数化查询
app.get('/users', (req: Request, res: Response): void => {
  db.query('SELECT * FROM users WHERE name = $1', [req.query.name]);
});
```

### 3.2 输入验证

```ts
import { z } from 'zod';

const userSchema = z.object({
  email: z.string().email(),
  password: z.string().min(8),
  age: z.number().min(0).max(150)
});

app.post('/users', (req: Request, res: Response): void => {
  const result = userSchema.safeParse(req.body);
  if (!result.success) {
    res.status(400).json({ errors: result.error.errors });
    return;
  }
  // 处理验证通过的数据
});
```

## 4. 最佳实践

### 4.1 安全开发

- 安全编码规范
- 代码审查
- 安全测试
- 威胁建模

### 4.2 安全运维

- 安全配置
- 定期更新
- 漏洞扫描
- 安全监控

## 5. 注意事项

- **持续更新**：关注 OWASP Top 10 更新
- **全面防护**：实施全面的安全防护
- **安全测试**：定期进行安全测试
- **安全意识**：提高团队安全意识

## 6. 常见问题

### 6.1 如何评估应用安全性？

使用 OWASP 工具、安全扫描、渗透测试。

### 6.2 如何修复安全漏洞？

根据 OWASP 指南修复漏洞，实施安全补丁。

### 6.3 如何建立安全流程？

参考 OWASP 最佳实践，建立安全开发流程。

## 7. 相关资源

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP 工具](https://owasp.org/www-project-web-security-testing-guide/)

---

**下一节**：[6.3.3 XSS 防护](section-03-xss.md)
