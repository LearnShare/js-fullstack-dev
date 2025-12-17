# 4.2.3 keyof 操作符

## 概述

`keyof` 操作符用于获取对象类型的所有键的联合类型。本节介绍 `keyof` 操作符的使用。

## keyof 操作符

### 基本语法

```ts
type Keys = keyof Type;
```

### 示例

```ts
interface User {
    name: string;
    age: number;
    email: string;
}

type UserKeys = keyof User;
// UserKeys 是 "name" | "age" | "email"
```

## keyof 与泛型

### 基本使用

```ts
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key];
}

let user = { name: "John", age: 30 };
let name = getProperty(user, "name"); // 类型为 string
let age = getProperty(user, "age");   // 类型为 number
```

### 类型安全

```ts
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key];
}

let user = { name: "John", age: 30 };
// getProperty(user, "invalid"); // 错误：key 必须是 user 的键
```

## keyof 与索引访问

### 索引访问类型

```ts
interface User {
    name: string;
    age: number;
}

type NameType = User["name"]; // string
type AgeType = User["age"];   // number
```

### 结合 keyof

```ts
interface User {
    name: string;
    age: number;
}

type UserPropertyTypes = User[keyof User]; // string | number
```

## keyof 与映射类型

### 创建映射类型

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

## 使用场景

### 1. 获取对象属性

```ts
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key];
}
```

### 2. 设置对象属性

```ts
function setProperty<T, K extends keyof T>(
    obj: T,
    key: K,
    value: T[K]
): void {
    obj[key] = value;
}
```

### 3. 创建只读类型

```ts
type Readonly<T> = {
    readonly [P in keyof T]: T[P];
};
```

### 4. 创建可选类型

```ts
type Partial<T> = {
    [P in keyof T]?: T[P];
};
```

## 常见错误

### 错误 1：keyof 使用错误

```ts
// 错误：keyof 不能用于值
function getKeys(value: any): keyof value {
    return Object.keys(value);
}

// 正确：keyof 用于类型
type Keys = keyof User;
```

### 错误 2：类型不匹配

```ts
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key];
}

let user = { name: "John", age: 30 };
// getProperty(user, "name", "invalid"); // 错误：参数过多
```

## 注意事项

1. **类型操作符**：`keyof` 是类型操作符，不是值操作符
2. **联合类型**：`keyof` 返回联合类型
3. **类型安全**：`keyof` 提供类型安全
4. **索引访问**：可以结合索引访问类型使用

## 最佳实践

1. **使用 keyof**：在需要访问对象属性时使用 `keyof`
2. **类型安全**：利用 `keyof` 提高类型安全
3. **结合泛型**：结合泛型使用 `keyof`
4. **索引访问**：结合索引访问类型使用

## 练习

1. **keyof 操作符**：使用 keyof 获取对象类型的键。

2. **泛型结合**：结合泛型和 keyof 定义类型安全的函数。

3. **索引访问**：使用 keyof 和索引访问类型。

4. **实际应用**：在实际场景中应用 keyof 操作符。

完成以上练习后，继续学习下一节，了解条件类型约束。

## 总结

`keyof` 操作符用于获取对象类型的所有键的联合类型。结合泛型使用可以提供类型安全的属性访问。理解 `keyof` 操作符的使用是学习 TypeScript 泛型的关键。

## 相关资源

- [TypeScript keyof 操作符文档](https://www.typescriptlang.org/docs/handbook/2/keyof-types.html)
