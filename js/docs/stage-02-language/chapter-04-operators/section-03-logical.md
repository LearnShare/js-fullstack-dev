# 2.4.3 逻辑运算符（&&、||、!）

## 概述

逻辑运算符用于执行逻辑运算。JavaScript 的逻辑运算符具有短路特性，可以用于条件判断和默认值设置。本节介绍逻辑运算符的使用和特性。

## 逻辑与（&&）

### 基本用法

```js
// 逻辑与：两个操作数都为真时返回 true
true && true;     // true
true && false;    // false
false && true;    // false
false && false;   // false
```

### 短路特性

```js
// && 的短路特性：如果第一个操作数为假，不执行第二个操作数
false && console.log("不会执行"); // false

// 如果第一个操作数为真，返回第二个操作数的值
true && "hello";  // "hello"
false && "hello"; // false
```

### 实际应用

```js
// 条件执行
user && user.name && console.log(user.name);

// 默认值设置
const name = user && user.name || "Guest";

// 条件赋值
const value = condition && result;
```

## 逻辑或（||）

### 基本用法

```js
// 逻辑或：至少一个操作数为真时返回 true
true || true;     // true
true || false;    // true
false || true;    // true
false || false;   // false
```

### 短路特性

```js
// || 的短路特性：如果第一个操作数为真，不执行第二个操作数
true || console.log("不会执行"); // true

// 如果第一个操作数为假，返回第二个操作数的值
false || "hello"; // "hello"
true || "hello";  // true
```

### 实际应用

```js
// 默认值设置
const name = userName || "Guest";
const port = process.env.PORT || 3000;

// 条件执行
error || console.log("No error");

// 多值选择
const value = option1 || option2 || option3 || "default";
```

## 逻辑非（!）

### 基本用法

```js
// 逻辑非：取反
!true;            // false
!false;           // true
!0;               // true
!1;               // false
!"";              // true
!"hello";         // false
```

### 双重否定（!!）

```js
// 双重否定：转换为布尔值
!!0;              // false
!!1;              // true
!!"";             // false
!!"hello";        // true
!!null;           // false
!!undefined;      // false
```

## 真值和假值

### 假值（Falsy）

```js
// 以下值在逻辑运算中被视为假
false
0
-0
0n
""
null
undefined
NaN

// 检查假值
!false;           // true
!0;               // true
!"";              // true
!null;            // true
!undefined;       // true
!NaN;             // true
```

### 真值（Truthy）

```js
// 除了假值之外的所有值都是真值
true
1
-1
"hello"
[]
{}
function(){}

// 检查真值
!!true;           // true
!!1;              // true
!!"hello";        // true
!![];             // true
!!{};             // true
```

## 实际应用

### 1. 条件执行

```js
// 使用 && 进行条件执行
user && user.isAdmin && deleteUser(user.id);

// 使用 || 进行条件执行
error || handleError(error);
```

### 2. 默认值设置

```js
// 使用 || 设置默认值
const name = userName || "Guest";
const port = process.env.PORT || 3000;
const config = userConfig || defaultConfig;
```

### 3. 条件赋值

```js
// 使用 && 进行条件赋值
const result = condition && value;

// 使用 || 进行多值选择
const value = option1 || option2 || "default";
```

### 4. 类型检查

```js
// 检查变量是否存在
if (user && user.name) {
    console.log(user.name);
}

// 检查数组是否为空
if (items && items.length > 0) {
    processItems(items);
}
```

## 运算符优先级

```js
// && 的优先级高于 ||
true || false && false;  // true（等价于 true || (false && false)）

// 使用括号明确优先级
(true || false) && false; // false
```

## 最佳实践

### 1. 使用 || 设置默认值

```js
// 好的做法
const name = userName || "Guest";
const port = process.env.PORT || 3000;

// 避免
const name = userName ? userName : "Guest";
```

### 2. 使用 && 进行条件执行

```js
// 好的做法
user && user.isAdmin && deleteUser(user.id);

// 避免
if (user && user.isAdmin) {
    deleteUser(user.id);
}
```

### 3. 注意假值陷阱

```js
// 注意：0、""、false 也是假值
const count = 0;
const result = count || 10; // 10（可能不是期望的结果）

// 使用空值合并运算符（??）
const result2 = count ?? 10; // 0（只检查 null 和 undefined）
```

## 练习

1. **逻辑与**：使用 `&&` 运算符实现条件执行，理解短路特性。

2. **逻辑或**：使用 `||` 运算符设置默认值，理解短路特性。

3. **逻辑非**：使用 `!` 运算符进行取反操作，理解真值和假值。

4. **组合使用**：组合使用逻辑运算符实现复杂的条件判断。

5. **假值陷阱**：演示假值陷阱，理解 `||` 和 `??` 的区别。

完成以上练习后，继续学习下一节，了解现代运算符。

## 总结

逻辑运算符是 JavaScript 中的重要工具。主要要点：

- &&：逻辑与，具有短路特性
- ||：逻辑或，具有短路特性
- !：逻辑非，取反操作
- 理解真值和假值
- 使用 || 设置默认值
- 使用 && 进行条件执行
- 注意假值陷阱

继续学习下一节，了解现代运算符。
