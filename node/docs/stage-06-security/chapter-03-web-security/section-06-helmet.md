# 6.3.6 Helmet.js 安全头

## 1. 概述

Helmet.js 是 Express 的安全中间件，通过设置 HTTP 安全头来防护多种 Web 安全威胁。Helmet.js 提供了简单易用的 API 来配置安全头。

## 2. 安装与配置

### 2.1 安装

```bash
npm install helmet
npm install @types/helmet -D
```

### 2.2 基本使用

```ts
import express, { Express } from 'express';
import helmet from 'helmet';

const app: Express = express();

// 使用所有默认安全头
app.use(helmet());
```

## 3. 安全头说明

### 3.1 Content-Security-Policy

```ts
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
    frameSrc: ["'none'"],
    upgradeInsecureRequests: []
  }
}));
```

### 3.2 X-Frame-Options

```ts
// 防止页面被嵌入 iframe
app.use(helmet.frameguard({ action: 'deny' }));
```

### 3.3 X-Content-Type-Options

```ts
// 防止 MIME 类型嗅探
app.use(helmet.noSniff());
```

### 3.4 X-XSS-Protection

```ts
// 启用浏览器 XSS 过滤器
app.use(helmet.xssFilter());
```

### 3.5 Strict-Transport-Security

```ts
// 强制使用 HTTPS
app.use(helmet.hsts({
  maxAge: 31536000,
  includeSubDomains: true,
  preload: true
}));
```

### 3.6 Referrer-Policy

```ts
// 控制 Referer 头
app.use(helmet.referrerPolicy({ policy: 'same-origin' }));
```

### 3.7 Permissions-Policy

```ts
// 控制浏览器功能
app.use(helmet.permissionsPolicy({
  features: {
    camera: ["'none'"],
    microphone: ["'none'"],
    geolocation: ["'self'"]
  }
}));
```

## 4. 完整配置

```ts
app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      scriptSrc: ["'self'"],
      styleSrc: ["'self'", "'unsafe-inline'"],
      imgSrc: ["'self'", 'data:', 'https:']
    }
  },
  hsts: {
    maxAge: 31536000,
    includeSubDomains: true
  },
  frameguard: {
    action: 'deny'
  },
  noSniff: true,
  xssFilter: true,
  referrerPolicy: {
    policy: 'same-origin'
  }
}));
```

## 5. 最佳实践

### 5.1 配置原则

- 根据应用需求配置
- 逐步收紧策略
- 测试安全头效果
- 定期审查配置

### 5.2 安全考虑

- 使用 HTTPS
- 配置 CSP
- 防止点击劫持
- 控制浏览器功能

## 6. 注意事项

- **CSP 配置**：正确配置 CSP，避免过于严格
- **HTTPS**：生产环境使用 HTTPS
- **测试**：测试安全头不影响功能
- **更新**：关注 Helmet.js 更新

## 7. 常见问题

### 7.1 如何配置 CSP？

根据应用需求逐步配置，从宽松到严格。

### 7.2 安全头是否影响性能？

影响很小，但建议在生产环境测试。

### 7.3 如何处理第三方资源？

在 CSP 中允许必要的第三方域名。

## 8. 实践任务

1. **安装配置**：安装和配置 Helmet.js
2. **安全头设置**：设置各种安全头
3. **CSP 配置**：配置 Content Security Policy
4. **测试验证**：测试安全头效果
5. **优化调整**：根据需求优化配置

---

**下一章**：[6.4 数据加密](../chapter-04-encryption/readme.md)
