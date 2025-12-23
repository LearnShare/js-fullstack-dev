# 6.2.4 权限中间件实现

## 1. 概述

权限中间件是授权系统的核心组件，用于在请求处理前验证用户权限。本章介绍如何实现灵活、可扩展的权限中间件。

## 2. 中间件设计

### 2.1 中间件接口

```ts
import { Request, Response, NextFunction } from 'express';

type PermissionChecker = (req: Request, user: any) => Promise<boolean>;

interface PermissionMiddlewareOptions {
  resource?: string;
  action?: string;
  checker?: PermissionChecker;
  onDenied?: (req: Request, res: Response) => void;
}
```

### 2.2 基础中间件

```ts
function requirePermission(options: PermissionMiddlewareOptions) {
  return async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    const user = (req as any).user;
    
    if (!user) {
      res.status(401).json({ message: 'Unauthorized' });
      return;
    }
    
    let hasPermission = false;
    
    if (options.checker) {
      hasPermission = await options.checker(req, user);
    } else if (options.resource && options.action) {
      hasPermission = await hasPermission(user.id, options.resource, options.action);
    } else {
      res.status(500).json({ message: 'Invalid permission configuration' });
      return;
    }
    
    if (!hasPermission) {
      if (options.onDenied) {
        options.onDenied(req, res);
      } else {
        res.status(403).json({ message: 'Forbidden' });
      }
      return;
    }
    
    next();
  };
}
```

## 3. 高级中间件

### 3.1 资源所有者检查

```ts
function requireOwnership(resourceType: string, ownerField: string = 'userId') {
  return async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    const user = (req as any).user;
    const resourceId = req.params.id;
    
    if (!user) {
      res.status(401).json({ message: 'Unauthorized' });
      return;
    }
    
    const resource = await getResource(resourceType, resourceId);
    if (!resource) {
      res.status(404).json({ message: 'Resource not found' });
      return;
    }
    
    if (resource[ownerField] !== user.id) {
      res.status(403).json({ message: 'Forbidden' });
      return;
    }
    
    next();
  };
}

// 使用
app.delete('/posts/:id', requireOwnership('post'), (req: Request, res: Response): void => {
  // 删除自己的帖子
});
```

### 3.2 条件权限检查

```ts
function requireCondition(condition: (req: Request, user: any) => Promise<boolean>) {
  return async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    const user = (req as any).user;
    
    if (!user) {
      res.status(401).json({ message: 'Unauthorized' });
      return;
    }
    
    const meetsCondition = await condition(req, user);
    if (!meetsCondition) {
      res.status(403).json({ message: 'Forbidden' });
      return;
    }
    
    next();
  };
}

// 使用
app.put('/users/:id', requireCondition(async (req: Request, user: any): Promise<boolean> => {
  const targetUserId = parseInt(req.params.id);
  return user.id === targetUserId || user.role === 'admin';
}), (req: Request, res: Response): void => {
  // 更新用户（自己或管理员）
});
```

### 3.3 组合中间件

```ts
function requireAny(...middlewares: Array<(req: Request, res: Response, next: NextFunction) => void>) {
  return async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    let lastError: Error | null = null;
    
    for (const middleware of middlewares) {
      try {
        await new Promise<void>((resolve, reject) => {
          middleware(req, res, (err?: any) => {
            if (err) {
              reject(err);
            } else {
              resolve();
            }
          });
        });
        // 如果任何一个中间件通过，继续
        next();
        return;
      } catch (error) {
        lastError = error as Error;
      }
    }
    
    // 所有中间件都失败
    res.status(403).json({ message: 'Forbidden' });
  };
}

// 使用
app.get('/admin/users', requireAny(
  requireRole('admin'),
  requireRole('super_admin')
), (req: Request, res: Response): void => {
  // 管理员或超级管理员可以访问
});
```

## 4. 错误处理

### 4.1 自定义错误响应

```ts
function requirePermission(options: PermissionMiddlewareOptions) {
  return async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    // ... 权限检查逻辑
    
    if (!hasPermission) {
      if (options.onDenied) {
        options.onDenied(req, res);
      } else {
        res.status(403).json({
          error: 'Forbidden',
          message: 'You do not have permission to perform this action',
          resource: options.resource,
          action: options.action
        });
      }
      return;
    }
    
    next();
  };
}
```

## 5. 性能优化

### 5.1 权限缓存

```ts
const permissionCache = new Map<string, { result: boolean; expires: number }>();

async function checkPermissionCached(userId: number, resource: string, action: string): Promise<boolean> {
  const key = `${userId}:${resource}:${action}`;
  const cached = permissionCache.get(key);
  
  if (cached && cached.expires > Date.now()) {
    return cached.result;
  }
  
  const result = await hasPermission(userId, resource, action);
  permissionCache.set(key, {
    result,
    expires: Date.now() + 60000 // 1 分钟缓存
  });
  
  return result;
}
```

## 6. 最佳实践

### 6.1 中间件设计

- 保持中间件简单
- 支持多种配置方式
- 提供清晰的错误信息
- 实现权限缓存

### 6.2 安全考虑

- 默认拒绝访问
- 服务器端验证
- 记录权限操作
- 防止权限提升

## 7. 注意事项

- **性能影响**：注意中间件的性能影响
- **错误处理**：实现完善的错误处理
- **权限缓存**：合理使用权限缓存
- **测试覆盖**：充分测试中间件

## 8. 常见问题

### 8.1 如何处理权限缓存失效？

在权限变更时清除相关缓存。

### 8.2 如何实现细粒度权限？

使用资源级别的权限检查，结合条件判断。

### 8.3 如何优化中间件性能？

使用权限缓存、优化数据库查询、批量检查权限。

## 9. 实践任务

1. **基础中间件**：实现基础权限中间件
2. **高级中间件**：实现高级权限中间件
3. **组合中间件**：实现组合权限中间件
4. **错误处理**：实现完善的错误处理
5. **性能优化**：优化中间件性能

---

**下一章**：[6.3 Web 安全](../chapter-03-web-security/readme.md)
