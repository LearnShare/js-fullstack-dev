# 7.3.3 数据库集成测试

## 1. 概述

数据库集成测试是测试数据库操作的测试，验证数据库查询、事务、约束等功能。数据库集成测试使用真实的数据库，测试完整的数据库操作流程。

## 2. 测试环境设置

### 2.1 测试数据库

```ts
import { Pool } from 'pg';

let testDb: Pool;

beforeAll(async (): Promise<void> => {
  testDb = new Pool({
    connectionString: process.env.TEST_DATABASE_URL || 'postgresql://localhost/test_db'
  });
  
  // 运行迁移
  await runMigrations(testDb);
});

afterAll(async (): Promise<void> => {
  await testDb.end();
});

beforeEach(async (): Promise<void> => {
  // 清理测试数据
  await testDb.query('TRUNCATE TABLE users, posts CASCADE');
});
```

### 2.2 事务回滚

```ts
import { Pool, PoolClient } from 'pg';

describe('Database Tests', () => {
  let client: PoolClient;
  
  beforeEach(async (): Promise<void> => {
    client = await testDb.connect();
    await client.query('BEGIN');
  });
  
  afterEach(async (): Promise<void> => {
    await client.query('ROLLBACK');
    client.release();
  });
  
  it('should create user', async (): Promise<void> => {
    await client.query(
      'INSERT INTO users (name, email) VALUES ($1, $2)',
      ['John', 'john@example.com']
    );
    
    const result = await client.query('SELECT * FROM users WHERE email = $1', ['john@example.com']);
    expect(result.rows).toHaveLength(1);
  });
});
```

## 3. 数据库操作测试

### 3.1 CRUD 操作

```ts
describe('User Repository', () => {
  it('should create a user', async (): Promise<void> => {
    const userId = await createUser({ name: 'John', email: 'john@example.com' });
    expect(userId).toBeDefined();
    
    const user = await getUserById(userId);
    expect(user?.name).toBe('John');
  });
  
  it('should update a user', async (): Promise<void> => {
    const userId = await createUser({ name: 'John', email: 'john@example.com' });
    
    await updateUser(userId, { name: 'Jane' });
    
    const user = await getUserById(userId);
    expect(user?.name).toBe('Jane');
  });
  
  it('should delete a user', async (): Promise<void> => {
    const userId = await createUser({ name: 'John', email: 'john@example.com' });
    
    await deleteUser(userId);
    
    const user = await getUserById(userId);
    expect(user).toBeNull();
  });
});
```

### 3.2 查询测试

```ts
describe('User Queries', () => {
  beforeEach(async (): Promise<void> => {
    await createUser({ name: 'John', email: 'john@example.com' });
    await createUser({ name: 'Jane', email: 'jane@example.com' });
  });
  
  it('should find users by email', async (): Promise<void> => {
    const user = await findUserByEmail('john@example.com');
    expect(user).toBeDefined();
    expect(user?.email).toBe('john@example.com');
  });
  
  it('should list users with pagination', async (): Promise<void> => {
    const users = await listUsers({ limit: 10, offset: 0 });
    expect(users).toHaveLength(2);
  });
  
  it('should search users by name', async (): Promise<void> => {
    const users = await searchUsers('John');
    expect(users).toHaveLength(1);
    expect(users[0].name).toBe('John');
  });
});
```

### 3.3 关系测试

```ts
describe('User-Post Relationship', () => {
  it('should create post with user', async (): Promise<void> => {
    const userId = await createUser({ name: 'John', email: 'john@example.com' });
    const postId = await createPost({ userId, title: 'Test Post', content: 'Content' });
    
    const post = await getPostById(postId);
    expect(post?.userId).toBe(userId);
    expect(post?.title).toBe('Test Post');
  });
  
  it('should cascade delete posts when user is deleted', async (): Promise<void> => {
    const userId = await createUser({ name: 'John', email: 'john@example.com' });
    await createPost({ userId, title: 'Test Post', content: 'Content' });
    
    await deleteUser(userId);
    
    const posts = await getPostsByUserId(userId);
    expect(posts).toHaveLength(0);
  });
});
```

## 4. 事务测试

### 4.1 事务成功

```ts
describe('Transactions', () => {
  it('should commit transaction', async (): Promise<void> => {
    const client = await testDb.connect();
    
    try {
      await client.query('BEGIN');
      
      await client.query(
        'INSERT INTO users (name, email) VALUES ($1, $2)',
        ['John', 'john@example.com']
      );
      
      await client.query('COMMIT');
      
      const result = await testDb.query('SELECT * FROM users WHERE email = $1', ['john@example.com']);
      expect(result.rows).toHaveLength(1);
    } finally {
      client.release();
    }
  });
  
  it('should rollback transaction on error', async (): Promise<void> => {
    const client = await testDb.connect();
    
    try {
      await client.query('BEGIN');
      
      await client.query(
        'INSERT INTO users (name, email) VALUES ($1, $2)',
        ['John', 'john@example.com']
      );
      
      // 模拟错误
      await client.query('INSERT INTO users (name, email) VALUES ($1, $2)', ['John', 'john@example.com']); // 重复 email
      
      await client.query('COMMIT');
    } catch (error) {
      await client.query('ROLLBACK');
    } finally {
      client.release();
    }
    
    const result = await testDb.query('SELECT * FROM users WHERE email = $1', ['john@example.com']);
    expect(result.rows).toHaveLength(0); // 应该回滚
  });
});
```

## 5. 约束测试

### 5.1 唯一约束

```ts
describe('Constraints', () => {
  it('should enforce unique email', async (): Promise<void> => {
    await createUser({ name: 'John', email: 'john@example.com' });
    
    await expect(
      createUser({ name: 'Jane', email: 'john@example.com' })
    ).rejects.toThrow();
  });
  
  it('should enforce foreign key', async (): Promise<void> => {
    await expect(
      createPost({ userId: 999, title: 'Test', content: 'Content' })
    ).rejects.toThrow();
  });
});
```

## 6. 性能测试

### 6.1 查询性能

```ts
describe('Performance', () => {
  it('should query users efficiently', async (): Promise<void> => {
    // 创建测试数据
    for (let i = 0; i < 1000; i++) {
      await createUser({ name: `User${i}`, email: `user${i}@example.com` });
    }
    
    const start = Date.now();
    const users = await listUsers({ limit: 100, offset: 0 });
    const duration = Date.now() - start;
    
    expect(duration).toBeLessThan(100); // 100ms
    expect(users).toHaveLength(100);
  });
});
```

## 7. 最佳实践

### 7.1 测试组织

- 使用事务隔离
- 清理测试数据
- 准备测试数据
- 测试约束和关系

### 7.2 性能考虑

- 使用索引
- 优化查询
- 批量操作
- 并行执行

## 8. 注意事项

- **环境隔离**：使用独立的测试数据库
- **数据清理**：及时清理测试数据
- **事务管理**：正确管理事务
- **性能优化**：优化数据库查询

## 9. 常见问题

### 9.1 如何处理测试数据库？

使用独立的测试数据库，使用事务或清理机制。

### 9.2 如何测试事务？

使用事务回滚机制，测试提交和回滚。

### 9.3 如何优化测试性能？

使用索引、优化查询、并行执行。

## 10. 实践任务

1. **数据库测试**：编写数据库集成测试
2. **事务测试**：测试事务功能
3. **约束测试**：测试数据库约束
4. **关系测试**：测试数据关系
5. **性能测试**：进行性能测试

---

**下一章**：[7.4 E2E 测试](../chapter-04-e2e/readme.md)
