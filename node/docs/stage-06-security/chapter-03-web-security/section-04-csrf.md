# 6.3.4 CSRF 防护

## 1. 概述

CSRF（Cross-Site Request Forgery）跨站请求伪造是诱导用户执行非预期操作的攻击方式。CSRF 攻击利用用户的身份认证状态，伪造用户请求。

## 2. CSRF 攻击原理

### 2.1 攻击流程

```
1. 用户登录网站 A，获得认证 Cookie
2. 用户访问恶意网站 B
3. 网站 B 包含指向网站 A 的请求
4. 浏览器自动携带 Cookie 发送请求
5. 网站 A 认为这是用户的合法请求
6. 执行非预期操作
```

### 2.2 攻击示例

```html
<!-- 恶意网站 -->
<img src="https://bank.com/transfer?to=attacker&amount=1000" />
```

## 3. 防护措施

### 3.1 CSRF Token

```ts
import csrf from 'csurf';
import { randomBytes } from 'node:crypto';

const csrfProtection = csrf({ cookie: true });

// 生成 CSRF Token
app.get('/form', csrfProtection, (req: Request, res: Response): void => {
  res.render('form', { csrfToken: req.csrfToken() });
});

// 验证 CSRF Token
app.post('/transfer', csrfProtection, (req: Request, res: Response): void => {
  // Token 验证通过，处理请求
  res.json({ message: 'Transfer successful' });
});
```

### 3.2 SameSite Cookie

```ts
app.use(session({
  cookie: {
    sameSite: 'strict', // 或 'lax'
    secure: true,
    httpOnly: true
  }
}));
```

### 3.3 双重提交 Cookie

```ts
function generateCSRFToken(): string {
  return randomBytes(32).toString('hex');
}

app.use((req: Request, res: Response, next: NextFunction): void => {
  if (req.method === 'GET') {
    const token = generateCSRFToken();
    res.cookie('csrf-token', token, { httpOnly: false, sameSite: 'strict' });
    (req as any).csrfToken = token;
  }
  next();
});

app.post('/transfer', (req: Request, res: Response): void => {
  const cookieToken = req.cookies['csrf-token'];
  const headerToken = req.headers['x-csrf-token'];
  
  if (!cookieToken || cookieToken !== headerToken) {
    res.status(403).json({ message: 'CSRF token mismatch' });
    return;
  }
  
  // 处理请求
});
```

### 3.4 Referer 检查

```ts
function checkReferer(req: Request, res: Response, next: NextFunction): void {
  const referer = req.headers.referer;
  const origin = req.headers.origin;
  const allowedOrigins = [process.env.ALLOWED_ORIGIN!];
  
  if (referer && !allowedOrigins.some((allowed: string) => referer.startsWith(allowed))) {
    res.status(403).json({ message: 'Invalid referer' });
    return;
  }
  
  next();
}

app.post('/transfer', checkReferer, (req: Request, res: Response): void => {
  // 处理请求
});
```

## 4. 最佳实践

### 4.1 多层防护

- 使用 CSRF Token
- 设置 SameSite Cookie
- 检查 Referer
- 验证 Origin

### 4.2 安全配置

- 使用 HTTPS
- 设置安全 Cookie
- 实现 Token 刷新
- 记录安全事件

## 5. 注意事项

- **Token 安全**：保护 CSRF Token
- **Cookie 配置**：正确配置 Cookie
- **Referer 检查**：注意 Referer 可能为空
- **GET 请求**：避免在 GET 请求中执行修改操作

## 6. 常见问题

### 6.1 如何选择防护方法？

结合使用多种方法，CSRF Token + SameSite Cookie 是推荐组合。

### 6.2 如何处理 API 请求？

使用 CSRF Token 或 API Key，避免依赖 Cookie。

### 6.3 如何测试 CSRF 防护？

创建测试页面，尝试伪造请求。

## 7. 实践任务

1. **CSRF Token**：实现 CSRF Token 防护
2. **SameSite Cookie**：配置 SameSite Cookie
3. **Referer 检查**：实现 Referer 检查
4. **多层防护**：实现多层 CSRF 防护
5. **安全测试**：进行 CSRF 攻击测试

---

**下一节**：[6.3.5 SQL 注入防护](section-05-sql-injection.md)
