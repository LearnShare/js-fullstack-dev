# 5.3.3 Drizzle ORM 简介

## 1. 概述

Drizzle ORM 是一个轻量级的 TypeScript ORM 框架，提供了 SQL-like 的语法和类型安全。Drizzle ORM 适合需要 SQL-like 语法和性能的场景。

## 2. 特性说明

- **轻量级**：体积小，性能高
- **SQL-like 语法**：接近原生 SQL 的语法
- **类型安全**：完整的 TypeScript 类型支持
- **高性能**：优化的查询性能

## 3. 安装与初始化

### 3.1 安装

```bash
npm install drizzle-orm
npm install drizzle-kit -D
npm install pg
npm install @types/pg -D
```

### 3.2 Schema 定义

```ts
import { pgTable, serial, varchar, timestamp, boolean, integer } from 'drizzle-orm/pg-core';
import { relations } from 'drizzle-orm';

export const users = pgTable('users', {
  id: serial('id').primaryKey(),
  name: varchar('name', { length: 100 }).notNull(),
  email: varchar('email', { length: 100 }).notNull().unique(),
  createdAt: timestamp('created_at').defaultNow().notNull(),
  updatedAt: timestamp('updated_at').defaultNow().notNull()
});

export const posts = pgTable('posts', {
  id: serial('id').primaryKey(),
  title: varchar('title', { length: 200 }).notNull(),
  content: varchar('content', { length: 1000 }),
  published: boolean('published').default(false).notNull(),
  authorId: integer('author_id').references(() => users.id).notNull(),
  createdAt: timestamp('created_at').defaultNow().notNull(),
  updatedAt: timestamp('updated_at').defaultNow().notNull()
});

export const usersRelations = relations(users, ({ many }) => ({
  posts: many(posts)
}));

export const postsRelations = relations(posts, ({ one }) => ({
  author: one(users, {
    fields: [posts.authorId],
    references: [users.id]
  })
}));
```

### 3.3 客户端初始化

```ts
import { drizzle } from 'drizzle-orm/node-postgres';
import { Pool } from 'pg';

const pool = new Pool({
  connectionString: process.env.DATABASE_URL!
});

const db = drizzle(pool);
```

## 4. 基本操作

### 4.1 创建数据

```ts
import { users } from './schema';

async function createUser(name: string, email: string): Promise<void> {
  const [user] = await db.insert(users).values({
    name,
    email
  }).returning();
  console.log('Created user:', user);
}
```

### 4.2 查询数据

```ts
import { eq, like, desc } from 'drizzle-orm';

// 查询单个
async function getUserById(id: number): Promise<void> {
  const [user] = await db.select().from(users).where(eq(users.id, id));
  console.log('User:', user);
}

// 查询多个
async function getUsers(): Promise<void> {
  const userList = await db.select().from(users)
    .where(like(users.email, '%@example.com'))
    .orderBy(desc(users.createdAt))
    .limit(10);
  console.log('Users:', userList);
}
```

### 4.3 更新数据

```ts
async function updateUser(id: number, name: string): Promise<void> {
  const [user] = await db.update(users)
    .set({ name })
    .where(eq(users.id, id))
    .returning();
  console.log('Updated user:', user);
}
```

### 4.4 删除数据

```ts
async function deleteUser(id: number): Promise<void> {
  await db.delete(users).where(eq(users.id, id));
}
```

## 5. 关联查询

### 5.1 JOIN 查询

```ts
import { users, posts } from './schema';

async function getUserWithPosts(id: number): Promise<void> {
  const result = await db.select({
    user: users,
    post: posts
  })
    .from(users)
    .leftJoin(posts, eq(users.id, posts.authorId))
    .where(eq(users.id, id));
  console.log('User with posts:', result);
}
```

## 6. 最佳实践

### 6.1 查询优化

- 使用索引
- 选择需要的字段
- 使用预编译查询
- 批量操作

### 6.2 类型安全

- 使用类型推断
- 定义明确的类型
- 使用类型检查
- 避免 any

## 7. 注意事项

- **SQL-like 语法**：需要熟悉 SQL 语法
- **性能**：注意查询性能优化
- **类型安全**：充分利用类型系统
- **迁移**：使用 Drizzle Kit 管理迁移

## 8. 常见问题

### 8.1 如何管理迁移？

使用 Drizzle Kit 生成和应用迁移。

### 8.2 如何优化查询性能？

使用索引、选择字段、批量操作。

### 8.3 如何处理复杂查询？

使用原生 SQL 或组合多个查询。

## 9. 实践任务

1. **初始化 Drizzle**：初始化 Drizzle 项目
2. **定义 Schema**：定义数据模型
3. **基本操作**：实现 CRUD 操作
4. **关联查询**：实现关联数据查询
5. **迁移管理**：使用 Drizzle Kit 管理数据库

---

**下一节**：[5.3.4 TypeORM 简介](section-04-typeorm.md)
