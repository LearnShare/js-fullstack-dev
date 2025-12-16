# 2.3.4 类型转换（隐式与显式）

## 概述

类型转换是将值从一种类型转换为另一种类型的过程。JavaScript 支持隐式类型转换和显式类型转换。本节介绍类型转换的机制和规则。

## 显式类型转换

### 转换为字符串

```js
// String()
String(123);        // "123"
String(true);       // "true"
String(null);       // "null"
String(undefined);  // "undefined"

// toString()
(123).toString();   // "123"
true.toString();    // "true"
```

### 转换为数字

```js
// Number()
Number("123");      // 123
Number("12.34");    // 12.34
Number("");         // 0
Number("abc");      // NaN
Number(true);       // 1
Number(false);      // 0
Number(null);       // 0
Number(undefined);  // NaN

// parseInt()
parseInt("123");    // 123
parseInt("12.34");  // 12
parseInt("abc");    // NaN

// parseFloat()
parseFloat("12.34"); // 12.34
parseFloat("12.3abc"); // 12.3
```

### 转换为布尔值

```js
// Boolean()
Boolean(1);         // true
Boolean(0);         // false
Boolean("");        // false
Boolean("hello");   // true
Boolean(null);      // false
Boolean(undefined); // false
Boolean([]);        // true
Boolean({});        // true

// 双重否定
!!1;        // true
!!0;        // false
!!"hello";  // true
```

## 隐式类型转换

### 字符串拼接

```js
// + 运算符用于字符串拼接
"Hello" + " World";     // "Hello World"
"Number: " + 123;       // "Number: 123"
123 + "456";            // "123456"
```

### 数学运算

```js
// 数学运算会转换为数字
"10" - 5;        // 5
"10" * 2;        // 20
"10" / 2;        // 5
"10" % 3;        // 1

// 但 + 运算符特殊
"10" + 5;        // "105"（字符串拼接）
```

### 比较运算

```js
// == 会进行类型转换
"5" == 5;        // true
null == undefined; // true
0 == false;      // true
"" == false;     // true

// === 不进行类型转换
"5" === 5;       // false
null === undefined; // false
```

### 逻辑运算

```js
// && 和 || 会进行类型转换
"hello" && "world"; // "world"
"" || "default";     // "default"
0 && "value";        // 0
null || "default";   // "default"
```

## 类型转换规则

### ToString

```js
String(123);        // "123"
String(true);       // "true"
String(null);       // "null"
String(undefined);  // "undefined"
String({});         // "[object Object]"
String([]);         // ""
```

### ToNumber

```js
Number("123");      // 123
Number("");         // 0
Number("abc");      // NaN
Number(true);       // 1
Number(false);      // 0
Number(null);       // 0
Number(undefined);  // NaN
```

### ToBoolean

```js
// 假值（falsy）
Boolean(false);     // false
Boolean(0);         // false
Boolean("");        // false
Boolean(null);       // false
Boolean(undefined); // false
Boolean(NaN);       // false

// 真值（truthy）
Boolean(true);      // true
Boolean(1);         // true
Boolean("hello");   // true
Boolean([]);        // true
Boolean({});        // true
```

## 常见陷阱

### 陷阱 1：+ 运算符

```js
// + 运算符的特殊行为
1 + 2;          // 3（数字相加）
"1" + 2;        // "12"（字符串拼接）
1 + "2";        // "12"（字符串拼接）
"1" + "2";      // "12"（字符串拼接）

// 解决方案：显式转换
Number("1") + Number("2"); // 3
String(1) + String(2);     // "12"
```

### 陷阱 2：== vs ===

```js
// == 会进行类型转换
"5" == 5;       // true
0 == false;     // true
"" == false;    // true

// === 不进行类型转换（推荐）
"5" === 5;      // false
0 === false;    // false
"" === false;   // false
```

### 陷阱 3：数组转换

```js
// 数组转换为字符串
String([1, 2, 3]);     // "1,2,3"
[1, 2, 3] + "";        // "1,2,3"

// 数组转换为数字
Number([1]);           // 1
Number([1, 2]);        // NaN
Number([]);            // 0
```

## 最佳实践

### 1. 使用显式转换

```js
// 好的做法：显式转换
let num = Number("123");
let str = String(123);
let bool = Boolean(value);

// 避免：隐式转换
let num = "123" - 0; // 不推荐
```

### 2. 使用严格相等

```js
// 好的做法：使用 ===
if (value === 10) { }

// 避免：使用 ==
if (value == 10) { } // 可能有意外的类型转换
```

### 3. 理解转换规则

```js
// 理解类型转换规则
String(null);      // "null"
String(undefined); // "undefined"
Number(null);      // 0
Number(undefined); // NaN
```

## 练习

1. **显式转换**：使用 `String()`、`Number()`、`Boolean()` 进行显式类型转换。

2. **隐式转换**：演示在运算和比较中的隐式类型转换，理解转换规则。

3. **+ 运算符陷阱**：演示 `+` 运算符的类型转换行为，区分字符串拼接和数字相加。

4. **== vs ===**：对比 `==` 和 `===` 的行为，理解类型转换的影响。

5. **数组转换**：演示数组在类型转换中的行为，理解 `toString()` 和 `join()` 的区别。

完成以上练习后，继续学习下一章：运算符与表达式。

## 总结

类型转换是 JavaScript 中的重要概念。主要要点：

- 显式转换：使用 String()、Number()、Boolean()
- 隐式转换：在运算和比较中自动发生
- 理解转换规则：ToString、ToNumber、ToBoolean
- 注意陷阱：+ 运算符、== vs ===、数组转换
- 使用显式转换和严格相等

完成本章学习后，继续学习下一章：运算符与表达式。
