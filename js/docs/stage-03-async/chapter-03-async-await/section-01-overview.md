# 3.3.1 async/await 概述

## 概述

async/await 是 ES2017 引入的异步编程语法，它基于 Promise，提供了一种更简洁、更易读的异步代码编写方式。本节介绍 async/await 的概念、优势和基本用法。

## 什么是 async/await

### 定义

- **async**：用于声明异步函数，函数会自动返回 Promise
- **await**：用于等待 Promise 完成，只能在 async 函数中使用

### 基本概念

async/await 是 Promise 的**语法糖**，使异步代码看起来更像同步代码：

```js
// 使用 Promise
function fetchData() {
    return fetch('/api/data')
        .then(response => response.json())
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.error(error);
        });
}

// 使用 async/await（更清晰）
async function fetchData() {
    try {
        const response = await fetch('/api/data');
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error(error);
    }
}
```

## 为什么需要 async/await

### Promise 链式调用的问题

虽然 Promise 解决了回调地狱问题，但在复杂场景下，链式调用仍然可能变得复杂：

```js
// Promise 链式调用
fetchUser(userId)
    .then(user => {
        return fetchUserPosts(user.id);
    })
    .then(posts => {
        return fetchUserComments(user.id); // user 不在作用域内
    })
    .then(comments => {
        // 需要处理多个异步结果
    })
    .catch(error => {
        console.error(error);
    });
```

### async/await 的优势

async/await 提供了以下优势：

1. **代码更清晰**：异步代码看起来像同步代码
2. **变量作用域**：可以在同一作用域内使用变量
3. **错误处理**：使用 try/catch 处理错误更自然
4. **调试友好**：更容易设置断点和调试

### 使用 async/await 简化

```js
// 使用 async/await
async function loadUserData(userId) {
    try {
        const user = await fetchUser(userId);
        const posts = await fetchUserPosts(user.id);
        const comments = await fetchUserComments(user.id);
        
        // 所有变量都在同一作用域内
        return { user, posts, comments };
    } catch (error) {
        console.error(error);
        throw error;
    }
}
```

## 基本用法

### async 函数声明

```js
async function myFunction() {
    // 函数体
}
```

### async 函数表达式

```js
const myFunction = async function() {
    // 函数体
};
```

### async 箭头函数

```js
const myFunction = async () => {
    // 函数体
};
```

### 使用 await

在 async 函数中使用 `await` 等待 Promise 完成：

```js
async function fetchData() {
    const response = await fetch('/api/data');
    const data = await response.json();
    return data;
}
```

### 完整示例

```js
async function getUserInfo(userId) {
    try {
        // 等待用户数据
        const user = await fetch(`/api/users/${userId}`).then(r => r.json());
        
        // 等待用户文章
        const posts = await fetch(`/api/users/${userId}/posts`).then(r => r.json());
        
        // 返回结果
        return { user, posts };
    } catch (error) {
        console.error('获取用户信息失败:', error);
        throw error;
    }
}

// 使用
getUserInfo(123)
    .then(info => {
        console.log(info);
    })
    .catch(error => {
        console.error(error);
    });
```

## async/await vs Promise

### 代码对比

| 特性           | Promise                | async/await                  |
|:---------------|:-----------------------|:-----------------------------|
| **代码风格**   | 链式调用               | 同步风格                     |
| **变量作用域** | 每个 then 独立作用域   | 同一作用域                   |
| **错误处理**   | catch 方法             | try/catch                    |
| **调试**       | 断点设置较困难         | 更容易设置断点               |
| **可读性**     | 复杂场景下较难阅读     | 代码更清晰易读               |

### 实际对比示例

```js
// 使用 Promise
function processData(id) {
    return fetchData(id)
        .then(data => {
            return validateData(data);
        })
        .then(validData => {
            return transformData(validData);
        })
        .then(transformed => {
            return saveData(transformed);
        })
        .catch(error => {
            console.error(error);
            throw error;
        });
}

// 使用 async/await（更清晰）
async function processData(id) {
    try {
        const data = await fetchData(id);
        const validData = await validateData(data);
        const transformed = await transformData(validData);
        return await saveData(transformed);
    } catch (error) {
        console.error(error);
        throw error;
    }
}
```

## 注意事项

1. **await 只能在 async 函数中使用**：在普通函数中使用 await 会报错
2. **async 函数总是返回 Promise**：即使没有显式返回 Promise
3. **await 会暂停执行**：等待 Promise 完成后继续执行
4. **错误处理**：使用 try/catch 处理错误

## 常见错误

### 错误 1：在非 async 函数中使用 await

```js
// 错误：在普通函数中使用 await
function fetchData() {
    const data = await fetch('/api/data'); // SyntaxError
}

// 正确：使用 async 函数
async function fetchData() {
    const data = await fetch('/api/data');
}
```

### 错误 2：忘记 await

```js
// 错误：忘记 await，得到 Promise 对象而不是结果
async function fetchData() {
    const response = fetch('/api/data'); // response 是 Promise，不是 Response
    const data = response.json(); // 错误
}

// 正确：使用 await
async function fetchData() {
    const response = await fetch('/api/data');
    const data = await response.json();
}
```

### 错误 3：错误处理不当

```js
// 错误：没有处理错误
async function fetchData() {
    const response = await fetch('/api/data');
    const data = await response.json();
    return data;
}

// 正确：使用 try/catch 处理错误
async function fetchData() {
    try {
        const response = await fetch('/api/data');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error(error);
        throw error;
    }
}
```

## 最佳实践

1. **使用 async/await**：在支持的环境中，优先使用 async/await
2. **错误处理**：始终使用 try/catch 处理错误
3. **避免过度使用**：不是所有异步操作都需要 async/await
4. **理解 Promise**：async/await 基于 Promise，需要理解 Promise

## 练习

1. **基本使用**：将一个使用 Promise 的异步函数改写为使用 async/await。

2. **async 函数**：创建一个 async 函数，使用 await 等待多个异步操作。

3. **错误处理**：编写一个 async 函数，使用 try/catch 处理可能的错误。

4. **对比练习**：将同一个异步操作分别用 Promise 和 async/await 实现，对比代码差异。

5. **实际场景**：实现一个完整的用户数据加载流程，使用 async/await 处理多个异步操作。

完成以上练习后，继续学习下一节，了解 async 函数的详细用法。

## 总结

async/await 是 JavaScript 异步编程的重要语法，它基于 Promise，使异步代码更加清晰易读。理解 async/await 的概念和基本用法，是掌握现代 JavaScript 异步编程的关键。使用 async/await 可以显著提高代码的可读性和可维护性。

## 相关资源

- [MDN：async function](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/async_function)
- [MDN：await](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/await)
- [JavaScript.info：async/await](https://zh.javascript.info/async-await)
