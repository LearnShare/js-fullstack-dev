# 2.3.3 类型检测（typeof、instanceof）

## 概述

类型检测是确定变量类型的方法。JavaScript 提供了 `typeof` 和 `instanceof` 运算符进行类型检测。本节介绍这些方法的使用和最佳实践。

## typeof 运算符

**语法格式**：`typeof operand`

**参数说明**：

| 参数名     | 类型 | 说明                           | 是否必需 | 默认值 |
|:-----------|:-----|:-------------------------------|:---------|:-------|
| `operand`  | any  | 要检测类型的值或表达式       | 是       | -      |

**返回值**：字符串，返回表示操作数类型的字符串

**返回值说明**：
- `"number"`：数字类型
- `"string"`：字符串类型
- `"boolean"`：布尔类型
- `"undefined"`：未定义
- `"symbol"`：Symbol 类型
- `"bigint"`：BigInt 类型
- `"object"`：对象类型（包括 null、数组、对象）
- `"function"`：函数类型

**基本用法**：

```js
typeof 10;           // "number"
typeof "hello";      // "string"
typeof true;         // "boolean"
typeof undefined;    // "undefined"
typeof Symbol();     // "symbol"
typeof 10n;          // "bigint"
typeof null;         // "object"（bug）
typeof {};           // "object"
typeof [];           // "object"
typeof function(){}; // "function"
```

### typeof 的局限性

```js
// typeof null 返回 "object"（这是 bug）
typeof null; // "object"

// typeof 数组返回 "object"
typeof []; // "object"

// typeof 对象返回 "object"
typeof {}; // "object"
```

### 使用 typeof 检测

```js
// 检测原始类型
function isNumber(value) {
    return typeof value === "number" && !isNaN(value);
}

function isString(value) {
    return typeof value === "string";
}

function isBoolean(value) {
    return typeof value === "boolean";
}

function isUndefined(value) {
    return typeof value === "undefined";
}
```

## instanceof 运算符

**语法格式**：`object instanceof constructor`

**参数说明**：

| 参数名        | 类型      | 说明                           | 是否必需 | 默认值 |
|:--------------|:----------|:-------------------------------|:---------|:-------|
| `object`      | Object    | 要检测的对象                   | 是       | -      |
| `constructor`  | Function  | 构造函数（类）                 | 是       | -      |

**返回值**：布尔值，如果对象是指定构造函数的实例返回 `true`，否则返回 `false`

**说明**：`instanceof` 检查对象的原型链中是否存在指定构造函数的 `prototype` 属性

**基本用法**：

```js
// 检测对象类型
[] instanceof Array;        // true
{} instanceof Object;       // true
new Date() instanceof Date; // true
/pattern/ instanceof RegExp; // true

// 检测函数
function greet() {}
greet instanceof Function;  // true

// 检测类实例
class User {}
let user = new User();
user instanceof User;       // true
```

### instanceof 的原理

```js
// instanceof 检查原型链
function Person() {}
let person = new Person();

console.log(person instanceof Person);  // true
console.log(person instanceof Object);  // true（Person 继承自 Object）
```

### 使用 instanceof 检测

```js
// 检测数组
function isArray(value) {
    return value instanceof Array;
}

// 检测日期
function isDate(value) {
    return value instanceof Date;
}

// 检测正则表达式
function isRegExp(value) {
    return value instanceof RegExp;
}
```

## Object.prototype.toString

### 使用 toString 检测类型

```js
// 使用 Object.prototype.toString 检测类型
Object.prototype.toString.call(10);        // "[object Number]"
Object.prototype.toString.call("hello");    // "[object String]"
Object.prototype.toString.call(true);       // "[object Boolean]"
Object.prototype.toString.call(null);       // "[object Null]"
Object.prototype.toString.call(undefined);  // "[object Undefined]"
Object.prototype.toString.call([]);         // "[object Array]"
Object.prototype.toString.call({});        // "[object Object]"
Object.prototype.toString.call(new Date()); // "[object Date]"
```

### 封装类型检测函数

```js
function getType(value) {
    return Object.prototype.toString.call(value).slice(8, -1);
}

getType(10);        // "Number"
getType("hello");   // "String"
getType([]);        // "Array"
getType({});        // "Object"
getType(null);      // "Null"
```

## Array.isArray() 方法

**语法格式**：`Array.isArray(value)`

**参数说明**：

| 参数名   | 类型 | 说明                           | 是否必需 | 默认值 |
|:---------|:-----|:-------------------------------|:---------|:-------|
| `value`  | any  | 要检测的值                     | 是       | -      |

**返回值**：布尔值，如果值是数组返回 `true`，否则返回 `false`

**说明**：`Array.isArray()` 是检测数组的最佳方法，比 `instanceof Array` 更可靠

**检测数组**：

```js
// Array.isArray() 是检测数组的最佳方法
Array.isArray([]);        // true
Array.isArray([1, 2, 3]); // true
Array.isArray({});        // false
Array.isArray(null);      // false
```

## 类型检测的最佳实践

### 1. 检测原始类型

```js
// 使用 typeof
typeof value === "number"
typeof value === "string"
typeof value === "boolean"
typeof value === "undefined"
```

### 2. 检测 null

```js
// 使用严格相等
value === null

// 或使用 Object.prototype.toString
Object.prototype.toString.call(value) === "[object Null]"
```

### 3. 检测数组

```js
// 使用 Array.isArray()（推荐）
Array.isArray(value)

// 或使用 instanceof
value instanceof Array
```

### 4. 检测对象

```js
// 检测普通对象
function isPlainObject(value) {
    return value !== null &&
           typeof value === "object" &&
           !Array.isArray(value) &&
           Object.prototype.toString.call(value) === "[object Object]";
}
```

### 5. 综合类型检测函数

```js
function getType(value) {
    if (value === null) return "null";
    if (value === undefined) return "undefined";
    if (typeof value === "object") {
        if (Array.isArray(value)) return "array";
        if (value instanceof Date) return "date";
        if (value instanceof RegExp) return "regexp";
        return "object";
    }
    return typeof value;
}
```

## 常见陷阱

### 陷阱 1：typeof null

```js
// typeof null 返回 "object"（bug）
typeof null; // "object"

// 正确检测 null
value === null; // true
```

### 陷阱 2：typeof 数组

```js
// typeof 数组返回 "object"
typeof []; // "object"

// 正确检测数组
Array.isArray([]); // true
```

### 陷阱 3：跨框架 instanceof

```js
// 跨框架的 instanceof 可能不准确
// 使用 Array.isArray() 更可靠
Array.isArray(value); // 推荐
```

## 练习

1. **类型检测函数**：编写函数检测值是否为数字、字符串、布尔值、数组、对象等类型。

2. **综合类型检测**：编写一个函数，使用 `Object.prototype.toString` 准确检测所有类型。

3. **数组检测对比**：对比 `typeof`、`instanceof Array` 和 `Array.isArray()` 的区别，并测试跨框架场景。

4. **null 检测**：编写函数正确检测 `null` 值（避免 `typeof null` 的 bug）。

5. **类型检测工具**：创建一个类型检测工具函数库，包含常用类型的检测方法。

完成以上练习后，继续学习下一节，了解类型转换。

## 总结

类型检测是 JavaScript 开发中的重要技能。主要要点：

- `typeof`：检测原始类型和函数
- `instanceof`：检测对象类型和类实例
- `Object.prototype.toString`：更准确的类型检测
- `Array.isArray()`：检测数组的最佳方法
- 注意 `typeof null` 的 bug
- 使用合适的检测方法

继续学习下一节，了解类型转换。
