# 4.2.1 事件模型（捕获、冒泡、委托）

## 概述

事件模型是浏览器中事件处理的核心机制。本节介绍事件捕获、事件冒泡和事件委托的概念，帮助你理解事件在 DOM 树中的传播过程。

## 事件流

### 三个阶段

事件在 DOM 中的传播分为三个阶段：

1. **捕获阶段（Capture Phase）**：从 window 对象向下传播到目标元素
2. **目标阶段（Target Phase）**：事件到达目标元素
3. **冒泡阶段（Bubble Phase）**：从目标元素向上传播到 window 对象

```html
<!DOCTYPE html>
<html>
<head>
    <title>事件流示例</title>
</head>
<body>
    <div id="outer">
        <div id="inner">
            <button id="button">点击我</button>
        </div>
    </div>
</body>
</html>
```

```js
// 事件流的三个阶段
const outer = document.getElementById('outer');
const inner = document.getElementById('inner');
const button = document.getElementById('button');

// 捕获阶段（第三个参数为 true）
outer.addEventListener('click', () => {
    console.log('捕获阶段：outer');
}, true);

inner.addEventListener('click', () => {
    console.log('捕获阶段：inner');
}, true);

button.addEventListener('click', () => {
    console.log('目标阶段：button');
});

// 冒泡阶段（第三个参数为 false 或省略）
inner.addEventListener('click', () => {
    console.log('冒泡阶段：inner');
}, false);

outer.addEventListener('click', () => {
    console.log('冒泡阶段：outer');
}, false);

// 点击按钮后的输出顺序：
// 1. 捕获阶段：outer
// 2. 捕获阶段：inner
// 3. 目标阶段：button
// 4. 冒泡阶段：inner
// 5. 冒泡阶段：outer
```

## 事件捕获

### 基本概念

事件捕获是事件从最外层元素向下传播到目标元素的过程。

### 使用捕获

```js
// 使用 addEventListener 的第三个参数启用捕获
element.addEventListener('click', handler, true);

// 或者使用 options 对象
element.addEventListener('click', handler, { capture: true });
```

### 捕获阶段示例

```js
document.addEventListener('click', (e) => {
    console.log('捕获：document');
}, true);

document.body.addEventListener('click', (e) => {
    console.log('捕获：body');
}, true);

const div = document.querySelector('div');
div.addEventListener('click', (e) => {
    console.log('捕获：div');
}, true);

// 点击 div 时的输出顺序：
// 1. 捕获：document
// 2. 捕获：body
// 3. 捕获：div
```

## 事件冒泡

### 基本概念

事件冒泡是事件从目标元素向上传播到最外层元素的过程。

### 使用冒泡

```js
// 默认使用冒泡（第三个参数为 false 或省略）
element.addEventListener('click', handler, false);

// 或者使用 options 对象
element.addEventListener('click', handler, { capture: false });
```

### 冒泡阶段示例

```js
const div = document.querySelector('div');
div.addEventListener('click', (e) => {
    console.log('冒泡：div');
});

document.body.addEventListener('click', (e) => {
    console.log('冒泡：body');
});

document.addEventListener('click', (e) => {
    console.log('冒泡：document');
});

// 点击 div 时的输出顺序：
// 1. 冒泡：div
// 2. 冒泡：body
// 3. 冒泡：document
```

### 阻止冒泡

```js
// 使用 stopPropagation() 阻止事件冒泡
element.addEventListener('click', (e) => {
    e.stopPropagation(); // 阻止事件继续传播
    console.log('事件被阻止，不会继续冒泡');
});
```

### stopPropagation() 方法

**语法格式**：`event.stopPropagation()`

**参数说明**：无

**返回值**：undefined

**基本使用**：

```js
const outer = document.getElementById('outer');
const inner = document.getElementById('inner');

outer.addEventListener('click', () => {
    console.log('outer 被点击');
});

inner.addEventListener('click', (e) => {
    e.stopPropagation(); // 阻止事件继续传播到 outer
    console.log('inner 被点击，事件不会传播到 outer');
});
```

## 事件委托

### 基本概念

事件委托（Event Delegation）是将事件监听器添加到父元素，利用事件冒泡机制处理子元素的事件。

### 为什么使用事件委托

1. **性能优势**：减少事件监听器数量，提升性能
2. **动态元素**：可以处理动态添加的元素
3. **代码简化**：减少重复代码

### 基本示例

```html
<ul id="list">
    <li>项目 1</li>
    <li>项目 2</li>
    <li>项目 3</li>
</ul>
```

```js
// 不使用事件委托（需要为每个 li 添加监听器）
const items = document.querySelectorAll('#list li');
items.forEach(item => {
    item.addEventListener('click', (e) => {
        console.log('点击了：', e.target.textContent);
    });
});

// 使用事件委托（只需要一个监听器）
const list = document.getElementById('list');
list.addEventListener('click', (e) => {
    if (e.target.tagName === 'LI') {
        console.log('点击了：', e.target.textContent);
    }
});
```

### 动态元素处理

```js
// 使用事件委托处理动态添加的元素
const list = document.getElementById('list');

// 委托监听器（可以处理后续添加的元素）
list.addEventListener('click', (e) => {
    if (e.target.tagName === 'LI') {
        console.log('点击了：', e.target.textContent);
    }
});

// 动态添加新元素
function addItem(text) {
    const li = document.createElement('li');
    li.textContent = text;
    list.appendChild(li);
    // 新添加的元素自动具有点击事件（通过事件委托）
}

addItem('项目 4');
addItem('项目 5');
```

### 使用 closest() 方法

```js
// 使用 closest() 查找最近的匹配元素
list.addEventListener('click', (e) => {
    const item = e.target.closest('li');
    if (item) {
        console.log('点击了：', item.textContent);
    }
});

// 即使点击的是 li 内部的元素（如 span），也能正确找到 li
```

### closest() 方法

**语法格式**：`element.closest(selector)`

**参数说明**：

| 参数名      | 类型   | 说明           | 是否必需 | 默认值 |
|:------------|:-------|:---------------|:---------|:-------|
| `selector`  | string | CSS 选择器     | 是       | -      |

**返回值**：匹配的元素或 null

**基本使用**：

```js
const element = document.querySelector('span');
const li = element.closest('li');
if (li) {
    console.log('找到父级 li 元素');
}
```

## 事件对象

### event.target vs event.currentTarget

```js
const outer = document.getElementById('outer');
const inner = document.getElementById('inner');

outer.addEventListener('click', (e) => {
    console.log('target:', e.target);        // 实际点击的元素（inner）
    console.log('currentTarget:', e.currentTarget); // 绑定事件的元素（outer）
});

inner.addEventListener('click', (e) => {
    console.log('target:', e.target);        // 实际点击的元素（inner）
    console.log('currentTarget:', e.currentTarget); // 绑定事件的元素（inner）
});
```

### 阻止默认行为

```js
// 使用 preventDefault() 阻止默认行为
const link = document.querySelector('a');
link.addEventListener('click', (e) => {
    e.preventDefault(); // 阻止链接跳转
    console.log('链接跳转被阻止');
});
```

### preventDefault() 方法

**语法格式**：`event.preventDefault()`

**参数说明**：无

**返回值**：undefined

**基本使用**：

```js
const form = document.querySelector('form');
form.addEventListener('submit', (e) => {
    e.preventDefault(); // 阻止表单提交
    // 执行自定义逻辑
});
```

## 注意事项

1. **事件顺序**：捕获阶段 → 目标阶段 → 冒泡阶段
2. **默认行为**：某些事件有默认行为，需要使用 preventDefault() 阻止
3. **事件委托**：适用于需要处理多个相似元素的情况
4. **性能考虑**：事件委托可以减少监听器数量，提升性能
5. **事件对象**：理解 target 和 currentTarget 的区别

## 常见错误

### 错误 1：混淆捕获和冒泡

```js
// 错误：以为第三个参数是控制冒泡
element.addEventListener('click', handler, false); // false 表示冒泡阶段

// 正确：理解第三个参数的作用
element.addEventListener('click', handler, true);  // true 表示捕获阶段
element.addEventListener('click', handler, false); // false 表示冒泡阶段
```

### 错误 2：事件委托中错误使用 target

```js
// 错误：直接使用 target，可能点击的是子元素
list.addEventListener('click', (e) => {
    console.log(e.target.textContent); // 如果点击的是 span，不会得到 li 的文本
});

// 正确：使用 closest() 或检查 tagName
list.addEventListener('click', (e) => {
    const item = e.target.closest('li');
    if (item) {
        console.log(item.textContent);
    }
});
```

### 错误 3：忘记阻止默认行为

```js
// 错误：没有阻止默认行为
link.addEventListener('click', () => {
    // 执行自定义逻辑，但链接仍然会跳转
});

// 正确：阻止默认行为
link.addEventListener('click', (e) => {
    e.preventDefault();
    // 执行自定义逻辑
});
```

## 最佳实践

1. **使用事件委托**：对于多个相似元素，使用事件委托
2. **理解事件流**：理解捕获和冒泡机制，选择合适的事件阶段
3. **合理阻止传播**：只在必要时使用 stopPropagation()
4. **阻止默认行为**：需要自定义行为时，记得阻止默认行为
5. **使用 closest()**：在事件委托中使用 closest() 查找目标元素

## 练习

1. **事件流演示**：创建一个包含嵌套元素的页面，演示事件的捕获和冒泡阶段。

2. **事件委托**：使用事件委托实现一个动态列表，可以添加和删除项目。

3. **阻止冒泡**：创建一个示例，演示 stopPropagation() 的使用。

4. **阻止默认行为**：创建一个表单，使用 preventDefault() 阻止默认提交，实现自定义验证。

5. **综合应用**：创建一个标签页切换组件，使用事件委托处理标签点击。

完成以上练习后，继续学习下一节，了解事件监听与移除。

## 总结

事件模型包括捕获、冒泡和委托三个核心概念。事件在 DOM 中按三个阶段传播：捕获阶段、目标阶段和冒泡阶段。事件委托利用冒泡机制，将事件监听器添加到父元素，可以处理多个子元素的事件，提升性能和代码可维护性。

## 相关资源

- [MDN：事件参考](https://developer.mozilla.org/zh-CN/docs/Web/Events)
- [MDN：事件介绍](https://developer.mozilla.org/zh-CN/docs/Learn/JavaScript/Building_blocks/Events)
