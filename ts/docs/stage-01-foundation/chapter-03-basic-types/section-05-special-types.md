# 1.2.5 特殊类型（any、unknown、void、never）

## 概述

TypeScript 提供了几个特殊类型：`any`、`unknown`、`void`、`never`。这些类型在特定场景下非常有用。本节介绍这些特殊类型的定义、使用和注意事项。

## any 类型

### 定义

`any` 类型表示任意类型，可以赋值给任何类型，也可以接收任何类型的值。

### 基本用法

```ts
let value: any = 42;
value = "hello";
value = true;
value = {};
value = [];
```

### 使用场景

#### 1. 迁移 JavaScript 代码

在将 JavaScript 代码迁移到 TypeScript 时，可以使用 `any` 作为过渡：

```ts
function legacyFunction(data: any) {
    // 处理任意类型的数据
    return data;
}
```

#### 2. 第三方库类型缺失

当第三方库没有类型定义时，可以使用 `any`：

```ts
declare const externalLib: any;
externalLib.doSomething();
```

### 注意事项

**⚠️ 不推荐使用 `any`**

使用 `any` 会失去 TypeScript 的类型安全优势：

```ts
let value: any = "hello";
let length: number = value.length; // 运行时可能出错
value.foo.bar; // 编译时不会报错，但运行时可能出错
```

### 最佳实践

1. **避免使用 `any`**：尽量使用明确的类型
2. **使用 `unknown` 替代**：当类型不确定时，使用 `unknown` 更安全
3. **逐步迁移**：迁移代码时，逐步替换 `any` 为具体类型

## unknown 类型

### 定义

`unknown` 类型表示未知类型，是 `any` 的类型安全替代。

### 基本用法

```ts
let value: unknown = 42;
value = "hello";
value = true;
```

### 类型安全

`unknown` 类型不能直接使用，必须先进行类型检查：

```ts
let value: unknown = "hello";

// 错误：不能直接使用
// let length: number = value.length;

// 正确：先进行类型检查
if (typeof value === "string") {
    let length: number = value.length; // 正确
}
```

### 使用场景

#### 1. 处理动态数据

```ts
function processData(data: unknown) {
    if (typeof data === "string") {
        return data.toUpperCase();
    } else if (typeof data === "number") {
        return data * 2;
    } else {
        throw new Error("Unsupported data type");
    }
}
```

#### 2. API 响应

```ts
async function fetchData(): Promise<unknown> {
    const response = await fetch("/api/data");
    return response.json();
}

async function useData() {
    const data = await fetchData();
    
    // 需要类型检查
    if (typeof data === "object" && data !== null && "name" in data) {
        console.log(data.name);
    }
}
```

### unknown vs any

| 特性       | any              | unknown          |
|:-----------|:-----------------|:-----------------|
| 类型安全   | 无               | 有               |
| 直接使用   | 可以             | 需要类型检查     |
| 推荐使用   | 不推荐           | 推荐             |
| 使用场景   | 迁移代码、第三方库 | 动态数据、API 响应 |

## void 类型

### 定义

`void` 类型表示没有返回值，通常用于函数返回值。

### 基本用法

```ts
function logMessage(message: string): void {
    console.log(message);
    // 没有 return 语句，或 return; 或 return undefined;
}
```

### 函数返回值

```ts
// 显式声明 void
function doSomething(): void {
    console.log("Doing something");
}

// 不返回值（隐式 void）
function doSomethingElse() {
    console.log("Doing something else");
}
```

### 变量类型

`void` 也可以作为变量类型，但只能赋值为 `undefined`：

```ts
let result: void = undefined;
// let result: void = null; // 错误（strictNullChecks 下）
```

### 使用场景

#### 1. 事件处理函数

```ts
function handleClick(): void {
    console.log("Button clicked");
}

button.addEventListener("click", handleClick);
```

#### 2. 回调函数

```ts
function forEach<T>(arr: T[], callback: (item: T) => void): void {
    for (const item of arr) {
        callback(item);
    }
}
```

## never 类型

### 定义

`never` 类型表示永远不会存在的值，是其他所有类型的子类型。

### 基本用法

```ts
// 抛出异常的函数
function throwError(message: string): never {
    throw new Error(message);
}

// 无限循环
function infiniteLoop(): never {
    while (true) {
        // 永远不会返回
    }
}
```

### 使用场景

#### 1. 抛出异常

```ts
function fail(message: string): never {
    throw new Error(message);
}

function process(value: string | number) {
    if (typeof value === "string") {
        return value.toUpperCase();
    } else if (typeof value === "number") {
        return value * 2;
    } else {
        // 这里 value 的类型是 never
        return fail("Unexpected value");
    }
}
```

#### 2. 类型收窄

```ts
function assertNever(value: never): never {
    throw new Error(`Unexpected value: ${value}`);
}

type Status = "pending" | "approved" | "rejected";

function processStatus(status: Status) {
    switch (status) {
        case "pending":
            return "处理中";
        case "approved":
            return "已批准";
        case "rejected":
            return "已拒绝";
        default:
            // 如果所有 case 都处理了，这里 value 的类型是 never
            return assertNever(status);
    }
}
```

#### 3. 数组类型收窄

```ts
function getFirst<T>(arr: T[]): T | never {
    if (arr.length === 0) {
        throw new Error("Array is empty");
    }
    return arr[0];
}
```

### never 的特性

1. **是所有类型的子类型**：`never` 可以赋值给任何类型
2. **没有类型是 never 的子类型**：除了 `never` 本身
3. **不能有值**：`never` 类型不能有任何值

## 类型对比

| 类型     | 含义           | 使用场景                 | 类型安全 |
|:---------|:---------------|:-------------------------|:---------|
| `any`    | 任意类型       | 迁移代码、第三方库       | 无       |
| `unknown`| 未知类型       | 动态数据、API 响应       | 有       |
| `void`   | 无返回值       | 函数返回值               | 有       |
| `never`  | 永不存在的值   | 异常、无限循环、类型收窄 | 有       |

## 常见错误

### 错误 1：滥用 any

```ts
// 不推荐
function process(data: any) {
    return data.value; // 可能出错
}

// 推荐
function process(data: unknown) {
    if (typeof data === "object" && data !== null && "value" in data) {
        return (data as { value: any }).value;
    }
    throw new Error("Invalid data");
}
```

### 错误 2：void 返回值使用

```ts
function logMessage(): void {
    console.log("Message");
}

let result: void = logMessage(); // 错误：void 不能作为值类型
```

## 注意事项

1. **避免 any**：尽量避免使用 `any`，使用 `unknown` 替代
2. **void 用于函数**：`void` 主要用于函数返回值
3. **never 用于收窄**：`never` 用于类型收窄和异常处理
4. **类型安全**：优先使用类型安全的类型（`unknown`、`void`、`never`）

## 最佳实践

1. **使用 unknown 替代 any**：当类型不确定时，使用 `unknown` 更安全
2. **明确 void 返回值**：函数不返回值时，明确声明 `void`
3. **利用 never 收窄**：使用 `never` 进行类型收窄，确保所有情况都被处理
4. **逐步减少 any**：迁移代码时，逐步将 `any` 替换为具体类型

## 练习

1. **any 使用**：理解 `any` 的使用场景和问题。

2. **unknown 实践**：使用 `unknown` 处理动态数据，进行类型检查。

3. **void 函数**：创建返回 `void` 的函数，理解其用途。

4. **never 类型**：使用 `never` 进行类型收窄，确保所有情况都被处理。

5. **类型对比**：对比 `any`、`unknown`、`void`、`never` 的区别和使用场景。

完成以上练习后，继续学习下一节，了解类型推断与类型注解。

## 总结

特殊类型（`any`、`unknown`、`void`、`never`）在特定场景下非常有用。`any` 应该避免使用，`unknown` 是更安全的替代。`void` 用于函数返回值，`never` 用于类型收窄和异常处理。理解这些特殊类型的特性和使用场景，可以帮助我们更好地使用 TypeScript 的类型系统。

## 相关资源

- [TypeScript any 类型文档](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#any)
- [TypeScript unknown 类型文档](https://www.typescriptlang.org/docs/handbook/2/functions.html#unknown)
- [TypeScript void 类型文档](https://www.typescriptlang.org/docs/handbook/2/functions.html#void)
- [TypeScript never 类型文档](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#the-never-type)
