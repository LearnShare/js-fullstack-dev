# 2.2.4 作用域（全局、函数、块级）

## 概述

作用域（Scope）决定了变量的可访问范围。JavaScript 有三种主要的作用域：全局作用域、函数作用域和块级作用域。本节详细介绍这些作用域的概念和使用。

## 什么是作用域

### 定义

作用域是变量、函数和对象的可访问范围。在作用域内定义的变量，只能在该作用域及其子作用域中访问。

### 作用域的作用

1. **变量隔离**：不同作用域的变量互不干扰
2. **命名空间**：避免变量名冲突
3. **内存管理**：作用域结束后，变量可以被垃圾回收

## 全局作用域

### 定义

全局作用域是最外层的作用域，在函数和块之外定义的变量属于全局作用域。

### 全局变量

```js
// 全局作用域
let globalVar = "global";
const GLOBAL_CONST = "constant";

function test() {
    console.log(globalVar);    // "global"
    console.log(GLOBAL_CONST);  // "constant"
}

test();
console.log(globalVar); // "global"
```

### 全局对象

在浏览器中，全局作用域的变量会成为 `window` 对象的属性：

```js
// 浏览器环境
var globalVar = "global";
console.log(window.globalVar); // "global"

// let 和 const 不会
let globalLet = "global";
console.log(window.globalLet); // undefined
```

在 Node.js 中，全局作用域的变量不会自动成为 `global` 对象的属性：

```js
// Node.js 环境
var globalVar = "global";
console.log(global.globalVar); // undefined（需要显式赋值）

global.globalVar = "global";
console.log(global.globalVar); // "global"
```

### 避免全局变量污染

```js
// 不好的做法：创建大量全局变量
var x = 10;
var y = 20;
var z = 30;

// 好的做法：使用对象封装
const App = {
    x: 10,
    y: 20,
    z: 30
};

// 或使用模块
// module.js
export const x = 10;
export const y = 20;
```

## 函数作用域

### 定义

函数作用域是函数内部的作用域，在函数内定义的变量只能在该函数内访问。

### 函数作用域变量

```js
function test() {
    // 函数作用域
    let functionVar = "function";
    const functionConst = "constant";
    
    console.log(functionVar);   // "function"
    console.log(functionConst);  // "constant"
}

test();
// console.log(functionVar); // ReferenceError: functionVar is not defined
```

### var 的函数作用域

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
    // console.log(y); // ReferenceError
}
```

### 嵌套函数

```js
function outer() {
    let outerVar = "outer";
    
    function inner() {
        let innerVar = "inner";
        console.log(outerVar); // "outer"（可以访问外部变量）
        console.log(innerVar); // "inner"
    }
    
    inner();
    // console.log(innerVar); // ReferenceError
}

outer();
```

## 块级作用域

### 定义

块级作用域是由 `{}` 创建的作用域，`let` 和 `const` 声明的变量具有块级作用域。

### 块级作用域变量

```js
{
    // 块级作用域
    let blockVar = "block";
    const blockConst = "constant";
    
    console.log(blockVar);   // "block"
    console.log(blockConst); // "constant"
}

// console.log(blockVar);   // ReferenceError
// console.log(blockConst); // ReferenceError
```

### if 语句中的块级作用域

```js
if (true) {
    let x = 10;
    const y = 20;
    console.log(x, y); // 10 20
}
// console.log(x, y); // ReferenceError

// var 不是块级作用域
if (true) {
    var z = 30;
}
console.log(z); // 30（可以访问）
```

### for 循环中的块级作用域

```js
// let 在每次迭代中创建新的作用域
for (let i = 0; i < 3; i++) {
    setTimeout(() => {
        console.log(i); // 0, 1, 2
    }, 100);
}

// var 在函数作用域中
for (var j = 0; j < 3; j++) {
    setTimeout(() => {
        console.log(j); // 3, 3, 3
    }, 100);
}
```

## 作用域链

### 定义

作用域链是 JavaScript 查找变量的机制。当访问一个变量时，JavaScript 会从当前作用域开始，逐级向上查找，直到找到变量或到达全局作用域。

### 作用域链示例

```js
let globalVar = "global";

function outer() {
    let outerVar = "outer";
    
    function inner() {
        let innerVar = "inner";
        
        // 查找顺序：inner -> outer -> global
        console.log(innerVar); // "inner"（当前作用域）
        console.log(outerVar); // "outer"（外部作用域）
        console.log(globalVar); // "global"（全局作用域）
    }
    
    inner();
}

outer();
```

### 变量遮蔽

```js
let x = "global";

function test() {
    let x = "local";
    console.log(x); // "local"（局部变量遮蔽全局变量）
}

test();
console.log(x); // "global"（全局变量未改变）
```

## 作用域与闭包

### 闭包基础

闭包是函数能够访问其外部作用域变量的特性：

```js
function outer() {
    let outerVar = "outer";
    
    function inner() {
        console.log(outerVar); // 可以访问外部变量
    }
    
    return inner;
}

const innerFunc = outer();
innerFunc(); // "outer"
```

## 最佳实践

### 1. 避免全局变量

```js
// 不好的做法
var globalVar = "global";

// 好的做法：使用模块或对象封装
const App = {
    config: {
        apiUrl: "https://api.example.com"
    }
};
```

### 2. 使用块级作用域

```js
// 好的做法：使用块级作用域限制变量作用范围
{
    let temp = calculateValue();
    process(temp);
}
// temp 在这里不可访问
```

### 3. 理解作用域链

```js
// 理解变量查找顺序
let global = "global";

function outer() {
    let outer = "outer";
    
    function inner() {
        // 查找顺序：inner -> outer -> global
        console.log(outer);  // "outer"
        console.log(global);  // "global"
    }
    
    inner();
}
```

### 4. 避免变量遮蔽

```js
// 避免不必要的变量遮蔽
let userName = "global";

function processUser() {
    // 如果不需要遮蔽，使用不同的名称
    let localUserName = "local";
    // 或直接使用全局变量
    console.log(userName);
}
```

## 练习

1. **作用域演示**：创建全局、函数和块级作用域的变量，演示不同作用域的特性。

2. **作用域链**：创建嵌套函数，演示作用域链的变量查找机制。

3. **变量遮蔽**：演示变量遮蔽现象，理解内部变量如何遮蔽外部变量。

4. **块级作用域**：在 `if` 和 `for` 循环中使用块级作用域，理解块级作用域的优势。

5. **闭包基础**：创建闭包函数，演示函数如何访问外部作用域的变量。

完成以上练习后，继续学习下一章：数据类型。

## 总结

理解作用域是掌握 JavaScript 的关键。主要要点：

- 全局作用域：最外层作用域
- 函数作用域：函数内部的作用域
- 块级作用域：由 `{}` 创建的作用域
- 作用域链：变量查找机制
- 变量遮蔽：内部变量遮蔽外部变量
- 避免全局变量污染
- 使用块级作用域限制变量作用范围

完成本章学习后，继续学习下一章：数据类型。
