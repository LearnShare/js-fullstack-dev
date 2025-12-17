# 3.1.2 调用栈与任务队列

## 概述

调用栈（Call Stack）和任务队列（Task Queue）是事件循环的核心组件。理解它们的工作原理对于掌握 JavaScript 异步编程至关重要。本节详细介绍调用栈和任务队列的概念、工作原理和交互方式。

## 调用栈（Call Stack）

### 什么是调用栈

调用栈是一种数据结构，用于跟踪函数调用的执行顺序。它遵循**后进先出**（LIFO，Last In First Out）的原则。

### 调用栈的工作原理

当函数被调用时：

1. 函数被推入（push）调用栈
2. 函数执行完毕，从调用栈弹出（pop）
3. 返回调用该函数的位置继续执行

```js
function first() {
    console.log('first 开始');
    second();
    console.log('first 结束');
}

function second() {
    console.log('second 开始');
    third();
    console.log('second 结束');
}

function third() {
    console.log('third');
}

first();

// 输出顺序：
// first 开始
// second 开始
// third
// second 结束
// first 结束
```

### 调用栈的可视化

执行 `first()` 时的调用栈变化：

```
调用栈状态变化：
[]                    ← 初始状态
[first]               ← first() 被调用
[first, second]       ← second() 被调用
[first, second, third] ← third() 被调用
[first, second]       ← third() 执行完毕
[first]               ← second() 执行完毕
[]                    ← first() 执行完毕
```

### 调用栈的深度限制

JavaScript 调用栈有深度限制，超过限制会导致**栈溢出**（Stack Overflow）：

```js
// 递归函数导致栈溢出
function recursive() {
    recursive(); // 无限递归
}

recursive(); // RangeError: Maximum call stack size exceeded
```

### 使用调试工具查看调用栈

```js
function a() {
    b();
}

function b() {
    c();
}

function c() {
    console.trace(); // 打印调用栈
}

a();

// 输出调用栈：
// Trace: 
//   at c (file.js:8:9)
//   at b (file.js:4:9)
//   at a (file.js:1:9)
```

## 任务队列（Task Queue）

### 什么是任务队列

任务队列是存储待执行任务的数据结构。当异步操作完成时，其回调函数会被放入任务队列中等待执行。

### 任务队列的类型

JavaScript 中有两种主要的任务队列：

1. **宏任务队列**（MacroTask Queue）：存储宏任务
2. **微任务队列**（MicroTask Queue）：存储微任务

### 宏任务队列

宏任务包括：

- `setTimeout`
- `setInterval`
- I/O 操作
- UI 渲染
- `setImmediate`（Node.js）

```js
console.log('1');

setTimeout(() => {
    console.log('2'); // 宏任务
}, 0);

console.log('3');

// 输出：1, 3, 2
```

### 微任务队列

微任务包括：

- `Promise.then()`
- `Promise.catch()`
- `Promise.finally()`
- `queueMicrotask()`
- `MutationObserver`（浏览器）

```js
console.log('1');

Promise.resolve().then(() => {
    console.log('2'); // 微任务
});

console.log('3');

// 输出：1, 3, 2
```

## 调用栈与任务队列的交互

### 基本交互流程

事件循环的基本流程：

1. 执行调用栈中的所有同步代码
2. 调用栈为空时，检查微任务队列
3. 执行所有微任务（直到微任务队列为空）
4. 执行一个宏任务
5. 重复步骤 2-4

```js
console.log('1'); // 同步代码

setTimeout(() => {
    console.log('2'); // 宏任务
}, 0);

Promise.resolve().then(() => {
    console.log('3'); // 微任务
});

console.log('4'); // 同步代码

// 执行流程：
// 1. 执行同步代码：输出 1, 4
// 2. 调用栈为空，执行微任务：输出 3
// 3. 执行宏任务：输出 2
// 最终输出：1, 4, 3, 2
```

### 复杂的执行顺序示例

```js
console.log('1'); // 同步

setTimeout(() => {
    console.log('2'); // 宏任务 1
    
    Promise.resolve().then(() => {
        console.log('3'); // 微任务 2
    });
}, 0);

Promise.resolve().then(() => {
    console.log('4'); // 微任务 1
    
    setTimeout(() => {
        console.log('5'); // 宏任务 2
    }, 0);
});

console.log('6'); // 同步

// 执行流程分析：
// 1. 同步代码：输出 1, 6
// 2. 微任务队列：[微任务1]
// 3. 执行微任务1：输出 4，同时添加宏任务2到队列
// 4. 宏任务队列：[宏任务1, 宏任务2]
// 5. 执行宏任务1：输出 2，同时添加微任务2到队列
// 6. 微任务队列：[微任务2]，执行微任务2：输出 3
// 7. 执行宏任务2：输出 5
// 最终输出：1, 6, 4, 2, 3, 5
```

## 任务队列的处理机制

### 微任务队列的特性

微任务队列的特点：

1. **优先级高**：微任务总是先于宏任务执行
2. **全部执行**：一次事件循环中会执行**所有**微任务
3. **可以嵌套**：微任务中可以产生新的微任务

```js
Promise.resolve().then(() => {
    console.log('微任务 1');
    
    Promise.resolve().then(() => {
        console.log('微任务 2');
        
        Promise.resolve().then(() => {
            console.log('微任务 3');
        });
    });
});

setTimeout(() => {
    console.log('宏任务');
}, 0);

// 输出：微任务 1, 微任务 2, 微任务 3, 宏任务
// 说明：所有微任务都会在一次循环中执行完
```

### 宏任务队列的特性

宏任务队列的特点：

1. **优先级低**：在微任务之后执行
2. **逐个执行**：一次事件循环中只执行**一个**宏任务
3. **可以嵌套**：宏任务中可以产生新的宏任务和微任务

```js
setTimeout(() => {
    console.log('宏任务 1');
    
    Promise.resolve().then(() => {
        console.log('微任务 1');
    });
    
    setTimeout(() => {
        console.log('宏任务 2');
    }, 0);
}, 0);

Promise.resolve().then(() => {
    console.log('微任务 0');
});

// 输出：微任务 0, 宏任务 1, 微任务 1, 宏任务 2
```

## queueMicrotask 的使用

### 基本用法

`queueMicrotask()` 用于将回调函数添加到微任务队列：

```js
console.log('1');

queueMicrotask(() => {
    console.log('2'); // 微任务
});

console.log('3');

// 输出：1, 3, 2
```

### 与 Promise.then 的对比

```js
// 使用 Promise.then
Promise.resolve().then(() => {
    console.log('Promise 微任务');
});

// 使用 queueMicrotask
queueMicrotask(() => {
    console.log('queueMicrotask 微任务');
});

// 两者执行顺序相同，都是微任务
```

### 使用场景

`queueMicrotask` 适用于需要在当前任务完成后、但在渲染之前执行的操作：

```js
// 批量更新 DOM，避免频繁重排
const updates = [];

function scheduleUpdate(element, value) {
    updates.push({ element, value });
    
    queueMicrotask(() => {
        updates.forEach(({ element, value }) => {
            element.textContent = value;
        });
        updates.length = 0;
    });
}
```

## 注意事项

1. **执行顺序**：同步代码 → 微任务 → 宏任务
2. **微任务优先级**：微任务总是先于宏任务执行
3. **全部执行**：一次循环中会执行所有微任务，但只执行一个宏任务
4. **栈溢出**：注意递归深度，避免栈溢出

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

### 错误 2：微任务嵌套导致阻塞

```js
// 错误：无限嵌套微任务会导致阻塞
function infiniteMicrotask() {
    Promise.resolve().then(() => {
        infiniteMicrotask(); // 无限递归
    });
}
infiniteMicrotask(); // 阻塞事件循环
```

### 错误 3：在微任务中创建大量微任务

```js
// 注意：虽然不会阻塞，但可能影响性能
for (let i = 0; i < 10000; i++) {
    Promise.resolve().then(() => {
        // 处理逻辑
    });
}
```

## 最佳实践

1. **理解执行顺序**：掌握同步、微任务、宏任务的执行顺序
2. **合理使用微任务**：微任务适合需要立即执行的操作
3. **避免阻塞**：避免在同步代码中执行耗时操作
4. **使用调试工具**：使用 `console.trace()` 查看调用栈

## 练习

1. **调用栈分析**：分析以下代码的调用栈变化过程：

```js
function a() {
    b();
}

function b() {
    c();
}

function c() {
    console.log('c');
}

a();
```

2. **执行顺序预测**：预测以下代码的输出顺序：

```js
console.log('1');
setTimeout(() => console.log('2'), 0);
queueMicrotask(() => console.log('3'));
Promise.resolve().then(() => console.log('4'));
console.log('5');
```

3. **微任务嵌套**：编写代码演示微任务嵌套的执行顺序。

4. **宏任务与微任务**：编写代码演示宏任务和微任务的交互。

5. **调用栈可视化**：使用 `console.trace()` 创建一个函数调用链，并分析调用栈的变化。

完成以上练习后，继续学习下一节，了解宏任务与微任务的详细机制。

## 总结

调用栈和任务队列是事件循环的核心组件。调用栈管理函数调用的执行顺序，任务队列存储待执行的异步任务。理解它们的交互机制，是掌握 JavaScript 异步编程的关键。

## 相关资源

- [MDN：并发模型与事件循环](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/EventLoop)
- [Jake Archibald：Tasks, microtasks, queues and schedules](https://jakearchibald.com/2015/tasks-microtasks-queues-and-schedules/)
