# 6.4.4 HTTPS/TLS

## 1. 概述

HTTPS（HTTP over TLS）是使用 TLS/SSL 加密的 HTTP 协议，保护数据传输安全。HTTPS 防止数据被窃听、篡改和中间人攻击。

## 2. TLS/SSL 基础

### 2.1 工作原理

```
1. 客户端请求 HTTPS 连接
2. 服务器发送证书
3. 客户端验证证书
4. 协商加密算法和密钥
5. 建立加密连接
6. 传输加密数据
```

### 2.2 证书类型

- **自签名证书**：开发和测试
- **CA 签名证书**：生产环境
- **通配符证书**：多个子域名
- **EV 证书**：扩展验证

## 3. Node.js HTTPS 服务器

### 3.1 基本配置

```ts
import https from 'node:https';
import { readFileSync } from 'node:fs';
import express, { Express } from 'express';

const app: Express = express();

const options = {
  key: readFileSync('private-key.pem'),
  cert: readFileSync('certificate.pem')
};

const server = https.createServer(options, app);

server.listen(443, (): void => {
  console.log('HTTPS server running on port 443');
});
```

### 3.2 Express 配置

```ts
import express, { Express } from 'express';

const app: Express = express();

// 强制 HTTPS（生产环境）
if (process.env.NODE_ENV === 'production') {
  app.use((req: express.Request, res: express.Response, next: express.NextFunction): void => {
    if (req.header('x-forwarded-proto') !== 'https') {
      res.redirect(`https://${req.header('host')}${req.url}`);
    } else {
      next();
    }
  });
}

app.listen(3000);
```

## 4. 证书管理

### 4.1 Let's Encrypt

```bash
# 安装 certbot
sudo apt-get install certbot

# 获取证书
sudo certbot certonly --standalone -d example.com

# 自动续期
sudo certbot renew
```

### 4.2 使用证书

```ts
const options = {
  key: readFileSync('/etc/letsencrypt/live/example.com/privkey.pem'),
  cert: readFileSync('/etc/letsencrypt/live/example.com/fullchain.pem')
};

const server = https.createServer(options, app);
```

## 5. 安全配置

### 5.1 TLS 版本

```ts
const options = {
  key: readFileSync('private-key.pem'),
  cert: readFileSync('certificate.pem'),
  minVersion: 'TLSv1.2',
  maxVersion: 'TLSv1.3',
  ciphers: 'ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384'
};
```

### 5.2 HSTS

```ts
import helmet from 'helmet';

app.use(helmet.hsts({
  maxAge: 31536000,
  includeSubDomains: true,
  preload: true
}));
```

## 6. 反向代理配置

### 6.1 Nginx 配置

```nginx
server {
    listen 443 ssl http2;
    server_name example.com;
    
    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
    
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;
    
    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## 7. 最佳实践

### 7.1 证书管理

- 使用 CA 签名证书
- 自动续期
- 监控证书过期
- 备份证书

### 7.2 安全配置

- 使用 TLS 1.2+
- 禁用弱加密
- 配置 HSTS
- 定期更新

## 8. 注意事项

- **证书有效期**：监控证书过期时间
- **TLS 版本**：使用最新 TLS 版本
- **性能影响**：HTTPS 有性能开销
- **配置测试**：使用 SSL Labs 测试配置

## 9. 常见问题

### 9.1 如何获取免费证书？

使用 Let's Encrypt 获取免费证书。

### 9.2 如何处理证书续期？

使用 certbot 自动续期，或使用 cron 任务。

### 9.3 如何测试 TLS 配置？

使用 SSL Labs SSL Test 测试配置。

## 10. 实践任务

1. **HTTPS 配置**：配置 HTTPS 服务器
2. **证书管理**：获取和管理证书
3. **安全配置**：配置 TLS 安全选项
4. **反向代理**：配置 Nginx 反向代理
5. **测试验证**：测试 HTTPS 配置

---

**下一章**：[6.5 API 安全](../chapter-05-api-security/readme.md)
