# 3.1.1 事件循环机制概述

## 概述

JavaScript 采用单线程执行模型，通过事件循环（Event Loop）机制实现异步操作。理解事件循环是掌握 JavaScript 异步编程的基础。本节介绍 JavaScript 的单线程模型和事件循环的基本概念。

## JavaScript 的单线程模型

### 什么是单线程

JavaScript 是**单线程**的，这意味着：

- 同一时间只能执行一个任务
- 代码按照顺序逐行执行
- 不能并行执行多个 JavaScript 代码段

### 为什么是单线程

JavaScript 最初设计用于浏览器中操作 DOM，单线程设计避免了复杂的同步问题：

```js
// 如果是多线程，可能出现问题：
// 线程1：删除元素
element.remove();
// 线程2：同时修改元素（冲突！）
element.innerHTML = 'new content';
```

单线程避免了竞争条件（Race Condition），简化了编程模型。

### 单线程的局限性

单线程模型的局限性：

```js
// 耗时操作会阻塞后续代码
console.log('开始');
for (let i = 0; i < 1000000000; i++) {
    // 耗时计算
}
console.log('结束'); // 要等待很久才能执行
```

为了解决这个问题，JavaScript 引入了**异步编程**机制。

## 事件循环的基本概念

### 什么是事件循环

事件循环（Event Loop）是 JavaScript 的执行机制，负责：

1. 管理调用栈（Call Stack）
2. 管理任务队列（Task Queue）
3. 在调用栈为空时，将队列中的任务推入调用栈执行

### 事件循环的工作原理

事件循环的工作流程：

1. **执行同步代码**：将同步代码推入调用栈执行
2. **处理异步操作**：遇到异步操作时，将其交给 Web API 处理
3. **接收回调**：异步操作完成后，将回调函数放入任务队列
4. **循环执行**：当调用栈为空时，从任务队列取出任务执行

```js
console.log('1'); // 同步代码，立即执行

setTimeout(() => {
    console.log('2'); // 异步代码，稍后执行
}, 0);

console.log('3'); // 同步代码，立即执行

// 输出顺序：1, 3, 2
```

### 事件循环的可视化

```
┌─────────────────┐
│   调用栈 (Stack) │  ← 当前执行的代码
└─────────────────┘
        ↓
┌─────────────────┐
│   事件循环      │  ← 管理调用栈和队列
└─────────────────┘
        ↓
┌─────────────────┐
│   任务队列       │  ← 等待执行的任务
└─────────────────┘
        ↓
┌─────────────────┐
│   Web APIs      │  ← 浏览器提供的异步 API
└─────────────────┘
```

## 异步操作的类型

### 定时器操作

```js
// setTimeout：延迟执行
setTimeout(() => {
    console.log('延迟执行');
}, 1000);

// setInterval：定时重复执行
const timer = setInterval(() => {
    console.log('重复执行');
}, 1000);

// 清除定时器
clearInterval(timer);
```

### I/O 操作

```js
// 文件读取（Node.js）
const fs = require('fs');
fs.readFile('file.txt', 'utf8', (err, data) => {
    console.log(data);
});

// 网络请求（浏览器）
fetch('https://api.example.com/data')
    .then(response => response.json())
    .then(data => console.log(data));
```

### 事件监听

```js
// DOM 事件
button.addEventListener('click', () => {
    console.log('按钮被点击');
});

// 自定义事件
window.addEventListener('load', () => {
    console.log('页面加载完成');
});
```

## 事件循环的执行顺序

### 基本执行顺序

1. **同步代码**：首先执行所有同步代码
2. **微任务**：执行所有微任务（Promise.then、queueMicrotask）
3. **宏任务**：执行一个宏任务（setTimeout、setInterval 等）
4. **重复**：重复步骤 2-3

```js
console.log('1'); // 同步代码

setTimeout(() => {
    console.log('2'); // 宏任务
}, 0);

Promise.resolve().then(() => {
    console.log('3'); // 微任务
});

console.log('4'); // 同步代码

// 输出顺序：1, 4, 3, 2
```

### 执行顺序示例

```js
console.log('开始');

setTimeout(() => {
    console.log('setTimeout 1');
}, 0);

Promise.resolve().then(() => {
    console.log('Promise 1');
});

setTimeout(() => {
    console.log('setTimeout 2');
}, 0);

Promise.resolve().then(() => {
    console.log('Promise 2');
});

console.log('结束');

// 输出顺序：
// 开始
// 结束
// Promise 1
// Promise 2
// setTimeout 1
// setTimeout 2
```

## 事件循环的应用场景

### 避免阻塞

```js
// 使用 setTimeout 将耗时操作分解
function processLargeArray(array) {
    const chunk = array.splice(0, 1000);
    
    // 处理当前块
    chunk.forEach(item => {
        // 处理逻辑
    });
    
    // 如果还有剩余，继续处理
    if (array.length > 0) {
        setTimeout(() => {
            processLargeArray(array);
        }, 0);
    }
}
```

### 批量更新 DOM

```js
// 批量更新 DOM，避免频繁重排
const updates = [];
function scheduleUpdate(element, value) {
    updates.push({ element, value });
    
    // 使用微任务批量更新
    Promise.resolve().then(() => {
        updates.forEach(({ element, value }) => {
            element.textContent = value;
        });
        updates.length = 0;
    });
}
```

## 注意事项

1. **执行顺序**：微任务总是先于宏任务执行
2. **阻塞问题**：同步代码会阻塞事件循环
3. **无限循环**：避免在事件循环中创建无限循环
4. **性能影响**：过多的异步操作可能影响性能

## 常见错误

### 错误 1：误解执行顺序

```js
// 错误理解：认为 setTimeout 0 会立即执行
setTimeout(() => {
    console.log('1');
}, 0);
console.log('2');
// 实际输出：2, 1（不是 1, 2）
```

### 错误 2：在循环中使用异步

```js
// 错误：循环中的异步操作
for (let i = 0; i < 3; i++) {
    setTimeout(() => {
        console.log(i); // 输出 3, 3, 3
    }, 100);
}

// 正确：使用 let 或闭包
for (let i = 0; i < 3; i++) {
    setTimeout(() => {
        console.log(i); // 输出 0, 1, 2
    }, 100);
}
```

### 错误 3：阻塞事件循环

```js
// 错误：同步阻塞操作
while (true) {
    // 无限循环，阻塞事件循环
}

// 正确：使用异步操作
function asyncLoop() {
    // 执行一些操作
    setTimeout(() => {
        asyncLoop(); // 继续循环
    }, 0);
}
```

## 最佳实践

1. **避免长时间阻塞**：将耗时操作分解为多个小任务
2. **合理使用微任务**：微任务优先级高，适合需要立即执行的操作
3. **理解执行顺序**：掌握同步、微任务、宏任务的执行顺序
4. **使用 Promise**：Promise 提供更好的异步编程体验

## 练习

1. **执行顺序预测**：预测以下代码的输出顺序，并解释原因：

```js
console.log('1');
setTimeout(() => console.log('2'), 0);
Promise.resolve().then(() => console.log('3'));
console.log('4');
setTimeout(() => console.log('5'), 0);
Promise.resolve().then(() => console.log('6'));
```

2. **异步循环**：使用 setTimeout 实现一个异步循环，每秒输出一个数字（1 到 10）。

3. **批量处理**：实现一个函数，使用事件循环批量处理大量数据，避免阻塞主线程。

4. **优先级理解**：编写代码演示微任务和宏任务的执行顺序差异。

5. **事件循环可视化**：使用 console.log 和 setTimeout 创建一个简单的"事件循环可视化"示例，展示调用栈和任务队列的交互。

完成以上练习后，继续学习下一节，了解调用栈与任务队列的详细机制。

## 总结

事件循环是 JavaScript 异步编程的核心机制。理解单线程模型和事件循环的工作原理，是掌握异步编程的基础。通过合理使用异步操作，可以避免阻塞主线程，提升应用的响应性能。

## 相关资源

- [MDN：并发模型与事件循环](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/EventLoop)
- [Philip Roberts：JavaScript 事件循环的可视化](https://www.youtube.com/watch?v=8aGhZQkoFbQ)
