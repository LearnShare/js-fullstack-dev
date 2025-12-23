# 6.1.2 Session + Cookie

## 1. 概述

Session + Cookie 是传统的身份认证方式，服务器在内存或数据库中存储会话信息，客户端通过 Cookie 存储 Session ID。这种方式安全性高，适合传统 Web 应用。

## 2. 工作原理

### 2.1 基本流程

```
1. 用户登录，服务器验证凭证
2. 服务器创建 Session，生成 Session ID
3. 服务器将 Session ID 通过 Cookie 发送给客户端
4. 客户端保存 Cookie
5. 后续请求携带 Cookie
6. 服务器根据 Session ID 查找 Session
7. 验证 Session 有效性
```

### 2.2 Session 存储

- **内存存储**：存储在服务器内存（简单但不持久）
- **数据库存储**：存储在数据库（持久但需要数据库）
- **Redis 存储**：存储在 Redis（性能好且持久）

## 3. Express 实现

### 3.1 安装依赖

```bash
npm install express-session
npm install connect-redis
npm install @types/express-session -D
```

### 3.2 基本配置

```ts
import express, { Express, Request, Response, NextFunction } from 'express';
import session from 'express-session';
import RedisStore from 'connect-redis';
import { createClient } from 'redis';

const app: Express = express();

const redisClient = createClient({
  url: process.env.REDIS_URL
});
redisClient.connect().catch(console.error);

app.use(session({
  store: new RedisStore({ client: redisClient }),
  secret: process.env.SESSION_SECRET!,
  resave: false,
  saveUninitialized: false,
  cookie: {
    secure: process.env.NODE_ENV === 'production',
    httpOnly: true,
    maxAge: 24 * 60 * 60 * 1000, // 24 小时
    sameSite: 'strict'
  },
  name: 'sessionId'
}));
```

### 3.3 登录实现

```ts
interface LoginRequest {
  username: string;
  password: string;
}

app.post('/login', async (req: Request, res: Response): Promise<void> => {
  const { username, password }: LoginRequest = req.body;
  
  // 验证用户凭证
  const user = await validateUser(username, password);
  
  if (user) {
    // 创建 Session
    (req.session as any).userId = user.id;
    (req.session as any).username = user.username;
    
    res.json({ message: 'Login successful' });
  } else {
    res.status(401).json({ message: 'Invalid credentials' });
  }
});
```

### 3.4 认证中间件

```ts
interface AuthenticatedRequest extends Request {
  session: {
    userId?: number;
    username?: string;
  };
}

function requireAuth(req: Request, res: Response, next: NextFunction): void {
  const authReq = req as AuthenticatedRequest;
  
  if (authReq.session && authReq.session.userId) {
    next();
  } else {
    res.status(401).json({ message: 'Unauthorized' });
  }
}

// 使用
app.get('/profile', requireAuth, (req: Request, res: Response): void => {
  const authReq = req as AuthenticatedRequest;
  res.json({ userId: authReq.session.userId, username: authReq.session.username });
});
```

### 3.5 登出实现

```ts
app.post('/logout', (req: Request, res: Response): void => {
  req.session.destroy((err: Error | null): void => {
    if (err) {
      res.status(500).json({ message: 'Logout failed' });
    } else {
      res.clearCookie('sessionId');
      res.json({ message: 'Logout successful' });
    }
  });
});
```

## 4. 安全配置

### 4.1 Cookie 安全

```ts
app.use(session({
  // ... 其他配置
  cookie: {
    secure: true,        // 仅 HTTPS
    httpOnly: true,      // 防止 XSS
    sameSite: 'strict',  // 防止 CSRF
    maxAge: 24 * 60 * 60 * 1000
  }
}));
```

### 4.2 Session 固定防护

```ts
app.post('/login', async (req: Request, res: Response): Promise<void> => {
  // 登录前重新生成 Session ID
  req.session.regenerate((err: Error | null): void => {
    if (err) {
      res.status(500).json({ message: 'Login failed' });
      return;
    }
    
    // 设置 Session 数据
    (req.session as any).userId = user.id;
    res.json({ message: 'Login successful' });
  });
});
```

## 5. 最佳实践

### 5.1 Session 管理

- 使用 Redis 存储 Session
- 设置合理的过期时间
- 实现 Session 刷新
- 定期清理过期 Session

### 5.2 安全考虑

- 使用 HTTPS
- 设置安全的 Cookie
- 防止 Session 固定
- 实现安全退出

## 6. 注意事项

- **存储选择**：根据需求选择 Session 存储方式
- **安全配置**：正确配置 Cookie 安全选项
- **性能优化**：使用 Redis 提高性能
- **会话管理**：合理管理会话生命周期

## 7. 常见问题

### 7.1 如何选择 Session 存储？

根据性能需求、持久化需求、扩展性需求选择。

### 7.2 如何处理 Session 过期？

设置合理的过期时间，实现自动刷新机制。

### 7.3 如何防止 Session 劫持？

使用 HTTPS、安全 Cookie、定期刷新 Session。

## 8. 实践任务

1. **配置 Session**：配置 Express Session
2. **实现登录**：实现登录功能
3. **认证中间件**：实现认证中间件
4. **安全配置**：配置安全选项
5. **会话管理**：实现会话管理功能

---

**下一节**：[6.1.3 JWT（JSON Web Token）](section-03-jwt.md)
