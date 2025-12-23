# 4.2.2 Express.js 简介

## 1. 概述

Express.js 是最流行的 Node.js Web 框架，提供了简洁灵活的 API 和丰富的中间件生态。Express 采用极简设计理念，核心功能最小化，通过中间件扩展功能。由于其简单易用和生态丰富，Express 成为 Node.js 开发的首选框架。

## 2. 特性说明

- **极简设计**：核心功能最小化，高度可定制
- **中间件机制**：强大的中间件系统，支持功能扩展
- **路由系统**：灵活的路由定义和参数处理
- **模板引擎**：支持多种模板引擎
- **丰富生态**：庞大的中间件和插件生态
- **广泛采用**：被大量项目使用，社区支持完善

## 3. 安装与初始化

### 3.1 安装

```bash
npm install express
npm install --save-dev @types/express
```

### 3.2 基本使用

```ts
import express, { Request, Response, NextFunction } from 'express';

const app = express();

app.get('/', (req: Request, res: Response) => {
  res.json({ message: 'Hello World' });
});

app.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});
```

## 4. 路由系统

### 4.1 基本路由

```ts
// GET 路由
app.get('/users', (req: Request, res: Response) => {
  res.json({ users: [] });
});

// POST 路由
app.post('/users', (req: Request, res: Response) => {
  res.json({ message: 'User created' });
});

// PUT 路由
app.put('/users/:id', (req: Request, res: Response) => {
  const { id } = req.params;
  res.json({ message: `User ${id} updated` });
});

// DELETE 路由
app.delete('/users/:id', (req: Request, res: Response) => {
  const { id } = req.params;
  res.json({ message: `User ${id} deleted` });
});
```

### 4.2 路由参数

```ts
// 路径参数
app.get('/users/:id', (req: Request, res: Response) => {
  const { id } = req.params;
  res.json({ userId: id });
});

// 查询参数
app.get('/users', (req: Request, res: Response) => {
  const { page, limit } = req.query;
  res.json({ page, limit });
});
```

### 4.3 路由模块化

```ts
// routes/users.ts
import { Router, Request, Response } from 'express';

const router = Router();

router.get('/', (req: Request, res: Response) => {
  res.json({ users: [] });
});

router.get('/:id', (req: Request, res: Response) => {
  const { id } = req.params;
  res.json({ userId: id });
});

export default router;

// app.ts
import express, { Request, Response, NextFunction } from 'express';
import usersRouter from './routes/users';

const app = express();
app.use('/users', usersRouter);
```

## 5. 中间件

### 5.1 内置中间件

```ts
// JSON 解析
app.use(express.json());

// URL 编码解析
app.use(express.urlencoded({ extended: true }));

// 静态文件服务
app.use(express.static('public'));
```

### 5.2 自定义中间件

```ts
// 日志中间件
app.use((req: Request, res: Response, next) => {
  console.log(`${req.method} ${req.url}`);
  next();
});

// 认证中间件
const authMiddleware = (req: Request, res: Response, next: NextFunction) => {
  const token = req.headers.authorization;
  if (!token) {
    return res.status(401).json({ error: 'Unauthorized' });
  }
  next();
};

app.use('/api', authMiddleware);
```

### 5.3 错误处理中间件

```ts
app.use((err: Error, req: Request, res: Response, next: NextFunction) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Internal Server Error' });
});
```

## 6. 请求处理

### 6.1 请求对象

```ts
app.get('/users', (req: Request, res: Response) => {
  // 请求方法
  console.log(req.method); // GET

  // 请求 URL
  console.log(req.url); // /users?page=1

  // 请求路径
  console.log(req.path); // /users

  // 查询参数
  console.log(req.query); // { page: '1' }

  // 路径参数
  console.log(req.params); // {}

  // 请求头
  console.log(req.headers); // { ... }

  // 请求体（需要中间件解析）
  console.log(req.body); // { ... }
});
```

### 6.2 响应对象

```ts
app.get('/users', (req: Request, res: Response) => {
  // 设置状态码
  res.status(200);

  // 设置响应头
  res.setHeader('Content-Type', 'application/json');

  // 发送 JSON 响应
  res.json({ users: [] });

  // 发送文本响应
  res.send('Hello World');

  // 重定向
  res.redirect('/login');
});
```

## 7. 常用中间件

### 7.1 第三方中间件

| 中间件            | 用途                     | 安装命令                           |
|:------------------|:-------------------------|:-----------------------------------|
| **cors**          | 跨域资源共享             | `npm install cors`                 |
| **helmet**         | 安全头部                 | `npm install helmet`               |
| **morgan**         | HTTP 请求日志            | `npm install morgan`               |
| **compression**    | 响应压缩                 | `npm install compression`          |
| **cookie-parser** | Cookie 解析              | `npm install cookie-parser`        |
| **express-rate-limit** | 请求限流         | `npm install express-rate-limit`   |

### 7.2 使用示例

```ts
import cors from 'cors';
import helmet from 'helmet';
import morgan from 'morgan';
import compression from 'compression';

app.use(cors());
app.use(helmet());
app.use(morgan('combined'));
app.use(compression());
```

## 8. 完整示例

```ts
import express, { Request, Response, NextFunction } from 'express';
import cors from 'cors';
import helmet from 'helmet';
import morgan from 'morgan';

const app = express();

// 中间件
app.use(cors());
app.use(helmet());
app.use(morgan('combined'));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// 路由
app.get('/', (req: Request, res: Response) => {
  res.json({ message: 'Hello World' });
});

app.get('/users', (req: Request, res: Response) => {
  const { page = '1', limit = '20' } = req.query;
  res.json({
    data: [],
    pagination: {
      page: parseInt(page as string),
      limit: parseInt(limit as string)
    }
  });
});

app.post('/users', (req: Request, res: Response) => {
  const { name, email } = req.body;
  res.status(201).json({
    data: {
      id: 1,
      name,
      email
    }
  });
});

// 错误处理
app.use((err: Error, req: Request, res: Response, next: NextFunction) => {
  console.error(err.stack);
  res.status(500).json({
    error: {
      message: 'Internal Server Error'
    }
  });
});

// 404 处理
app.use((req: Request, res: Response) => {
  res.status(404).json({
    error: {
      message: 'Not Found'
    }
  });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
```

## 9. 最佳实践

### 9.1 项目结构

```
project/
├── src/
│   ├── routes/
│   │   ├── users.ts
│   │   └── posts.ts
│   ├── middleware/
│   │   ├── auth.ts
│   │   └── error.ts
│   ├── controllers/
│   │   ├── users.ts
│   │   └── posts.ts
│   ├── services/
│   │   ├── users.ts
│   │   └── posts.ts
│   └── app.ts
└── package.json
```

### 9.2 代码组织

- **路由分离**：将路由定义分离到独立文件
- **中间件复用**：将通用中间件提取为独立模块
- **错误处理**：统一错误处理机制
- **环境配置**：使用环境变量管理配置

### 9.3 性能优化

- **启用压缩**：使用 compression 中间件
- **静态文件缓存**：合理设置静态文件缓存
- **连接池**：使用数据库连接池
- **异步处理**：避免阻塞操作

## 10. 注意事项

- **安全性**：使用 helmet 等安全中间件
- **错误处理**：实现完整的错误处理机制
- **输入验证**：验证和清理用户输入
- **性能监控**：监控应用性能，及时发现问题

## 11. 常见问题

### 11.1 如何处理异步错误？

使用 try-catch 或 async/await：

```ts
app.get('/users', async (req: Request, res: Response, next: NextFunction) => {
  try {
    const users = await getUsers();
    res.json({ data: users });
  } catch (error) {
    next(error);
  }
});
```

### 11.2 如何实现文件上传？

使用 multer 中间件：

```ts
import multer from 'multer';

const upload = multer({ dest: 'uploads/' });

app.post('/upload', upload.single('file'), (req: Request, res: Response) => {
  res.json({ file: req.file });
});
```

---

**下一节**：[4.2.3 Fastify 简介](section-03-fastify.md)
