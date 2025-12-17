# 5.1.3 选择工具类型（Pick、Omit）

## 概述

选择工具类型用于从类型中选择或排除部分属性。本节介绍 Pick 和 Omit 的使用。

## Pick

### 定义

`Pick<T, K>` 从类型 `T` 中选择属性 `K`。

### 语法

```ts
type Pick<T, K extends keyof T> = {
    [P in K]: T[P];
};
```

### 示例

```ts
interface User {
    name: string;
    age: number;
    email: string;
    password: string;
}

type UserPublic = Pick<User, "name" | "email">;
// { name: string; email: string; }

let publicUser: UserPublic = {
    name: "John",
    email: "john@example.com"
};
```

### 使用场景

```ts
// 选择公开字段
interface User {
    id: number;
    name: string;
    email: string;
    password: string;
}

type PublicUser = Pick<User, "id" | "name" | "email">;
// 排除敏感信息
```

## Omit

### 定义

`Omit<T, K>` 从类型 `T` 中排除属性 `K`。

### 语法

```ts
type Omit<T, K extends keyof T> = Pick<T, Exclude<keyof T, K>>;
```

### 示例

```ts
interface User {
    name: string;
    age: number;
    email: string;
    password: string;
}

type UserWithoutPassword = Omit<User, "password">;
// { name: string; age: number; email: string; }

let user: UserWithoutPassword = {
    name: "John",
    age: 30,
    email: "john@example.com"
};
```

### 使用场景

```ts
// 排除敏感字段
interface User {
    id: number;
    name: string;
    password: string;
    token: string;
}

type SafeUser = Omit<User, "password" | "token">;
// 排除敏感信息
```

## Pick vs Omit

### 对比

| 特性       | Pick<T, K>              | Omit<T, K>              |
|:-----------|:------------------------|:------------------------|
| 作用       | 选择属性                | 排除属性                |
| 参数       | 要选择的属性            | 要排除的属性            |
| 使用场景   | 选择部分属性            | 排除部分属性            |

### 示例对比

```ts
interface User {
    name: string;
    age: number;
    email: string;
}

// 使用 Pick：选择 name 和 email
type UserNameEmail = Pick<User, "name" | "email">;

// 使用 Omit：排除 age
type UserNameEmail2 = Omit<User, "age">;

// 结果相同
```

## 组合使用

### 与其他工具类型组合

```ts
interface User {
    name: string;
    age: number;
    email: string;
    password: string;
}

// 选择并设为可选
type PartialUserPublic = Partial<Pick<User, "name" | "email">>>;

// 排除并设为只读
type ReadonlyUserSafe = Readonly<Omit<User, "password">>>;
```

## 常见错误

### 错误 1：键不存在

```ts
interface User {
    name: string;
    age: number;
}

// 错误：invalidKey 不在 User 中
type Invalid = Pick<User, "invalidKey">;
```

### 错误 2：类型不匹配

```ts
interface User {
    name: string;
}

// 错误：不能选择不存在的属性
let user: Pick<User, "age"> = { age: 30 };
```

## 注意事项

1. **键约束**：K 必须是 T 的键
2. **类型安全**：Pick 和 Omit 提供类型安全
3. **组合使用**：可以与其他工具类型组合使用
4. **类型推导**：支持类型推导

## 最佳实践

1. **使用 Pick**：在需要选择部分属性时使用 Pick
2. **使用 Omit**：在需要排除部分属性时使用 Omit
3. **组合使用**：合理组合使用多个工具类型
4. **类型安全**：利用工具类型提高类型安全

## 练习

1. **Pick**：使用 Pick 选择类型属性。

2. **Omit**：使用 Omit 排除类型属性。

3. **组合使用**：组合使用 Pick、Omit 和其他工具类型。

4. **实际应用**：在实际场景中应用选择工具类型。

完成以上练习后，继续学习下一节，了解构造工具类型。

## 总结

Pick 和 Omit 是选择工具类型，用于从类型中选择或排除部分属性。Pick 选择属性，Omit 排除属性。理解这些工具类型的使用是学习 TypeScript 工具类型的关键。

## 相关资源

- [TypeScript Pick 文档](https://www.typescriptlang.org/docs/handbook/utility-types.html#picktype-keys)
- [TypeScript Omit 文档](https://www.typescriptlang.org/docs/handbook/utility-types.html#omittype-keys)
