# 4.2.6 Elysia 简介

## 1. 概述

Elysia 是一个基于 Bun 运行时的现代 Web 框架，专注于提供最佳的性能和开发体验。Elysia 采用 TypeScript 优先的设计，提供了强大的类型推断、验证和性能优化。Elysia 充分利用 Bun 运行时的特性，提供了极快的启动速度和执行性能。

## 2. 特性说明

- **Bun 运行时**：专为 Bun 运行时优化
- **TypeScript 优先**：原生支持 TypeScript，提供强大的类型推断
- **高性能**：极快的启动速度和执行性能
- **类型安全**：端到端的类型安全
- **简洁 API**：简洁直观的 API 设计
- **插件系统**：强大的插件系统

## 3. 安装与初始化

### 3.1 安装

```bash
bun add elysia
```

### 3.2 基本使用

```ts
import { Elysia } from 'elysia';

const app = new Elysia()
  .get('/', (): string => 'Hello World')
  .listen(3000);

console.log('Server running on http://localhost:3000');
```

## 4. 路由系统

### 4.1 基本路由

```ts
import { Elysia, Context } from 'elysia';

interface UserBody {
  name: string;
  email: string;
}

interface UserParams {
  id: string;
}

const app = new Elysia()
  .get('/users', (): { users: never[] } => ({ users: [] }))
  .post('/users', ({ body }: Context<{ body: UserBody }>) => ({ message: 'User created', data: body }))
  .put('/users/:id', ({ params, body }: Context<{ params: UserParams; body: UserBody }>) => ({
    message: `User ${params.id} updated`,
    data: body,
  }))
  .delete('/users/:id', ({ params }: Context<{ params: UserParams }>) => ({
    message: `User ${params.id} deleted`,
  }))
  .listen(3000);
```

### 4.2 路由参数

```ts
import { Context } from 'elysia';

interface UserParams {
  id: string;
}

interface UserQuery {
  page?: string;
  limit?: string;
}

interface UserBody {
  name: string;
  email: string;
}

// 路径参数
app.get('/users/:id', ({ params }: Context<{ params: UserParams }>) => {
  return { userId: params.id };
});

// 查询参数
app.get('/users', ({ query }: Context<{ query: UserQuery }>) => {
  return { page: query.page, limit: query.limit };
});

// 请求体
app.post('/users', ({ body }: Context<{ body: UserBody }>) => {
  return { data: body };
});
```

### 4.3 路由分组

```ts
import { Elysia, Context } from 'elysia';

interface UserParams {
  id: string;
}

const users = new Elysia()
  .get('/', (): { users: never[] } => ({ users: [] }))
  .get('/:id', ({ params }: Context<{ params: UserParams }>) => ({ userId: params.id }));

const app = new Elysia().group('/users', (app: Elysia) => app.use(users)).listen(3000);
```

## 5. 类型安全

### 5.1 类型推断

```ts
import { Elysia, t, Context } from 'elysia';

interface UserParams {
  id: string;
}

interface CreateUserBody {
  name: string;
  email: string;
}

const app = new Elysia()
  .get('/users/:id', ({ params }: Context<{ params: UserParams }>) => {
    // params.id 类型推断为 string
    return { userId: params.id };
  })
  .post(
    '/users',
    ({ body }: Context<{ body: CreateUserBody }>) => {
      // body 类型推断
      return { data: body };
    },
    {
      body: t.Object({
        name: t.String(),
        email: t.String({ format: 'email' }),
      }),
    }
  )
  .listen(3000);
```

### 5.2 验证器

```ts
import { Elysia, t, Context } from 'elysia';

interface CreateUserBody {
  name: string;
  email: string;
}

const app = new Elysia()
  .post(
    '/users',
    ({ body }: Context<{ body: CreateUserBody }>) => {
      return { data: body };
    },
    {
      body: t.Object({
        name: t.String({ minLength: 1 }),
        email: t.String({ format: 'email' }),
      }),
    }
  )
  .listen(3000);
```

## 6. 中间件

### 6.1 内置中间件

```ts
import { Elysia } from 'elysia';
import { cors } from '@elysiajs/cors';
import { swagger } from '@elysiajs/swagger';

const app = new Elysia()
  .use(cors())
  .use(swagger())
  .get('/', () => 'Hello World')
  .listen(3000);
```

### 6.2 自定义中间件

```ts
import { Context } from 'elysia';

// 日志中间件
app.derive(({ request }: Context<{ request: Request }>) => {
  console.log(`${request.method} ${request.url}`);
});

// 认证中间件
app.onBeforeHandle(({ request, set }: Context<{ request: Request; set: { status: number } }>) => {
  const token = request.headers.get('Authorization');
  if (!token) {
    set.status = 401;
    return { error: 'Unauthorized' };
  }
});
```

## 7. 插件系统

### 7.1 使用插件

```ts
import { Elysia } from 'elysia';
import { cors } from '@elysiajs/cors';
import { swagger } from '@elysiajs/swagger';
import { jwt } from '@elysiajs/jwt';

const app = new Elysia()
  .use(cors())
  .use(swagger())
  .use(jwt({ secret: 'secret' }))
  .get('/', () => 'Hello World')
  .listen(3000);
```

### 7.2 创建插件

```ts
import { Elysia, Context } from 'elysia';

interface User {
  id: number;
  name: string;
}

const authPlugin = new Elysia()
  .derive(({ request }: Context<{ request: Request }>) => {
    const token = request.headers.get('Authorization');
    return {
      user: token ? { id: 1, name: 'John' } : null,
    };
  })
  .onBeforeHandle(({ user, set }: Context<{ user: User | null; set: { status: number } }>) => {
    if (!user) {
      set.status = 401;
      return { error: 'Unauthorized' };
    }
  });

const app = new Elysia().use(authPlugin).get('/profile', ({ user }: Context<{ user: User }>) => {
  return { user };
});
```

## 8. 完整示例

```ts
import { Elysia, t, Context } from 'elysia';
import { cors } from '@elysiajs/cors';
import { swagger } from '@elysiajs/swagger';

interface UserParams {
  id: string;
}

interface UserQuery {
  page?: string;
  limit?: string;
}

interface CreateUserBody {
  name: string;
  email: string;
}

const app = new Elysia()
  .use(cors())
  .use(swagger())
  .get('/', (): { message: string } => ({ message: 'Hello World' }))
  .get(
    '/users',
    ({ query }: Context<{ query: UserQuery }>) => {
      const page = query.page || '1';
      const limit = query.limit || '20';
      return {
        data: [],
        pagination: {
          page: parseInt(page),
          limit: parseInt(limit),
        },
      };
    },
    {
      query: t.Object({
        page: t.Optional(t.String()),
        limit: t.Optional(t.String()),
      }),
    }
  )
  .post(
    '/users',
    ({ body }: Context<{ body: CreateUserBody }>) => {
      return { message: 'User created', data: body };
    },
    {
      body: t.Object({
        name: t.String({ minLength: 1 }),
        email: t.String({ format: 'email' }),
      }),
    }
  )
  .get('/users/:id', ({ params }: Context<{ params: UserParams }>) => {
    return { userId: params.id };
  })
  .onError(({ code, error }: Context<{ code: string; error: Error }>) => {
    console.error(error);
    return { error: 'Internal Server Error' };
  })
  .listen(3000);

console.log('Server running on http://localhost:3000');
```

## 9. 性能优化

### 9.1 性能特点

- **极快的启动**：利用 Bun 运行时的快速启动
- **高性能执行**：优化的执行性能
- **低内存占用**：最小化内存占用
- **类型安全**：编译时类型检查，运行时无类型开销

### 9.2 Bun 运行时优势

- **原生 TypeScript 支持**：无需编译，直接运行 TypeScript
- **快速启动**：极快的启动时间
- **高性能**：优化的 JavaScript 引擎
- **内置工具**：内置包管理器、测试工具等

## 10. 最佳实践

### 10.1 类型安全

充分利用 TypeScript 类型系统：

```ts
import { Elysia, t, Context } from 'elysia';

interface CreateUserBody {
  name: string;
  email: string;
}

const app = new Elysia()
  .post(
    '/users',
    ({ body }: Context<{ body: CreateUserBody }>) => {
      // body 类型自动推断
      return { data: body };
    },
    {
      body: t.Object({
        name: t.String(),
        email: t.String({ format: 'email' }),
      }),
    }
  )
  .listen(3000);
```

### 10.2 插件组织

按功能组织插件：

```ts
import { Elysia, Context } from 'elysia';

const authPlugin = new Elysia().derive(({ request }: Context<{ request: Request }>) => {
  // 认证逻辑
});

const app = new Elysia().use(authPlugin);
```

## 11. 注意事项

- **Bun 运行时**：Elysia 专为 Bun 运行时设计，需要 Bun 环境
- **类型安全**：充分利用 TypeScript 类型系统
- **性能优化**：注意 Bun 运行时的性能特点
- **插件生态**：关注插件生态的发展

## 12. 常见问题

### 12.1 如何处理文件上传？

使用 `@elysiajs/static` 插件：

```ts
import { Elysia, Context } from 'elysia';
import { staticPlugin } from '@elysiajs/static';

const app = new Elysia()
  .use(staticPlugin())
  .post('/upload', ({ body }: Context<{ body: unknown }>) => {
    // 处理文件上传
  })
  .listen(3000);
```

### 12.2 如何实现 WebSocket？

使用 `@elysiajs/websocket` 插件：

```ts
import { Elysia } from 'elysia';
import { websocket } from '@elysiajs/websocket';

const app = new Elysia()
  .use(websocket())
  .ws('/ws', {
    message(ws: WebSocket, message: string | ArrayBuffer) {
      ws.send(message);
    },
  })
  .listen(3000);
```

---

**下一节**：[4.2.7 其他 Web 框架](section-07-other-frameworks.md)
