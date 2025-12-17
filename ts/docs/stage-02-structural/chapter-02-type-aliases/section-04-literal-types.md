# 2.2.4 字面量类型

## 概述

字面量类型是 TypeScript 中的特殊类型，表示特定的值。本节介绍字面量类型的定义、使用和与联合类型的结合。

## 什么是字面量类型

### 定义

字面量类型是表示特定值的类型，而不是值的类型。

### 基本概念

```ts
// 字面量类型
let x: "hello" = "hello";
// x = "world"; // 错误：只能赋值 "hello"

// 普通类型
let y: string = "hello";
y = "world"; // 正确
```

## 字符串字面量类型

### 定义

字符串字面量类型表示特定的字符串值。

### 示例

```ts
// 单个字面量
type Direction = "up";
let dir: Direction = "up";
// dir = "down"; // 错误

// 联合字面量类型
type Direction = "up" | "down" | "left" | "right";
let dir: Direction = "up";
dir = "down"; // 正确
// dir = "north"; // 错误
```

### 使用场景

```ts
// 状态类型
type Status = "pending" | "approved" | "rejected";

// 主题类型
type Theme = "light" | "dark";

// HTTP 方法
type HttpMethod = "GET" | "POST" | "PUT" | "DELETE";
```

## 数字字面量类型

### 定义

数字字面量类型表示特定的数字值。

### 示例

```ts
// 单个字面量
type One = 1;
let value: One = 1;
// value = 2; // 错误

// 联合字面量类型
type StatusCode = 200 | 404 | 500;
let status: StatusCode = 200;
status = 404; // 正确
// status = 403; // 错误
```

### 使用场景

```ts
// HTTP 状态码
type HttpStatus = 200 | 404 | 500;

// 权限级别
type PermissionLevel = 0 | 1 | 2 | 3;
```

## 布尔字面量类型

### 定义

布尔字面量类型表示特定的布尔值。

### 示例

```ts
// 单个字面量
type True = true;
let value: True = true;
// value = false; // 错误

// 联合字面量类型（实际上就是 boolean）
type Bool = true | false; // 等价于 boolean
```

## 字面量类型推断

### const 断言

使用 `as const` 可以将值推断为字面量类型：

```ts
// 普通推断
let direction = "up"; // 类型是 string

// const 断言
let direction = "up" as const; // 类型是 "up"

// 对象 const 断言
const config = {
    theme: "dark",
    lang: "zh"
} as const;
// config.theme 的类型是 "dark"
```

## 字面量类型与联合类型

### 结合使用

字面量类型常与联合类型结合使用：

```ts
// 字符串字面量联合
type Status = "pending" | "approved" | "rejected";

// 数字字面量联合
type StatusCode = 200 | 404 | 500;

// 混合字面量联合
type Result = "success" | "error" | 0 | 1;
```

## 使用场景

### 1. 配置选项

```ts
type Theme = "light" | "dark";
type Language = "zh" | "en";

interface Config {
    theme: Theme;
    language: Language;
}
```

### 2. API 响应

```ts
type ApiStatus = "success" | "error";

interface ApiResponse {
    status: ApiStatus;
    data: any;
}
```

### 3. 状态管理

```ts
type LoadingState = "idle" | "loading" | "success" | "error";
```

## 常见错误

### 错误 1：字面量类型赋值错误

```ts
type Direction = "up" | "down";

let dir: Direction = "up";
// dir = "left"; // 错误：不在联合类型中
```

### 错误 2：类型推断问题

```ts
// 推断为 string，不是字面量类型
let theme = "dark";

// 需要使用 const 断言
let theme = "dark" as const;
```

## 注意事项

1. **字面量类型是具体值**：字面量类型表示特定的值
2. **const 断言**：使用 `as const` 可以推断为字面量类型
3. **联合字面量**：字面量类型常与联合类型结合使用
4. **类型收窄**：字面量类型可以用于类型收窄

## 最佳实践

1. **使用字面量类型表示固定值**：对于固定的值使用字面量类型
2. **结合联合类型**：字面量类型常与联合类型结合使用
3. **使用 const 断言**：需要字面量类型时使用 const 断言
4. **明确意图**：使用字面量类型明确表达意图

## 练习

1. **字面量类型**：定义各种字面量类型，理解其用法。

2. **联合字面量**：定义联合字面量类型，练习使用。

3. **const 断言**：使用 const 断言创建字面量类型。

4. **类型收窄**：使用字面量类型进行类型收窄。

5. **实际应用**：在实际场景中应用字面量类型。

完成以上练习后，继续学习下一节，了解 Interface vs Type。

## 总结

字面量类型是 TypeScript 中表示特定值的类型。字面量类型包括字符串字面量、数字字面量和布尔字面量。字面量类型常与联合类型结合使用，可以用于类型收窄和明确表达意图。

## 相关资源

- [TypeScript 字面量类型文档](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#literal-types)
