# 3.1.4 浏览器与 Node.js 的事件循环差异

## 概述

虽然 JavaScript 的事件循环机制在浏览器和 Node.js 中基本相同，但在实现细节上存在一些差异。理解这些差异有助于在不同环境中正确使用异步编程。本节介绍浏览器和 Node.js 事件循环的主要差异。

## 浏览器的事件循环

### 基本结构

浏览器的事件循环包含：

1. **调用栈**（Call Stack）
2. **微任务队列**（MicroTask Queue）
3. **宏任务队列**（MacroTask Queue）
4. **Web APIs**（定时器、DOM 事件、网络请求等）

### 浏览器的事件循环阶段

浏览器的事件循环主要阶段：

1. **执行同步代码**
2. **执行所有微任务**
3. **执行一个宏任务**
4. **UI 渲染**（如果需要）
5. **重复步骤 2-4**

### 浏览器中的宏任务

浏览器中的宏任务包括：

- `setTimeout`
- `setInterval`
- I/O 操作
- UI 渲染
- `postMessage`
- `MessageChannel`

### 浏览器中的微任务

浏览器中的微任务包括：

- `Promise.then()`
- `Promise.catch()`
- `Promise.finally()`
- `queueMicrotask()`
- `MutationObserver`

### 浏览器示例

```js
console.log('1');

setTimeout(() => {
    console.log('2');
}, 0);

Promise.resolve().then(() => {
    console.log('3');
});

console.log('4');

// 输出：1, 4, 3, 2
```

## Node.js 的事件循环

### 基本结构

Node.js 的事件循环包含：

1. **调用栈**（Call Stack）
2. **微任务队列**（MicroTask Queue）
3. **多个阶段**（Timers、Pending Callbacks、Idle/Prepare、Poll、Check、Close Callbacks）

### Node.js 的事件循环阶段

Node.js 的事件循环分为 6 个阶段：

1. **Timers**：执行 `setTimeout` 和 `setInterval` 的回调
2. **Pending Callbacks**：执行延迟到下一循环的 I/O 回调
3. **Idle/Prepare**：内部使用
4. **Poll**：获取新的 I/O 事件，执行相关回调
5. **Check**：执行 `setImmediate` 的回调
6. **Close Callbacks**：执行关闭回调（如 `socket.on('close')`）

### Node.js 中的宏任务

Node.js 中的宏任务包括：

- `setTimeout`
- `setInterval`
- `setImmediate`
- I/O 操作（文件、网络等）

### Node.js 中的微任务

Node.js 中的微任务包括：

- `Promise.then()`
- `Promise.catch()`
- `Promise.finally()`
- `queueMicrotask()`
- `process.nextTick()`（优先级最高，不是标准的微任务）

### process.nextTick

`process.nextTick` 是 Node.js 特有的，优先级高于所有其他任务：

```js
console.log('1');

setTimeout(() => {
    console.log('2');
}, 0);

Promise.resolve().then(() => {
    console.log('3');
});

process.nextTick(() => {
    console.log('4');
});

console.log('5');

// 输出：1, 5, 4, 3, 2
// process.nextTick 优先级最高
```

### Node.js 示例

```js
console.log('开始');

setTimeout(() => {
    console.log('setTimeout');
}, 0);

setImmediate(() => {
    console.log('setImmediate');
});

Promise.resolve().then(() => {
    console.log('Promise');
});

process.nextTick(() => {
    console.log('nextTick');
});

console.log('结束');

// 输出：
// 开始
// 结束
// nextTick
// Promise
// setTimeout 或 setImmediate（顺序不确定）
```

## 主要差异对比

### 执行顺序差异

| 特性           | 浏览器                           | Node.js                                    |
|:---------------|:---------------------------------|:-------------------------------------------|
| **微任务**     | Promise.then、queueMicrotask     | Promise.then、queueMicrotask、process.nextTick |
| **宏任务**     | setTimeout、setInterval、I/O     | setTimeout、setInterval、setImmediate、I/O |
| **优先级**     | 微任务 > 宏任务                  | process.nextTick > 微任务 > 宏任务         |
| **阶段**       | 简单循环                         | 6 个阶段                                   |

### setImmediate vs setTimeout

在 Node.js 中，`setImmediate` 和 `setTimeout` 的执行顺序可能不同：

```js
// Node.js 环境
setTimeout(() => {
    console.log('setTimeout');
}, 0);

setImmediate(() => {
    console.log('setImmediate');
});

// 输出顺序不确定，取决于 I/O 循环的状态
```

### process.nextTick 的特殊性

`process.nextTick` 不是标准的微任务，但行为类似，优先级更高：

```js
Promise.resolve().then(() => {
    console.log('Promise 1');
    
    process.nextTick(() => {
        console.log('nextTick 1');
    });
});

process.nextTick(() => {
    console.log('nextTick 2');
    
    Promise.resolve().then(() => {
        console.log('Promise 2');
    });
});

// 输出：
// nextTick 2
// Promise 1
// nextTick 1
// Promise 2
```

## 实际应用场景

### 浏览器环境

```js
// 浏览器：使用 requestAnimationFrame 优化渲染
function animate() {
    // 动画逻辑
    requestAnimationFrame(animate);
}

// 浏览器：使用 MutationObserver 监听 DOM 变化
const observer = new MutationObserver(() => {
    console.log('DOM 变化');
});

observer.observe(document.body, {
    childList: true
});
```

### Node.js 环境

```js
// Node.js：使用 setImmediate 在 I/O 之后执行
fs.readFile('file.txt', (err, data) => {
    setImmediate(() => {
        console.log('在 I/O 之后执行');
    });
});

// Node.js：使用 process.nextTick 确保异步执行
function asyncOperation(callback) {
    process.nextTick(callback);
}
```

## 注意事项

1. **环境差异**：注意浏览器和 Node.js 的事件循环差异
2. **process.nextTick**：Node.js 特有，优先级最高
3. **setImmediate**：Node.js 特有，在 Check 阶段执行
4. **执行顺序**：不同环境下的执行顺序可能不同

## 常见错误

### 错误 1：假设执行顺序相同

```js
// 错误：假设浏览器和 Node.js 执行顺序相同
setTimeout(() => console.log('1'), 0);
setImmediate(() => console.log('2')); // 浏览器中没有 setImmediate
```

### 错误 2：滥用 process.nextTick

```js
// 错误：process.nextTick 可能导致无限递归
function recursive() {
    process.nextTick(recursive);
}
```

### 错误 3：在浏览器中使用 Node.js API

```js
// 错误：在浏览器中使用 Node.js API
process.nextTick(() => {
    console.log('这在浏览器中不存在');
});
```

## 最佳实践

1. **环境检测**：使用环境检测确保代码在不同环境中正确运行
2. **避免依赖顺序**：不要依赖 setTimeout 和 setImmediate 的执行顺序
3. **合理使用 nextTick**：避免滥用 process.nextTick
4. **使用标准 API**：优先使用标准的 Promise 和 queueMicrotask

## 练习

1. **环境差异**：编写代码演示浏览器和 Node.js 事件循环的差异。

2. **执行顺序**：在 Node.js 中测试 setTimeout 和 setImmediate 的执行顺序。

3. **process.nextTick**：编写代码演示 process.nextTick 的优先级。

4. **跨环境代码**：编写可以在浏览器和 Node.js 中都能运行的异步代码。

5. **性能对比**：对比不同环境下的异步操作性能。

完成以上练习后，继续学习下一章，了解 Promise 的使用。

## 总结

浏览器和 Node.js 的事件循环在基本机制上相同，但在实现细节上存在差异。Node.js 有 process.nextTick 和 setImmediate 等特有特性，浏览器有 MutationObserver 和 requestAnimationFrame 等特性。理解这些差异有助于在不同环境中正确使用异步编程。

## 相关资源

- [Node.js 官方文档：事件循环](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/)
- [MDN：并发模型与事件循环](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/EventLoop)
