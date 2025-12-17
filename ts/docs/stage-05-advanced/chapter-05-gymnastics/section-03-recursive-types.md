# 5.5.3 类型递归

## 概述

类型递归允许类型定义引用自身，用于处理嵌套结构。本节介绍类型递归的使用。

## 什么是类型递归

### 定义

类型递归是类型定义引用自身的模式，用于处理嵌套或递归的数据结构。

### 基本概念

```ts
type DeepReadonly<T> = {
    readonly [P in keyof T]: T[P] extends object ? DeepReadonly<T[P]> : T[P];
};

interface User {
    name: string;
    address: {
        city: string;
        country: string;
    };
}

type ReadonlyUser = DeepReadonly<User>;
// {
//     readonly name: string;
//     readonly address: {
//         readonly city: string;
//         readonly country: string;
//     };
// }
```

## 深度类型转换

### 深度只读

```ts
type DeepReadonly<T> = {
    readonly [P in keyof T]: T[P] extends object
        ? T[P] extends Function
            ? T[P]
            : DeepReadonly<T[P]>
        : T[P];
};
```

### 深度可选

```ts
type DeepPartial<T> = {
    [P in keyof T]?: T[P] extends object ? DeepPartial<T[P]> : T[P];
};
```

### 深度必需

```ts
type DeepRequired<T> = {
    [P in keyof T]-?: T[P] extends object ? DeepRequired<T[P]> : T[P];
};
```

## 数组递归

### 展平数组

```ts
type Flatten<T> = T extends (infer U)[]
    ? U extends any[]
        ? Flatten<U>
        : U
    : T;

type A = Flatten<number[][]>; // number[]
```

### 数组深度

```ts
type ArrayDepth<T, D extends number = 0> = T extends (infer U)[]
    ? U extends any[]
        ? ArrayDepth<U, [...D[], any]>
        : D
    : never;
```

## 对象递归

### 深度合并

```ts
type DeepMerge<T, U> = {
    [K in keyof T | keyof U]: K extends keyof U
        ? K extends keyof T
            ? T[K] extends object
                ? U[K] extends object
                    ? DeepMerge<T[K], U[K]>
                    : U[K]
                : U[K]
            : U[K]
        : K extends keyof T
        ? T[K]
        : never;
}
```

## 使用场景

### 1. 深度只读

```ts
type DeepReadonly<T> = {
    readonly [P in keyof T]: T[P] extends object
        ? T[P] extends Function
            ? T[P]
            : DeepReadonly<T[P]>
        : T[P];
};
```

### 2. 深度可选

```ts
type DeepPartial<T> = {
    [P in keyof T]?: T[P] extends object ? DeepPartial<T[P]> : T[P];
};
```

### 3. 路径类型

```ts
type Paths<T> = T extends object
    ? {
          [K in keyof T]: K extends string
              ? T[K] extends object
                  ? K | `${K}.${Paths<T[K]>}`
                  : K
              : never;
      }[keyof T]
    : never;
```

## 常见错误

### 错误 1：无限递归

```ts
// 错误：可能导致无限递归
type Invalid<T> = T extends object ? Invalid<T> : T;

// 正确：添加终止条件
type Valid<T> = T extends object
    ? T extends Function
        ? T
        : { [P in keyof T]: Valid<T[P]> }
    : T;
```

### 错误 2：类型检查不足

```ts
// 错误：没有检查 Function
type Invalid<T> = {
    readonly [P in keyof T]: T[P] extends object ? Invalid<T[P]> : T[P];
};

// 正确：排除 Function
type Valid<T> = {
    readonly [P in keyof T]: T[P] extends object
        ? T[P] extends Function
            ? T[P]
            : Valid<T[P]>
        : T[P];
};
```

## 注意事项

1. **终止条件**：必须提供终止条件避免无限递归
2. **Function 检查**：需要排除 Function 类型
3. **性能考虑**：深度递归可能影响编译性能
4. **类型安全**：确保递归类型类型安全

## 最佳实践

1. **终止条件**：为递归类型提供终止条件
2. **Function 检查**：排除 Function 类型
3. **深度限制**：考虑递归深度限制
4. **类型安全**：确保递归类型类型安全

## 练习

1. **类型递归**：定义不同类型的递归类型。

2. **深度转换**：使用递归进行深度类型转换。

3. **终止条件**：为递归类型添加终止条件。

4. **实际应用**：在实际场景中应用类型递归。

完成以上练习后，继续学习下一节，了解实际应用案例。

## 总结

类型递归允许类型定义引用自身，用于处理嵌套结构。必须提供终止条件避免无限递归，需要排除 Function 类型。理解类型递归的使用是学习类型体操的关键。

## 相关资源

- [TypeScript 递归类型文档](https://www.typescriptlang.org/docs/handbook/2/types-from-types.html)
