# 4.8.1 API 限流概述

## 1. 概述

API 限流是一种保护 API 服务的机制，通过限制客户端在特定时间内的请求次数，防止服务过载、资源滥用和恶意攻击。API 限流是 Web 应用安全性和稳定性的重要保障。

## 2. 核心概念

### 2.1 限流的目的

- **防止过载**：保护服务器不被过多请求压垮
- **防止滥用**：防止恶意用户或程序滥用 API
- **公平使用**：确保所有用户公平使用资源
- **成本控制**：控制 API 调用成本

### 2.2 限流指标

- **请求频率**：单位时间内的请求次数
- **并发数**：同时处理的请求数量
- **带宽限制**：数据传输速率限制
- **资源限制**：CPU、内存等资源限制

## 3. 限流算法

### 3.1 固定窗口

**原理**：在固定时间窗口内限制请求次数

```
时间窗口：1 分钟
限制：100 次请求
[0:00-1:00] 100 次
[1:00-2:00] 100 次
```

**优点**：实现简单
**缺点**：窗口边界可能出现突发流量

### 3.2 滑动窗口

**原理**：在滑动时间窗口内限制请求次数

```
当前时间：1:30
窗口：1 分钟
限制：100 次请求
[0:30-1:30] 100 次
```

**优点**：更平滑的限流
**缺点**：实现复杂

### 3.3 令牌桶

**原理**：以固定速率生成令牌，请求消耗令牌

```
令牌生成速率：10/秒
桶容量：100
请求需要 1 个令牌
```

**优点**：允许突发流量
**缺点**：需要维护令牌状态

### 3.4 漏桶

**原理**：以固定速率处理请求，超出容量则拒绝

```
处理速率：10/秒
桶容量：100
超出容量则拒绝
```

**优点**：平滑输出
**缺点**：不允许突发流量

## 4. 限流策略

### 4.1 基于 IP

```ts
// 基于客户端 IP 限流
const rateLimiter = new Map<string, number[]>();

function checkRateLimit(ip: string, maxRequests: number, windowMs: number): boolean {
  const now = Date.now();
  const requests = rateLimiter.get(ip) || [];
  const recentRequests = requests.filter((time: number) => now - time < windowMs);

  if (recentRequests.length >= maxRequests) {
    return false;
  }

  recentRequests.push(now);
  rateLimiter.set(ip, recentRequests);
  return true;
}
```

### 4.2 基于用户

```ts
// 基于用户 ID 限流
function checkUserRateLimit(userId: string, maxRequests: number, windowMs: number): boolean {
  // 类似 IP 限流，但使用 userId
  return checkRateLimit(userId, maxRequests, windowMs);
}
```

### 4.3 基于 API 端点

```ts
// 不同端点不同限流
const endpointLimits: Record<string, { maxRequests: number; windowMs: number }> = {
  '/api/login': { maxRequests: 5, windowMs: 60000 },
  '/api/users': { maxRequests: 100, windowMs: 60000 }
};
```

## 5. 限流响应

### 5.1 HTTP 状态码

- **429 Too Many Requests**：请求过多
- **503 Service Unavailable**：服务暂时不可用

### 5.2 响应头

```ts
res.setHeader('X-RateLimit-Limit', '100');
res.setHeader('X-RateLimit-Remaining', '95');
res.setHeader('X-RateLimit-Reset', '1609459200');
res.status(429).json({ error: 'Too many requests' });
```

## 6. 适用场景

### 6.1 需要限流的场景

- **公开 API**：防止滥用
- **登录接口**：防止暴力破解
- **资源密集型操作**：保护服务器资源
- **付费 API**：控制成本

### 6.2 不需要限流的场景

- **内部服务**：内部服务通信
- **低频率操作**：更新频率很低的接口
- **静态资源**：CDN 分发的静态资源

## 7. 注意事项

- **用户体验**：限流不应过度影响正常用户
- **错误处理**：提供清晰的错误信息
- **监控**：监控限流效果和影响
- **灵活性**：支持不同场景的限流策略

## 8. 常见问题

### 8.1 如何设置合理的限流值？

根据 API 性能、用户需求和业务场景设置，需要测试和调整。

### 8.2 如何处理限流误杀？

实现白名单机制，对特定用户或 IP 放宽限制。

### 8.3 限流对性能的影响？

限流本身消耗资源，需要选择合适的实现方式和存储方案。

## 9. 相关资源

- [RFC 6585 - 429 Too Many Requests](https://tools.ietf.org/html/rfc6585)
- [限流算法详解](https://en.wikipedia.org/wiki/Rate_limiting)

---

**下一节**：[4.8.2 express-rate-limit](section-02-express-rate-limit.md)
