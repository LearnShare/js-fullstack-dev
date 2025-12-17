# 6.4.4 CDN 与边缘计算

## 概述

CDN（内容分发网络）和边缘计算是 JAMstack 架构中提升性能和用户体验的关键技术。本节介绍 CDN 和边缘计算在 JAMstack 中的应用。

## CDN（内容分发网络）

### CDN 的概念

CDN 是一个分布式的服务器网络，将内容缓存到全球各地的边缘节点，用户可以从最近的节点获取内容。

### CDN 的工作原理

```
用户请求 → 最近的边缘节点 → 返回缓存内容
         ↓（如果未缓存）
         源服务器 → 边缘节点 → 用户
```

### CDN 的优势

1. **降低延迟**：用户从最近的节点获取内容
2. **提升性能**：减少源服务器负载
3. **高可用性**：多个节点提供冗余
4. **全球分发**：内容可以分发到全球

### 在 JAMstack 中的应用

```js
// 静态文件通过 CDN 分发
// HTML、CSS、JavaScript、图片等静态资源
// 都部署到 CDN
```

## 常用 CDN 服务

### Netlify

Netlify 是一个集成了 CDN 的部署平台。

```bash
# 部署到 Netlify
netlify deploy --prod
```

**特点**：
- 自动 CDN 分发
- 自动 HTTPS
- 边缘函数支持

### Vercel

Vercel 是一个专注于前端部署的平台。

```bash
# 部署到 Vercel
vercel --prod
```

**特点**：
- 全球 CDN 网络
- 边缘函数
- 自动优化

### Cloudflare Pages

Cloudflare Pages 是 Cloudflare 的静态站点托管服务。

**特点**：
- Cloudflare 全球网络
- 边缘计算支持
- DDoS 防护

### AWS CloudFront

AWS CloudFront 是 AWS 的 CDN 服务。

**特点**：
- 全球覆盖
- 与 AWS 服务集成
- 可定制配置

## 边缘计算

### 边缘计算的概念

边缘计算是将计算能力推到网络的边缘，在接近用户的位置执行代码。

### 边缘函数（Edge Functions）

边缘函数是在 CDN 边缘节点执行的函数，可以处理请求和响应。

#### Netlify Functions

```js
// netlify/functions/hello.js
exports.handler = async (event, context) => {
    return {
        statusCode: 200,
        body: JSON.stringify({ message: 'Hello from edge!' })
    };
};
```

#### Vercel Edge Functions

```js
// middleware.js
export default function middleware(request) {
    return new Response('Hello from edge!');
}

export const config = {
    runtime: 'edge'
};
```

#### Cloudflare Workers

```js
// worker.js
addEventListener('fetch', event => {
    event.respondWith(handleRequest(event.request));
});

async function handleRequest(request) {
    return new Response('Hello from edge!');
}
```

### 边缘计算的优势

1. **低延迟**：在边缘执行，延迟低
2. **全球分布**：代码在全球边缘节点执行
3. **减轻服务器负载**：减少源服务器负载
4. **实时处理**：可以实时处理请求

## CDN 缓存策略

### 缓存控制

```js
// 设置缓存头
res.setHeader('Cache-Control', 'public, max-age=3600');

// 静态资源长期缓存
res.setHeader('Cache-Control', 'public, max-age=31536000, immutable');
```

### 缓存失效

1. **版本控制**：使用文件版本号
2. **Hash 文件名**：使用内容 hash 作为文件名
3. **Purge API**：使用 API 清除缓存

## 性能优化

### 1. 静态资源优化

```js
// 压缩资源
// 使用 Gzip/Brotli 压缩

// 图片优化
// 使用现代图片格式（WebP、AVIF）
// 响应式图片
```

### 2. HTTP/2 和 HTTP/3

- HTTP/2：多路复用、服务器推送
- HTTP/3：基于 QUIC，性能更好

### 3. 预加载和预取

```html
<!-- 预加载关键资源 -->
<link rel="preload" href="/critical.css" as="style">

<!-- DNS 预取 -->
<link rel="dns-prefetch" href="https://api.example.com">

<!-- 预连接 -->
<link rel="preconnect" href="https://api.example.com">
```

## 注意事项

1. **缓存策略**：合理设置缓存策略
2. **缓存失效**：实现合理的缓存失效机制
3. **成本控制**：注意 CDN 和边缘计算的成本
4. **安全性**：注意边缘函数的安全性

## 最佳实践

1. **CDN 配置**：合理配置 CDN 缓存
2. **边缘函数**：将简单逻辑放到边缘执行
3. **性能监控**：监控 CDN 和边缘计算的性能
4. **成本优化**：优化 CDN 和边缘计算的使用成本

## 练习

1. **CDN 部署**：将静态站点部署到 CDN（Netlify、Vercel 等）。

2. **边缘函数**：创建边缘函数，处理请求和响应。

3. **缓存策略**：配置合理的缓存策略，实现缓存优化。

4. **性能测试**：测试 CDN 和边缘计算的性能提升。

5. **成本分析**：分析 CDN 和边缘计算的使用成本。

完成以上练习后，你已经了解了 JAMstack 架构的完整实现。

## 总结

CDN 和边缘计算是 JAMstack 架构中提升性能的关键技术。CDN 通过全球分发降低延迟，边缘计算在边缘节点执行代码。Netlify、Vercel、Cloudflare 等平台提供了集成的 CDN 和边缘计算能力。合理使用 CDN 和边缘计算可以显著提升 JAMstack 应用的性能和用户体验。

## 相关资源

- [Netlify 官网](https://www.netlify.com/)
- [Vercel 官网](https://vercel.com/)
- [Cloudflare Pages](https://pages.cloudflare.com/)
- [边缘计算指南](https://www.cloudflare.com/learning/serverless/glossary/what-is-edge-computing/)
