# 5.5.2 复杂类型推导

## 概述

本节介绍复杂类型推导的技巧，包括多级推断、条件推断和组合推断。

## 多级推断

### 嵌套 infer

```ts
type UnwrapPromise<T> = T extends Promise<infer U>
    ? U extends Promise<infer V>
        ? UnwrapPromise<V>
        : U
    : T;

type A = UnwrapPromise<Promise<Promise<string>>>; // string
```

### 数组元素推断

```ts
type FirstElement<T> = T extends [infer First, ...any[]] ? First : never;

type A = FirstElement<[string, number, boolean]>; // string
```

### 数组尾部推断

```ts
type Tail<T> = T extends [any, ...infer Rest] ? Rest : never;

type A = Tail<[string, number, boolean]>; // [number, boolean]
```

## 条件推断

### 条件类型推断

```ts
type IsFunction<T> = T extends (...args: any[]) => any ? true : false;

type A = IsFunction<() => void>; // true
type B = IsFunction<string>;      // false
```

### 条件数组推断

```ts
type IsArray<T> = T extends (infer U)[] ? true : false;

type A = IsArray<string[]>;  // true
type B = IsArray<number>;    // false
```

## 组合推断

### 函数参数和返回类型

```ts
type FunctionInfo<T> = T extends (...args: infer P) => infer R
    ? { params: P; return: R }
    : never;

type A = FunctionInfo<(a: string, b: number) => boolean>;
// { params: [string, number]; return: boolean }
```

### 对象属性类型

```ts
type PropertyTypes<T> = {
    [K in keyof T]: T[K];
};

interface User {
    name: string;
    age: number;
}

type UserTypes = PropertyTypes<User>;
// { name: string; age: number }
```

## 实际应用

### 1. 提取 Promise 类型

```ts
type Awaited<T> = T extends Promise<infer U> ? Awaited<U> : T;

type A = Awaited<Promise<Promise<string>>>; // string
```

### 2. 提取数组元素

```ts
type Flatten<T> = T extends (infer U)[] ? U : T;

type A = Flatten<string[]>;  // string
type B = Flatten<number>;    // number
```

### 3. 提取函数信息

```ts
type FunctionSignature<T> = T extends (...args: infer P) => infer R
    ? { parameters: P; returnType: R }
    : never;
```

## 常见错误

### 错误 1：infer 位置错误

```ts
// 错误：infer 位置不正确
type Invalid<T> = infer U extends T ? U : never;

// 正确
type Valid<T> = T extends infer U ? U : never;
```

### 错误 2：推断失败

```ts
// 错误：无法推断类型
type Invalid<T> = T extends any ? infer U : never;

// 正确：infer 必须在条件类型的分支中
type Valid<T> = T extends (infer U) ? U : never;
```

## 注意事项

1. **infer 位置**：infer 必须在条件类型的分支中
2. **类型推断**：确保类型可以正确推断
3. **递归推断**：可以使用递归进行多级推断
4. **类型安全**：确保推断结果类型安全

## 最佳实践

1. **使用 infer**：在需要类型推断时使用 infer
2. **多级推断**：使用递归进行多级推断
3. **组合推断**：组合多个推断操作
4. **类型安全**：确保推断结果类型安全

## 练习

1. **多级推断**：进行多级类型推断。

2. **条件推断**：使用条件类型进行推断。

3. **组合推断**：组合多个推断操作。

4. **实际应用**：在实际场景中应用复杂类型推导。

完成以上练习后，继续学习下一节，了解类型递归。

## 总结

复杂类型推导使用 infer 关键字和条件类型进行多级推断。可以推断函数参数、返回类型、数组元素等。理解复杂类型推导的技巧是学习类型体操的关键。

## 相关资源

- [TypeScript infer 关键字文档](https://www.typescriptlang.org/docs/handbook/2/conditional-types.html#inferring-within-conditional-types)
