# 7.5.4 MSW（Mock Service Worker）

## 1. 概述

MSW（Mock Service Worker）是一个用于 Mock HTTP 请求的库，使用 Service Worker 拦截网络请求。MSW 可以在浏览器和 Node.js 环境中使用，适合 API Mock 和集成测试。

## 2. 特性说明

- **Service Worker**：使用 Service Worker 拦截请求
- **浏览器和 Node**：支持浏览器和 Node.js
- **真实请求**：拦截真实 HTTP 请求
- **类型安全**：支持 TypeScript

## 3. 安装与配置

### 3.1 安装

```bash
npm install -D msw
```

### 3.2 浏览器配置

```ts
// src/mocks/browser.ts
import { setupWorker } from 'msw/browser';
import { handlers } from './handlers';

export const worker = setupWorker(...handlers);
```

```ts
// src/main.ts
if (process.env.NODE_ENV === 'development') {
  const { worker } = await import('./mocks/browser');
  await worker.start();
}
```

### 3.3 Node.js 配置

```ts
// src/mocks/server.ts
import { setupServer } from 'msw/node';
import { handlers } from './handlers';

export const server = setupServer(...handlers);
```

```ts
// vitest.setup.ts
import { beforeAll, afterEach, afterAll } from 'vitest';
import { server } from './src/mocks/server';

beforeAll(() => server.listen({ onUnhandledRequest: 'error' }));
afterEach(() => server.resetHandlers());
afterAll(() => server.close());
```

## 4. 请求处理

### 4.1 定义 Handlers

```ts
// src/mocks/handlers.ts
import { http, HttpResponse } from 'msw';

export const handlers = [
  // GET 请求
  http.get('/api/users', () => {
    return HttpResponse.json([
      { id: 1, name: 'John', email: 'john@example.com' },
      { id: 2, name: 'Jane', email: 'jane@example.com' }
    ]);
  }),
  
  // POST 请求
  http.post('/api/users', async ({ request }) => {
    const body = await request.json() as { name: string; email: string };
    return HttpResponse.json(
      { id: 3, ...body },
      { status: 201 }
    );
  }),
  
  // 带参数的请求
  http.get('/api/users/:id', ({ params }) => {
    const { id } = params;
    return HttpResponse.json({ id: Number(id), name: 'John', email: 'john@example.com' });
  }),
  
  // 错误响应
  http.get('/api/users/999', () => {
    return HttpResponse.json(
      { error: 'User not found' },
      { status: 404 }
    );
  })
];
```

### 4.2 动态响应

```ts
http.get('/api/users', ({ request }) => {
  const url = new URL(request.url);
  const page = url.searchParams.get('page');
  const limit = url.searchParams.get('limit');
  
  return HttpResponse.json({
    data: [],
    page: Number(page) || 1,
    limit: Number(limit) || 10
  });
});
```

## 5. 测试使用

### 5.1 单元测试

```ts
import { describe, it, expect } from 'vitest';
import { server } from './mocks/server';
import { http, HttpResponse } from 'msw';

describe('User API', () => {
  it('should fetch users', async (): Promise<void> => {
    const response = await fetch('/api/users');
    const users = await response.json();
    
    expect(users).toHaveLength(2);
    expect(users[0].name).toBe('John');
  });
  
  it('should handle custom response', async (): Promise<void> => {
    server.use(
      http.get('/api/users', () => {
        return HttpResponse.json([{ id: 1, name: 'Custom User' }]);
      })
    );
    
    const response = await fetch('/api/users');
    const users = await response.json();
    
    expect(users).toHaveLength(1);
    expect(users[0].name).toBe('Custom User');
  });
});
```

### 5.2 E2E 测试

```ts
import { test, expect } from '@playwright/test';
import { server } from './mocks/server';

test.beforeEach(() => {
  server.listen({ onUnhandledRequest: 'error' });
});

test.afterEach(() => {
  server.resetHandlers();
});

test.afterAll(() => {
  server.close();
});

test('should display users', async ({ page }): Promise<void> => {
  await page.goto('/users');
  await expect(page.locator('.user-list')).toContainText('John');
});
```

## 6. 最佳实践

### 6.1 Handler 组织

- 按 API 端点组织
- 使用共享数据
- 保持 Handler 简单
- 支持动态响应

### 6.2 测试使用

- 在测试中覆盖 Handler
- 清理 Handler 状态
- 处理未匹配请求
- 验证请求参数

## 7. 注意事项

- **请求匹配**：确保请求正确匹配
- **Handler 顺序**：注意 Handler 顺序
- **状态管理**：管理 Handler 状态
- **性能考虑**：注意 Service Worker 性能

## 8. 常见问题

### 8.1 如何处理未匹配请求？

设置 `onUnhandledRequest` 选项，记录或错误处理。

### 8.2 如何在测试中动态修改响应？

使用 `server.use()` 在测试中覆盖 Handler。

### 8.3 如何共享测试数据？

创建共享的数据工厂函数。

## 9. 实践任务

1. **安装配置**：安装和配置 MSW
2. **定义 Handlers**：定义请求 Handlers
3. **测试使用**：在测试中使用 MSW
4. **动态响应**：实现动态响应
5. **最佳实践**：遵循 MSW 最佳实践

---

**下一章**：[7.6 测试驱动开发（TDD）](../chapter-06-tdd/readme.md)
