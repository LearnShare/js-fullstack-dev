# 5.3.2 映射类型基础

## 概述

本节介绍映射类型的基本用法，包括基本语法、属性修改和实际应用。

## 基本语法

### 遍历键

```ts
type MappedType<T> = {
    [P in keyof T]: T[P];
};

interface User {
    name: string;
    age: number;
}

type MappedUser = MappedType<User>;
// { name: string; age: number; }
```

### 修改属性类型

```ts
type Stringify<T> = {
    [P in keyof T]: string;
};

interface User {
    name: string;
    age: number;
}

type StringifiedUser = Stringify<User>;
// { name: string; age: string; }
```

## 属性修改

### 可选属性

```ts
type Partial<T> = {
    [P in keyof T]?: T[P];
};

interface User {
    name: string;
    age: number;
}

type PartialUser = Partial<User>;
// { name?: string; age?: number; }
```

### 只读属性

```ts
type Readonly<T> = {
    readonly [P in keyof T]: T[P];
};

interface User {
    name: string;
    age: number;
}

type ReadonlyUser = Readonly<User>;
// { readonly name: string; readonly age: number; }
```

### 必需属性

```ts
type Required<T> = {
    [P in keyof T]-?: T[P];
};

interface User {
    name?: string;
    age?: number;
}

type RequiredUser = Required<User>;
// { name: string; age: number; }
```

## 条件映射

### 条件类型结合

```ts
type NonNullable<T> = {
    [P in keyof T]: T[P] extends null | undefined ? never : T[P];
};

interface User {
    name: string | null;
    age: number;
}

type NonNullUser = NonNullable<User>;
// { name: string; age: number; }
```

### 过滤属性

```ts
type FilterFunction<T> = {
    [P in keyof T]: T[P] extends Function ? T[P] : never;
};

interface User {
    name: string;
    greet: () => void;
    age: number;
}

type FunctionProps = FilterFunction<User>;
// { name: never; greet: () => void; age: never; }
```

## 使用场景

### 1. 创建工具类型

```ts
type Partial<T> = {
    [P in keyof T]?: T[P];
};

type Readonly<T> = {
    readonly [P in keyof T]: T[P];
};
```

### 2. 类型转换

```ts
type Stringify<T> = {
    [P in keyof T]: string;
};

type Numberify<T> = {
    [P in keyof T]: number;
};
```

### 3. 类型选择

```ts
type Pick<T, K extends keyof T> = {
    [P in K]: T[P];
};
```

## 常见错误

### 错误 1：语法错误

```ts
// 错误：映射类型语法不正确
type Invalid = {
    P in keyof T: T[P];
};

// 正确
type Valid<T> = {
    [P in keyof T]: T[P];
};
```

### 错误 2：键不存在

```ts
// 错误：不能访问不存在的键
type Invalid<T> = {
    [P in keyof T]: T[InvalidKey];
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

1. **基本语法**：练习映射类型的基本语法。

2. **属性修改**：使用映射类型修改属性特性。

3. **条件映射**：结合条件类型使用映射类型。

4. **实际应用**：在实际场景中应用映射类型。

完成以上练习后，继续学习下一节，了解键重映射。

## 总结

映射类型允许遍历类型的键并创建新类型。可以修改属性特性，结合条件类型使用。理解映射类型的基础用法是学习高级类型系统的关键。

## 相关资源

- [TypeScript 映射类型文档](https://www.typescriptlang.org/docs/handbook/2/mapped-types.html)
