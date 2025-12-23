# 6.1.4 OAuth 2.0 与 OIDC

## 1. 概述

OAuth 2.0 是一个授权框架，允许第三方应用访问用户资源。OIDC（OpenID Connect）是基于 OAuth 2.0 的身份认证协议。OAuth 2.0 和 OIDC 广泛用于第三方登录和 API 授权。

## 2. OAuth 2.0 流程

### 2.1 授权码流程

```
1. 用户访问应用
2. 应用重定向到授权服务器
3. 用户登录并授权
4. 授权服务器返回授权码
5. 应用使用授权码换取访问令牌
6. 应用使用访问令牌访问资源
```

### 2.2 角色说明

- **资源所有者（Resource Owner）**：用户
- **客户端（Client）**：应用
- **授权服务器（Authorization Server）**：提供授权
- **资源服务器（Resource Server）**：提供资源

## 3. Node.js 实现

### 3.1 安装依赖

```bash
npm install oauth2-server
npm install @types/oauth2-server -D
```

### 3.2 授权服务器

```ts
import { Request, Response } from 'express';
import { OAuth2Server, Request as OAuthRequest, Response as OAuthResponse } from 'oauth2-server';

const oauth = new OAuth2Server({
  model: {
    // 获取客户端
    async getClient(clientId: string, clientSecret: string | null): Promise<any> {
      return await db.query('SELECT * FROM oauth_clients WHERE client_id = $1', [clientId]);
    },
    
    // 获取访问令牌
    async getAccessToken(token: string): Promise<any> {
      return await db.query('SELECT * FROM oauth_access_tokens WHERE token = $1', [token]);
    },
    
    // 保存访问令牌
    async saveToken(token: any, client: any, user: any): Promise<any> {
      await db.query(
        'INSERT INTO oauth_access_tokens (token, client_id, user_id, expires_at) VALUES ($1, $2, $3, $4)',
        [token.accessToken, client.id, user.id, token.accessTokenExpiresAt]
      );
      return token;
    },
    
    // 获取授权码
    async getAuthorizationCode(code: string): Promise<any> {
      return await db.query('SELECT * FROM oauth_authorization_codes WHERE code = $1', [code]);
    },
    
    // 保存授权码
    async saveAuthorizationCode(code: any, client: any, user: any): Promise<any> {
      await db.query(
        'INSERT INTO oauth_authorization_codes (code, client_id, user_id, expires_at) VALUES ($1, $2, $3, $4)',
        [code.authorizationCode, client.id, user.id, code.expiresAt]
      );
      return code;
    }
  }
});

// 授权端点
app.get('/oauth/authorize', async (req: Request, res: Response): Promise<void> => {
  const request = new OAuthRequest(req);
  const response = new OAuthResponse(res);
  
  try {
    const code = await oauth.authorize(request, response);
    res.json({ code: code.authorizationCode });
  } catch (error) {
    res.status(500).json({ error: 'Authorization failed' });
  }
});

// 令牌端点
app.post('/oauth/token', async (req: Request, res: Response): Promise<void> => {
  const request = new OAuthRequest(req);
  const response = new OAuthResponse(res);
  
  try {
    const token = await oauth.token(request, response);
    res.json({ access_token: token.accessToken, refresh_token: token.refreshToken });
  } catch (error) {
    res.status(500).json({ error: 'Token generation failed' });
  }
});
```

### 3.3 资源保护

```ts
async function authenticate(req: Request, res: Response, next: NextFunction): Promise<void> {
  const request = new OAuthRequest(req);
  const response = new OAuthResponse(res);
  
  try {
    const token = await oauth.authenticate(request, response);
    (req as any).user = token.user;
    next();
  } catch (error) {
    res.status(401).json({ error: 'Unauthorized' });
  }
}

app.get('/api/user', authenticate, (req: Request, res: Response): void => {
  res.json({ user: (req as any).user });
});
```

## 4. OIDC 实现

### 4.1 安装依赖

```bash
npm install openid-client
```

### 4.2 客户端配置

```ts
import { Issuer, Client } from 'openid-client';

async function setupOIDCClient(): Promise<Client> {
  const issuer = await Issuer.discover('https://accounts.google.com');
  
  const client = new issuer.Client({
    client_id: process.env.OIDC_CLIENT_ID!,
    client_secret: process.env.OIDC_CLIENT_SECRET!,
    redirect_uris: [process.env.OIDC_REDIRECT_URI!],
    response_types: ['code']
  });
  
  return client;
}
```

### 4.3 登录流程

```ts
app.get('/login', async (req: Request, res: Response): Promise<void> => {
  const client = await setupOIDCClient();
  const authUrl = client.authorizationUrl({
    scope: 'openid email profile'
  });
  
  res.redirect(authUrl);
});

app.get('/callback', async (req: Request, res: Response): Promise<void> => {
  const client = await setupOIDCClient();
  const params = client.callbackParams(req.url);
  const tokenSet = await client.callback(process.env.OIDC_REDIRECT_URI!, params);
  
  // 获取用户信息
  const userInfo = await client.userinfo(tokenSet.access_token!);
  
  // 创建本地会话
  (req.session as any).user = userInfo;
  res.redirect('/');
});
```

## 5. 最佳实践

### 5.1 安全配置

- 使用 HTTPS
- 验证重定向 URI
- 保护客户端密钥
- 实现 PKCE

### 5.2 令牌管理

- 安全存储令牌
- 实现令牌刷新
- 处理令牌过期
- 支持令牌撤销

## 6. 注意事项

- **安全配置**：正确配置 OAuth 参数
- **令牌安全**：安全存储和传输令牌
- **重定向验证**：验证重定向 URI
- **错误处理**：实现完善的错误处理

## 7. 常见问题

### 7.1 OAuth 2.0 和 OIDC 的区别？

OAuth 2.0 是授权框架，OIDC 是基于 OAuth 2.0 的身份认证协议。

### 7.2 如何选择 OAuth 流程？

根据应用类型选择，Web 应用用授权码流程，移动应用用隐式流程。

### 7.3 如何实现 PKCE？

在授权请求中包含 code_challenge，在令牌请求中包含 code_verifier。

## 8. 实践任务

1. **配置 OAuth**：配置 OAuth 2.0 服务器
2. **实现授权**：实现授权流程
3. **资源保护**：实现资源保护
4. **OIDC 集成**：集成 OIDC 客户端
5. **安全配置**：配置安全选项

---

**下一节**：[6.1.5 Passport.js](section-05-passport.md)
