# 6.3.3 XSS 防护

## 1. 概述

XSS（Cross-Site Scripting）跨站脚本攻击是注入恶意脚本到网页中的攻击方式。XSS 攻击可以窃取用户数据、劫持用户会话、进行钓鱼攻击等。

## 2. XSS 类型

### 2.1 存储型 XSS

**特点**：恶意脚本存储在服务器，每次访问都会执行。

**示例**：
```ts
// ❌ 不安全：直接输出用户输入
app.post('/comments', (req: Request, res: Response): void => {
  const comment = req.body.comment;
  db.query('INSERT INTO comments (content) VALUES ($1)', [comment]);
  // 前端直接显示 comment，如果包含 <script>alert('XSS')</script> 会被执行
});
```

### 2.2 反射型 XSS

**特点**：恶意脚本通过 URL 参数反射到页面。

**示例**：
```ts
// ❌ 不安全：直接输出 URL 参数
app.get('/search', (req: Request, res: Response): void => {
  const query = req.query.q;
  res.send(`<h1>搜索结果: ${query}</h1>`); // 如果 query 包含脚本会被执行
});
```

### 2.3 DOM 型 XSS

**特点**：恶意脚本通过 DOM 操作注入。

**示例**：
```ts
// ❌ 不安全：前端直接使用 URL 参数
// const query = new URLSearchParams(window.location.search).get('q');
// document.getElementById('result').innerHTML = query; // 危险
```

## 3. 防护措施

### 3.1 输入验证和清理

```ts
import DOMPurify from 'isomorphic-dompurify';

// 清理 HTML
function sanitizeHtml(input: string): string {
  return DOMPurify.sanitize(input);
}

// 清理文本
function sanitizeText(input: string): string {
  return input
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#x27;')
    .replace(/\//g, '&#x2F;');
}

app.post('/comments', (req: Request, res: Response): void => {
  const comment = sanitizeHtml(req.body.comment);
  db.query('INSERT INTO comments (content) VALUES ($1)', [comment]);
});
```

### 3.2 输出编码

```ts
// 使用模板引擎自动编码
app.set('view engine', 'ejs');
// EJS 自动编码：<%= comment %>

// 手动编码
function encodeHtml(input: string): string {
  return input
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#x27;');
}
```

### 3.3 Content Security Policy

```ts
import helmet from 'helmet';

app.use(helmet.contentSecurityPolicy({
  directives: {
    defaultSrc: ["'self'"],
    scriptSrc: ["'self'", "'unsafe-inline'"],
    styleSrc: ["'self'", "'unsafe-inline'"],
    imgSrc: ["'self'", 'data:', 'https:'],
    connectSrc: ["'self'"],
    fontSrc: ["'self'"],
    objectSrc: ["'none'"],
    mediaSrc: ["'self'"],
    frameSrc: ["'none'"]
  }
}));
```

## 4. 最佳实践

### 4.1 输入处理

- 验证所有输入
- 清理用户输入
- 使用白名单验证
- 避免黑名单验证

### 4.2 输出处理

- 输出编码
- 使用模板引擎
- 避免 innerHTML
- 使用 textContent

## 5. 注意事项

- **输入验证**：始终验证和清理输入
- **输出编码**：始终编码输出
- **CSP 配置**：正确配置 CSP
- **框架使用**：使用安全的框架和库

## 6. 常见问题

### 6.1 如何检测 XSS 漏洞？

使用安全扫描工具、代码审查、渗透测试。

### 6.2 如何处理富文本输入？

使用 HTML 清理库（如 DOMPurify），配置白名单标签和属性。

### 6.3 如何配置 CSP？

根据应用需求配置 CSP，逐步收紧策略。

## 7. 实践任务

1. **输入清理**：实现输入清理功能
2. **输出编码**：实现输出编码
3. **CSP 配置**：配置 Content Security Policy
4. **XSS 测试**：进行 XSS 漏洞测试
5. **安全加固**：加固应用防止 XSS

---

**下一节**：[6.3.4 CSRF 防护](section-04-csrf.md)
