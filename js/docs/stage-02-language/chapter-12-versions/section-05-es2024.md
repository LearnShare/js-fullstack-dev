# 2.12.5 ES2024 新特性

## 概述

ES2024（ES15）是 ECMAScript 2024 标准，于 2024 年 6 月发布。ES2024 引入了 Promise.withResolvers、正则表达式 /v 标志、Object.groupBy 等特性，进一步完善了 JavaScript 的异步编程和数据处理能力。

## 核心特性

ES2024 主要包含以下新特性：

1. **Promise.withResolvers()**：创建可外部控制的 Promise
2. **Object.groupBy()**：按条件分组对象数组
3. **Array.prototype.groupBy()**：按条件分组数组元素
4. **正则表达式 /v 标志**：可编排正则模式（Unicode 属性转义改进）

---

## Promise.withResolvers()

### 概述

`Promise.withResolvers()` 返回一个对象，包含一个新的 Promise 及其 resolve 和 reject 函数，允许在 Promise 外部控制其状态。

### 语法格式

```js
Promise.withResolvers()
```

### 返回值

返回一个对象，包含以下属性：

| 属性名      | 类型     | 说明                     |
|:------------|:---------|:-------------------------|
| `promise`   | Promise  | 新的 Promise 对象        |
| `resolve`   | function | 解决 Promise 的函数      |
| `reject`    | function | 拒绝 Promise 的函数      |

### 基本用法

**示例 1**：基本使用

```js
const { promise, resolve, reject } = Promise.withResolvers();

// 异步操作
setTimeout(() => {
  resolve('Success');
}, 1000);

promise.then(value => {
  console.log(value); // 'Success'
});
```

**输出说明**：`Promise.withResolvers()` 返回的对象允许在外部控制 Promise 的状态。

**示例 2**：事件监听器中的使用

```js
function createEventPromise(element, eventType) {
  const { promise, resolve } = Promise.withResolvers();

  element.addEventListener(eventType, resolve, { once: true });

  return promise;
}

const button = document.querySelector('button');
const clickPromise = createEventPromise(button, 'click');

clickPromise.then(() => {
  console.log('Button clicked!');
});
```

**输出说明**：在事件监听器中，可以使用 `resolve` 函数手动解决 Promise。

### 与传统 Promise 构造函数的对比

**传统方式**（需要包装）：

```js
function createPromise() {
  let resolve, reject;
  const promise = new Promise((res, rej) => {
    resolve = res;
    reject = rej;
  });
  return { promise, resolve, reject };
}
```

**ES2024 方式**（直接使用）：

```js
const { promise, resolve, reject } = Promise.withResolvers();
```

### 注意事项

1. **使用场景**：适用于需要在 Promise 外部控制其状态的场景
2. **兼容性**：需要 Node.js 22.0.0+ 或现代浏览器支持
3. **最佳实践**：避免过度使用，优先使用标准的 Promise 构造函数

### 常见错误

**错误 1**：多次调用 resolve 或 reject

```js
const { promise, resolve, reject } = Promise.withResolvers();

resolve('First');
resolve('Second'); // 无效，Promise 已解决

promise.then(value => {
  console.log(value); // 'First'
});
```

---

## Object.groupBy()

### 概述

`Object.groupBy()` 方法根据提供的测试函数返回的值，将可迭代对象的元素分组。

### 语法格式

```js
Object.groupBy(items, callbackFn)
```

### 参数说明

| 参数名       | 类型     | 说明                           | 是否必需 | 默认值 |
|:-------------|:---------|:-------------------------------|:---------|:-------|
| `items`      | iterable | 要分组的可迭代对象             | 是       | -      |
| `callbackFn` | function | 为每个元素调用的函数           | 是       | -      |

**回调函数参数**：

| 参数名      | 类型   | 说明           |
|:------------|:-------|:---------------|
| `element`   | any    | 当前元素       |
| `index`     | number | 当前索引       |

### 返回值

返回一个对象，键是回调函数返回的值，值是对应元素的数组。

### 基本用法

**示例 1**：按属性分组

```js
const users = [
  { name: 'Alice', age: 20 },
  { name: 'Bob', age: 25 },
  { name: 'Charlie', age: 20 },
  { name: 'David', age: 25 }
];

const grouped = Object.groupBy(users, user => user.age);
console.log(grouped);
// {
//   20: [{ name: 'Alice', age: 20 }, { name: 'Charlie', age: 20 }],
//   25: [{ name: 'Bob', age: 25 }, { name: 'David', age: 25 }]
// }
```

**输出说明**：按 `age` 属性分组，返回以年龄为键、用户数组为值的对象。

**示例 2**：按条件分组

```js
const numbers = [1, 2, 3, 4, 5, 6];
const grouped = Object.groupBy(numbers, n => n % 2 === 0 ? 'even' : 'odd');
console.log(grouped);
// {
//   odd: [1, 3, 5],
//   even: [2, 4, 6]
// }
```

**输出说明**：按奇偶性分组，返回包含 'odd' 和 'even' 键的对象。

### 注意事项

1. **返回对象**：返回一个普通对象，不是 Map
2. **键的类型**：键会被转换为字符串
3. **兼容性**：需要 Node.js 22.0.0+ 或现代浏览器支持

---

## Array.prototype.groupBy()

### 概述

`Array.prototype.groupBy()` 方法根据提供的测试函数返回的值，将数组元素分组。

### 语法格式

```js
array.groupBy(callbackFn, thisArg)
```

### 参数说明

与 `Object.groupBy()` 相同。

### 返回值

返回一个对象，键是回调函数返回的值，值是对应元素的数组。

### 基本用法

**示例**：

```js
const numbers = [1, 2, 3, 4, 5, 6];
const grouped = numbers.groupBy(n => n % 2 === 0 ? 'even' : 'odd');
console.log(grouped);
// {
//   odd: [1, 3, 5],
//   even: [2, 4, 6]
// }
```

**输出说明**：与 `Object.groupBy()` 功能相同，但作为数组方法调用。

### 与 Object.groupBy() 的对比

| 特性              | `Object.groupBy()`        | `Array.prototype.groupBy()` |
|:------------------|:--------------------------|:---------------------------|
| **调用方式**      | `Object.groupBy(arr, fn)` | `arr.groupBy(fn)`          |
| **适用对象**      | 任何可迭代对象            | 仅数组                     |
| **返回值**        | 对象                      | 对象                       |

---

## 兼容性说明

### 浏览器支持

| 特性                  | Chrome | Firefox | Safari | Edge  |
|:----------------------|:-------|:--------|:-------|:------|
| `Promise.withResolvers()` | 119+ | 121+    | 18+    | 119+  |
| `Object.groupBy()`    | 117+   | 119+    | 18+    | 117+  |
| `Array.prototype.groupBy()` | 117+ | 119+    | 18+    | 117+  |

### Node.js 支持

- **`Promise.withResolvers()`**：Node.js 22.0.0+
- **`Object.groupBy()`**：Node.js 22.0.0+
- **`Array.prototype.groupBy()`**：Node.js 22.0.0+

### 转译和 Polyfill

如果需要在旧环境中使用 ES2024 特性：

1. **Babel**：使用相应的插件转译
2. **TypeScript**：在 `tsconfig.json` 中设置 `target: "ES2024"`
3. **Polyfill**：可以使用 `core-js` 的 polyfill

---

## 最佳实践

1. **Promise.withResolvers()**：
   - 用于需要在 Promise 外部控制其状态的场景
   - 避免过度使用，优先使用标准 Promise 构造函数

2. **分组方法**：
   - 使用 `Object.groupBy()` 处理任何可迭代对象
   - 使用 `Array.prototype.groupBy()` 处理数组（更简洁）

---

## 练习

1. **Promise.withResolvers()**：
   - 创建一个函数，使用 `Promise.withResolvers()` 实现超时控制
   - 在事件监听器中使用 `Promise.withResolvers()` 等待用户交互

2. **分组方法**：
   - 使用 `Object.groupBy()` 将用户数组按年龄分组
   - 使用 `Array.prototype.groupBy()` 将数字数组按奇偶性分组

3. **综合练习**：
   - 实现一个数据统计函数，使用分组方法分析数据分布

---

## 总结

ES2024 进一步完善了 JavaScript 的异步编程和数据处理能力：

- **Promise.withResolvers()**：提供更灵活的 Promise 控制机制
- **分组方法**：简化数据分组操作

这些特性在现代 JavaScript 开发中非常有用。

完成阶段二学习后，继续学习阶段三：异步编程。

---

**最后更新**：2025-12-16
