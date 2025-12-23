# 4.5.4 CDN 与边缘计算

## 1. 概述

CDN（Content Delivery Network）和边缘计算是 JAMstack 架构的重要组成部分，通过全球分布的边缘节点提供快速、可靠的内容分发和计算服务。CDN 和边缘计算提升了 Web 应用的性能和用户体验。

## 2. CDN 概述

### 2.1 CDN 的作用

- **内容分发**：将静态内容分发到全球边缘节点
- **缓存加速**：缓存静态内容，减少源站负载
- **降低延迟**：从最近的边缘节点提供服务
- **提高可用性**：多个节点提供冗余

### 2.2 CDN 工作原理

```
用户请求 → DNS 解析 → 最近的边缘节点 → 缓存检查 → 返回内容
```

## 3. 主流 CDN 服务

### 3.1 Cloudflare

**特点**：
- 全球边缘网络
- DDoS 防护
- SSL/TLS 加密
- 边缘计算支持

**基本配置**：

```ts
// 使用 Cloudflare Workers
export default {
  async fetch(request: Request): Promise<Response> {
    const url = new URL(request.url);
    
    // 边缘缓存
    const cacheKey = new Request(url.toString(), request);
    const cache = caches.default;
    
    let response = await cache.match(cacheKey);
    if (!response) {
      response = await fetch(request);
      response = new Response(response.body, response);
      response.headers.set('Cache-Control', 'public, max-age=3600');
      await cache.put(cacheKey, response.clone());
    }
    
    return response;
  }
};
```

### 3.2 Vercel Edge Network

**特点**：
- 全球边缘网络
- 自动 CDN
- 边缘函数支持
- Next.js 优化

**基本使用**：

```ts
// middleware.ts
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest): NextResponse {
  const response = NextResponse.next();
  
  // 设置缓存头
  response.headers.set('Cache-Control', 'public, s-maxage=3600, stale-while-revalidate=86400');
  
  return response;
}
```

### 3.3 AWS CloudFront

**特点**：
- 全球边缘网络
- Lambda@Edge 支持
- 自定义域名
- 价格灵活

**基本配置**：

```json
{
  "CacheBehaviors": {
    "Default": {
      "TargetOriginId": "S3-Origin",
      "ViewerProtocolPolicy": "redirect-to-https",
      "CachePolicyId": "4135ea2d-6df8-44a3-9df3-4b5a84be39ad"
    }
  }
}
```

## 4. 边缘计算

### 4.1 边缘计算概念

边缘计算将计算能力部署到 CDN 边缘节点，在靠近用户的位置执行代码，减少延迟，提升性能。

### 4.2 边缘函数

**Cloudflare Workers**：

```ts
// 边缘函数示例
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    
    // 边缘计算逻辑
    if (url.pathname === '/api/geo') {
      const country = request.cf?.country || 'Unknown';
      return new Response(JSON.stringify({ country }), {
        headers: { 'Content-Type': 'application/json' }
      });
    }
    
    return fetch(request);
  }
};
```

**Vercel Edge Functions**：

```ts
// app/api/hello/route.ts
export const config = {
  runtime: 'edge'
};

export default async function handler(request: Request): Promise<Response> {
  const { searchParams } = new URL(request.url);
  const name = searchParams.get('name') || 'World';
  
  return new Response(JSON.stringify({ message: `Hello ${name}` }), {
    headers: { 'Content-Type': 'application/json' }
  });
}
```

## 5. 缓存策略

### 5.1 静态资源缓存

```ts
// 设置缓存头
const headers = new Headers();
headers.set('Cache-Control', 'public, max-age=31536000, immutable');
headers.set('ETag', '"abc123"');
headers.set('Last-Modified', 'Wed, 21 Oct 2023 07:28:00 GMT');
```

### 5.2 动态内容缓存

```ts
// 使用边缘缓存
const cacheKey = new Request(url.toString(), request);
const cache = caches.default;

let response = await cache.match(cacheKey);
if (!response) {
  response = await fetch(request);
  response.headers.set('Cache-Control', 'public, s-maxage=60, stale-while-revalidate=300');
  await cache.put(cacheKey, response.clone());
}
```

### 5.3 缓存失效

```ts
// 清除缓存
async function purgeCache(url: string): Promise<void> {
  await fetch(`https://api.cloudflare.com/client/v4/zones/${ZONE_ID}/purge_cache`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${API_TOKEN}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ files: [url] })
  });
}
```

## 6. 性能优化

### 6.1 图片优化

```ts
// 使用 Cloudflare Images
const imageUrl = `https://imagedelivery.net/${ACCOUNT_HASH}/${IMAGE_ID}/public`;
```

### 6.2 压缩优化

```ts
// 启用 Brotli 压缩
const response = await fetch(request);
const compressed = await compressResponse(response, 'br');
return compressed;
```

### 6.3 预加载

```html
<link rel="preconnect" href="https://cdn.example.com">
<link rel="dns-prefetch" href="https://cdn.example.com">
<link rel="preload" href="/fonts/example.woff2" as="font" type="font/woff2" crossorigin>
```

## 7. 安全实践

### 7.1 HTTPS

```ts
// 强制 HTTPS
if (request.url.startsWith('http://')) {
  return Response.redirect(request.url.replace('http://', 'https://'), 301);
}
```

### 7.2 安全头

```ts
const headers = new Headers();
headers.set('X-Content-Type-Options', 'nosniff');
headers.set('X-Frame-Options', 'DENY');
headers.set('X-XSS-Protection', '1; mode=block');
headers.set('Strict-Transport-Security', 'max-age=31536000; includeSubDomains');
```

### 7.3 DDoS 防护

```ts
// 使用 Cloudflare 自动 DDoS 防护
// 或实现速率限制
const rateLimiter = new Map<string, number[]>();

function checkRateLimit(ip: string): boolean {
  const now = Date.now();
  const requests = rateLimiter.get(ip) || [];
  const recentRequests = requests.filter((time: number) => now - time < 60000);
  
  if (recentRequests.length >= 100) {
    return false; // 超过限制
  }
  
  recentRequests.push(now);
  rateLimiter.set(ip, recentRequests);
  return true;
}
```

## 8. 最佳实践

### 8.1 CDN 配置

- 使用合适的缓存策略
- 配置压缩
- 启用 HTTPS
- 设置安全头

### 8.2 边缘计算

- 将计算逻辑移到边缘
- 减少到源站的请求
- 优化边缘函数性能

### 8.3 监控和优化

- 监控 CDN 性能
- 分析缓存命中率
- 优化缓存策略

## 9. 注意事项

- **缓存失效**：实现合理的缓存失效策略
- **成本控制**：注意 CDN 和边缘计算成本
- **安全配置**：正确配置安全设置
- **性能监控**：监控 CDN 性能指标

## 10. 常见问题

### 10.1 CDN 和边缘计算的区别？

CDN 主要用于内容分发，边缘计算在边缘节点执行代码。

### 10.2 如何选择 CDN 服务？

根据需求、预算和地理位置选择。全球服务用 Cloudflare，Next.js 项目用 Vercel。

### 10.3 如何处理缓存失效？

使用 Webhook 或 API 清除缓存，或使用版本化 URL。

## 11. 实践任务

1. **配置 CDN**：在 Cloudflare 或 Vercel 配置 CDN
2. **实现边缘函数**：实现边缘计算逻辑
3. **优化缓存策略**：配置合适的缓存策略
4. **实现安全配置**：配置 HTTPS 和安全头
5. **性能监控**：监控 CDN 性能指标

---

**下一章**：[4.6 WebSocket 服务器](../chapter-06-websocket/readme.md)
