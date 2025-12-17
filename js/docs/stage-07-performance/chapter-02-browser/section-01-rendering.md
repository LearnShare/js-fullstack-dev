# 7.2.1 渲染性能优化

## 概述

浏览器渲染性能优化是前端开发中的重要技能。本节介绍重排（Reflow）、重绘（Repaint）、合成层（Compositing Layer）和动画优化等渲染性能优化方法。

## 浏览器渲染流程

### 渲染步骤

1. **解析 HTML**：构建 DOM 树
2. **解析 CSS**：构建 CSSOM 树
3. **合并**：构建渲染树（Render Tree）
4. **布局（Layout）**：计算元素位置和大小（重排）
5. **绘制（Paint）**：绘制元素（重绘）
6. **合成（Composite）**：合成图层

### 性能影响

- **重排**：最耗时，需要重新计算布局
- **重绘**：较耗时，需要重新绘制
- **合成**：最快，只合成图层

## 重排（Reflow）优化

### 什么是重排

重排是浏览器重新计算元素的位置和大小。

### 触发重排的操作

```js
// 以下操作会触发重排
element.style.width = '100px';
element.style.height = '100px';
element.style.display = 'none';
element.offsetWidth; // 读取布局属性也会触发重排
```

### 优化方法

#### 1. 批量修改 DOM

```js
// 错误：多次修改触发多次重排
const div = document.getElementById('myDiv');
div.style.width = '100px';
div.style.height = '100px';
div.style.margin = '10px';

// 正确：使用 class 或 cssText
div.className = 'new-style';
// 或
div.style.cssText = 'width: 100px; height: 100px; margin: 10px;';
```

#### 2. 使用 DocumentFragment

```js
// 错误：直接操作 DOM
const list = document.getElementById('list');
for (let i = 0; i < 1000; i++) {
    const item = document.createElement('li');
    item.textContent = `Item ${i}`;
    list.appendChild(item); // 每次都会触发重排
}

// 正确：使用 DocumentFragment
const fragment = document.createDocumentFragment();
for (let i = 0; i < 1000; i++) {
    const item = document.createElement('li');
    item.textContent = `Item ${i}`;
    fragment.appendChild(item);
}
list.appendChild(fragment); // 只触发一次重排
```

#### 3. 读写分离

```js
// 错误：读写混合
for (let i = 0; i < elements.length; i++) {
    elements[i].style.width = elements[i].offsetWidth + 10 + 'px';
}

// 正确：先读后写
let widths = [];
for (let i = 0; i < elements.length; i++) {
    widths[i] = elements[i].offsetWidth;
}
for (let i = 0; i < elements.length; i++) {
    elements[i].style.width = widths[i] + 10 + 'px';
}
```

#### 4. 使用 transform 代替位置属性

```js
// 错误：使用 left/top 触发重排
element.style.left = '100px';
element.style.top = '100px';

// 正确：使用 transform 只触发合成
element.style.transform = 'translate(100px, 100px)';
```

## 重绘（Repaint）优化

### 什么是重绘

重绘是浏览器重新绘制元素，但不改变布局。

### 触发重绘的操作

```js
// 以下操作会触发重绘
element.style.color = 'red';
element.style.backgroundColor = 'blue';
element.style.outline = '1px solid black';
```

### 优化方法

#### 1. 使用 will-change

```js
// 提示浏览器该元素会变化，提前优化
.element {
    will-change: transform;
}
```

#### 2. 使用 transform 和 opacity

```js
// transform 和 opacity 只触发合成，不触发重排和重绘
.element {
    transform: translateX(100px);
    opacity: 0.5;
}
```

## 合成层优化

### 什么是合成层

合成层是浏览器将元素提升到独立的图层，可以独立合成。

### 创建合成层

以下情况会创建合成层：

1. 3D transform
2. will-change
3. video、canvas、iframe
4. opacity 动画
5. position: fixed

### 优化建议

```js
// 使用 transform 和 opacity 进行动画
.element {
    will-change: transform;
    transform: translateZ(0); // 强制创建合成层
}
```

## 动画优化

### 使用 requestAnimationFrame

```js
// 错误：使用 setTimeout
function animate() {
    element.style.left = (parseInt(element.style.left) + 1) + 'px';
    setTimeout(animate, 16);
}

// 正确：使用 requestAnimationFrame
function animate() {
    element.style.transform = `translateX(${x}px)`;
    x++;
    requestAnimationFrame(animate);
}
```

### 使用 CSS 动画

```js
// CSS 动画由浏览器优化，性能更好
.element {
    transition: transform 0.3s ease;
}
.element:hover {
    transform: scale(1.1);
}
```

### 避免动画属性

```js
// 错误：动画会触发重排的属性
.element {
    transition: width 0.3s, height 0.3s, left 0.3s, top 0.3s;
}

// 正确：动画只触发合成的属性
.element {
    transition: transform 0.3s, opacity 0.3s;
}
```

## 注意事项

1. **减少重排**：批量修改 DOM，使用 DocumentFragment
2. **使用 transform**：用 transform 代替位置属性
3. **读写分离**：先读取所有值，再统一写入
4. **CSS 动画**：优先使用 CSS 动画
5. **合成层**：合理使用合成层，避免过度使用

## 常见错误

### 错误 1：频繁读取布局属性

```js
// 错误：在循环中频繁读取布局属性
for (let i = 0; i < elements.length; i++) {
    const width = elements[i].offsetWidth; // 触发重排
    elements[i].style.width = width + 10 + 'px';
}

// 正确：缓存布局属性
const widths = elements.map(el => el.offsetWidth);
for (let i = 0; i < elements.length; i++) {
    elements[i].style.width = widths[i] + 10 + 'px';
}
```

### 错误 2：动画会触发重排的属性

```js
// 错误：动画 left/top 会触发重排
.element {
    transition: left 0.3s, top 0.3s;
}

// 正确：使用 transform
.element {
    transition: transform 0.3s;
}
```

## 最佳实践

1. **批量修改**：批量修改 DOM，减少重排次数
2. **使用 transform**：用 transform 代替位置属性
3. **CSS 动画**：优先使用 CSS 动画
4. **合成层**：合理使用合成层
5. **性能测试**：使用性能分析工具验证优化效果

## 练习

1. **批量 DOM 操作**：优化一个频繁修改 DOM 的函数，使用 DocumentFragment。

2. **动画优化**：将一个使用 left/top 的动画改为使用 transform。

3. **读写分离**：优化一个混合读写布局属性的函数。

4. **CSS 动画**：使用 CSS 动画实现一个性能优化的动画效果。

5. **性能分析**：使用 Chrome DevTools 分析渲染性能，找出性能瓶颈。

完成以上练习后，继续学习下一节，了解网络性能优化。

## 总结

渲染性能优化包括减少重排、减少重绘、使用合成层和优化动画。通过批量修改 DOM、使用 transform、读写分离、使用 CSS 动画等方法，可以显著提升渲染性能。使用性能分析工具可以帮助识别和解决性能问题。

## 相关资源

- [MDN：渲染性能](https://developer.mozilla.org/zh-CN/docs/Web/Performance)
- [Chrome DevTools Performance 面板](https://developer.chrome.com/docs/devtools/performance/)
