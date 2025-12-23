# 5.3.1 ORM 框架概述

## 1. 概述

ORM（Object-Relational Mapping）框架将数据库表映射为对象，提供面向对象的数据库操作接口。ORM 框架简化了数据库操作，提高了开发效率。

## 2. 核心概念

### 2.1 ORM 的作用

- **对象映射**：将数据库表映射为对象
- **查询抽象**：提供高级查询接口
- **关系管理**：管理表之间的关系
- **类型安全**：提供类型安全的操作

### 2.2 ORM 的优势

- **开发效率**：简化数据库操作
- **类型安全**：TypeScript 类型支持
- **代码复用**：减少重复代码
- **维护性**：提高代码可维护性

### 2.3 ORM 的劣势

- **性能开销**：可能影响查询性能
- **学习成本**：需要学习 ORM 语法
- **灵活性**：某些复杂查询可能受限

## 3. ORM 框架对比

### 3.1 Prisma

**特点**：
- 类型安全
- 代码生成
- 迁移工具
- 现代化设计

**适用场景**：
- TypeScript 项目
- 需要类型安全
- 现代化应用

### 3.2 Drizzle ORM

**特点**：
- 轻量级
- SQL-like 语法
- 类型安全
- 高性能

**适用场景**：
- 需要 SQL-like 语法
- 性能要求高
- TypeScript 项目

### 3.3 TypeORM

**特点**：
- 装饰器语法
- 功能丰富
- 广泛使用
- 支持多种数据库

**适用场景**：
- 需要丰富功能
- 装饰器语法偏好
- 企业级应用

### 3.4 Sequelize

**特点**：
- 成熟稳定
- 功能完善
- 广泛使用
- JavaScript/TypeScript 支持

**适用场景**：
- 需要成熟方案
- JavaScript 项目
- 企业级应用

## 4. ORM 基本操作

### 4.1 模型定义

```ts
// Prisma
model User {
  id        Int      @id @default(autoincrement())
  name      String
  email     String   @unique
  createdAt DateTime @default(now())
}

// TypeORM
@Entity()
class User {
  @PrimaryGeneratedColumn()
  id!: number;

  @Column()
  name!: string;

  @Column({ unique: true })
  email!: string;

  @CreateDateColumn()
  createdAt!: Date;
}
```

### 4.2 CRUD 操作

```ts
// 创建
const user = await User.create({ name: 'John', email: 'john@example.com' });

// 查询
const user = await User.findByPk(1);
const users = await User.findAll({ where: { name: 'John' } });

// 更新
await user.update({ name: 'Jane' });

// 删除
await user.destroy();
```

## 5. 关系管理

### 5.1 一对一关系

```ts
// User 和 Profile 一对一
user.profile = profile;
await user.save();
```

### 5.2 一对多关系

```ts
// User 和 Order 一对多
const orders = await user.getOrders();
await user.createOrder({ amount: 100 });
```

### 5.3 多对多关系

```ts
// User 和 Role 多对多
await user.addRole(role);
const roles = await user.getRoles();
```

## 6. 查询构建器

### 6.1 基本查询

```ts
// 条件查询
const users = await User.findAll({
  where: {
    name: 'John',
    age: { [Op.gte]: 18 }
  }
});
```

### 6.2 关联查询

```ts
// 包含关联数据
const user = await User.findByPk(1, {
  include: [Order, Profile]
});
```

### 6.3 聚合查询

```ts
// 统计查询
const count = await User.count({ where: { active: true } });
const avgAge = await User.findAll({
  attributes: [[sequelize.fn('AVG', sequelize.col('age')), 'avgAge']]
});
```

## 7. 最佳实践

### 7.1 模型设计

- 清晰的模型定义
- 合理的关系设计
- 使用类型定义
- 添加验证

### 7.2 查询优化

- 使用索引
- 避免 N+1 查询
- 使用预加载
- 优化关联查询

### 7.3 性能考虑

- 批量操作
- 使用原生查询
- 缓存查询结果
- 监控查询性能

## 8. 注意事项

- **性能**：注意 ORM 的性能影响
- **学习成本**：需要学习 ORM 语法
- **灵活性**：某些复杂查询可能需要原生 SQL
- **版本兼容**：注意 ORM 版本兼容性

## 9. 常见问题

### 9.1 如何选择 ORM 框架？

根据项目需求、团队经验、性能要求选择。

### 9.2 ORM 会影响性能吗？

可能会，但可以通过优化查询、使用索引、批量操作等方式优化。

### 9.3 何时使用原生 SQL？

复杂查询、性能要求高、ORM 无法满足的场景。

## 10. 相关资源

- [ORM 模式](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping)
- [ORM 最佳实践](https://www.prisma.io/docs/guides/performance-and-optimization)

---

**下一节**：[5.3.2 Prisma 简介](section-02-prisma.md)
