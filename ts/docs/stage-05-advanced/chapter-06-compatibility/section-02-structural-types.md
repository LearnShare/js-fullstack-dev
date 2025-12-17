# 5.6.2 结构化类型系统深入

## 概述

TypeScript 使用结构化类型系统（Duck Typing），基于类型的结构而非名称进行兼容性判断。本节深入介绍结构化类型系统的原理。

## 什么是结构化类型

### 定义

结构化类型系统基于类型的结构（属性）而非名称进行兼容性判断。

### 基本概念

```ts
interface Point {
    x: number;
    y: number;
}

interface Coordinate {
    x: number;
    y: number;
}

let point: Point = { x: 1, y: 2 };
let coord: Coordinate = point; // 兼容：结构相同
```

## 结构兼容性

### 属性兼容性

类型兼容性基于属性：

```ts
interface Animal {
    name: string;
}

interface Dog {
    name: string;
    breed: string;
}

let animal: Animal = { name: "Animal" };
let dog: Dog = { name: "Dog", breed: "Golden" };

animal = dog; // 兼容：Dog 有 Animal 的所有属性
```

### 额外属性

可以包含额外属性：

```ts
interface Point {
    x: number;
    y: number;
}

let point: Point = { x: 1, y: 2, z: 3 }; // 兼容：可以包含额外属性
```

## 函数结构兼容性

### 参数兼容性

函数参数兼容性：

```ts
interface Func1 {
    (x: number): number;
}

interface Func2 {
    (x: number, y: number): number;
}

let func1: Func1 = (x) => x * 2;
let func2: Func2 = (x, y) => x + y;

// func1 = func2; // 不兼容：参数数量不同
func2 = func1; // 兼容：可以忽略额外参数
```

### 返回值兼容性

返回值必须兼容：

```ts
interface Func1 {
    (): number;
}

interface Func2 {
    (): number | string;
}

let func1: Func1 = () => 1;
let func2: Func2 = () => "hello";

// func1 = func2; // 不兼容：返回值类型不匹配
func2 = func1; // 兼容：number 可以赋值给 number | string
```

## 数组结构兼容性

### 元素类型兼容性

```ts
let arr1: number[] = [1, 2, 3];
let arr2: (number | string)[] = ["a", "b", "c"];

// arr1 = arr2; // 不兼容：元素类型不匹配
arr2 = arr1; // 兼容：number 可以赋值给 number | string
```

## 使用场景

### 1. 接口实现

```ts
interface Animal {
    name: string;
}

class Dog {
    name: string;
    breed: string;
}

let animal: Animal = new Dog(); // 兼容：Dog 有 name 属性
```

### 2. 对象字面量

```ts
interface Point {
    x: number;
    y: number;
}

function process(point: Point): void {
    // ...
}

process({ x: 1, y: 2, z: 3 }); // 兼容：可以包含额外属性
```

## 常见错误

### 错误 1：名称混淆

```ts
// 错误：认为名称相同才兼容
interface Point {
    x: number;
    y: number;
}

interface Coordinate {
    x: number;
    y: number;
}

// 实际上它们是兼容的，因为结构相同
```

### 错误 2：属性缺失

```ts
interface Animal {
    name: string;
    age: number;
}

let animal: Animal = { name: "Animal" }; // 错误：缺少 age 属性
```

## 注意事项

1. **结构优先**：结构比名称更重要
2. **属性检查**：检查属性是否存在和类型是否匹配
3. **额外属性**：可以包含额外属性
4. **函数兼容**：函数有特殊的兼容性规则

## 最佳实践

1. **理解结构**：理解结构化类型系统的原理
2. **属性检查**：确保属性存在和类型匹配
3. **类型安全**：利用结构化类型提高类型安全
4. **代码复用**：利用结构化类型支持代码复用

## 练习

1. **结构兼容性**：理解结构兼容性的原理。

2. **属性检查**：练习属性兼容性检查。

3. **函数兼容性**：理解函数结构兼容性。

4. **实际应用**：在实际场景中应用结构化类型系统。

完成以上练习后，继续学习下一节，了解协变与逆变。

## 总结

结构化类型系统基于类型的结构而非名称进行兼容性判断。可以包含额外属性，函数和数组有特殊的兼容性规则。理解结构化类型系统的原理是学习类型兼容性的关键。

## 相关资源

- [TypeScript 结构化类型文档](https://www.typescriptlang.org/docs/handbook/type-compatibility.html#structural-typing)
