# 3.2.2 Promise 基础

## 概述

本节详细介绍 Promise 的创建、状态转换和基本方法的使用，包括 Promise 构造函数、then、catch、finally 等方法。

## 创建 Promise

### 使用构造函数

**语法格式**：`new Promise(executor)`

**参数说明**：

| 参数名      | 类型     | 说明                           | 是否必需 | 默认值 |
|:------------|:---------|:-------------------------------|:---------|:-------|
| `executor`  | function | 执行函数，接收 resolve 和 reject | 是       | -      |

**executor 函数参数**：

| 参数名      | 类型     | 说明                 |
|:------------|:---------|:---------------------|
| `resolve`   | function | 成功时调用，传入结果值 |
| `reject`    | function | 失败时调用，传入错误信息 |

**返回值**：一个新的 Promise 对象

### 基本创建

```js
const promise = new Promise((resolve, reject) => {
    // 异步操作
    setTimeout(() => {
        const success = true;
        
        if (success) {
            resolve('操作成功');
        } else {
            reject('操作失败');
        }
    }, 1000);
});
```

### 立即解析的 Promise

```js
// 立即成功
const resolved = Promise.resolve('成功');

// 立即失败
const rejected = Promise.reject('失败');
```

### Promise.resolve()

**语法格式**：`Promise.resolve(value)`

**参数说明**：

| 参数名   | 类型 | 说明                     | 是否必需 | 默认值 |
|:---------|:-----|:-------------------------|:---------|:-------|
| `value`  | any  | 要解析的值（可以是 Promise） | 是       | -      |

**返回值**：一个已解析的 Promise 对象

```js
// 解析普通值
const p1 = Promise.resolve(42);
p1.then(value => console.log(value)); // 42

// 解析 Promise（保持不变）
const p2 = Promise.resolve(Promise.resolve('hello'));
p2.then(value => console.log(value)); // "hello"
```

### Promise.reject()

**语法格式**：`Promise.reject(reason)`

**参数说明**：

| 参数名   | 类型 | 说明           | 是否必需 | 默认值 |
|:---------|:-----|:---------------|:---------|:-------|
| `reason` | any  | 拒绝的原因     | 是       | -      |

**返回值**：一个已拒绝的 Promise 对象

```js
const p = Promise.reject('错误');
p.catch(error => console.error(error)); // "错误"
```

## Promise 的状态

### 三种状态

Promise 有三种状态：

1. **pending**（等待中）：初始状态
2. **fulfilled**（已成功）：操作成功完成
3. **rejected**（已失败）：操作失败

### 状态转换

状态转换是**单向的**，一旦改变就不会再变：

```
pending → fulfilled（成功）
pending → rejected（失败）
```

### 状态检查

```js
const promise = new Promise((resolve) => {
    setTimeout(() => resolve('完成'), 1000);
});

// Promise 创建时是 pending 状态
console.log(promise); // Promise { <pending> }

promise.then(() => {
    // 此时 Promise 是 fulfilled 状态
    console.log('已完成');
});
```

## then() 方法

### 基本语法

**语法格式**：`promise.then(onFulfilled[, onRejected])`

**参数说明**：

| 参数名         | 类型     | 说明                           | 是否必需 | 默认值 |
|:---------------|:---------|:-------------------------------|:---------|:-------|
| `onFulfilled`  | function | 成功时的回调函数               | 否       | -      |
| `onRejected`   | function | 失败时的回调函数               | 否       | -      |

**返回值**：一个新的 Promise 对象

### 基本使用

```js
const promise = Promise.resolve('成功');

promise.then(
    value => {
        console.log(value); // "成功"
    },
    error => {
        console.error(error); // 不会执行
    }
);
```

### 只处理成功情况

```js
promise.then(value => {
    console.log(value);
});
```

### 链式调用

```js
Promise.resolve(1)
    .then(value => value + 1)      // 2
    .then(value => value * 2)      // 4
    .then(value => console.log(value)); // 4
```

## catch() 方法

### 基本语法

**语法格式**：`promise.catch(onRejected)`

**参数说明**：

| 参数名        | 类型     | 说明           | 是否必需 | 默认值 |
|:--------------|:---------|:---------------|:---------|:-------|
| `onRejected`  | function | 失败时的回调函数 | 是       | -      |

**返回值**：一个新的 Promise 对象

### 基本使用

```js
const promise = Promise.reject('错误');

promise.catch(error => {
    console.error(error); // "错误"
});
```

### 错误处理

```js
Promise.resolve(1)
    .then(value => {
        throw new Error('错误');
    })
    .catch(error => {
        console.error(error.message); // "错误"
    });
```

### 捕获链式调用中的错误

```js
Promise.resolve(1)
    .then(value => value + 1)
    .then(value => {
        throw new Error('错误');
    })
    .then(value => {
        // 不会执行
    })
    .catch(error => {
        console.error(error); // 捕获上面的错误
    });
```

## finally() 方法

### 基本语法

**语法格式**：`promise.finally(onFinally)`

**参数说明**：

| 参数名       | 类型     | 说明                           | 是否必需 | 默认值 |
|:-------------|:---------|:-------------------------------|:---------|:-------|
| `onFinally`  | function | 无论成功或失败都会执行的函数   | 是       | -      |

**返回值**：一个新的 Promise 对象

### 基本使用

```js
Promise.resolve('成功')
    .then(value => console.log(value))
    .finally(() => {
        console.log('总是执行');
    });

// 输出：
// "成功"
// "总是执行"
```

### 清理资源

```js
let isLoading = true;

fetchData()
    .then(data => {
        // 处理数据
    })
    .catch(error => {
        // 处理错误
    })
    .finally(() => {
        isLoading = false; // 清理状态
    });
```

## Promise 的特性

### 立即执行

Promise 构造函数中的函数会**立即执行**：

```js
console.log('1');

const promise = new Promise((resolve) => {
    console.log('2'); // 立即执行
    resolve('3');
});

console.log('4');

// 输出：1, 2, 4, 3
```

### 状态不可变

Promise 的状态一旦改变就不会再变：

```js
const promise = new Promise((resolve, reject) => {
    resolve('成功');
    reject('失败'); // 无效，状态已经是 fulfilled
});

promise.then(value => console.log(value)); // "成功"
```

### then 方法返回新 Promise

每次调用 `then` 都返回一个新的 Promise：

```js
const p1 = Promise.resolve(1);
const p2 = p1.then(value => value + 1);

console.log(p1 === p2); // false（是不同的 Promise）
```

## 注意事项

1. **状态不可变**：Promise 的状态一旦改变就不会再变
2. **立即执行**：Promise 构造函数中的函数会立即执行
3. **返回值**：then、catch、finally 都返回新的 Promise
4. **错误处理**：必须处理 Promise 的错误，否则会导致未捕获的异常

## 常见错误

### 错误 1：忘记处理错误

```js
// 错误：没有处理 Promise 的错误
Promise.reject('错误');
// 会导致未捕获的异常：Uncaught (in promise) 错误
```

### 错误 2：在 Promise 中抛出同步错误

```js
// 错误：在 Promise 构造函数中抛出同步错误
const promise = new Promise((resolve, reject) => {
    throw new Error('错误'); // 会被自动转换为 reject
});

promise.catch(error => console.error(error)); // 需要捕获
```

### 错误 3：在 then 中抛出错误

```js
// 错误：在 then 中抛出错误，但没有 catch
Promise.resolve(1)
    .then(value => {
        throw new Error('错误');
    }); // 未捕获的错误

// 正确：使用 catch 处理
Promise.resolve(1)
    .then(value => {
        throw new Error('错误');
    })
    .catch(error => console.error(error));
```

## 最佳实践

1. **始终处理错误**：使用 catch 处理 Promise 的错误
2. **使用 finally**：使用 finally 进行清理操作
3. **链式调用**：利用 Promise 的链式调用特性
4. **避免嵌套**：不要嵌套 then 回调

## 练习

1. **创建 Promise**：创建一个 Promise，模拟异步操作，1 秒后随机返回成功或失败。

2. **使用 then 和 catch**：创建一个 Promise，使用 then 处理成功情况，使用 catch 处理失败情况。

3. **链式调用**：创建一个 Promise 链，依次执行多个异步操作。

4. **错误处理**：编写代码演示 Promise 的错误处理机制，包括 catch 的使用。

5. **finally 使用**：编写代码演示 finally 方法的使用，包括清理资源的场景。

完成以上练习后，继续学习下一节，了解 Promise 链式调用的详细机制。

## 总结

Promise 提供了创建、状态管理和错误处理的能力。理解 Promise 的三种状态和基本方法的使用，是掌握 Promise 的基础。通过 then、catch 和 finally 方法，可以优雅地处理异步操作的结果和错误。

## 相关资源

- [MDN：Promise](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [JavaScript.info：Promise](https://zh.javascript.info/promise-basics)
