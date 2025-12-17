# 4.2.2 extends 约束

## 概述

`extends` 约束是最常用的泛型约束方式，用于限制类型参数必须满足某些条件。本节介绍 `extends` 约束的使用。

## extends 约束语法

### 基本语法

```ts
function functionName<T extends ConstraintType>(param: T): ReturnType {
    // 函数体
}
```

### 示例

```ts
// 基本约束
interface HasLength {
    length: number;
}

function getLength<T extends HasLength>(value: T): number {
    return value.length;
}

getLength("Hello");     // 正确：string 有 length 属性
getLength([1, 2, 3]);   // 正确：array 有 length 属性
// getLength(42);       // 错误：number 没有 length 属性
```

## 接口约束

### 使用接口约束

```ts
interface HasId {
    id: number;
}

function process<T extends HasId>(value: T): number {
    return value.id;
}

let user = { id: 1, name: "John" };
process(user); // 正确：user 有 id 属性
```

### 多个属性约束

```ts
interface HasNameAndAge {
    name: string;
    age: number;
}

function process<T extends HasNameAndAge>(value: T): string {
    return `${value.name} is ${value.age} years old`;
}
```

## 类型别名约束

### 使用类型别名约束

```ts
type HasLength = {
    length: number;
};

function getLength<T extends HasLength>(value: T): number {
    return value.length;
}
```

## 联合类型约束

### 限制为特定类型

```ts
function process<T extends string | number>(value: T): T {
    return value;
}

process("Hello");  // 正确
process(42);       // 正确
// process(true);  // 错误：boolean 不在约束范围内
```

## 类约束

### 使用类约束

```ts
class Animal {
    name: string;
}

function getName<T extends Animal>(animal: T): string {
    return animal.name;
}

class Dog extends Animal {
    breed: string;
}

let dog = new Dog();
getName(dog); // 正确：Dog 继承自 Animal
```

## 多个约束

### 使用交叉类型

```ts
interface HasId {
    id: number;
}

interface HasName {
    name: string;
}

function process<T extends HasId & HasName>(value: T): string {
    return `${value.name} (${value.id})`;
}
```

## 约束继承

### 约束可以继承

```ts
interface Base {
    id: number;
}

interface Extended extends Base {
    name: string;
}

function process<T extends Extended>(value: T): string {
    return `${value.name} (${value.id})`;
}
```

## 使用场景

### 1. 访问对象属性

```ts
interface HasValue {
    value: number;
}

function getValue<T extends HasValue>(obj: T): number {
    return obj.value;
}
```

### 2. 确保方法存在

```ts
interface HasToString {
    toString(): string;
}

function process<T extends HasToString>(value: T): string {
    return value.toString();
}
```

### 3. 限制类型范围

```ts
function process<T extends string | number>(value: T): T {
    return value;
}
```

## 常见错误

### 错误 1：约束类型不匹配

```ts
interface HasLength {
    length: number;
}

function getLength<T extends HasLength>(value: T): number {
    return value.length;
}

// 错误：number 没有 length 属性
getLength(42);
```

### 错误 2：约束位置错误

```ts
// 错误：约束应该在类型参数后
function process<T>(value: T extends HasLength): T {
    return value;
}

// 正确
function process<T extends HasLength>(value: T): T {
    return value;
}
```

## 注意事项

1. **extends 关键字**：使用 `extends` 关键字定义约束
2. **约束位置**：约束在类型参数后
3. **多个约束**：可以使用交叉类型实现多个约束
4. **约束继承**：约束可以继承其他类型

## 最佳实践

1. **使用约束**：在需要访问特定属性时使用约束
2. **明确约束**：为约束使用明确的接口或类型
3. **合理约束**：不要过度约束，保持灵活性
4. **类型安全**：利用约束提高类型安全

## 练习

1. **extends 约束**：定义使用 extends 约束的泛型函数。

2. **接口约束**：定义使用接口约束的泛型函数。

3. **多个约束**：定义使用多个约束的泛型函数。

4. **实际应用**：在实际场景中应用 extends 约束。

完成以上练习后，继续学习下一节，了解 keyof 操作符。

## 总结

`extends` 约束是最常用的泛型约束方式，用于限制类型参数必须满足某些条件。可以使用接口、类型别名、联合类型、类等作为约束。理解 `extends` 约束的使用是学习 TypeScript 泛型的关键。

## 相关资源

- [TypeScript extends 约束文档](https://www.typescriptlang.org/docs/handbook/2/generics.html#generic-constraints)
