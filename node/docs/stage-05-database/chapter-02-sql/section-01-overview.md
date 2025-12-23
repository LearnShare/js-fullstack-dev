# 5.2.1 关系型数据库概述

## 1. 概述

关系型数据库是基于关系模型的数据库，使用表（Table）存储数据，通过 SQL 语言进行数据操作。关系型数据库具有 ACID 特性，保证数据的一致性和完整性。

## 2. 核心概念

### 2.1 关系模型

- **表（Table）**：数据的二维结构
- **行（Row）**：表中的一条记录
- **列（Column）**：表中的字段
- **主键（Primary Key）**：唯一标识一行
- **外键（Foreign Key）**：关联其他表

### 2.2 ACID 特性

- **原子性（Atomicity）**：事务要么全部执行，要么全部不执行
- **一致性（Consistency）**：事务执行前后数据保持一致
- **隔离性（Isolation）**：并发事务相互隔离
- **持久性（Durability）**：事务提交后数据持久化

## 3. 关系型数据库特点

### 3.1 优势

- **数据一致性**：ACID 特性保证数据一致性
- **标准化**：SQL 标准统一
- **成熟稳定**：技术成熟，生态完善
- **事务支持**：完善的事务支持

### 3.2 劣势

- **扩展性**：水平扩展相对困难
- **性能**：复杂查询性能可能受限
- **灵活性**：表结构相对固定

## 4. 主流关系型数据库

### 4.1 PostgreSQL

**特点**：
- 功能强大
- 标准兼容性好
- 扩展性强
- 开源免费

**适用场景**：
- 复杂查询
- 大数据量
- 企业应用

### 4.2 MySQL

**特点**：
- 使用广泛
- 性能优秀
- 易于使用
- 社区活跃

**适用场景**：
- Web 应用
- 中小型应用
- 高并发场景

### 4.3 SQLite

**特点**：
- 轻量级
- 嵌入式
- 零配置
- 单文件

**适用场景**：
- 小型应用
- 移动应用
- 开发测试

## 5. SQL 语言

### 5.1 DDL（数据定义语言）

```sql
-- 创建表
CREATE TABLE users (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100) UNIQUE
);

-- 修改表
ALTER TABLE users ADD COLUMN age INT;

-- 删除表
DROP TABLE users;
```

### 5.2 DML（数据操作语言）

```sql
-- 插入数据
INSERT INTO users (name, email) VALUES ('John', 'john@example.com');

-- 更新数据
UPDATE users SET name = 'Jane' WHERE id = 1;

-- 删除数据
DELETE FROM users WHERE id = 1;
```

### 5.3 DQL（数据查询语言）

```sql
-- 查询数据
SELECT * FROM users WHERE id = 1;

-- 连接查询
SELECT u.name, o.order_date
FROM users u
JOIN orders o ON u.id = o.user_id;
```

## 6. 关系操作

### 6.1 连接（JOIN）

- **INNER JOIN**：内连接
- **LEFT JOIN**：左连接
- **RIGHT JOIN**：右连接
- **FULL OUTER JOIN**：全外连接

### 6.2 集合操作

- **UNION**：并集
- **INTERSECT**：交集
- **EXCEPT**：差集

## 7. 注意事项

- **性能优化**：合理使用索引和查询优化
- **数据完整性**：使用约束保证数据完整性
- **事务管理**：合理使用事务
- **安全性**：注意 SQL 注入防护

## 8. 常见问题

### 8.1 如何选择关系型数据库？

根据项目需求、性能要求、团队经验选择。

### 8.2 关系型数据库和 NoSQL 的区别？

关系型数据库强调一致性，NoSQL 强调性能和扩展性。

### 8.3 如何优化关系型数据库性能？

使用索引、优化查询、合理设计表结构、使用连接池。

## 9. 相关资源

- [SQL 标准](https://en.wikipedia.org/wiki/SQL)
- [关系模型](https://en.wikipedia.org/wiki/Relational_model)

---

**下一节**：[5.2.2 PostgreSQL（推荐）](section-02-postgresql.md)
