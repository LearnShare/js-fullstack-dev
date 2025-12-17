# 5.3.4 模板字面量类型

## 概述

模板字面量类型允许使用模板字符串语法创建类型。本节介绍模板字面量类型的使用。

## 什么是模板字面量类型

### 定义

模板字面量类型是使用模板字符串语法创建的类型。

### 基本语法

```ts
type TemplateLiteral = `prefix_${string}`;
```

### 示例

```ts
type EventName = `on${string}`;
// "onclick" | "onchange" | "onfocus" | ...

type ApiEndpoint = `/api/${string}`;
// "/api/users" | "/api/posts" | ...
```

## 基本用法

### 字符串拼接

```ts
type Greeting<T extends string> = `Hello, ${T}!`;

type A = Greeting<"World">; // "Hello, World!"
```

### 联合类型

```ts
type Method = "GET" | "POST" | "PUT" | "DELETE";
type ApiRoute = `/api/${Method}`;
// "/api/GET" | "/api/POST" | "/api/PUT" | "/api/DELETE"
```

## 与映射类型结合

### 键重映射

```ts
type AddPrefix<T> = {
    [P in keyof T as `prefix_${string & P}`]: T[P];
};

interface User {
    name: string;
    age: number;
}

type PrefixedUser = AddPrefix<User>;
// { prefix_name: string; prefix_age: number; }
```

### 条件类型结合

```ts
type EventHandler<T extends string> = T extends `on${infer Event}`
    ? `handle${Capitalize<Event>}`
    : never;

type A = EventHandler<"onclick">; // "handleClick"
```

## 内置工具类型

### Uppercase

```ts
type Uppercase<S extends string> = intrinsic;

type A = Uppercase<"hello">; // "HELLO"
```

### Lowercase

```ts
type Lowercase<S extends string> = intrinsic;

type A = Lowercase<"HELLO">; // "hello"
```

### Capitalize

```ts
type Capitalize<S extends string> = intrinsic;

type A = Capitalize<"hello">; // "Hello"
```

### Uncapitalize

```ts
type Uncapitalize<S extends string> = intrinsic;

type A = Uncapitalize<"Hello">; // "hello"
```

## 使用场景

### 1. API 路由

```ts
type ApiRoute<T extends string> = `/api/${T}`;

type UsersRoute = ApiRoute<"users">; // "/api/users"
```

### 2. 事件处理

```ts
type EventName = `on${Capitalize<string>}`;
// "onClick" | "onChange" | "onFocus" | ...
```

### 3. CSS 类名

```ts
type CssClass<T extends string> = `btn-${T}`;

type PrimaryButton = CssClass<"primary">; // "btn-primary"
```

## 常见错误

### 错误 1：类型不匹配

```ts
// 错误：模板字面量类型使用错误
type Invalid = `prefix_${number}`;
// number 不能用于模板字面量类型
```

### 错误 2：联合类型错误

```ts
// 错误：联合类型使用错误
type Invalid<T> = `prefix_${T}`;
// T 必须是 string 类型
```

## 注意事项

1. **字符串类型**：模板字面量类型只能用于字符串类型
2. **类型转换**：需要将其他类型转换为 string
3. **工具类型**：可以使用内置工具类型
4. **类型安全**：模板字面量类型提供类型安全

## 最佳实践

1. **使用模板字面量**：在需要字符串模板时使用模板字面量类型
2. **类型转换**：确保类型正确转换
3. **工具类型**：使用内置工具类型
4. **类型安全**：利用模板字面量类型提高类型安全

## 练习

1. **基本用法**：练习模板字面量类型的基本用法。

2. **字符串拼接**：使用模板字面量类型拼接字符串。

3. **映射类型结合**：结合映射类型使用模板字面量类型。

4. **实际应用**：在实际场景中应用模板字面量类型。

完成以上练习后，映射类型章节学习完成。可以继续学习下一章：类型守卫。

## 总结

模板字面量类型允许使用模板字符串语法创建类型。可以与映射类型、条件类型结合使用。理解模板字面量类型的使用是学习 TypeScript 高级类型系统的关键。

## 相关资源

- [TypeScript 模板字面量类型文档](https://www.typescriptlang.org/docs/handbook/2/template-literal-types.html)
