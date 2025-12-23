# 6.3.5 SQL 注入防护

## 1. 概述

SQL 注入是通过注入恶意 SQL 语句来攻击数据库的攻击方式。SQL 注入可以导致数据泄露、数据篡改、权限提升等严重后果。

## 2. SQL 注入原理

### 2.1 攻击示例

```ts
// ❌ 不安全：字符串拼接
app.get('/users', (req: Request, res: Response): void => {
  const name = req.query.name;
  const query = `SELECT * FROM users WHERE name = '${name}'`;
  // 如果 name = "admin' OR '1'='1"，查询变成：
  // SELECT * FROM users WHERE name = 'admin' OR '1'='1'
  db.query(query);
});
```

### 2.2 攻击类型

- **联合查询注入**：使用 UNION 查询
- **布尔盲注**：通过布尔结果推断数据
- **时间盲注**：通过延迟推断数据
- **错误注入**：通过错误信息获取数据

## 3. 防护措施

### 3.1 参数化查询

```ts
// ✅ 安全：参数化查询
app.get('/users', (req: Request, res: Response): void => {
  const name = req.query.name;
  db.query('SELECT * FROM users WHERE name = $1', [name]);
});

// ✅ 安全：使用 ORM
const user = await User.findOne({ where: { name: req.query.name } });
```

### 3.2 输入验证

```ts
import { z } from 'zod';

const nameSchema = z.string().regex(/^[a-zA-Z0-9_]+$/);

app.get('/users', (req: Request, res: Response): void => {
  const result = nameSchema.safeParse(req.query.name);
  if (!result.success) {
    res.status(400).json({ message: 'Invalid name' });
    return;
  }
  
  db.query('SELECT * FROM users WHERE name = $1', [result.data]);
});
```

### 3.3 最小权限

```ts
// 使用最小权限的数据库用户
const db = new Pool({
  user: 'app_user', // 只有必要权限的用户
  password: 'password',
  database: 'mydb'
});

// 避免使用超级用户
// const db = new Pool({ user: 'postgres' }); // ❌ 危险
```

### 3.4 使用 ORM

```ts
// 使用 Prisma（自动参数化）
const user = await prisma.user.findFirst({
  where: { name: req.query.name }
});

// 使用 TypeORM（自动参数化）
const user = await userRepository.findOne({
  where: { name: req.query.name }
});
```

## 4. 最佳实践

### 4.1 开发规范

- 永远不使用字符串拼接
- 始终使用参数化查询
- 验证所有输入
- 使用 ORM 框架

### 4.2 安全配置

- 最小权限原则
- 禁用危险函数
- 错误信息不泄露
- 定期安全审计

## 5. 注意事项

- **参数化查询**：始终使用参数化查询
- **输入验证**：验证所有输入
- **错误处理**：不泄露数据库错误信息
- **权限管理**：使用最小权限

## 6. 常见问题

### 6.1 如何检测 SQL 注入？

使用安全扫描工具、代码审查、渗透测试。

### 6.2 ORM 是否完全安全？

ORM 通常安全，但仍需注意动态查询和原始查询。

### 6.3 如何处理动态查询？

使用查询构建器，避免字符串拼接。

## 7. 实践任务

1. **参数化查询**：实现参数化查询
2. **输入验证**：实现输入验证
3. **ORM 使用**：使用 ORM 框架
4. **安全配置**：配置数据库安全
5. **漏洞测试**：进行 SQL 注入测试

---

**下一节**：[6.3.6 Helmet.js 安全头](section-06-helmet.md)
