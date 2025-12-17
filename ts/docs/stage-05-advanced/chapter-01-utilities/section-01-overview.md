# 5.1.1 工具类型概述

## 概述

工具类型是 TypeScript 提供的用于类型转换的内置类型。本节介绍工具类型的概念、作用和分类。

## 什么是工具类型

### 定义

工具类型是用于转换和操作其他类型的类型，通常基于泛型、条件类型和映射类型实现。

### 基本概念

```ts
interface User {
    name: string;
    age: number;
    email: string;
}

// 使用工具类型转换类型
type PartialUser = Partial<User>;
// { name?: string; age?: number; email?: string; }

type ReadonlyUser = Readonly<User>;
// { readonly name: string; readonly age: number; readonly email: string; }
```

## 工具类型的作用

### 1. 类型转换

工具类型可以转换现有类型：

```ts
interface User {
    name: string;
    age: number;
}

type PartialUser = Partial<User>;
// 所有属性变为可选
```

### 2. 类型选择

工具类型可以选择类型的部分属性：

```ts
interface User {
    name: string;
    age: number;
    email: string;
}

type UserName = Pick<User, "name">;
// { name: string; }
```

### 3. 类型构造

工具类型可以构造新类型：

```ts
type StringRecord = Record<string, string>;
// { [key: string]: string; }
```

## 工具类型分类

### 1. 基础工具类型

- `Partial<T>`：所有属性变为可选
- `Required<T>`：所有属性变为必需
- `Readonly<T>`：所有属性变为只读

### 2. 选择工具类型

- `Pick<T, K>`：选择类型的部分属性
- `Omit<T, K>`：排除类型的部分属性

### 3. 构造工具类型

- `Record<K, V>`：构造记录类型
- `Exclude<T, U>`：从类型中排除某些类型
- `Extract<T, U>`：从类型中提取某些类型

### 4. 函数工具类型

- `Parameters<T>`：获取函数参数类型
- `ReturnType<T>`：获取函数返回类型

## 工具类型的优势

### 1. 类型安全

工具类型提供类型安全：

```ts
type PartialUser = Partial<User>;
// 类型安全，所有属性都是可选的
```

### 2. 代码复用

工具类型提高代码复用：

```ts
// 不需要为每个类型定义 Partial 版本
type PartialUser = Partial<User>;
type PartialProduct = Partial<Product>;
```

### 3. 类型推导

工具类型支持类型推导：

```ts
function process<T>(value: Partial<T>): T {
    // TypeScript 可以推导类型
}
```

## 使用场景

### 1. API 请求/响应

```ts
interface CreateUserRequest {
    name: string;
    email: string;
}

type UpdateUserRequest = Partial<CreateUserRequest>;
// 更新时所有字段都是可选的
```

### 2. 表单处理

```ts
interface FormData {
    name: string;
    email: string;
    age: number;
}

type FormErrors = Partial<Record<keyof FormData, string>>;
// 每个字段可能有错误信息
```

### 3. 状态管理

```ts
interface State {
    user: User;
    loading: boolean;
}

type StateUpdate = Partial<State>;
// 可以部分更新状态
```

## 注意事项

1. **类型转换**：工具类型是类型转换，不影响运行时
2. **类型推导**：工具类型支持类型推导
3. **组合使用**：可以组合使用多个工具类型
4. **自定义类型**：可以创建自定义工具类型

## 最佳实践

1. **使用内置类型**：优先使用 TypeScript 内置工具类型
2. **理解原理**：理解工具类型的实现原理
3. **自定义类型**：在需要时创建自定义工具类型
4. **类型安全**：利用工具类型提高类型安全

## 练习

1. **工具类型概念**：理解工具类型的概念和作用。

2. **类型转换**：使用工具类型转换类型。

3. **类型选择**：使用工具类型选择类型属性。

4. **实际应用**：在实际场景中应用工具类型。

完成以上练习后，继续学习下一节，了解基础工具类型。

## 总结

工具类型是 TypeScript 提供的用于类型转换的内置类型。工具类型可以转换类型、选择属性、构造新类型。理解工具类型的概念和作用是学习 TypeScript 高级类型系统的关键。

## 相关资源

- [TypeScript 工具类型文档](https://www.typescriptlang.org/docs/handbook/utility-types.html)
