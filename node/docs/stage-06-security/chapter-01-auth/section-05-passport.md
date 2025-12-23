# 6.1.5 Passport.js

## 1. 概述

Passport.js 是 Node.js 的身份认证中间件，支持多种认证策略（本地、OAuth、JWT 等）。Passport.js 简化了认证流程，提供了统一的认证接口。

## 2. 安装与配置

### 2.1 安装

```bash
npm install passport
npm install passport-local
npm install passport-jwt
npm install @types/passport -D
npm install @types/passport-local -D
npm install @types/passport-jwt -D
```

### 2.2 基本配置

```ts
import express, { Express } from 'express';
import passport from 'passport';
import { Strategy as LocalStrategy } from 'passport-local';
import { Strategy as JWTStrategy, ExtractJwt } from 'passport-jwt';

const app: Express = express();

app.use(passport.initialize());
```

## 3. 本地策略

### 3.1 配置本地策略

```ts
passport.use(new LocalStrategy(
  {
    usernameField: 'email',
    passwordField: 'password'
  },
  async (email: string, password: string, done: (error: any, user?: any) => void): Promise<void> => {
    try {
      const user = await findUserByEmail(email);
      if (!user) {
        return done(null, false, { message: 'User not found' });
      }
      
      const isValid = await verifyPassword(password, user.password);
      if (!isValid) {
        return done(null, false, { message: 'Invalid password' });
      }
      
      return done(null, user);
    } catch (error) {
      return done(error);
    }
  }
));
```

### 3.2 序列化用户

```ts
passport.serializeUser((user: any, done: (err: any, id?: any) => void): void => {
  done(null, user.id);
});

passport.deserializeUser(async (id: number, done: (err: any, user?: any) => void): Promise<void> => {
  try {
    const user = await findUserById(id);
    done(null, user);
  } catch (error) {
    done(error);
  }
});
```

### 3.3 登录路由

```ts
app.post('/login', passport.authenticate('local', {
  successRedirect: '/',
  failureRedirect: '/login',
  failureFlash: true
}));
```

## 4. JWT 策略

### 4.1 配置 JWT 策略

```ts
passport.use(new JWTStrategy(
  {
    jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
    secretOrKey: process.env.JWT_SECRET!
  },
  async (payload: any, done: (error: any, user?: any) => void): Promise<void> => {
    try {
      const user = await findUserById(payload.userId);
      if (user) {
        return done(null, user);
      }
      return done(null, false);
    } catch (error) {
      return done(error);
    }
  }
));
```

### 4.2 保护路由

```ts
app.get('/profile', passport.authenticate('jwt', { session: false }), (req: Request, res: Response): void => {
  res.json({ user: req.user });
});
```

## 5. OAuth 策略

### 5.1 安装 OAuth 策略

```bash
npm install passport-google-oauth20
npm install passport-github2
```

### 5.2 配置 Google 策略

```ts
import { Strategy as GoogleStrategy } from 'passport-google-oauth20';

passport.use(new GoogleStrategy(
  {
    clientID: process.env.GOOGLE_CLIENT_ID!,
    clientSecret: process.env.GOOGLE_CLIENT_SECRET!,
    callbackURL: '/auth/google/callback'
  },
  async (accessToken: string, refreshToken: string, profile: any, done: (error: any, user?: any) => void): Promise<void> => {
    try {
      let user = await findUserByGoogleId(profile.id);
      if (!user) {
        user = await createUserFromGoogleProfile(profile);
      }
      return done(null, user);
    } catch (error) {
      return done(error);
    }
  }
));
```

### 5.3 OAuth 路由

```ts
app.get('/auth/google', passport.authenticate('google', { scope: ['profile', 'email'] }));

app.get('/auth/google/callback',
  passport.authenticate('google', { failureRedirect: '/login' }),
  (req: Request, res: Response): void => {
    res.redirect('/');
  }
);
```

## 6. 最佳实践

### 6.1 策略组织

- 将策略配置分离到单独文件
- 使用策略工厂模式
- 统一错误处理
- 实现策略测试

### 6.2 安全考虑

- 验证所有输入
- 使用 HTTPS
- 保护密钥和令牌
- 实现安全退出

## 7. 注意事项

- **策略选择**：根据需求选择合适的策略
- **错误处理**：实现完善的错误处理
- **会话管理**：合理管理会话
- **安全配置**：配置安全选项

## 8. 常见问题

### 8.1 如何自定义策略？

实现 Strategy 接口，定义验证逻辑。

### 8.2 如何处理多种认证方式？

使用多个策略，根据路由选择策略。

### 8.3 如何实现记住我功能？

使用长期有效的令牌或会话。

## 9. 实践任务

1. **配置 Passport**：配置 Passport.js
2. **本地策略**：实现本地认证策略
3. **JWT 策略**：实现 JWT 认证策略
4. **OAuth 策略**：实现 OAuth 认证策略
5. **路由保护**：使用 Passport 保护路由

---

**下一章**：[6.2 授权（Authorization）](../chapter-02-authorization/readme.md)
