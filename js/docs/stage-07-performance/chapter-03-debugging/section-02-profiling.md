# 7.3.2 性能分析工具

## 概述

性能分析工具可以帮助识别和解决性能问题。本节介绍各种性能分析工具、性能指标和优化建议。

## 性能指标

### 1. 首屏时间（First Contentful Paint, FCP）

首次内容绘制的时间。

```js
// 使用 Performance API 测量 FCP
const observer = new PerformanceObserver((list) => {
    for (const entry of list.getEntries()) {
        if (entry.name === 'first-contentful-paint') {
            console.log('FCP:', entry.startTime);
        }
    }
});
observer.observe({ entryTypes: ['paint'] });
```

### 2. 最大内容绘制（Largest Contentful Paint, LCP）

最大内容元素渲染的时间。

```js
// 使用 Performance API 测量 LCP
const observer = new PerformanceObserver((list) => {
    const entries = list.getEntries();
    const lastEntry = entries[entries.length - 1];
    console.log('LCP:', lastEntry.renderTime);
});
observer.observe({ entryTypes: ['largest-contentful-paint'] });
```

### 3. 首次输入延迟（First Input Delay, FID）

用户首次交互到浏览器响应的延迟。

```js
// 使用 Performance API 测量 FID
const observer = new PerformanceObserver((list) => {
    for (const entry of list.getEntries()) {
        console.log('FID:', entry.processingStart - entry.startTime);
    }
});
observer.observe({ entryTypes: ['first-input'] });
```

### 4. 累积布局偏移（Cumulative Layout Shift, CLS）

页面布局的稳定性。

```js
// 使用 Performance API 测量 CLS
let clsValue = 0;
const observer = new PerformanceObserver((list) => {
    for (const entry of list.getEntries()) {
        if (!entry.hadRecentInput) {
            clsValue += entry.value;
        }
    }
    console.log('CLS:', clsValue);
});
observer.observe({ entryTypes: ['layout-shift'] });
```

## Performance API

### 基本使用

```js
// 测量代码执行时间
performance.mark('start');
// 执行代码
performance.mark('end');
performance.measure('duration', 'start', 'end');
const measure = performance.getEntriesByName('duration')[0];
console.log('Duration:', measure.duration);
```

### 资源计时

```js
// 获取资源加载时间
const resources = performance.getEntriesByType('resource');
resources.forEach(resource => {
    console.log(resource.name, resource.duration);
});
```

### 导航计时

```js
// 获取页面加载时间
const navigation = performance.getEntriesByType('navigation')[0];
console.log('DOMContentLoaded:', navigation.domContentLoadedEventEnd - navigation.domContentLoadedEventStart);
console.log('Load:', navigation.loadEventEnd - navigation.loadEventStart);
```

## Chrome DevTools Performance 面板

### 录制性能

1. 打开 Performance 面板
2. 点击录制按钮
3. 执行操作
4. 停止录制
5. 查看性能报告

### 分析性能

- **FPS**：帧率，目标 60 FPS
- **CPU**：CPU 使用率
- **内存**：内存使用情况
- **网络**：网络请求

### 性能优化建议

根据性能报告，找出性能瓶颈并优化。

## Lighthouse

### 基本使用

1. 打开 Chrome DevTools
2. 切换到 Lighthouse 面板
3. 选择类别（Performance、Accessibility 等）
4. 点击"Generate report"
5. 查看报告

### 性能评分

- **Performance**：性能分数（0-100）
- **Accessibility**：可访问性分数
- **Best Practices**：最佳实践分数
- **SEO**：SEO 分数

### 优化建议

Lighthouse 会提供具体的优化建议。

## WebPageTest

### 基本使用

1. 访问 WebPageTest.org
2. 输入 URL
3. 选择测试配置
4. 运行测试
5. 查看报告

### 性能指标

- **First Byte Time**：首字节时间
- **Start Render**：开始渲染时间
- **Speed Index**：速度指数
- **Total Load Time**：总加载时间

## 注意事项

1. **真实环境测试**：在真实环境中测试性能
2. **多次测试**：进行多次测试，取平均值
3. **关注指标**：关注核心性能指标
4. **持续监控**：持续监控性能指标
5. **优化验证**：优化后验证效果

## 常见错误

### 错误 1：只在开发环境测试

```js
// 错误：只在开发环境测试性能
// 开发环境和生产环境性能差异很大

// 正确：在生产环境或类似环境中测试
```

### 错误 2：忽略用户体验指标

```js
// 错误：只关注技术指标，忽略用户体验
// 技术指标好不代表用户体验好

// 正确：关注用户体验指标（FCP、LCP、FID、CLS）
```

## 最佳实践

1. **真实环境测试**：在真实环境中测试性能
2. **关注核心指标**：关注 FCP、LCP、FID、CLS 等核心指标
3. **持续监控**：持续监控性能指标
4. **优化验证**：优化后验证效果
5. **工具结合**：结合多种工具进行分析

## 练习

1. **性能指标测量**：使用 Performance API 测量各种性能指标。

2. **Lighthouse 分析**：使用 Lighthouse 分析页面性能。

3. **性能优化**：根据分析结果优化页面性能。

4. **持续监控**：实现一个性能监控系统。

5. **综合分析**：综合使用多种工具分析性能。

完成以上练习后，继续学习下一节，了解常见错误与解决方案。

## 总结

性能分析工具可以帮助识别和解决性能问题。通过使用 Performance API、Chrome DevTools、Lighthouse 等工具，可以全面分析页面性能。关注核心性能指标，持续监控和优化，可以显著提升用户体验。

## 相关资源

- [Web Vitals](https://web.dev/vitals/)
- [Lighthouse](https://developers.google.com/web/tools/lighthouse)
- [WebPageTest](https://www.webpagetest.org/)
