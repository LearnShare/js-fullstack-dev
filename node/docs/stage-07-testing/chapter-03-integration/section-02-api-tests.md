# 7.3.2 API 集成测试

## 1. 概述

API 集成测试是测试 API 接口的测试，验证 API 的功能、性能和错误处理。API 集成测试使用真实的 HTTP 请求，测试完整的请求-响应流程。

## 2. 测试工具

### 2.1 Supertest

**特点**：
- 专为 Express 设计
- 简单的 API
- 支持链式调用

### 2.2 安装

```bash
npm install -D supertest
npm install -D @types/supertest
```

## 3. 基本使用

### 3.1 Express 应用测试

```ts
import request from 'supertest';
import express, { Express } from 'express';

const app: Express = express();

describe('User API', () => {
  describe('POST /api/users', () => {
    it('should create a user', async (): Promise<void> => {
      const response = await request(app)
        .post('/api/users')
        .send({ name: 'John', email: 'john@example.com' })
        .expect(201);
      
      expect(response.body).toHaveProperty('id');
      expect(response.body.name).toBe('John');
      expect(response.body.email).toBe('john@example.com');
    });
    
    it('should validate input', async (): Promise<void> => {
      const response = await request(app)
        .post('/api/users')
        .send({ name: '' })
        .expect(400);
      
      expect(response.body).toHaveProperty('error');
    });
  });
  
  describe('GET /api/users/:id', () => {
    it('should get a user', async (): Promise<void> => {
      const response = await request(app)
        .get('/api/users/1')
        .expect(200);
      
      expect(response.body).toHaveProperty('id');
      expect(response.body.id).toBe(1);
    });
    
    it('should return 404 for non-existent user', async (): Promise<void> => {
      await request(app)
        .get('/api/users/999')
        .expect(404);
    });
  });
});
```

### 3.2 认证测试

```ts
describe('Protected API', () => {
  let authToken: string;
  
  beforeAll(async (): Promise<void> => {
    // 登录获取 token
    const response = await request(app)
      .post('/api/login')
      .send({ email: 'user@example.com', password: 'password' });
    
    authToken = response.body.token;
  });
  
  it('should access protected route with token', async (): Promise<void> => {
    const response = await request(app)
      .get('/api/profile')
      .set('Authorization', `Bearer ${authToken}`)
      .expect(200);
    
    expect(response.body).toHaveProperty('email');
  });
  
  it('should reject request without token', async (): Promise<void> => {
    await request(app)
      .get('/api/profile')
      .expect(401);
  });
});
```

## 4. 测试数据管理

### 4.1 测试数据库

```ts
import { Pool } from 'pg';

let testDb: Pool;

beforeAll(async (): Promise<void> => {
  testDb = new Pool({
    connectionString: process.env.TEST_DATABASE_URL
  });
  
  // 运行迁移
  await runMigrations(testDb);
});

afterAll(async (): Promise<void> => {
  await testDb.end();
});

beforeEach(async (): Promise<void> => {
  // 清理测试数据
  await testDb.query('TRUNCATE TABLE users CASCADE');
});
```

### 4.2 测试数据准备

```ts
async function createTestUser(data: { name: string; email: string }): Promise<number> {
  const result = await testDb.query(
    'INSERT INTO users (name, email) VALUES ($1, $2) RETURNING id',
    [data.name, data.email]
  );
  return result.rows[0].id;
}

it('should update user', async (): Promise<void> => {
  const userId = await createTestUser({ name: 'John', email: 'john@example.com' });
  
  const response = await request(app)
    .put(`/api/users/${userId}`)
    .send({ name: 'Jane' })
    .expect(200);
  
  expect(response.body.name).toBe('Jane');
});
```

## 5. 错误处理测试

```ts
describe('Error Handling', () => {
  it('should handle database errors', async (): Promise<void> => {
    // 模拟数据库错误
    jest.spyOn(db, 'query').mockRejectedValue(new Error('Database error'));
    
    const response = await request(app)
      .get('/api/users/1')
      .expect(500);
    
    expect(response.body).toHaveProperty('error');
  });
  
  it('should handle validation errors', async (): Promise<void> => {
    const response = await request(app)
      .post('/api/users')
      .send({ email: 'invalid-email' })
      .expect(400);
    
    expect(response.body).toHaveProperty('errors');
  });
});
```

## 6. 性能测试

```ts
describe('Performance', () => {
  it('should respond within acceptable time', async (): Promise<void> => {
    const start = Date.now();
    
    await request(app)
      .get('/api/users')
      .expect(200);
    
    const duration = Date.now() - start;
    expect(duration).toBeLessThan(1000); // 1 秒内响应
  });
});
```

## 7. 最佳实践

### 7.1 测试组织

- 按 API 端点组织
- 使用描述性名称
- 保持测试独立
- 使用测试钩子

### 7.2 数据管理

- 使用测试数据库
- 清理测试数据
- 准备测试数据
- 隔离测试环境

## 8. 注意事项

- **环境隔离**：使用独立的测试环境
- **数据清理**：及时清理测试数据
- **测试速度**：优化测试执行速度
- **错误处理**：测试错误处理逻辑

## 9. 常见问题

### 9.1 如何处理测试数据库？

使用独立的测试数据库，每次测试前清理数据。

### 9.2 如何测试认证？

使用测试用户登录，获取 token 进行测试。

### 9.3 如何优化测试性能？

并行执行、使用缓存、优化数据库查询。

## 10. 实践任务

1. **API 测试**：编写 API 集成测试
2. **认证测试**：测试认证相关 API
3. **数据管理**：管理测试数据
4. **错误处理**：测试错误处理
5. **性能测试**：进行性能测试

---

**下一节**：[7.3.3 数据库集成测试](section-03-database-tests.md)
