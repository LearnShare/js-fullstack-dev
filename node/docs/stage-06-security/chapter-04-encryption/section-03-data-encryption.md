# 6.4.3 数据加密

## 1. 概述

数据加密用于保护存储的敏感数据，使用对称加密算法（如 AES）对数据进行加密和解密。数据加密确保即使数据泄露，攻击者也无法直接读取数据。

## 2. Node.js 实现

### 2.1 使用 crypto 模块

```ts
import { createCipheriv, createDecipheriv, randomBytes, scrypt } from 'node:crypto';
import { promisify } from 'node:util';

const scryptAsync = promisify(scrypt);

interface EncryptionResult {
  iv: string;
  encrypted: string;
}

async function encryptData(data: string, password: string): Promise<EncryptionResult> {
  const salt = randomBytes(16);
  const key = (await scryptAsync(password, salt, 32)) as Buffer;
  const iv = randomBytes(16);
  
  const cipher = createCipheriv('aes-256-cbc', key, iv);
  let encrypted = cipher.update(data, 'utf8', 'hex');
  encrypted += cipher.final('hex');
  
  return {
    iv: iv.toString('hex'),
    encrypted: encrypted
  };
}

async function decryptData(encryptedData: EncryptionResult, password: string, salt: Buffer): Promise<string> {
  const key = (await scryptAsync(password, salt, 32)) as Buffer;
  const iv = Buffer.from(encryptedData.iv, 'hex');
  
  const decipher = createDecipheriv('aes-256-cbc', key, iv);
  let decrypted = decipher.update(encryptedData.encrypted, 'hex', 'utf8');
  decrypted += decipher.final('utf8');
  
  return decrypted;
}
```

### 2.2 使用环境变量密钥

```ts
const ENCRYPTION_KEY = process.env.ENCRYPTION_KEY!;
const ALGORITHM = 'aes-256-gcm';

function encrypt(data: string): { encrypted: string; iv: string; authTag: string } {
  const iv = randomBytes(16);
  const key = Buffer.from(ENCRYPTION_KEY, 'hex');
  
  const cipher = createCipheriv(ALGORITHM, key, iv);
  let encrypted = cipher.update(data, 'utf8', 'hex');
  encrypted += cipher.final('hex');
  
  const authTag = cipher.getAuthTag();
  
  return {
    encrypted,
    iv: iv.toString('hex'),
    authTag: authTag.toString('hex')
  };
}

function decrypt(encryptedData: { encrypted: string; iv: string; authTag: string }): string {
  const key = Buffer.from(ENCRYPTION_KEY, 'hex');
  const iv = Buffer.from(encryptedData.iv, 'hex');
  const authTag = Buffer.from(encryptedData.authTag, 'hex');
  
  const decipher = createDecipheriv(ALGORITHM, key, iv);
  decipher.setAuthTag(authTag);
  
  let decrypted = decipher.update(encryptedData.encrypted, 'hex', 'utf8');
  decrypted += decipher.final('utf8');
  
  return decrypted;
}
```

## 3. 数据库字段加密

### 3.1 加密敏感字段

```ts
interface User {
  id: number;
  email: string;
  ssn: string; // 需要加密
}

async function createUser(email: string, ssn: string): Promise<void> {
  const encryptedSSN = encrypt(ssn);
  
  await db.query(
    'INSERT INTO users (email, ssn_encrypted, ssn_iv, ssn_auth_tag) VALUES ($1, $2, $3, $4)',
    [email, encryptedSSN.encrypted, encryptedSSN.iv, encryptedSSN.authTag]
  );
}

async function getUserSSN(userId: number): Promise<string> {
  const user = await db.query(
    'SELECT ssn_encrypted, ssn_iv, ssn_auth_tag FROM users WHERE id = $1',
    [userId]
  );
  
  if (user.length === 0) {
    throw new Error('User not found');
  }
  
  return decrypt({
    encrypted: user[0].ssn_encrypted,
    iv: user[0].ssn_iv,
    authTag: user[0].ssn_auth_tag
  });
}
```

## 4. 文件加密

### 4.1 加密文件

```ts
import { createReadStream, createWriteStream } from 'node:fs';
import { pipeline } from 'node:stream/promises';

async function encryptFile(inputPath: string, outputPath: string, password: string): Promise<void> {
  const salt = randomBytes(16);
  const key = (await scryptAsync(password, salt, 32)) as Buffer;
  const iv = randomBytes(16);
  
  const cipher = createCipheriv('aes-256-cbc', key, iv);
  const input = createReadStream(inputPath);
  const output = createWriteStream(outputPath);
  
  // 写入 salt 和 iv
  output.write(salt);
  output.write(iv);
  
  await pipeline(input, cipher, output);
}

async function decryptFile(inputPath: string, outputPath: string, password: string): Promise<void> {
  const input = createReadStream(inputPath);
  const salt = Buffer.alloc(16);
  const iv = Buffer.alloc(16);
  
  await new Promise<void>((resolve, reject) => {
    input.once('readable', () => {
      input.read(16).copy(salt);
      input.read(16).copy(iv);
      resolve();
    });
    input.once('error', reject);
  });
  
  const key = (await scryptAsync(password, salt, 32)) as Buffer;
  const decipher = createDecipheriv('aes-256-cbc', key, iv);
  const output = createWriteStream(outputPath);
  
  await pipeline(input, decipher, output);
}
```

## 5. 最佳实践

### 5.1 密钥管理

- 使用环境变量
- 密钥轮换
- 密钥分离
- 密钥备份

### 5.2 安全考虑

- 使用强算法
- 随机 IV
- 认证加密（GCM）
- 密钥保护

## 6. 注意事项

- **密钥安全**：保护加密密钥
- **IV 随机性**：每次加密使用随机 IV
- **性能影响**：考虑加密性能
- **数据备份**：加密数据备份

## 7. 常见问题

### 7.1 如何管理加密密钥？

使用密钥管理服务，实现密钥轮换。

### 7.2 如何处理密钥轮换？

逐步迁移数据，使用新密钥加密新数据。

### 7.3 如何选择加密算法？

使用 AES-256-GCM，提供认证加密。

## 8. 实践任务

1. **数据加密**：实现数据加密功能
2. **数据解密**：实现数据解密功能
3. **字段加密**：实现数据库字段加密
4. **文件加密**：实现文件加密功能
5. **密钥管理**：实现密钥管理功能

---

**下一节**：[6.4.4 HTTPS/TLS](section-04-https-tls.md)
