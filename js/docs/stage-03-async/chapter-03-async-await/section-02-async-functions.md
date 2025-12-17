# 3.3.2 async 函数

## 概述

async 函数是使用 async 关键字声明的函数，它会自动返回一个 Promise。本节详细介绍 async 函数的定义、返回值、特性和使用场景。

## async 函数的定义

### 函数声明

```js
async function myFunction() {
    // 函数体
}
```

### 函数表达式

```js
const myFunction = async function() {
    // 函数体
};
```

### 箭头函数

```js
const myFunction = async () => {
    // 函数体
};
```

### 对象方法

```js
const obj = {
    async myMethod() {
        // 方法体
    }
};
```

### 类方法

```js
class MyClass {
    async myMethod() {
        // 方法体
    }
}
```

## async 函数的返回值

### 自动包装为 Promise

async 函数总是返回 Promise，即使函数体内没有异步操作：

```js
async function syncFunction() {
    return 42;
}

const result = syncFunction();
console.log(result); // Promise { <fulfilled>: 42 }

result.then(value => {
    console.log(value); // 42
});
```

### 返回普通值

如果 async 函数返回普通值，会被自动包装为 resolved Promise：

```js
async function getValue() {
    return 'hello';
}

getValue().then(value => {
    console.log(value); // "hello"
});
```

### 返回 Promise

如果 async 函数返回 Promise，会直接返回该 Promise：

```js
async function getPromise() {
    return Promise.resolve('hello');
}

getPromise().then(value => {
    console.log(value); // "hello"
});
```

### 抛出错误

如果 async 函数抛出错误，会返回 rejected Promise：

```js
async function throwError() {
    throw new Error('错误');
}

throwError().catch(error => {
    console.error(error.message); // "错误"
});
```

## async 函数的特性

### 异步执行

async 函数内部的代码是异步执行的：

```js
async function asyncFunction() {
    console.log('1');
    await Promise.resolve();
    console.log('2');
}

console.log('开始');
asyncFunction();
console.log('结束');

// 输出：
// 开始
// 1
// 结束
// 2
```

### 可以使用 await

async 函数内可以使用 await 等待 Promise：

```js
async function fetchData() {
    const response = await fetch('/api/data');
    const data = await response.json();
    return data;
}
```

### 可以被 await

async 函数返回 Promise，可以被 await：

```js
async function getData() {
    return 'data';
}

async function main() {
    const data = await getData();
    console.log(data); // "data"
}
```

## 注意事项

1. **总是返回 Promise**：async 函数总是返回 Promise
2. **可以使用 await**：async 函数内可以使用 await
3. **异步执行**：async 函数内的代码是异步执行的
4. **错误处理**：抛出错误会返回 rejected Promise

## 常见错误

### 错误 1：忘记 async 关键字

```js
// 错误：忘记 async，不能使用 await
function fetchData() {
    const data = await fetch('/api/data'); // SyntaxError
}

// 正确：使用 async
async function fetchData() {
    const data = await fetch('/api/data');
}
```

### 错误 2：误解返回值

```js
// 错误：async 函数返回 Promise，不是直接返回值
async function getValue() {
    return 42;
}

const value = getValue(); // value 是 Promise，不是 42
console.log(value); // Promise { <fulfilled>: 42 }

// 正确：使用 await 或 then
const value = await getValue(); // 42
// 或
getValue().then(value => console.log(value)); // 42
```

## 最佳实践

1. **明确标记 async**：需要异步操作的函数使用 async
2. **理解返回值**：记住 async 函数返回 Promise
3. **错误处理**：正确处理 async 函数的错误
4. **合理使用**：不是所有函数都需要 async

## 练习

1. **async 函数定义**：使用不同的方式定义 async 函数（函数声明、表达式、箭头函数）。

2. **返回值理解**：创建 async 函数，返回不同类型的数据，理解返回值的处理。

3. **异步执行**：编写代码演示 async 函数的异步执行特性。

4. **嵌套调用**：创建多个 async 函数，演示它们之间的调用关系。

5. **实际应用**：实现一个使用 async 函数的实际场景（如数据获取、处理等）。

完成以上练习后，继续学习下一节，了解 await 表达式的详细用法。

## 总结

async 函数是声明异步函数的关键字，它使函数自动返回 Promise，并允许在函数内使用 await。理解 async 函数的定义、返回值和特性，是掌握 async/await 的基础。
