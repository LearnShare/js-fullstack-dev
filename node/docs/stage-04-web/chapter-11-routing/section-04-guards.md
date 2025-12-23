# 4.11.4 路由守卫与权限控制

## 1. 概述

路由守卫和权限控制是保护 API 端点的重要机制。通过路由守卫可以控制哪些用户可以访问哪些路由，实现细粒度的权限控制。

## 2. 路由守卫概念

### 2.1 守卫的作用

- **认证检查**：验证用户是否已登录
- **权限检查**：验证用户是否有权限访问
- **角色检查**：验证用户角色是否匹配
- **资源检查**：验证用户是否可以访问特定资源

### 2.2 守卫的类型

- **全局守卫**：应用于所有路由
- **路由守卫**：应用于特定路由
- **资源守卫**：应用于特定资源

## 3. 认证守卫

### 3.1 基本认证守卫

```ts
function authGuard(req: Request, res: Response, next: NextFunction): void {
  const token = req.headers.authorization?.replace('Bearer ', '');
  
  if (!token) {
    return res.status(401).json({ error: 'Authentication required' });
  }
  
  try {
    const user = verifyToken(token);
    req.user = user;
    next();
  } catch (error) {
    res.status(401).json({ error: 'Invalid token' });
  }
}

app.use('/api/protected', authGuard);
```

### 3.2 可选认证守卫

```ts
function optionalAuthGuard(req: Request, res: Response, next: NextFunction): void {
  const token = req.headers.authorization?.replace('Bearer ', '');
  
  if (token) {
    try {
      const user = verifyToken(token);
      req.user = user;
    } catch (error) {
      // 忽略错误，继续执行
    }
  }
  
  next();
}

app.use(optionalAuthGuard);
```

## 4. 权限守卫

### 4.1 角色守卫

```ts
function roleGuard(allowedRoles: string[]) {
  return (req: AuthRequest, res: Response, next: NextFunction): void => {
    if (!req.user) {
      return res.status(401).json({ error: 'Authentication required' });
    }
    
    if (!allowedRoles.includes(req.user.role)) {
      return res.status(403).json({ error: 'Insufficient permissions' });
    }
    
    next();
  };
}

app.get('/api/admin', authGuard, roleGuard(['admin']), adminHandler);
```

### 4.2 权限守卫

```ts
function permissionGuard(requiredPermission: string) {
  return (req: AuthRequest, res: Response, next: NextFunction): void => {
    if (!req.user) {
      return res.status(401).json({ error: 'Authentication required' });
    }
    
    if (!req.user.permissions.includes(requiredPermission)) {
      return res.status(403).json({ error: 'Insufficient permissions' });
    }
    
    next();
  };
}

app.delete('/api/users/:id', authGuard, permissionGuard('users.delete'), deleteUser);
```

## 5. 资源守卫

### 5.1 资源所有权检查

```ts
async function resourceOwnerGuard(req: AuthRequest, res: Response, next: NextFunction): Promise<void> {
  const { id } = req.params;
  const user = await getUserById(id);
  
  if (!user) {
    return res.status(404).json({ error: 'User not found' });
  }
  
  // 检查是否是资源所有者或管理员
  if (user.id !== req.user?.id && req.user?.role !== 'admin') {
    return res.status(403).json({ error: 'Access denied' });
  }
  
  req.resource = user;
  next();
}

app.put('/api/users/:id', authGuard, resourceOwnerGuard, updateUser);
```

### 5.2 资源访问控制

```ts
function resourceAccessGuard(resourceType: string) {
  return async (req: AuthRequest, res: Response, next: NextFunction): Promise<void> => {
    const resourceId = req.params.id;
    const resource = await getResource(resourceType, resourceId);
    
    if (!resource) {
      return res.status(404).json({ error: 'Resource not found' });
    }
    
    // 检查访问权限
    const hasAccess = await checkResourceAccess(req.user, resource);
    if (!hasAccess) {
      return res.status(403).json({ error: 'Access denied' });
    }
    
    req.resource = resource;
    next();
  };
}
```

## 6. 组合守卫

### 6.1 守卫链

```ts
function guardChain(...guards: Array<(req: Request, res: Response, next: NextFunction) => void>) {
  return (req: Request, res: Response, next: NextFunction): void => {
    let index = 0;
    
    const runNext = (): void => {
      if (index < guards.length) {
        guards[index++](req, res, runNext);
      } else {
        next();
      }
    };
    
    runNext();
  };
}

app.get('/api/admin/users', guardChain(authGuard, roleGuard(['admin'])), getUsers);
```

### 6.2 条件守卫

```ts
function conditionalGuard(condition: (req: Request) => boolean, guard: (req: Request, res: Response, next: NextFunction) => void) {
  return (req: Request, res: Response, next: NextFunction): void => {
    if (condition(req)) {
      guard(req, res, next);
    } else {
      next();
    }
  };
}

app.use(conditionalGuard(
  (req: Request) => req.path.startsWith('/api'),
  authGuard
));
```

## 7. 最佳实践

### 7.1 守卫设计

- 保持守卫单一职责
- 使用守卫工厂创建可配置守卫
- 实现错误处理

### 7.2 权限控制

- 实现细粒度权限控制
- 使用角色和权限组合
- 实现资源级权限控制

### 7.3 性能优化

- 缓存权限检查结果
- 优化数据库查询
- 使用索引优化

## 8. 注意事项

- **安全性**：确保权限检查的完整性
- **性能**：注意权限检查的性能影响
- **错误处理**：提供清晰的错误信息
- **可维护性**：保持守卫代码清晰

## 9. 常见问题

### 9.1 如何实现细粒度权限控制？

使用权限守卫和资源守卫实现细粒度权限控制。

### 9.2 如何处理权限缓存？

使用 Redis 或内存缓存缓存权限检查结果。

### 9.3 如何实现动态权限？

使用数据库存储权限配置，动态加载权限规则。

## 10. 实践任务

1. **实现认证守卫**：实现用户认证守卫
2. **实现权限守卫**：实现角色和权限守卫
3. **实现资源守卫**：实现资源访问控制守卫
4. **实现守卫组合**：实现守卫链和组合
5. **优化权限检查**：优化权限检查性能

---

**下一章**：[4.12 请求验证与数据校验](../chapter-12-validation/readme.md)
