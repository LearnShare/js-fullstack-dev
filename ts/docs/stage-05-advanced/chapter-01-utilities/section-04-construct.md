# 5.1.4 构造工具类型（Record、Exclude、Extract）

## 概述

构造工具类型用于构造新类型或操作联合类型。本节介绍 Record、Exclude、Extract 的使用。

## Record

### 定义

`Record<K, V>` 构造一个对象类型，键为 `K`，值为 `V`。

### 语法

```ts
type Record<K extends keyof any, T> = {
    [P in K]: T;
};
```

### 示例

```ts
type StringRecord = Record<string, string>;
// { [key: string]: string; }

let record: StringRecord = {
    name: "John",
    email: "john@example.com"
};

type NumberRecord = Record<"id" | "count", number>;
// { id: number; count: number; }
```

### 使用场景

```ts
// 配置对象
type Config = Record<string, string | number>;

// 状态映射
type StatusMap = Record<"pending" | "success" | "error", string>;
```

## Exclude

### 定义

`Exclude<T, U>` 从类型 `T` 中排除可以赋值给 `U` 的类型。

### 语法

```ts
type Exclude<T, U> = T extends U ? never : T;
```

### 示例

```ts
type T0 = Exclude<"a" | "b" | "c", "a">;
// "b" | "c"

type T1 = Exclude<string | number | boolean, number>;
// string | boolean

type T2 = Exclude<"a" | "b" | "c", "a" | "b">;
// "c"
```

### 使用场景

```ts
// 排除特定类型
type NonNullable<T> = Exclude<T, null | undefined>;

// 排除特定值
type Status = "pending" | "success" | "error";
type NonErrorStatus = Exclude<Status, "error">;
// "pending" | "success"
```

## Extract

### 定义

`Extract<T, U>` 从类型 `T` 中提取可以赋值给 `U` 的类型。

### 语法

```ts
type Extract<T, U> = T extends U ? T : never;
```

### 示例

```ts
type T0 = Extract<"a" | "b" | "c", "a" | "f">;
// "a"

type T1 = Extract<string | number | boolean, number>;
// number

type T2 = Extract<"a" | "b" | "c", "a" | "b">;
// "a" | "b"
```

### 使用场景

```ts
// 提取特定类型
type StringOrNumber = Extract<string | number | boolean, string | number>;
// string | number

// 提取函数类型
type FunctionPropertyNames<T> = {
    [K in keyof T]: T[K] extends Function ? K : never;
}[keyof T];
```

## Exclude vs Extract

### 对比

| 特性       | Exclude<T, U>           | Extract<T, U>           |
|:-----------|:------------------------|:------------------------|
| 作用       | 排除类型                | 提取类型                |
| 结果       | T 中不在 U 中的类型     | T 中在 U 中的类型       |
| 使用场景   | 排除特定类型            | 提取特定类型            |

### 示例对比

```ts
type Status = "pending" | "success" | "error";

// Exclude：排除 "error"
type NonError = Exclude<Status, "error">;
// "pending" | "success"

// Extract：提取 "success" 和 "error"
type Result = Extract<Status, "success" | "error">;
// "success" | "error"
```

## 组合使用

### 与其他工具类型组合

```ts
interface User {
    name: string;
    age: number;
    email: string;
}

// 排除某些键并构造新类型
type UserKeys = keyof User;
type PublicKeys = Exclude<UserKeys, "email">;
type PublicUser = Pick<User, PublicKeys>;
```

## 常见错误

### 错误 1：类型不匹配

```ts
// 错误：Record 的键必须是 string | number | symbol
type Invalid = Record<boolean, string>;
```

### 错误 2：Exclude/Extract 使用错误

```ts
// 错误：Exclude 和 Extract 用于联合类型
type Invalid = Exclude<string, number>;
// string 不能赋值给 number，结果是 string
```

## 注意事项

1. **Record 键类型**：K 必须是 string | number | symbol
2. **Exclude/Extract**：用于联合类型
3. **类型安全**：提供类型安全
4. **组合使用**：可以与其他工具类型组合使用

## 最佳实践

1. **使用 Record**：在需要构造对象类型时使用 Record
2. **使用 Exclude**：在需要排除类型时使用 Exclude
3. **使用 Extract**：在需要提取类型时使用 Extract
4. **组合使用**：合理组合使用多个工具类型

## 练习

1. **Record**：使用 Record 构造对象类型。

2. **Exclude**：使用 Exclude 排除类型。

3. **Extract**：使用 Extract 提取类型。

4. **组合使用**：组合使用构造工具类型。

5. **实际应用**：在实际场景中应用构造工具类型。

完成以上练习后，继续学习下一节，了解函数工具类型。

## 总结

Record、Exclude、Extract 是构造工具类型。Record 用于构造对象类型，Exclude 用于排除类型，Extract 用于提取类型。理解这些工具类型的使用是学习 TypeScript 工具类型的关键。

## 相关资源

- [TypeScript Record 文档](https://www.typescriptlang.org/docs/handbook/utility-types.html#recordkeys-type)
- [TypeScript Exclude 文档](https://www.typescriptlang.org/docs/handbook/utility-types.html#excludetype-excludedunion)
- [TypeScript Extract 文档](https://www.typescriptlang.org/docs/handbook/utility-types.html#extracttype-union)
