# 8.7.2 CDN 缓存策略

## 1. 概述

CDN 缓存策略决定了内容在 CDN 中的缓存方式和时间，合理的缓存策略可以显著提高性能、减少回源、降低成本。

## 2. 缓存策略类型

### 2.1 强缓存

**特点**：客户端直接使用缓存，不请求服务器。

**HTTP 头**：
```ts
res.setHeader('Cache-Control', 'public, max-age=31536000, immutable');
res.setHeader('Expires', new Date(Date.now() + 31536000000).toUTCString());
```

**适用**：静态资源（CSS、JS、图片）

### 2.2 协商缓存

**特点**：客户端请求服务器验证缓存是否有效。

**HTTP 头**：
```ts
res.setHeader('ETag', etag);
res.setHeader('Last-Modified', lastModified);

// 检查
if (req.headers['if-none-match'] === etag) {
  res.status(304).end();
  return;
}
```

**适用**：动态内容、需要验证的内容

## 3. 不同资源的缓存策略

### 3.1 HTML

```ts
// HTML 不缓存或短时间缓存
res.setHeader('Cache-Control', 'no-cache, must-revalidate');
```

### 3.2 CSS/JS

```ts
// 长期缓存，使用版本号
res.setHeader('Cache-Control', 'public, max-age=31536000, immutable');
```

### 3.3 图片

```ts
// 中等时间缓存
res.setHeader('Cache-Control', 'public, max-age=2592000');
```

### 3.4 API

```ts
// 根据数据特性决定
res.setHeader('Cache-Control', 'private, max-age=300');
```

## 4. 版本控制

### 4.1 查询参数

```ts
function getAssetUrl(filename: string): string {
  const version = process.env.ASSET_VERSION || Date.now();
  return `/static/${filename}?v=${version}`;
}
```

### 4.2 文件名哈希

```ts
import { createHash } from 'node:crypto';

function getAssetHash(content: string): string {
  return createHash('md5').update(content).digest('hex').substring(0, 8);
}

function getAssetUrl(filename: string, hash: string): string {
  const [name, ext] = filename.split('.');
  return `/static/${name}.${hash}.${ext}`;
}
```

## 5. 缓存失效

### 5.1 主动刷新

```ts
async function purgeCDNCache(urls: string[]): Promise<void> {
  // 调用 CDN API 刷新缓存
  await cdnApi.purge(urls);
}
```

### 5.2 版本更新

```ts
// 更新版本号触发缓存失效
process.env.ASSET_VERSION = Date.now().toString();
```

## 6. 最佳实践

### 6.1 策略设计

- HTML：不缓存或短时间缓存
- CSS/JS：长期缓存，使用版本号
- 图片：中等时间缓存
- API：根据数据特性决定

### 6.2 版本管理

- 使用版本号或哈希
- 更新时自动失效
- 支持多版本共存

## 7. 注意事项

- **缓存一致性**：保证缓存一致性
- **版本控制**：使用版本控制
- **主动刷新**：支持主动刷新
- **成本控制**：控制缓存成本

## 8. 常见问题

### 8.1 如何处理缓存更新？

使用版本号、哈希、主动刷新。

### 8.2 如何选择缓存时间？

根据内容特性、更新频率、业务需求选择。

### 8.3 如何优化缓存命中率？

使用长期缓存、合理版本控制、优化缓存策略。

## 9. 实践任务

1. **设计策略**：设计 CDN 缓存策略
2. **实现版本控制**：实现版本控制
3. **配置缓存**：配置 CDN 缓存
4. **性能测试**：测试缓存效果
5. **持续优化**：持续优化缓存策略

---

**下一节**：[8.7.3 CDN 性能优化](section-03-optimization.md)
