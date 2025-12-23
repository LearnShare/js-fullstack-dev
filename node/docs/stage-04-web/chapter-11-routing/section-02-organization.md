# 4.11.2 路由组织与模块化

## 1. 概述

路由组织与模块化是大型应用开发中的重要实践。通过合理的路由组织和模块化，可以提高代码的可维护性、可扩展性和可测试性。

## 2. 路由模块化

### 2.1 基本模块化

```ts
// routes/users.ts
import { Router, Request, Response } from 'express';

const router = Router();

router.get('/', (req: Request, res: Response): void => {
  res.json({ users: [] });
});

router.get('/:id', (req: Request, res: Response): void => {
  const { id } = req.params;
  res.json({ userId: id });
});

router.post('/', (req: Request, res: Response): void => {
  res.json({ message: 'User created' });
});

export default router;
```

```ts
// app.ts
import express, { Express } from 'express';
import usersRouter from './routes/users';

const app: Express = express();

app.use('/api/users', usersRouter);

app.listen(3000, (): void => {
  console.log('Server running on port 3000');
});
```

### 2.2 嵌套路由

```ts
// routes/users.ts
import { Router } from 'express';
import postsRouter from './users/posts';

const router = Router();

router.use('/:userId/posts', postsRouter);

export default router;
```

```ts
// routes/users/posts.ts
import { Router, Request, Response } from 'express';

const router = Router({ mergeParams: true });

router.get('/', (req: Request, res: Response): void => {
  const { userId } = req.params;
  res.json({ userId, posts: [] });
});

export default router;
```

## 3. 路由组织方式

### 3.1 按功能组织

```
routes/
├── users.ts
├── posts.ts
├── comments.ts
└── auth.ts
```

```ts
// routes/index.ts
import { Router } from 'express';
import usersRouter from './users';
import postsRouter from './posts';
import commentsRouter from './comments';
import authRouter from './auth';

const router = Router();

router.use('/users', usersRouter);
router.use('/posts', postsRouter);
router.use('/comments', commentsRouter);
router.use('/auth', authRouter);

export default router;
```

### 3.2 按模块组织

```
routes/
├── api/
│   ├── users.ts
│   └── posts.ts
├── admin/
│   ├── users.ts
│   └── settings.ts
└── public/
    └── pages.ts
```

```ts
// routes/index.ts
import { Router } from 'express';
import apiRouter from './api';
import adminRouter from './admin';
import publicRouter from './public';

const router = Router();

router.use('/api', apiRouter);
router.use('/admin', adminRouter);
router.use('/', publicRouter);

export default router;
```

## 4. 路由控制器

### 4.1 控制器分离

```ts
// controllers/userController.ts
import { Request, Response } from 'express';

export class UserController {
  static async getUsers(req: Request, res: Response): Promise<void> {
    const users = await fetchUsers();
    res.json({ users });
  }

  static async getUserById(req: Request, res: Response): Promise<void> {
    const { id } = req.params;
    const user = await fetchUser(id);
    res.json({ user });
  }

  static async createUser(req: Request, res: Response): Promise<void> {
    const user = await createUser(req.body);
    res.status(201).json({ user });
  }
}
```

```ts
// routes/users.ts
import { Router } from 'express';
import { UserController } from '../controllers/userController';

const router = Router();

router.get('/', UserController.getUsers);
router.get('/:id', UserController.getUserById);
router.post('/', UserController.createUser);

export default router;
```

## 5. 路由前缀

### 5.1 API 版本控制

```ts
// routes/v1/users.ts
const v1UsersRouter = Router();
// v1 路由

// routes/v2/users.ts
const v2UsersRouter = Router();
// v2 路由

// app.ts
app.use('/api/v1/users', v1UsersRouter);
app.use('/api/v2/users', v2UsersRouter);
```

### 5.2 功能前缀

```ts
// routes/api/users.ts
app.use('/api/users', usersRouter);

// routes/admin/users.ts
app.use('/admin/users', adminUsersRouter);
```

## 6. 路由中间件

### 6.1 路由级中间件

```ts
// routes/users.ts
import { Router } from 'express';
import { authMiddleware } from '../middleware/auth';

const router = Router();

// 所有用户路由需要认证
router.use(authMiddleware);

router.get('/', getUsers);
router.get('/:id', getUserById);
```

### 6.2 特定路由中间件

```ts
// routes/users.ts
router.get('/', getUsers); // 不需要认证
router.get('/:id', authMiddleware, getUserById); // 需要认证
router.post('/', authMiddleware, createUser); // 需要认证
```

## 7. 最佳实践

### 7.1 路由组织

- 按功能模块组织路由
- 使用路由前缀区分不同模块
- 实现路由复用

### 7.2 控制器分离

- 将业务逻辑分离到控制器
- 保持路由文件简洁
- 实现控制器复用

### 7.3 模块化

- 使用模块化路由
- 实现路由组合
- 保持路由独立

## 8. 注意事项

- **模块化**：按功能模块组织路由
- **可维护性**：保持路由清晰和文档化
- **可扩展性**：支持路由扩展
- **性能**：注意路由匹配性能

## 9. 常见问题

### 9.1 如何组织大量路由？

按功能模块组织，使用路由前缀和嵌套路由。

### 9.2 如何实现路由复用？

使用路由模块和控制器实现路由复用。

### 9.3 如何处理路由冲突？

使用路由优先级和更具体的路径匹配。

## 10. 实践任务

1. **实现路由模块化**：将路由按功能模块化
2. **实现嵌套路由**：实现嵌套资源路由
3. **实现控制器分离**：将业务逻辑分离到控制器
4. **实现路由组合**：实现路由组合和复用
5. **优化路由组织**：优化路由组织结构

---

**下一节**：[4.11.3 动态路由与参数](section-03-dynamic.md)
