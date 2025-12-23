# 5.4.3 TypeORM Migrations

## 1. 概述

TypeORM Migrations 是 TypeORM 的数据库迁移工具，支持手动编写迁移文件和管理数据库结构变更。TypeORM Migrations 提供了灵活的迁移方式。

## 2. 基本使用

### 2.1 生成迁移

```bash
# 根据实体变更生成迁移
npx typeorm migration:generate -n MigrationName

# 创建空迁移文件
npx typeorm migration:create -n MigrationName
```

### 2.2 运行迁移

```bash
# 运行所有待应用的迁移
npx typeorm migration:run

# 回滚最后一个迁移
npx typeorm migration:revert
```

## 3. 迁移文件

### 3.1 迁移类定义

```ts
import { MigrationInterface, QueryRunner } from 'typeorm';

export class AddUserTable1234567890 implements MigrationInterface {
  name = 'AddUserTable1234567890';

  public async up(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.query(`
      CREATE TABLE "users" (
        "id" SERIAL NOT NULL,
        "name" VARCHAR(100) NOT NULL,
        "email" VARCHAR(100) NOT NULL,
        "created_at" TIMESTAMP NOT NULL DEFAULT now(),
        CONSTRAINT "PK_users" PRIMARY KEY ("id")
      )
    `);
    
    await queryRunner.query(`
      CREATE UNIQUE INDEX "IDX_users_email" ON "users" ("email")
    `);
  }

  public async down(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.query(`DROP INDEX "IDX_users_email"`);
    await queryRunner.query(`DROP TABLE "users"`);
  }
}
```

## 4. 迁移配置

### 4.1 数据源配置

```ts
import { DataSource } from 'typeorm';

export const AppDataSource = new DataSource({
  type: 'postgres',
  host: 'localhost',
  port: 5432,
  username: 'postgres',
  password: 'password',
  database: 'mydb',
  entities: [User, Post],
  migrations: ['src/migrations/*.ts'],
  migrationsTableName: 'migrations',
  synchronize: false
});
```

## 5. 最佳实践

### 5.1 迁移编写

- 实现 up 和 down 方法
- 保持迁移原子性
- 编写可回滚的迁移
- 测试迁移脚本

### 5.2 迁移管理

- 使用版本控制
- 命名规范
- 记录迁移说明
- 团队协作规范

## 6. 注意事项

- **同步模式**：生产环境禁用 synchronize
- **迁移顺序**：确保迁移顺序正确
- **回滚支持**：实现 down 方法支持回滚
- **测试**：充分测试迁移脚本

## 7. 常见问题

### 7.1 如何生成迁移？

根据实体变更自动生成或手动创建。

### 7.2 如何回滚迁移？

使用 `migration:revert` 或手动执行 down 方法。

### 7.3 如何处理数据迁移？

在迁移类中编写数据迁移逻辑。

## 8. 实践任务

1. **创建迁移**：创建数据库结构迁移
2. **应用迁移**：运行迁移脚本
3. **回滚迁移**：回滚迁移操作
4. **数据迁移**：编写数据迁移逻辑
5. **最佳实践**：遵循迁移最佳实践

---

**下一节**：[5.4.4 迁移最佳实践](section-04-best-practices.md)
