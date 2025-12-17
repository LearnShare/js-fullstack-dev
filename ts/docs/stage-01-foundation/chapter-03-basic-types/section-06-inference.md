# 1.2.6 类型推断与类型注解

## 概述

TypeScript 具有强大的类型推断能力，可以根据上下文自动推断类型。同时，也可以显式添加类型注解。本节介绍类型推断的工作原理和类型注解的使用。

## 类型推断

### 定义

类型推断是 TypeScript 根据值自动推断类型的能力，无需显式指定类型。

### 基本推断

#### 变量推断

```ts
// TypeScript 推断为 string
let name = "John";

// TypeScript 推断为 number
let age = 30;

// TypeScript 推断为 boolean
let isActive = true;
```

#### 数组推断

```ts
// TypeScript 推断为 number[]
let numbers = [1, 2, 3, 4, 5];

// TypeScript 推断为 string[]
let names = ["John", "Jane", "Bob"];
```

#### 对象推断

```ts
// TypeScript 推断对象类型
let user = {
    name: "John",
    age: 30,
    isActive: true
};
// 类型为：{ name: string; age: number; isActive: boolean; }
```

### 函数推断

#### 返回值推断

```ts
// TypeScript 推断返回值为 number
function add(a: number, b: number) {
    return a + b;
}
```

#### 参数推断

```ts
// 回调函数参数推断
let numbers = [1, 2, 3, 4, 5];

// TypeScript 推断 item 为 number
numbers.map(item => item * 2);
```

### 上下文推断

#### 函数上下文

```ts
// TypeScript 根据上下文推断类型
function process(callback: (value: number) => void) {
    callback(42);
}

// TypeScript 推断 value 为 number
process(value => {
    console.log(value); // value 的类型是 number
});
```

#### 对象方法

```ts
let calculator = {
    add(a: number, b: number) {
        // TypeScript 推断返回值为 number
        return a + b;
    }
};
```

## 类型注解

### 定义

类型注解是显式指定类型的方式，使用冒号 `:` 后跟类型名称。

### 变量类型注解

```ts
// 显式类型注解
let name: string = "John";
let age: number = 30;
let isActive: boolean = true;
```

### 函数类型注解

#### 参数类型注解

```ts
// 参数类型注解
function greet(name: string) {
    return `Hello, ${name}!`;
}
```

#### 返回值类型注解

```ts
// 返回值类型注解
function add(a: number, b: number): number {
    return a + b;
}
```

#### 完整函数类型注解

```ts
// 函数类型注解
let multiply: (a: number, b: number) => number = function(a, b) {
    return a * b;
};
```

### 对象类型注解

```ts
// 对象类型注解
let user: {
    name: string;
    age: number;
    isActive: boolean;
} = {
    name: "John",
    age: 30,
    isActive: true
};
```

### 数组类型注解

```ts
// 数组类型注解
let numbers: number[] = [1, 2, 3, 4, 5];
let names: Array<string> = ["John", "Jane"];
```

## 何时使用类型注解

### 需要类型注解的场景

#### 1. 函数参数

函数参数通常需要类型注解：

```ts
// 推荐：添加类型注解
function processUser(name: string, age: number) {
    // ...
}

// 不推荐：参数没有类型注解
function processUser(name, age) {
    // ...
}
```

#### 2. 函数返回值（复杂函数）

复杂函数建议添加返回类型注解：

```ts
// 推荐：添加返回类型注解
function getUserData(): { name: string; age: number } {
    return { name: "John", age: 30 };
}
```

#### 3. 对象字面量（复杂对象）

复杂对象建议添加类型注解：

```ts
// 推荐：添加类型注解
let config: {
    apiUrl: string;
    timeout: number;
    retries: number;
} = {
    apiUrl: "https://api.example.com",
    timeout: 5000,
    retries: 3
};
```

#### 4. 类型不明确时

当类型推断不够明确时，添加类型注解：

```ts
// 类型推断为 any[]
let items = [];

// 推荐：添加类型注解
let items: number[] = [];
```

### 可以利用类型推断的场景

#### 1. 简单变量

简单变量可以利用类型推断：

```ts
// 推荐：利用类型推断
let name = "John";
let age = 30;

// 不必要：显式类型注解
let name: string = "John";
let age: number = 30;
```

#### 2. 简单函数返回值

简单函数返回值可以利用类型推断：

```ts
// 推荐：利用类型推断
function add(a: number, b: number) {
    return a + b; // 推断为 number
}
```

## 类型推断的限制

### 推断为 any

当无法推断类型时，TypeScript 可能推断为 `any`：

```ts
// 推断为 any[]
let items = [];

// 需要显式类型注解
let items: number[] = [];
```

### 推断不够精确

有时类型推断不够精确：

```ts
// 推断为 (string | number)[]
let mixed = ["hello", 42];

// 如果需要更精确的类型，需要类型注解
let mixed: [string, number] = ["hello", 42];
```

## 类型推断的优势

### 1. 减少冗余

类型推断可以减少冗余的类型注解：

```ts
// 利用类型推断，代码更简洁
let name = "John";
let age = 30;

// 显式类型注解，代码冗余
let name: string = "John";
let age: number = 30;
```

### 2. 保持同步

类型推断可以自动保持类型与值同步：

```ts
// 如果修改值，类型会自动更新
let value = "hello"; // 推断为 string
value = "world";     // 仍然是 string
```

## 类型注解的优势

### 1. 明确意图

类型注解可以明确表达意图：

```ts
// 明确表示这是一个数字数组
let numbers: number[] = [];
```

### 2. 早期错误检测

类型注解可以在编译时发现错误：

```ts
function process(value: string): string {
    return value.toUpperCase();
}

// 编译时发现错误
process(123); // 错误：类型 'number' 不能赋值给类型 'string'
```

### 3. 文档化

类型注解可以作为代码文档：

```ts
// 类型注解清楚地说明了函数的参数和返回值
function calculateTotal(price: number, quantity: number): number {
    return price * quantity;
}
```

## 最佳实践

### 1. 函数参数必须注解

函数参数应该始终添加类型注解：

```ts
// ✅ 推荐
function greet(name: string, age: number) {
    // ...
}

// ❌ 不推荐
function greet(name, age) {
    // ...
}
```

### 2. 函数返回值（复杂函数）建议注解

复杂函数建议添加返回类型注解：

```ts
// ✅ 推荐
function getUser(): { name: string; age: number } {
    return { name: "John", age: 30 };
}
```

### 3. 简单变量利用推断

简单变量可以利用类型推断：

```ts
// ✅ 推荐
let name = "John";
let age = 30;

// ❌ 不必要
let name: string = "John";
let age: number = 30;
```

### 4. 类型不明确时添加注解

当类型推断不够明确时，添加类型注解：

```ts
// ✅ 推荐
let items: number[] = [];

// ❌ 不推荐（推断为 any[]）
let items = [];
```

## 练习

1. **类型推断**：观察 TypeScript 如何推断不同类型变量的类型。

2. **类型注解**：为函数参数和返回值添加类型注解。

3. **推断 vs 注解**：理解何时使用类型推断，何时使用类型注解。

4. **推断限制**：体验类型推断的限制，理解何时需要显式注解。

5. **最佳实践**：按照最佳实践编写代码，平衡类型推断和类型注解。

完成以上练习后，继续学习下一节，了解类型断言。

## 总结

类型推断和类型注解是 TypeScript 类型系统的两个重要特性。类型推断可以减少冗余代码，类型注解可以明确意图和提供文档。在实际开发中，应该根据场景选择合适的策略：函数参数必须注解，简单变量可以利用推断，类型不明确时添加注解。

## 相关资源

- [TypeScript 类型推断文档](https://www.typescriptlang.org/docs/handbook/type-inference.html)
- [TypeScript 类型注解文档](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-annotations)
