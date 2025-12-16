# 2.7.3 数组方法（map、filter、reduce）

## 概述

数组提供了丰富的方法来处理数据。本节介绍常用的数组方法，包括 map、filter、reduce、forEach 等。这些方法都是函数式编程风格，不修改原数组（除了 `sort()`），返回新数组或新值。

数组方法的主要特点：

- **不修改原数组**：大多数方法返回新数组，不修改原数组
- **函数式风格**：使用回调函数处理每个元素
- **链式调用**：可以组合多个方法进行链式调用
- **性能优化**：现代 JavaScript 引擎对这些方法进行了优化

## map()

### 语法格式

```js
array.map(callbackFn[, thisArg])
```

### 参数说明

| 参数名       | 类型     | 说明                           | 是否必需 | 默认值 |
|:-------------|:---------|:-------------------------------|:---------|:-------|
| `callbackFn` | function | 为每个元素调用的函数           | 是       | -      |
| `thisArg`    | any      | 回调函数的 this 值             | 否       | -      |

**回调函数参数**：

| 参数名      | 类型   | 说明           |
|:------------|:-------|:---------------|
| `element`   | any    | 当前元素       |
| `index`     | number | 当前索引       |
| `array`     | Array  | 原数组         |

### 返回值

新的数组对象，包含回调函数返回的所有值

### 基本用法

**示例 1**：将每个元素乘以 2

```js
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(x => x * 2);
console.log(doubled); // [2, 4, 6, 8, 10]
console.log(numbers); // [1, 2, 3, 4, 5]（原数组未改变）
```

**输出说明**：`map()` 返回新数组，原数组不变。

**示例 2**：转换对象数组

```js
const users = [
  { name: "John", age: 30 },
  { name: "Jane", age: 25 }
];

const names = users.map(user => user.name);
console.log(names); // ["John", "Jane"]
```

**输出说明**：从对象数组中提取特定属性。

**示例 3**：使用索引

```js
const numbers = [1, 2, 3, 4, 5];
const indexed = numbers.map((value, index) => `${index}: ${value}`);
console.log(indexed);
// ["0: 1", "1: 2", "2: 3", "3: 4", "4: 5"]
```

**输出说明**：回调函数可以接收元素和索引两个参数。

### 注意事项

1. **不修改原数组**：`map()` 不会修改原数组
2. **返回新数组**：总是返回一个新数组，长度与原数组相同
3. **稀疏数组**：稀疏数组中的空位会被跳过，但会保留在结果中

## filter()

### 语法格式

```js
array.filter(callbackFn[, thisArg])
```

### 参数说明

| 参数名       | 类型     | 说明                           | 是否必需 | 默认值 |
|:-------------|:---------|:-------------------------------|:---------|:-------|
| `callbackFn` | function | 测试函数，返回 true 保留元素  | 是       | -      |
| `thisArg`    | any      | 回调函数的 this 值             | 否       | -      |

**回调函数参数**：

| 参数名      | 类型   | 说明           |
|:------------|:-------|:---------------|
| `element`   | any    | 当前元素       |
| `index`     | number | 当前索引       |
| `array`     | Array  | 原数组         |

### 返回值

新的数组对象，包含通过测试的所有元素

### 基本用法

**示例 1**：过滤偶数

```js
const numbers = [1, 2, 3, 4, 5];
const evens = numbers.filter(x => x % 2 === 0);
console.log(evens); // [2, 4]
console.log(numbers); // [1, 2, 3, 4, 5]（原数组未改变）
```

**输出说明**：`filter()` 返回通过测试的元素组成的新数组。

**示例 2**：过滤对象数组

```js
const users = [
  { name: "John", age: 30 },
  { name: "Jane", age: 25 },
  { name: "Bob", age: 35 }
];

const adults = users.filter(user => user.age >= 30);
console.log(adults);
// [{ name: "John", age: 30 }, { name: "Bob", age: 35 }]
```

**输出说明**：根据条件过滤对象数组。

### 注意事项

1. **返回新数组**：总是返回一个新数组，长度可能小于原数组
2. **真值测试**：回调函数返回真值时保留元素，假值时过滤
3. **稀疏数组**：稀疏数组中的空位会被跳过

## reduce()

### 语法格式

```js
array.reduce(callbackFn[, initialValue])
```

### 参数说明

| 参数名         | 类型     | 说明                           | 是否必需 | 默认值 |
|:---------------|:---------|:-------------------------------|:---------|:-------|
| `callbackFn`   | function | 归约函数                       | 是       | -      |
| `initialValue` | any      | 初始值                         | 否       | -      |

**回调函数参数**：

| 参数名      | 类型   | 说明           |
|:------------|:-------|:---------------|
| `accumulator` | any    | 累加器（上一次回调的返回值） |
| `currentValue` | any    | 当前元素       |
| `index`     | number | 当前索引       |
| `array`     | Array  | 原数组         |

### 返回值

归约后的值（可以是任何类型）

### 基本用法

**示例 1**：求和

```js
const numbers = [1, 2, 3, 4, 5];
const sum = numbers.reduce((acc, x) => acc + x, 0);
console.log(sum); // 15
```

**输出说明**：从 0 开始累加所有元素。

**示例 2**：计算对象数组的总和

```js
const users = [
  { name: "John", age: 30 },
  { name: "Jane", age: 25 }
];

const totalAge = users.reduce((acc, user) => acc + user.age, 0);
console.log(totalAge); // 55
```

**输出说明**：从对象数组中提取并累加数值。

**示例 3**：不使用初始值

```js
const numbers = [1, 2, 3, 4, 5];
const sum = numbers.reduce((acc, x) => acc + x);
console.log(sum); // 15
// 第一次调用时，acc 为第一个元素，x 为第二个元素
```

**输出说明**：如果不提供初始值，第一次调用时 `acc` 为第一个元素，`x` 为第二个元素。

**示例 4**：复杂归约（数组转对象）

```js
const users = [
  { id: 1, name: "John" },
  { id: 2, name: "Jane" }
];

const userMap = users.reduce((acc, user) => {
  acc[user.id] = user.name;
  return acc;
}, {});

console.log(userMap); // { 1: "John", 2: "Jane" }
```

**输出说明**：将数组转换为对象。

### 注意事项

1. **初始值**：提供初始值更安全，避免空数组错误
2. **返回值**：必须返回累加器，否则下次迭代会得到 `undefined`
3. **空数组**：空数组且无初始值会抛出错误

## forEach()

### 语法格式

```js
array.forEach(callbackFn[, thisArg])
```

### 参数说明

| 参数名       | 类型     | 说明                           | 是否必需 | 默认值 |
|:-------------|:---------|:-------------------------------|:---------|:-------|
| `callbackFn` | function | 为每个元素调用的函数           | 是       | -      |
| `thisArg`    | any      | 回调函数的 this 值             | 否       | -      |

**回调函数参数**：

| 参数名      | 类型   | 说明           |
|:------------|:-------|:---------------|
| `element`   | any    | 当前元素       |
| `index`     | number | 当前索引       |
| `array`     | Array  | 原数组         |

### 返回值

`undefined`

### 基本用法

**示例 1**：遍历数组

```js
const numbers = [1, 2, 3, 4, 5];
numbers.forEach(x => console.log(x));
// 1
// 2
// 3
// 4
// 5
```

**输出说明**：`forEach()` 用于遍历数组，不返回新数组。

**示例 2**：修改外部变量

```js
let sum = 0;
const numbers = [1, 2, 3, 4, 5];
numbers.forEach(x => {
  sum += x;
});
console.log(sum); // 15
```

**输出说明**：可以通过修改外部变量来累积值。

### 与 map 的区别

| 特性          | `forEach()`              | `map()`                  |
|:--------------|:------------------------|:-------------------------|
| **返回值**    | `undefined`             | 新数组                   |
| **用途**      | 遍历执行副作用          | 转换数组                 |
| **链式调用**  | 不支持                  | 支持                     |
| **性能**      | 略快（不创建新数组）    | 略慢（创建新数组）       |

```js
// forEach：不返回新数组
const numbers = [1, 2, 3];
const result = numbers.forEach(x => x * 2);
console.log(result); // undefined

// map：返回新数组
const doubled = numbers.map(x => x * 2);
console.log(doubled); // [2, 4, 6]
```

## 其他常用方法

### find() 和 findIndex()

**语法**：`array.find(callbackFn[, thisArg])`  
**返回值**：找到的元素，未找到返回 `undefined`

**语法**：`array.findIndex(callbackFn[, thisArg])`  
**返回值**：找到的索引，未找到返回 -1

```js
const users = [
  { id: 1, name: "John" },
  { id: 2, name: "Jane" }
];

const user = users.find(u => u.id === 2);
console.log(user); // { id: 2, name: "Jane" }

const index = users.findIndex(u => u.id === 2);
console.log(index); // 1
```

### some() 和 every()

**语法**：`array.some(callbackFn[, thisArg])`  
**返回值**：布尔值，至少一个元素通过测试返回 `true`

**语法**：`array.every(callbackFn[, thisArg])`  
**返回值**：布尔值，所有元素通过测试返回 `true`

```js
const numbers = [1, 2, 3, 4, 5];

console.log(numbers.some(x => x > 3));  // true（至少一个满足）
console.log(numbers.every(x => x > 0)); // true（全部满足）
console.log(numbers.every(x => x > 3)); // false（不是全部满足）
```

### sort()

**语法**：`array.sort([compareFunction])`

**参数说明**：

| 参数名            | 类型     | 说明                           | 是否必需 | 默认值 |
|:------------------|:---------|:-------------------------------|:---------|:-------|
| `compareFunction` | function | 比较函数                       | 否       | -      |

**返回值**：排序后的数组（修改原数组）

**比较函数**：
- 返回负数：第一个元素排在前面
- 返回 0：保持原顺序
- 返回正数：第二个元素排在前面

```js
// 默认排序（字符串排序）
const numbers = [3, 1, 4, 1, 5];
numbers.sort();
console.log(numbers); // [1, 1, 3, 4, 5]

// 数字排序
const nums = [3, 1, 4, 1, 5];
nums.sort((a, b) => a - b);
console.log(nums); // [1, 1, 3, 4, 5]

// 对象排序
const users = [
  { name: "John", age: 30 },
  { name: "Jane", age: 25 }
];
users.sort((a, b) => a.age - b.age);
console.log(users); // 按年龄升序排序
```

**注意事项**：

- `sort()` 会修改原数组
- 默认按字符串排序，数字排序需要提供比较函数
- 排序是稳定的（ES2019+）

## 方法链式调用

数组方法可以链式调用，组合多个操作：

```js
const numbers = [1, 2, 3, 4, 5];

const result = numbers
  .filter(x => x % 2 === 0)  // [2, 4]
  .map(x => x * 2)            // [4, 8]
  .reduce((acc, x) => acc + x, 0); // 12

console.log(result); // 12
```

**说明**：链式调用时，每个方法接收上一个方法的返回值。

## 注意事项

### 1. 不修改原数组

大多数数组方法不修改原数组（除了 `sort()`、`reverse()` 等）：

```js
const arr = [1, 2, 3];
const doubled = arr.map(x => x * 2);
console.log(arr);      // [1, 2, 3]（未改变）
console.log(doubled);  // [2, 4, 6]
```

### 2. 回调函数的返回值

- `map()`：必须返回值，用于构建新数组
- `filter()`：必须返回布尔值，决定是否保留元素
- `reduce()`：必须返回累加器，用于下次迭代

### 3. 空数组处理

```js
// map 和 filter 返回空数组
[].map(x => x * 2);     // []
[].filter(x => x > 0);   // []

// reduce 需要初始值
[].reduce((acc, x) => acc + x, 0);  // 0
[].reduce((acc, x) => acc + x);     // 错误！
```

### 4. 性能考虑

- `forEach()` 比 `map()` 略快（不创建新数组）
- 链式调用会创建中间数组，可能影响性能
- 对于大量数据，考虑使用 `for` 循环

## 常见错误

### 错误 1：忘记返回累加器

```js
// 错误
const sum = [1, 2, 3].reduce((acc, x) => {
  acc + x; // 忘记 return
}, 0);
console.log(sum); // undefined

// 正确
const sum = [1, 2, 3].reduce((acc, x) => {
  return acc + x;
}, 0);
console.log(sum); // 6
```

### 错误 2：在 forEach 中返回

```js
// 错误：forEach 不返回值
const doubled = [1, 2, 3].forEach(x => x * 2);
console.log(doubled); // undefined

// 正确：使用 map
const doubled = [1, 2, 3].map(x => x * 2);
console.log(doubled); // [2, 4, 6]
```

## 最佳实践

1. **优先使用数组方法**：比传统循环更简洁、可读
2. **链式调用**：组合多个方法处理数据
3. **提供初始值**：`reduce()` 总是提供初始值，避免错误
4. **避免副作用**：`map()` 和 `filter()` 应该是纯函数
5. **性能考虑**：大量数据时考虑使用 `for` 循环

## 练习

1. **map() 练习**：
   - 将数字数组转换为字符串数组
   - 从对象数组中提取特定属性

2. **filter() 练习**：
   - 过滤出大于 10 的数字
   - 过滤出年龄大于 18 的用户

3. **reduce() 练习**：
   - 计算数组元素的总和和平均值
   - 将数组转换为对象（键值对）

4. **方法组合**：
   - 使用链式调用过滤、转换、归约数组
   - 实现复杂的数据处理流程

5. **实际应用**：
   - 处理 API 返回的数据
   - 实现数据统计和分析功能

## 总结

数组方法提供了强大的数据处理能力：

- **map()**：转换每个元素，返回新数组
- **filter()**：过滤元素，返回新数组
- **reduce()**：归约数组，返回单个值
- **forEach()**：遍历数组，不返回新数组
- **链式调用**：组合多个方法处理数据

掌握这些方法是函数式编程的基础。

继续学习下一节，了解解构赋值。

---

**最后更新**：2025-12-16
