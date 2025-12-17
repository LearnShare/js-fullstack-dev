# 7.2.2 网络性能优化

## 概述

网络性能优化是前端开发中的重要技能。本节介绍资源加载优化、缓存策略、HTTP/2、CDN 等网络性能优化方法。

## 资源加载优化

### 1. 减少 HTTP 请求

```js
// 合并文件
// 将多个 CSS 文件合并为一个
// 将多个 JS 文件合并为一个

// 使用图片精灵（Sprite）
// 将多个小图片合并为一个大图片
```

### 2. 压缩资源

```js
// 压缩 JavaScript
// 使用 UglifyJS、Terser 等工具压缩

// 压缩 CSS
// 使用 CSSNano 等工具压缩

// 压缩图片
// 使用 WebP、AVIF 等现代图片格式
```

### 3. 使用 CDN

```js
// 使用 CDN 加速资源加载
// <script src="https://cdn.example.com/library.js"></script>
```

### 4. 预加载关键资源

```html
<!-- 预加载关键资源 -->
<link rel="preload" href="critical.css" as="style">
<link rel="preload" href="critical.js" as="script">
```

### 5. 延迟加载非关键资源

```html
<!-- 延迟加载图片 -->
<img src="image.jpg" loading="lazy">

<!-- 延迟加载脚本 -->
<script src="non-critical.js" defer></script>
```

## 缓存策略

### 浏览器缓存

#### 1. 强缓存

```http
Cache-Control: max-age=3600
Expires: Wed, 21 Oct 2025 07:28:00 GMT
```

#### 2. 协商缓存

```http
ETag: "33a64df551425fcc55e4d42a148795d9f25f89d4"
Last-Modified: Wed, 21 Oct 2025 07:28:00 GMT
```

### Service Worker 缓存

```js
// 使用 Service Worker 实现离线缓存
self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request).then(response => {
            return response || fetch(event.request);
        })
    );
});
```

## HTTP/2

### HTTP/2 的优势

1. **多路复用**：一个连接可以处理多个请求
2. **服务器推送**：服务器可以主动推送资源
3. **头部压缩**：减少头部大小

### 使用 HTTP/2

```js
// 使用 HTTP/2 时，可以并行加载多个小文件
// 不需要合并文件
```

## 代码分割

### 动态导入

```js
// 使用动态导入实现代码分割
import('./module.js').then(module => {
    module.doSomething();
});

// 或使用 async/await
const module = await import('./module.js');
module.doSomething();
```

### 路由级别的代码分割

```js
// React Router 示例
const Home = lazy(() => import('./pages/Home'));
const About = lazy(() => import('./pages/About'));
```

## 图片优化

### 1. 使用现代图片格式

```html
<!-- 使用 WebP -->
<picture>
    <source srcset="image.webp" type="image/webp">
    <img src="image.jpg" alt="Image">
</picture>
```

### 2. 响应式图片

```html
<!-- 使用 srcset -->
<img srcset="small.jpg 480w, medium.jpg 768w, large.jpg 1200w"
     sizes="(max-width: 480px) 100vw, (max-width: 768px) 50vw, 33vw"
     src="medium.jpg" alt="Image">
```

### 3. 懒加载

```html
<!-- 使用 loading="lazy" -->
<img src="image.jpg" loading="lazy" alt="Image">
```

## 字体优化

### 1. 字体子集化

```css
/* 只加载需要的字符 */
@font-face {
    font-family: 'CustomFont';
    src: url('font-subset.woff2') format('woff2');
    unicode-range: U+0020-007F; /* 只包含 ASCII */
}
```

### 2. 字体预加载

```html
<link rel="preload" href="font.woff2" as="font" type="font/woff2" crossorigin>
```

### 3. font-display

```css
@font-face {
    font-family: 'CustomFont';
    src: url('font.woff2') format('woff2');
    font-display: swap; /* 显示回退字体，然后替换 */
}
```

## 注意事项

1. **减少请求**：合并文件，使用图片精灵
2. **压缩资源**：压缩 JavaScript、CSS、图片
3. **使用缓存**：合理设置缓存策略
4. **代码分割**：按需加载代码
5. **图片优化**：使用现代格式，懒加载

## 常见错误

### 错误 1：阻塞渲染的资源

```html
<!-- 错误：阻塞渲染的脚本 -->
<script src="library.js"></script>

<!-- 正确：使用 defer 或 async -->
<script src="library.js" defer></script>
```

### 错误 2：未压缩的资源

```js
// 错误：未压缩的 JavaScript
// 文件大小：100KB

// 正确：压缩后的 JavaScript
// 文件大小：30KB（压缩率 70%）
```

## 最佳实践

1. **减少请求**：合并文件，使用图片精灵
2. **压缩资源**：压缩所有资源
3. **使用缓存**：合理设置缓存策略
4. **代码分割**：按需加载代码
5. **图片优化**：使用现代格式，懒加载

## 练习

1. **资源合并**：合并多个 CSS 和 JavaScript 文件。

2. **代码分割**：使用动态导入实现代码分割。

3. **缓存策略**：实现一个合理的缓存策略。

4. **图片优化**：优化图片加载，使用懒加载和现代格式。

5. **性能测试**：使用网络分析工具测试网络性能。

完成以上练习后，继续学习下一节，了解代码分割与懒加载。

## 总结

网络性能优化包括减少 HTTP 请求、压缩资源、使用缓存、代码分割、图片优化等方法。通过合理使用这些优化方法，可以显著提升页面加载速度。使用网络分析工具可以帮助识别和解决性能问题。

## 相关资源

- [MDN：Web 性能](https://developer.mozilla.org/zh-CN/docs/Web/Performance)
- [Chrome DevTools Network 面板](https://developer.chrome.com/docs/devtools/network/)
