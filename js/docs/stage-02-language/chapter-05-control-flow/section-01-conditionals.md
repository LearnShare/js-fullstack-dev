# 2.5.1 条件语句（if、else、switch）

## 概述

条件语句用于根据条件执行不同的代码。JavaScript 提供了 if、else if、else 和 switch 语句。本节介绍这些条件语句的使用方法。

## if 语句

### 基本语法

```js
if (condition) {
    // 代码块
}
```

### 示例

```js
let age = 18;

if (age >= 18) {
    console.log("成年人");
}
```

### 单行语句

```js
// 单行语句可以省略花括号（不推荐）
if (age >= 18) console.log("成年人");

// 推荐：始终使用花括号
if (age >= 18) {
    console.log("成年人");
}
```

## if...else 语句

### 基本语法

```js
if (condition) {
    // 条件为真时执行
} else {
    // 条件为假时执行
}
```

### 示例

```js
let age = 16;

if (age >= 18) {
    console.log("成年人");
} else {
    console.log("未成年人");
}
```

## if...else if...else 语句

### 基本语法

```js
if (condition1) {
    // 条件1为真时执行
} else if (condition2) {
    // 条件2为真时执行
} else {
    // 所有条件都为假时执行
}
```

### 示例

```js
let score = 85;

if (score >= 90) {
    console.log("优秀");
} else if (score >= 80) {
    console.log("良好");
} else if (score >= 60) {
    console.log("及格");
} else {
    console.log("不及格");
}
```

## switch 语句

### 基本语法

```js
switch (expression) {
    case value1:
        // 代码块
        break;
    case value2:
        // 代码块
        break;
    default:
        // 默认代码块
}
```

### 示例

```js
let day = 1;

switch (day) {
    case 1:
        console.log("星期一");
        break;
    case 2:
        console.log("星期二");
        break;
    case 3:
        console.log("星期三");
        break;
    default:
        console.log("其他");
}
```

### break 语句

```js
// 没有 break 会继续执行下一个 case
let day = 1;

switch (day) {
    case 1:
        console.log("星期一");
        // 没有 break，继续执行
    case 2:
        console.log("星期二");
        break;
}
// 输出：星期一 星期二
```

### 多个 case 共享代码

```js
let month = 2;

switch (month) {
    case 1:
    case 3:
    case 5:
    case 7:
    case 8:
    case 10:
    case 12:
        console.log("31天");
        break;
    case 4:
    case 6:
    case 9:
    case 11:
        console.log("30天");
        break;
    case 2:
        console.log("28或29天");
        break;
}
```

## 三元运算符

### 基本语法

```js
condition ? valueIfTrue : valueIfFalse
```

### 示例

```js
let age = 18;
let status = age >= 18 ? "成年人" : "未成年人";
console.log(status); // "成年人"
```

### 嵌套三元运算符

```js
let score = 85;
let grade = score >= 90 ? "优秀" : 
            score >= 80 ? "良好" : 
            score >= 60 ? "及格" : "不及格";
console.log(grade); // "良好"
```

## 条件表达式

### 真值和假值

```js
// 假值：false、0、""、null、undefined、NaN
if (0) {
    console.log("不会执行");
}

// 真值：其他所有值
if (1) {
    console.log("会执行");
}

if ("hello") {
    console.log("会执行");
}
```

### 逻辑运算符在条件中

```js
// 使用 && 和 ||
if (user && user.isAdmin) {
    console.log("管理员");
}

if (name || "Guest") {
    console.log(name || "Guest");
}
```

## 最佳实践

### 1. 使用严格相等

```js
// 好的做法：使用 ===
if (value === 10) { }

// 避免：使用 ==
if (value == 10) { }
```

### 2. 简化条件

```js
// 好的做法：简化条件
if (user && user.name) {
    console.log(user.name);
}

// 避免：嵌套过深
if (user) {
    if (user.name) {
        console.log(user.name);
    }
}
```

### 3. 早期返回

```js
// 好的做法：早期返回
function processUser(user) {
    if (!user) return;
    if (!user.name) return;
    
    // 处理用户
}

// 避免：嵌套过深
function processUser2(user) {
    if (user) {
        if (user.name) {
            // 处理用户
        }
    }
}
```

### 4. switch vs if...else

```js
// switch 适合多个固定值
switch (day) {
    case 1: case 2: case 3:
        // ...
}

// if...else 适合范围判断
if (score >= 90) {
    // ...
} else if (score >= 80) {
    // ...
}
```

## 练习

1. **if...else 语句**：编写一个函数，根据年龄判断是否为成年人，使用 if...else 语句。

2. **if...else if...else**：编写一个函数，根据分数判断等级（A、B、C、D、F）。

3. **switch 语句**：编写一个函数，根据星期几返回对应的活动安排，使用 switch 语句。

4. **三元运算符**：使用三元运算符简化条件判断，根据条件返回不同的值。

5. **嵌套条件**：编写一个函数，处理嵌套的条件判断，使用早期返回简化代码。

完成以上练习后，继续学习下一节，了解循环结构。

## 总结

条件语句是控制程序流程的基础。主要要点：

- if、else if、else：基本条件语句
- switch：多值选择语句
- 三元运算符：简单的条件表达式
- 使用严格相等（===）
- 简化条件表达式
- 使用早期返回减少嵌套

继续学习下一节，了解循环结构。
