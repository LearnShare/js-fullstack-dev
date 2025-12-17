# 5.6.1 类型兼容性概述

## 概述

类型兼容性是 TypeScript 类型系统的基础，决定了哪些类型可以相互赋值。本节介绍类型兼容性的概念、规则和作用。

## 什么是类型兼容性

### 定义

类型兼容性是指一个类型是否可以赋值给另一个类型的规则。

### 基本概念

```ts
interface Animal {
    name: string;
}

interface Dog extends Animal {
    breed: string;
}

let animal: Animal = { name: "Animal" };
let dog: Dog = { name: "Dog", breed: "Golden" };

animal = dog; // 兼容：Dog 可以赋值给 Animal
// dog = animal; // 不兼容：Animal 不能赋值给 Dog
```

## 类型兼容性规则

### 1. 结构化类型

TypeScript 使用结构化类型系统：

```ts
interface Point {
    x: number;
    y: number;
}

let point: Point = { x: 1, y: 2 };
let obj = { x: 1, y: 2, z: 3 };
point = obj; // 兼容：obj 有 x 和 y 属性
```

### 2. 函数兼容性

函数类型兼容性基于参数和返回值：

```ts
let func1: (x: number) => number;
let func2: (x: number, y: number) => number;

func1 = func2; // 不兼容：参数数量不同
func2 = func1; // 兼容：可以忽略额外参数
```

### 3. 数组兼容性

数组兼容性基于元素类型：

```ts
let arr1: number[];
let arr2: (number | string)[];

arr1 = arr2; // 不兼容：元素类型不匹配
arr2 = arr1; // 兼容：number 可以赋值给 number | string
```

## 类型兼容性的作用

### 1. 类型安全

类型兼容性提供类型安全：

```ts
interface User {
    name: string;
    age: number;
}

function process(user: User): void {
    console.log(user.name);
}

let data = { name: "John", age: 30, email: "john@example.com" };
process(data); // 兼容：data 有 name 和 age 属性
```

### 2. 代码复用

类型兼容性支持代码复用：

```ts
interface Animal {
    name: string;
}

function getName(animal: Animal): string {
    return animal.name;
}

let dog = { name: "Dog", breed: "Golden" };
getName(dog); // 兼容：可以使用
```

### 3. 灵活性

类型兼容性提供灵活性：

```ts
interface Point {
    x: number;
    y: number;
}

let point: Point = { x: 1, y: 2, z: 3 }; // 兼容：可以包含额外属性
```

## 兼容性检查

### 赋值兼容性

```ts
let a: number = 1;
let b: number | string = a; // 兼容

let c: string = "hello";
// let d: number = c; // 不兼容
```

### 函数参数兼容性

```ts
function process(value: number | string): void {
    // ...
}

process(1);      // 兼容
process("hello"); // 兼容
```

## 使用场景

### 1. 接口实现

```ts
interface Animal {
    name: string;
}

class Dog implements Animal {
    name: string;
    breed: string;
}
```

### 2. 函数参数

```ts
function process(animal: Animal): void {
    // ...
}

let dog = new Dog();
process(dog); // 兼容
```

### 3. 类型断言

```ts
let value: unknown = "hello";
let str: string = value as string; // 类型断言
```

## 注意事项

1. **结构化类型**：TypeScript 使用结构化类型系统
2. **函数兼容性**：函数类型兼容性有特殊规则
3. **数组兼容性**：数组兼容性基于元素类型
4. **类型安全**：类型兼容性提供类型安全

## 最佳实践

1. **理解规则**：理解类型兼容性的规则
2. **类型安全**：利用类型兼容性提高类型安全
3. **灵活性**：利用类型兼容性提供灵活性
4. **代码复用**：利用类型兼容性支持代码复用

## 练习

1. **类型兼容性概念**：理解类型兼容性的概念和规则。

2. **赋值兼容性**：练习类型赋值兼容性。

3. **函数兼容性**：理解函数类型兼容性。

4. **实际应用**：在实际场景中应用类型兼容性。

完成以上练习后，继续学习下一节，了解结构化类型系统深入。

## 总结

类型兼容性是 TypeScript 类型系统的基础，决定了哪些类型可以相互赋值。TypeScript 使用结构化类型系统，函数和数组有特殊的兼容性规则。理解类型兼容性的概念和规则是学习 TypeScript 类型系统的关键。

## 相关资源

- [TypeScript 类型兼容性文档](https://www.typescriptlang.org/docs/handbook/type-compatibility.html)
