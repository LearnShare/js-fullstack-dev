# 7.2.3 代码分割与懒加载

## 概述

代码分割和懒加载是优化 JavaScript 应用性能的重要技术。本节介绍代码分割、懒加载、预加载和预取等方法。

## 代码分割

### 什么是代码分割

代码分割是将代码拆分为多个较小的块，按需加载。

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

### Webpack 代码分割

```js
// 使用 import() 实现代码分割
const loadModule = () => import('./module.js');

// Webpack 会自动创建单独的 chunk
```

### 路由级别的代码分割

```js
// React Router 示例
import { lazy, Suspense } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

const Home = lazy(() => import('./pages/Home'));
const About = lazy(() => import('./pages/About'));

function App() {
    return (
        <BrowserRouter>
            <Suspense fallback={<div>Loading...</div>}>
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/about" element={<About />} />
                </Routes>
            </Suspense>
        </BrowserRouter>
    );
}
```

## 懒加载

### 图片懒加载

```html
<!-- 使用 loading="lazy" -->
<img src="image.jpg" loading="lazy" alt="Image">

<!-- 或使用 Intersection Observer -->
<img data-src="image.jpg" alt="Image">
```

```js
// 使用 Intersection Observer 实现懒加载
const images = document.querySelectorAll('img[data-src]');

const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const img = entry.target;
            img.src = img.dataset.src;
            img.removeAttribute('data-src');
            observer.unobserve(img);
        }
    });
});

images.forEach(img => imageObserver.observe(img));
```

### 组件懒加载

```js
// React 组件懒加载
const LazyComponent = lazy(() => import('./LazyComponent'));

function App() {
    return (
        <Suspense fallback={<div>Loading...</div>}>
            <LazyComponent />
        </Suspense>
    );
}
```

### 数据懒加载

```js
// 无限滚动：懒加载数据
let page = 1;
const loadMore = async () => {
    const data = await fetch(`/api/data?page=${page}`).then(r => r.json());
    appendData(data);
    page++;
};

const observer = new IntersectionObserver(entries => {
    if (entries[0].isIntersecting) {
        loadMore();
    }
});

observer.observe(document.getElementById('load-more'));
```

## 预加载

### 资源预加载

```html
<!-- 预加载关键资源 -->
<link rel="preload" href="critical.css" as="style">
<link rel="preload" href="critical.js" as="script">
<link rel="preload" href="font.woff2" as="font" type="font/woff2" crossorigin>
```

### 模块预加载

```js
// 预加载模块
const link = document.createElement('link');
link.rel = 'modulepreload';
link.href = './module.js';
document.head.appendChild(link);
```

## 预取

### DNS 预取

```html
<!-- DNS 预取 -->
<link rel="dns-prefetch" href="https://api.example.com">
```

### 预连接

```html
<!-- 预连接 -->
<link rel="preconnect" href="https://api.example.com">
```

### 预取资源

```html
<!-- 预取下一页资源 -->
<link rel="prefetch" href="/next-page.html">
```

```js
// 使用 JavaScript 预取
const link = document.createElement('link');
link.rel = 'prefetch';
link.href = '/next-page.html';
document.head.appendChild(link);
```

## 注意事项

1. **按需加载**：只加载当前需要的代码
2. **合理分割**：不要过度分割，保持合理的 chunk 大小
3. **预加载关键资源**：预加载关键资源，提升首屏性能
4. **懒加载非关键资源**：懒加载图片、组件等非关键资源
5. **性能测试**：使用性能分析工具验证优化效果

## 常见错误

### 错误 1：过度分割

```js
// 错误：过度分割，导致请求过多
import('./module1.js');
import('./module2.js');
import('./module3.js');
// ... 太多小 chunk

// 正确：合理分割
import('./features.js'); // 合并相关功能
```

### 错误 2：未处理加载状态

```js
// 错误：未处理加载状态
const module = await import('./module.js');
module.doSomething(); // 用户可能看到空白

// 正确：显示加载状态
setLoading(true);
const module = await import('./module.js');
setLoading(false);
module.doSomething();
```

## 最佳实践

1. **路由分割**：按路由分割代码
2. **组件分割**：大型组件按需加载
3. **资源预加载**：预加载关键资源
4. **懒加载**：懒加载图片和非关键组件
5. **性能测试**：使用工具验证优化效果

## 练习

1. **代码分割**：使用动态导入实现代码分割。

2. **路由懒加载**：实现路由级别的代码分割。

3. **图片懒加载**：使用 Intersection Observer 实现图片懒加载。

4. **预加载策略**：实现一个合理的资源预加载策略。

5. **性能分析**：使用性能分析工具分析代码分割的效果。

完成以上练习后，继续学习下一章，了解调试与性能分析。

## 总结

代码分割和懒加载是优化 JavaScript 应用性能的重要技术。通过代码分割、懒加载、预加载和预取等方法，可以显著提升页面加载速度和运行性能。使用性能分析工具可以帮助识别和优化性能瓶颈。

## 相关资源

- [MDN：代码分割](https://developer.mozilla.org/zh-CN/docs/Web/Performance)
- [Webpack 代码分割](https://webpack.js.org/guides/code-splitting/)
