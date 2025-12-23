# 5.3.4 TypeORM 简介

## 1. 概述

TypeORM 是一个功能丰富的 ORM 框架，使用装饰器语法定义模型，支持多种数据库。TypeORM 适合需要丰富功能和装饰器语法的项目。

## 2. 特性说明

- **装饰器语法**：使用装饰器定义模型
- **功能丰富**：提供丰富的 ORM 功能
- **多数据库支持**：支持多种关系型数据库
- **Active Record 和 Data Mapper**：支持两种模式

## 3. 安装与初始化

### 3.1 安装

```bash
npm install typeorm reflect-metadata
npm install pg
npm install @types/pg -D
```

### 3.2 实体定义

```ts
import { Entity, PrimaryGeneratedColumn, Column, CreateDateColumn, UpdateDateColumn, OneToMany } from 'typeorm';
import { Post } from './Post';

@Entity('users')
export class User {
  @PrimaryGeneratedColumn()
  id!: number;

  @Column({ length: 100 })
  name!: string;

  @Column({ unique: true, length: 100 })
  email!: string;

  @OneToMany(() => Post, (post: Post) => post.author)
  posts!: Post[];

  @CreateDateColumn()
  createdAt!: Date;

  @UpdateDateColumn()
  updatedAt!: Date;
}
```

### 3.3 数据源配置

```ts
import { DataSource } from 'typeorm';
import { User } from './entity/User';
import { Post } from './entity/Post';

export const AppDataSource = new DataSource({
  type: 'postgres',
  host: 'localhost',
  port: 5432,
  username: 'postgres',
  password: 'password',
  database: 'mydb',
  entities: [User, Post],
  synchronize: false,
  logging: true
});

await AppDataSource.initialize();
```

## 4. 基本操作

### 4.1 创建数据

```ts
import { AppDataSource } from './data-source';
import { User } from './entity/User';

async function createUser(name: string, email: string): Promise<void> {
  const userRepository = AppDataSource.getRepository(User);
  const user = userRepository.create({ name, email });
  await userRepository.save(user);
  console.log('Created user:', user);
}
```

### 4.2 查询数据

```ts
// 查询单个
async function getUserById(id: number): Promise<User | null> {
  const userRepository = AppDataSource.getRepository(User);
  return await userRepository.findOne({ where: { id } });
}

// 查询多个
async function getUsers(): Promise<User[]> {
  const userRepository = AppDataSource.getRepository(User);
  return await userRepository.find({
    where: { email: Like('%@example.com') },
    order: { createdAt: 'DESC' },
    take: 10
  });
}
```

### 4.3 更新数据

```ts
async function updateUser(id: number, name: string): Promise<void> {
  const userRepository = AppDataSource.getRepository(User);
  await userRepository.update(id, { name });
}
```

### 4.4 删除数据

```ts
async function deleteUser(id: number): Promise<void> {
  const userRepository = AppDataSource.getRepository(User);
  await userRepository.delete(id);
}
```

## 5. 关联查询

### 5.1 预加载关联

```ts
async function getUserWithPosts(id: number): Promise<User | null> {
  const userRepository = AppDataSource.getRepository(User);
  return await userRepository.findOne({
    where: { id },
    relations: ['posts']
  });
}
```

## 6. 查询构建器

```ts
async function getUsersWithPosts(): Promise<User[]> {
  const userRepository = AppDataSource.getRepository(User);
  return await userRepository
    .createQueryBuilder('user')
    .leftJoinAndSelect('user.posts', 'post')
    .where('user.email LIKE :email', { email: '%@example.com' })
    .getMany();
}
```

## 7. 最佳实践

### 7.1 实体设计

- 使用装饰器定义实体
- 合理使用关系
- 添加索引
- 使用类型定义

### 7.2 查询优化

- 使用索引
- 预加载关联
- 使用查询构建器
- 避免 N+1 查询

## 8. 注意事项

- **装饰器**：需要启用装饰器支持
- **性能**：注意查询性能优化
- **迁移**：使用 TypeORM Migrations
- **同步**：生产环境禁用 synchronize

## 9. 常见问题

### 9.1 如何处理迁移？

使用 TypeORM Migrations 创建和应用迁移。

### 9.2 如何优化查询性能？

使用索引、预加载关联、优化查询构建器。

### 9.3 何时使用 Active Record？

简单场景使用 Active Record，复杂场景使用 Data Mapper。

## 10. 实践任务

1. **初始化 TypeORM**：初始化 TypeORM 项目
2. **定义实体**：使用装饰器定义实体
3. **基本操作**：实现 CRUD 操作
4. **关联查询**：实现关联数据查询
5. **迁移管理**：使用 TypeORM Migrations 管理数据库

---

**下一节**：[5.3.5 Sequelize 简介](section-05-sequelize.md)
