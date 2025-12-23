# 5.3.6 其他 ORM 框架

## 1. 概述

除了主流的 ORM 框架，还有一些其他的 ORM 框架，各有特色和适用场景。了解这些框架有助于根据项目需求选择合适的工具。

## 2. 其他 ORM 框架

### 2.1 Kysely

**特点**：
- SQL-like 语法
- 类型安全
- 轻量级
- 查询构建器

**适用场景**：
- 需要 SQL-like 语法
- TypeScript 项目
- 性能要求高

**示例**：
```ts
import { Kysely, PostgresAdapter } from 'kysely';

interface Database {
  users: {
    id: number;
    name: string;
    email: string;
  };
}

const db = new Kysely<Database>({
  dialect: new PostgresAdapter({
    pool: new Pool({ connectionString: process.env.DATABASE_URL })
  })
});

const users = await db.selectFrom('users')
  .selectAll()
  .where('email', 'like', '%@example.com')
  .execute();
```

### 2.2 Objection.js

**特点**：
- 基于 Knex.js
- 关系查询
- 插件系统
- 灵活查询

**适用场景**：
- 需要灵活查询
- 关系查询复杂
- 基于 Knex.js 的项目

### 2.3 MikroORM

**特点**：
- 装饰器语法
- 单元工作模式
- 类型安全
- 多数据库支持

**适用场景**：
- 需要装饰器语法
- 单元工作模式
- TypeScript 项目

## 3. 框架选择建议

### 3.1 根据项目需求

- **类型安全优先**：Prisma、Drizzle
- **SQL-like 语法**：Drizzle、Kysely
- **装饰器语法**：TypeORM、MikroORM
- **成熟稳定**：Sequelize、TypeORM

### 3.2 根据团队经验

- 熟悉 SQL：Drizzle、Kysely
- 熟悉装饰器：TypeORM、MikroORM
- 需要简单：Prisma
- 需要灵活：Sequelize

## 4. 注意事项

- **学习成本**：考虑团队学习成本
- **生态支持**：考虑框架生态
- **性能要求**：考虑性能需求
- **长期维护**：考虑框架维护情况

## 5. 常见问题

### 5.1 如何选择 ORM 框架？

根据项目需求、团队经验、性能要求选择。

### 5.2 可以混用多个 ORM 吗？

可以，但不推荐，会增加复杂度。

### 5.3 何时不使用 ORM？

复杂查询、性能要求极高、需要原生 SQL 的场景。

## 6. 实践任务

1. **了解其他框架**：了解 Kysely、Objection.js、MikroORM
2. **对比框架**：对比不同框架的特点
3. **选择框架**：根据项目需求选择合适的框架
4. **迁移框架**：了解框架迁移的方法
5. **最佳实践**：遵循 ORM 使用最佳实践

---

**下一章**：[5.4 数据库迁移](../chapter-04-migrations/readme.md)
