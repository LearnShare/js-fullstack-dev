# 8.8.4 类型测试

## 概述

类型测试是验证类型定义正确性的测试方法。本节介绍如何在测试框架中进行类型测试，确保类型定义的正确性。

## 类型测试方法

### 1. 使用 expectTypeOf

使用 Vitest 的 `expectTypeOf` 进行类型测试：

```ts
// 需要安装 @vitest/ui
import { expectTypeOf } from 'vitest';

describe('type testing', () => {
    it('should have correct type', () => {
        const user = { id: 1, name: 'John' };
        expectTypeOf(user).toMatchTypeOf<{ id: number; name: string }>();
    });
});
```

### 2. 使用类型断言

使用类型断言验证类型：

```ts
import { describe, it, expect } from 'vitest';

describe('type assertions', () => {
    it('should assert type', () => {
        const value: number = 42;
        expect(typeof value).toBe('number');
    });
});
```

### 3. 使用类型守卫

使用类型守卫验证类型：

```ts
import { describe, it, expect } from 'vitest';

function isUser(data: unknown): data is User {
    return (
        typeof data === 'object' &&
        data !== null &&
        'id' in data &&
        'name' in data
    );
}

describe('type guards', () => {
    it('should validate type', () => {
        const data = { id: 1, name: 'John' };
        expect(isUser(data)).toBe(true);
    });
});
```

## tsd 类型测试

### 1. 安装 tsd

安装 tsd 进行类型测试：

```bash
npm install --save-dev tsd
```

### 2. 编写类型测试

创建 `.test-d.ts` 文件：

```ts
// types.test-d.ts
import { expectType } from 'tsd';
import { User, CreateUserRequest } from './types';

// 测试类型
expectType<string>(new User('John').name);
expectType<number>(new User('John', 30).age);

// 测试函数类型
expectType<Promise<User>>(createUser({ name: 'John', email: 'john@example.com' }));
```

### 3. 运行类型测试

运行类型测试：

```bash
npx tsd
```

## 类型测试实践

### 1. API 类型测试

测试 API 类型：

```ts
// api.test-d.ts
import { expectType } from 'tsd';
import { fetchUser, createUser } from './api';
import { User, CreateUserRequest } from './types';

// 测试返回类型
expectType<Promise<User>>(fetchUser(1));

// 测试参数类型
expectType<Promise<User>>(createUser({ name: 'John', email: 'john@example.com' }));
```

### 2. 工具类型测试

测试工具类型：

```ts
// utils.test-d.ts
import { expectType } from 'tsd';
import { Partial, Pick, Omit } from './utils';

interface User {
    id: number;
    name: string;
    email: string;
}

// 测试 Partial
expectType<Partial<User>>({ name: 'John' });

// 测试 Pick
expectType<Pick<User, 'name'>>({ name: 'John' });

// 测试 Omit
expectType<Omit<User, 'id'>>({ name: 'John', email: 'john@example.com' });
```

### 3. 泛型类型测试

测试泛型类型：

```ts
// generics.test-d.ts
import { expectType } from 'tsd';

interface Container<T> {
    value: T;
}

// 测试泛型类型
expectType<Container<string>>({ value: 'hello' });
expectType<Container<number>>({ value: 42 });
```

## 注意事项

1. **工具选择**：选择合适的类型测试工具
2. **测试范围**：确定需要测试的类型范围
3. **持续维护**：需要持续维护类型测试
4. **性能考虑**：类型测试可能影响构建性能
5. **工具支持**：确保工具链支持类型测试

## 最佳实践

1. **关键类型**：为重点类型编写类型测试
2. **工具类型**：为工具类型编写类型测试
3. **API 类型**：为 API 类型编写类型测试
4. **持续集成**：在 CI/CD 中运行类型测试
5. **文档说明**：为类型测试添加文档

## 练习任务

1. **类型测试**：
   - 使用 expectTypeOf 进行类型测试
   - 使用类型断言验证类型
   - 理解类型测试的作用

2. **tsd 测试**：
   - 安装和配置 tsd
   - 编写类型测试文件
   - 运行类型测试

3. **API 类型测试**：
   - 为 API 类型编写类型测试
   - 测试请求和响应类型
   - 理解 API 类型测试的作用

4. **工具类型测试**：
   - 为工具类型编写类型测试
   - 测试类型转换
   - 理解工具类型测试的作用

5. **实际应用**：
   - 在实际项目中编写类型测试
   - 评估类型测试的效果
   - 总结使用经验

完成以上练习后，继续学习下一节：Mock 类型。

## 总结

类型测试是验证类型定义正确性的重要方法：

- **类型验证**：验证类型定义的正确性
- **工具支持**：使用工具进行类型测试
- **最佳实践**：遵循类型测试的最佳实践
- **持续维护**：需要持续维护类型测试

掌握类型测试有助于确保类型定义的正确性。

---

**最后更新**：2025-01-XX
