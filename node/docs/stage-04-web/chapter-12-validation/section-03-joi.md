# 4.12.3 Joi 数据校验

## 1. 概述

Joi 是一个功能强大的数据验证库，提供了丰富的验证规则和链式 API。Joi 支持 JavaScript 和 TypeScript，广泛应用于 Node.js 项目。

## 2. 特性说明

- **功能丰富**：提供丰富的验证规则
- **链式 API**：流畅的链式 API
- **广泛使用**：社区广泛使用
- **JavaScript/TypeScript**：支持 JavaScript 和 TypeScript

## 3. 安装与初始化

### 3.1 安装

```bash
npm install joi
npm install @types/joi -D
```

### 3.2 基本使用

```ts
import Joi from 'joi';

const userSchema = Joi.object({
  name: Joi.string().required(),
  email: Joi.string().email().required(),
  age: Joi.number().integer().min(0).max(150).optional()
});

const { value, error } = userSchema.validate({ name: 'John', email: 'john@example.com', age: 30 });
```

## 4. 基本类型

### 4.1 字符串验证

```ts
const stringSchema = Joi.string()
  .min(1)
  .max(100)
  .email()
  .uri()
  .pattern(/^[A-Z]/)
  .required();
```

### 4.2 数字验证

```ts
const numberSchema = Joi.number()
  .integer()
  .positive()
  .min(0)
  .max(100)
  .required();
```

### 4.3 布尔值验证

```ts
const booleanSchema = Joi.boolean();
```

### 4.4 日期验证

```ts
const dateSchema = Joi.date()
  .min('2020-01-01')
  .max('now');
```

## 5. 对象验证

### 5.1 基本对象

```ts
const userSchema = Joi.object({
  name: Joi.string().min(1).required(),
  email: Joi.string().email().required(),
  age: Joi.number().integer().min(0).optional()
});
```

### 5.2 嵌套对象

```ts
const addressSchema = Joi.object({
  street: Joi.string().required(),
  city: Joi.string().required(),
  zipCode: Joi.string().required()
});

const userSchema = Joi.object({
  name: Joi.string().required(),
  email: Joi.string().email().required(),
  address: addressSchema
});
```

### 5.3 条件验证

```ts
const userSchema = Joi.object({
  type: Joi.string().valid('individual', 'company').required(),
  name: Joi.string().when('type', {
    is: 'individual',
    then: Joi.required(),
    otherwise: Joi.optional()
  }),
  companyName: Joi.string().when('type', {
    is: 'company',
    then: Joi.required(),
    otherwise: Joi.optional()
  })
});
```

## 6. 数组验证

### 6.1 基本数组

```ts
const arraySchema = Joi.array().items(Joi.string());
```

### 6.2 数组长度

```ts
const arraySchema = Joi.array()
  .items(Joi.string())
  .min(1)
  .max(10);
```

### 6.3 对象数组

```ts
const usersSchema = Joi.array().items(Joi.object({
  name: Joi.string().required(),
  email: Joi.string().email().required()
}));
```

## 7. 与 Express 集成

### 7.1 验证中间件

```ts
import { Request, Response, NextFunction } from 'express';
import Joi from 'joi';

function validateBody(schema: Joi.ObjectSchema) {
  return (req: Request, res: Response, next: NextFunction): void => {
    const { error, value } = schema.validate(req.body, { abortEarly: false });
    
    if (error) {
      return res.status(400).json({
        error: 'Validation failed',
        details: error.details.map((detail: Joi.ValidationErrorItem) => ({
          path: detail.path.join('.'),
          message: detail.message
        }))
      });
    }
    
    req.body = value;
    next();
  };
}

const createUserSchema = Joi.object({
  name: Joi.string().min(1).required(),
  email: Joi.string().email().required()
});

app.post('/api/users', validateBody(createUserSchema), (req: Request, res: Response): void => {
  res.json({ message: 'User created' });
});
```

### 7.2 验证查询参数

```ts
function validateQuery(schema: Joi.ObjectSchema) {
  return (req: Request, res: Response, next: NextFunction): void => {
    const { error, value } = schema.validate(req.query, { abortEarly: false });
    
    if (error) {
      return res.status(400).json({
        error: 'Invalid query parameters',
        details: error.details
      });
    }
    
    req.query = value;
    next();
  };
}

const paginationSchema = Joi.object({
  page: Joi.number().integer().min(1).default(1),
  limit: Joi.number().integer().min(1).max(100).default(10)
});

app.get('/api/users', validateQuery(paginationSchema), (req: Request, res: Response): void => {
  const { page, limit } = req.query as { page: number; limit: number };
  res.json({ page, limit });
});
```

## 8. 自定义验证

### 8.1 自定义规则

```ts
const passwordSchema = Joi.string()
  .min(8)
  .pattern(/[A-Z]/, 'uppercase')
  .pattern(/[a-z]/, 'lowercase')
  .pattern(/[0-9]/, 'number')
  .required();
```

### 8.2 自定义消息

```ts
const userSchema = Joi.object({
  name: Joi.string().min(1).required().messages({
    'string.empty': 'Name is required',
    'string.min': 'Name must be at least 1 character'
  }),
  email: Joi.string().email().required().messages({
    'string.email': 'Invalid email format',
    'any.required': 'Email is required'
  })
});
```

## 9. 最佳实践

### 9.1 Schema 组织

- 按功能模块组织 Schema
- 复用通用 Schema
- 使用 Joi 扩展

### 9.2 错误处理

- 提供清晰的错误信息
- 使用自定义消息
- 记录验证失败

### 9.3 性能优化

- 缓存 Schema 定义
- 优化验证逻辑
- 使用 abortEarly 选项

## 10. 注意事项

- **错误处理**：正确处理验证错误
- **性能**：注意验证的性能影响
- **可维护性**：保持 Schema 清晰
- **类型安全**：使用 TypeScript 类型定义

## 11. 常见问题

### 11.1 如何处理可选字段？

使用 `.optional()` 定义可选字段。

### 11.2 如何实现自定义验证？

使用 `.custom()` 实现自定义验证函数。

### 11.3 如何处理类型转换？

使用 `.transform()` 实现类型转换。

## 12. 实践任务

1. **定义 Schema**：定义用户、文章等数据的 Schema
2. **实现验证中间件**：实现请求体验证中间件
3. **实现自定义验证**：实现自定义验证规则
4. **实现错误处理**：实现验证错误处理
5. **优化验证性能**：优化验证逻辑和性能

---

**下一节**：[4.12.4 class-validator](section-04-class-validator.md)
