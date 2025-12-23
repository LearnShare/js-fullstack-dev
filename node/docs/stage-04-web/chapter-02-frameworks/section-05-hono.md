# 4.2.5 Hono 简介

## 1. 概述

Hono 是一个轻量级、高性能的 Web 框架，专为边缘计算和 Serverless 场景设计。Hono 支持多个运行时（Node.js、Bun、Deno、Cloudflare Workers 等），提供了简洁的 API 和强大的类型推断。Hono 注重性能和开发体验，适合构建现代 Web 应用。

## 2. 特性说明

- **跨运行时**：支持 Node.js、Bun、Deno、Cloudflare Workers 等
- **高性能**：极小的体积和极高的性能
- **TypeScript 优先**：原生支持 TypeScript，提供强大的类型推断
- **中间件系统**：强大的中间件系统
- **边缘计算优化**：专为边缘计算和 Serverless 优化
- **简洁 API**：简洁直观的 API 设计

## 3. 安装与初始化

### 3.1 安装

```bash
npm install hono
```

### 3.2 基本使用

```ts
import { Hono, Context } from 'hono';

const app = new Hono();

app.get('/', (c: Context) => {
  return c.text('Hello World');
});

export default app;
```

### 3.3 不同运行时的使用

**Node.js**：

```ts
import { serve } from '@hono/node-server';
import { Hono, Context } from 'hono';

const app = new Hono();

app.get('/', (c: Context) => {
  return c.json({ message: 'Hello World' });
});

serve(app, (info: { port: number }) => {
  console.log(`Server running on http://localhost:${info.port}`);
});
```

**Cloudflare Workers**：

```ts
import { Hono, Context } from 'hono';

const app = new Hono();

app.get('/', (c: Context) => {
  return c.json({ message: 'Hello World' });
});

export default app;
```

**Bun**：

```ts
import { Hono } from 'hono';

const app = new Hono();

app.get('/', (c) => {
  return c.json({ message: 'Hello World' });
});

export default {
  port: 3000,
  fetch: app.fetch,
};
```

## 4. 路由系统

### 4.1 基本路由

```ts
import { Hono, Context } from 'hono';

const app = new Hono();

// GET 路由
app.get('/users', (c: Context) => {
  return c.json({ users: [] });
});

// POST 路由
app.post('/users', async (c: Context) => {
  const body = await c.req.json();
  return c.json({ message: 'User created', data: body });
});

// PUT 路由
app.put('/users/:id', async (c: Context) => {
  const id = c.req.param('id');
  const body = await c.req.json();
  return c.json({ message: `User ${id} updated`, data: body });
});

// DELETE 路由
app.delete('/users/:id', (c: Context) => {
  const id = c.req.param('id');
  return c.json({ message: `User ${id} deleted` });
});
```

### 4.2 路由参数

```ts
import { Context } from 'hono';

// 路径参数
app.get('/users/:id', (c: Context) => {
  const id = c.req.param('id');
  return c.json({ userId: id });
});

// 查询参数
app.get('/users', (c: Context) => {
  const page = c.req.query('page');
  const limit = c.req.query('limit');
  return c.json({ page, limit });
});

// 通配符
app.get('/users/*', (c: Context) => {
  return c.json({ message: 'Match all' });
});
```

### 4.3 路由分组

```ts
import { Hono, Context } from 'hono';

const users = new Hono();

users.get('/', (c: Context) => {
  return c.json({ users: [] });
});

users.get('/:id', (c: Context) => {
  const id = c.req.param('id');
  return c.json({ userId: id });
});

app.route('/users', users);
```

## 5. 中间件

### 5.1 内置中间件

```ts
import { cors } from 'hono/cors';
import { logger } from 'hono/logger';
import { secureHeaders } from 'hono/secure-headers';

app.use('*', cors());
app.use('*', logger());
app.use('*', secureHeaders());
```

### 5.2 自定义中间件

```ts
import { Context, Next } from 'hono';

// 日志中间件
app.use('*', async (c: Context, next: Next) => {
  console.log(`${c.req.method} ${c.req.path}`);
  await next();
  console.log(`Status: ${c.res.status}`);
});

// 认证中间件
app.use('/api/*', async (c: Context, next: Next) => {
  const token = c.req.header('Authorization');
  if (!token) {
    return c.json({ error: 'Unauthorized' }, 401);
  }
  await next();
});
```

### 5.3 错误处理中间件

```ts
import { Context, ErrorHandler } from 'hono';

app.onError((err: Error, c: Context) => {
  console.error(err);
  return c.json({ error: 'Internal Server Error' }, 500);
});

app.notFound((c: Context) => {
  return c.json({ error: 'Not Found' }, 404);
});
```

## 6. 类型安全

### 6.1 类型推断

```ts
import { Hono, Context, Next } from 'hono';

type Env = {
  Variables: {
    user: {
      id: number;
      name: string;
    };
  };
};

const app = new Hono<Env>();

app.use('*', async (c: Context, next: Next) => {
  c.set('user', { id: 1, name: 'John' });
  await next();
});

app.get('/profile', (c: Context) => {
  const user = c.get('user'); // 类型推断
  return c.json({ user });
});
```

### 6.2 验证器

```ts
import { validator } from 'hono/validator';
import { z } from 'zod';

const createUserSchema = z.object({
  name: z.string().min(1),
  email: z.string().email(),
});

app.post(
  '/users',
  validator('json', (value: unknown, c: Context) => {
    const parsed = createUserSchema.safeParse(value);
    if (!parsed.success) {
      return c.json({ error: 'Validation failed' }, 400);
    }
    return parsed.data;
  }),
  async (c: Context) => {
    const data = c.req.valid('json'); // 类型安全
    return c.json({ message: 'User created', data });
  }
);
```

## 7. 响应处理

### 7.1 响应类型

```ts
import { Context } from 'hono';

// JSON 响应
app.get('/users', (c: Context) => {
  return c.json({ users: [] });
});

// 文本响应
app.get('/text', (c: Context) => {
  return c.text('Hello World');
});

// HTML 响应
app.get('/html', (c: Context) => {
  return c.html('<h1>Hello World</h1>');
});

// 重定向
app.get('/redirect', (c: Context) => {
  return c.redirect('/users');
});

// 流响应
app.get('/stream', (c: Context) => {
  const stream = new ReadableStream({
    start(controller: ReadableStreamDefaultController<Uint8Array>) {
      controller.enqueue(new TextEncoder().encode('Hello'));
      controller.close();
    },
  });
  return c.body(stream);
});
```

### 7.2 状态码和头部

```ts
import { Context } from 'hono';

app.get('/users', (c: Context) => {
  return c.json({ users: [] }, 200, {
    'X-Custom-Header': 'value',
  });
});
```

## 8. 完整示例

```ts
import { Hono, Context, Next } from 'hono';
import { cors } from 'hono/cors';
import { logger } from 'hono/logger';
import { validator } from 'hono/validator';
import { z } from 'zod';

const app = new Hono();

// 中间件
app.use('*', cors());
app.use('*', logger());

// 验证器
const createUserSchema = z.object({
  name: z.string().min(1),
  email: z.string().email(),
});

// 路由
app.get('/', (c: Context) => {
  return c.json({ message: 'Hello World' });
});

app.get('/users', (c: Context) => {
  const page = c.req.query('page') || '1';
  const limit = c.req.query('limit') || '20';
  return c.json({
    data: [],
    pagination: {
      page: parseInt(page),
      limit: parseInt(limit),
    },
  });
});

app.post(
  '/users',
  validator('json', (value: unknown, c: Context) => {
    const parsed = createUserSchema.safeParse(value);
    if (!parsed.success) {
      return c.json({ error: 'Validation failed' }, 400);
    }
    return parsed.data;
  }),
  async (c: Context) => {
    const data = c.req.valid('json');
    return c.json({ message: 'User created', data }, 201);
  }
);

app.get('/users/:id', (c: Context) => {
  const id = c.req.param('id');
  return c.json({ userId: id });
});

// 错误处理
app.onError((err: Error, c: Context) => {
  console.error(err);
  return c.json({ error: 'Internal Server Error' }, 500);
});

app.notFound((c: Context) => {
  return c.json({ error: 'Not Found' }, 404);
});

export default app;
```

## 9. 性能优化

### 9.1 性能特点

- **极小的体积**：框架体积极小，适合边缘计算
- **高性能**：优化的性能，适合高并发场景
- **低内存占用**：最小化内存占用
- **快速启动**：极快的启动时间

### 9.2 边缘计算优化

- **跨运行时支持**：支持多个运行时环境
- **Serverless 优化**：专为 Serverless 场景优化
- **CDN 集成**：与 CDN 和边缘计算平台集成

## 10. 最佳实践

### 10.1 类型安全

充分利用 TypeScript 类型系统：

```ts
type Env = {
  Variables: {
    user: User;
  };
  Bindings: {
    DB: D1Database;
  };
};

const app = new Hono<Env>();
```

### 10.2 中间件组织

按功能组织中间件：

```ts
import { Hono, Context, Next } from 'hono';

const auth = new Hono();
auth.use('*', async (c: Context, next: Next) => {
  // 认证逻辑
  await next();
});

app.route('/api', auth);
```

## 11. 注意事项

- **运行时兼容**：注意不同运行时的差异
- **类型安全**：充分利用 TypeScript 类型系统
- **性能优化**：注意边缘计算的性能特点
- **错误处理**：实现完整的错误处理机制

## 12. 常见问题

### 12.1 如何处理文件上传？

使用 `c.req.parseBody()`：

```ts
import { Context } from 'hono';

app.post('/upload', async (c: Context) => {
  const body = await c.req.parseBody();
  const file = body.file as File;
  // 处理文件
  return c.json({ message: 'File uploaded' });
});
```

### 12.2 如何实现 WebSocket？

Hono 本身不支持 WebSocket，但可以通过适配器实现：

```ts
// 使用 Cloudflare Workers 的 WebSocket 支持
export default {
  fetch: app.fetch,
  websocket: {
    async message(ws: WebSocket, message: string | ArrayBuffer) {
      ws.send(message);
    },
  },
};
```

---

**下一节**：[4.2.6 Elysia 简介](section-06-elysia.md)
