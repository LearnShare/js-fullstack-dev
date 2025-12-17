# 3.2.4 Promise 组合方法（all、race、allSettled）

## 概述

Promise 提供了多个组合方法，用于同时处理多个 Promise。本节介绍 Promise.all、Promise.race、Promise.allSettled、Promise.any 等组合方法的使用场景和区别。

## Promise.all()

### 基本概念

`Promise.all()` 接收一个 Promise 数组，当**所有** Promise 都成功时，返回所有结果的数组；如果**任何一个** Promise 失败，立即返回失败。

### 语法格式

**语法格式**：`Promise.all(iterable)`

**参数说明**：

| 参数名      | 类型      | 说明                           | 是否必需 | 默认值 |
|:------------|:----------|:-------------------------------|:---------|:-------|
| `iterable`  | iterable  | Promise 数组或可迭代对象        | 是       | -      |

**返回值**：一个新的 Promise 对象

- 如果所有 Promise 都成功，返回所有结果的数组
- 如果任何一个 Promise 失败，返回第一个失败的错误

### 基本使用

```js
const p1 = Promise.resolve(1);
const p2 = Promise.resolve(2);
const p3 = Promise.resolve(3);

Promise.all([p1, p2, p3])
    .then(values => {
        console.log(values); // [1, 2, 3]
    });
```

### 所有成功的情况

```js
Promise.all([
    fetch('/api/user'),
    fetch('/api/posts'),
    fetch('/api/comments')
])
    .then(([user, posts, comments]) => {
        // 所有请求都成功
        console.log(user, posts, comments);
    });
```

### 其中一个失败的情况

```js
const p1 = Promise.resolve(1);
const p2 = Promise.reject('错误');
const p3 = Promise.resolve(3);

Promise.all([p1, p2, p3])
    .then(values => {
        // 不会执行
    })
    .catch(error => {
        console.error(error); // "错误"（第一个失败的错误）
    });
```

### 使用场景

适用于需要**所有**操作都成功才能继续的场景：

```js
// 需要同时获取多个数据
Promise.all([
    fetchUserData(userId),
    fetchUserPosts(userId),
    fetchUserComments(userId)
])
    .then(([user, posts, comments]) => {
        // 所有数据都获取成功
        renderPage({ user, posts, comments });
    })
    .catch(error => {
        // 任何一个失败都显示错误
        showError(error);
    });
```

## Promise.race()

### 基本概念

`Promise.race()` 接收一个 Promise 数组，返回**第一个**完成（成功或失败）的 Promise 的结果。

### 语法格式

**语法格式**：`Promise.race(iterable)`

**参数说明**：

| 参数名      | 类型      | 说明                           | 是否必需 | 默认值 |
|:------------|:----------|:-------------------------------|:---------|:-------|
| `iterable`  | iterable  | Promise 数组或可迭代对象        | 是       | -      |

**返回值**：一个新的 Promise 对象，返回第一个完成的 Promise 的结果

### 基本使用

```js
const p1 = new Promise(resolve => setTimeout(() => resolve(1), 1000));
const p2 = new Promise(resolve => setTimeout(() => resolve(2), 500));
const p3 = new Promise(resolve => setTimeout(() => resolve(3), 2000));

Promise.race([p1, p2, p3])
    .then(value => {
        console.log(value); // 2（p2 最快完成）
    });
```

### 超时控制

```js
// 使用 Promise.race 实现超时控制
function fetchWithTimeout(url, timeout = 5000) {
    const fetchPromise = fetch(url);
    const timeoutPromise = new Promise((_, reject) => {
        setTimeout(() => reject(new Error('请求超时')), timeout);
    });
    
    return Promise.race([fetchPromise, timeoutPromise]);
}

fetchWithTimeout('/api/data', 3000)
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => {
        if (error.message === '请求超时') {
            console.error('请求超时，请重试');
        } else {
            console.error('请求失败:', error);
        }
    });
```

### 使用场景

适用于只需要**第一个**完成结果的场景：

- 超时控制
- 多个数据源，取最快的
- 竞态条件处理

## Promise.allSettled()

### 基本概念

`Promise.allSettled()` 接收一个 Promise 数组，等待**所有** Promise 完成（无论成功或失败），返回所有结果的数组。

### 语法格式

**语法格式**：`Promise.allSettled(iterable)`

**参数说明**：

| 参数名      | 类型      | 说明                           | 是否必需 | 默认值 |
|:------------|:----------|:-------------------------------|:---------|:-------|
| `iterable`  | iterable  | Promise 数组或可迭代对象        | 是       | -      |

**返回值**：一个新的 Promise 对象，返回所有 Promise 的结果数组

每个结果对象的结构：
- `status`: `'fulfilled'` 或 `'rejected'`
- `value`: 成功时的值（status 为 'fulfilled' 时）
- `reason`: 失败时的错误（status 为 'rejected' 时）

### 基本使用

```js
const p1 = Promise.resolve(1);
const p2 = Promise.reject('错误');
const p3 = Promise.resolve(3);

Promise.allSettled([p1, p2, p3])
    .then(results => {
        console.log(results);
        // [
        //   { status: 'fulfilled', value: 1 },
        //   { status: 'rejected', reason: '错误' },
        //   { status: 'fulfilled', value: 3 }
        // ]
    });
```

### 处理部分失败

```js
Promise.allSettled([
    fetch('/api/user'),
    fetch('/api/posts'),
    fetch('/api/comments')
])
    .then(results => {
        results.forEach((result, index) => {
            if (result.status === 'fulfilled') {
                console.log(`请求 ${index} 成功:`, result.value);
            } else {
                console.error(`请求 ${index} 失败:`, result.reason);
            }
        });
    });
```

### 使用场景

适用于需要知道**所有**操作的结果，即使部分失败的场景：

- 批量操作，需要知道每个操作的结果
- 容错处理，允许部分失败
- 数据收集，需要所有结果

## Promise.any()

### 基本概念

`Promise.any()` 接收一个 Promise 数组，返回**第一个成功**的 Promise 的结果；如果**所有** Promise 都失败，返回 AggregateError。

### 语法格式

**语法格式**：`Promise.any(iterable)`

**参数说明**：

| 参数名      | 类型      | 说明                           | 是否必需 | 默认值 |
|:------------|:----------|:-------------------------------|:---------|:-------|
| `iterable`  | iterable  | Promise 数组或可迭代对象        | 是       | -      |

**返回值**：一个新的 Promise 对象

- 如果任何一个 Promise 成功，返回第一个成功的结果
- 如果所有 Promise 都失败，返回 AggregateError

### 基本使用

```js
const p1 = Promise.reject('错误1');
const p2 = Promise.resolve(2);
const p3 = Promise.reject('错误3');

Promise.any([p1, p2, p3])
    .then(value => {
        console.log(value); // 2（第一个成功的结果）
    });
```

### 所有都失败的情况

```js
Promise.any([
    Promise.reject('错误1'),
    Promise.reject('错误2'),
    Promise.reject('错误3')
])
    .catch(error => {
        console.error(error); // AggregateError: All promises were rejected
        console.error(error.errors); // ['错误1', '错误2', '错误3']
    });
```

### 使用场景

适用于多个数据源，取第一个成功的场景：

- 多个 API 端点，使用最快的可用端点
- 容错机制，尝试多个方案
- 负载均衡，选择可用的服务

## 方法对比

| 方法                  | 成功条件           | 失败条件           | 返回值                     |
|:-----------------------|:-------------------|:-------------------|:---------------------------|
| `Promise.all`          | 所有都成功         | 任何一个失败       | 所有结果的数组             |
| `Promise.race`         | 第一个完成（任意） | 第一个完成（失败） | 第一个完成的结果           |
| `Promise.allSettled`   | 所有都完成（任意） | 不会失败（等待所有） | 所有结果的数组（包含状态） |
| `Promise.any`          | 第一个成功         | 所有都失败         | 第一个成功的结果           |

## 注意事项

1. **Promise.all**：需要所有都成功，任何一个失败立即返回失败
2. **Promise.race**：只关心第一个完成的结果
3. **Promise.allSettled**：等待所有完成，不会失败
4. **Promise.any**：只需要一个成功，所有都失败才失败

## 常见错误

### 错误 1：使用 Promise.all 处理部分失败场景

```js
// 错误：使用 Promise.all，部分失败会导致整个失败
Promise.all([
    fetch('/api/data1'), // 可能失败
    fetch('/api/data2'), // 可能失败
    fetch('/api/data3')  // 可能失败
])
    .then(results => {
        // 如果任何一个失败，这里不会执行
    });

// 正确：使用 Promise.allSettled
Promise.allSettled([
    fetch('/api/data1'),
    fetch('/api/data2'),
    fetch('/api/data3')
])
    .then(results => {
        // 即使部分失败，也会执行
    });
```

### 错误 2：误用 Promise.race

```js
// 错误：使用 Promise.race 期望所有都成功
Promise.race([
    fetch('/api/data1'),
    fetch('/api/data2'),
    fetch('/api/data3')
])
    .then(result => {
        // 只得到第一个完成的结果，其他可能还没完成
    });
```

## 最佳实践

1. **选择合适的方法**：根据需求选择合适的方法
2. **错误处理**：为每个组合方法添加错误处理
3. **性能考虑**：Promise.all 和 Promise.race 可以并行执行
4. **容错设计**：使用 Promise.allSettled 处理部分失败场景

## 练习

1. **Promise.all**：使用 Promise.all 同时获取用户信息、文章列表和评论列表。

2. **Promise.race**：使用 Promise.race 实现请求超时控制功能。

3. **Promise.allSettled**：使用 Promise.allSettled 批量处理多个操作，即使部分失败也能继续处理。

4. **Promise.any**：使用 Promise.any 从多个 API 端点获取数据，使用第一个成功的响应。

5. **实际场景**：实现一个数据加载器，需要同时从多个数据源获取数据，使用合适的 Promise 组合方法处理各种情况。

完成以上练习后，继续学习下一节，了解 Promise 错误处理的详细机制。

## 总结

Promise 组合方法提供了处理多个 Promise 的强大能力。Promise.all 适用于需要所有成功的场景，Promise.race 适用于只关心第一个完成的场景，Promise.allSettled 适用于需要所有结果的场景，Promise.any 适用于只需要一个成功的场景。根据实际需求选择合适的方法。

## 相关资源

- [MDN：Promise.all()](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/all)
- [MDN：Promise.race()](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/race)
- [MDN：Promise.allSettled()](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettled)
