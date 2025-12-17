# 4.2.3 常见事件类型

## 概述

浏览器支持多种事件类型，包括鼠标事件、键盘事件、表单事件、焦点事件等。本节介绍常见的事件类型及其使用方法。

## 鼠标事件

### 常见鼠标事件

| 事件类型      | 说明                       | 触发时机                     |
|:--------------|:---------------------------|:-----------------------------|
| `click`       | 点击事件                   | 鼠标点击元素                 |
| `dblclick`    | 双击事件                   | 鼠标双击元素                 |
| `mousedown`   | 鼠标按下                   | 鼠标按下时                   |
| `mouseup`     | 鼠标释放                   | 鼠标释放时                   |
| `mousemove`   | 鼠标移动                   | 鼠标在元素上移动时           |
| `mouseenter`  | 鼠标进入                   | 鼠标进入元素时（不冒泡）     |
| `mouseleave`  | 鼠标离开                   | 鼠标离开元素时（不冒泡）     |
| `mouseover`   | 鼠标悬停                   | 鼠标进入元素时（冒泡）       |
| `mouseout`    | 鼠标移出                   | 鼠标离开元素时（冒泡）       |
| `contextmenu` | 右键菜单                   | 右键点击时                   |

### click 事件

```js
const button = document.querySelector('button');
button.addEventListener('click', (e) => {
    console.log('按钮被点击');
    console.log('鼠标位置：', e.clientX, e.clientY);
    console.log('点击的按键：', e.button); // 0: 左键, 1: 中键, 2: 右键
});
```

### mousedown 和 mouseup

```js
const element = document.querySelector('div');

element.addEventListener('mousedown', (e) => {
    console.log('鼠标按下');
    console.log('按键：', e.button);
});

element.addEventListener('mouseup', (e) => {
    console.log('鼠标释放');
});
```

### mousemove 事件

```js
const element = document.querySelector('div');
let moveCount = 0;

element.addEventListener('mousemove', (e) => {
    moveCount++;
    console.log(`鼠标移动 ${moveCount} 次`);
    console.log('位置：', e.clientX, e.clientY);
});
```

### mouseenter 和 mouseleave

```js
// mouseenter 和 mouseleave 不冒泡
const outer = document.getElementById('outer');
const inner = document.getElementById('inner');

outer.addEventListener('mouseenter', () => {
    console.log('进入 outer');
});

outer.addEventListener('mouseleave', () => {
    console.log('离开 outer');
});

// 鼠标从 outer 移动到 inner 时：
// 不会触发 outer 的 mouseleave
```

### mouseover 和 mouseout

```js
// mouseover 和 mouseout 会冒泡
const outer = document.getElementById('outer');
const inner = document.getElementById('inner');

outer.addEventListener('mouseover', () => {
    console.log('mouseover outer');
});

outer.addEventListener('mouseout', () => {
    console.log('mouseout outer');
});

// 鼠标从 outer 移动到 inner 时：
// 会触发 outer 的 mouseout（因为冒泡）
```

### contextmenu 事件

```js
const element = document.querySelector('div');

element.addEventListener('contextmenu', (e) => {
    e.preventDefault(); // 阻止默认右键菜单
    console.log('右键点击');
    // 显示自定义菜单
});
```

## 键盘事件

### 常见键盘事件

| 事件类型    | 说明         | 触发时机           |
|:------------|:-------------|:-------------------|
| `keydown`   | 按键按下     | 按下键盘按键时     |
| `keyup`     | 按键释放     | 释放键盘按键时     |
| `keypress`  | 按键按下     | 按下字符键时（已废弃） |

### keydown 和 keyup

```js
document.addEventListener('keydown', (e) => {
    console.log('按键按下：', e.key);
    console.log('键码：', e.code);
    console.log('是否按下 Ctrl：', e.ctrlKey);
    console.log('是否按下 Shift：', e.shiftKey);
    console.log('是否按下 Alt：', e.altKey);
});

document.addEventListener('keyup', (e) => {
    console.log('按键释放：', e.key);
});
```

### 常用按键检测

```js
document.addEventListener('keydown', (e) => {
    // 检测特定按键
    if (e.key === 'Enter') {
        console.log('按下了 Enter 键');
    }
    
    if (e.key === 'Escape') {
        console.log('按下了 ESC 键');
    }
    
    // 检测组合键
    if (e.ctrlKey && e.key === 's') {
        e.preventDefault(); // 阻止默认保存
        console.log('Ctrl+S 被按下');
    }
    
    if (e.shiftKey && e.key === 'Tab') {
        console.log('Shift+Tab 被按下');
    }
});
```

### key 属性 vs code 属性

```js
document.addEventListener('keydown', (e) => {
    console.log('key:', e.key);   // 实际字符（如 'a', 'A'）
    console.log('code:', e.code); // 物理按键（如 'KeyA'）
});

// 按下 'a' 键：
// key: 'a'（如果同时按 Shift，则为 'A'）
// code: 'KeyA'（始终是 'KeyA'）
```

## 表单事件

### 常见表单事件

| 事件类型    | 说明         | 触发时机                   |
|:------------|:-------------|:---------------------------|
| `submit`    | 表单提交     | 表单提交时                 |
| `reset`     | 表单重置     | 表单重置时                 |
| `change`    | 值改变       | 表单元素值改变并失去焦点时 |
| `input`     | 输入事件     | 表单元素值改变时（实时）   |
| `focus`     | 获得焦点     | 元素获得焦点时             |
| `blur`      | 失去焦点     | 元素失去焦点时             |

### submit 事件

```js
const form = document.querySelector('form');

form.addEventListener('submit', (e) => {
    e.preventDefault(); // 阻止默认提交
    console.log('表单提交');
    
    // 获取表单数据
    const formData = new FormData(form);
    for (const [key, value] of formData.entries()) {
        console.log(key, value);
    }
});
```

### change 事件

```js
const input = document.querySelector('input[type="text"]');
const select = document.querySelector('select');
const checkbox = document.querySelector('input[type="checkbox"]');

input.addEventListener('change', (e) => {
    console.log('输入值改变：', e.target.value);
});

select.addEventListener('change', (e) => {
    console.log('选择改变：', e.target.value);
});

checkbox.addEventListener('change', (e) => {
    console.log('复选框状态：', e.target.checked);
});
```

### input 事件

```js
// input 事件在值改变时立即触发（不需要失去焦点）
const input = document.querySelector('input');

input.addEventListener('input', (e) => {
    console.log('当前值：', e.target.value);
    // 实时验证或搜索
});
```

### focus 和 blur 事件

```js
const input = document.querySelector('input');

input.addEventListener('focus', (e) => {
    console.log('输入框获得焦点');
    e.target.style.borderColor = 'blue';
});

input.addEventListener('blur', (e) => {
    console.log('输入框失去焦点');
    e.target.style.borderColor = '';
    // 验证输入
});
```

## 窗口事件

### 常见窗口事件

| 事件类型    | 说明         | 触发时机           |
|:------------|:-------------|:-------------------|
| `load`      | 页面加载完成 | 页面完全加载后     |
| `DOMContentLoaded` | DOM 加载完成 | DOM 解析完成后   |
| `resize`    | 窗口大小改变 | 窗口大小改变时     |
| `scroll`    | 滚动事件     | 页面滚动时         |
| `beforeunload` | 页面卸载前 | 页面卸载前         |

### load 事件

```js
window.addEventListener('load', () => {
    console.log('页面完全加载完成');
    // 所有资源（图片、样式等）都已加载
});

// 图片加载完成
const img = document.querySelector('img');
img.addEventListener('load', () => {
    console.log('图片加载完成');
});
```

### DOMContentLoaded 事件

```js
// DOMContentLoaded 在 DOM 解析完成后立即触发（不需要等待资源）
document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM 加载完成');
    // 可以安全地操作 DOM
});
```

### resize 事件

```js
window.addEventListener('resize', () => {
    console.log('窗口大小改变');
    console.log('宽度：', window.innerWidth);
    console.log('高度：', window.innerHeight);
});
```

### scroll 事件

```js
window.addEventListener('scroll', () => {
    console.log('页面滚动');
    console.log('滚动位置：', window.scrollY);
});

// 使用节流优化性能
let ticking = false;
window.addEventListener('scroll', () => {
    if (!ticking) {
        window.requestAnimationFrame(() => {
            console.log('滚动位置：', window.scrollY);
            ticking = false;
        });
        ticking = true;
    }
});
```

### beforeunload 事件

```js
window.addEventListener('beforeunload', (e) => {
    e.preventDefault();
    e.returnValue = ''; // Chrome 需要设置 returnValue
    return ''; // 某些浏览器需要返回值
});
```

## 触摸事件（移动端）

### 常见触摸事件

| 事件类型      | 说明         | 触发时机           |
|:--------------|:-------------|:-------------------|
| `touchstart`  | 触摸开始     | 手指触摸屏幕时     |
| `touchmove`   | 触摸移动     | 手指在屏幕上移动时 |
| `touchend`    | 触摸结束     | 手指离开屏幕时     |
| `touchcancel` | 触摸取消     | 触摸被系统取消时   |

### 基本使用

```js
const element = document.querySelector('div');

element.addEventListener('touchstart', (e) => {
    console.log('触摸开始');
    const touch = e.touches[0];
    console.log('位置：', touch.clientX, touch.clientY);
});

element.addEventListener('touchmove', (e) => {
    e.preventDefault(); // 阻止滚动（如果不是 passive）
    const touch = e.touches[0];
    console.log('移动位置：', touch.clientX, touch.clientY);
});

element.addEventListener('touchend', (e) => {
    console.log('触摸结束');
});
```

## 注意事项

1. **事件顺序**：理解事件的触发顺序（如 mousedown → mouseup → click）
2. **移动端适配**：移动端需要考虑触摸事件
3. **性能优化**：scroll 和 resize 事件需要使用节流
4. **事件冒泡**：理解不同事件的冒泡行为
5. **默认行为**：某些事件有默认行为，需要时阻止

## 常见错误

### 错误 1：混淆 mouseenter 和 mouseover

```js
// mouseenter 不冒泡，mouseover 会冒泡
// 根据需求选择合适的事件
```

### 错误 2：scroll 事件性能问题

```js
// 错误：scroll 事件频繁触发，影响性能
window.addEventListener('scroll', () => {
    // 复杂的计算
});

// 正确：使用节流或 requestAnimationFrame
```

### 错误 3：input 和 change 混淆

```js
// change 在失去焦点时触发
// input 在值改变时立即触发
// 根据需求选择合适的事件
```

## 最佳实践

1. **选择合适的事件**：根据需求选择最合适的事件类型
2. **性能优化**：对频繁触发的事件使用节流或防抖
3. **移动端适配**：考虑触摸事件的兼容性
4. **阻止默认行为**：需要时使用 preventDefault()
5. **事件委托**：对多个元素使用事件委托

## 练习

1. **鼠标事件**：创建一个可拖拽的元素，使用 mousedown、mousemove、mouseup 实现。

2. **键盘事件**：创建一个快捷键系统，支持 Ctrl+S、Ctrl+C 等组合键。

3. **表单验证**：创建一个表单，使用 input 和 blur 事件实现实时验证。

4. **滚动加载**：使用 scroll 事件实现无限滚动加载。

5. **触摸滑动**：在移动端实现一个可以滑动切换的图片轮播。

完成以上练习后，继续学习下一节，了解自定义事件。

## 总结

常见事件类型包括鼠标事件、键盘事件、表单事件、窗口事件和触摸事件。不同事件有不同的触发时机和用途。理解各种事件的特点和使用方法，可以更好地实现交互功能。

## 相关资源

- [MDN：事件参考](https://developer.mozilla.org/zh-CN/docs/Web/Events)
- [MDN：鼠标事件](https://developer.mozilla.org/zh-CN/docs/Web/API/MouseEvent)
- [MDN：键盘事件](https://developer.mozilla.org/zh-CN/docs/Web/API/KeyboardEvent)
