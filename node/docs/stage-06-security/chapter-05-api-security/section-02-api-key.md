# 6.5.2 API Key 管理

## 1. 概述

API Key 是用于识别和认证 API 客户端的密钥。API Key 管理包括生成、存储、验证和撤销等操作。

## 2. API Key 生成

### 2.1 生成方法

```ts
import { randomBytes } from 'node:crypto';

function generateAPIKey(): string {
  return randomBytes(32).toString('hex');
}

function generateAPIKeyWithPrefix(prefix: string = 'sk'): string {
  const key = randomBytes(32).toString('hex');
  return `${prefix}_${key}`;
}

// 使用
const apiKey = generateAPIKeyWithPrefix('sk');
console.log('API Key:', apiKey);
```

### 2.2 哈希存储

```ts
import { createHash } from 'node:crypto';

function hashAPIKey(apiKey: string): string {
  return createHash('sha256').update(apiKey).digest('hex');
}

// 存储哈希值
async function storeAPIKey(userId: number, apiKey: string): Promise<void> {
  const hashedKey = hashAPIKey(apiKey);
  await db.query(
    'INSERT INTO api_keys (user_id, key_hash, created_at) VALUES ($1, $2, NOW())',
    [userId, hashedKey]
  );
}
```

## 3. API Key 验证

### 3.1 验证中间件

```ts
import { Request, Response, NextFunction } from 'express';

async function validateAPIKey(req: Request, res: Response, next: NextFunction): Promise<void> {
  const apiKey = req.headers['x-api-key'] as string;
  
  if (!apiKey) {
    res.status(401).json({ message: 'API Key required' });
    return;
  }
  
  const hashedKey = hashAPIKey(apiKey);
  const keyRecord = await db.query(
    'SELECT * FROM api_keys WHERE key_hash = $1 AND revoked = false',
    [hashedKey]
  );
  
  if (keyRecord.length === 0) {
    res.status(401).json({ message: 'Invalid API Key' });
    return;
  }
  
  (req as any).apiKey = keyRecord[0];
  next();
}

// 使用
app.use('/api', validateAPIKey);
```

### 3.2 密钥信息查询

```ts
async function getAPIKeyInfo(apiKey: string): Promise<any> {
  const hashedKey = hashAPIKey(apiKey);
  const result = await db.query(
    `SELECT ak.*, u.username 
     FROM api_keys ak 
     JOIN users u ON ak.user_id = u.id 
     WHERE ak.key_hash = $1 AND ak.revoked = false`,
    [hashedKey]
  );
  
  return result[0] || null;
}
```

## 4. API Key 管理

### 4.1 撤销密钥

```ts
async function revokeAPIKey(apiKey: string): Promise<void> {
  const hashedKey = hashAPIKey(apiKey);
  await db.query(
    'UPDATE api_keys SET revoked = true, revoked_at = NOW() WHERE key_hash = $1',
    [hashedKey]
  );
}
```

### 4.2 密钥过期

```ts
async function checkAPIKeyExpiry(apiKey: string): Promise<boolean> {
  const hashedKey = hashAPIKey(apiKey);
  const result = await db.query(
    'SELECT expires_at FROM api_keys WHERE key_hash = $1',
    [hashedKey]
  );
  
  if (result.length === 0) {
    return false;
  }
  
  const expiresAt = result[0].expires_at;
  if (expiresAt && new Date(expiresAt) < new Date()) {
    return false;
  }
  
  return true;
}
```

### 4.3 使用统计

```ts
async function recordAPIKeyUsage(apiKey: string, endpoint: string): Promise<void> {
  const hashedKey = hashAPIKey(apiKey);
  await db.query(
    'INSERT INTO api_key_usage (key_hash, endpoint, accessed_at) VALUES ($1, $2, NOW())',
    [hashedKey, endpoint]
  );
}

async function getAPIKeyUsage(apiKey: string, days: number = 30): Promise<any[]> {
  const hashedKey = hashAPIKey(apiKey);
  return await db.query(
    `SELECT endpoint, COUNT(*) as count 
     FROM api_key_usage 
     WHERE key_hash = $1 AND accessed_at > NOW() - INTERVAL '${days} days'
     GROUP BY endpoint`,
    [hashedKey]
  );
}
```

## 5. 最佳实践

### 5.1 密钥设计

- 使用强随机密钥
- 哈希存储密钥
- 设置密钥过期
- 支持密钥撤销

### 5.2 安全考虑

- 使用 HTTPS 传输
- 限制密钥权限
- 监控密钥使用
- 实现密钥轮换

## 6. 注意事项

- **密钥存储**：哈希存储，不存储明文
- **传输安全**：使用 HTTPS
- **权限控制**：限制密钥权限
- **监控告警**：监控异常使用

## 7. 常见问题

### 7.1 如何安全存储 API Key？

哈希存储，使用环境变量或密钥管理服务。

### 7.2 如何处理密钥泄露？

立即撤销泄露的密钥，生成新密钥。

### 7.3 如何实现密钥轮换？

定期生成新密钥，逐步迁移客户端。

## 8. 实践任务

1. **生成密钥**：实现 API Key 生成
2. **验证密钥**：实现 API Key 验证
3. **密钥管理**：实现密钥管理功能
4. **使用统计**：实现使用统计
5. **安全加固**：加固 API Key 安全

---

**下一节**：[6.5.3 API 签名验证](section-03-signature.md)
