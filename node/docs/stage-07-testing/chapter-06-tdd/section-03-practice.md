# 7.6.3 TDD 实践

## 1. 概述

TDD 实践包括在实际项目中应用 TDD 方法，处理各种场景和挑战。本章介绍 TDD 的实际应用技巧和最佳实践。

## 2. 实践场景

### 2.1 业务逻辑

```ts
// 需求：实现用户年龄验证
// 规则：用户必须年满 18 岁

// Red：编写测试
describe('UserValidator', () => {
  it('should validate user age', (): void => {
    const validator = new UserValidator();
    expect(validator.validateAge(18)).toBe(true);
    expect(validator.validateAge(17)).toBe(false);
    expect(validator.validateAge(0)).toBe(false);
  });
});

// Green：编写实现
class UserValidator {
  validateAge(age: number): boolean {
    return age >= 18;
  }
}

// Refactor：重构
class UserValidator {
  private readonly MIN_AGE = 18;
  
  validateAge(age: number): boolean {
    if (age < 0) {
      throw new Error('Age cannot be negative');
    }
    return age >= this.MIN_AGE;
  }
}
```

### 2.2 API 开发

```ts
// Red：编写测试
describe('POST /api/users', () => {
  it('should create a user', async (): Promise<void> => {
    const response = await request(app)
      .post('/api/users')
      .send({ name: 'John', email: 'john@example.com' })
      .expect(201);
    
    expect(response.body).toHaveProperty('id');
    expect(response.body.name).toBe('John');
  });
});

// Green：编写实现
app.post('/api/users', async (req: Request, res: Response): Promise<void> => {
  const user = await db.query(
    'INSERT INTO users (name, email) VALUES ($1, $2) RETURNING *',
    [req.body.name, req.body.email]
  );
  res.status(201).json(user.rows[0]);
});

// Refactor：重构
app.post('/api/users', validateUserInput, async (req: Request, res: Response): Promise<void> => {
  const user = await userService.createUser(req.body);
  res.status(201).json(user);
});
```

## 3. 处理复杂场景

### 3.1 依赖处理

```ts
// Red：编写测试（使用 Mock）
describe('OrderService', () => {
  it('should create order', async (): Promise<void> => {
    const mockPaymentService = {
      processPayment: vi.fn().mockResolvedValue({ success: true })
    };
    
    const service = new OrderService(mockPaymentService);
    const order = await service.createOrder({ userId: 1, items: [] });
    
    expect(order).toBeDefined();
    expect(mockPaymentService.processPayment).toHaveBeenCalled();
  });
});

// Green：编写实现
class OrderService {
  constructor(private paymentService: PaymentService) {}
  
  async createOrder(data: { userId: number; items: any[] }): Promise<Order> {
    const order = await this.saveOrder(data);
    await this.paymentService.processPayment(order.id);
    return order;
  }
}
```

### 3.2 错误处理

```ts
// Red：编写测试
describe('UserService', () => {
  it('should throw error for duplicate email', async (): Promise<void> => {
    await userService.createUser({ name: 'John', email: 'john@example.com' });
    
    await expect(
      userService.createUser({ name: 'Jane', email: 'john@example.com' })
    ).rejects.toThrow('Email already exists');
  });
});

// Green：编写实现
async createUser(data: { name: string; email: string }): Promise<User> {
  const existing = await this.findUserByEmail(data.email);
  if (existing) {
    throw new Error('Email already exists');
  }
  return await this.saveUser(data);
}
```

## 4. TDD 技巧

### 4.1 测试驱动设计

- 测试帮助发现设计问题
- 测试驱动接口设计
- 测试帮助简化设计
- 测试支持重构

### 4.2 增量开发

- 从简单开始
- 逐步增加功能
- 保持测试通过
- 持续重构

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

### 7.1 如何处理复杂功能？

将复杂功能分解为简单功能，逐步实现。

### 7.2 如何处理遗留代码？

逐步添加测试，逐步重构。

### 7.3 如何保持 TDD 节奏？

保持小步快跑，快速通过 Red-Green-Refactor。

## 8. 实践任务

1. **简单功能**：使用 TDD 实现简单功能
2. **复杂功能**：使用 TDD 实现复杂功能
3. **API 开发**：使用 TDD 开发 API
4. **错误处理**：使用 TDD 处理错误
5. **持续实践**：持续实践 TDD 方法

---

**下一章**：[7.7 行为驱动开发（BDD）](../chapter-07-bdd/readme.md)
