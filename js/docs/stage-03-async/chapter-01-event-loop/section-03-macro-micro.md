# 3.1.3 宏任务与微任务

## 概述

宏任务（MacroTask）和微任务（MicroTask）是事件循环中两种不同类型的任务队列。理解它们的区别和执行顺序对于正确使用异步编程至关重要。本节详细介绍宏任务和微任务的概念、区别和应用场景。

## 宏任务（MacroTask）

### 什么是宏任务

宏任务是由浏览器或 Node.js 环境提供的异步操作，会被添加到宏任务队列中等待执行。

### 宏任务的类型

常见的宏任务包括：

- `setTimeout`
- `setInterval`
- `setImmediate`（Node.js）
- I/O 操作（文件读取、网络请求等）
- UI 渲染（浏览器）
- `MessageChannel`

### setTimeout 示例

```js
console.log('1');

setTimeout(() => {
    console.log('2'); // 宏任务
}, 0);

console.log('3');

// 输出：1, 3, 2
```

### setInterval 示例

```js
let count = 0;
const timer = setInterval(() => {
    count++;
    console.log(`第 ${count} 次执行`);
    
    if (count >= 5) {
        clearInterval(timer);
    }
}, 1000);
```

### I/O 操作示例

```js
// Node.js 文件读取
const fs = require('fs');

console.log('开始读取文件');

fs.readFile('file.txt', 'utf8', (err, data) => {
    console.log('文件读取完成'); // 宏任务
    console.log(data);
});

console.log('继续执行其他代码');
```

## 微任务（MicroTask）

### 什么是微任务

微任务是优先级更高的异步操作，会在当前宏任务执行完毕后、下一个宏任务执行之前执行。

### 微任务的类型

常见的微任务包括：

- `Promise.then()`
- `Promise.catch()`
- `Promise.finally()`
- `queueMicrotask()`
- `MutationObserver`（浏览器）
- `process.nextTick`（Node.js，优先级最高）

### Promise.then 示例

```js
console.log('1');

Promise.resolve().then(() => {
    console.log('2'); // 微任务
});

console.log('3');

// 输出：1, 3, 2
```

### queueMicrotask 示例

```js
console.log('1');

queueMicrotask(() => {
    console.log('2'); // 微任务
});

console.log('3');

// 输出：1, 3, 2
```

### MutationObserver 示例

```js
// 浏览器环境
const observer = new MutationObserver(() => {
    console.log('DOM 变化'); // 微任务
});

observer.observe(document.body, {
    childList: true,
    subtree: true
});
```

## 宏任务与微任务的区别

### 执行顺序

**关键规则**：微任务总是先于宏任务执行

```js
console.log('1'); // 同步

setTimeout(() => {
    console.log('2'); // 宏任务
}, 0);

Promise.resolve().then(() => {
    console.log('3'); // 微任务
});

console.log('4'); // 同步

// 输出：1, 4, 3, 2
// 说明：微任务（3）先于宏任务（2）执行
```

### 执行数量

- **微任务**：一次事件循环中执行**所有**微任务
- **宏任务**：一次事件循环中只执行**一个**宏任务

```js
// 微任务：全部执行
Promise.resolve().then(() => console.log('微任务 1'));
Promise.resolve().then(() => console.log('微任务 2'));
Promise.resolve().then(() => console.log('微任务 3'));

setTimeout(() => console.log('宏任务 1'), 0);
setTimeout(() => console.log('宏任务 2'), 0);

// 输出：
// 微任务 1
// 微任务 2
// 微任务 3
// 宏任务 1
// 宏任务 2
```

### 嵌套执行

微任务中可以产生新的微任务，宏任务中也可以产生新的宏任务和微任务：

```js
// 微任务嵌套
Promise.resolve().then(() => {
    console.log('微任务 1');
    
    Promise.resolve().then(() => {
        console.log('微任务 2'); // 会在同一次循环中执行
    });
});

setTimeout(() => {
    console.log('宏任务 1');
}, 0);

// 输出：微任务 1, 微任务 2, 宏任务 1
```

## 执行顺序详解

### 完整的事件循环流程

```js
console.log('1'); // 同步代码

setTimeout(() => {
    console.log('2'); // 宏任务
}, 0);

Promise.resolve().then(() => {
    console.log('3'); // 微任务
});

setTimeout(() => {
    console.log('4'); // 宏任务
}, 0);

Promise.resolve().then(() => {
    console.log('5'); // 微任务
});

console.log('6'); // 同步代码

// 执行流程：
// 1. 执行同步代码：输出 1, 6
// 2. 调用栈为空，检查微任务队列：[微任务1, 微任务2]
// 3. 执行所有微任务：输出 3, 5
// 4. 执行第一个宏任务：输出 2
// 5. 执行第二个宏任务：输出 4
// 最终输出：1, 6, 3, 5, 2, 4
```

### 复杂场景示例

```js
console.log('开始');

setTimeout(() => {
    console.log('setTimeout 1');
    
    Promise.resolve().then(() => {
        console.log('Promise 1');
    });
}, 0);

Promise.resolve().then(() => {
    console.log('Promise 2');
    
    setTimeout(() => {
        console.log('setTimeout 2');
    }, 0);
});

setTimeout(() => {
    console.log('setTimeout 3');
}, 0);

console.log('结束');

// 执行流程：
// 1. 同步代码：输出 "开始", "结束"
// 2. 微任务队列：[Promise 2]
// 3. 宏任务队列：[setTimeout 1, setTimeout 3]
// 4. 执行微任务 Promise 2：输出 "Promise 2"，添加 setTimeout 2 到宏任务队列
// 5. 宏任务队列：[setTimeout 1, setTimeout 3, setTimeout 2]
// 6. 执行宏任务 setTimeout 1：输出 "setTimeout 1"，添加 Promise 1 到微任务队列
// 7. 微任务队列：[Promise 1]，执行微任务 Promise 1：输出 "Promise 1"
// 8. 执行宏任务 setTimeout 3：输出 "setTimeout 3"
// 9. 执行宏任务 setTimeout 2：输出 "setTimeout 2"
// 最终输出：开始, 结束, Promise 2, setTimeout 1, Promise 1, setTimeout 3, setTimeout 2
```

## 应用场景

### 使用微任务进行批量更新

```js
// 批量更新 DOM，避免频繁重排
const updates = [];

function scheduleUpdate(element, value) {
    updates.push({ element, value });
    
    // 使用微任务批量更新
    queueMicrotask(() => {
        updates.forEach(({ element, value }) => {
            element.textContent = value;
        });
        updates.length = 0;
    });
}

// 多次调用，但只触发一次 DOM 更新
scheduleUpdate(element1, 'value1');
scheduleUpdate(element2, 'value2');
scheduleUpdate(element3, 'value3');
```

### 使用宏任务分解耗时操作

```js
// 使用 setTimeout 分解耗时操作
function processLargeArray(array, callback) {
    const chunk = array.splice(0, 1000);
    
    chunk.forEach(item => {
        // 处理逻辑
    });
    
    if (array.length > 0) {
        setTimeout(() => {
            processLargeArray(array, callback);
        }, 0);
    } else {
        callback();
    }
}
```

### Promise 链中的微任务

```js
Promise.resolve()
    .then(() => {
        console.log('1'); // 微任务 1
        return Promise.resolve();
    })
    .then(() => {
        console.log('2'); // 微任务 2
    });

setTimeout(() => {
    console.log('3'); // 宏任务
}, 0);

// 输出：1, 2, 3
```

## 注意事项

1. **执行顺序**：微任务总是先于宏任务执行
2. **执行数量**：一次循环执行所有微任务，但只执行一个宏任务
3. **嵌套任务**：微任务中可以产生新的微任务，会在同一次循环中执行
4. **性能考虑**：过多的微任务可能阻塞事件循环

## 常见错误

### 错误 1：误解执行顺序

```js
// 错误理解：认为 setTimeout 0 会立即执行
setTimeout(() => {
    console.log('1');
}, 0);
Promise.resolve().then(() => {
    console.log('2');
});
// 实际输出：2, 1（不是 1, 2）
```

### 错误 2：微任务无限嵌套

```js
// 错误：无限嵌套微任务会导致阻塞
function infiniteMicrotask() {
    Promise.resolve().then(() => {
        infiniteMicrotask();
    });
}
```

### 错误 3：在微任务中执行耗时操作

```js
// 注意：微任务中执行耗时操作会阻塞事件循环
Promise.resolve().then(() => {
    // 耗时操作
    for (let i = 0; i < 1000000000; i++) {
        // 计算
    }
});
```

## 最佳实践

1. **理解执行顺序**：掌握微任务和宏任务的执行顺序
2. **合理使用微任务**：微任务适合需要立即执行的操作
3. **避免阻塞**：避免在微任务中执行耗时操作
4. **使用 Promise**：Promise 提供更好的异步编程体验

## 练习

1. **执行顺序预测**：预测以下代码的输出顺序：

```js
console.log('1');
setTimeout(() => console.log('2'), 0);
Promise.resolve().then(() => console.log('3'));
queueMicrotask(() => console.log('4'));
setTimeout(() => console.log('5'), 0);
Promise.resolve().then(() => console.log('6'));
console.log('7');
```

2. **嵌套任务**：编写代码演示微任务和宏任务的嵌套执行顺序。

3. **批量更新**：使用微任务实现一个批量更新 DOM 的函数。

4. **任务优先级**：编写代码演示不同优先级任务的执行顺序。

5. **实际应用**：实现一个使用微任务和宏任务协作的数据处理函数。

完成以上练习后，继续学习下一节，了解浏览器与 Node.js 的事件循环差异。

## 总结

宏任务和微任务是事件循环中的两种任务类型。微任务优先级更高，会在当前宏任务执行完毕后、下一个宏任务执行之前执行。理解它们的区别和执行顺序，是掌握 JavaScript 异步编程的关键。

## 相关资源

- [Jake Archibald：Tasks, microtasks, queues and schedules](https://jakearchibald.com/2015/tasks-microtasks-queues-and-schedules/)
- [MDN：并发模型与事件循环](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/EventLoop)
