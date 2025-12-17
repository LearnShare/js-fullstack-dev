# 3.3.3 await 表达式

## 概述

await 表达式用于在 async 函数中等待 Promise 完成，并返回 Promise 的结果。本节详细介绍 await 的使用、等待机制和注意事项。

## await 的基本用法

### 语法格式

**语法格式**：`await expression`

**参数说明**：

| 参数名       | 类型      | 说明                           | 是否必需 | 默认值 |
|:-------------|:----------|:-------------------------------|:---------|:-------|
| `expression` | Promise   | 要等待的 Promise 或值           | 是       | -      |

**返回值**：Promise 的结果值

### 基本使用

```js
async function fetchData() {
    const response = await fetch('/api/data');
    const data = await response.json();
    return data;
}
```

### 等待 Promise 完成

await 会暂停 async 函数的执行，等待 Promise 完成：

```js
async function example() {
    console.log('1');
    
    await new Promise(resolve => setTimeout(resolve, 1000));
    
    console.log('2'); // 1 秒后执行
}
```

### 获取返回值

await 返回 Promise 的结果值：

```js
async function getValue() {
    const value = await Promise.resolve(42);
    console.log(value); // 42
    return value;
}
```

## await 的等待机制

### 等待 fulfilled Promise

如果 Promise 成功，await 返回 resolved 的值：

```js
async function example() {
    const value = await Promise.resolve('成功');
    console.log(value); // "成功"
}
```

### 等待 rejected Promise

如果 Promise 失败，await 会抛出错误：

```js
async function example() {
    try {
        await Promise.reject('错误');
    } catch (error) {
        console.error(error); // "错误"
    }
}
```

### 等待非 Promise 值

如果 await 的值不是 Promise，会被转换为 resolved Promise：

```js
async function example() {
    const value = await 42; // 等同于 await Promise.resolve(42)
    console.log(value); // 42
}
```

## await 的使用场景

### 串行执行

await 让异步操作按顺序执行：

```js
async function processData() {
    const data1 = await fetchData1();
    const data2 = await fetchData2();
    const data3 = await fetchData3();
    
    return { data1, data2, data3 };
}
```

### 依赖关系

当后续操作依赖于前面的结果时：

```js
async function getUserPosts(userId) {
    const user = await fetchUser(userId);
    const posts = await fetchUserPosts(user.id);
    return posts;
}
```

### 错误处理

使用 try/catch 处理 await 的错误：

```js
async function fetchData() {
    try {
        const response = await fetch('/api/data');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('获取数据失败:', error);
        throw error;
    }
}
```

## 注意事项

1. **只能在 async 函数中使用**：在普通函数中使用 await 会报错
2. **会暂停执行**：await 会暂停 async 函数的执行
3. **错误处理**：await 的 Promise 失败会抛出错误，需要用 try/catch 处理
4. **性能考虑**：多个 await 会串行执行，考虑使用 Promise.all 并行执行

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
// 错误：忘记 await，得到 Promise 对象
async function fetchData() {
    const response = fetch('/api/data'); // response 是 Promise
    const data = response.json(); // 错误
}

// 正确：使用 await
async function fetchData() {
    const response = await fetch('/api/data');
    const data = await response.json();
}
```

### 错误 3：在顶层使用 await（旧版本）

```js
// 错误：在模块顶层使用 await（需要支持顶层 await 的环境）
const data = await fetch('/api/data');

// 正确：在 async 函数中使用
async function main() {
    const data = await fetch('/api/data');
}
main();
```

## 最佳实践

1. **合理使用 await**：只在需要等待结果时使用 await
2. **错误处理**：使用 try/catch 处理 await 的错误
3. **性能优化**：多个独立的 await 考虑使用 Promise.all 并行执行
4. **理解机制**：理解 await 的等待和暂停机制

## 练习

1. **基本使用**：创建 async 函数，使用 await 等待多个 Promise。

2. **错误处理**：编写代码演示 await 的错误处理机制。

3. **串行执行**：使用 await 实现多个异步操作的串行执行。

4. **依赖关系**：实现依赖前一个异步操作结果的场景。

5. **实际应用**：实现一个使用 await 的实际场景，正确处理错误和返回值。

完成以上练习后，继续学习下一节，了解错误处理和并行执行。

## 总结

await 表达式用于在 async 函数中等待 Promise 完成，它会让函数暂停执行直到 Promise 完成。理解 await 的使用、等待机制和注意事项，是掌握 async/await 的关键。
