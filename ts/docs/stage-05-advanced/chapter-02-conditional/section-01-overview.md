# 5.2.1 条件类型概述

## 概述

条件类型允许根据条件选择类型。本节介绍条件类型的概念、作用和语法。

## 什么是条件类型

### 定义

条件类型是一种类型级别的条件表达式，根据条件选择不同的类型。

### 基本语法

```ts
type ConditionalType<T> = T extends U ? X : Y;
```

### 示例

```ts
type IsString<T> = T extends string ? true : false;

type A = IsString<string>;  // true
type B = IsString<number>;   // false
```

## 条件类型的作用

### 1. 类型选择

条件类型可以根据条件选择类型：

```ts
type NonNullable<T> = T extends null | undefined ? never : T;

type A = NonNullable<string | null>;  // string
type B = NonNullable<number | undefined>; // number
```

### 2. 类型过滤

条件类型可以过滤类型：

```ts
type FilterString<T> = T extends string ? T : never;

type A = FilterString<string | number | boolean>; // string
```

### 3. 类型转换

条件类型可以转换类型：

```ts
type ToArray<T> = T extends any ? T[] : never;

type A = ToArray<string>; // string[]
```

## 条件类型语法

### 基本语法

```ts
T extends U ? X : Y
```

- `T extends U`：条件检查
- `X`：条件为真时的类型
- `Y`：条件为假时的类型

### 嵌套条件

```ts
type TypeName<T> =
    T extends string ? "string" :
    T extends number ? "number" :
    T extends boolean ? "boolean" :
    "unknown";
```

## 条件类型的优势

### 1. 类型安全

条件类型提供类型安全：

```ts
type NonNullable<T> = T extends null | undefined ? never : T;
// 确保类型不为 null 或 undefined
```

### 2. 类型推导

条件类型支持类型推导：

```ts
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : any;
// 可以推导函数返回类型
```

### 3. 代码复用

条件类型提高代码复用：

```ts
type NonNullable<T> = T extends null | undefined ? never : T;
// 可以用于任何类型
```

## 使用场景

### 1. 类型工具

```ts
type NonNullable<T> = T extends null | undefined ? never : T;
type NonNull<T> = T extends null ? never : T;
```

### 2. 类型提取

```ts
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : any;
type Parameters<T> = T extends (...args: infer P) => any ? P : never;
```

### 3. 类型过滤

```ts
type FilterFunction<T> = T extends Function ? T : never;
```

## 注意事项

1. **条件检查**：使用 `extends` 进行条件检查
2. **类型推导**：可以使用 `infer` 进行类型推导
3. **分布式**：条件类型对联合类型是分布式的
4. **嵌套**：可以嵌套使用条件类型

## 最佳实践

1. **使用条件类型**：在需要条件判断时使用条件类型
2. **类型推导**：使用 `infer` 进行类型推导
3. **理解分布式**：理解条件类型的分布式行为
4. **类型安全**：利用条件类型提高类型安全

## 练习

1. **条件类型概念**：理解条件类型的概念和作用。

2. **基本语法**：练习条件类型的基本语法。

3. **类型选择**：使用条件类型选择类型。

4. **实际应用**：在实际场景中应用条件类型。

完成以上练习后，继续学习下一节，了解条件类型基础。

## 总结

条件类型允许根据条件选择类型。条件类型提供类型安全、类型推导和代码复用。理解条件类型的概念和作用是学习 TypeScript 高级类型系统的关键。

## 相关资源

- [TypeScript 条件类型文档](https://www.typescriptlang.org/docs/handbook/2/conditional-types.html)
