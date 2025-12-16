# 2.2.1 变量声明（let、const）

## 概述

变量是存储数据的容器。本节介绍如何使用 `let` 和 `const` 声明变量，以及变量命名规则和最佳实践。

## let 声明

### 基本语法

```js
// 声明变量
let x;

// 声明并初始化
let y = 10;

// 声明多个变量
let a = 1, b = 2, c = 3;
```

### 特点

1. **块级作用域**：`let` 声明的变量只在当前块中有效
2. **不能重复声明**：同一作用域内不能重复声明
3. **暂时性死区**：声明前无法访问
4. **可以重新赋值**：可以修改变量的值

### 示例

```js
// 块级作用域
{
    let x = 10;
    console.log(x); // 10
}
// console.log(x); // ReferenceError: x is not defined

// 不能重复声明
let y = 10;
// let y = 20; // SyntaxError: Identifier 'y' has already been declared

// 可以重新赋值
let z = 10;
z = 20;
console.log(z); // 20
```

## const 声明

### 基本语法

```js
// 声明常量（必须初始化）
const PI = 3.14159;

// 声明多个常量
const MAX_SIZE = 100, MIN_SIZE = 1;
```

### 特点

1. **块级作用域**：与 `let` 相同
2. **不能重复声明**：与 `let` 相同
3. **暂时性死区**：与 `let` 相同
4. **不能重新赋值**：常量一旦赋值，不能修改
5. **必须初始化**：声明时必须赋值

### 示例

```js
// 必须初始化
// const x; // SyntaxError: Missing initializer in const declaration

// 不能重新赋值
const PI = 3.14159;
// PI = 3.14; // TypeError: Assignment to constant variable

// 块级作用域
{
    const x = 10;
    console.log(x); // 10
}
// console.log(x); // ReferenceError
```

## 变量命名规则

### 基本规则

1. **必须以字母、下划线或美元符号开头**
2. **可以包含字母、数字、下划线和美元符号**
3. **区分大小写**
4. **不能使用保留字**

### 合法命名

```js
let userName = "John";
let _private = "secret";
let $element = document.getElementById("id");
let user123 = "user";
let user_name = "John";
```

### 非法命名

```js
// let 123user = "user";     // 不能以数字开头
// let user-name = "John";   // 不能使用连字符
// let let = "value";        // 不能使用保留字
// let class = "value";      // 不能使用保留字
```

### 命名约定

#### 驼峰命名（camelCase）

```js
let userName = "John";
let userAge = 30;
let isActive = true;
```

#### 常量命名（UPPER_SNAKE_CASE）

```js
const MAX_RETRIES = 3;
const API_BASE_URL = "https://api.example.com";
const DEFAULT_TIMEOUT = 5000;
```

#### 私有变量（下划线前缀）

```js
let _privateData = "secret";
let _internalCounter = 0;
```

## 变量声明的最佳实践

### 1. 优先使用 const

```js
// 好的做法：优先使用 const
const PI = 3.14159;
const MAX_SIZE = 100;

// 只有在需要重新赋值时才使用 let
let counter = 0;
counter++;
```

### 2. 使用有意义的名称

```js
// 好的做法：有意义的名称
let userCount = 10;
let isLoggedIn = true;
let currentUser = null;

// 不好的做法：无意义的名称
let x = 10;
let flag = true;
let temp = null;
```

### 3. 避免使用 var

```js
// 不好的做法：使用 var
var x = 10;

// 好的做法：使用 let 或 const
let x = 10;
const y = 20;
```

### 4. 声明时初始化

```js
// 好的做法：声明时初始化
let userName = "John";
let userAge = 30;

// 避免：先声明后赋值（除非必要）
let userName;
userName = "John";
```

### 5. 一行一个声明

```js
// 好的做法：一行一个声明
let userName = "John";
let userAge = 30;
let isActive = true;

// 避免：一行多个声明（除非相关）
let userName = "John", userAge = 30, isActive = true;
```

## 变量作用域

### 块级作用域

```js
{
    let x = 10;
    const y = 20;
    console.log(x, y); // 10 20
}
// console.log(x, y); // ReferenceError
```

### 函数作用域

```js
function greet() {
    let message = "Hello";
    const name = "World";
    console.log(message, name); // Hello World
}
// console.log(message, name); // ReferenceError
```

### 全局作用域

```js
// 在全局作用域中声明
let globalVar = "global";
const GLOBAL_CONST = "constant";

function test() {
    console.log(globalVar);    // "global"
    console.log(GLOBAL_CONST); // "constant"
}
```

## 变量提升

### let 和 const 的变量提升

`let` 和 `const` 也会被提升，但在赋值前无法访问（暂时性死区）：

```js
// 暂时性死区
console.log(x); // ReferenceError: Cannot access 'x' before initialization
let x = 10;
```

## 练习

1. **let 声明**：使用 `let` 声明变量，修改变量值，理解可变性。

2. **const 声明**：使用 `const` 声明常量，尝试修改常量，观察结果。

3. **块级作用域**：在块级作用域中声明变量，演示块级作用域的特性。

4. **变量命名**：遵循命名规则，使用有意义的变量名。

5. **变量初始化**：在声明时初始化变量，理解最佳实践。

完成以上练习后，继续学习下一节，了解 `var` 的问题和暂时性死区。

## 总结

掌握 `let` 和 `const` 的使用是 JavaScript 开发的基础。主要要点：

- 使用 `let` 声明可变变量
- 使用 `const` 声明常量
- 遵循命名规则和约定
- 优先使用 `const`
- 使用有意义的名称
- 避免使用 `var`

继续学习下一节，了解 `var` 的问题和暂时性死区。
