# 1.2.2 原始类型（string、number、boolean）

## 概述

原始类型是 TypeScript 类型系统的基础。本节介绍 TypeScript 中的原始类型：string、number、boolean，以及它们的用法和特性。

## string 类型

### 定义

`string` 类型表示字符串值。

### 基本用法

```ts
// 类型注解
let name: string = "John";

// 类型推断
let message = "Hello, TypeScript!";

// 模板字符串
let greeting: string = `Hello, ${name}!`;
```

### 字符串方法

TypeScript 支持所有 JavaScript 字符串方法：

```ts
let text: string = "Hello, TypeScript!";

// 获取长度
let length: number = text.length;

// 转换为大写
let upper: string = text.toUpperCase();

// 转换为小写
let lower: string = text.toLowerCase();

// 查找子字符串
let index: number = text.indexOf("TypeScript");

// 截取子字符串
let substring: string = text.substring(0, 5);
```

### 字符串字面量类型

可以使用字符串字面量作为类型：

```ts
// 字面量类型
let direction: "up" | "down" | "left" | "right" = "up";

// 只能赋值指定的字面量值
direction = "down"; // 正确
direction = "north"; // 错误
```

### 注意事项

1. **字符串是不可变的**：字符串值不能修改
2. **字符串方法返回新字符串**：不会修改原字符串
3. **模板字符串**：支持多行字符串和表达式插值

## number 类型

### 定义

`number` 类型表示数字值，包括整数和浮点数。

### 基本用法

```ts
// 整数
let count: number = 10;

// 浮点数
let price: number = 99.99;

// 科学计数法
let largeNumber: number = 1e10;

// 二进制
let binary: number = 0b1010;

// 八进制
let octal: number = 0o744;

// 十六进制
let hex: number = 0xff;
```

### 数字方法

```ts
let num: number = 123.456;

// 转换为字符串
let str: string = num.toString();

// 保留小数位
let fixed: string = num.toFixed(2); // "123.46"

// 指数表示
let exp: string = num.toExponential(2); // "1.23e+2"
```

### 数字字面量类型

可以使用数字字面量作为类型：

```ts
// 字面量类型
let status: 200 | 404 | 500 = 200;

// 只能赋值指定的字面量值
status = 404; // 正确
status = 403; // 错误
```

### 特殊值

```ts
// 正无穷
let positiveInfinity: number = Infinity;

// 负无穷
let negativeInfinity: number = -Infinity;

// 非数字
let notANumber: number = NaN;
```

### 注意事项

1. **所有数字都是浮点数**：TypeScript/JavaScript 中所有数字都是 64 位浮点数
2. **精度问题**：浮点数运算可能存在精度问题
3. **NaN 检查**：使用 `isNaN()` 或 `Number.isNaN()` 检查 NaN

## boolean 类型

### 定义

`boolean` 类型表示布尔值：`true` 或 `false`。

### 基本用法

```ts
// 类型注解
let isActive: boolean = true;
let isCompleted: boolean = false;

// 类型推断
let isValid = true;
let hasError = false;
```

### 布尔运算

```ts
let a: boolean = true;
let b: boolean = false;

// 逻辑与
let and: boolean = a && b; // false

// 逻辑或
let or: boolean = a || b; // true

// 逻辑非
let not: boolean = !a; // false
```

### 条件判断

```ts
let isLoggedIn: boolean = true;

if (isLoggedIn) {
    console.log("用户已登录");
} else {
    console.log("用户未登录");
}
```

### 注意事项

1. **只有两个值**：boolean 类型只有 `true` 和 `false` 两个值
2. **不能与其他类型混用**：不能将其他类型隐式转换为 boolean
3. **严格相等**：使用 `===` 进行严格比较

## 类型注解示例

### 变量声明

```ts
// string
let name: string = "John";
let message: string = `Hello, ${name}!`;

// number
let count: number = 10;
let price: number = 99.99;

// boolean
let isActive: boolean = true;
let isCompleted: boolean = false;
```

### 函数参数和返回值

```ts
// 函数参数类型注解
function greet(name: string): string {
    return `Hello, ${name}!`;
}

// 多个参数
function add(a: number, b: number): number {
    return a + b;
}

// 布尔返回值
function isEven(num: number): boolean {
    return num % 2 === 0;
}
```

### 对象属性

```ts
interface User {
    name: string;
    age: number;
    isActive: boolean;
}

let user: User = {
    name: "John",
    age: 30,
    isActive: true
};
```

## 类型推断

### 自动推断

TypeScript 可以根据值自动推断类型：

```ts
// 推断为 string
let name = "John";

// 推断为 number
let count = 10;

// 推断为 boolean
let isActive = true;
```

### 推断规则

```ts
// 字符串字面量推断为 string
let message = "Hello"; // string

// 数字字面量推断为 number
let count = 10; // number

// 布尔字面量推断为 boolean
let isValid = true; // boolean
```

## 类型转换

### 显式转换

```ts
// 数字转字符串
let num: number = 123;
let str: string = num.toString();

// 字符串转数字
let strNum: string = "123";
let numValue: number = Number(strNum);
let parseIntValue: number = parseInt(strNum, 10);

// 字符串转布尔
let strBool: string = "true";
let boolValue: boolean = strBool === "true";
```

### 类型断言

```ts
// 类型断言（不推荐，应使用正确的类型）
let value: any = "123";
let num: number = value as number; // 不推荐
```

## 常见错误

### 错误 1：类型不匹配

```ts
let count: number = 10;
count = "ten"; // 错误：类型 'string' 不能赋值给类型 'number'
```

### 错误 2：未定义的类型

```ts
let value: string;
console.log(value.length); // 错误：'value' 可能为 'undefined'
```

### 错误 3：隐式 any

```ts
// strict 模式下会报错
function process(value) { // 错误：参数 'value' 隐式具有 'any' 类型
    return value;
}
```

## 注意事项

1. **类型注解是可选的**：可以使用类型推断，但建议在函数参数和返回值处使用类型注解
2. **严格模式**：启用 `strict` 模式可以获得更严格的类型检查
3. **类型安全**：类型注解不会影响运行时行为，只用于编译时检查
4. **类型推断**：在类型明确的地方可以利用类型推断，减少冗余

## 最佳实践

1. **明确类型**：函数参数和返回值使用明确的类型注解
2. **利用推断**：在类型明确的地方利用类型推断
3. **避免 any**：尽量避免使用 `any` 类型
4. **类型一致**：保持类型使用的一致性

## 练习

1. **类型注解**：为变量、函数参数和返回值添加类型注解。

2. **类型推断**：观察 TypeScript 如何推断原始类型。

3. **类型错误**：故意制造类型错误，理解错误信息。

4. **字符串操作**：使用字符串类型和方法进行字符串操作。

5. **数字运算**：使用数字类型进行数学运算，注意精度问题。

完成以上练习后，继续学习下一节，了解数组与元组。

## 总结

原始类型（string、number、boolean）是 TypeScript 类型系统的基础。理解这些类型的用法和特性是学习 TypeScript 的第一步。类型注解可以帮助 TypeScript 进行类型检查，类型推断可以减少冗余代码。在实际开发中，应该根据场景选择合适的类型注解方式。

## 相关资源

- [TypeScript 原始类型文档](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#the-primitives-string-number-and-boolean)
