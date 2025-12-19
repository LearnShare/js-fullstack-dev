# 4.4.2 泛型相关的工具类型

## 概述

本节介绍与泛型相关的内置工具类型，包括 `Record`、`Exclude`、`Extract` 等，这些工具类型专门用于泛型类型操作。

## Record<K, T>

### 定义

`Record<K, T>` 创建一个对象类型，其键的类型为 `K`，值的类型为 `T`。

### 语法

```ts
type Record<K extends keyof any, T> = {
    [P in K]: T;
};
```

### 基本用法

```ts
// 创建记录类型
type UserRecord = Record<string, number>;
// 等价于：{ [key: string]: number }

let userAges: UserRecord = {
    "alice": 25,
    "bob": 30,
    "charlie": 35
};

// 使用字面量类型作为键
type Status = "pending" | "approved" | "rejected";
type StatusConfig = Record<Status, string>;

let config: StatusConfig = {
    pending: "等待中",
    approved: "已批准",
    rejected: "已拒绝"
};
```

### 使用场景

#### 1. 创建映射类型

```ts
// 创建状态映射
type Status = "success" | "error" | "warning";
type StatusMessages = Record<Status, string>;

let messages: StatusMessages = {
    success: "操作成功",
    error: "操作失败",
    warning: "操作警告"
};
```

#### 2. 创建配置对象

```ts
// 创建 API 端点配置
type Endpoint = "users" | "posts" | "comments";
type EndpointConfig = Record<Endpoint, {
    url: string;
    method: "GET" | "POST" | "PUT" | "DELETE";
}>;

let apiConfig: EndpointConfig = {
    users: { url: "/api/users", method: "GET" },
    posts: { url: "/api/posts", method: "GET" },
    comments: { url: "/api/comments", method: "GET" }
};
```

## Exclude<T, U>

### 定义

`Exclude<T, U>` 从联合类型 `T` 中排除可以赋值给 `U` 的类型。

### 语法

```ts
type Exclude<T, U> = T extends U ? never : T;
```

### 基本用法

```ts
// 从联合类型中排除特定类型
type AllTypes = string | number | boolean | null | undefined;
type PrimitiveTypes = Exclude<AllTypes, null | undefined>;
// 等价于：string | number | boolean

let value: PrimitiveTypes = "hello";  // ✅
let value2: PrimitiveTypes = 42;  // ✅
// let value3: PrimitiveTypes = null;  // ❌ 不兼容
```

### 使用场景

#### 1. 过滤类型

```ts
// 从函数参数类型中排除 undefined
type FunctionParams = string | number | undefined;
type ValidParams = Exclude<FunctionParams, undefined>;
// 等价于：string | number

function process(param: ValidParams): void {
    console.log(param);
}

process("hello");  // ✅
process(42);  // ✅
// process(undefined);  // ❌ 不兼容
```

#### 2. 类型清理

```ts
// 从对象属性类型中排除 null
type UserStatus = "active" | "inactive" | null;
type ValidStatus = Exclude<UserStatus, null>;
// 等价于："active" | "inactive"

interface User {
    status: ValidStatus;
}
```

## Extract<T, U>

### 定义

`Extract<T, U>` 从联合类型 `T` 中提取可以赋值给 `U` 的类型。

### 语法

```ts
type Extract<T, U> = T extends U ? T : never;
```

### 基本用法

```ts
// 从联合类型中提取特定类型
type AllTypes = string | number | boolean | null;
type StringOrNumber = Extract<AllTypes, string | number>;
// 等价于：string | number

let value: StringOrNumber = "hello";  // ✅
let value2: StringOrNumber = 42;  // ✅
// let value3: StringOrNumber = true;  // ❌ 不兼容
```

### 使用场景

#### 1. 类型提取

```ts
// 从函数参数类型中提取特定类型
type FunctionParams = string | number | boolean;
type StringParams = Extract<FunctionParams, string>;
// 等价于：string

function processString(param: StringParams): void {
    console.log(param.toUpperCase());
}
```

#### 2. 类型过滤

```ts
// 从对象属性类型中提取特定类型
type Status = "pending" | "approved" | "rejected" | "cancelled";
type ActiveStatus = Extract<Status, "pending" | "approved">;
// 等价于："pending" | "approved"

interface Task {
    status: ActiveStatus;
}
```

## NonNullable<T>

### 定义

`NonNullable<T>` 从类型 `T` 中排除 `null` 和 `undefined`。

### 语法

```ts
type NonNullable<T> = T extends null | undefined ? never : T;
```

### 基本用法

```ts
// 排除 null 和 undefined
type MaybeString = string | null | undefined;
type String = NonNullable<MaybeString>;
// 等价于：string

let value: String = "hello";  // ✅
// let value2: String = null;  // ❌ 不兼容
// let value3: String = undefined;  // ❌ 不兼容
```

### 使用场景

#### 1. 类型清理

```ts
// 清理可能为 null 或 undefined 的类型
type UserName = string | null | undefined;
type ValidName = NonNullable<UserName>;
// 等价于：string

function greet(name: ValidName): void {
    console.log(`Hello, ${name}!`);
}
```

#### 2. 数组元素类型

```ts
// 从数组中排除 null 和 undefined
type MaybeNumbers = (number | null | undefined)[];
type Numbers = NonNullable<MaybeNumbers[number]>;
// 等价于：number

let numbers: Numbers[] = [1, 2, 3];  // ✅
// let numbers2: Numbers[] = [1, null, 3];  // ❌ 不兼容
```

## 工具类型组合

### 组合使用

可以组合多个工具类型实现复杂的类型操作：

```ts
interface User {
    id: number;
    name: string;
    email: string | null;
    age: number | undefined;
}

// 组合多个工具类型
type CleanUser = {
    [K in keyof User]: NonNullable<User[K]>;
};
// 等价于：
// type CleanUser = {
//     id: number;
//     name: string;
//     email: string;
//     age: number;
// }
```

### 实际应用

```ts
// API 响应处理
interface ApiResponse<T> {
    data: T | null;
    error: string | null;
    status: number;
}

// 提取非空数据
type SuccessResponse<T> = {
    data: NonNullable<ApiResponse<T>["data"]>;
    status: Extract<ApiResponse<T>["status"], 200 | 201>;
};

function handleSuccess<T>(response: SuccessResponse<T>): T {
    return response.data;
}
```

## 注意事项

1. **类型操作**：这些工具类型是类型操作，不影响运行时
2. **联合类型**：`Exclude` 和 `Extract` 主要用于联合类型
3. **类型推断**：工具类型可以保留类型推断信息
4. **性能考虑**：复杂的类型操作可能影响编译性能
5. **可读性**：过度使用可能降低代码可读性

## 最佳实践

1. **合理使用**：根据实际需求选择合适的工具类型
2. **类型别名**：为复杂的工具类型组合创建类型别名
3. **文档说明**：为复杂的类型操作添加注释
4. **性能优化**：避免过度嵌套的工具类型操作
5. **类型安全**：利用工具类型提高类型安全

## 练习任务

1. **Record 类型**：
   - 使用 `Record` 创建映射类型
   - 创建配置对象类型
   - 理解 `Record` 的使用场景

2. **Exclude 类型**：
   - 使用 `Exclude` 从联合类型中排除类型
   - 过滤函数参数类型
   - 理解 `Exclude` 的作用

3. **Extract 类型**：
   - 使用 `Extract` 从联合类型中提取类型
   - 提取特定类型
   - 理解 `Extract` 的作用

4. **NonNullable 类型**：
   - 使用 `NonNullable` 排除 null 和 undefined
   - 清理可能为空的类型
   - 理解 `NonNullable` 的作用

5. **工具类型组合**：
   - 组合多个工具类型
   - 创建复杂的类型操作
   - 理解工具类型组合的效果

完成以上练习后，继续学习下一节：泛型约束工具。

## 总结

泛型相关的工具类型提供了强大的类型操作能力：

- **Record**：创建记录类型，键值对映射
- **Exclude**：从联合类型中排除类型
- **Extract**：从联合类型中提取类型
- **NonNullable**：排除 null 和 undefined

掌握这些工具类型有助于编写更灵活、更安全的 TypeScript 代码。

---

**最后更新**：2025-01-XX
