# 8.7.3 CDN 性能优化

## 1. 概述

CDN 性能优化是提高 CDN 效果的重要手段，通过优化资源、配置、策略等方式，可以进一步提高 CDN 的性能和效果。

## 2. 资源优化

### 2.1 压缩

```ts
import express, { Express } from 'express';
import compression from 'compression';

const app: Express = express();

// 启用 gzip 压缩
app.use(compression({
  level: 6,
  threshold: 1024
}));
```

### 2.2 图片优化

```ts
// 使用 WebP 格式
app.use('/images', (req: Request, res: Response, next): void => {
  const accept = req.headers.accept || '';
  if (accept.includes('image/webp')) {
    req.url = req.url.replace(/\.(jpg|png)$/, '.webp');
  }
  next();
});
```

### 2.3 代码优化

```ts
// 代码压缩和混淆
// 使用构建工具（如 webpack、vite）进行优化
```

## 3. 配置优化

### 3.1 HTTP/2

```ts
// 使用 HTTP/2 提高性能
// 在 CDN 配置中启用 HTTP/2
```

### 3.2 预连接

```html
<!-- 预连接到 CDN -->
<link rel="dns-prefetch" href="https://cdn.example.com">
<link rel="preconnect" href="https://cdn.example.com">
```

### 3.3 预加载

```html
<!-- 预加载关键资源 -->
<link rel="preload" href="/static/main.js" as="script">
<link rel="preload" href="/static/main.css" as="style">
```

## 4. 缓存优化

### 4.1 缓存预热

```ts
async function warmupCDN(urls: string[]): Promise<void> {
  // 预热 CDN 缓存
  for (const url of urls) {
    await fetch(url);
  }
}
```

### 4.2 缓存分层

```ts
// 不同资源使用不同的缓存策略
const cacheStrategies: Record<string, CacheStrategy> = {
  'critical': { ttl: 31536000, immutable: true },
  'normal': { ttl: 2592000 },
  'dynamic': { ttl: 300 }
};
```

## 5. 监控和优化

### 5.1 性能监控

```ts
interface CDNMetrics {
  hitRate: number;
  latency: number;
  bandwidth: number;
}

async function getCDNMetrics(): Promise<CDNMetrics> {
  // 从 CDN API 获取指标
  return {
    hitRate: 0.95,
    latency: 50,
    bandwidth: 1000
  };
}
```

### 5.2 优化建议

```ts
function analyzeCDNPerformance(metrics: CDNMetrics): string[] {
  const suggestions: string[] = [];
  
  if (metrics.hitRate < 0.9) {
    suggestions.push('提高缓存命中率：增加缓存时间、优化缓存策略');
  }
  
  if (metrics.latency > 100) {
    suggestions.push('降低延迟：选择更近的 CDN 节点、优化资源大小');
  }
  
  return suggestions;
}
```

## 6. 最佳实践

### 6.1 性能优化

- 优化资源大小
- 使用压缩
- 启用 HTTP/2
- 使用预加载

### 6.2 缓存优化

- 提高缓存命中率
- 优化缓存策略
- 使用缓存预热
- 监控缓存效果

## 7. 注意事项

- **成本控制**：控制 CDN 成本
- **性能监控**：监控 CDN 性能
- **缓存一致性**：保证缓存一致性
- **持续优化**：持续优化 CDN 配置

## 8. 常见问题

### 8.1 如何提高缓存命中率？

使用长期缓存、优化缓存策略、使用版本控制。

### 8.2 如何降低延迟？

选择更近的 CDN 节点、优化资源大小、使用 HTTP/2。

### 8.3 如何优化带宽使用？

使用压缩、优化资源、提高缓存命中率。

## 9. 实践任务

1. **资源优化**：优化静态资源
2. **配置优化**：优化 CDN 配置
3. **缓存优化**：优化缓存策略
4. **性能监控**：监控 CDN 性能
5. **持续优化**：持续优化 CDN 性能

---

**阶段八完成**：恭喜完成阶段八的学习！可以继续学习阶段九：部署与 DevOps。
