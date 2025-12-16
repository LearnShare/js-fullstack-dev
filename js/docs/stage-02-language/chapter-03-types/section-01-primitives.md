# 2.3.1 原始类型（Primitives）

## 概述

原始类型（Primitives）是 JavaScript 中最基本的数据类型，包括 number、string、boolean、null、undefined、symbol 和 bigint。原始类型的值是不可变的。

## number（数字）

### 整数和浮点数

```js
// 整数
let integer = 10;
let negative = -5;

// 浮点数
let float = 3.14;
let scientific = 1.5e3; // 1500
```

### 特殊值

```js
// Infinity（无穷大）
let infinity = Infinity;
let negativeInfinity = -Infinity;

// NaN（Not a Number）
let notANumber = NaN;
console.log(typeof NaN); // "number"

// 检查 NaN
console.log(isNaN(NaN));        // true
console.log(Number.isNaN(NaN)); // true（推荐）
```

### 数值范围

```js
// 最大安全整数
console.log(Number.MAX_SAFE_INTEGER); // 9007199254740991

// 最小安全整数
console.log(Number.MIN_SAFE_INTEGER); // -9007199254740991

// 最大值
console.log(Number.MAX_VALUE); // 1.7976931348623157e+308

// 最小值
console.log(Number.MIN_VALUE); // 5e-324
```

## string（字符串）

### 字符串创建

```js
// 单引号
let str1 = 'Hello';

// 双引号
let str2 = "World";

// 模板字符串（ES6）
let name = "John";
let str3 = `Hello, ${name}!`;
```

### 字符串是不可变的

```js
let str = "Hello";
str[0] = "h"; // 无效，字符串不可变
console.log(str); // "Hello"（未改变）

// 需要创建新字符串
let newStr = "h" + str.slice(1);
console.log(newStr); // "hello"
```

### 字符串方法

```js
let str = "Hello, World!";

// 长度
console.log(str.length); // 13

// 索引访问
console.log(str[0]);     // "H"
console.log(str.charAt(0)); // "H"

// 查找
console.log(str.indexOf("World")); // 7
console.log(str.includes("World")); // true

// 截取
console.log(str.slice(0, 5)); // "Hello"
console.log(str.substring(0, 5)); // "Hello"

// 转换
console.log(str.toUpperCase()); // "HELLO, WORLD!"
console.log(str.toLowerCase()); // "hello, world!"
```

## boolean（布尔值）

### 布尔值

```js
let isTrue = true;
let isFalse = false;
```

### 真值和假值

```js
// 假值（falsy）
false
0
-0
0n
""
null
undefined
NaN

// 真值（truthy）
true
1
-1
"hello"
[]
{}
```

### 布尔转换

```js
// 显式转换
Boolean(1);        // true
Boolean(0);        // false
Boolean("");       // false
Boolean("hello");  // true

// 双重否定
!!1;        // true
!!0;        // false
```

## null 和 undefined

### null

```js
// null 表示空值
let value = null;
console.log(typeof value); // "object"（这是 JavaScript 的 bug）
```

### undefined

```js
// undefined 表示未定义
let value;
console.log(value);        // undefined
console.log(typeof value); // "undefined"
```

### 区别

```js
// null 是显式赋值的空值
let x = null;

// undefined 是未定义的值
let y;
console.log(y); // undefined

// 检查
console.log(x === null);      // true
console.log(y === undefined); // true
```

## symbol（符号）

### 创建 Symbol

```js
// 创建唯一的 Symbol
let sym1 = Symbol();
let sym2 = Symbol();
console.log(sym1 === sym2); // false

// 带描述的 Symbol
let sym3 = Symbol("description");
console.log(sym3.toString()); // "Symbol(description)"
```

### Symbol 作为属性键

```js
let sym = Symbol("key");
let obj = {
    [sym]: "value"
};
console.log(obj[sym]); // "value"
```

## bigint（大整数）

### 创建 BigInt

```js
// 使用 n 后缀
let bigInt1 = 9007199254740991n;

// 使用 BigInt() 函数
let bigInt2 = BigInt("9007199254740991");

// 不能混合使用
let num = 10;
let big = 20n;
// console.log(num + big); // TypeError
console.log(num + Number(big)); // 30
```

## 原始类型的特性

### 不可变性

```js
// 原始类型是不可变的
let str = "Hello";
str.toUpperCase(); // 返回新字符串，不修改原字符串
console.log(str); // "Hello"（未改变）

let num = 10;
num.toString(); // 返回新字符串，不修改原数字
console.log(num); // 10（未改变）
```

### 值比较

```js
// 原始类型按值比较
let a = 10;
let b = 10;
console.log(a === b); // true

let str1 = "Hello";
let str2 = "Hello";
console.log(str1 === str2); // true
```

## 类型检测

```js
// typeof 检测原始类型
typeof 10;           // "number"
typeof "hello";      // "string"
typeof true;         // "boolean"
typeof undefined;    // "undefined"
typeof Symbol();     // "symbol"
typeof 10n;          // "bigint"
typeof null;         // "object"（bug）
```

## 练习

1. **数字运算**：使用不同的数字类型（整数、浮点数、科学计数法）进行运算。

2. **字符串操作**：创建字符串，演示字符串的不可变性，使用字符串方法创建新字符串。

3. **布尔值判断**：编写代码判断值的真假，理解真值和假值的概念。

4. **null 和 undefined**：演示 null 和 undefined 的区别，理解它们的使用场景。

5. **Symbol 唯一性**：创建多个 Symbol，演示 Symbol 的唯一性特性。

6. **BigInt 大整数**：使用 BigInt 处理超出 Number 范围的大整数。

完成以上练习后，继续学习下一节，了解引用类型。

## 总结

原始类型是 JavaScript 的基础数据类型，具有不可变性和值比较的特性。主要要点：

- number：数字类型，包括整数、浮点数和特殊值
- string：字符串类型，不可变
- boolean：布尔类型，true 或 false
- null 和 undefined：表示空值和未定义
- symbol：唯一的符号类型
- bigint：大整数类型
- 原始类型是不可变的
- 原始类型按值比较

继续学习下一节，了解引用类型。
