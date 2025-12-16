# 2.4.2 比较运算符（=== vs ==）

## 概述

比较运算符用于比较两个值。JavaScript 提供了严格相等（===）和相等（==）两种比较方式。本节详细介绍它们的区别和使用场景。

## 严格相等（===）

### 基本用法

```js
// 严格相等：类型和值都必须相同
10 === 10;        // true
"10" === 10;      // false（类型不同）
10 === "10";      // false（类型不同）
true === true;    // true
null === null;    // true
undefined === undefined; // true
```

### 严格不相等（!==）

```js
// 严格不相等：类型或值不同
10 !== 10;        // false
"10" !== 10;      // true（类型不同）
10 !== "10";      // true（类型不同）
```

## 相等（==）

### 基本用法

```js
// 相等：会进行类型转换
10 == 10;         // true
"10" == 10;       // true（类型转换）
10 == "10";       // true（类型转换）
true == 1;        // true（类型转换）
false == 0;       // true（类型转换）
null == undefined; // true（特殊规则）
```

### 不相等（!=）

```js
// 不相等：会进行类型转换
10 != 10;         // false
"10" != 10;       // false（类型转换后相等）
10 != "10";       // false（类型转换后相等）
```

## 比较规则

### 严格相等规则

```js
// 1. 类型不同，返回 false
"10" === 10;      // false

// 2. 都是 null 或都是 undefined，返回 true
null === null;    // true
undefined === undefined; // true

// 3. 都是数字，按数值比较
10 === 10.0;      // true
NaN === NaN;      // false（特殊规则）

// 4. 都是字符串，按字符比较
"hello" === "hello"; // true

// 5. 都是布尔值，按值比较
true === true;    // true

// 6. 都是对象，按引用比较
{} === {};        // false（不同的引用）
let obj = {};
obj === obj;      // true（相同的引用）
```

### 相等规则（类型转换）

```js
// 1. null 和 undefined 相等
null == undefined; // true

// 2. 数字和字符串：字符串转换为数字
"10" == 10;       // true
"10" == 10.0;    // true

// 3. 布尔值转换为数字
true == 1;        // true
false == 0;       // true

// 4. 对象转换为原始值
[1, 2, 3] == "1,2,3"; // true
```

## 大小比较

### 大于（>）和小于（<）

```js
10 > 5;           // true
10 < 5;           // false
"10" > "5";       // true（字符串比较）
"10" > 5;         // true（字符串转换为数字）

// 字符串按字典序比较
"a" > "b";        // false
"abc" > "ab";     // true
```

### 大于等于（>=）和小于等于（<=）

```js
10 >= 10;         // true
10 <= 10;         // true
10 >= 5;          // true
10 <= 5;          // false
```

## 常见陷阱

### 陷阱 1：== 的类型转换

```js
// == 会进行意外的类型转换
"0" == false;     // true
0 == false;       // true
"" == false;      // true
null == undefined; // true

// 使用 === 避免这些问题
"0" === false;    // false
0 === false;      // false
"" === false;     // false
null === undefined; // false
```

### 陷阱 2：NaN 的比较

```js
// NaN 与任何值都不相等（包括自己）
NaN == NaN;       // false
NaN === NaN;      // false

// 检查 NaN
isNaN(NaN);           // true
Number.isNaN(NaN);    // true（推荐）
```

### 陷阱 3：对象的比较

```js
// 对象按引用比较
{} == {};         // false
{} === {};        // false

let obj1 = {};
let obj2 = obj1;
obj1 === obj2;    // true（相同的引用）
```

## 最佳实践

### 1. 始终使用 ===

```js
// 好的做法：使用 ===
if (value === 10) { }
if (value !== null) { }

// 避免：使用 ==
if (value == 10) { } // 可能有意外的类型转换
```

### 2. 特殊情况使用 ==

```js
// 只在需要类型转换时使用 ==
if (value == null) { } // 检查 null 或 undefined
// 等价于
if (value === null || value === undefined) { }
```

### 3. 检查 NaN

```js
// 使用 Number.isNaN() 检查 NaN
if (Number.isNaN(value)) { }

// 避免使用 == 或 === 检查 NaN
if (value === NaN) { } // 永远为 false
```

## 练习

1. **严格相等**：使用 `===` 和 `!==` 比较不同类型的值，理解严格相等的含义。

2. **相等运算符**：使用 `==` 和 `!=` 比较值，观察类型转换的行为。

3. **NaN 比较**：演示 NaN 的特殊比较行为，使用 `Number.isNaN()` 正确检查 NaN。

4. **对象比较**：比较对象引用，理解对象按引用比较的特性。

5. **实际应用**：编写函数使用比较运算符判断值的范围、类型等。

完成以上练习后，继续学习下一节，了解逻辑运算符。

## 总结

比较运算符是 JavaScript 中的重要工具。主要要点：

- 严格相等（===）：类型和值都必须相同
- 相等（==）：会进行类型转换
- 始终使用 === 避免意外的类型转换
- 注意 NaN 的特殊行为
- 对象按引用比较

继续学习下一节，了解逻辑运算符。
