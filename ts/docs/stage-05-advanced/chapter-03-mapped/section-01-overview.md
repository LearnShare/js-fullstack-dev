# 5.3.1 映射类型概述

## 概述

映射类型允许基于旧类型创建新类型。本节介绍映射类型的概念、作用和语法。

## 什么是映射类型

### 定义

映射类型是一种类型转换机制，允许基于现有类型的键创建新类型。

### 基本语法

```ts
type MappedType<T> = {
    [P in keyof T]: T[P];
};
```

### 示例

```ts
interface User {
    name: string;
    age: number;
}

type ReadonlyUser = {
    readonly [P in keyof User]: User[P];
};
// { readonly name: string; readonly age: number; }
```

## 映射类型的作用

### 1. 类型转换

映射类型可以转换类型：

```ts
type Partial<T> = {
    [P in keyof T]?: T[P];
};

type Readonly<T> = {
    readonly [P in keyof T]: T[P];
};
```

### 2. 类型选择

映射类型可以选择类型：

```ts
type Pick<T, K extends keyof T> = {
    [P in K]: T[P];
};
```

### 3. 类型构造

映射类型可以构造新类型：

```ts
type Record<K extends keyof any, T> = {
    [P in K]: T;
};
```

## 映射类型语法

### 基本语法

```ts
{
    [P in keyof T]: T[P];
}
```

- `P in keyof T`：遍历 T 的所有键
- `T[P]`：访问 T 的属性类型

### 修改属性

```ts
// 可选属性
type Partial<T> = {
    [P in keyof T]?: T[P];
};

// 只读属性
type Readonly<T> = {
    readonly [P in keyof T]: T[P];
};

// 必需属性
type Required<T> = {
    [P in keyof T]-?: T[P];
};
```

## 映射类型的优势

### 1. 类型安全

映射类型提供类型安全：

```ts
type Readonly<T> = {
    readonly [P in keyof T]: T[P];
};
// 所有属性都是只读的
```

### 2. 代码复用

映射类型提高代码复用：

```ts
type Partial<T> = {
    [P in keyof T]?: T[P];
};
// 可以用于任何类型
```

### 3. 类型推导

映射类型支持类型推导：

```ts
type Mapped<T> = {
    [P in keyof T]: T[P];
};
// TypeScript 可以推导类型
```

## 使用场景

### 1. 工具类型

```ts
type Partial<T> = {
    [P in keyof T]?: T[P];
};

type Readonly<T> = {
    readonly [P in keyof T]: T[P];
};
```

### 2. 类型选择

```ts
type Pick<T, K extends keyof T> = {
    [P in K]: T[P];
};
```

### 3. 类型构造

```ts
type Record<K extends keyof any, T> = {
    [P in K]: T;
};
```

## 注意事项

1. **键遍历**：使用 `in keyof` 遍历键
2. **属性访问**：使用索引访问类型访问属性
3. **修改属性**：可以修改属性特性
4. **类型安全**：映射类型提供类型安全

## 最佳实践

1. **使用映射类型**：在需要类型转换时使用映射类型
2. **理解语法**：理解映射类型的语法
3. **类型安全**：利用映射类型提高类型安全
4. **代码复用**：使用映射类型提高代码复用

## 练习

1. **映射类型概念**：理解映射类型的概念和作用。

2. **基本语法**：练习映射类型的基本语法。

3. **类型转换**：使用映射类型转换类型。

4. **实际应用**：在实际场景中应用映射类型。

完成以上练习后，继续学习下一节，了解映射类型基础。

## 总结

映射类型允许基于旧类型创建新类型。映射类型提供类型安全、代码复用和类型推导。理解映射类型的概念和作用是学习 TypeScript 高级类型系统的关键。

## 相关资源

- [TypeScript 映射类型文档](https://www.typescriptlang.org/docs/handbook/2/mapped-types.html)
