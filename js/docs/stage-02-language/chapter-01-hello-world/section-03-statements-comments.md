# 2.1.3 语句与注释

## 概述

语句是 JavaScript 程序的基本执行单元，注释用于说明代码。本节介绍语句的规则、注释的用法和代码风格。

## 语句

### 什么是语句

语句（Statement）是执行特定操作的代码单元。JavaScript 程序由一系列语句组成。

### 语句的规则

#### 1. 语句以分号结尾（可选但推荐）

```js
// 使用分号（推荐）
console.log("Hello");
let x = 10;

// 不使用分号（也有效，但不推荐）
console.log("Hello")
let x = 10
```

**建议**：始终使用分号，避免潜在问题。

#### 2. 语句可以跨多行

```js
// 单行语句
let x = 10;

// 多行语句
let result = 
    10 + 
    20 + 
    30;
```

#### 3. 多个语句可以写在一行

```js
// 多个语句写在一行（不推荐，但有效）
let x = 10; let y = 20; let z = 30;
```

**建议**：每行只写一个语句，提高可读性。

### 语句的类型

#### 1. 声明语句

```js
// 变量声明
let x = 10;
const y = 20;
var z = 30;

// 函数声明
function greet() {
    return "Hello";
}

// 类声明
class User {
    constructor(name) {
        this.name = name;
    }
}
```

#### 2. 表达式语句

```js
// 赋值表达式
x = 10;
x += 5;

// 函数调用表达式
console.log("Hello");
greet();

// 自增/自减表达式
x++;
y--;
```

#### 3. 控制语句

```js
// 条件语句
if (x > 10) {
    console.log("x is greater than 10");
}

// 循环语句
for (let i = 0; i < 10; i++) {
    console.log(i);
}

// 跳转语句
return result;
break;
continue;
```

#### 4. 空语句

```js
// 空语句（什么都不做）
;

// 在循环中使用空语句
for (let i = 0; i < 10; i++);
```

### 语句块

使用花括号 `{}` 将多个语句组合成语句块：

```js
// 语句块
{
    let x = 10;
    let y = 20;
    let sum = x + y;
    console.log(sum);
}
```

## 注释

### 单行注释

使用 `//` 创建单行注释：

```js
// 这是单行注释
let x = 10; // 这是行尾注释

// 注释可以单独一行
// 也可以跟在代码后面
```

### 多行注释

使用 `/* */` 创建多行注释：

```js
/* 
 * 这是多行注释
 * 可以跨越多行
 * 用于说明复杂的代码逻辑
 */

/*
也可以不使用星号
这样写也是有效的
*/
```

### 文档注释（JSDoc）

使用 `/** */` 创建文档注释：

```js
/**
 * 计算两个数的和
 * @param {number} a - 第一个数
 * @param {number} b - 第二个数
 * @returns {number} 两个数的和
 */
function add(a, b) {
    return a + b;
}
```

### 注释的最佳实践

#### 1. 解释"为什么"，而非"是什么"

```js
// 好的注释：解释为什么
// 使用快速排序算法，因为数据量可能很大
function sortData(data) {
    // ...
}

// 不好的注释：只说明是什么
// 这是一个排序函数
function sortData(data) {
    // ...
}
```

#### 2. 注释复杂逻辑

```js
// 好的注释：解释复杂逻辑
// 计算斐波那契数列的第 n 项
// 使用动态规划避免重复计算
function fibonacci(n) {
    // ...
}
```

#### 3. 保持注释更新

```js
// 不好的做法：注释与代码不一致
// 这个函数返回用户的名字
function getUser() {
    return user.id; // 实际返回的是 ID，不是名字
}
```

#### 4. 避免过度注释

```js
// 不好的做法：注释过于明显
// 定义变量 x，值为 10
let x = 10;

// 好的做法：代码自解释
let userCount = 10;
```

## 代码风格

### 缩进

使用 2 个空格或 4 个空格进行缩进（推荐 2 个空格）：

```js
// 使用 2 个空格缩进（推荐）
function greet(name) {
  if (name) {
    return `Hello, ${name}!`;
  }
  return "Hello, World!";
}

// 使用 4 个空格缩进
function greet(name) {
    if (name) {
        return `Hello, ${name}!`;
    }
    return "Hello, World!";
}
```

### 换行

#### 长语句换行

```js
// 好的做法：长语句换行
let result = 
    calculateSum(a, b) + 
    calculateProduct(c, d) + 
    calculateDifference(e, f);

// 函数参数换行
function processData(
    userId,
    orderId,
    paymentMethod
) {
    // ...
}
```

#### 对象和数组换行

```js
// 对象换行
const user = {
    name: "John",
    age: 30,
    email: "john@example.com"
};

// 数组换行
const numbers = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
];
```

### 命名规范

#### 变量和函数

```js
// 使用驼峰命名（camelCase）
let userName = "John";
let userAge = 30;

function getUserName() {
    return userName;
}
```

#### 常量

```js
// 使用全大写，单词间用下划线分隔
const MAX_RETRIES = 3;
const API_BASE_URL = "https://api.example.com";
```

#### 类

```js
// 使用帕斯卡命名（PascalCase）
class UserProfile {
    constructor(name) {
        this.name = name;
    }
}
```

## 常见错误

### 错误 1：缺少分号导致的问题

```js
// 问题代码
let x = 10
[1, 2, 3].forEach(console.log)

// JavaScript 会解释为：
// let x = 10[1, 2, 3].forEach(console.log)
// 这会导致错误

// 正确的写法
let x = 10;
[1, 2, 3].forEach(console.log);
```

### 错误 2：注释中的代码

```js
// 不好的做法：注释掉大量代码
// function oldFunction() {
//     // 大量代码
// }

// 好的做法：使用版本控制管理代码历史
// 如果不再需要，直接删除
```

## 总结

掌握语句和注释的用法，有助于编写规范的代码。主要要点：

- 语句以分号结尾（推荐）
- 使用单行注释 `//` 和多行注释 `/* */`
- 使用 JSDoc 注释文档化函数
- 保持一致的代码风格
- 使用有意义的命名
- 避免常见错误

继续学习下一节，了解不同环境下的执行方式。
