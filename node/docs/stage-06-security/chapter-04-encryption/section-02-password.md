# 6.4.2 密码加密（bcrypt、argon2）

## 1. 概述

密码加密是保护用户密码的重要手段，使用哈希算法将密码转换为不可逆的哈希值。bcrypt 和 argon2 是常用的密码哈希算法，提供了安全的密码存储方案。

## 2. bcrypt

### 2.1 安装

```bash
npm install bcrypt
npm install @types/bcrypt -D
```

### 2.2 密码哈希

```ts
import bcrypt from 'bcrypt';

async function hashPassword(password: string): Promise<string> {
  const saltRounds: number = 10;
  const hashedPassword: string = await bcrypt.hash(password, saltRounds);
  return hashedPassword;
}

// 使用
const password = 'userpassword';
const hashed = await hashPassword(password);
console.log('Hashed password:', hashed);
```

### 2.3 密码验证

```ts
async function verifyPassword(password: string, hashedPassword: string): Promise<boolean> {
  const isValid: boolean = await bcrypt.compare(password, hashedPassword);
  return isValid;
}

// 使用
const isValid = await verifyPassword('userpassword', hashed);
if (isValid) {
  console.log('Password is correct');
}
```

### 2.4 完整示例

```ts
import express, { Express, Request, Response } from 'express';

const app: Express = express();

// 注册
app.post('/register', async (req: Request, res: Response): Promise<void> => {
  const { username, password }: { username: string; password: string } = req.body;
  
  const hashedPassword = await bcrypt.hash(password, 10);
  
  await db.query(
    'INSERT INTO users (username, password) VALUES ($1, $2)',
    [username, hashedPassword]
  );
  
  res.json({ message: 'User registered' });
});

// 登录
app.post('/login', async (req: Request, res: Response): Promise<void> => {
  const { username, password }: { username: string; password: string } = req.body;
  
  const user = await db.query('SELECT * FROM users WHERE username = $1', [username]);
  
  if (user.length === 0) {
    res.status(401).json({ message: 'Invalid credentials' });
    return;
  }
  
  const isValid = await bcrypt.compare(password, user[0].password);
  
  if (!isValid) {
    res.status(401).json({ message: 'Invalid credentials' });
    return;
  }
  
  res.json({ message: 'Login successful' });
});
```

## 3. argon2

### 3.1 安装

```bash
npm install argon2
```

### 3.2 密码哈希

```ts
import argon2 from 'argon2';

async function hashPassword(password: string): Promise<string> {
  const hashedPassword: string = await argon2.hash(password);
  return hashedPassword;
}

// 使用自定义参数
async function hashPasswordWithOptions(password: string): Promise<string> {
  const hashedPassword: string = await argon2.hash(password, {
    type: argon2.argon2id,
    memoryCost: 65536, // 64 MB
    timeCost: 3,
    parallelism: 4
  });
  return hashedPassword;
}
```

### 3.3 密码验证

```ts
async function verifyPassword(password: string, hashedPassword: string): Promise<boolean> {
  try {
    const isValid: boolean = await argon2.verify(hashedPassword, password);
    return isValid;
  } catch (error) {
    return false;
  }
}
```

## 4. 算法对比

### 4.1 bcrypt vs argon2

| 特性 | bcrypt | argon2 |
|------|--------|--------|
| 内存硬度 | 低 | 高 |
| 抗 GPU 攻击 | 中等 | 强 |
| 性能 | 中等 | 可配置 |
| 标准化 | 是 | 是（2015） |

### 4.2 选择建议

- **bcrypt**：简单场景，成熟稳定
- **argon2**：高安全要求，抗 GPU 攻击

## 5. 最佳实践

### 5.1 密码策略

- 最小长度要求
- 复杂度要求
- 定期更换
- 密码历史

### 5.2 安全考虑

- 使用强哈希算法
- 合适的成本参数
- 加盐处理（自动）
- 防止时序攻击

## 6. 注意事项

- **成本参数**：根据性能和安全需求设置
- **密码策略**：实施强密码策略
- **错误处理**：不泄露密码相关信息
- **性能影响**：考虑哈希性能

## 7. 常见问题

### 7.1 如何选择成本参数？

根据服务器性能和安全性需求平衡选择。

### 7.2 如何处理密码重置？

生成安全的重置令牌，设置过期时间。

### 7.3 如何实现密码历史？

存储最近 N 个密码哈希，防止重复使用。

## 8. 实践任务

1. **密码哈希**：实现密码哈希功能
2. **密码验证**：实现密码验证功能
3. **注册登录**：实现注册和登录功能
4. **密码策略**：实施密码策略
5. **安全测试**：测试密码安全性

---

**下一节**：[6.4.3 数据加密](section-03-data-encryption.md)
