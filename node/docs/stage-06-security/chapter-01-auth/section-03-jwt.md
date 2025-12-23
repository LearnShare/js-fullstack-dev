# 6.1.3 JWT（JSON Web Token）

## 1. 概述

JWT（JSON Web Token）是一种无状态的身份认证方式，将用户信息编码为 Token，客户端存储 Token 并在请求中携带。JWT 适合 API 服务和分布式系统。

## 2. JWT 结构

### 2.1 Token 组成

JWT 由三部分组成，用 `.` 分隔：
- **Header**：算法和类型
- **Payload**：用户信息和声明
- **Signature**：签名

### 2.2 Token 示例

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjEsInVzZXJuYW1lIjoiam9obiJ9.signature
```

## 3. 安装与使用

### 3.1 安装

```bash
npm install jsonwebtoken
npm install @types/jsonwebtoken -D
```

### 3.2 生成 Token

```ts
import jwt from 'jsonwebtoken';

interface TokenPayload {
  userId: number;
  username: string;
}

function generateToken(payload: TokenPayload): string {
  const secret: string = process.env.JWT_SECRET!;
  const expiresIn: string = process.env.JWT_EXPIRES_IN || '24h';
  
  return jwt.sign(payload, secret, { expiresIn });
}

// 使用
const token = generateToken({ userId: 1, username: 'john' });
```

### 3.3 验证 Token

```ts
function verifyToken(token: string): TokenPayload | null {
  try {
    const secret: string = process.env.JWT_SECRET!;
    const decoded = jwt.verify(token, secret) as TokenPayload;
    return decoded;
  } catch (error) {
    return null;
  }
}

// 使用
const payload = verifyToken(token);
if (payload) {
  console.log('User ID:', payload.userId);
}
```

## 4. Express 实现

### 4.1 登录接口

```ts
import express, { Express, Request, Response } from 'express';

const app: Express = express();

app.post('/login', async (req: Request, res: Response): Promise<void> => {
  const { username, password }: { username: string; password: string } = req.body;
  
  // 验证用户凭证
  const user = await validateUser(username, password);
  
  if (user) {
    const token = generateToken({ userId: user.id, username: user.username });
    res.json({ token });
  } else {
    res.status(401).json({ message: 'Invalid credentials' });
  }
});
```

### 4.2 认证中间件

```ts
import { Request, Response, NextFunction } from 'express';

interface AuthenticatedRequest extends Request {
  user?: TokenPayload;
}

function authenticateToken(req: Request, res: Response, next: NextFunction): void {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1]; // Bearer TOKEN
  
  if (!token) {
    res.status(401).json({ message: 'Token required' });
    return;
  }
  
  const payload = verifyToken(token);
  if (!payload) {
    res.status(403).json({ message: 'Invalid token' });
    return;
  }
  
  (req as AuthenticatedRequest).user = payload;
  next();
}

// 使用
app.get('/profile', authenticateToken, (req: Request, res: Response): void => {
  const authReq = req as AuthenticatedRequest;
  res.json({ userId: authReq.user!.userId, username: authReq.user!.username });
});
```

## 5. Token 刷新

### 5.1 刷新 Token 实现

```ts
function generateRefreshToken(payload: TokenPayload): string {
  const secret: string = process.env.JWT_REFRESH_SECRET!;
  return jwt.sign(payload, secret, { expiresIn: '7d' });
}

function verifyRefreshToken(token: string): TokenPayload | null {
  try {
    const secret: string = process.env.JWT_REFRESH_SECRET!;
    const decoded = jwt.verify(token, secret) as TokenPayload;
    return decoded;
  } catch (error) {
    return null;
  }
}

app.post('/refresh', (req: Request, res: Response): void => {
  const { refreshToken }: { refreshToken: string } = req.body;
  
  const payload = verifyRefreshToken(refreshToken);
  if (!payload) {
    res.status(403).json({ message: 'Invalid refresh token' });
    return;
  }
  
  const newToken = generateToken({ userId: payload.userId, username: payload.username });
  res.json({ token: newToken });
});
```

## 6. 最佳实践

### 6.1 Token 安全

- 使用强密钥
- 设置合理的过期时间
- 实现 Token 刷新
- 支持 Token 撤销

### 6.2 存储方式

- **内存存储**：适合单页应用
- **HttpOnly Cookie**：更安全但需要 CSRF 防护
- **LocalStorage**：简单但不安全

## 7. 注意事项

- **密钥安全**：保护 JWT 密钥
- **Token 大小**：避免在 Payload 中存储过多数据
- **过期时间**：设置合理的过期时间
- **Token 撤销**：实现 Token 撤销机制

## 8. 常见问题

### 8.1 如何存储 JWT Token？

根据应用类型选择，Web 应用用 HttpOnly Cookie，移动应用用安全存储。

### 8.2 如何处理 Token 过期？

实现 Token 刷新机制，使用 Refresh Token。

### 8.3 如何撤销 Token？

使用黑名单或数据库存储 Token 状态。

## 9. 实践任务

1. **生成 Token**：实现 JWT Token 生成
2. **验证 Token**：实现 Token 验证
3. **认证中间件**：实现认证中间件
4. **Token 刷新**：实现 Token 刷新机制
5. **安全配置**：配置 Token 安全选项

---

**下一节**：[6.1.4 OAuth 2.0 与 OIDC](section-04-oauth2.md)
