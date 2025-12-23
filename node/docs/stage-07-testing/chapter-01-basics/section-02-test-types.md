# 7.1.2 测试类型（单元、集成、E2E）

## 1. 概述

测试类型包括单元测试、集成测试和 E2E 测试，每种测试类型有不同的特点和适用场景。理解不同测试类型有助于选择合适的测试策略。

## 2. 单元测试

### 2.1 定义

单元测试是对代码最小单元（函数、方法、类）的测试，在隔离环境中执行，不依赖外部资源。

### 2.2 特点

- **快速**：执行速度快
- **隔离**：独立执行
- **简单**：编写简单
- **覆盖广**：覆盖大部分代码

### 2.3 示例

```ts
// 被测试函数
function add(a: number, b: number): number {
  return a + b;
}

// 单元测试
import { describe, it, expect } from 'vitest';

describe('add', () => {
  it('should add two numbers', () => {
    expect(add(1, 2)).toBe(3);
  });
  
  it('should handle negative numbers', () => {
    expect(add(-1, 2)).toBe(1);
  });
});
```

### 2.4 适用场景

- 业务逻辑测试
- 工具函数测试
- 算法测试
- 数据处理测试

## 3. 集成测试

### 3.1 定义

集成测试是测试多个组件协作的测试，验证组件之间的接口和交互。

### 3.2 特点

- **协作**：测试组件协作
- **真实环境**：使用真实或模拟环境
- **中等速度**：执行速度中等
- **覆盖接口**：覆盖组件接口

### 3.3 示例

```ts
// API 集成测试
import { describe, it, expect, beforeAll, afterAll } from 'vitest';
import request from 'supertest';
import app from './app';

describe('User API', () => {
  beforeAll(async () => {
    // 设置测试数据库
  });
  
  afterAll(async () => {
    // 清理测试数据
  });
  
  it('should create a user', async () => {
    const response = await request(app)
      .post('/api/users')
      .send({ name: 'John', email: 'john@example.com' });
    
    expect(response.status).toBe(201);
    expect(response.body.name).toBe('John');
  });
});
```

### 3.4 适用场景

- API 测试
- 数据库测试
- 服务集成测试
- 中间件测试

## 4. E2E 测试

### 4.1 定义

E2E（End-to-End）测试是从用户角度测试完整流程的测试，模拟真实用户操作。

### 4.2 特点

- **完整流程**：测试完整用户流程
- **真实环境**：使用真实环境
- **速度慢**：执行速度慢
- **成本高**：编写和维护成本高

### 4.3 示例

```ts
// E2E 测试
import { test, expect } from '@playwright/test';

test('user can login and view profile', async ({ page }) => {
  // 访问登录页面
  await page.goto('http://localhost:3000/login');
  
  // 填写登录表单
  await page.fill('#email', 'user@example.com');
  await page.fill('#password', 'password123');
  await page.click('#login-button');
  
  // 验证跳转到个人资料页面
  await expect(page).toHaveURL('http://localhost:3000/profile');
  await expect(page.locator('h1')).toContainText('Profile');
});
```

### 4.4 适用场景

- 关键用户流程
- 用户界面测试
- 跨浏览器测试
- 回归测试

## 5. 测试类型对比

| 特性 | 单元测试 | 集成测试 | E2E 测试 |
|------|---------|---------|---------|
| 执行速度 | 快 | 中等 | 慢 |
| 编写成本 | 低 | 中等 | 高 |
| 维护成本 | 低 | 中等 | 高 |
| 稳定性 | 高 | 中等 | 低 |
| 覆盖范围 | 代码逻辑 | 组件接口 | 用户流程 |

## 6. 选择建议

### 6.1 测试策略

- **单元测试**：优先编写，覆盖大部分代码
- **集成测试**：适量编写，验证关键接口
- **E2E 测试**：关键流程，覆盖主要用户场景

### 6.2 工具选择

- **单元测试**：Vitest、Jest
- **集成测试**：Supertest、Testcontainers
- **E2E 测试**：Playwright、Cypress、Puppeteer

## 7. 最佳实践

### 7.1 测试组织

- 遵循测试金字塔
- 保持测试独立
- 使用描述性名称
- 组织测试结构

### 7.2 测试质量

- 测试应该简单
- 测试应该快速
- 测试应该稳定
- 测试应该可维护

## 8. 注意事项

- **测试平衡**：保持测试类型平衡
- **工具选择**：根据需求选择工具
- **持续优化**：定期优化测试策略
- **测试维护**：及时维护测试代码

## 9. 常见问题

### 9.1 如何选择测试类型？

根据测试目标、执行速度、维护成本选择。

### 9.2 如何平衡测试比例？

遵循测试金字塔，根据项目特点调整。

### 9.3 如何处理测试冲突？

保持测试独立，使用测试隔离。

## 10. 实践任务

1. **理解类型**：深入理解不同测试类型
2. **编写示例**：编写不同类型的测试示例
3. **工具对比**：对比不同测试工具
4. **策略设计**：设计测试策略
5. **最佳实践**：遵循测试最佳实践

---

**下一章**：[7.2 单元测试](../chapter-02-unit/readme.md)
