# 5.2.4 SQLite

## 1. 概述

SQLite 是一个轻量级的嵌入式关系型数据库，无需独立的服务器进程，数据存储在单个文件中。SQLite 适合小型应用、移动应用和开发测试场景。

## 2. 特性说明

- **轻量级**：体积小，资源占用少
- **嵌入式**：无需独立服务器
- **零配置**：无需配置即可使用
- **单文件**：数据存储在单个文件

## 3. 安装与连接

### 3.1 安装

```bash
# macOS（通常已预装）
# 或使用 Homebrew
brew install sqlite

# Ubuntu
sudo apt-get install sqlite3

# Windows
# 下载预编译二进制文件
```

### 3.2 Node.js 连接

```bash
npm install better-sqlite3
npm install @types/better-sqlite3 -D
```

```ts
import Database from 'better-sqlite3';

const db: Database.Database = new Database('mydb.sqlite');

// 启用外键约束
db.pragma('foreign_keys = ON');

// 关闭连接
db.close();
```

## 4. 基本操作

### 4.1 创建表

```ts
function createTable(): void {
  db.exec(`
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      email TEXT UNIQUE NOT NULL,
      created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
  `);
}
```

### 4.2 插入数据

```ts
function insertUser(name: string, email: string): number {
  const stmt = db.prepare('INSERT INTO users (name, email) VALUES (?, ?)');
  const result = stmt.run(name, email);
  return result.lastInsertRowid as number;
}

// 批量插入
function insertUsers(users: Array<{ name: string; email: string }>): void {
  const stmt = db.prepare('INSERT INTO users (name, email) VALUES (?, ?)');
  const insertMany = db.transaction((users: Array<{ name: string; email: string }>): void => {
    for (const user of users) {
      stmt.run(user.name, user.email);
    }
  });
  insertMany(users);
}
```

### 4.3 查询数据

```ts
interface User {
  id: number;
  name: string;
  email: string;
  created_at: string;
}

function getUserById(id: number): User | undefined {
  const stmt = db.prepare('SELECT * FROM users WHERE id = ?');
  return stmt.get(id) as User | undefined;
}

function getUsers(limit: number = 10, offset: number = 0): User[] {
  const stmt = db.prepare('SELECT * FROM users ORDER BY id LIMIT ? OFFSET ?');
  return stmt.all(limit, offset) as User[];
}
```

### 4.4 更新数据

```ts
function updateUser(id: number, name: string, email: string): boolean {
  const stmt = db.prepare('UPDATE users SET name = ?, email = ? WHERE id = ?');
  const result = stmt.run(name, email, id);
  return result.changes === 1;
}
```

### 4.5 删除数据

```ts
function deleteUser(id: number): boolean {
  const stmt = db.prepare('DELETE FROM users WHERE id = ?');
  const result = stmt.run(id);
  return result.changes === 1;
}
```

## 5. 事务处理

### 5.1 基本事务

```ts
function transferFunds(fromId: number, toId: number, amount: number): void {
  const transfer = db.transaction((fromId: number, toId: number, amount: number): void => {
    const updateFrom = db.prepare('UPDATE accounts SET balance = balance - ? WHERE id = ?');
    const updateTo = db.prepare('UPDATE accounts SET balance = balance + ? WHERE id = ?');
    
    updateFrom.run(amount, fromId);
    updateTo.run(amount, toId);
  });
  
  transfer(fromId, toId, amount);
}
```

## 6. 最佳实践

### 6.1 性能优化

- 使用预编译语句
- 使用事务批量操作
- 合理使用索引
- 定期 VACUUM

### 6.2 数据安全

- 定期备份数据库文件
- 使用 WAL 模式提高并发
- 处理数据库锁定
- 错误处理

### 6.3 使用场景

- 小型应用
- 移动应用
- 开发测试
- 嵌入式系统

## 7. 注意事项

- **并发限制**：SQLite 并发写入性能有限
- **文件大小**：单个数据库文件大小有限制
- **数据类型**：SQLite 数据类型较灵活
- **备份恢复**：备份数据库文件即可

## 8. 常见问题

### 8.1 SQLite 适合生产环境吗？

适合小型应用和读多写少的场景，不适合高并发写入。

### 8.2 如何处理并发？

使用 WAL 模式提高并发性能，注意锁定问题。

### 8.3 如何备份 SQLite？

直接复制数据库文件即可，或使用 `.backup` 命令。

## 9. 实践任务

1. **连接数据库**：建立 SQLite 连接
2. **基本操作**：实现 CRUD 操作
3. **事务处理**：实现事务操作
4. **性能优化**：优化查询和批量操作
5. **备份恢复**：实现数据库备份和恢复

---

**下一章**：[5.3 ORM 框架概览](../chapter-03-orm/readme.md)
