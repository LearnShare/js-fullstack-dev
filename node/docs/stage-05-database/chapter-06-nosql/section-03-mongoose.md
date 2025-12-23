# 5.6.3 Mongoose ODM

## 1. 概述

Mongoose 是 MongoDB 的 ODM（Object Document Mapper），提供了 Schema 定义、模型、验证等功能。Mongoose 简化了 MongoDB 操作，提供了类型安全和数据验证。

## 2. 特性说明

- **Schema 定义**：定义文档结构
- **模型和验证**：数据验证和类型转换
- **中间件**：钩子和中间件支持
- **查询构建**：强大的查询构建器

## 3. 安装与初始化

### 3.1 安装

```bash
npm install mongoose
```

### 3.2 连接数据库

```ts
import mongoose from 'mongoose';

async function connectDatabase(): Promise<void> {
  await mongoose.connect(process.env.MONGODB_URI!);
  console.log('Connected to MongoDB');
}

async function disconnectDatabase(): Promise<void> {
  await mongoose.disconnect();
  console.log('Disconnected from MongoDB');
}
```

## 4. Schema 和模型

### 4.1 Schema 定义

```ts
import { Schema, model, Model } from 'mongoose';

interface IUser {
  name: string;
  email: string;
  age?: number;
  createdAt: Date;
}

const userSchema = new Schema<IUser>({
  name: {
    type: String,
    required: true,
    trim: true
  },
  email: {
    type: String,
    required: true,
    unique: true,
    lowercase: true,
    match: [/^\S+@\S+\.\S+$/, 'Invalid email']
  },
  age: {
    type: Number,
    min: 0,
    max: 150
  },
  createdAt: {
    type: Date,
    default: Date.now
  }
});

const User: Model<IUser> = model<IUser>('User', userSchema);
```

### 4.2 模型使用

```ts
// 创建
async function createUser(name: string, email: string): Promise<IUser> {
  const user = new User({ name, email });
  return await user.save();
}

// 查询
async function getUserById(id: string): Promise<IUser | null> {
  return await User.findById(id);
}

async function getUsers(): Promise<IUser[]> {
  return await User.find({}).sort({ createdAt: -1 }).limit(10);
}

// 更新
async function updateUser(id: string, name: string): Promise<IUser | null> {
  return await User.findByIdAndUpdate(id, { name }, { new: true });
}

// 删除
async function deleteUser(id: string): Promise<IUser | null> {
  return await User.findByIdAndDelete(id);
}
```

## 5. 中间件

### 5.1 保存前钩子

```ts
userSchema.pre('save', async function (next): Promise<void> {
  if (this.isModified('password')) {
    this.password = await hashPassword(this.password);
  }
  next();
});
```

### 5.2 查询后钩子

```ts
userSchema.post('find', function (docs: IUser[]): void {
  console.log(`Found ${docs.length} users`);
});
```

## 6. 关联查询

### 6.1 引用关联

```ts
const postSchema = new Schema({
  title: String,
  content: String,
  author: {
    type: Schema.Types.ObjectId,
    ref: 'User'
  }
});

const Post = model('Post', postSchema);

// 查询时填充关联
const posts = await Post.find({}).populate('author');
```

## 7. 最佳实践

### 7.1 Schema 设计

- 合理设计 Schema
- 使用验证
- 使用索引
- 使用中间件

### 7.2 查询优化

- 使用索引
- 使用投影
- 使用分页
- 避免 N+1 查询

## 8. 注意事项

- **类型安全**：使用 TypeScript 类型定义
- **性能优化**：优化查询和索引
- **连接管理**：合理管理数据库连接
- **错误处理**：实现完善的错误处理

## 9. 常见问题

### 9.1 如何处理关联查询？

使用 populate 填充关联数据。

### 9.2 如何优化查询性能？

使用索引、投影、分页，避免 N+1 查询。

### 9.3 如何实现数据验证？

在 Schema 中定义验证规则，使用中间件。

## 10. 实践任务

1. **定义 Schema**：定义数据模型 Schema
2. **基本操作**：实现 CRUD 操作
3. **中间件**：使用中间件处理数据
4. **关联查询**：实现关联数据查询
5. **性能优化**：优化查询和索引

---

**下一章**：[5.7 Redis 缓存](../chapter-07-redis/readme.md)
