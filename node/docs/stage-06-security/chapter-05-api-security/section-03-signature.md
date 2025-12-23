# 6.5.3 API 签名验证

## 1. 概述

API 签名验证通过计算请求签名来验证请求的完整性和真实性。签名验证防止请求被篡改和重放攻击。

## 2. 签名算法

### 2.1 HMAC 签名

```ts
import { createHmac } from 'node:crypto';

function generateSignature(
  method: string,
  path: string,
  query: string,
  body: string,
  timestamp: string,
  secret: string
): string {
  const message = `${method}\n${path}\n${query}\n${body}\n${timestamp}`;
  const signature = createHmac('sha256', secret).update(message).digest('hex');
  return signature;
}

// 使用
const signature = generateSignature(
  'POST',
  '/api/users',
  '',
  JSON.stringify({ name: 'John' }),
  Date.now().toString(),
  'secret-key'
);
```

### 2.2 请求签名

```ts
interface SignedRequest {
  method: string;
  path: string;
  query: Record<string, string>;
  body: any;
  timestamp: string;
  signature: string;
}

function signRequest(
  method: string,
  path: string,
  query: Record<string, string>,
  body: any,
  secret: string
): SignedRequest {
  const timestamp = Date.now().toString();
  const queryString = Object.keys(query)
    .sort()
    .map((key: string) => `${key}=${query[key]}`)
    .join('&');
  const bodyString = body ? JSON.stringify(body) : '';
  
  const signature = generateSignature(method, path, queryString, bodyString, timestamp, secret);
  
  return {
    method,
    path,
    query,
    body,
    timestamp,
    signature
  };
}
```

## 3. 签名验证

### 3.1 验证中间件

```ts
import { Request, Response, NextFunction } from 'express';

async function verifySignature(req: Request, res: Response, next: NextFunction): Promise<void> {
  const signature = req.headers['x-signature'] as string;
  const timestamp = req.headers['x-timestamp'] as string;
  const apiKey = req.headers['x-api-key'] as string;
  
  if (!signature || !timestamp || !apiKey) {
    res.status(401).json({ message: 'Missing signature headers' });
    return;
  }
  
  // 检查时间戳（防止重放攻击）
  const requestTime = parseInt(timestamp);
  const now = Date.now();
  const timeDiff = Math.abs(now - requestTime);
  
  if (timeDiff > 5 * 60 * 1000) { // 5 分钟
    res.status(401).json({ message: 'Request expired' });
    return;
  }
  
  // 获取密钥
  const keyRecord = await getAPIKeyRecord(apiKey);
  if (!keyRecord) {
    res.status(401).json({ message: 'Invalid API Key' });
    return;
  }
  
  // 计算签名
  const queryString = Object.keys(req.query)
    .sort()
    .map((key: string) => `${key}=${req.query[key]}`)
    .join('&');
  const bodyString = req.body ? JSON.stringify(req.body) : '';
  
  const expectedSignature = generateSignature(
    req.method,
    req.path,
    queryString,
    bodyString,
    timestamp,
    keyRecord.secret
  );
  
  // 验证签名
  if (signature !== expectedSignature) {
    res.status(401).json({ message: 'Invalid signature' });
    return;
  }
  
  (req as any).apiKey = keyRecord;
  next();
}

// 使用
app.use('/api', verifySignature);
```

### 3.2 防止重放攻击

```ts
import Redis from 'ioredis';

const redis = new Redis();

async function checkNonce(nonce: string, timestamp: string): Promise<boolean> {
  const key = `nonce:${nonce}`;
  const exists = await redis.exists(key);
  
  if (exists) {
    return false; // 重复使用
  }
  
  // 存储 nonce，5 分钟过期
  await redis.setex(key, 300, '1');
  return true;
}

async function verifySignatureWithNonce(req: Request, res: Response, next: NextFunction): Promise<void> {
  const nonce = req.headers['x-nonce'] as string;
  
  if (!nonce) {
    res.status(401).json({ message: 'Missing nonce' });
    return;
  }
  
  const isValid = await checkNonce(nonce, req.headers['x-timestamp'] as string);
  if (!isValid) {
    res.status(401).json({ message: 'Duplicate request' });
    return;
  }
  
  // 继续验证签名
  // ...
}
```

## 4. 客户端实现

### 4.1 签名请求

```ts
import axios, { AxiosInstance } from 'axios';

class SignedAPIClient {
  private client: AxiosInstance;
  private apiKey: string;
  private secret: string;
  
  constructor(baseURL: string, apiKey: string, secret: string) {
    this.apiKey = apiKey;
    this.secret = secret;
    this.client = axios.create({ baseURL });
  }
  
  private signRequest(method: string, url: string, data?: any): { signature: string; timestamp: string; nonce: string } {
    const timestamp = Date.now().toString();
    const nonce = randomBytes(16).toString('hex');
    const path = new URL(url, this.client.defaults.baseURL).pathname;
    
    const bodyString = data ? JSON.stringify(data) : '';
    const signature = generateSignature(method, path, '', bodyString, timestamp, this.secret);
    
    return { signature, timestamp, nonce };
  }
  
  async request(method: string, url: string, data?: any): Promise<any> {
    const { signature, timestamp, nonce } = this.signRequest(method, url, data);
    
    const response = await this.client.request({
      method,
      url,
      data,
      headers: {
        'X-API-Key': this.apiKey,
        'X-Signature': signature,
        'X-Timestamp': timestamp,
        'X-Nonce': nonce
      }
    });
    
    return response.data;
  }
}

// 使用
const client = new SignedAPIClient('https://api.example.com', 'api-key', 'secret');
const result = await client.request('POST', '/api/users', { name: 'John' });
```

## 5. 最佳实践

### 5.1 签名设计

- 包含所有请求参数
- 使用时间戳
- 使用随机数
- 使用强密钥

### 5.2 安全考虑

- 验证时间戳
- 检查随机数
- 保护密钥
- 记录签名操作

## 6. 注意事项

- **时间同步**：确保服务器时间同步
- **密钥安全**：保护签名密钥
- **性能影响**：考虑签名验证性能
- **错误处理**：提供清晰的错误信息

## 7. 常见问题

### 7.1 如何处理时间差？

设置合理的时间窗口，考虑网络延迟。

### 7.2 如何存储随机数？

使用 Redis 存储，设置合理的过期时间。

### 7.3 如何优化性能？

缓存密钥信息，优化签名计算。

## 8. 实践任务

1. **生成签名**：实现请求签名生成
2. **验证签名**：实现签名验证
3. **防重放**：实现防重放攻击
4. **客户端**：实现签名客户端
5. **安全测试**：测试签名安全性

---

**下一章**：[6.6 安全审计与日志](../chapter-06-audit/readme.md)
