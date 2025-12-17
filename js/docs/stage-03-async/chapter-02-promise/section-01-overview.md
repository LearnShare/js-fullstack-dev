# 3.2.1 Promise 概述

## 概述

Promise 是 JavaScript 中处理异步操作的重要机制，它提供了一种更优雅的方式来处理异步代码。本节介绍 Promise 的概念、解决的问题以及为什么需要 Promise。

## 什么是 Promise

### 定义

Promise 是一个对象，表示一个异步操作的最终完成（或失败）及其结果值。

### 基本概念

Promise 有三种状态：

1. **pending**（等待中）：初始状态，既不是成功，也不是失败
2. **fulfilled**（已成功）：操作成功完成
3. **rejected**（已失败）：操作失败

### 状态转换

Promise 的状态转换是**单向的**：

```
pending → fulfilled（成功）
pending → rejected（失败）
```

一旦状态改变，就不会再变。

## 为什么需要 Promise

### 回调地狱问题

在 Promise 出现之前，使用回调函数处理异步操作会导致"回调地狱"：

```js
// 回调地狱示例
getData(function(a) {
    getMoreData(a, function(b) {
        getMoreData(b, function(c) {
            getMoreData(c, function(d) {
                // 代码嵌套过深，难以维护
            });
        });
    });
});
```

### Promise 的优势

Promise 提供了以下优势：

1. **链式调用**：避免回调嵌套
2. **错误处理**：统一的错误处理机制
3. **代码可读性**：代码更加清晰易读
4. **组合能力**：可以轻松组合多个异步操作

### Promise 解决回调地狱

```js
// 使用 Promise 链式调用
getData()
    .then(a => getMoreData(a))
    .then(b => getMoreData(b))
    .then(c => getMoreData(c))
    .then(d => {
        // 代码清晰，易于维护
    })
    .catch(error => {
        // 统一错误处理
    });
```

## Promise 的基本用法

### 创建 Promise

使用 `new Promise()` 构造函数创建 Promise：

```js
const promise = new Promise((resolve, reject) => {
    // 异步操作
    if (/* 操作成功 */) {
        resolve(value); // 成功时调用
    } else {
        reject(error); // 失败时调用
    }
});
```

### 使用 Promise

使用 `then()` 方法处理成功情况，使用 `catch()` 方法处理失败情况：

```js
promise
    .then(value => {
        // 处理成功情况
        console.log(value);
    })
    .catch(error => {
        // 处理失败情况
        console.error(error);
    });
```

### 完整示例

```js
// 创建一个简单的 Promise
const myPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
        const success = true;
        
        if (success) {
            resolve('操作成功');
        } else {
            reject('操作失败');
        }
    }, 1000);
});

// 使用 Promise
myPromise
    .then(result => {
        console.log(result); // "操作成功"
    })
    .catch(error => {
        console.error(error); // "操作失败"
    });
```

## Promise 的常见使用场景

### 网络请求

```js
// 使用 fetch API（返回 Promise）
fetch('https://api.example.com/data')
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error('请求失败:', error);
    });
```

### 文件读取

```js
// Node.js 文件读取（需要 promisify）
const fs = require('fs').promises;

fs.readFile('file.txt', 'utf8')
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error('读取失败:', error);
    });
```

### 定时操作

```js
// 使用 Promise 包装 setTimeout
function delay(ms) {
    return new Promise(resolve => {
        setTimeout(resolve, ms);
    });
}

delay(1000)
    .then(() => {
        console.log('1 秒后执行');
    });
```

## Promise vs 回调函数

### 回调函数方式

```js
// 使用回调函数
function fetchData(callback) {
    setTimeout(() => {
        callback('数据');
    }, 1000);
}

fetchData(data => {
    console.log(data);
});
```

### Promise 方式

```js
// 使用 Promise
function fetchData() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve('数据');
        }, 1000);
    });
}

fetchData()
    .then(data => {
        console.log(data);
    });
```

### 对比优势

| 特性           | 回调函数                 | Promise                       |
|:---------------|:-------------------------|:------------------------------|
| **可读性**     | 嵌套过深，难以阅读       | 链式调用，代码清晰            |
| **错误处理**   | 需要在每个回调中处理     | 统一的 catch 处理             |
| **组合能力**   | 难以组合多个异步操作     | 可以轻松组合（all、race 等）  |
| **控制流程**   | 难以控制执行流程         | 可以精确控制执行流程          |

## 注意事项

1. **状态不可变**：Promise 的状态一旦改变就不会再变
2. **立即执行**：Promise 构造函数中的函数会立即执行
3. **错误处理**：必须处理 Promise 的错误，否则会导致未捕获的异常
4. **返回值**：then 方法返回新的 Promise

## 常见错误

### 错误 1：忘记处理错误

```js
// 错误：没有处理 Promise 的错误
fetch('https://api.example.com/data')
    .then(response => response.json())
    .then(data => console.log(data));
// 如果请求失败，会导致未捕获的异常
```

### 错误 2：在 Promise 中抛出同步错误

```js
// 错误：在 Promise 构造函数中抛出同步错误
const promise = new Promise((resolve, reject) => {
    throw new Error('错误'); // 会被自动转换为 reject
});
```

### 错误 3：返回 undefined

```js
// 错误：then 中返回 undefined
promise
    .then(value => {
        // 没有返回值，下一个 then 接收 undefined
    })
    .then(result => {
        console.log(result); // undefined
    });
```

## 最佳实践

1. **始终处理错误**：使用 catch 处理 Promise 的错误
2. **使用链式调用**：利用 Promise 的链式调用特性
3. **避免嵌套**：不要嵌套 then 回调
4. **使用 async/await**：在支持的环境中，使用 async/await 更清晰

## 练习

1. **创建 Promise**：创建一个 Promise，模拟异步操作，1 秒后返回成功或失败。

2. **Promise 基础使用**：使用 Promise 处理一个简单的异步操作，包括成功和失败两种情况。

3. **对比回调**：将一个使用回调函数的异步操作改写为使用 Promise。

4. **错误处理**：编写代码演示 Promise 的错误处理机制。

5. **实际应用**：使用 Promise 处理一个实际的异步场景（如网络请求或文件读取）。

完成以上练习后，继续学习下一节，了解 Promise 的详细用法。

## 总结

Promise 是 JavaScript 异步编程的重要机制，它解决了回调地狱问题，提供了更好的代码可读性和错误处理能力。理解 Promise 的概念和使用方法，是掌握现代 JavaScript 异步编程的基础。

## 相关资源

- [MDN：Promise](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [JavaScript.info：Promise](https://zh.javascript.info/promise-basics)
