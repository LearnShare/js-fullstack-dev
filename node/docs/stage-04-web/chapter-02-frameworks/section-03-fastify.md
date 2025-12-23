# 4.2.3 Fastify 简介

## 1. 概述

Fastify 是一个高性能的现代 Web 框架，专注于提供最佳的性能和开发体验。Fastify 采用插件架构，支持 TypeScript，提供了强大的类型推断和验证功能。相比 Express，Fastify 在性能上有显著提升，同时保持了简洁的 API 设计。

## 2. 特性说明

- **高性能**：基于高性能的 HTTP 服务器，性能优于 Express
- **插件系统**：强大的插件系统，支持功能扩展
- **TypeScript 支持**：原生支持 TypeScript，提供类型推断
- **JSON Schema 验证**：内置 JSON Schema 验证
- **日志系统**：内置高性能日志系统
- **低开销**：最小化开销，适合高性能场景

## 3. 安装与初始化

### 3.1 安装

```bash
npm install fastify
npm install --save-dev @types/node
```

### 3.2 基本使用

```ts
import Fastify, { FastifyRequest, FastifyReply } from 'fastify';

const fastify = Fastify({
  logger: true
});

fastify.get('/', async (request: FastifyRequest, reply: FastifyReply) => {
  return { message: 'Hello World' };
});

const start = async () => {
  try {
    await fastify.listen({ port: 3000 });
    console.log('Server running on http://localhost:3000');
  } catch (err) {
    fastify.log.error(err);
    process.exit(1);
  }
};

start();
```

## 4. 路由系统

### 4.1 基本路由

```ts
// GET 路由
fastify.get('/users', async (request: FastifyRequest, reply: FastifyReply) => {
  return { users: [] };
});

// POST 路由
fastify.post('/users', async (request: FastifyRequest, reply: FastifyReply) => {
  return { message: 'User created' };
});

// PUT 路由
fastify.put('/users/:id', async (request: FastifyRequest, reply: FastifyReply) => {
  const { id } = request.params as { id: string };
  return { message: `User ${id} updated` };
});

// DELETE 路由
fastify.delete('/users/:id', async (request: FastifyRequest, reply: FastifyReply) => {
  const { id } = request.params as { id: string };
  return { message: `User ${id} deleted` };
});
```

### 4.2 路由参数

```ts
// 路径参数
fastify.get('/users/:id', async (request: FastifyRequest, reply: FastifyReply) => {
  const { id } = request.params as { id: string };
  return { userId: id };
});

// 查询参数
fastify.get('/users', async (request: FastifyRequest, reply: FastifyReply) => {
  const { page, limit } = request.query as { page?: string; limit?: string };
  return { page, limit };
});
```

### 4.3 路由模块化

```ts
// routes/users.ts
import { FastifyInstance } from 'fastify';

async function usersRoutes(fastify: FastifyInstance) {
  fastify.get('/', async (request: FastifyRequest, reply: FastifyReply) => {
    return { users: [] };
  });

  fastify.get('/:id', async (request: FastifyRequest, reply: FastifyReply) => {
    const { id } = request.params as { id: string };
    return { userId: id };
  });
}

export default usersRoutes;

// app.ts
import Fastify, { FastifyRequest, FastifyReply } from 'fastify';
import usersRoutes from './routes/users';

const fastify = Fastify({ logger: true });

fastify.register(usersRoutes, { prefix: '/users' });

const start = async () => {
  try {
    await fastify.listen({ port: 3000 });
  } catch (err) {
    fastify.log.error(err);
    process.exit(1);
  }
};

start();
```

## 5. JSON Schema 验证

### 5.1 请求验证

```ts
interface CreateUserBody {
  name: string;
  email: string;
}

const createUserSchema = {
  body: {
    type: 'object',
    required: ['name', 'email'],
    properties: {
      name: { type: 'string', minLength: 1 },
      email: { type: 'string', format: 'email' }
    }
  }
};

fastify.post<{ Body: CreateUserBody }>(
  '/users',
  { schema: createUserSchema },
  async (request: FastifyRequest<{ Body: CreateUserBody }>, reply: FastifyReply) => {
    const { name, email } = request.body;
    return { id: 1, name, email };
  }
);
```

### 5.2 响应验证

```ts
const getUserSchema = {
  response: {
    200: {
      type: 'object',
      properties: {
        id: { type: 'number' },
        name: { type: 'string' },
        email: { type: 'string' }
      }
    }
  }
};

fastify.get('/users/:id', { schema: getUserSchema }, async (request: FastifyRequest, reply: FastifyReply) => {
  const { id } = request.params as { id: string };
  return { id: parseInt(id), name: 'John', email: 'john@example.com' };
});
```

## 6. 插件系统

### 6.1 使用插件

```ts
import cors from '@fastify/cors';
import helmet from '@fastify/helmet';
import rateLimit from '@fastify/rate-limit';

// 注册插件
await fastify.register(cors);
await fastify.register(helmet);
await fastify.register(rateLimit, {
  max: 100,
  timeWindow: '1 minute'
});
```

### 6.2 创建插件

```ts
// plugins/auth.ts
import { FastifyInstance, FastifyPluginOptions } from 'fastify';

async function authPlugin(
  fastify: FastifyInstance,
  options: FastifyPluginOptions
) {
  fastify.decorate('authenticate', async (request: FastifyRequest, reply: FastifyReply) => {
    const token = request.headers.authorization;
    if (!token) {
      reply.code(401).send({ error: 'Unauthorized' });
    }
  });
}

export default authPlugin;

// 使用插件
await fastify.register(authPlugin);
```

## 7. 钩子（Hooks）

### 7.1 请求钩子

```ts
// onRequest - 请求开始时
fastify.addHook('onRequest', async (request: FastifyRequest, reply: FastifyReply) => {
  console.log(`${request.method} ${request.url}`);
});

// preHandler - 处理前
fastify.addHook('preHandler', async (request: FastifyRequest, reply: FastifyReply) => {
  // 执行预处理
});

// onResponse - 响应后
fastify.addHook('onResponse', async (request: FastifyRequest, reply: FastifyReply) => {
  console.log(`Response time: ${reply.getResponseTime()}ms`);
});
```

### 7.2 错误钩子

```ts
fastify.setErrorHandler((error: Error, request: FastifyRequest, reply: FastifyReply) => {
  fastify.log.error(error);
  reply.status(500).send({
    error: {
      message: 'Internal Server Error'
    }
  });
});
```

## 8. 完整示例

```ts
import Fastify, { FastifyInstance } from 'fastify';
import cors from '@fastify/cors';
import helmet from '@fastify/helmet';

const fastify = Fastify({
  logger: true
});

// 注册插件
await fastify.register(cors);
await fastify.register(helmet);

// 路由
fastify.get('/', async (request: FastifyRequest, reply: FastifyReply) => {
  return { message: 'Hello World' };
});

interface CreateUserBody {
  name: string;
  email: string;
}

const createUserSchema = {
  body: {
    type: 'object',
    required: ['name', 'email'],
    properties: {
      name: { type: 'string', minLength: 1 },
      email: { type: 'string', format: 'email' }
    }
  }
};

fastify.post<{ Body: CreateUserBody }>(
  '/users',
  { schema: createUserSchema },
  async (request: FastifyRequest, reply: FastifyReply) => {
    const { name, email } = request.body;
    reply.code(201).send({
      data: {
        id: 1,
        name,
        email
      }
    });
  }
);

// 错误处理
fastify.setErrorHandler((error: Error, request: FastifyRequest, reply: FastifyReply) => {
  fastify.log.error(error);
  reply.status(500).send({
    error: {
      message: 'Internal Server Error'
    }
  });
});

// 404 处理
fastify.setNotFoundHandler((request: FastifyRequest, reply: FastifyReply) => {
  reply.status(404).send({
    error: {
      message: 'Not Found'
    }
  });
});

const start = async () => {
  try {
    await fastify.listen({ port: 3000, host: '0.0.0.0' });
    console.log('Server running on http://localhost:3000');
  } catch (err) {
    fastify.log.error(err);
    process.exit(1);
  }
};

start();
```

## 9. 性能优化

### 9.1 性能特点

- **高性能 HTTP 服务器**：基于高性能的 HTTP 服务器实现
- **JSON 序列化优化**：优化的 JSON 序列化性能
- **低开销**：最小化框架开销
- **异步处理**：完全异步的处理机制

### 9.2 性能对比

Fastify 相比 Express 在性能上有显著提升：

- **请求处理速度**：快 2-3 倍
- **JSON 序列化**：快 2-3 倍
- **内存占用**：更低

## 10. 最佳实践

### 10.1 使用 TypeScript

充分利用 TypeScript 的类型推断：

```ts
interface RouteParams {
  id: string;
}

interface RouteQuery {
  page?: string;
  limit?: string;
}

interface RouteBody {
  name: string;
  email: string;
}

fastify.get<{ Params: RouteParams; Querystring: RouteQuery }>(
  '/users/:id',
  async (request: FastifyRequest, reply: FastifyReply) => {
    const { id } = request.params;
    const { page, limit } = request.query;
    // TypeScript 类型推断
  }
);
```

### 10.2 使用 JSON Schema

充分利用 JSON Schema 验证：

```ts
const schema = {
  body: {
    type: 'object',
    required: ['name', 'email'],
    properties: {
      name: { type: 'string', minLength: 1 },
      email: { type: 'string', format: 'email' }
    }
  }
};

fastify.post('/users', { schema }, async (request: FastifyRequest, reply: FastifyReply) => {
  // 请求已自动验证
});
```

## 11. 注意事项

- **插件顺序**：注意插件的注册顺序
- **异步处理**：所有路由处理函数都应该是异步的
- **错误处理**：实现完整的错误处理机制
- **类型安全**：充分利用 TypeScript 类型系统

## 12. 常见问题

### 12.1 如何处理文件上传？

使用 `@fastify/multipart` 插件：

```ts
import multipart from '@fastify/multipart';

await fastify.register(multipart);

fastify.post('/upload', async (request: FastifyRequest, reply: FastifyReply) => {
  const data = await request.file();
  // 处理文件
});
```

### 12.2 如何实现认证？

使用装饰器和钩子：

```ts
fastify.decorate('authenticate', async (request: FastifyRequest, reply: FastifyReply) => {
  const token = request.headers.authorization;
  if (!token) {
    reply.code(401).send({ error: 'Unauthorized' });
  }
});

fastify.addHook('preHandler', async (request: FastifyRequest, reply: FastifyReply) => {
  if (request.url.startsWith('/api')) {
    await fastify.authenticate(request, reply);
  }
});
```

---

**下一节**：[4.2.4 NestJS 简介](section-04-nestjs.md)
