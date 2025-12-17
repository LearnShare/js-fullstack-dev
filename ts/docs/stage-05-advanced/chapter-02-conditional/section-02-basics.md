# 5.2.2 条件类型基础

## 概述

本节介绍条件类型的基本用法，包括基本语法、嵌套条件和实际应用。

## 基本语法

### 三元运算符

条件类型使用三元运算符语法：

```ts
type ConditionalType<T> = T extends U ? X : Y;
```

### 示例

```ts
type IsString<T> = T extends string ? true : false;

type A = IsString<string>;  // true
type B = IsString<number>;   // false
type C = IsString<boolean>;  // false
```

## 类型检查

### extends 检查

条件类型使用 `extends` 进行类型检查：

```ts
type IsArray<T> = T extends any[] ? true : false;

type A = IsArray<string[]>;  // true
type B = IsArray<number>;    // false
```

### 联合类型检查

```ts
type IsStringOrNumber<T> = T extends string | number ? true : false;

type A = IsStringOrNumber<string>;  // true
type B = IsStringOrNumber<number>;  // true
type C = IsStringOrNumber<boolean>; // false
```

## 嵌套条件

### 多条件判断

```ts
type TypeName<T> =
    T extends string ? "string" :
    T extends number ? "number" :
    T extends boolean ? "boolean" :
    "unknown";

type A = TypeName<string>;   // "string"
type B = TypeName<number>;   // "number"
type C = TypeName<boolean>;  // "boolean"
type D = TypeName<object>;    // "unknown"
```

### 复杂条件

```ts
type IsPrimitive<T> =
    T extends string ? true :
    T extends number ? true :
    T extends boolean ? true :
    false;
```

## 类型转换

### 转换为数组

```ts
type ToArray<T> = T extends any ? T[] : never;

type A = ToArray<string>;  // string[]
type B = ToArray<number>;  // number[]
```

### 转换为可选

```ts
type ToOptional<T> = T extends any ? T | undefined : never;

type A = ToOptional<string>;  // string | undefined
```

## 使用场景

### 1. 类型过滤

```ts
type FilterString<T> = T extends string ? T : never;

type A = FilterString<string | number | boolean>; // string
```

### 2. 类型排除

```ts
type ExcludeNull<T> = T extends null ? never : T;

type A = ExcludeNull<string | null>; // string
```

### 3. 类型选择

```ts
type SelectFunction<T> = T extends Function ? T : never;

type A = SelectFunction<string | (() => void)>; // () => void
```

## 常见错误

### 错误 1：语法错误

```ts
// 错误：条件类型语法不正确
type Invalid = T extends U ? X;

// 正确
type Valid = T extends U ? X : Y;
```

### 错误 2：类型不匹配

```ts
// 错误：条件检查失败
type Invalid = string extends number ? true : false;
// 结果总是 false
```

## 注意事项

1. **三元运算符**：条件类型必须使用三元运算符
2. **extends 检查**：使用 `extends` 进行类型检查
3. **嵌套条件**：可以嵌套使用条件类型
4. **类型推导**：条件类型支持类型推导

## 最佳实践

1. **明确条件**：使用明确的条件检查
2. **嵌套使用**：在需要多条件判断时使用嵌套条件
3. **类型安全**：利用条件类型提高类型安全
4. **代码复用**：使用条件类型提高代码复用

## 练习

1. **基本语法**：练习条件类型的基本语法。

2. **类型检查**：使用条件类型进行类型检查。

3. **嵌套条件**：定义嵌套条件类型。

4. **实际应用**：在实际场景中应用条件类型。

完成以上练习后，继续学习下一节，了解分布式条件类型。

## 总结

条件类型使用三元运算符语法，通过 `extends` 进行类型检查。可以嵌套使用条件类型，支持类型转换和类型过滤。理解条件类型的基础用法是学习高级类型系统的关键。

## 相关资源

- [TypeScript 条件类型文档](https://www.typescriptlang.org/docs/handbook/2/conditional-types.html)
