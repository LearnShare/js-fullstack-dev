# 5.2.4 infer 关键字

## 概述

`infer` 关键字用于在条件类型中进行类型推断。本节介绍 `infer` 关键字的使用。

## 什么是 infer

### 定义

`infer` 关键字用于在条件类型中声明一个类型变量，用于推断类型。

### 基本语法

```ts
type InferType<T> = T extends (infer U) ? U : never;
```

### 示例

```ts
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : any;

type Func = () => string;
type R = ReturnType<Func>; // string
```

## infer 的使用

### 推断返回类型

```ts
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : any;

function add(a: number, b: number): number {
    return a + b;
}

type AddReturn = ReturnType<typeof add>; // number
```

### 推断参数类型

```ts
type Parameters<T> = T extends (...args: infer P) => any ? P : never;

function process(name: string, age: number): void {
    // ...
}

type ProcessParams = Parameters<typeof process>; // [string, number]
```

### 推断数组元素类型

```ts
type ArrayElement<T> = T extends (infer U)[] ? U : never;

type A = ArrayElement<string[]>;  // string
type B = ArrayElement<number[]>;  // number
```

### 推断 Promise 类型

```ts
type Awaited<T> = T extends Promise<infer U> ? U : T;

type A = Awaited<Promise<string>>; // string
type B = Awaited<string>;           // string
```

## 多个 infer

### 推断多个类型

```ts
type FirstAndRest<T> = T extends [infer First, ...infer Rest] 
    ? { first: First; rest: Rest } 
    : never;

type A = FirstAndRest<[string, number, boolean]>;
// { first: string; rest: [number, boolean] }
```

## 实际应用

### 1. ReturnType 实现

```ts
type ReturnType<T extends (...args: any) => any> = 
    T extends (...args: any) => infer R ? R : any;
```

### 2. Parameters 实现

```ts
type Parameters<T extends (...args: any) => any> = 
    T extends (...args: infer P) => any ? P : never;
```

### 3. InstanceType 实现

```ts
type InstanceType<T extends new (...args: any) => any> = 
    T extends new (...args: any) => infer R ? R : any;
```

### 4. 提取数组元素

```ts
type Flatten<T> = T extends (infer U)[] ? U : T;

type A = Flatten<string[]>;  // string
type B = Flatten<number>;    // number
```

## 常见错误

### 错误 1：infer 位置错误

```ts
// 错误：infer 只能在条件类型中使用
type Invalid = infer U;

// 正确
type Valid<T> = T extends (infer U) ? U : never;
```

### 错误 2：infer 类型推断失败

```ts
// 错误：无法推断类型
type Invalid<T> = T extends any ? infer U : never;

// 正确：infer 必须在条件类型的分支中
type Valid<T> = T extends (infer U) ? U : never;
```

## 注意事项

1. **infer 位置**：`infer` 只能在条件类型中使用
2. **类型推断**：`infer` 用于推断类型
3. **多个 infer**：可以使用多个 `infer` 推断多个类型
4. **类型安全**：`infer` 提供类型安全

## 最佳实践

1. **使用 infer**：在需要类型推断时使用 `infer`
2. **明确推断**：明确要推断的类型位置
3. **多个推断**：在需要时使用多个 `infer`
4. **类型安全**：利用 `infer` 提高类型安全

## 练习

1. **infer 基础**：使用 infer 推断函数返回类型。

2. **参数推断**：使用 infer 推断函数参数类型。

3. **数组推断**：使用 infer 推断数组元素类型。

4. **实际应用**：在实际场景中应用 infer 关键字。

完成以上练习后，条件类型章节学习完成。可以继续学习下一章：映射类型。

## 总结

`infer` 关键字用于在条件类型中进行类型推断。可以推断函数返回类型、参数类型、数组元素类型等。理解 `infer` 关键字的使用是学习 TypeScript 高级类型系统的关键。

## 相关资源

- [TypeScript infer 关键字文档](https://www.typescriptlang.org/docs/handbook/2/conditional-types.html#inferring-within-conditional-types)
