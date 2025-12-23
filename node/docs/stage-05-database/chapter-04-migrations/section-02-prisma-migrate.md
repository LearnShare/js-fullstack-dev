# 5.4.2 Prisma Migrate

## 1. 概述

Prisma Migrate 是 Prisma 的数据库迁移工具，可以自动生成迁移文件并管理数据库结构变更。Prisma Migrate 提供了类型安全和自动化的迁移流程。

## 2. 基本使用

### 2.1 创建迁移

```bash
# 开发环境：创建并应用迁移
npx prisma migrate dev --name add_user_table

# 生产环境：创建迁移文件
npx prisma migrate dev --create-only --name add_user_table
```

### 2.2 应用迁移

```bash
# 应用所有待应用的迁移
npx prisma migrate deploy
```

### 2.3 重置数据库

```bash
# 重置数据库并应用所有迁移
npx prisma migrate reset
```

## 3. 迁移文件

### 3.1 迁移文件结构

```
prisma/
├── migrations/
│   ├── 20231222000000_add_user_table/
│   │   └── migration.sql
│   └── migration_lock.toml
└── schema.prisma
```

### 3.2 迁移 SQL

```sql
-- CreateTable
CREATE TABLE "users" (
    "id" SERIAL NOT NULL,
    "name" VARCHAR(100) NOT NULL,
    "email" VARCHAR(100) NOT NULL,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "users_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "users_email_key" ON "users"("email");
```

## 4. 迁移工作流

### 4.1 开发环境

```bash
# 1. 修改 schema.prisma
# 2. 创建迁移
npx prisma migrate dev --name migration_name
# 3. 自动生成客户端
npx prisma generate
```

### 4.2 生产环境

```bash
# 1. 创建迁移（不应用）
npx prisma migrate dev --create-only --name migration_name
# 2. 检查迁移文件
# 3. 应用迁移
npx prisma migrate deploy
```

## 5. 数据迁移

### 5.1 编写数据迁移

```ts
// prisma/migrations/20231222000000_add_default_users/migration.sql
INSERT INTO "users" ("name", "email") VALUES
  ('John Doe', 'john@example.com'),
  ('Jane Doe', 'jane@example.com');
```

## 6. 最佳实践

### 6.1 迁移命名

- 使用描述性名称
- 包含变更内容
- 遵循命名规范

### 6.2 迁移审查

- 检查生成的 SQL
- 测试迁移脚本
- 准备回滚方案

## 7. 注意事项

- **备份数据**：迁移前备份数据
- **测试迁移**：充分测试迁移脚本
- **版本控制**：使用版本控制管理迁移
- **生产环境**：生产环境使用 `migrate deploy`

## 8. 常见问题

### 8.1 如何处理迁移冲突？

解决 Schema 冲突，重新生成迁移。

### 8.2 如何回滚迁移？

手动编写回滚 SQL 或使用数据库备份恢复。

### 8.3 如何处理数据迁移？

在迁移文件中编写数据迁移 SQL。

## 9. 实践任务

1. **创建迁移**：创建数据库结构迁移
2. **应用迁移**：在开发和生产环境应用迁移
3. **数据迁移**：编写数据迁移脚本
4. **迁移管理**：管理迁移版本和状态
5. **最佳实践**：遵循迁移最佳实践

---

**下一节**：[5.4.3 TypeORM Migrations](section-03-typeorm-migrations.md)
