# 4.12.2 Zod 数据校验

## 1. 概述

Zod 是一个 TypeScript 优先的数据验证库，提供了强大的类型推断和链式 API。Zod 通过 Schema 定义数据结构，自动推断 TypeScript 类型，提供类型安全的验证。

## 2. 特性说明

- **TypeScript 优先**：原生支持 TypeScript
- **类型推断**：自动推断 TypeScript 类型
- **链式 API**：流畅的链式 API
- **零依赖**：无外部依赖

## 3. 安装与初始化

### 3.1 安装

```bash
npm install zod
```

### 3.2 基本使用

```ts
import { z } from 'zod';

const userSchema = z.object({
  name: z.string(),
  email: z.string().email(),
  age: z.number().int().min(0).max(150)
});

type User = z.infer<typeof userSchema>;

const result = userSchema.parse({ name: 'John', email: 'john@example.com', age: 30 });
```

## 4. 基本类型

### 4.1 字符串验证

```ts
const stringSchema = z.string()
  .min(1, 'String cannot be empty')
  .max(100, 'String too long')
  .email('Invalid email format')
  .url('Invalid URL format')
  .regex(/^[A-Z]/, 'Must start with uppercase');
```

### 4.2 数字验证

```ts
const numberSchema = z.number()
  .int('Must be an integer')
  .positive('Must be positive')
  .min(0, 'Must be at least 0')
  .max(100, 'Must be at most 100');
```

### 4.3 布尔值验证

```ts
const booleanSchema = z.boolean();
```

### 4.4 日期验证

```ts
const dateSchema = z.date()
  .min(new Date('2020-01-01'), 'Date too early')
  .max(new Date(), 'Date cannot be in the future');
```

## 5. 对象验证

### 5.1 基本对象

```ts
const userSchema = z.object({
  name: z.string().min(1),
  email: z.string().email(),
  age: z.number().int().min(0).optional()
});

type User = z.infer<typeof userSchema>;
```

### 5.2 嵌套对象

```ts
const addressSchema = z.object({
  street: z.string(),
  city: z.string(),
  zipCode: z.string()
});

const userSchema = z.object({
  name: z.string(),
  email: z.string().email(),
  address: addressSchema
});
```

### 5.3 可选字段

```ts
const userSchema = z.object({
  name: z.string(),
  email: z.string().email(),
  age: z.number().int().optional(),
  phone: z.string().optional()
});
```

### 5.4 默认值

```ts
const userSchema = z.object({
  name: z.string(),
  email: z.string().email(),
  role: z.string().default('user'),
  active: z.boolean().default(true)
});
```

## 6. 数组验证

### 6.1 基本数组

```ts
const arraySchema = z.array(z.string());
```

### 6.2 数组长度

```ts
const arraySchema = z.array(z.string())
  .min(1, 'Array cannot be empty')
  .max(10, 'Array too long');
```

### 6.3 对象数组

```ts
const usersSchema = z.array(z.object({
  name: z.string(),
  email: z.string().email()
}));
```

## 7. 联合类型

### 7.1 字符串联合

```ts
const statusSchema = z.enum(['pending', 'approved', 'rejected']);
```

### 7.2 类型联合

```ts
const valueSchema = z.union([z.string(), z.number()]);
```

### 7.3 判别联合

```ts
const eventSchema = z.discriminatedUnion('type', [
  z.object({ type: z.literal('click'), x: z.number(), y: z.number() }),
  z.object({ type: z.literal('keypress'), key: z.string() })
]);
```

## 8. 与 Express 集成

### 8.1 验证中间件

```ts
import { Request, Response, NextFunction } from 'express';
import { z, ZodError } from 'zod';

function validateBody(schema: z.ZodSchema) {
  return (req: Request, res: Response, next: NextFunction): void => {
    try {
      req.body = schema.parse(req.body);
      next();
    } catch (error) {
      if (error instanceof ZodError) {
        return res.status(400).json({
          error: 'Validation failed',
          details: error.errors
        });
      }
      next(error);
    }
  };
}

const createUserSchema = z.object({
  name: z.string().min(1),
  email: z.string().email()
});

app.post('/api/users', validateBody(createUserSchema), (req: Request, res: Response): void => {
  // req.body 已经验证
  res.json({ message: 'User created' });
});
```

### 8.2 验证查询参数

```ts
function validateQuery(schema: z.ZodSchema) {
  return (req: Request, res: Response, next: NextFunction): void => {
    try {
      req.query = schema.parse(req.query);
      next();
    } catch (error) {
      if (error instanceof ZodError) {
        return res.status(400).json({
          error: 'Invalid query parameters',
          details: error.errors
        });
      }
      next(error);
    }
  };
}

const paginationSchema = z.object({
  page: z.string().transform((val) => parseInt(val, 10)).pipe(z.number().int().positive()),
  limit: z.string().transform((val) => parseInt(val, 10)).pipe(z.number().int().positive().max(100))
});

app.get('/api/users', validateQuery(paginationSchema), (req: Request, res: Response): void => {
  const { page, limit } = req.query as { page: number; limit: number };
  res.json({ page, limit });
});
```

## 9. 自定义验证

### 9.1 自定义验证函数

```ts
const passwordSchema = z.string()
  .min(8, 'Password must be at least 8 characters')
  .refine((val: string) => /[A-Z]/.test(val), 'Password must contain uppercase letter')
  .refine((val: string) => /[a-z]/.test(val), 'Password must contain lowercase letter')
  .refine((val: string) => /[0-9]/.test(val), 'Password must contain number');
```

### 9.2 异步验证

```ts
const uniqueEmailSchema = z.string().email().refine(
  async (email: string) => {
    const exists = await checkEmailExists(email);
    return !exists;
  },
  'Email already exists'
);
```

## 10. 最佳实践

### 10.1 Schema 组织

- 按功能模块组织 Schema
- 复用通用 Schema
- 使用类型推断

### 10.2 错误处理

- 提供清晰的错误信息
- 使用标准错误格式
- 记录验证失败

### 10.3 性能优化

- 缓存 Schema 定义
- 优化验证逻辑
- 使用 transform 减少重复验证

## 11. 注意事项

- **类型安全**：充分利用类型推断
- **错误处理**：正确处理验证错误
- **性能**：注意验证的性能影响
- **可维护性**：保持 Schema 清晰

## 12. 常见问题

### 12.1 如何处理可选字段？

使用 `.optional()` 或 `.nullable()` 定义可选字段。

### 12.2 如何实现自定义验证？

使用 `.refine()` 或 `.superRefine()` 实现自定义验证。

### 12.3 如何处理类型转换？

使用 `.transform()` 实现类型转换。

## 13. 实践任务

1. **定义 Schema**：定义用户、文章等数据的 Schema
2. **实现验证中间件**：实现请求体验证中间件
3. **实现自定义验证**：实现自定义验证规则
4. **实现错误处理**：实现验证错误处理
5. **优化验证性能**：优化验证逻辑和性能

---

**下一节**：[4.12.3 Joi 数据校验](section-03-joi.md)
