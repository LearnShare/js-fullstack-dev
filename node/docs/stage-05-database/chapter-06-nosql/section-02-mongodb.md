# 5.6.2 MongoDB

## 1. 概述

MongoDB 是一个流行的文档数据库，使用 BSON 格式存储数据，提供了灵活的文档模型和强大的查询能力。MongoDB 适合处理非结构化数据和需要快速开发的项目。

## 2. 特性说明

- **文档模型**：灵活的文档结构
- **高性能**：优秀的读写性能
- **水平扩展**：支持分片和副本集
- **丰富查询**：支持复杂查询和聚合

## 3. 安装与连接

### 3.1 安装

```bash
# macOS
brew install mongodb-community

# Ubuntu
sudo apt-get install mongodb

# Windows
# 下载安装包从官网安装
```

### 3.2 Node.js 连接

```bash
npm install mongodb
```

```ts
import { MongoClient, Db, Collection } from 'mongodb';

const client = new MongoClient(process.env.MONGODB_URI!);

async function connectDatabase(): Promise<Db> {
  await client.connect();
  return client.db('mydb');
}

async function closeConnection(): Promise<void> {
  await client.close();
}
```

## 4. 基本操作

### 4.1 创建文档

```ts
async function createUser(name: string, email: string): Promise<void> {
  const db = await connectDatabase();
  const collection: Collection = db.collection('users');
  
  const result = await collection.insertOne({
    name,
    email,
    createdAt: new Date()
  });
  
  console.log('Created user:', result.insertedId);
}
```

### 4.2 查询文档

```ts
interface User {
  _id: string;
  name: string;
  email: string;
  createdAt: Date;
}

async function getUserById(id: string): Promise<User | null> {
  const db = await connectDatabase();
  const collection: Collection<User> = db.collection('users');
  
  return await collection.findOne({ _id: id as any });
}

async function getUsers(): Promise<User[]> {
  const db = await connectDatabase();
  const collection: Collection<User> = db.collection('users');
  
  return await collection.find({}).toArray();
}
```

### 4.3 更新文档

```ts
async function updateUser(id: string, name: string): Promise<void> {
  const db = await connectDatabase();
  const collection: Collection = db.collection('users');
  
  await collection.updateOne(
    { _id: id as any },
    { $set: { name, updatedAt: new Date() } }
  );
}
```

### 4.4 删除文档

```ts
async function deleteUser(id: string): Promise<void> {
  const db = await connectDatabase();
  const collection: Collection = db.collection('users');
  
  await collection.deleteOne({ _id: id as any });
}
```

## 5. 查询操作

### 5.1 条件查询

```ts
async function getUsersByEmail(email: string): Promise<User[]> {
  const db = await connectDatabase();
  const collection: Collection<User> = db.collection('users');
  
  return await collection.find({
    email: { $regex: email, $options: 'i' }
  }).toArray();
}
```

### 5.2 聚合查询

```ts
async function getUserStats(): Promise<void> {
  const db = await connectDatabase();
  const collection: Collection = db.collection('users');
  
  const stats = await collection.aggregate([
    { $group: { _id: null, count: { $sum: 1 }, avgAge: { $avg: '$age' } } }
  ]).toArray();
  
  console.log('Stats:', stats);
}
```

## 6. 索引

### 6.1 创建索引

```ts
async function createIndexes(): Promise<void> {
  const db = await connectDatabase();
  const collection: Collection = db.collection('users');
  
  await collection.createIndex({ email: 1 }, { unique: true });
  await collection.createIndex({ name: 1, email: 1 });
}
```

## 7. 最佳实践

### 7.1 数据模型设计

- 合理设计文档结构
- 避免过度嵌套
- 使用引用而非嵌入
- 考虑查询模式

### 7.2 性能优化

- 使用索引
- 优化查询
- 使用投影选择字段
- 批量操作

## 8. 注意事项

- **数据一致性**：理解最终一致性
- **索引设计**：合理设计索引
- **查询优化**：优化查询性能
- **连接管理**：合理管理数据库连接

## 9. 常见问题

### 9.1 如何处理关系数据？

使用引用或嵌入，根据查询模式选择。

### 9.2 如何优化查询性能？

使用索引、优化查询、使用投影。

### 9.3 如何保证数据一致性？

使用事务（MongoDB 4.0+）或应用层保证。

## 10. 实践任务

1. **连接 MongoDB**：建立 MongoDB 连接
2. **基本操作**：实现 CRUD 操作
3. **查询操作**：实现条件查询和聚合
4. **索引设计**：创建和使用索引
5. **性能优化**：优化查询和索引

---

**下一节**：[5.6.3 Mongoose ODM](section-03-mongoose.md)
