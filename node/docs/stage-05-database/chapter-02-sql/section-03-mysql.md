# 5.2.3 MySQL

## 1. 概述

MySQL 是一个广泛使用的开源关系型数据库，具有优秀的性能、易于使用和活跃的社区。MySQL 适合 Web 应用、中小型应用和高并发场景。

## 2. 特性说明

- **性能优秀**：查询性能优秀
- **易于使用**：简单易学
- **广泛使用**：社区活跃，生态完善
- **高可用**：支持主从复制和集群

## 3. 安装与连接

### 3.1 安装

```bash
# macOS
brew install mysql

# Ubuntu
sudo apt-get install mysql-server

# Windows
# 下载安装包从官网安装
```

### 3.2 Node.js 连接

```bash
npm install mysql2
npm install @types/mysql2 -D
```

```ts
import { createPool, Pool, PoolConnection } from 'mysql2/promise';

const pool: Pool = createPool({
  host: 'localhost',
  port: 3306,
  database: 'mydb',
  user: 'root',
  password: 'password',
  waitForConnections: true,
  connectionLimit: 10,
  queueLimit: 0
});

async function queryDatabase(): Promise<void> {
  const connection: PoolConnection = await pool.getConnection();
  try {
    const [rows] = await connection.query('SELECT * FROM users WHERE id = ?', [1]);
    console.log(rows);
  } finally {
    connection.release();
  }
}
```

## 4. 基本操作

### 4.1 创建表

```ts
async function createTable(): Promise<void> {
  const connection = await pool.getConnection();
  try {
    await connection.query(`
      CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      )
    `);
  } finally {
    connection.release();
  }
}
```

### 4.2 插入数据

```ts
async function insertUser(name: string, email: string): Promise<number> {
  const connection = await pool.getConnection();
  try {
    const [result] = await connection.query(
      'INSERT INTO users (name, email) VALUES (?, ?)',
      [name, email]
    ) as any;
    return result.insertId;
  } finally {
    connection.release();
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
  const connection = await pool.getConnection();
  try {
    const [rows] = await connection.query<User[]>(
      'SELECT * FROM users WHERE id = ?',
      [id]
    );
    return rows[0] || null;
  } finally {
    connection.release();
  }
}

async function getUsers(limit: number = 10, offset: number = 0): Promise<User[]> {
  const connection = await pool.getConnection();
  try {
    const [rows] = await connection.query<User[]>(
      'SELECT * FROM users ORDER BY id LIMIT ? OFFSET ?',
      [limit, offset]
    );
    return rows;
  } finally {
    connection.release();
  }
}
```

### 4.4 更新数据

```ts
async function updateUser(id: number, name: string, email: string): Promise<boolean> {
  const connection = await pool.getConnection();
  try {
    const [result] = await connection.query(
      'UPDATE users SET name = ?, email = ? WHERE id = ?',
      [name, email, id]
    ) as any;
    return result.affectedRows === 1;
  } finally {
    connection.release();
  }
}
```

### 4.5 删除数据

```ts
async function deleteUser(id: number): Promise<boolean> {
  const connection = await pool.getConnection();
  try {
    const [result] = await connection.query(
      'DELETE FROM users WHERE id = ?',
      [id]
    ) as any;
    return result.affectedRows === 1;
  } finally {
    connection.release();
  }
}
```

## 5. 事务处理

### 5.1 基本事务

```ts
async function transferFunds(fromId: number, toId: number, amount: number): Promise<void> {
  const connection = await pool.getConnection();
  try {
    await connection.beginTransaction();
    
    await connection.query(
      'UPDATE accounts SET balance = balance - ? WHERE id = ?',
      [amount, fromId]
    );
    
    await connection.query(
      'UPDATE accounts SET balance = balance + ? WHERE id = ?',
      [amount, toId]
    );
    
    await connection.commit();
  } catch (error) {
    await connection.rollback();
    throw error;
  } finally {
    connection.release();
  }
}
```

## 6. 存储引擎

### 6.1 InnoDB

**特点**：
- 支持事务
- 支持外键
- 行级锁
- 崩溃恢复

**适用场景**：
- 需要事务支持
- 需要外键约束
- 高并发写入

### 6.2 MyISAM

**特点**：
- 不支持事务
- 表级锁
- 查询性能好
- 不支持外键

**适用场景**：
- 只读或读多写少
- 不需要事务
- 简单查询

## 7. 最佳实践

### 7.1 连接管理

- 使用连接池管理连接
- 及时释放连接
- 设置合理的连接池大小
- 处理连接错误

### 7.2 查询优化

- 使用参数化查询
- 合理使用索引
- 优化查询语句
- 使用 EXPLAIN 分析

### 7.3 存储引擎选择

- 默认使用 InnoDB
- 根据场景选择存储引擎
- 考虑事务需求
- 考虑性能需求

## 8. 注意事项

- **SQL 注入**：使用参数化查询
- **连接管理**：合理管理数据库连接
- **性能优化**：优化查询和索引
- **存储引擎**：选择合适的存储引擎

## 9. 常见问题

### 9.1 如何选择存储引擎？

需要事务和外键用 InnoDB，只读场景用 MyISAM。

### 9.2 如何处理连接池？

使用 `mysql2` 的连接池，设置合理的连接数。

### 9.3 如何优化查询性能？

使用索引、优化查询语句、使用 EXPLAIN 分析。

## 10. 实践任务

1. **连接数据库**：建立 MySQL 连接
2. **基本操作**：实现 CRUD 操作
3. **事务处理**：实现事务操作
4. **存储引擎**：选择合适的存储引擎
5. **性能优化**：优化查询和索引

---

**下一节**：[5.2.4 SQLite](section-04-sqlite.md)
