# 4.8.2 express-rate-limit

## 1. 概述

express-rate-limit 是一个 Express 中间件，用于限制 API 请求频率。express-rate-limit 提供了简单易用的 API，支持多种存储后端和灵活的配置选项。

## 2. 特性说明

- **Express 中间件**：专为 Express 设计
- **多种存储**：支持内存、Redis 等存储
- **灵活配置**：提供丰富的配置选项
- **TypeScript 支持**：提供类型定义

## 3. 安装与初始化

### 3.1 安装

```bash
npm install express-rate-limit
```

### 3.2 基本使用

```ts
import express, { Express, Request, Response } from 'express';
import rateLimit from 'express-rate-limit';

const app: Express = express();

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 分钟
  max: 100, // 限制 100 次请求
  message: 'Too many requests from this IP, please try again later.'
});

app.use('/api/', limiter);

app.get('/api/users', (req: Request, res: Response): void => {
  res.json({ users: [] });
});

app.listen(3000, (): void => {
  console.log('Server running on port 3000');
});
```

## 4. 配置选项

### 4.1 基本配置

```ts
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 时间窗口：15 分钟
  max: 100, // 最大请求数：100 次
  message: 'Too many requests', // 错误消息
  standardHeaders: true, // 返回标准限流头
  legacyHeaders: false, // 禁用旧版限流头
  skipSuccessfulRequests: false, // 是否跳过成功请求
  skipFailedRequests: false // 是否跳过失败请求
});
```

### 4.2 自定义键生成

```ts
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100,
  keyGenerator: (req: Request): string => {
    // 基于用户 ID 限流
    return req.user?.id || req.ip;
  }
});
```

### 4.3 自定义跳过条件

```ts
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100,
  skip: (req: Request): boolean => {
    // 跳过管理员请求
    return req.user?.role === 'admin';
  }
});
```

## 5. 不同端点的限流

### 5.1 全局限流

```ts
const globalLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100
});

app.use(globalLimiter);
```

### 5.2 特定端点限流

```ts
const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 5, // 登录接口限制更严格
  message: 'Too many login attempts, please try again later.'
});

app.post('/api/login', loginLimiter, (req: Request, res: Response): void => {
  // 登录逻辑
});

const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100
});

app.use('/api/', apiLimiter);
```

### 5.3 不同限流策略

```ts
// 严格限流（登录）
const strictLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 5
});

// 中等限流（一般 API）
const moderateLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100
});

// 宽松限流（公开接口）
const lenientLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 1000
});

app.post('/api/login', strictLimiter, loginHandler);
app.use('/api/users', moderateLimiter);
app.use('/api/public', lenientLimiter);
```

## 6. Redis 存储

### 6.1 安装 Redis 存储

```bash
npm install rate-limit-redis
```

### 6.2 使用 Redis 存储

```ts
import RedisStore from 'rate-limit-redis';
import { createClient } from 'redis';

const redisClient = createClient({
  url: process.env.REDIS_URL
});

await redisClient.connect();

const limiter = rateLimit({
  store: new RedisStore({
    client: redisClient,
    prefix: 'rl:'
  }),
  windowMs: 15 * 60 * 1000,
  max: 100
});
```

## 7. 自定义响应

### 7.1 自定义错误响应

```ts
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100,
  handler: (req: Request, res: Response): void => {
    res.status(429).json({
      error: 'Too many requests',
      retryAfter: Math.ceil(15 * 60)
    });
  }
});
```

### 7.2 自定义响应头

```ts
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100,
  standardHeaders: true,
  legacyHeaders: false,
  handler: (req: Request, res: Response): void => {
    res.setHeader('X-RateLimit-Limit', '100');
    res.setHeader('X-RateLimit-Remaining', '0');
    res.setHeader('X-RateLimit-Reset', new Date(Date.now() + 15 * 60 * 1000).toISOString());
    res.status(429).json({ error: 'Too many requests' });
  }
});
```

## 8. 最佳实践

### 8.1 分层限流

```ts
// 全局限流
const globalLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 1000
});

// API 限流
const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100
});

// 端点限流
const endpointLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 10
});

app.use(globalLimiter);
app.use('/api/', apiLimiter);
app.post('/api/login', endpointLimiter, loginHandler);
```

### 8.2 白名单机制

```ts
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100,
  skip: (req: Request): boolean => {
    // 跳过白名单 IP
    const whitelist = ['127.0.0.1', '::1'];
    return whitelist.includes(req.ip);
  }
});
```

## 9. 注意事项

- **存储选择**：单服务器用内存，多服务器用 Redis
- **性能影响**：限流本身消耗资源，需要优化
- **用户体验**：提供清晰的错误信息和重试建议
- **监控**：监控限流效果和影响

## 10. 常见问题

### 10.1 如何处理多服务器场景？

使用 Redis 存储，确保所有服务器共享限流状态。

### 10.2 如何实现动态限流？

使用自定义 keyGenerator 和 skip 函数实现动态限流。

### 10.3 限流对性能的影响？

使用 Redis 存储时注意 Redis 性能，使用内存存储时注意内存使用。

## 11. 实践任务

1. **实现基本限流**：实现基本的 API 限流功能
2. **实现分层限流**：实现全局、API、端点三层限流
3. **集成 Redis**：使用 Redis 存储限流状态
4. **实现白名单**：实现白名单机制
5. **监控限流**：实现限流监控和统计

---

**下一节**：[4.8.3 bottleneck](section-03-bottleneck.md)
