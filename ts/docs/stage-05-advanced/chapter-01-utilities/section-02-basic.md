# 5.1.2 基础工具类型（Partial、Required、Readonly）

## 概述

基础工具类型用于修改类型的属性特性。本节介绍 Partial、Required、Readonly 的使用。

## Partial

### 定义

`Partial<T>` 将类型 `T` 的所有属性变为可选。

### 语法

```ts
type Partial<T> = {
    [P in keyof T]?: T[P];
};
```

### 示例

```ts
interface User {
    name: string;
    age: number;
    email: string;
}

type PartialUser = Partial<User>;
// { name?: string; age?: number; email?: string; }

let user: PartialUser = {
    name: "John"
    // age 和 email 是可选的
};
```

### 使用场景

```ts
// API 更新请求
interface User {
    name: string;
    age: number;
    email: string;
}

function updateUser(id: number, data: Partial<User>): void {
    // 可以只更新部分字段
}
```

## Required

### 定义

`Required<T>` 将类型 `T` 的所有属性变为必需。

### 语法

```ts
type Required<T> = {
    [P in keyof T]-?: T[P];
};
```

### 示例

```ts
interface User {
    name?: string;
    age?: number;
    email?: string;
}

type RequiredUser = Required<User>;
// { name: string; age: number; email: string; }

let user: RequiredUser = {
    name: "John",
    age: 30,
    email: "john@example.com"
    // 所有属性都是必需的
};
```

### 使用场景

```ts
// 确保所有字段都有值
interface Config {
    apiUrl?: string;
    timeout?: number;
}

function initialize(config: Required<Config>): void {
    // 所有配置项都是必需的
}
```

## Readonly

### 定义

`Readonly<T>` 将类型 `T` 的所有属性变为只读。

### 语法

```ts
type Readonly<T> = {
    readonly [P in keyof T]: T[P];
};
```

### 示例

```ts
interface User {
    name: string;
    age: number;
}

type ReadonlyUser = Readonly<User>;
// { readonly name: string; readonly age: number; }

let user: ReadonlyUser = {
    name: "John",
    age: 30
};

// user.name = "Jane"; // 错误：不能修改只读属性
```

### 使用场景

```ts
// 不可变数据
interface State {
    user: User;
    count: number;
}

function getState(): Readonly<State> {
    return { user, count };
}
```

## 组合使用

### 组合多个工具类型

```ts
interface User {
    name: string;
    age: number;
    email: string;
}

// 只读且部分可选
type ReadonlyPartialUser = Readonly<Partial<User>>;
// { readonly name?: string; readonly age?: number; readonly email?: string; }
```

## 常见错误

### 错误 1：类型不匹配

```ts
interface User {
    name: string;
}

let user: Partial<User> = {
    name: "John",
    age: 30 // 错误：age 不在 User 中
};
```

### 错误 2：修改只读属性

```ts
let user: Readonly<User> = { name: "John" };
// user.name = "Jane"; // 错误：不能修改只读属性
```

## 注意事项

1. **类型转换**：工具类型是类型转换，不影响运行时
2. **深度只读**：Readonly 只影响第一层属性
3. **组合使用**：可以组合使用多个工具类型
4. **类型推导**：工具类型支持类型推导

## 最佳实践

1. **使用 Partial**：在更新操作中使用 Partial
2. **使用 Required**：在需要所有字段时使用 Required
3. **使用 Readonly**：在需要不可变数据时使用 Readonly
4. **组合使用**：合理组合使用多个工具类型

## 练习

1. **Partial**：使用 Partial 创建可选属性类型。

2. **Required**：使用 Required 创建必需属性类型。

3. **Readonly**：使用 Readonly 创建只读属性类型。

4. **组合使用**：组合使用多个工具类型。

5. **实际应用**：在实际场景中应用基础工具类型。

完成以上练习后，继续学习下一节，了解选择工具类型。

## 总结

Partial、Required、Readonly 是基础工具类型，用于修改类型的属性特性。Partial 使属性可选，Required 使属性必需，Readonly 使属性只读。理解这些工具类型的使用是学习 TypeScript 工具类型的关键。

## 相关资源

- [TypeScript Partial 文档](https://www.typescriptlang.org/docs/handbook/utility-types.html#partialtype)
- [TypeScript Required 文档](https://www.typescriptlang.org/docs/handbook/utility-types.html#requiredtype)
- [TypeScript Readonly 文档](https://www.typescriptlang.org/docs/handbook/utility-types.html#readonlytype)
