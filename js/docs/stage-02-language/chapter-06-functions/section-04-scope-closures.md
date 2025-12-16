# 2.6.4 作用域与闭包

## 概述

闭包是 JavaScript 中的重要概念，允许函数访问外部作用域的变量。本节介绍作用域链、闭包的概念和应用。

## 作用域链

### 变量查找

```js
let global = "global";

function outer() {
    let outer = "outer";
    
    function inner() {
        let inner = "inner";
        // 查找顺序：inner -> outer -> global
        console.log(inner);  // "inner"
        console.log(outer);  // "outer"
        console.log(global); // "global"
    }
    
    inner();
}

outer();
```

## 闭包

### 基本概念

闭包是函数能够访问外部作用域变量的特性：

```js
function outer() {
    let outerVar = "outer";
    
    function inner() {
        console.log(outerVar); // 访问外部变量
    }
    
    return inner;
}

const innerFunc = outer();
innerFunc(); // "outer"
```

### 闭包保持变量

```js
function createCounter() {
    let count = 0;
    
    return function() {
        return ++count;
    };
}

const counter = createCounter();
console.log(counter()); // 1
console.log(counter()); // 2
console.log(counter()); // 3
```

## 闭包应用

### 1. 数据私有化

```js
function createBankAccount(initialBalance) {
    let balance = initialBalance;
    
    return {
        deposit: function(amount) {
            balance += amount;
            return balance;
        },
        withdraw: function(amount) {
            if (amount <= balance) {
                balance -= amount;
                return balance;
            }
            return "Insufficient funds";
        },
        getBalance: function() {
            return balance;
        }
    };
}

const account = createBankAccount(100);
console.log(account.getBalance()); // 100
account.deposit(50);
console.log(account.getBalance()); // 150
```

### 2. 函数工厂

```js
function createMultiplier(factor) {
    return function(x) {
        return x * factor;
    };
}

const double = createMultiplier(2);
const triple = createMultiplier(3);

console.log(double(5));  // 10
console.log(triple(5));  // 15
```

### 3. 回调函数

```js
function fetchData(url, callback) {
    // 模拟异步操作
    setTimeout(() => {
        const data = { url, result: "data" };
        callback(data);
    }, 1000);
}

function processData(data) {
    console.log("Processing:", data);
}

fetchData("/api/data", processData);
```

## 常见陷阱

### 循环中的闭包

```js
// 问题：所有函数共享同一个变量
for (var i = 0; i < 3; i++) {
    setTimeout(() => {
        console.log(i); // 3, 3, 3
    }, 100);
}

// 解决方案1：使用 let
for (let i = 0; i < 3; i++) {
    setTimeout(() => {
        console.log(i); // 0, 1, 2
    }, 100);
}

// 解决方案2：使用 IIFE
for (var i = 0; i < 3; i++) {
    (function(j) {
        setTimeout(() => {
            console.log(j); // 0, 1, 2
        }, 100);
    })(i);
}
```

## 最佳实践

### 1. 理解闭包的作用

```js
// 闭包保持对外部变量的引用
function createFunction() {
    let value = 10;
    return function() {
        return value;
    };
}

const func = createFunction();
console.log(func()); // 10
```

### 2. 避免内存泄漏

```js
// 注意：闭包会保持对外部变量的引用
function createHandler() {
    let largeData = new Array(1000000).fill(0);
    
    return function() {
        // 即使不使用 largeData，它也会被保持
        console.log("Handler");
    };
}

// 解决方案：不需要时清除引用
function createHandler2() {
    return function() {
        console.log("Handler");
    };
}
```

## 练习

1. **创建闭包**：编写一个函数，返回一个内部函数，内部函数访问外部函数的变量。

2. **数据私有化**：使用闭包实现一个计数器，外部无法直接访问计数值。

3. **函数工厂**：使用闭包创建一个函数工厂，生成不同功能的函数。

4. **循环中的闭包**：演示循环中闭包的问题，并使用正确的方式解决。

5. **模块模式**：使用闭包实现模块模式，创建私有变量和公共方法。

完成以上练习后，继续学习下一节，了解高阶函数。

## 总结

闭包是 JavaScript 中的重要特性。主要要点：

- 闭包允许函数访问外部作用域
- 闭包保持对外部变量的引用
- 用于数据私有化、函数工厂等场景
- 注意循环中的闭包陷阱
- 避免内存泄漏

继续学习下一节，了解高阶函数。
