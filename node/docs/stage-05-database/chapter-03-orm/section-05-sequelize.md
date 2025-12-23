# 5.3.5 Sequelize 简介

## 1. 概述

Sequelize 是一个成熟稳定的 ORM 框架，支持多种数据库，提供丰富的功能和良好的 TypeScript 支持。Sequelize 适合需要成熟方案和丰富功能的项目。

## 2. 特性说明

- **成熟稳定**：经过长期验证
- **功能完善**：提供丰富的 ORM 功能
- **多数据库支持**：支持多种关系型数据库
- **TypeScript 支持**：良好的 TypeScript 支持

## 3. 安装与初始化

### 3.1 安装

```bash
npm install sequelize
npm install pg pg-hstore
npm install @types/sequelize -D
```

### 3.2 模型定义

```ts
import { Sequelize, DataTypes, Model, Optional } from 'sequelize';

interface UserAttributes {
  id: number;
  name: string;
  email: string;
}

interface UserCreationAttributes extends Optional<UserAttributes, 'id'> {}

class User extends Model<UserAttributes, UserCreationAttributes> implements UserAttributes {
  public id!: number;
  public name!: string;
  public email!: string;
  public readonly createdAt!: Date;
  public readonly updatedAt!: Date;
}

User.init({
  id: {
    type: DataTypes.INTEGER,
    autoIncrement: true,
    primaryKey: true
  },
  name: {
    type: DataTypes.STRING(100),
    allowNull: false
  },
  email: {
    type: DataTypes.STRING(100),
    allowNull: false,
    unique: true
  }
}, {
  sequelize,
  tableName: 'users'
});
```

### 3.3 连接初始化

```ts
import { Sequelize } from 'sequelize';

const sequelize = new Sequelize({
  dialect: 'postgres',
  host: 'localhost',
  port: 5432,
  database: 'mydb',
  username: 'postgres',
  password: 'password',
  logging: console.log
});

await sequelize.authenticate();
```

## 4. 基本操作

### 4.1 创建数据

```ts
async function createUser(name: string, email: string): Promise<User> {
  const user = await User.create({ name, email });
  return user;
}
```

### 4.2 查询数据

```ts
// 查询单个
async function getUserById(id: number): Promise<User | null> {
  return await User.findByPk(id);
}

// 查询多个
async function getUsers(): Promise<User[]> {
  return await User.findAll({
    where: {
      email: {
        [Op.like]: '%@example.com'
      }
    },
    order: [['createdAt', 'DESC']],
    limit: 10
  });
}
```

### 4.3 更新数据

```ts
async function updateUser(id: number, name: string): Promise<void> {
  await User.update({ name }, { where: { id } });
}
```

### 4.4 删除数据

```ts
async function deleteUser(id: number): Promise<void> {
  await User.destroy({ where: { id } });
}
```

## 5. 关联定义

```ts
import { HasMany, BelongsTo } from 'sequelize';

// User 和 Post 一对多
User.hasMany(Post, { foreignKey: 'authorId' });
Post.belongsTo(User, { foreignKey: 'authorId' });
```

## 6. 最佳实践

### 6.1 模型设计

- 使用 TypeScript 类型
- 合理使用关联
- 添加验证
- 使用钩子

### 6.2 查询优化

- 使用索引
- 预加载关联
- 使用事务
- 避免 N+1 查询

## 7. 注意事项

- **类型安全**：使用 TypeScript 类型定义
- **性能**：注意查询性能优化
- **迁移**：使用 Sequelize Migrations
- **连接管理**：合理管理数据库连接

## 8. 常见问题

### 8.1 如何处理迁移？

使用 Sequelize CLI 创建和应用迁移。

### 8.2 如何优化查询性能？

使用索引、预加载关联、优化查询条件。

### 8.3 如何处理关联查询？

使用 include 预加载关联数据。

## 9. 实践任务

1. **初始化 Sequelize**：初始化 Sequelize 项目
2. **定义模型**：定义数据模型
3. **基本操作**：实现 CRUD 操作
4. **关联查询**：实现关联数据查询
5. **迁移管理**：使用 Sequelize Migrations 管理数据库

---

**下一节**：[5.3.6 其他 ORM 框架](section-06-other-orms.md)
