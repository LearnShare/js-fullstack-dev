# 2.6.1 函数声明与表达式

## 概述

函数是 JavaScript 中的一等公民，可以声明、赋值、传递和返回。本节介绍函数声明和函数表达式的区别和使用。

## 函数声明

### 基本语法

```js
function functionName(parameters) {
    // 函数体
    return value;
}
```

### 示例

```js
function greet(name) {
    return `Hello, ${name}!`;
}

let message = greet("World");
console.log(message); // "Hello, World!"
```

### 函数提升

```js
// 函数声明会被提升
greet("World"); // "Hello, World!"（可以调用）

function greet(name) {
    return `Hello, ${name}!`;
}
```

## 函数表达式

### 基本语法

```js
const functionName = function(parameters) {
    // 函数体
    return value;
};
```

### 示例

```js
const greet = function(name) {
    return `Hello, ${name}!`;
};

let message = greet("World");
console.log(message); // "Hello, World!"
```

### 函数表达式不提升

```js
// 函数表达式不会被提升
// greet("World"); // TypeError: greet is not a function

const greet = function(name) {
    return `Hello, ${name}!`;
};
```

## 匿名函数

### 作为参数

```js
// 匿名函数作为参数
setTimeout(function() {
    console.log("Hello");
}, 1000);
```

### 立即执行函数（IIFE）

```js
// 立即执行函数表达式
(function() {
    console.log("Hello");
})();

// 带参数的 IIFE
(function(name) {
    console.log(`Hello, ${name}!`);
})("World");
```

## 命名函数表达式

### 基本语法

```js
const functionName = function innerName(parameters) {
    // 函数体
};
```

### 示例

```js
const factorial = function fact(n) {
    if (n <= 1) return 1;
    return n * fact(n - 1); // 使用内部名称递归
};

console.log(factorial(5)); // 120
```

## 函数声明 vs 函数表达式

### 提升差异

```js
// 函数声明：会被提升
greet(); // "Hello"

function greet() {
    console.log("Hello");
}

// 函数表达式：不会被提升
// greet2(); // TypeError

const greet2 = function() {
    console.log("Hello");
};
```

### 使用场景

```js
// 函数声明：适合主要功能
function calculateTotal(items) {
    return items.reduce((sum, item) => sum + item.price, 0);
}

// 函数表达式：适合回调、条件函数
const handler = function(event) {
    console.log(event);
};

// 条件函数
let process;
if (condition) {
    process = function() {
        console.log("A");
    };
} else {
    process = function() {
        console.log("B");
    };
}
```

## 函数作为值

### 赋值给变量

```js
function greet() {
    return "Hello";
}

let sayHello = greet;
console.log(sayHello()); // "Hello"
```

### 作为参数传递

```js
function process(callback) {
    return callback(10);
}

function double(x) {
    return x * 2;
}

let result = process(double);
console.log(result); // 20
```

### 作为返回值

```js
function createMultiplier(factor) {
    return function(x) {
        return x * factor;
    };
}

let double = createMultiplier(2);
console.log(double(5)); // 10
```

## 最佳实践

### 1. 选择合适的方式

```js
// 主要功能：使用函数声明
function mainFunction() {
    // ...
}

// 回调、条件函数：使用函数表达式
const callback = function() {
    // ...
};
```

### 2. 使用有意义的名称

```js
// 好的做法：有意义的名称
function calculateTotal(items) { }
const handleClick = function() { }

// 避免：无意义的名称
function func() { }
const fn = function() { }
```

### 3. 避免函数提升的陷阱

```js
// 注意：函数声明会被提升
if (true) {
    function test() {
        return "A";
    }
} else {
    function test() {
        return "B";
    }
}

// 使用函数表达式避免问题
let test;
if (true) {
    test = function() {
        return "A";
    };
} else {
    test = function() {
        return "B";
    };
}
```

## 练习

1. **函数声明**：编写一个函数声明，计算两个数的和，并调用它。

2. **函数表达式**：编写一个函数表达式，计算两个数的乘积，并调用它。

3. **函数提升**：演示函数声明的提升行为，在函数声明之前调用函数。

4. **函数作为值**：将函数赋值给变量，并将函数作为参数传递给另一个函数。

5. **条件函数**：根据条件使用函数表达式创建不同的函数。

完成以上练习后，继续学习下一节，了解箭头函数。

## 总结

函数声明和函数表达式是定义函数的两种方式。主要要点：

- 函数声明：会被提升，适合主要功能
- 函数表达式：不会被提升，适合回调、条件函数
- 函数是一等公民，可以作为值传递
- 选择合适的方式定义函数
- 使用有意义的函数名称

继续学习下一节，了解箭头函数。
