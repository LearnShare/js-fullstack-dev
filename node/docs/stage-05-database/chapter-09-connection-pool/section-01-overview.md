# 5.9.1 连接池概述

## 1. 概述

连接池是管理数据库连接的机制，通过预先创建和复用连接，提高性能和资源利用率。连接池避免了频繁创建和销毁连接的开销。

## 2. 核心概念

### 2.1 连接池的作用

- **性能优化**：复用连接，减少创建开销
- **资源管理**：合理管理数据库连接
- **并发控制**：控制并发连接数
- **连接复用**：提高资源利用率

### 2.2 连接池的组成

- **连接池**：管理连接的容器
- **连接对象**：数据库连接实例
- **连接配置**：连接池的配置参数
- **连接状态**：连接的使用状态

## 3. 连接池工作流程

### 3.1 获取连接

```
1. 检查连接池中是否有可用连接
2. 如果有，返回可用连接
3. 如果没有，创建新连接（如果未达到最大连接数）
4. 如果达到最大连接数，等待可用连接
```

### 3.2 释放连接

```
1. 使用完连接后，归还到连接池
2. 连接池标记连接为可用
3. 等待下次使用
```

## 4. 连接池参数

### 4.1 基本参数

- **min**：最小连接数
- **max**：最大连接数
- **idleTimeout**：空闲连接超时时间
- **connectionTimeout**：获取连接超时时间

### 4.2 高级参数

- **acquireTimeout**：获取连接超时
- **createTimeout**：创建连接超时
- **destroyTimeout**：销毁连接超时
- **reapInterval**：清理间隔

## 5. 连接池实现

### 5.1 PostgreSQL

```ts
import { Pool } from 'pg';

const pool = new Pool({
  host: 'localhost',
  port: 5432,
  database: 'mydb',
  user: 'postgres',
  password: 'password',
  max: 20,
  min: 5,
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 2000
});
```

### 5.2 MySQL

```ts
import { createPool, Pool } from 'mysql2/promise';

const pool: Pool = createPool({
  host: 'localhost',
  port: 3306,
  database: 'mydb',
  user: 'root',
  password: 'password',
  connectionLimit: 10,
  queueLimit: 0
});
```

## 6. 最佳实践

### 6.1 配置原则

- 根据应用负载设置连接数
- 设置合理的超时时间
- 监控连接池状态
- 处理连接错误

### 6.2 性能优化

- 合理设置连接数
- 使用连接复用
- 避免连接泄漏
- 监控连接使用

## 7. 注意事项

- **连接数设置**：合理设置最大和最小连接数
- **连接泄漏**：避免连接泄漏
- **错误处理**：处理连接错误
- **监控**：监控连接池状态

## 8. 常见问题

### 8.1 如何设置连接数？

根据应用负载、数据库性能、服务器资源设置。

### 8.2 如何处理连接泄漏？

实现连接泄漏检测，确保连接正确释放。

### 8.3 如何优化连接池性能？

合理设置连接数，使用连接复用，避免连接泄漏。

## 9. 相关资源

- [连接池模式](https://en.wikipedia.org/wiki/Connection_pool)
- [数据库连接管理](https://node-postgres.com/features/pooling)

---

**下一节**：[5.9.2 连接池配置](section-02-config.md)
