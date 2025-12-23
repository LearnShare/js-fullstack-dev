# 8.4.4 CDN 与静态资源缓存

## 1. 概述

CDN（Content Delivery Network）是分布式网络，通过将内容缓存到边缘节点，可以显著减少延迟、提高访问速度。静态资源缓存是 CDN 的主要应用场景。

## 2. CDN 工作原理

### 2.1 基本流程

```
1. 用户请求资源
2. DNS 解析到最近的 CDN 节点
3. CDN 节点检查缓存
4. 缓存命中，直接返回
5. 缓存未命中，回源获取并缓存
```

### 2.2 优势

- **减少延迟**：就近访问
- **降低带宽**：减少源站压力
- **提高可用性**：多节点冗余
- **全球加速**：全球节点分布

## 3. 静态资源缓存

### 3.1 HTTP 缓存头

```ts
import express, { Express, Request, Response } from 'express';

const app: Express = express();

// 设置缓存头
app.use('/static', (req: Request, res: Response, next): void => {
  // 强缓存：1 年
  res.setHeader('Cache-Control', 'public, max-age=31536000, immutable');
  res.setHeader('Expires', new Date(Date.now() + 31536000000).toUTCString());
  next();
});

// 协商缓存
app.use('/api', (req: Request, res: Response, next): void => {
  const etag = generateETag(req.url);
  res.setHeader('ETag', etag);
  
  if (req.headers['if-none-match'] === etag) {
    res.status(304).end();
    return;
  }
  
  next();
});
```

### 3.2 文件版本控制

```ts
// 使用版本号
app.use('/static', express.static('public', {
  maxAge: '1y',
  etag: true,
  lastModified: true
}));

// 使用哈希
function getAssetPath(filename: string): string {
  const hash = generateHash(filename);
  return `/static/${filename}?v=${hash}`;
}
```

## 4. CDN 配置

### 4.1 缓存策略

```ts
// 不同资源类型的缓存策略
const cacheStrategies: Record<string, string> = {
  'html': 'no-cache',           // HTML 不缓存
  'css': 'public, max-age=31536000',  // CSS 长期缓存
  'js': 'public, max-age=31536000',   // JS 长期缓存
  'images': 'public, max-age=2592000', // 图片缓存 30 天
  'fonts': 'public, max-age=31536000'  // 字体长期缓存
};

app.use('/assets', (req: Request, res: Response, next): void => {
  const ext = req.path.split('.').pop() || '';
  const strategy = cacheStrategies[ext] || 'no-cache';
  res.setHeader('Cache-Control', strategy);
  next();
});
```

### 4.2 CDN 回源配置

```ts
// 配置回源规则
interface CDNConfig {
  origin: string;
  cacheRules: Array<{
    path: string;
    ttl: number;
  }>;
}

const cdnConfig: CDNConfig = {
  origin: 'https://example.com',
  cacheRules: [
    { path: '/static/*', ttl: 31536000 },
    { path: '/api/*', ttl: 0 },
    { path: '/images/*', ttl: 2592000 }
  ]
};
```

## 5. 最佳实践

### 5.1 缓存策略

- HTML：不缓存或短时间缓存
- CSS/JS：长期缓存，使用版本号
- 图片：中等时间缓存
- API：根据数据特性决定

### 5.2 CDN 使用

- 使用 CDN 加速静态资源
- 配置合理的缓存时间
- 使用版本控制避免缓存问题
- 监控 CDN 性能

## 6. 注意事项

- **缓存失效**：使用版本控制
- **HTTPS**：使用 HTTPS
- **CORS**：配置 CORS
- **性能监控**：监控 CDN 性能

## 7. 常见问题

### 7.1 如何选择 CDN？

根据地理位置、价格、性能、功能选择。

### 7.2 如何处理缓存更新？

使用版本号、哈希、主动刷新。

### 7.3 如何优化 CDN 性能？

选择合适的缓存策略、优化资源大小、使用压缩。

## 8. 实践任务

1. **CDN 配置**：配置 CDN
2. **缓存策略**：设置缓存策略
3. **版本控制**：实现版本控制
4. **性能测试**：测试 CDN 性能
5. **持续优化**：持续优化 CDN 配置

---

**下一章**：[8.5 可观测性](../chapter-05-observability/readme.md)
