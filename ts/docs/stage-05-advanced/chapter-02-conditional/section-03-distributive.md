# 5.2.3 分布式条件类型

## 概述

分布式条件类型是条件类型的一个重要特性，当条件类型作用于联合类型时，会分布到每个成员上。本节介绍分布式条件类型的行为和使用。

## 什么是分布式条件类型

### 定义

当条件类型作用于联合类型时，TypeScript 会将条件类型分布到联合类型的每个成员上。

### 基本行为

```ts
type ToArray<T> = T extends any ? T[] : never;

type A = ToArray<string | number>;
// 分布为：(string extends any ? string[] : never) | (number extends any ? number[] : never)
// 结果：string[] | number[]
```

## 分布式行为

### 示例 1：数组转换

```ts
type ToArray<T> = T extends any ? T[] : never;

type A = ToArray<string | number>;
// string[] | number[]

// 非分布式版本
type ToArrayNonDist<T> = [T] extends [any] ? T[] : never;

type B = ToArrayNonDist<string | number>;
// (string | number)[]
```

### 示例 2：类型过滤

```ts
type FilterString<T> = T extends string ? T : never;

type A = FilterString<string | number | boolean>;
// 分布为：(string extends string ? string : never) | (number extends string ? number : never) | (boolean extends string ? boolean : never)
// 结果：string
```

## 非分布式条件类型

### 使用元组包装

```ts
// 分布式
type Distributed<T> = T extends any ? T[] : never;

// 非分布式
type NonDistributed<T> = [T] extends [any] ? T[] : never;

type A = Distributed<string | number>;      // string[] | number[]
type B = NonDistributed<string | number>;   // (string | number)[]
```

## 使用场景

### 1. 类型过滤

```ts
type FilterFunction<T> = T extends Function ? T : never;

type A = FilterFunction<string | (() => void) | number>;
// () => void
```

### 2. 类型排除

```ts
type ExcludeNull<T> = T extends null ? never : T;

type A = ExcludeNull<string | null | number>;
// string | number
```

### 3. 类型提取

```ts
type ExtractString<T> = T extends string ? T : never;

type A = ExtractString<string | number | boolean>;
// string
```

## 常见错误

### 错误 1：不理解分布式行为

```ts
type ToArray<T> = T extends any ? T[] : never;

// 可能期望得到 (string | number)[]
// 实际得到 string[] | number[]
type A = ToArray<string | number>;
```

### 错误 2：需要非分布式行为

```ts
// 错误：使用了分布式条件类型
type ToArray<T> = T extends any ? T[] : never;

// 正确：使用非分布式条件类型
type ToArray<T> = [T] extends [any] ? T[] : never;
```

## 注意事项

1. **分布式行为**：条件类型对联合类型是分布式的
2. **元组包装**：使用元组可以避免分布式行为
3. **类型安全**：分布式行为提供类型安全
4. **性能考虑**：分布式条件类型可能影响编译性能

## 最佳实践

1. **理解行为**：理解分布式条件类型的行为
2. **选择合适**：根据需求选择分布式或非分布式
3. **类型安全**：利用分布式行为提高类型安全
4. **性能优化**：在必要时避免分布式行为

## 练习

1. **分布式行为**：理解条件类型的分布式行为。

2. **类型过滤**：使用分布式条件类型过滤类型。

3. **非分布式**：使用元组包装避免分布式行为。

4. **实际应用**：在实际场景中应用分布式条件类型。

完成以上练习后，继续学习下一节，了解 infer 关键字。

## 总结

分布式条件类型是条件类型的重要特性，当作用于联合类型时会分布到每个成员上。可以使用元组包装避免分布式行为。理解分布式条件类型的行为是学习高级类型系统的关键。

## 相关资源

- [TypeScript 分布式条件类型文档](https://www.typescriptlang.org/docs/handbook/2/conditional-types.html#distributive-conditional-types)
