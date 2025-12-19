# 2.6.1 加密与安全概述

## 1. 概述

crypto 模块是 Node.js 提供加密功能的核心模块，支持哈希、加密、解密、数字签名等安全操作。理解加密模块的使用对于构建安全的 Node.js 应用至关重要，特别是在处理敏感数据、用户认证、数据传输等场景中。

## 2. 特性说明

- **哈希算法**：支持多种哈希算法（MD5、SHA-256、SHA-512 等）。
- **加密解密**：支持对称加密（AES）和非对称加密（RSA）。
- **数字签名**：支持数字签名和验证。
- **随机数生成**：提供加密安全的随机数生成。
- **密钥管理**：支持密钥生成和管理。

## 3. 模块导入方式

### ES Modules 方式

```ts
import crypto from 'node:crypto';
```

### CommonJS 方式

```ts
const crypto = require('node:crypto');
```

## 4. 加密算法类型

| 算法类型     | 说明                                     | 示例                           |
|:-------------|:-----------------------------------------|:-------------------------------|
| **哈希算法** | 单向加密，不可逆                         | SHA-256、MD5                    |
| **对称加密** | 加密和解密使用相同密钥                    | AES-256                         |
| **非对称加密**| 加密和解密使用不同密钥（公钥/私钥）      | RSA、ECDSA                      |
| **数字签名** | 使用私钥签名，公钥验证                    | RSA-SHA256、ECDSA-SHA256        |

## 5. 参数说明：crypto 模块常用 API

| API 名称      | 说明                                     | 示例                           |
|:--------------|:-----------------------------------------|:-------------------------------|
| **createHash**| 创建哈希对象                              | `crypto.createHash('sha256')`  |
| **createCipheriv**| 创建加密对象（对称加密）              | `crypto.createCipheriv(...)`   |
| **createDecipheriv**| 创建解密对象（对称加密）              | `crypto.createDecipheriv(...)` |
| **randomBytes**| 生成随机字节                              | `crypto.randomBytes(32)`       |

## 6. 返回值与状态说明

加密操作的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **哈希**     | String/Buffer| 返回哈希值（十六进制字符串或 Buffer）    |
| **加密**     | Buffer       | 返回加密后的数据（Buffer）                |
| **解密**     | Buffer       | 返回解密后的数据（Buffer）                |
| **随机数**   | Buffer       | 返回随机字节（Buffer）                    |

## 7. 代码示例：基本加密操作

以下示例演示了 crypto 模块的基本使用：

```ts
// 文件: crypto-basic.ts
// 功能: crypto 模块基本使用

import crypto from 'node:crypto';

// 1. 哈希计算
const data = 'Hello, Node.js!';
const hash = crypto.createHash('sha256').update(data).digest('hex');
console.log('Hash:', hash);

// 2. 生成随机字节
const randomBytes = crypto.randomBytes(32);
console.log('Random bytes:', randomBytes.toString('hex'));

// 3. 生成随机 UUID
const uuid = crypto.randomUUID();
console.log('UUID:', uuid);
```

## 8. 输出结果说明

加密操作的输出结果：

```text
Hash: a1b2c3d4e5f6...
Random bytes: 1a2b3c4d5e6f...
UUID: 550e8400-e29b-41d4-a716-446655440000
```

**逻辑解析**：
- 哈希计算：使用 SHA-256 算法计算数据的哈希值
- 随机字节：生成 32 字节的随机数据
- UUID：生成唯一标识符

## 9. 使用场景

### 1. 密码哈希

对用户密码进行哈希存储：

```ts
// 密码哈希示例
function hashPassword(password: string): string {
    return crypto.createHash('sha256').update(password).digest('hex');
}
```

### 2. 数据完整性验证

验证数据的完整性：

```ts
// 数据完整性验证示例
function verifyData(data: string, hash: string): boolean {
    const computedHash = crypto.createHash('sha256').update(data).digest('hex');
    return computedHash === hash;
}
```

### 3. 随机令牌生成

生成随机令牌：

```ts
// 随机令牌生成示例
function generateToken(): string {
    return crypto.randomBytes(32).toString('hex');
}
```

## 10. 注意事项与常见错误

- **密钥安全**：密钥必须安全存储，不要硬编码在代码中
- **算法选择**：使用安全的加密算法（避免 MD5、SHA-1）
- **随机数质量**：使用 `crypto.randomBytes()` 而非 `Math.random()`
- **数据编码**：注意数据的编码格式（UTF-8、Base64 等）
- **性能考虑**：加密操作可能较耗时，注意性能影响

## 11. 常见问题 (FAQ)

**Q: MD5 和 SHA-256 有什么区别？**
A: SHA-256 更安全，抗碰撞能力更强。MD5 已不推荐用于安全场景。

**Q: 如何安全地存储密钥？**
A: 使用环境变量、密钥管理服务（如 AWS KMS）或加密的配置文件。

**Q: 对称加密和非对称加密如何选择？**
A: 对称加密速度快，适合大量数据；非对称加密更安全，适合密钥交换。

## 12. 最佳实践

- **算法选择**：使用现代、安全的加密算法（SHA-256、AES-256、RSA-2048+）
- **密钥管理**：安全地存储和管理密钥
- **盐值使用**：哈希时使用盐值，提高安全性
- **错误处理**：完善的错误处理和日志记录
- **性能优化**：合理使用加密操作，避免性能瓶颈

## 13. 对比分析：哈希算法选择

| 算法       | 安全性     | 速度     | 输出长度 | 推荐使用           |
|:-----------|:-----------|:---------|:---------|:-------------------|
| **MD5**    | 低（已破解）| 快       | 128 位   | ❌ 不推荐          |
| **SHA-1**  | 低（已破解）| 快       | 160 位   | ❌ 不推荐          |
| **SHA-256**| 高         | 中等     | 256 位   | ✅ 推荐            |
| **SHA-512**| 高         | 较慢     | 512 位   | ✅ 推荐（更高安全）|

## 14. 练习任务

1. **哈希计算实践**：
   - 使用不同的哈希算法计算哈希值
   - 理解哈希的不可逆性
   - 实现数据完整性验证

2. **随机数生成实践**：
   - 生成随机字节和 UUID
   - 理解随机数的安全性
   - 实现令牌生成功能

3. **实际应用**：
   - 实现密码哈希功能
   - 实现数据完整性验证
   - 实现令牌生成功能

完成以上练习后，继续学习下一节：哈希算法。

## 总结

加密与安全模块是 Node.js 安全功能的基础：

- **核心功能**：哈希、加密、解密、数字签名
- **算法选择**：使用现代、安全的加密算法
- **密钥管理**：安全地存储和管理密钥
- **最佳实践**：算法选择、密钥管理、错误处理

掌握加密模块有助于构建安全的 Node.js 应用。

---

**最后更新**：2025-01-XX
