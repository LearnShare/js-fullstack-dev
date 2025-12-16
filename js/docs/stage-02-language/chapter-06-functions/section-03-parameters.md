# 2.6.3 参数（默认参数、剩余参数）

## 概述

函数参数可以有默认值，也可以使用剩余参数接收多个参数。本节介绍默认参数、剩余参数和参数解构的使用。

## 默认参数

### 基本语法

```js
function greet(name = "Guest") {
    return `Hello, ${name}!`;
}

greet();        // "Hello, Guest!"
greet("John");  // "Hello, John!"
```

### 多个默认参数

```js
function createUser(name = "Guest", age = 18, city = "Unknown") {
    return { name, age, city };
}

createUser();                    // { name: "Guest", age: 18, city: "Unknown" }
createUser("John");              // { name: "John", age: 18, city: "Unknown" }
createUser("John", 30);          // { name: "John", age: 30, city: "Unknown" }
createUser("John", 30, "NYC");   // { name: "John", age: 30, city: "NYC" }
```

### 表达式作为默认值

```js
function createId(prefix = "ID", timestamp = Date.now()) {
    return `${prefix}-${timestamp}`;
}

createId();           // "ID-1234567890"
createId("USER");     // "USER-1234567890"
```

### 函数调用作为默认值

```js
function getDefaultName() {
    return "Guest";
}

function greet(name = getDefaultName()) {
    return `Hello, ${name}!`;
}

greet();        // "Hello, Guest!"
```

## 剩余参数

### 基本语法

```js
function sum(...numbers) {
    return numbers.reduce((acc, n) => acc + n, 0);
}

sum(1, 2, 3);        // 6
sum(1, 2, 3, 4, 5);  // 15
```

### 与其他参数组合

```js
function greet(greeting, ...names) {
    return `${greeting}, ${names.join(", ")}!`;
}

greet("Hello", "John", "Jane", "Bob");
// "Hello, John, Jane, Bob!"
```

### 展开运算符

```js
// 使用展开运算符传递参数
function sum(a, b, c) {
    return a + b + c;
}

let numbers = [1, 2, 3];
sum(...numbers); // 6
```

## 参数解构

### 对象解构

```js
function greet({ name, age = 18 }) {
    return `Hello, ${name}, age ${age}!`;
}

greet({ name: "John" });        // "Hello, John, age 18!"
greet({ name: "John", age: 30 }); // "Hello, John, age 30!"
```

### 数组解构

```js
function process([first, second, ...rest]) {
    console.log(first, second, rest);
}

process([1, 2, 3, 4, 5]); // 1 2 [3, 4, 5]
```

## arguments 对象

### 基本用法

```js
function sum() {
    let total = 0;
    for (let i = 0; i < arguments.length; i++) {
        total += arguments[i];
    }
    return total;
}

sum(1, 2, 3); // 6
```

### 与剩余参数的区别

```js
// arguments 是类数组对象
function oldWay() {
    console.log(arguments); // 类数组对象
    // arguments.forEach(...) // 错误，不是数组
}

// 剩余参数是真正的数组
function newWay(...args) {
    console.log(args); // 真正的数组
    args.forEach(...); // 正确
}
```

## 最佳实践

### 1. 使用默认参数

```js
// 好的做法：使用默认参数
function greet(name = "Guest") {
    return `Hello, ${name}!`;
}

// 避免：在函数体内检查
function greet2(name) {
    name = name || "Guest";
    return `Hello, ${name}!`;
}
```

### 2. 使用剩余参数

```js
// 好的做法：使用剩余参数
function sum(...numbers) {
    return numbers.reduce((acc, n) => acc + n, 0);
}

// 避免：使用 arguments
function sum2() {
    let total = 0;
    for (let i = 0; i < arguments.length; i++) {
        total += arguments[i];
    }
    return total;
}
```

### 3. 参数解构提高可读性

```js
// 好的做法：参数解构
function createUser({ name, age, email }) {
    return { name, age, email };
}

// 避免：访问对象属性
function createUser2(user) {
    return {
        name: user.name,
        age: user.age,
        email: user.email
    };
}
```

## 练习

1. **默认参数**：编写一个函数，使用默认参数为 `name` 和 `age` 设置默认值。

2. **剩余参数**：编写一个函数，使用剩余参数接收多个数字，并计算它们的总和。

3. **参数解构**：编写一个函数，使用对象参数解构接收用户信息（name、age、email）。

4. **默认参数与剩余参数**：编写一个函数，结合使用默认参数和剩余参数。

5. **参数解构与默认值**：编写一个函数，使用参数解构和默认值处理配置对象。

完成以上练习后，继续学习下一节，了解作用域和闭包。

## 总结

函数参数提供了灵活的参数处理方式。主要要点：

- 默认参数：为参数提供默认值
- 剩余参数：接收多个参数
- 参数解构：从对象或数组中提取值
- 使用默认参数简化代码
- 使用剩余参数替代 arguments
- 参数解构提高可读性

继续学习下一节，了解作用域和闭包。
