# 6.2.2 RBAC（基于角色的访问控制）

## 1. 概述

RBAC（Role-Based Access Control）是基于角色的访问控制模型，通过角色分配权限，用户通过角色获得权限。RBAC 简单易用，适合大多数应用场景。

## 2. RBAC 模型

### 2.1 基本概念

- **用户（User）**：系统用户
- **角色（Role）**：权限集合
- **权限（Permission）**：操作权限
- **资源（Resource）**：被访问的资源

### 2.2 关系模型

```
用户 -> 角色 -> 权限 -> 资源
```

## 3. 数据库设计

### 3.1 表结构

```sql
-- 用户表
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(100) UNIQUE NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL
);

-- 角色表
CREATE TABLE roles (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) UNIQUE NOT NULL,
  description TEXT
);

-- 权限表
CREATE TABLE permissions (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) UNIQUE NOT NULL,
  resource VARCHAR(100) NOT NULL,
  action VARCHAR(100) NOT NULL
);

-- 用户角色关联表
CREATE TABLE user_roles (
  user_id INT REFERENCES users(id),
  role_id INT REFERENCES roles(id),
  PRIMARY KEY (user_id, role_id)
);

-- 角色权限关联表
CREATE TABLE role_permissions (
  role_id INT REFERENCES roles(id),
  permission_id INT REFERENCES permissions(id),
  PRIMARY KEY (role_id, permission_id)
);
```

## 4. Node.js 实现

### 4.1 权限检查函数

```ts
interface User {
  id: number;
  username: string;
  roles: Role[];
}

interface Role {
  id: number;
  name: string;
  permissions: Permission[];
}

interface Permission {
  id: number;
  name: string;
  resource: string;
  action: string;
}

async function hasPermission(userId: number, resource: string, action: string): Promise<boolean> {
  const user = await db.query(`
    SELECT u.*, r.*, p.*
    FROM users u
    JOIN user_roles ur ON u.id = ur.user_id
    JOIN roles r ON ur.role_id = r.id
    JOIN role_permissions rp ON r.id = rp.role_id
    JOIN permissions p ON rp.permission_id = p.id
    WHERE u.id = $1 AND p.resource = $2 AND p.action = $3
  `, [userId, resource, action]);
  
  return user.length > 0;
}
```

### 4.2 权限中间件

```ts
import { Request, Response, NextFunction } from 'express';

function requirePermission(resource: string, action: string) {
  return async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    const userId = (req as any).user?.id;
    
    if (!userId) {
      res.status(401).json({ message: 'Unauthorized' });
      return;
    }
    
    const hasAccess = await hasPermission(userId, resource, action);
    if (!hasAccess) {
      res.status(403).json({ message: 'Forbidden' });
      return;
    }
    
    next();
  };
}

// 使用
app.delete('/users/:id', requirePermission('users', 'delete'), (req: Request, res: Response): void => {
  // 删除用户
});
```

### 4.3 角色检查中间件

```ts
function requireRole(roleName: string) {
  return async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    const userId = (req as any).user?.id;
    
    if (!userId) {
      res.status(401).json({ message: 'Unauthorized' });
      return;
    }
    
    const userRoles = await getUserRoles(userId);
    const hasRole = userRoles.some((role: Role) => role.name === roleName);
    
    if (!hasRole) {
      res.status(403).json({ message: 'Forbidden' });
      return;
    }
    
    next();
  };
}

// 使用
app.get('/admin/users', requireRole('admin'), (req: Request, res: Response): void => {
  // 管理员功能
});
```

## 5. 权限缓存

### 5.1 Redis 缓存

```ts
import Redis from 'ioredis';

const redis = new Redis();

async function getCachedPermissions(userId: number): Promise<Permission[]> {
  const cached = await redis.get(`user:${userId}:permissions`);
  if (cached) {
    return JSON.parse(cached);
  }
  
  const permissions = await getUserPermissions(userId);
  await redis.setex(`user:${userId}:permissions`, 3600, JSON.stringify(permissions));
  return permissions;
}
```

## 6. 最佳实践

### 6.1 角色设计

- 角色命名清晰
- 角色职责单一
- 避免角色过多
- 支持角色继承

### 6.2 权限设计

- 权限粒度适中
- 权限命名规范
- 权限可组合
- 权限可审计

## 7. 注意事项

- **权限验证**：始终在服务器端验证权限
- **权限缓存**：合理使用权限缓存
- **权限更新**：及时更新权限缓存
- **权限审计**：记录权限操作

## 8. 常见问题

### 8.1 如何设计角色？

根据业务需求设计角色，保持角色职责清晰。

### 8.2 如何处理权限继承？

使用角色继承或权限组实现权限继承。

### 8.3 如何优化权限查询？

使用权限缓存、优化数据库查询、使用索引。

## 9. 实践任务

1. **设计模型**：设计 RBAC 数据模型
2. **实现检查**：实现权限检查函数
3. **权限中间件**：实现权限中间件
4. **权限缓存**：实现权限缓存
5. **权限管理**：实现权限管理功能

---

**下一节**：[6.2.3 ABAC（基于属性的访问控制）](section-03-abac.md)
