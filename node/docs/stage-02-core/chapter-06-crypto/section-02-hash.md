# 2.6.2 哈希算法

## 1. 概述

哈希算法是将任意长度的数据映射为固定长度哈希值的单向函数。哈希算法在密码存储、数据完整性验证、数字签名等场景中广泛应用。Node.js 的 crypto 模块提供了多种哈希算法的支持。

## 2. 特性说明

- **单向性**：哈希是单向的，无法从哈希值反推原始数据。
- **确定性**：相同输入总是产生相同输出。
- **雪崩效应**：输入微小变化会导致输出巨大变化。
- **抗碰撞性**：难以找到两个不同的输入产生相同的哈希值。
- **快速计算**：哈希计算速度快，适合大量数据。

## 3. 语法与定义

### 创建哈希对象

```ts
// 创建哈希对象
crypto.createHash(algorithm: string): Hash

// 更新哈希数据
hash.update(data: string | Buffer, encoding?: string): Hash

// 计算哈希值
hash.digest(encoding?: string): string | Buffer
```

## 4. 基本用法

### 示例 1：基本哈希计算

```ts
// 文件: crypto-hash-basic.ts
// 功能: 基本哈希计算

import crypto from 'node:crypto';

const data = 'Hello, Node.js!';

// SHA-256 哈希
const sha256 = crypto.createHash('sha256').update(data).digest('hex');
console.log('SHA-256:', sha256);

// SHA-512 哈希
const sha512 = crypto.createHash('sha512').update(data).digest('hex');
console.log('SHA-512:', sha512);

// MD5 哈希（不推荐用于安全场景）
const md5 = crypto.createHash('md5').update(data).digest('hex');
console.log('MD5:', md5);
```

### 示例 2：流式哈希计算

```ts
// 文件: crypto-hash-stream.ts
// 功能: 流式哈希计算

import crypto from 'node:crypto';
import fs from 'node:fs';

function hashFile(filePath: string): Promise<string> {
    return new Promise((resolve, reject) => {
        const hash = crypto.createHash('sha256');
        const stream = fs.createReadStream(filePath);
        
        stream.on('data', (chunk) => {
            hash.update(chunk);
        });
        
        stream.on('end', () => {
            resolve(hash.digest('hex'));
        });
        
        stream.on('error', reject);
    });
}

// 使用
hashFile('./large-file.txt')
    .then(hash => console.log('File hash:', hash))
    .catch(error => console.error('Error:', error));
```

### 示例 3：密码哈希（带盐值）

```ts
// 文件: crypto-hash-password.ts
// 功能: 密码哈希（带盐值）

import crypto from 'node:crypto';

function hashPassword(password: string, salt?: string): { hash: string; salt: string } {
    // 生成盐值（如果未提供）
    if (!salt) {
        salt = crypto.randomBytes(16).toString('hex');
    }
    
    // 使用盐值计算哈希
    const hash = crypto
        .createHash('sha256')
        .update(password + salt)
        .digest('hex');
    
    return { hash, salt };
}

function verifyPassword(password: string, hash: string, salt: string): boolean {
    const computed = hashPassword(password, salt);
    return computed.hash === hash;
}

// 使用
const { hash, salt } = hashPassword('myPassword123');
console.log('Hash:', hash);
console.log('Salt:', salt);

const isValid = verifyPassword('myPassword123', hash, salt);
console.log('Password valid:', isValid);
```

## 5. 参数说明：哈希方法参数

### createHash 参数

| 参数名       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **algorithm**| String   | 哈希算法名称                             | `'sha256'`, `'sha512'`, `'md5'`|

### update 参数

| 参数名       | 类型           | 说明                                     | 示例                           |
|:-------------|:---------------|:-----------------------------------------|:-------------------------------|
| **data**     | String/Buffer  | 要哈希的数据                             | `'Hello'` 或 `Buffer.from('Hello')`|
| **encoding** | String         | 数据编码（如果 data 是字符串）           | `'utf8'`                       |

### digest 参数

| 参数名       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **encoding** | String   | 输出编码格式                             | `'hex'`, `'base64'`, `'binary'`|

## 6. 返回值与状态说明

哈希操作的返回结果：

| 方法         | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **createHash**| Hash        | 返回哈希对象                             |
| **update**   | Hash         | 返回哈希对象，支持链式调用               |
| **digest**   | String/Buffer| 返回哈希值（根据 encoding 参数）         |

## 7. 代码示例：HMAC（密钥哈希）

HMAC 是带密钥的哈希算法，提供更好的安全性：

```ts
// 文件: crypto-hmac.ts
// 功能: HMAC 哈希

import crypto from 'node:crypto';

function createHMAC(data: string, secret: string): string {
    return crypto
        .createHmac('sha256', secret)
        .update(data)
        .digest('hex');
}

function verifyHMAC(data: string, secret: string, hmac: string): boolean {
    const computed = createHMAC(data, secret);
    return computed === hmac;
}

// 使用
const data = 'sensitive data';
const secret = 'my-secret-key';
const hmac = createHMAC(data, secret);

console.log('HMAC:', hmac);
console.log('Verified:', verifyHMAC(data, secret, hmac));
```

## 8. 输出结果说明

哈希计算的输出结果：

```text
SHA-256: a1b2c3d4e5f6...
SHA-512: 1a2b3c4d5e6f...
HMAC: x1y2z3w4v5u6...
```

**逻辑解析**：
- SHA-256：256 位（32 字节）哈希值
- SHA-512：512 位（64 字节）哈希值
- HMAC：使用密钥的哈希值，提供更好的安全性

## 9. 使用场景

### 1. 密码存储

安全地存储用户密码：

```ts
// 密码存储示例
import crypto from 'node:crypto';

class PasswordManager {
    hashPassword(password: string): { hash: string; salt: string } {
        const salt = crypto.randomBytes(16).toString('hex');
        const hash = crypto
            .createHash('sha256')
            .update(password + salt)
            .digest('hex');
        return { hash, salt };
    }
    
    verifyPassword(password: string, hash: string, salt: string): boolean {
        const computed = crypto
            .createHash('sha256')
            .update(password + salt)
            .digest('hex');
        return computed === hash;
    }
}
```

### 2. 数据完整性验证

验证数据的完整性：

```ts
// 数据完整性验证示例
function verifyDataIntegrity(data: string, expectedHash: string): boolean {
    const computedHash = crypto
        .createHash('sha256')
        .update(data)
        .digest('hex');
    return computedHash === expectedHash;
}
```

### 3. 文件校验

校验文件是否被篡改：

```ts
// 文件校验示例
async function verifyFile(filePath: string, expectedHash: string): Promise<boolean> {
    const hash = await hashFile(filePath);
    return hash === expectedHash;
}
```

## 10. 注意事项与常见错误

- **算法选择**：使用安全的哈希算法（SHA-256、SHA-512），避免 MD5、SHA-1
- **盐值使用**：密码哈希时使用盐值，提高安全性
- **编码格式**：注意哈希值的编码格式（hex、base64）
- **性能考虑**：大文件使用流式哈希，避免内存问题
- **安全性**：不要使用哈希作为加密，哈希是单向的

## 11. 常见问题 (FAQ)

**Q: MD5 和 SHA-256 有什么区别？**
A: SHA-256 更安全，抗碰撞能力更强。MD5 已不推荐用于安全场景。

**Q: 为什么密码哈希要使用盐值？**
A: 盐值可以防止彩虹表攻击，即使两个用户使用相同密码，哈希值也不同。

**Q: 如何选择哈希算法？**
A: 安全场景使用 SHA-256 或 SHA-512，性能要求高时使用 SHA-256。

## 12. 最佳实践

- **算法选择**：使用 SHA-256 或 SHA-512，避免 MD5、SHA-1
- **盐值使用**：密码哈希时使用随机盐值
- **流式处理**：大文件使用流式哈希
- **错误处理**：处理哈希计算中的错误
- **性能优化**：合理选择哈希算法，平衡安全性和性能

## 13. 对比分析：哈希算法选择

| 算法       | 安全性     | 速度     | 输出长度 | 推荐场景           |
|:-----------|:-----------|:---------|:---------|:-------------------|
| **MD5**    | 低（已破解）| 快       | 128 位   | ❌ 仅用于非安全场景|
| **SHA-1**  | 低（已破解）| 快       | 160 位   | ❌ 不推荐          |
| **SHA-256**| 高         | 中等     | 256 位   | ✅ 推荐（通用）    |
| **SHA-512**| 高         | 较慢     | 512 位   | ✅ 推荐（更高安全）|

## 14. 练习任务

1. **哈希计算实践**：
   - 使用不同算法计算哈希值
   - 理解哈希的不可逆性
   - 实现数据完整性验证

2. **密码哈希实践**：
   - 实现带盐值的密码哈希
   - 实现密码验证功能
   - 理解盐值的作用

3. **HMAC 实践**：
   - 使用 HMAC 计算哈希
   - 实现 HMAC 验证
   - 理解 HMAC 的优势

4. **实际应用**：
   - 在实际项目中应用哈希算法
   - 实现密码存储功能
   - 实现数据完整性验证

完成以上练习后，继续学习下一节：加密与解密。

## 总结

哈希算法是加密与安全的基础：

- **单向性**：哈希是单向的，无法反推
- **算法选择**：使用 SHA-256 或 SHA-512
- **盐值使用**：密码哈希时使用盐值
- **最佳实践**：算法选择、盐值使用、流式处理

掌握哈希算法有助于实现安全的密码存储和数据验证。

---

**最后更新**：2025-01-XX
