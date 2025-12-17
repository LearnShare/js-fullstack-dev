# 4.2.4 条件类型约束

## 概述

条件类型约束允许根据条件限制类型参数。本节介绍条件类型约束的使用。

## 条件类型基础

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

## 条件类型约束

### 在泛型中使用

```ts
type NonNullable<T> = T extends null | undefined ? never : T;

function process<T>(value: NonNullable<T>): T {
    return value;
}
```

### 约束类型参数

```ts
type ExtractString<T> = T extends string ? T : never;

function process<T extends ExtractString<T>>(value: T): T {
    return value;
}
```

## 分布式条件类型

### 联合类型分发

```ts
type ToArray<T> = T extends any ? T[] : never;

type StrArrOrNumArr = ToArray<string | number>;
// string[] | number[]
```

### 非分布式条件类型

```ts
type ToArray<T> = [T] extends [any] ? T[] : never;

type StrArrOrNumArr = ToArray<string | number>;
// (string | number)[]
```

## infer 关键字

### 类型推断

```ts
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : any;

type Func = () => string;
type R = ReturnType<Func>; // string
```

### 在约束中使用

```ts
type Parameters<T> = T extends (...args: infer P) => any ? P : never;

type Func = (a: string, b: number) => void;
type P = Parameters<Func>; // [string, number]
```

## 使用场景

### 1. 类型提取

```ts
type ExtractProperty<T, K extends keyof T> = T[K];

interface User {
    name: string;
    age: number;
}

type Name = ExtractProperty<User, "name">; // string
```

### 2. 类型过滤

```ts
type FilterString<T> = T extends string ? T : never;

type A = FilterString<string | number | boolean>; // string
```

### 3. 类型转换

```ts
type ToReadonly<T> = {
    readonly [P in keyof T]: T[P];
};
```

## 常见错误

### 错误 1：条件类型语法错误

```ts
// 错误：条件类型语法不正确
type IsString<T> = T extends string ? true : false;

// 正确
type IsString<T> = T extends string ? true : false;
```

### 错误 2：infer 使用错误

```ts
// 错误：infer 只能在条件类型中使用
type ReturnType<T> = infer R;

// 正确
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : any;
```

## 注意事项

1. **条件语法**：条件类型使用三元运算符
2. **分布式**：条件类型对联合类型是分布式的
3. **infer 关键字**：`infer` 用于类型推断
4. **约束位置**：条件类型约束在类型参数后

## 最佳实践

1. **使用条件类型**：在需要条件判断时使用条件类型
2. **类型推断**：使用 `infer` 进行类型推断
3. **分布式理解**：理解条件类型的分布式行为
4. **类型安全**：利用条件类型提高类型安全

## 练习

1. **条件类型**：定义不同类型的条件类型。

2. **类型推断**：使用 infer 进行类型推断。

3. **分布式类型**：理解条件类型的分布式行为。

4. **实际应用**：在实际场景中应用条件类型约束。

完成以上练习后，泛型约束章节学习完成。可以继续学习下一章：泛型实战。

## 总结

条件类型约束允许根据条件限制类型参数。可以使用 `infer` 关键字进行类型推断，条件类型对联合类型是分布式的。理解条件类型约束的使用是学习 TypeScript 泛型的关键。

## 相关资源

- [TypeScript 条件类型文档](https://www.typescriptlang.org/docs/handbook/2/conditional-types.html)
