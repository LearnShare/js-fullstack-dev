# 4.2.2 事件监听与移除

## 概述

事件监听是前端开发中的基础技能。本节介绍 addEventListener、removeEventListener 的使用方法，以及事件监听器的最佳实践。

## addEventListener()

### 基本语法

**语法格式**：`element.addEventListener(type, listener[, options])`

**参数说明**：

| 参数名      | 类型     | 说明                           | 是否必需 | 默认值 |
|:------------|:---------|:-------------------------------|:---------|:-------|
| `type`      | string   | 事件类型（如 'click'）         | 是       | -      |
| `listener`  | function | 事件处理函数                    | 是       | -      |
| `options`   | object   | 可选配置对象                    | 否       | -      |

**options 对象属性**：

| 属性名      | 类型    | 说明                           | 默认值 |
|:------------|:--------|:-------------------------------|:-------|
| `capture`   | boolean | 是否在捕获阶段触发              | false  |
| `once`      | boolean | 是否只触发一次后自动移除        | false  |
| `passive`   | boolean | 是否是被动监听器                | false  |
| `signal`    | AbortSignal | 用于移除监听器的信号对象    | -      |

**返回值**：undefined

### 基本使用

```js
const button = document.querySelector('button');

// 基本用法
button.addEventListener('click', () => {
    console.log('按钮被点击');
});

// 使用函数引用
function handleClick() {
    console.log('按钮被点击');
}
button.addEventListener('click', handleClick);
```

### 传递参数

```js
// 使用箭头函数传递参数
button.addEventListener('click', () => {
    handleClick('参数1', '参数2');
});

// 使用 bind 传递参数
button.addEventListener('click', handleClick.bind(null, '参数1', '参数2'));

// 使用包装函数
button.addEventListener('click', function(e) {
    handleClick('参数1', '参数2', e);
});
```

### 事件对象

```js
button.addEventListener('click', (event) => {
    console.log('事件类型：', event.type);
    console.log('目标元素：', event.target);
    console.log('当前元素：', event.currentTarget);
    console.log('时间戳：', event.timeStamp);
});
```

### 使用 options 对象

```js
// 只在捕获阶段触发
button.addEventListener('click', handler, { capture: true });

// 只触发一次后自动移除
button.addEventListener('click', handler, { once: true });

// 被动监听器（提升性能）
button.addEventListener('touchstart', handler, { passive: true });

// 组合使用
button.addEventListener('click', handler, {
    capture: false,
    once: true,
    passive: false
});
```

### once 选项

```js
// 使用 once 选项，事件只触发一次
button.addEventListener('click', () => {
    console.log('只会执行一次');
}, { once: true });

// 等同于：
let executed = false;
button.addEventListener('click', () => {
    if (!executed) {
        console.log('只会执行一次');
        executed = true;
        button.removeEventListener('click', arguments.callee);
    }
});
```

### passive 选项

```js
// passive 选项提升滚动性能
window.addEventListener('scroll', (e) => {
    // 不能调用 e.preventDefault()（会警告）
}, { passive: true });

// 非 passive 监听器
window.addEventListener('scroll', (e) => {
    e.preventDefault(); // 可以调用，但会影响性能
}, { passive: false });
```

### signal 选项

```js
// 使用 AbortController 创建信号
const controller = new AbortController();
const signal = controller.signal;

button.addEventListener('click', handler, { signal });

// 移除监听器
controller.abort();
```

## removeEventListener()

### 基本语法

**语法格式**：`element.removeEventListener(type, listener[, options])`

**参数说明**：

| 参数名      | 类型     | 说明                           | 是否必需 | 默认值 |
|:------------|:---------|:-------------------------------|:---------|:-------|
| `type`      | string   | 事件类型                        | 是       | -      |
| `listener`  | function | 要移除的事件处理函数            | 是       | -      |
| `options`   | object   | 可选配置对象（需与添加时一致）  | 否       | -      |

**返回值**：undefined

### 基本使用

```js
// 添加监听器
function handleClick() {
    console.log('按钮被点击');
}
button.addEventListener('click', handleClick);

// 移除监听器
button.removeEventListener('click', handleClick);
```

### 必须使用相同的函数引用

```js
// 错误：无法移除匿名函数
button.addEventListener('click', () => {
    console.log('点击');
});
button.removeEventListener('click', () => {
    console.log('点击');
}); // 无法移除，因为这是不同的函数引用

// 正确：使用函数引用
function handleClick() {
    console.log('点击');
}
button.addEventListener('click', handleClick);
button.removeEventListener('click', handleClick); // 成功移除
```

### 使用对象方法

```js
// 使用对象方法作为监听器
const obj = {
    name: 'MyObject',
    handleClick(e) {
        console.log(this.name, '被点击');
    }
};

// 需要使用 bind 绑定 this
button.addEventListener('click', obj.handleClick.bind(obj));
button.removeEventListener('click', obj.handleClick.bind(obj)); // 无法移除，bind 创建了新函数

// 正确：保存绑定后的函数引用
const boundHandler = obj.handleClick.bind(obj);
button.addEventListener('click', boundHandler);
button.removeEventListener('click', boundHandler); // 成功移除
```

### 移除带有 options 的监听器

```js
// 添加监听器时指定 options
button.addEventListener('click', handler, { capture: true });

// 移除时必须指定相同的 options
button.removeEventListener('click', handler, { capture: true });
```

## 事件监听器管理

### 存储函数引用

```js
// 存储所有监听器引用，便于管理
const listeners = {
    click: [],
    mouseover: [],
    mouseout: []
};

function addManagedListener(element, type, handler) {
    element.addEventListener(type, handler);
    listeners[type].push({ element, handler });
}

function removeAllListeners(element) {
    Object.keys(listeners).forEach(type => {
        listeners[type].forEach(({ element: el, handler }) => {
            if (el === element) {
                el.removeEventListener(type, handler);
            }
        });
    });
}
```

### 使用 AbortController

```js
// 使用 AbortController 管理多个监听器
const controller = new AbortController();
const { signal } = controller;

button.addEventListener('click', handler1, { signal });
button.addEventListener('click', handler2, { signal });
window.addEventListener('scroll', handler3, { signal });

// 一次性移除所有监听器
controller.abort();
```

### 命名空间模式

```js
// 创建带命名空间的监听器管理
const EventManager = {
    listeners: new Map(),
    
    on(element, type, handler, options) {
        element.addEventListener(type, handler, options);
        const key = `${element}-${type}`;
        if (!this.listeners.has(key)) {
            this.listeners.set(key, []);
        }
        this.listeners.get(key).push({ handler, options });
    },
    
    off(element, type, handler, options) {
        element.removeEventListener(type, handler, options);
        const key = `${element}-${type}`;
        const handlers = this.listeners.get(key);
        if (handlers) {
            const index = handlers.findIndex(h => h.handler === handler);
            if (index > -1) {
                handlers.splice(index, 1);
            }
        }
    },
    
    removeAll(element, type) {
        const key = `${element}-${type}`;
        const handlers = this.listeners.get(key);
        if (handlers) {
            handlers.forEach(({ handler, options }) => {
                element.removeEventListener(type, handler, options);
            });
            this.listeners.delete(key);
        }
    }
};
```

## 注意事项

1. **函数引用**：removeEventListener 需要相同的函数引用
2. **options 一致性**：移除时 options 需与添加时一致
3. **内存泄漏**：及时移除不再需要的监听器，避免内存泄漏
4. **性能考虑**：使用 passive 选项提升滚动性能
5. **once 选项**：需要只触发一次时，使用 once 选项

## 常见错误

### 错误 1：无法移除匿名函数

```js
// 错误：无法移除匿名函数
button.addEventListener('click', () => {
    console.log('点击');
});
button.removeEventListener('click', () => {
    console.log('点击');
}); // 无法移除

// 正确：使用函数引用
const handler = () => {
    console.log('点击');
};
button.addEventListener('click', handler);
button.removeEventListener('click', handler);
```

### 错误 2：options 不一致

```js
// 错误：添加和移除时的 options 不一致
button.addEventListener('click', handler, { capture: true });
button.removeEventListener('click', handler); // 无法移除

// 正确：使用相同的 options
button.addEventListener('click', handler, { capture: true });
button.removeEventListener('click', handler, { capture: true });
```

### 错误 3：忘记移除监听器

```js
// 错误：动态元素被移除后，监听器仍然存在
function createElement() {
    const div = document.createElement('div');
    div.addEventListener('click', handler);
    document.body.appendChild(div);
    // 元素移除后，监听器可能无法被垃圾回收
}

// 正确：在移除元素前先移除监听器
function removeElement(div) {
    div.removeEventListener('click', handler);
    div.remove();
}
```

## 最佳实践

1. **使用函数引用**：避免使用匿名函数，便于移除
2. **及时清理**：在元素移除前清理监听器
3. **使用 once**：需要只触发一次时使用 once 选项
4. **使用 passive**：滚动事件使用 passive 提升性能
5. **管理监听器**：使用工具类或 AbortController 管理监听器

## 练习

1. **基本监听**：创建一个按钮，添加点击事件监听器，点击后移除监听器。

2. **options 使用**：创建一个按钮，使用 once 选项，观察事件只触发一次。

3. **监听器管理**：创建一个监听器管理类，可以添加、移除和批量移除监听器。

4. **AbortController**：使用 AbortController 管理多个事件监听器，实现一次性移除。

5. **动态元素**：创建动态添加和移除元素的场景，确保监听器正确清理。

完成以上练习后，继续学习下一节，了解常见事件类型。

## 总结

addEventListener 和 removeEventListener 是事件处理的基础方法。addEventListener 可以添加事件监听器，支持多种 options 配置。removeEventListener 用于移除监听器，需要提供相同的函数引用和 options。正确管理事件监听器可以避免内存泄漏，提升应用性能。

## 相关资源

- [MDN：addEventListener](https://developer.mozilla.org/zh-CN/docs/Web/API/EventTarget/addEventListener)
- [MDN：removeEventListener](https://developer.mozilla.org/zh-CN/docs/Web/API/EventTarget/removeEventListener)
