# 4.3.4 tRPC

## 1. 概述

tRPC 是一个端到端类型安全的 API 框架，专为 TypeScript 全栈应用设计。tRPC 无需代码生成，提供完整的类型安全，简化 API 开发流程。

## 2. 特性说明

- **端到端类型安全**：从客户端到服务器完全类型安全
- **无需代码生成**：直接使用 TypeScript 类型
- **轻量级**：极小的运行时开销
- **快速开发**：简化 API 开发流程
- **自动类型推断**：自动推断请求和响应类型

## 3. 安装与初始化

### 3.1 安装

```bash
npm install @trpc/server @trpc/client @trpc/react-query
npm install @tanstack/react-query
```

### 3.2 服务器端设置

```ts
import { initTRPC } from '@trpc/server';
import { z } from 'zod';

// 初始化 tRPC
const t = initTRPC.context<{ userId?: string }>().create();

// 导出路由器、过程和中间件
export const router = t.router;
export const publicProcedure = t.procedure;
```

### 3.3 基本路由器

```ts
import { router, publicProcedure } from './trpc';
import { z } from 'zod';

interface User {
  id: number;
  name: string;
  email: string;
}

const users: User[] = [
  { id: 1, name: 'John', email: 'john@example.com' },
  { id: 2, name: 'Jane', email: 'jane@example.com' }
];

export const appRouter = router({
  // 查询：获取所有用户
  getUsers: publicProcedure.query((): User[] => {
    return users;
  }),

  // 查询：根据 ID 获取用户
  getUserById: publicProcedure
    .input(z.object({ id: z.number() }))
    .query(({ input }: { input: { id: number } }): User | undefined => {
      return users.find((u: User) => u.id === input.id);
    }),

  // 变更：创建用户
  createUser: publicProcedure
    .input(z.object({
      name: z.string(),
      email: z.string().email()
    }))
    .mutation(({ input }: { input: { name: string; email: string } }): User => {
      const newUser: User = {
        id: users.length + 1,
        name: input.name,
        email: input.email
      };
      users.push(newUser);
      return newUser;
    }),

  // 变更：更新用户
  updateUser: publicProcedure
    .input(z.object({
      id: z.number(),
      name: z.string().optional(),
      email: z.string().email().optional()
    }))
    .mutation(({ input }: { input: { id: number; name?: string; email?: string } }): User | null => {
      const userIndex: number = users.findIndex((u: User) => u.id === input.id);
      if (userIndex === -1) return null;

      if (input.name) users[userIndex].name = input.name;
      if (input.email) users[userIndex].email = input.email;

      return users[userIndex];
    }),

  // 变更：删除用户
  deleteUser: publicProcedure
    .input(z.object({ id: z.number() }))
    .mutation(({ input }: { input: { id: number } }): boolean => {
      const userIndex: number = users.findIndex((u: User) => u.id === input.id);
      if (userIndex === -1) return false;

      users.splice(userIndex, 1);
      return true;
    })
});

export type AppRouter = typeof appRouter;
```

## 4. 与 Express 集成

### 4.1 Express 集成

```ts
import express, { Express } from 'express';
import { createExpressMiddleware } from '@trpc/server/adapters/express';
import { appRouter } from './router';

const app: Express = express();

app.use(
  '/trpc',
  createExpressMiddleware({
    router: appRouter,
    createContext: (): { userId?: string } => {
      // 从请求中获取用户信息
      return { userId: undefined };
    }
  })
);

app.listen(3000, (): void => {
  console.log('tRPC server ready at http://localhost:3000/trpc');
});
```

### 4.2 Fastify 集成

```ts
import { FastifyInstance } from 'fastify';
import { fastifyTRPCPlugin } from '@trpc/server/adapters/fastify';
import { appRouter } from './router';

export default async function (fastify: FastifyInstance): Promise<void> {
  await fastify.register(fastifyTRPCPlugin, {
    prefix: '/trpc',
    trpcOptions: {
      router: appRouter,
      createContext: (): { userId?: string } => {
        return { userId: undefined };
      }
    }
  });
}
```

## 5. 客户端使用

### 5.1 React 客户端

```ts
import { createTRPCReact } from '@trpc/react-query';
import { httpBatchLink } from '@trpc/client';
import type { AppRouter } from './server/router';

export const trpc = createTRPCReact<AppRouter>();

function App(): JSX.Element {
  const trpcClient = trpc.createClient({
    links: [
      httpBatchLink({
        url: 'http://localhost:3000/trpc'
      })
    ]
  });

  return (
    <trpc.Provider client={trpcClient} queryClient={queryClient}>
      <Users />
    </trpc.Provider>
  );
}

function Users(): JSX.Element {
  const { data, isLoading } = trpc.getUsers.useQuery();

  if (isLoading) return <div>Loading...</div>;

  return (
    <div>
      {data?.map((user: User) => (
        <div key={user.id}>{user.name}</div>
      ))}
    </div>
  );
}
```

### 5.2 原生客户端

```ts
import { createTRPCProxyClient, httpBatchLink } from '@trpc/client';
import type { AppRouter } from './server/router';

const trpc = createTRPCProxyClient<AppRouter>({
  links: [
    httpBatchLink({
      url: 'http://localhost:3000/trpc'
    })
  ]
});

// 使用
const users = await trpc.getUsers.query();
const user = await trpc.getUserById.query({ id: 1 });
const newUser = await trpc.createUser.mutate({ name: 'Alice', email: 'alice@example.com' });
```

## 6. 中间件

### 6.1 认证中间件

```ts
import { TRPCError } from '@trpc/server';

const isAuthenticated = t.middleware(({ ctx, next }: { ctx: { userId?: string }; next: () => any }) => {
  if (!ctx.userId) {
    throw new TRPCError({ code: 'UNAUTHORIZED' });
  }
  return next({
    ctx: {
      userId: ctx.userId
    }
  });
});

export const protectedProcedure = t.procedure.use(isAuthenticated);
```

### 6.2 日志中间件

```ts
const logger = t.middleware(async ({ path, type, next }: { path: string; type: string; next: () => any }) => {
  const start = Date.now();
  const result = await next();
  const duration = Date.now() - start;
  
  console.log(`${type} ${path} - ${duration}ms`);
  
  return result;
});

export const loggedProcedure = t.procedure.use(logger);
```

## 7. 错误处理

### 7.1 自定义错误

```ts
import { TRPCError } from '@trpc/server';

export const appRouter = router({
  getUserById: publicProcedure
    .input(z.object({ id: z.number() }))
    .query(({ input }: { input: { id: number } }): User => {
      const user: User | undefined = users.find((u: User) => u.id === input.id);
      
      if (!user) {
        throw new TRPCError({
          code: 'NOT_FOUND',
          message: 'User not found'
        });
      }
      
      return user;
    })
});
```

### 7.2 错误格式化

```ts
import { TRPCError, initTRPC } from '@trpc/server';

const t = initTRPC.context<Context>().create({
  errorFormatter({ shape, error }) {
    return {
      ...shape,
      data: {
        ...shape.data,
        zodError: error.cause instanceof z.ZodError ? error.cause.flatten() : null
      }
    };
  }
});
```

## 8. 数据验证

### 8.1 Zod 验证

```ts
import { z } from 'zod';

export const appRouter = router({
  createUser: publicProcedure
    .input(z.object({
      name: z.string().min(1).max(100),
      email: z.string().email(),
      age: z.number().int().min(0).max(150).optional()
    }))
    .mutation(({ input }: { input: { name: string; email: string; age?: number } }): User => {
      // input 已经通过验证
      const newUser: User = {
        id: users.length + 1,
        name: input.name,
        email: input.email
      };
      users.push(newUser);
      return newUser;
    })
});
```

## 9. 最佳实践

### 9.1 路由器组织

```ts
// routers/users.ts
export const usersRouter = router({
  getUsers: publicProcedure.query((): User[] => users),
  getUserById: publicProcedure.input(z.object({ id: z.number() })).query(({ input }) => {
    return users.find((u: User) => u.id === input.id);
  })
});

// routers/index.ts
export const appRouter = router({
  users: usersRouter,
  posts: postsRouter
});
```

### 9.2 类型导出

```ts
// 导出类型供客户端使用
export type AppRouter = typeof appRouter;
```

### 9.3 上下文创建

```ts
createContext: async (opts: { req: Request; res: Response }): Promise<Context> => {
  const token = opts.req.headers.authorization;
  const user = await getUserFromToken(token);
  
  return {
    userId: user?.id,
    user
  };
}
```

## 10. 注意事项

- **类型安全**：充分利用 TypeScript 类型系统
- **错误处理**：实现统一的错误处理机制
- **性能优化**：使用批量链接减少请求次数
- **安全性**：实现认证和授权机制

## 11. 常见问题

### 11.1 tRPC 和 RESTful 的区别？

tRPC 提供端到端类型安全，无需代码生成；RESTful 需要手动维护类型定义。

### 11.2 如何处理文件上传？

使用 RESTful API 或 GraphQL 处理文件上传，tRPC 主要用于数据操作。

### 11.3 如何实现分页？

使用输入验证定义分页参数：

```ts
.input(z.object({
  page: z.number().int().min(1),
  limit: z.number().int().min(1).max(100)
}))
```

## 12. 实践任务

1. **实现基本 tRPC API**：实现用户 CRUD 的 tRPC API
2. **实现认证**：实现 tRPC 认证和授权机制
3. **实现中间件**：实现日志和认证中间件
4. **客户端集成**：在 React 应用中集成 tRPC 客户端
5. **错误处理**：实现统一的错误处理机制

---

**下一节**：[4.3.5 gRPC](section-05-grpc.md)
