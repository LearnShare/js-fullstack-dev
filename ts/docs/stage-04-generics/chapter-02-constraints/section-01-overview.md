# 4.2.1 泛型约束概述

## 概述

泛型约束允许限制类型参数的范围，确保类型参数具有某些属性或方法。本节介绍泛型约束的概念、作用和优势。

## 什么是泛型约束

### 定义

泛型约束使用 `extends` 关键字限制类型参数必须满足某些条件。

### 基本概念

```ts
// 不使用约束：可能访问不存在的属性
function getLength<T>(value: T): number {
    // return value.length; // 错误：T 可能没有 length 属性
    return 0;
}

// 使用约束：确保类型参数有 length 属性
function getLength<T extends { length: number }>(value: T): number {
    return value.length; // 正确：T 必须有 length 属性
}
```

## 泛型约束的作用

### 1. 类型安全

约束确保类型参数具有必要的属性或方法：

```ts
interface HasLength {
    length: number;
}

function getLength<T extends HasLength>(value: T): number {
    return value.length; // 类型安全
}
```

### 2. 访问属性

约束允许访问类型参数的属性：

```ts
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key]; // 可以访问属性
}
```

### 3. 限制范围

约束限制类型参数的范围：

```ts
function process<T extends string | number>(value: T): T {
    return value; // T 只能是 string 或 number
}
```

## 约束类型

### 1. 接口约束

```ts
interface HasId {
    id: number;
}

function process<T extends HasId>(value: T): number {
    return value.id;
}
```

### 2. 类型别名约束

```ts
type HasName = {
    name: string;
};

function process<T extends HasName>(value: T): string {
    return value.name;
}
```

### 3. 联合类型约束

```ts
function process<T extends string | number>(value: T): T {
    return value;
}
```

### 4. 类约束

```ts
class Animal {
    name: string;
}

function process<T extends Animal>(value: T): string {
    return value.name;
}
```

## 约束的优势

### 1. 类型安全

约束提供类型安全：

```ts
interface HasLength {
    length: number;
}

function getLength<T extends HasLength>(value: T): number {
    return value.length; // 类型安全
}
```

### 2. 更好的 IDE 支持

约束提供更好的 IDE 支持：

```ts
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key]; // IDE 知道返回值的类型
}
```

### 3. 代码复用

约束允许编写可重用的代码：

```ts
function process<T extends { id: number }>(value: T): number {
    return value.id; // 可以处理任何有 id 属性的类型
}
```

## 约束 vs 无约束

### 对比

| 特性       | 有约束                     | 无约束                     |
|:-----------|:---------------------------|:---------------------------|
| 类型安全   | 高                         | 低                         |
| 访问属性   | 可以访问约束的属性         | 不能访问特定属性           |
| 灵活性     | 中等                       | 高                         |
| 使用场景   | 需要访问特定属性或方法     | 不需要特定属性或方法       |

### 示例对比

```ts
// 无约束：不能访问特定属性
function process<T>(value: T): T {
    // return value.length; // 错误：T 可能没有 length 属性
    return value;
}

// 有约束：可以访问约束的属性
function process<T extends { length: number }>(value: T): T {
    console.log(value.length); // 正确：T 必须有 length 属性
    return value;
}
```

## 使用场景

### 1. 访问对象属性

```ts
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key];
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

1. **约束概念**：理解泛型约束的概念和作用。

2. **接口约束**：定义使用接口约束的泛型函数。

3. **类型约束**：定义使用类型别名约束的泛型函数。

4. **实际应用**：在实际场景中应用泛型约束。

完成以上练习后，继续学习下一节，了解 extends 约束。

## 总结

泛型约束允许限制类型参数的范围，确保类型参数具有某些属性或方法。约束提供类型安全、更好的 IDE 支持和代码复用。理解泛型约束的概念和作用是学习 TypeScript 泛型的关键。

## 相关资源

- [TypeScript 泛型约束文档](https://www.typescriptlang.org/docs/handbook/2/generics.html#generic-constraints)
