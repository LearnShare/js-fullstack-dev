# 3.6.4 验证库

## 1. 概述

验证库用于验证数据的格式和有效性，是 API 开发和数据处理中的重要工具。验证库可以确保数据的正确性，防止无效数据进入系统。理解验证库的使用对于构建健壮的应用非常重要。

## 2. 特性说明

- **数据验证**：验证数据的格式和有效性。
- **类型安全**：提供 TypeScript 类型支持。
- **错误信息**：提供详细的错误信息。
- **模式定义**：使用模式定义验证规则。
- **组合验证**：支持复杂的组合验证。

## 3. 主流验证库

| 库名         | 特点                                     | 适用场景                       |
|:-------------|:-----------------------------------------|:-------------------------------|
| **zod**      | TypeScript 优先、类型推断、现代 API     | TypeScript 项目、推荐使用      |
| **yup**      | 功能丰富、使用广泛                       | 通用场景                       |
| **joi**      | 功能强大、配置灵活                       | 需要复杂验证规则               |

## 4. 基本用法

### 示例 1：zod

```ts
// 文件: validation-zod.ts
// 功能: zod 使用示例

import { z } from 'zod';

// 定义模式
const UserSchema = z.object({
    name: z.string().min(1).max(100),
    email: z.string().email(),
    age: z.number().int().min(0).max(150)
});

// 验证数据
function validateUser(data: unknown) {
    try {
        const user = UserSchema.parse(data);
        return { success: true, data: user };
    } catch (error) {
        return { success: false, error };
    }
}

// 类型推断
type User = z.infer<typeof UserSchema>;
```

### 示例 2：yup

```ts
// 文件: validation-yup.ts
// 功能: yup 使用示例

import * as yup from 'yup';

// 定义模式
const UserSchema = yup.object({
    name: yup.string().required().min(1).max(100),
    email: yup.string().required().email(),
    age: yup.number().required().integer().min(0).max(150)
});

// 验证数据
async function validateUser(data: unknown) {
    try {
        const user = await UserSchema.validate(data);
        return { success: true, data: user };
    } catch (error) {
        return { success: false, error };
    }
}
```

### 示例 3：joi

```ts
// 文件: validation-joi.ts
// 功能: joi 使用示例

import Joi from 'joi';

// 定义模式
const UserSchema = Joi.object({
    name: Joi.string().min(1).max(100).required(),
    email: Joi.string().email().required(),
    age: Joi.number().integer().min(0).max(150).required()
});

// 验证数据
function validateUser(data: unknown) {
    const { error, value } = UserSchema.validate(data);
    if (error) {
        return { success: false, error };
    }
    return { success: true, data: value };
}
```

## 5. 参数说明：验证库参数

### zod 参数

| 方法名       | 参数                                     | 说明                           |
|:-------------|:-----------------------------------------|:-------------------------------|
| **string()** | 链式调用                                 | 字符串验证                     |
| **number()** | 链式调用                                 | 数字验证                       |
| **email()**  | 无参数                                   | 邮箱验证                       |
| **min()**    | `(value)`                                | 最小值验证                     |
| **max()**    | `(value)`                                | 最大值验证                     |

## 6. 返回值与状态说明

验证库操作的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **验证成功** | 验证后的数据 | 返回验证后的数据                         |
| **验证失败** | 错误对象     | 返回详细的错误信息                       |

## 7. 代码示例：完整的验证系统

以下示例演示了完整的验证系统：

```ts
// 文件: validation-complete.ts
// 功能: 完整的验证系统

import { z } from 'zod';

// 定义验证模式
const UserSchema = z.object({
    name: z.string().min(1, 'Name is required').max(100, 'Name too long'),
    email: z.string().email('Invalid email'),
    age: z.number().int('Age must be integer').min(0).max(150),
    tags: z.array(z.string()).optional()
});

const CreateUserSchema = UserSchema.extend({
    password: z.string().min(8, 'Password too short')
});

const UpdateUserSchema = UserSchema.partial();

// 验证函数
function validateCreateUser(data: unknown) {
    try {
        const user = CreateUserSchema.parse(data);
        return { success: true, data: user };
    } catch (error) {
        if (error instanceof z.ZodError) {
            return {
                success: false,
                errors: error.errors.map(e => ({
                    path: e.path.join('.'),
                    message: e.message
                }))
            };
        }
        return { success: false, error };
    }
}

// 类型推断
type User = z.infer<typeof UserSchema>;
type CreateUser = z.infer<typeof CreateUserSchema>;
```

## 8. 输出结果说明

验证库的输出结果：

```text
Success: { name: 'Alice', email: 'alice@example.com', age: 25 }

Error: [
  { path: 'email', message: 'Invalid email' },
  { path: 'age', message: 'Age must be integer' }
]
```

**逻辑解析**：
- 验证成功返回验证后的数据
- 验证失败返回详细的错误信息
- 支持类型推断

## 9. 使用场景

### 1. API 请求验证

验证 API 请求数据：

```ts
// API 请求验证示例
import { z } from 'zod';

const RequestSchema = z.object({
    body: z.object({
        name: z.string(),
        email: z.string().email()
    })
});

function validateRequest(req: any) {
    return RequestSchema.parse(req);
}
```

### 2. 表单验证

验证表单数据：

```ts
// 表单验证示例
import { z } from 'zod';

const FormSchema = z.object({
    username: z.string().min(3),
    password: z.string().min(8)
});
```

### 3. 配置验证

验证配置文件：

```ts
// 配置验证示例
import { z } from 'zod';

const ConfigSchema = z.object({
    port: z.number().int().min(1).max(65535),
    database: z.string().url()
});
```

## 10. 注意事项与常见错误

- **类型安全**：使用 TypeScript 提供类型安全
- **错误处理**：完善的错误处理和用户友好的错误信息
- **性能考虑**：某些复杂验证可能有性能开销
- **模式复用**：合理复用验证模式
- **文档说明**：为验证规则提供文档说明

## 11. 常见问题 (FAQ)

**Q: zod 和 yup 如何选择？**
A: zod TypeScript 优先，类型推断好；yup 功能丰富，使用广泛。

**Q: 如何自定义验证规则？**
A: 使用 `refine` 或 `superRefine` 方法定义自定义验证。

**Q: 如何处理嵌套对象验证？**
A: 使用 `object()` 嵌套定义，或使用 `z.lazy()` 处理循环引用。

## 12. 最佳实践

- **类型安全**：使用 TypeScript 和类型推断
- **错误处理**：提供用户友好的错误信息
- **模式复用**：合理复用验证模式
- **性能优化**：注意性能，合理使用
- **文档说明**：为验证规则提供文档说明

## 13. 对比分析：验证库选择

| 维度             | zod                                    | yup                                 | joi                                 |
|:-----------------|:--------------------------------------|:-------------------------------------|:------------------------------------|
| **TypeScript**   | 优秀（类型推断）                      | 良好                                 | 良好                                |
| **功能**         | 功能丰富                              | 功能丰富                             | 功能强大                            |
| **API 风格**     | 现代、链式                            | 链式                                 | 配置式                              |
| **推荐使用**     | ✅ 推荐（TypeScript 项目）             | 通用场景                             | 需要复杂验证规则                    |

## 14. 练习任务

1. **验证库实践**：
   - 使用不同的验证库
   - 理解各库的特点
   - 实现数据验证

2. **模式定义实践**：
   - 定义验证模式
   - 实现复杂验证规则
   - 处理嵌套对象

3. **实际应用**：
   - 在实际项目中应用验证库
   - 实现 API 请求验证
   - 提供用户友好的错误信息

完成以上练习后，继续学习下一节：Markdown 处理库。

## 总结

验证库是保证数据正确性的重要工具：

- **核心功能**：数据验证、类型安全、错误信息
- **主流库**：zod、yup、joi
- **最佳实践**：类型安全、错误处理、模式复用

掌握验证库有助于构建健壮的应用。

---

**最后更新**：2025-01-XX
