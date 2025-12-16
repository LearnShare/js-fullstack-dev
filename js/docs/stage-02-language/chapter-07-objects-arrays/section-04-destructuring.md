# 2.7.4 解构赋值

## 概述

解构赋值允许从对象或数组中提取值并赋值给变量。本节介绍对象解构、数组解构和参数解构的使用。

## 对象解构

### 基本语法

```js
const user = {
    name: "John",
    age: 30,
    email: "john@example.com"
};

const { name, age } = user;
console.log(name); // "John"
console.log(age);  // 30
```

### 重命名变量

```js
const { name: userName, age: userAge } = user;
console.log(userName); // "John"
console.log(userAge);  // 30
```

### 默认值

```js
const { name, age = 18 } = user;
console.log(age); // 30（如果 user.age 存在）

const { name: userName, city = "Unknown" } = user;
console.log(city); // "Unknown"（默认值）
```

### 嵌套解构

```js
const user = {
    name: "John",
    address: {
        city: "New York",
        zip: "10001"
    }
};

const { address: { city, zip } } = user;
console.log(city); // "New York"
console.log(zip);  // "10001"
```

## 数组解构

### 基本语法

```js
const arr = [1, 2, 3];
const [a, b, c] = arr;
console.log(a); // 1
console.log(b); // 2
console.log(c); // 3
```

### 跳过元素

```js
const [first, , third] = [1, 2, 3];
console.log(first); // 1
console.log(third); // 3
```

### 剩余元素

```js
const [first, ...rest] = [1, 2, 3, 4, 5];
console.log(first); // 1
console.log(rest);  // [2, 3, 4, 5]
```

### 默认值

```js
const [a = 1, b = 2] = [10];
console.log(a); // 10
console.log(b); // 2（默认值）
```

## 参数解构

### 对象参数

```js
function greet({ name, age = 18 }) {
    return `Hello, ${name}, age ${age}!`;
}

greet({ name: "John" });        // "Hello, John, age 18!"
greet({ name: "John", age: 30 }); // "Hello, John, age 30!"
```

### 数组参数

```js
function process([first, second, ...rest]) {
    console.log(first, second, rest);
}

process([1, 2, 3, 4, 5]); // 1 2 [3, 4, 5]
```

## 交换变量

```js
let a = 1;
let b = 2;

[a, b] = [b, a];
console.log(a); // 2
console.log(b); // 1
```

## 注意事项

### 1. 解构不存在的属性

```js
const obj = { name: "John" };
const { age } = obj;
console.log(age); // undefined

// 使用默认值
const { age = 18 } = obj;
console.log(age); // 18
```

### 2. 解构 null 或 undefined

```js
// 解构 null 或 undefined 会报错
// const { name } = null;        // TypeError
// const { name } = undefined;  // TypeError

// 使用默认值避免错误
const { name = "Guest" } = null || {};
console.log(name); // "Guest"
```

### 3. 数组解构超出范围

```js
const arr = [1, 2];
const [a, b, c] = arr;
console.log(a, b, c); // 1 2 undefined

// 使用默认值
const [x, y, z = 0] = arr;
console.log(x, y, z); // 1 2 0
```

### 4. 解构时不能使用已声明的变量

```js
// 错误：不能使用已声明的变量
let name = "John";
// const { name } = user; // SyntaxError

// 正确：使用重命名
const { name: userName } = user;
```

## 常见问题

### 问题 1：如何解构并保留原对象？

```js
const user = { name: "John", age: 30, email: "john@example.com" };

// 解构部分属性，保留其余
const { email, ...rest } = user;
console.log(rest); // { name: "John", age: 30 }
```

### 问题 2：如何解构并设置默认值？

```js
const user = { name: "John" };

// 对象解构默认值
const { name, age = 18, city = "Unknown" } = user;

// 数组解构默认值
const [a = 1, b = 2, c = 3] = [10];
```

### 问题 3：如何交换变量？

```js
let a = 1;
let b = 2;

// 使用解构交换
[a, b] = [b, a];
console.log(a, b); // 2 1
```

## 最佳实践

### 1. 使用解构简化函数参数

```js
// 好的做法：使用解构参数
function createUser({ name, age, email }) {
    return { name, age, email };
}

// 避免：直接访问对象属性
function createUser2(user) {
    return {
        name: user.name,
        age: user.age,
        email: user.email
    };
}
```

### 2. 使用默认值提供后备

```js
// 好的做法：使用默认值
function greet({ name = "Guest", age = 18 } = {}) {
    return `Hello, ${name}, age ${age}!`;
}

// 避免：手动检查
function greet2(user) {
    const name = user && user.name || "Guest";
    const age = user && user.age || 18;
    return `Hello, ${name}, age ${age}!`;
}
```

### 3. 使用剩余参数收集多余值

```js
// 好的做法：使用剩余参数
const [first, second, ...rest] = [1, 2, 3, 4, 5];

// 避免：使用 slice
const arr = [1, 2, 3, 4, 5];
const first2 = arr[0];
const second2 = arr[1];
const rest2 = arr.slice(2);
```

## 练习

1. **对象解构**：从用户对象中解构出 `name`、`age`、`email`，并为 `age` 设置默认值 18。

2. **数组解构**：从数组中解构出第一个和最后一个元素，使用剩余参数收集中间的元素。

3. **嵌套解构**：从嵌套对象中解构出 `address.city` 和 `address.zip`。

4. **参数解构**：编写一个函数，使用对象参数解构，接收 `name`、`age`、`email` 参数。

5. **变量交换**：使用数组解构交换两个变量的值。

6. **解构重命名**：从对象中解构属性并重命名为不同的变量名。

完成以上练习后，继续学习下一节，了解展开运算符。

## 总结

解构赋值提供了简洁的变量赋值方式。主要要点：

- 对象解构：从对象中提取值
- 数组解构：从数组中提取值
- 参数解构：函数参数解构
- 默认值：为解构变量提供默认值
- 嵌套解构：解构嵌套结构
- 重命名：解构时重命名变量
- 剩余参数：收集多余的解构值

继续学习下一节，了解展开运算符。
