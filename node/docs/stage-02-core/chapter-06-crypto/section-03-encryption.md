# 2.6.3 加密与解密

## 1. 概述

加密与解密是保护数据安全的重要手段。Node.js 的 crypto 模块支持对称加密（如 AES）和非对称加密（如 RSA）。理解加密与解密的原理和使用方法对于构建安全的 Node.js 应用至关重要。

## 2. 特性说明

- **对称加密**：加密和解密使用相同密钥，速度快，适合大量数据。
- **非对称加密**：使用公钥加密、私钥解密，更安全，适合密钥交换。
- **多种算法**：支持 AES、RSA、ECDSA 等多种加密算法。
- **初始化向量**：对称加密使用 IV（初始化向量）提高安全性。
- **密钥管理**：支持密钥生成、导入、导出等操作。

## 3. 语法与定义

### 对称加密

```ts
// 创建加密对象
crypto.createCipheriv(algorithm: string, key: Buffer, iv: Buffer): Cipher

// 创建解密对象
crypto.createDecipheriv(algorithm: string, key: Buffer, iv: Buffer): Decipher
```

### 非对称加密

```ts
// 公钥加密
crypto.publicEncrypt(key: string | Buffer, buffer: Buffer): Buffer

// 私钥解密
crypto.privateDecrypt(key: string | Buffer, buffer: Buffer): Buffer
```

## 4. 基本用法

### 示例 1：对称加密（AES）

```ts
// 文件: crypto-encrypt-aes.ts
// 功能: AES 对称加密

import crypto from 'node:crypto';

function encryptAES(data: string, password: string): { encrypted: string; iv: string } {
    // 生成密钥和 IV
    const key = crypto.scryptSync(password, 'salt', 32);
    const iv = crypto.randomBytes(16);
    
    // 创建加密对象
    const cipher = crypto.createCipheriv('aes-256-cbc', key, iv);
    
    // 加密数据
    let encrypted = cipher.update(data, 'utf8', 'hex');
    encrypted += cipher.final('hex');
    
    return {
        encrypted,
        iv: iv.toString('hex')
    };
}

function decryptAES(encrypted: string, password: string, ivHex: string): string {
    const key = crypto.scryptSync(password, 'salt', 32);
    const iv = Buffer.from(ivHex, 'hex');
    
    // 创建解密对象
    const decipher = crypto.createDecipheriv('aes-256-cbc', key, iv);
    
    // 解密数据
    let decrypted = decipher.update(encrypted, 'hex', 'utf8');
    decrypted += decipher.final('utf8');
    
    return decrypted;
}

// 使用
const data = 'Sensitive data';
const password = 'my-password';
const { encrypted, iv } = encryptAES(data, password);
console.log('Encrypted:', encrypted);

const decrypted = decryptAES(encrypted, password, iv);
console.log('Decrypted:', decrypted);
```

### 示例 2：非对称加密（RSA）

```ts
// 文件: crypto-encrypt-rsa.ts
// 功能: RSA 非对称加密

import crypto from 'node:crypto';
import fsPromises from 'node:fs/promises';

async function generateRSAKeys() {
    const { publicKey, privateKey } = crypto.generateKeyPairSync('rsa', {
        modulusLength: 2048,
        publicKeyEncoding: { type: 'spki', format: 'pem' },
        privateKeyEncoding: { type: 'pkcs8', format: 'pem' }
    });
    
    return { publicKey, privateKey };
}

function encryptRSA(data: string, publicKey: string): string {
    const buffer = Buffer.from(data, 'utf8');
    const encrypted = crypto.publicEncrypt(publicKey, buffer);
    return encrypted.toString('base64');
}

function decryptRSA(encrypted: string, privateKey: string): string {
    const buffer = Buffer.from(encrypted, 'base64');
    const decrypted = crypto.privateDecrypt(privateKey, buffer);
    return decrypted.toString('utf8');
}

// 使用
async function example() {
    const { publicKey, privateKey } = await generateRSAKeys();
    
    const data = 'Sensitive data';
    const encrypted = encryptRSA(data, publicKey);
    console.log('Encrypted:', encrypted);
    
    const decrypted = decryptRSA(encrypted, privateKey);
    console.log('Decrypted:', decrypted);
}

example();
```

## 5. 参数说明：加密方法参数

### createCipheriv 参数

| 参数名       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **algorithm**| String   | 加密算法                                 | `'aes-256-cbc'`                |
| **key**      | Buffer   | 加密密钥                                 | `Buffer.from('key')`            |
| **iv**       | Buffer   | 初始化向量                               | `crypto.randomBytes(16)`        |

### publicEncrypt/privateDecrypt 参数

| 参数名       | 类型           | 说明                                     | 示例                           |
|:-------------|:---------------|:-----------------------------------------|:-------------------------------|
| **key**      | String/Buffer  | 公钥或私钥（PEM 格式）                   | `'-----BEGIN PUBLIC KEY-----...'`|
| **buffer**   | Buffer         | 要加密/解密的数据                        | `Buffer.from('data')`           |

## 6. 返回值与状态说明

加密操作的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **加密**     | Buffer/String| 返回加密后的数据                         |
| **解密**     | Buffer/String| 返回解密后的数据                         |
| **密钥生成** | Object       | 返回包含公钥和私钥的对象                 |

## 7. 代码示例：完整的加密工具类

以下示例演示了如何构建完整的加密工具类：

```ts
// 文件: crypto-encrypt-complete.ts
// 功能: 完整的加密工具类

import crypto from 'node:crypto';

class EncryptionService {
    private algorithm = 'aes-256-cbc';
    
    encrypt(data: string, password: string): { encrypted: string; iv: string; salt: string } {
        // 生成盐值和密钥
        const salt = crypto.randomBytes(16);
        const key = crypto.scryptSync(password, salt, 32);
        const iv = crypto.randomBytes(16);
        
        // 加密
        const cipher = crypto.createCipheriv(this.algorithm, key, iv);
        let encrypted = cipher.update(data, 'utf8', 'hex');
        encrypted += cipher.final('hex');
        
        return {
            encrypted,
            iv: iv.toString('hex'),
            salt: salt.toString('hex')
        };
    }
    
    decrypt(encrypted: string, password: string, ivHex: string, saltHex: string): string {
        const salt = Buffer.from(saltHex, 'hex');
        const key = crypto.scryptSync(password, salt, 32);
        const iv = Buffer.from(ivHex, 'hex');
        
        const decipher = crypto.createDecipheriv(this.algorithm, key, iv);
        let decrypted = decipher.update(encrypted, 'hex', 'utf8');
        decrypted += decipher.final('utf8');
        
        return decrypted;
    }
}

// 使用
const service = new EncryptionService();
const data = 'Sensitive information';
const password = 'my-secret-password';

const { encrypted, iv, salt } = service.encrypt(data, password);
console.log('Encrypted:', encrypted);

const decrypted = service.decrypt(encrypted, password, iv, salt);
console.log('Decrypted:', decrypted);
```

## 8. 输出结果说明

加密操作的输出结果：

```text
Encrypted: a1b2c3d4e5f6...
IV: 1a2b3c4d5e6f...
Salt: x1y2z3w4v5u6...
Decrypted: Sensitive information
```

**逻辑解析**：
- 加密：使用密钥和 IV 加密数据，返回加密后的数据和 IV
- 解密：使用相同的密钥和 IV 解密数据
- 盐值：用于从密码派生密钥，提高安全性

## 9. 使用场景

### 1. 数据加密存储

加密存储敏感数据：

```ts
// 数据加密存储示例
class SecureStorage {
    private encryptionService: EncryptionService;
    
    async store(key: string, value: string, password: string) {
        const { encrypted, iv, salt } = this.encryptionService.encrypt(value, password);
        // 存储 encrypted, iv, salt
    }
    
    async retrieve(key: string, password: string): Promise<string> {
        // 读取 encrypted, iv, salt
        return this.encryptionService.decrypt(encrypted, password, iv, salt);
    }
}
```

### 2. 通信加密

加密通信数据：

```ts
// 通信加密示例
function encryptMessage(message: string, recipientPublicKey: string): string {
    return encryptRSA(message, recipientPublicKey);
}
```

### 3. 配置文件加密

加密配置文件中的敏感信息：

```ts
// 配置文件加密示例
async function encryptConfig(config: any, password: string) {
    const json = JSON.stringify(config);
    return encryptionService.encrypt(json, password);
}
```

## 10. 注意事项与常见错误

- **密钥安全**：密钥必须安全存储，不要硬编码
- **IV 使用**：每次加密使用不同的 IV，不要重复使用
- **算法选择**：使用安全的加密算法（AES-256、RSA-2048+）
- **密钥长度**：确保密钥长度符合算法要求
- **错误处理**：处理加密解密过程中的错误

## 11. 常见问题 (FAQ)

**Q: 对称加密和非对称加密如何选择？**
A: 对称加密速度快，适合大量数据；非对称加密更安全，适合密钥交换和小数据。

**Q: 如何安全地存储密钥？**
A: 使用环境变量、密钥管理服务或加密的配置文件。

**Q: IV 可以重复使用吗？**
A: 不可以，每次加密都应使用不同的 IV，提高安全性。

## 12. 最佳实践

- **算法选择**：使用 AES-256（对称）或 RSA-2048+（非对称）
- **IV 管理**：每次加密使用随机 IV，与加密数据一起存储
- **密钥派生**：使用 scrypt 或 pbkdf2 从密码派生密钥
- **错误处理**：完善的错误处理和日志记录
- **性能优化**：大量数据使用对称加密，小数据使用非对称加密

## 13. 对比分析：对称 vs 非对称加密

| 维度             | 对称加密（AES）                          | 非对称加密（RSA）                        |
|:-----------------|:------------------------------------------|:------------------------------------------|
| **密钥数量**     | 1 个（共享密钥）                          | 2 个（公钥和私钥）                        |
| **速度**         | 快                                        | 慢                                        |
| **安全性**       | 高（密钥安全的前提下）                    | 高                                        |
| **适用场景**     | 大量数据加密                              | 密钥交换、数字签名、小数据加密            |
| **密钥管理**     | 需要安全共享密钥                          | 公钥可以公开，私钥保密                    |

## 14. 练习任务

1. **对称加密实践**：
   - 使用 AES 加密和解密数据
   - 理解 IV 的作用
   - 实现密钥派生

2. **非对称加密实践**：
   - 生成 RSA 密钥对
   - 使用公钥加密、私钥解密
   - 理解非对称加密的原理

3. **实际应用**：
   - 实现数据加密存储功能
   - 实现通信加密功能
   - 实现配置文件加密功能

完成以上练习后，继续学习下一节：数字签名。

## 总结

加密与解密是保护数据安全的重要手段：

- **对称加密**：AES，速度快，适合大量数据
- **非对称加密**：RSA，更安全，适合密钥交换
- **IV 使用**：每次加密使用不同的 IV
- **最佳实践**：算法选择、密钥管理、错误处理

掌握加密与解密有助于构建安全的 Node.js 应用。

---

**最后更新**：2025-01-XX
