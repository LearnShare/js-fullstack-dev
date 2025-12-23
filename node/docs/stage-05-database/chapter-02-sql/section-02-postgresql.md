# 5.2.2 PostgreSQL（推荐）

## 1. 概述

PostgreSQL 是一个功能强大的开源关系型数据库，具有丰富的特性、良好的标准兼容性和强大的扩展能力。PostgreSQL 适合复杂查询、大数据量和企业级应用。

## 2. 特性说明

- **功能强大**：支持复杂查询和高级特性
- **标准兼容**：高度兼容 SQL 标准
- **扩展性强**：支持自定义函数和扩展
- **开源免费**：完全开源免费

## 3. 安装与连接

### 3.1 安装

```bash
# macOS
brew install postgresql

# Ubuntu
sudo apt-get install postgresql

# Windows
# 下载安装包从官网安装
```

### 3.2 Node.js 连接

```bash
npm install pg
npm install @types/pg -D
```

```ts
import { Pool, PoolClient } from 'pg';

const pool = new Pool({
  host: 'localhost',
  port: 5432,
  database: 'mydb',
  user: 'postgres',
  password: 'password',
  max: 20,
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 2000
});

async function queryDatabase(): Promise<void> {
  const client: PoolClient = await pool.connect();
  try {
    const result = await client.query('SELECT * FROM users WHERE id = $1', [1]);
    console.log(result.rows);
  } finally {
    client.release();
  }
}
```

## 4. 基本操作

### 4.1 创建表

```ts
async function createTable(): Promise<void> {
  const client = await pool.connect();
  try {
    await client.query(`
      CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      )
    `);
  } finally {
    client.release();
  }
}
```

### 4.2 插入数据

```ts
async function insertUser(name: string, email: string): Promise<number> {
  const client = await pool.connect();
  try {
    const result = await client.query(
      'INSERT INTO users (name, email) VALUES ($1, $2) RETURNING id',
      [name, email]
    );
    return result.rows[0].id;
  } finally {
    client.release();
  }
}
```

### 4.3 查询数据

```ts
interface User {
  id: number;
  name: string;
  email: string;
  created_at: Date;
}

async function getUserById(id: number): Promise<User | null> {
  const client = await pool.connect();
  try {
    const result = await client.query<User>(
      'SELECT * FROM users WHERE id = $1',
      [id]
    );
    return result.rows[0] || null;
  } finally {
    client.release();
  }
}

async function getUsers(limit: number = 10, offset: number = 0): Promise<User[]> {
  const client = await pool.connect();
  try {
    const result = await client.query<User>(
      'SELECT * FROM users ORDER BY id LIMIT $1 OFFSET $2',
      [limit, offset]
    );
    return result.rows;
  } finally {
    client.release();
  }
}
```

### 4.4 更新数据

```ts
async function updateUser(id: number, name: string, email: string): Promise<boolean> {
  const client = await pool.connect();
  try {
    const result = await client.query(
      'UPDATE users SET name = $1, email = $2 WHERE id = $3',
      [name, email, id]
    );
    return result.rowCount === 1;
  } finally {
    client.release();
  }
}
```

### 4.5 删除数据

```ts
async function deleteUser(id: number): Promise<boolean> {
  const client = await pool.connect();
  try {
    const result = await client.query('DELETE FROM users WHERE id = $1', [id]);
    return result.rowCount === 1;
  } finally {
    client.release();
  }
}
```

## 5. 事务处理

### 5.1 基本事务

```ts
async function transferFunds(fromId: number, toId: number, amount: number): Promise<void> {
  const client = await pool.connect();
  try {
    await client.query('BEGIN');
    
    await client.query(
      'UPDATE accounts SET balance = balance - $1 WHERE id = $2',
      [amount, fromId]
    );
    
    await client.query(
      'UPDATE accounts SET balance = balance + $1 WHERE id = $2',
      [amount, toId]
    );
    
    await client.query('COMMIT');
  } catch (error) {
    await client.query('ROLLBACK');
    throw error;
  } finally {
    client.release();
  }
}
```

## 6. 高级特性

### 6.1 JSON 支持

```ts
async function storeJsonData(): Promise<void> {
  const client = await pool.connect();
  try {
    await client.query(`
      CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        attributes JSONB
      )
    `);
    
    await client.query(
      'INSERT INTO products (name, attributes) VALUES ($1, $2)',
      ['Product 1', JSON.stringify({ color: 'red', size: 'large' })]
    );
    
    const result = await client.query(
      "SELECT * FROM products WHERE attributes->>'color' = 'red'"
    );
    console.log(result.rows);
  } finally {
    client.release();
  }
}
```

### 6.2 全文搜索

```ts
async function fullTextSearch(): Promise<void> {
  const client = await pool.connect();
  try {
    await client.query(`
      CREATE TABLE IF NOT EXISTS articles (
        id SERIAL PRIMARY KEY,
        title VARCHAR(200),
        content TEXT,
        search_vector tsvector
      )
    `);
    
    await client.query(`
      CREATE INDEX idx_search_vector ON articles USING GIN(search_vector)
    `);
    
    await client.query(`
      UPDATE articles SET search_vector = 
        to_tsvector('english', title || ' ' || content)
    `);
    
    const result = await client.query(`
      SELECT * FROM articles 
      WHERE search_vector @@ to_tsquery('english', 'search & term')
    `);
    console.log(result.rows);
  } finally {
    client.release();
  }
}
```

## 7. 最佳实践

### 7.1 连接管理

- 使用连接池管理连接
- 及时释放连接
- 设置合理的连接池大小
- 处理连接错误

### 7.2 查询优化

- 使用参数化查询防止 SQL 注入
- 合理使用索引
- 优化查询语句
- 使用 EXPLAIN 分析查询

### 7.3 错误处理

- 正确处理数据库错误
- 实现重试机制
- 记录错误日志
- 处理连接超时

## 8. 注意事项

- **SQL 注入**：使用参数化查询
- **连接管理**：合理管理数据库连接
- **性能优化**：优化查询和索引
- **错误处理**：实现完善的错误处理

## 9. 常见问题

### 9.1 如何处理连接池？

使用 `pg.Pool` 管理连接池，设置合理的连接数。

### 9.2 如何防止 SQL 注入？

使用参数化查询，避免字符串拼接。

### 9.3 如何优化查询性能？

使用索引、优化查询语句、使用 EXPLAIN 分析。

## 10. 实践任务

1. **连接数据库**：建立 PostgreSQL 连接
2. **基本操作**：实现 CRUD 操作
3. **事务处理**：实现事务操作
4. **高级特性**：使用 JSON 和全文搜索
5. **性能优化**：优化查询和索引

---

**下一节**：[5.2.3 MySQL](section-03-mysql.md)
