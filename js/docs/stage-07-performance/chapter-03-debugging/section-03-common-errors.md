# 7.3.3 常见错误与解决方案

## 概述

本节介绍常见的性能问题和错误，以及相应的解决方案和最佳实践。

## 常见性能问题

### 1. 内存泄漏

#### 问题描述

内存泄漏导致内存占用持续增长，最终可能导致页面崩溃。

#### 常见原因

```js
// 1. 全局变量
function leak() {
    name = 'test'; // 意外创建全局变量
}

// 2. 事件监听器未移除
function addListener() {
    button.addEventListener('click', handleClick);
    // 未移除监听器
}

// 3. 定时器未清除
function startTimer() {
    setInterval(() => {
        console.log('tick');
    }, 1000);
    // 未清除定时器
}

// 4. 闭包持有大量数据
function createLeak() {
    const largeData = new Array(1000000).fill(0);
    return function() {
        console.log('closure'); // 闭包持有 largeData
    };
}
```

#### 解决方案

```js
// 1. 使用局部变量
function noLeak() {
    const name = 'test';
}

// 2. 移除事件监听器
function addListenerCorrect() {
    button.addEventListener('click', handleClick);
    // 在适当时机移除
    button.removeEventListener('click', handleClick);
}

// 3. 清除定时器
function startTimerCorrect() {
    const timerId = setInterval(() => {
        console.log('tick');
    }, 1000);
    // 在适当时机清除
    clearInterval(timerId);
}

// 4. 只保留需要的数据
function createNoLeak() {
    const largeData = new Array(1000000).fill(0);
    const neededData = largeData.length;
    return function() {
        console.log(neededData);
    };
}
```

### 2. 频繁重排和重绘

#### 问题描述

频繁的重排和重绘导致页面卡顿。

#### 常见原因

```js
// 1. 频繁修改 DOM
for (let i = 0; i < 1000; i++) {
    element.style.left = i + 'px'; // 每次都会触发重排
}

// 2. 在循环中读取布局属性
for (let i = 0; i < elements.length; i++) {
    const width = elements[i].offsetWidth; // 触发重排
    elements[i].style.width = width + 10 + 'px';
}
```

#### 解决方案

```js
// 1. 批量修改 DOM
element.style.cssText = 'left: 1000px;';

// 2. 使用 transform
element.style.transform = 'translateX(1000px)';

// 3. 读写分离
const widths = elements.map(el => el.offsetWidth);
for (let i = 0; i < elements.length; i++) {
    elements[i].style.width = widths[i] + 10 + 'px';
}
```

### 3. 阻塞渲染

#### 问题描述

JavaScript 执行阻塞页面渲染。

#### 常见原因

```html
<!-- 阻塞渲染的脚本 -->
<script src="library.js"></script>
```

#### 解决方案

```html
<!-- 使用 defer 或 async -->
<script src="library.js" defer></script>
<script src="library.js" async></script>
```

### 4. 大量 DOM 操作

#### 问题描述

大量 DOM 操作导致性能问题。

#### 常见原因

```js
// 直接操作 DOM
for (let i = 0; i < 1000; i++) {
    const div = document.createElement('div');
    document.body.appendChild(div); // 每次都会触发重排
}
```

#### 解决方案

```js
// 使用 DocumentFragment
const fragment = document.createDocumentFragment();
for (let i = 0; i < 1000; i++) {
    const div = document.createElement('div');
    fragment.appendChild(div);
}
document.body.appendChild(fragment); // 只触发一次重排
```

### 5. 未优化的循环

#### 问题描述

低效的循环导致性能问题。

#### 常见原因

```js
// 在循环中使用 includes（O(n²)）
function hasDuplicates(arr) {
    for (let i = 0; i < arr.length; i++) {
        if (arr.includes(arr[i], i + 1)) {
            return true;
        }
    }
    return false;
}
```

#### 解决方案

```js
// 使用 Set（O(n)）
function hasDuplicatesOptimized(arr) {
    const seen = new Set();
    for (let i = 0; i < arr.length; i++) {
        if (seen.has(arr[i])) return true;
        seen.add(arr[i]);
    }
    return false;
}
```

## 性能优化最佳实践

### 1. 代码优化

- 减少循环次数
- 使用合适的数据结构
- 避免不必要的计算
- 使用缓存

### 2. 内存管理

- 及时释放引用
- 避免内存泄漏
- 使用对象池
- 监控内存使用

### 3. 渲染优化

- 减少重排和重绘
- 使用 transform 和 opacity
- 批量修改 DOM
- 使用 CSS 动画

### 4. 网络优化

- 减少 HTTP 请求
- 压缩资源
- 使用缓存
- 代码分割

### 5. 持续监控

- 使用性能分析工具
- 监控核心性能指标
- 定期性能测试
- 持续优化

## 注意事项

1. **平衡性能与可读性**：不要过度优化，保持代码可读性
2. **实际测试**：在真实环境中测试性能
3. **持续改进**：性能优化是一个持续的过程
4. **关注用户体验**：关注用户体验指标
5. **工具辅助**：使用工具识别和解决性能问题

## 常见错误

### 错误 1：过早优化

```js
// 错误：在功能未完成时就优化
// 可能导致代码复杂且难以维护

// 正确：先确保功能正确，再优化性能
```

### 错误 2：忽略用户体验

```js
// 错误：只关注技术指标，忽略用户体验
// 技术指标好不代表用户体验好

// 正确：关注用户体验指标（FCP、LCP、FID、CLS）
```

## 最佳实践

1. **性能测试**：定期进行性能测试
2. **监控指标**：监控核心性能指标
3. **优化验证**：优化后验证效果
4. **持续改进**：持续优化性能
5. **工具辅助**：使用工具识别和解决性能问题

## 练习

1. **内存泄漏检测**：编写代码检测和修复内存泄漏。

2. **性能优化**：优化一个存在性能问题的函数。

3. **渲染优化**：优化一个导致频繁重排的代码。

4. **性能监控**：实现一个性能监控系统。

5. **综合优化**：综合优化一个页面的性能。

完成以上练习后，你已经掌握了性能优化的核心技能。

## 总结

常见的性能问题包括内存泄漏、频繁重排和重绘、阻塞渲染、大量 DOM 操作等。通过识别这些问题并应用相应的解决方案，可以显著提升应用性能。性能优化是一个持续的过程，需要持续监控和改进。

## 相关资源

- [MDN：Web 性能](https://developer.mozilla.org/zh-CN/docs/Web/Performance)
- [Web.dev 性能指南](https://web.dev/performance/)
