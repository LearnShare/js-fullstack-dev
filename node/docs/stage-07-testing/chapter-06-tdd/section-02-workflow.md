# 7.6.2 TDD 工作流程

## 1. 概述

TDD 工作流程是 Red-Green-Refactor 循环，包括编写失败测试（Red）、编写实现通过测试（Green）、重构代码（Refactor）三个阶段。

## 2. Red-Green-Refactor 循环

### 2.1 流程说明

```
1. Red（红）：编写失败测试
   ↓
2. Green（绿）：编写实现通过测试
   ↓
3. Refactor（重构）：重构代码
   ↓
   回到步骤 1
```

### 2.2 各阶段说明

- **Red**：编写测试，测试应该失败
- **Green**：编写最小实现，使测试通过
- **Refactor**：重构代码，保持测试通过

## 3. 实践示例

### 3.1 示例：计算器

#### 步骤 1：Red（编写失败测试）

```ts
// calculator.test.ts
import { describe, it, expect } from 'vitest';

describe('Calculator', () => {
  it('should add two numbers', (): void => {
    const calculator = new Calculator();
    expect(calculator.add(1, 2)).toBe(3);
  });
});
```

运行测试，测试失败（因为 Calculator 类不存在）。

#### 步骤 2：Green（编写实现）

```ts
// calculator.ts
export class Calculator {
  add(a: number, b: number): number {
    return a + b;
  }
}
```

运行测试，测试通过。

#### 步骤 3：Refactor（重构）

```ts
// calculator.ts
export class Calculator {
  add(a: number, b: number): number {
    // 重构：添加输入验证
    if (typeof a !== 'number' || typeof b !== 'number') {
      throw new Error('Invalid input');
    }
    return a + b;
  }
}
```

运行测试，测试仍然通过。

### 3.2 完整示例：用户服务

#### Red：编写测试

```ts
// user-service.test.ts
import { describe, it, expect } from 'vitest';
import { UserService } from './user-service';

describe('UserService', () => {
  it('should create a user', async (): Promise<void> => {
    const service = new UserService();
    const user = await service.createUser({ name: 'John', email: 'john@example.com' });
    
    expect(user).toHaveProperty('id');
    expect(user.name).toBe('John');
    expect(user.email).toBe('john@example.com');
  });
});
```

#### Green：编写实现

```ts
// user-service.ts
export class UserService {
  async createUser(data: { name: string; email: string }): Promise<{ id: number; name: string; email: string }> {
    // 最小实现
    return {
      id: 1,
      name: data.name,
      email: data.email
    };
  }
}
```

#### Refactor：重构

```ts
// user-service.ts
import { db } from './db';

export class UserService {
  async createUser(data: { name: string; email: string }): Promise<{ id: number; name: string; email: string }> {
    // 验证输入
    if (!data.name || !data.email) {
      throw new Error('Name and email are required');
    }
    
    // 保存到数据库
    const result = await db.query(
      'INSERT INTO users (name, email) VALUES ($1, $2) RETURNING id, name, email',
      [data.name, data.email]
    );
    
    return result.rows[0];
  }
}
```

## 4. TDD 节奏

### 4.1 小步快跑

- 每次只添加一个功能
- 快速通过 Red-Green-Refactor
- 保持测试通过
- 持续集成

### 4.2 测试粒度

- 测试应该小
- 一次测试一个功能
- 测试应该快速
- 测试应该独立

## 5. 最佳实践

### 5.1 测试编写

- 先写测试
- 测试应该失败
- 测试应该简单
- 测试应该快速

### 5.2 实现编写

- 最小实现
- 通过测试即可
- 避免过度设计
- 及时重构

### 5.3 重构

- 保持测试通过
- 小步重构
- 持续改进
- 保持简单

## 6. 注意事项

- **测试先行**：始终先写测试
- **小步迭代**：小步快跑
- **测试质量**：注重测试质量
- **重构时机**：及时重构

## 7. 常见问题

### 7.1 如何开始 TDD？

从简单功能开始，逐步适应 TDD 流程。

### 7.2 如何处理复杂功能？

将复杂功能分解为简单功能，逐步实现。

### 7.3 何时重构？

在 Green 阶段后，及时重构代码。

## 8. 实践任务

1. **理解流程**：理解 Red-Green-Refactor 流程
2. **编写测试**：先编写失败测试
3. **编写实现**：编写最小实现
4. **重构代码**：重构代码保持测试通过
5. **持续迭代**：持续进行 TDD 循环

---

**下一节**：[7.6.3 TDD 实践](section-03-practice.md)
