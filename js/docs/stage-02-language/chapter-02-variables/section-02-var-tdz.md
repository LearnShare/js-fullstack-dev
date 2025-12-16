# 2.2.2 var 的问题与暂时性死区（TDZ）

## 概述

`var` 是 ES5 及之前版本的变量声明方式，存在一些问题。本节介绍 `var` 的问题、变量提升的概念，以及 `let` 和 `const` 的暂时性死区（Temporal Dead Zone, TDZ）。

## var 的问题

### 1. 函数作用域而非块级作用域

```js
// var 是函数作用域
function test() {
    if (true) {
        var x = 10;
    }
    console.log(x); // 10（在 if 块外仍可访问）
}

// let 是块级作用域
function test2() {
    if (true) {
        let y = 10;
    }
    console.log(y); // ReferenceError: y is not defined
}
```

### 2. 变量提升

```js
// var 会被提升到作用域顶部
console.log(x); // undefined（不会报错）
var x = 10;

// 等价于
var x;
console.log(x); // undefined
x = 10;
```

### 3. 可以重复声明

```js
// var 可以重复声明（不会报错）
var x = 10;
var x = 20;
console.log(x); // 20

// let 不能重复声明
let y = 10;
// let y = 20; // SyntaxError: Identifier 'y' has already been declared
```

### 4. 全局变量污染

```js
// var 在全局作用域中声明会创建全局对象属性
var globalVar = "global";
console.log(window.globalVar); // "global"（浏览器环境）

// let 不会
let globalLet = "global";
console.log(window.globalLet); // undefined
```

## 变量提升（Hoisting）

### var 的变量提升

`var` 声明的变量会被提升到作用域顶部，但赋值不会：

```js
// 代码
console.log(x);
var x = 10;

// 实际执行顺序
var x;           // 声明被提升
console.log(x);  // undefined
x = 10;          // 赋值留在原地
```

### 函数声明提升

函数声明也会被提升：

```js
// 函数声明会被提升
greet(); // "Hello"

function greet() {
    console.log("Hello");
}
```

### 函数表达式不提升

```js
// 函数表达式不会被提升
// greet(); // TypeError: greet is not a function

var greet = function() {
    console.log("Hello");
};
```

## 暂时性死区（TDZ）

### 什么是 TDZ

暂时性死区（Temporal Dead Zone, TDZ）是指从作用域开始到变量声明之间的区域，在这个区域内无法访问该变量。

### let 和 const 的 TDZ

```js
// TDZ 开始
console.log(x); // ReferenceError: Cannot access 'x' before initialization
// TDZ 结束
let x = 10;
```

### TDZ 的示例

```js
// 示例 1：基本 TDZ
{
    // TDZ 开始
    console.log(x); // ReferenceError
    let x = 10;
    // TDZ 结束
}

// 示例 2：函数中的 TDZ
function test() {
    console.log(x); // ReferenceError
    let x = 10;
}

// 示例 3：循环中的 TDZ
for (let i = 0; i < 3; i++) {
    // 每次迭代都有独立的 TDZ
    setTimeout(() => {
        console.log(i); // 0, 1, 2
    }, 100);
}
```

### TDZ 与 var 的对比

```js
// var：没有 TDZ
console.log(x); // undefined（不会报错）
var x = 10;

// let：有 TDZ
console.log(y); // ReferenceError
let y = 10;
```

## 常见问题

### 问题 1：循环中的 var

```js
// 问题代码
for (var i = 0; i < 3; i++) {
    setTimeout(() => {
        console.log(i); // 3, 3, 3（不是 0, 1, 2）
    }, 100);
}

// 解决方案：使用 let
for (let i = 0; i < 3; i++) {
    setTimeout(() => {
        console.log(i); // 0, 1, 2
    }, 100);
}
```

### 问题 2：条件声明

```js
// var 的问题
if (true) {
    var x = 10;
}
console.log(x); // 10（意外地可以访问）

// let 的正确行为
if (true) {
    let y = 10;
}
// console.log(y); // ReferenceError（正确行为）
```

### 问题 3：重复声明

```js
// var 允许重复声明（可能导致问题）
var x = 10;
var x = 20; // 不会报错，可能覆盖之前的声明

// let 不允许重复声明
let y = 10;
// let y = 20; // SyntaxError（正确的行为）
```

## 最佳实践

### 1. 避免使用 var

```js
// 不好的做法
var x = 10;
var y = 20;

// 好的做法
let x = 10;
const y = 20;
```

### 2. 使用 let 和 const

```js
// 优先使用 const
const PI = 3.14159;
const MAX_SIZE = 100;

// 需要重新赋值时使用 let
let counter = 0;
counter++;
```

### 3. 理解 TDZ

```js
// 理解 TDZ，避免在声明前访问变量
let x = 10; // 先声明
console.log(x); // 再使用
```

### 4. 使用块级作用域

```js
// 使用块级作用域限制变量作用范围
{
    let temp = calculateValue();
    process(temp);
}
// temp 在这里不可访问（正确）
```

## 练习

1. **var 的问题**：演示 var 在循环中的问题，使用 let 解决。

2. **暂时性死区**：演示 let 和 const 的 TDZ，在声明前访问变量观察错误。

3. **变量提升对比**：对比 var 和 let/const 的变量提升行为。

4. **重复声明**：尝试重复声明变量，观察 var 和 let/const 的区别。

5. **块级作用域**：在块级作用域中使用 let，理解与 var 的区别。

完成以上练习后，继续学习下一节，了解常量与引用类型的关系。

## 总结

理解 `var` 的问题和 TDZ 的概念，有助于编写更安全的代码。主要要点：

- `var` 存在函数作用域、变量提升、可重复声明等问题
- `let` 和 `const` 有块级作用域和 TDZ
- 避免使用 `var`，优先使用 `let` 和 `const`
- 理解 TDZ 的概念，避免在声明前访问变量

继续学习下一节，了解常量与引用类型的关系。
