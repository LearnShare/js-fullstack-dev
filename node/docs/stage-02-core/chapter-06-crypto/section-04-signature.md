# 2.6.4 数字签名

## 1. 概述

数字签名用于验证数据的完整性和来源。通过使用私钥签名、公钥验证的方式，可以确保数据未被篡改且来自可信来源。数字签名在 API 认证、数据完整性验证、软件分发等场景中广泛应用。

## 2. 特性说明

- **数据完整性**：验证数据是否被篡改。
- **身份认证**：验证数据来源的身份。
- **不可否认性**：签名者无法否认已签名的数据。
- **非对称加密**：使用私钥签名、公钥验证。
- **多种算法**：支持 RSA、ECDSA 等多种签名算法。

## 3. 语法与定义

### 创建签名对象

```ts
// 创建签名对象
crypto.createSign(algorithm: string): Sign

// 创建验证对象
crypto.createVerify(algorithm: string): Verify
```

### 签名和验证

```ts
// 签名数据
sign.update(data: string | Buffer): Sign
sign.sign(privateKey: string | Buffer, encoding?: string): string | Buffer

// 验证签名
verify.update(data: string | Buffer): Verify
verify.verify(publicKey: string | Buffer, signature: string | Buffer, encoding?: string): boolean
```

## 4. 基本用法

### 示例 1：基本数字签名

```ts
// 文件: crypto-signature-basic.ts
// 功能: 基本数字签名

import crypto from 'node:crypto';

// 生成密钥对
const { publicKey, privateKey } = crypto.generateKeyPairSync('rsa', {
    modulusLength: 2048,
    publicKeyEncoding: { type: 'spki', format: 'pem' },
    privateKeyEncoding: { type: 'pkcs8', format: 'pem' }
});

// 签名数据
function signData(data: string, privateKey: string): string {
    const sign = crypto.createSign('RSA-SHA256');
    sign.update(data);
    return sign.sign(privateKey, 'hex');
}

// 验证签名
function verifySignature(data: string, signature: string, publicKey: string): boolean {
    const verify = crypto.createVerify('RSA-SHA256');
    verify.update(data);
    return verify.verify(publicKey, signature, 'hex');
}

// 使用
const data = 'Important message';
const signature = signData(data, privateKey);
console.log('Signature:', signature);

const isValid = verifySignature(data, signature, publicKey);
console.log('Signature valid:', isValid);
```

### 示例 2：HMAC 签名（对称签名）

```ts
// 文件: crypto-signature-hmac.ts
// 功能: HMAC 签名

import crypto from 'node:crypto';

function signHMAC(data: string, secret: string): string {
    return crypto
        .createHmac('sha256', secret)
        .update(data)
        .digest('hex');
}

function verifyHMAC(data: string, signature: string, secret: string): boolean {
    const computed = signHMAC(data, secret);
    return crypto.timingSafeEqual(
        Buffer.from(computed),
        Buffer.from(signature)
    );
}

// 使用
const data = 'API request data';
const secret = 'api-secret-key';
const signature = signHMAC(data, secret);
console.log('HMAC Signature:', signature);

const isValid = verifyHMAC(data, signature, secret);
console.log('Signature valid:', isValid);
```

## 5. 参数说明：签名方法参数

### createSign/createVerify 参数

| 参数名       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **algorithm**| String   | 签名算法                                 | `'RSA-SHA256'`, `'ECDSA-SHA256'`|

### sign 方法参数

| 参数名       | 类型           | 说明                                     | 示例                           |
|:-------------|:---------------|:-----------------------------------------|:-------------------------------|
| **privateKey**| String/Buffer  | 私钥（PEM 格式）                         | `'-----BEGIN PRIVATE KEY-----...'`|
| **encoding** | String         | 输出编码格式                             | `'hex'`, `'base64'`            |

### verify 方法参数

| 参数名       | 类型           | 说明                                     | 示例                           |
|:-------------|:---------------|:-----------------------------------------|:-------------------------------|
| **publicKey**| String/Buffer  | 公钥（PEM 格式）                         | `'-----BEGIN PUBLIC KEY-----...'`|
| **signature**| String/Buffer  | 要验证的签名                             | `'a1b2c3d4...'`                |
| **encoding** | String         | 签名编码格式                             | `'hex'`, `'base64'`            |

## 6. 返回值与状态说明

签名操作的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **签名**     | String/Buffer| 返回数字签名                             |
| **验证**     | Boolean      | 返回签名是否有效                         |

## 7. 代码示例：API 请求签名

以下示例演示了如何使用数字签名进行 API 请求认证：

```ts
// 文件: crypto-signature-api.ts
// 功能: API 请求签名

import crypto from 'node:crypto';

class APISigner {
    private privateKey: string;
    private publicKey: string;
    
    constructor() {
        const { publicKey, privateKey } = crypto.generateKeyPairSync('rsa', {
            modulusLength: 2048,
            publicKeyEncoding: { type: 'spki', format: 'pem' },
            privateKeyEncoding: { type: 'pkcs8', format: 'pem' }
        });
        this.privateKey = privateKey;
        this.publicKey = publicKey;
    }
    
    signRequest(method: string, path: string, body: string, timestamp: number): string {
        const data = `${method}${path}${body}${timestamp}`;
        const sign = crypto.createSign('RSA-SHA256');
        sign.update(data);
        return sign.sign(this.privateKey, 'base64');
    }
    
    verifyRequest(method: string, path: string, body: string, timestamp: number, signature: string): boolean {
        const data = `${method}${path}${body}${timestamp}`;
        const verify = crypto.createVerify('RSA-SHA256');
        verify.update(data);
        return verify.verify(this.publicKey, signature, 'base64');
    }
    
    getPublicKey(): string {
        return this.publicKey;
    }
}

// 使用
const signer = new APISigner();

// 客户端：签名请求
const method = 'POST';
const path = '/api/users';
const body = JSON.stringify({ name: 'Alice' });
const timestamp = Date.now();
const signature = signer.signRequest(method, path, body, timestamp);

// 服务端：验证签名
const isValid = signer.verifyRequest(method, path, body, timestamp, signature);
console.log('Request valid:', isValid);
```

## 8. 输出结果说明

数字签名的输出结果：

```text
Signature: a1b2c3d4e5f6...
Signature valid: true
Request valid: true
```

**逻辑解析**：
- 使用私钥对数据进行签名
- 使用公钥验证签名
- 签名验证通过说明数据未被篡改且来源可信

## 9. 使用场景

### 1. API 认证

实现 API 请求签名认证：

```ts
// API 认证示例
function authenticateRequest(req: any, publicKey: string): boolean {
    const data = `${req.method}${req.path}${req.body}${req.timestamp}`;
    return verifySignature(data, req.signature, publicKey);
}
```

### 2. 数据完整性验证

验证数据完整性：

```ts
// 数据完整性验证示例
function verifyDataIntegrity(data: string, signature: string, publicKey: string): boolean {
    return verifySignature(data, signature, publicKey);
}
```

### 3. 软件分发

验证软件包的完整性：

```ts
// 软件分发验证示例
async function verifyPackage(packagePath: string, signature: string, publicKey: string): Promise<boolean> {
    const packageData = await fsPromises.readFile(packagePath);
    return verifySignature(packageData.toString(), signature, publicKey);
}
```

## 10. 注意事项与常见错误

- **密钥安全**：私钥必须严格保密，公钥可以公开
- **算法选择**：使用安全的签名算法（RSA-SHA256、ECDSA-SHA256）
- **时间戳**：API 签名时使用时间戳，防止重放攻击
- **数据格式**：确保签名和验证使用相同的数据格式
- **错误处理**：处理签名验证失败的情况

## 11. 常见问题 (FAQ)

**Q: 数字签名和加密有什么区别？**
A: 数字签名用于验证数据完整性和来源，不加密数据；加密用于保护数据内容。

**Q: 如何防止签名重放攻击？**
A: 在签名数据中包含时间戳或随机数（nonce），验证时检查时间戳和 nonce。

**Q: HMAC 和数字签名有什么区别？**
A: HMAC 是对称的，需要共享密钥；数字签名是非对称的，使用公钥/私钥对。

## 12. 最佳实践

- **算法选择**：使用 RSA-SHA256 或 ECDSA-SHA256
- **密钥管理**：安全地存储和管理私钥
- **时间戳**：API 签名时包含时间戳，防止重放攻击
- **错误处理**：完善的错误处理和日志记录
- **性能优化**：大量数据使用 HMAC，小数据使用数字签名

## 13. 对比分析：数字签名 vs HMAC

| 维度             | 数字签名（RSA/ECDSA）                    | HMAC                                    |
|:-----------------|:------------------------------------------|:----------------------------------------|
| **密钥类型**     | 非对称（公钥/私钥）                      | 对称（共享密钥）                        |
| **安全性**       | 高（公钥可以公开）                        | 高（需要共享密钥）                      |
| **性能**         | 较慢                                      | 快                                      |
| **适用场景**     | API 认证、软件分发                        | API 认证、内部通信                      |
| **密钥管理**     | 公钥可以公开，私钥保密                    | 需要安全共享密钥                        |

## 14. 练习任务

1. **数字签名实践**：
   - 生成 RSA 密钥对
   - 使用私钥签名数据
   - 使用公钥验证签名

2. **HMAC 签名实践**：
   - 使用 HMAC 签名数据
   - 验证 HMAC 签名
   - 理解 HMAC 的优势

3. **API 认证实践**：
   - 实现 API 请求签名
   - 实现签名验证
   - 防止重放攻击

4. **实际应用**：
   - 在实际项目中应用数字签名
   - 实现 API 认证功能
   - 实现数据完整性验证

完成以上练习后，继续学习下一章：Buffer 与 Stream。

## 总结

数字签名是验证数据完整性和来源的重要手段：

- **核心功能**：使用私钥签名、公钥验证
- **算法选择**：使用 RSA-SHA256 或 ECDSA-SHA256
- **应用场景**：API 认证、数据完整性验证、软件分发
- **最佳实践**：密钥管理、时间戳、错误处理

掌握数字签名有助于构建安全的 Node.js 应用。

---

**最后更新**：2025-01-XX
