# 2.2.2 类型别名基础

## 概述

本节介绍类型别名的基本定义和使用方法，包括基本语法、各种类型的别名定义和基本用法。

## 类型别名定义

### 基本语法

```ts
type AliasName = Type;
```

### 基础类型别名

```ts
// 字符串别名
type Name = string;
type Email = string;

// 数字别名
type Age = number;
type Price = number;

// 布尔别名
type IsActive = boolean;
```

### 对象类型别名

```ts
// 对象类型别名
type User = {
    name: string;
    age: number;
    email: string;
};

let user: User = {
    name: "John",
    age: 30,
    email: "john@example.com"
};
```

### 数组类型别名

```ts
// 数组类型别名
type Numbers = number[];
type Names = string[];

// 或使用泛型语法
type Numbers2 = Array<number>;
```

### 元组类型别名

```ts
// 元组类型别名
type Point = [number, number];
type UserInfo = [string, number, boolean];
```

### 函数类型别名

```ts
// 函数类型别名
type Handler = (event: Event) => void;
type Calculator = (a: number, b: number) => number;
```

## 使用类型别名

### 类型注解

使用类型别名作为类型注解：

```ts
type User = {
    name: string;
    age: number;
};

// 变量类型注解
let user: User = {
    name: "John",
    age: 30
};
```

### 函数参数和返回值

```ts
type User = {
    name: string;
    age: number;
};

// 函数参数
function greet(user: User): string {
    return `Hello, ${user.name}!`;
}

// 函数返回值
function createUser(name: string, age: number): User {
    return { name, age };
}
```

### 嵌套类型别名

类型别名可以嵌套使用：

```ts
type Address = {
    street: string;
    city: string;
};

type User = {
    name: string;
    address: Address; // 使用其他类型别名
};
```

## 类型别名组合

### 复用类型别名

类型别名可以在多个地方复用：

```ts
type ID = string | number;

interface User {
    id: ID;
    name: string;
}

interface Product {
    id: ID;
    title: string;
}
```

### 组合类型别名

类型别名可以组合使用：

```ts
type Name = string;
type Age = number;

type User = {
    name: Name;
    age: Age;
};
```

## 泛型类型别名

### 定义

类型别名可以包含泛型参数：

```ts
type Container<T> = {
    value: T;
};

let stringContainer: Container<string> = {
    value: "hello"
};

let numberContainer: Container<number> = {
    value: 42
};
```

### 多个泛型参数

```ts
type Pair<T, U> = {
    first: T;
    second: U;
};

let pair: Pair<string, number> = {
    first: "hello",
    second: 42
};
```

## 常见错误

### 错误 1：循环引用

```ts
// 错误：循环引用
type A = B;
type B = A;
```

### 错误 2：类型不匹配

```ts
type User = {
    name: string;
    age: number;
};

// 错误：类型不匹配
let user: User = {
    name: "John",
    age: "30" // 错误：应该是 number
};
```

## 注意事项

1. **类型别名是类型**：类型别名只在编译时存在
2. **不能合并**：类型别名不支持声明合并
3. **可以嵌套**：类型别名可以嵌套使用
4. **支持泛型**：类型别名支持泛型参数

## 最佳实践

1. **明确命名**：使用清晰的类型别名名称
2. **合理复用**：在多个地方使用的类型定义类型别名
3. **避免循环**：避免类型别名的循环引用
4. **使用泛型**：对于需要参数化的类型使用泛型

## 练习

1. **基础类型别名**：定义各种基础类型的别名。

2. **对象类型别名**：定义对象类型的别名，练习使用。

3. **嵌套类型别名**：定义嵌套的类型别名。

4. **泛型类型别名**：定义包含泛型参数的类型别名。

5. **实际应用**：在实际场景中应用类型别名。

完成以上练习后，继续学习下一节，了解联合类型与交叉类型。

## 总结

类型别名是 TypeScript 中创建类型名称的方式。类型别名可以简化复杂类型的定义，支持基础类型、对象类型、数组类型、元组类型、函数类型等。理解类型别名的基本定义和使用是学习 TypeScript 类型系统的基础。

## 相关资源

- [TypeScript 类型别名文档](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-aliases)
