# 5.3.2 Prisma 简介

## 1. 概述

Prisma 是一个现代化的 ORM 框架，提供了类型安全的数据库访问、代码生成和强大的迁移工具。Prisma 适合 TypeScript 项目和需要类型安全的场景。

## 2. 特性说明

- **类型安全**：完整的 TypeScript 类型支持
- **代码生成**：自动生成类型和客户端
- **迁移工具**：强大的数据库迁移支持
- **现代化设计**：简洁的 API 设计

## 3. 安装与初始化

### 3.1 安装

```bash
npm install prisma @prisma/client
npm install -D prisma
```

### 3.2 初始化

```bash
npx prisma init
```

### 3.3 Schema 定义

```prisma
// prisma/schema.prisma
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model User {
  id        Int      @id @default(autoincrement())
  name      String
  email     String   @unique
  posts     Post[]
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
}

model Post {
  id        Int      @id @default(autoincrement())
  title     String
  content   String?
  published Boolean  @default(false)
  author    User     @relation(fields: [authorId], references: [id])
  authorId  Int
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
}
```

## 4. 基本操作

### 4.1 客户端初始化

```ts
import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

// 关闭连接
async function disconnect(): Promise<void> {
  await prisma.$disconnect();
}
```

### 4.2 创建数据

```ts
async function createUser(name: string, email: string): Promise<void> {
  const user = await prisma.user.create({
    data: {
      name,
      email
    }
  });
  console.log('Created user:', user);
}

// 创建关联数据
async function createUserWithPosts(name: string, email: string): Promise<void> {
  const user = await prisma.user.create({
    data: {
      name,
      email,
      posts: {
        create: [
          { title: 'Post 1', content: 'Content 1' },
          { title: 'Post 2', content: 'Content 2' }
        ]
      }
    },
    include: {
      posts: true
    }
  });
  console.log('Created user with posts:', user);
}
```

### 4.3 查询数据

```ts
// 查询单个
async function getUserById(id: number): Promise<void> {
  const user = await prisma.user.findUnique({
    where: { id },
    include: { posts: true }
  });
  console.log('User:', user);
}

// 查询多个
async function getUsers(): Promise<void> {
  const users = await prisma.user.findMany({
    where: {
      email: {
        contains: '@example.com'
      }
    },
    orderBy: {
      createdAt: 'desc'
    },
    take: 10,
    skip: 0
  });
  console.log('Users:', users);
}
```

### 4.4 更新数据

```ts
async function updateUser(id: number, name: string): Promise<void> {
  const user = await prisma.user.update({
    where: { id },
    data: { name }
  });
  console.log('Updated user:', user);
}

// 更新多个
async function updateManyUsers(): Promise<void> {
  const result = await prisma.user.updateMany({
    where: {
      email: {
        contains: '@example.com'
      }
    },
    data: {
      name: 'Updated Name'
    }
  });
  console.log('Updated count:', result.count);
}
```

### 4.5 删除数据

```ts
async function deleteUser(id: number): Promise<void> {
  const user = await prisma.user.delete({
    where: { id }
  });
  console.log('Deleted user:', user);
}

// 删除多个
async function deleteManyUsers(): Promise<void> {
  const result = await prisma.user.deleteMany({
    where: {
      email: {
        contains: '@example.com'
      }
    }
  });
  console.log('Deleted count:', result.count);
}
```

## 5. 高级查询

### 5.1 关联查询

```ts
async function getUserWithPosts(id: number): Promise<void> {
  const user = await prisma.user.findUnique({
    where: { id },
    include: {
      posts: {
        where: {
          published: true
        },
        orderBy: {
          createdAt: 'desc'
        }
      }
    }
  });
  console.log('User with posts:', user);
}
```

### 5.2 聚合查询

```ts
async function getUserStats(): Promise<void> {
  const stats = await prisma.user.aggregate({
    _count: {
      id: true
    },
    _avg: {
      id: true
    },
    _max: {
      id: true
    },
    _min: {
      id: true
    }
  });
  console.log('Stats:', stats);
}
```

### 5.3 事务

```ts
async function transferPosts(fromUserId: number, toUserId: number): Promise<void> {
  await prisma.$transaction(async (tx) => {
    await tx.post.updateMany({
      where: { authorId: fromUserId },
      data: { authorId: toUserId }
    });
  });
}
```

## 6. 最佳实践

### 6.1 客户端管理

- 使用单例模式
- 正确关闭连接
- 处理连接错误
- 使用连接池

### 6.2 查询优化

- 使用 select 选择字段
- 使用 include 预加载关联
- 避免 N+1 查询
- 使用索引

### 6.3 类型安全

- 使用生成的类型
- 类型推断
- 类型检查
- 避免 any

## 7. 注意事项

- **代码生成**：修改 Schema 后需要重新生成客户端
- **迁移**：使用 Prisma Migrate 管理迁移
- **性能**：注意查询性能，使用索引
- **类型安全**：充分利用类型系统

## 8. 常见问题

### 8.1 如何生成 Prisma Client？

运行 `npx prisma generate` 生成客户端。

### 8.2 如何处理迁移？

使用 `npx prisma migrate dev` 创建和应用迁移。

### 8.3 如何优化查询性能？

使用 select、include、索引，避免 N+1 查询。

## 9. 实践任务

1. **初始化 Prisma**：初始化 Prisma 项目
2. **定义 Schema**：定义数据模型
3. **基本操作**：实现 CRUD 操作
4. **关联查询**：实现关联数据查询
5. **迁移管理**：使用 Prisma Migrate 管理数据库

---

**下一节**：[5.3.3 Drizzle ORM 简介](section-03-drizzle.md)
