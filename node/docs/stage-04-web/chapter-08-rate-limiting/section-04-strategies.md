# 4.8.4 限流策略

## 1. 概述

限流策略是根据不同场景和需求制定的限流规则。合理的限流策略可以平衡用户体验和服务稳定性，保护 API 服务不被滥用。

## 2. 分层限流策略

### 2.1 全局限流

```ts
import rateLimit from 'express-rate-limit';

// 全局限流：保护整个应用
const globalLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 1000, // 全局限制较宽松
  message: 'Too many requests from this IP'
});

app.use(globalLimiter);
```

### 2.2 API 限流

```ts
// API 限流：保护 API 端点
const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100,
  message: 'Too many API requests'
});

app.use('/api/', apiLimiter);
```

### 2.3 端点限流

```ts
// 端点限流：保护特定端点
const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 5, // 登录接口限制更严格
  message: 'Too many login attempts'
});

app.post('/api/login', loginLimiter, loginHandler);
```

## 3. 基于用户的限流

### 3.1 认证用户限流

```ts
const authenticatedLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 200,
  keyGenerator: (req: Request): string => {
    return req.user?.id || req.ip;
  },
  skip: (req: Request): boolean => {
    return !req.user; // 跳过未认证用户
  }
});

app.use('/api/protected', authenticatedLimiter);
```

### 3.2 用户等级限流

```ts
const userLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: (req: Request): number => {
    // 根据用户等级设置不同限制
    const limits: Record<string, number> = {
      'free': 100,
      'premium': 1000,
      'enterprise': 10000
    };
    return limits[req.user?.plan || 'free'] || 100;
  },
  keyGenerator: (req: Request): string => {
    return req.user?.id || req.ip;
  }
});
```

## 4. 基于 IP 的限流

### 4.1 基本 IP 限流

```ts
const ipLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100,
  keyGenerator: (req: Request): string => {
    return req.ip;
  }
});
```

### 4.2 IP 白名单

```ts
const ipLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100,
  skip: (req: Request): boolean => {
    const whitelist = ['127.0.0.1', '::1', '192.168.1.1'];
    return whitelist.includes(req.ip);
  }
});
```

### 4.3 IP 黑名单

```ts
const blacklist = new Set<string>(['1.2.3.4', '5.6.7.8']);

const ipLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100,
  skip: (req: Request): boolean => {
    return blacklist.has(req.ip); // 黑名单直接拒绝
  },
  handler: (req: Request, res: Response): void => {
    if (blacklist.has(req.ip)) {
      res.status(403).json({ error: 'IP blocked' });
    } else {
      res.status(429).json({ error: 'Too many requests' });
    }
  }
});
```

## 5. 动态限流

### 5.1 基于负载的限流

```ts
import { cpus } from 'node:os';

function getSystemLoad(): number {
  const load = cpus().length;
  return load;
}

const dynamicLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: (req: Request): number => {
    const load = getSystemLoad();
    // 负载高时降低限流阈值
    if (load > 0.8) {
      return 50;
    } else if (load > 0.5) {
      return 100;
    } else {
      return 200;
    }
  }
});
```

### 5.2 基于时间的限流

```ts
const timeBasedLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: (req: Request): number => {
    const hour = new Date().getHours();
    // 高峰时段降低限流阈值
    if (hour >= 9 && hour <= 17) {
      return 50; // 工作时间
    } else {
      return 200; // 非工作时间
    }
  }
});
```

## 6. 组合限流策略

### 6.1 多层限流

```ts
// 第一层：全局限流
const globalLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 1000
});

// 第二层：API 限流
const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100
});

// 第三层：端点限流
const endpointLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 10
});

app.use(globalLimiter);
app.use('/api/', apiLimiter);
app.post('/api/login', endpointLimiter, loginHandler);
```

### 6.2 不同算法的组合

```ts
import Bottleneck from 'bottleneck';

// 使用 bottleneck 实现并发限制
const concurrentLimiter = new Bottleneck({
  maxConcurrent: 10
});

// 使用 express-rate-limit 实现速率限制
const rateLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100
});

app.use(rateLimiter);
app.use(async (req: Request, res: Response, next: NextFunction): Promise<void> => {
  await concurrentLimiter.schedule(async (): Promise<void> => {
    next();
  });
});
```

## 7. 限流监控

### 7.1 限流统计

```ts
interface RateLimitStats {
  total: number;
  blocked: number;
  byEndpoint: Record<string, number>;
}

const stats: RateLimitStats = {
  total: 0,
  blocked: 0,
  byEndpoint: {}
};

const monitoredLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100,
  onLimitReached: (req: Request, res: Response): void => {
    stats.blocked++;
    stats.byEndpoint[req.path] = (stats.byEndpoint[req.path] || 0) + 1;
  }
});

app.get('/api/stats', (req: Request, res: Response): void => {
  res.json(stats);
});
```

## 8. 最佳实践

### 8.1 策略选择

- **公开 API**：使用基于 IP 的限流
- **认证 API**：使用基于用户的限流
- **敏感操作**：使用更严格的限流

### 8.2 错误处理

- 提供清晰的错误信息
- 返回重试时间
- 记录限流事件

### 8.3 性能优化

- 使用 Redis 存储（多服务器）
- 使用内存存储（单服务器）
- 优化限流检查逻辑

## 9. 注意事项

- **用户体验**：限流不应过度影响正常用户
- **灵活性**：支持不同场景的限流策略
- **监控**：监控限流效果和影响
- **调整**：根据实际情况调整限流参数

## 10. 常见问题

### 10.1 如何设置合理的限流值？

根据 API 性能、用户需求和业务场景设置，需要测试和调整。

### 10.2 如何处理限流误杀？

实现白名单机制，对特定用户或 IP 放宽限制。

### 10.3 如何实现动态限流？

使用自定义 max 函数和系统负载监控实现动态限流。

## 11. 实践任务

1. **实现分层限流**：实现全局、API、端点三层限流
2. **实现用户限流**：实现基于用户的限流策略
3. **实现动态限流**：实现基于负载的动态限流
4. **实现限流监控**：实现限流统计和监控
5. **优化限流性能**：优化限流实现和存储方案

---

**下一章**：[4.9 配置管理](../chapter-09-config/readme.md)
