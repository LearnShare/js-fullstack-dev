# 4.1.1 泛型概述

## 概述

泛型是 TypeScript 类型系统的核心特性，允许创建可重用的类型和函数。本节介绍泛型的概念、作用和优势。

## 什么是泛型

### 定义

泛型是一种类型参数化机制，允许在定义函数、接口、类时使用类型参数，在使用时指定具体类型。

### 基本概念

```ts
// 不使用泛型
function identity(value: number): number {
    return value;
}

// 使用泛型
function identity<T>(value: T): T {
    return value;
}

let result = identity<string>("Hello");
let result2 = identity<number>(42);
```

## 泛型的作用

### 1. 代码复用

泛型允许编写可重用的代码：

```ts
// 不使用泛型：需要为每种类型写一个函数
function getFirstNumber(arr: number[]): number {
    return arr[0];
}

function getFirstString(arr: string[]): string {
    return arr[0];
}

// 使用泛型：一个函数处理所有类型
function getFirst<T>(arr: T[]): T {
    return arr[0];
}
```

### 2. 类型安全

泛型提供类型安全：

```ts
function getFirst<T>(arr: T[]): T {
    return arr[0];
}

let numbers = [1, 2, 3];
let first = getFirst<number>(numbers); // 类型为 number

let strings = ["a", "b", "c"];
let firstStr = getFirst<string>(strings); // 类型为 string
```

### 3. 灵活性

泛型提供灵活性：

```ts
interface Box<T> {
    value: T;
}

let numberBox: Box<number> = { value: 42 };
let stringBox: Box<string> = { value: "Hello" };
```

## 泛型的优势

### 1. 类型安全

泛型在编译时提供类型检查：

```ts
function process<T>(value: T): T {
    return value;
}

let result = process<number>(42);
// result 的类型是 number，类型安全
```

### 2. 代码复用

泛型减少代码重复：

```ts
// 不使用泛型：需要多个函数
function processNumber(value: number): number { return value; }
function processString(value: string): string { return value; }

// 使用泛型：一个函数处理所有类型
function process<T>(value: T): T { return value; }
```

### 3. 更好的 IDE 支持

泛型提供更好的 IDE 支持：

```ts
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key];
}

let user = { name: "John", age: 30 };
let name = getProperty(user, "name"); // IDE 知道 name 的类型是 string
```

## 泛型 vs any

### 区别

| 特性       | 泛型（Generics）            | any                        |
|:-----------|:----------------------------|:---------------------------|
| 类型安全   | 编译时类型检查              | 无类型检查                 |
| 代码提示   | 完整的 IDE 支持             | 有限的 IDE 支持            |
| 使用场景   | 需要类型安全                | 需要动态类型               |
| 性能       | 编译时优化                  | 运行时检查                 |

### 示例对比

```ts
// 使用 any：失去类型安全
function process(value: any): any {
    return value;
}

let result = process(42);
// result 的类型是 any，没有类型安全

// 使用泛型：保持类型安全
function process<T>(value: T): T {
    return value;
}

let result2 = process<number>(42);
// result2 的类型是 number，类型安全
```

## 使用场景

### 1. 函数

```ts
function identity<T>(value: T): T {
    return value;
}
```

### 2. 接口

```ts
interface Container<T> {
    value: T;
    getValue(): T;
}
```

### 3. 类

```ts
class Box<T> {
    private value: T;

    constructor(value: T) {
        this.value = value;
    }

    getValue(): T {
        return this.value;
    }
}
```

## 注意事项

1. **类型参数命名**：通常使用单个大写字母（T、U、V 等）
2. **类型推断**：TypeScript 可以推断泛型类型
3. **类型约束**：可以使用 extends 约束类型参数
4. **默认类型**：可以为类型参数提供默认类型

## 最佳实践

1. **使用泛型**：在需要类型安全时使用泛型而不是 any
2. **明确类型**：为类型参数使用有意义的名称
3. **类型推断**：利用类型推断简化代码
4. **合理约束**：使用类型约束限制类型参数

## 练习

1. **泛型概念**：理解泛型的概念和作用。

2. **类型参数**：练习使用类型参数定义泛型。

3. **类型推断**：体验 TypeScript 的类型推断功能。

4. **实际应用**：在实际场景中应用泛型。

完成以上练习后，继续学习下一节，了解泛型函数。

## 总结

泛型是 TypeScript 类型系统的核心特性，允许创建可重用的类型和函数。泛型提供类型安全、代码复用和更好的 IDE 支持。理解泛型的概念和作用是学习 TypeScript 高级特性的关键。

## 相关资源

- [TypeScript 泛型文档](https://www.typescriptlang.org/docs/handbook/2/generics.html)
