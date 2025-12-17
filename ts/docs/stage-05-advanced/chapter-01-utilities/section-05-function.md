# 5.1.5 函数工具类型（Parameters、ReturnType）

## 概述

函数工具类型用于从函数类型中提取信息。本节介绍 Parameters 和 ReturnType 的使用。

## Parameters

### 定义

`Parameters<T>` 获取函数类型 `T` 的参数类型元组。

### 语法

```ts
type Parameters<T extends (...args: any) => any> = T extends (...args: infer P) => any ? P : never;
```

### 示例

```ts
function add(a: number, b: number): number {
    return a + b;
}

type AddParams = Parameters<typeof add>;
// [number, number]

let params: AddParams = [1, 2];
```

### 使用场景

```ts
// 提取函数参数类型
function process(name: string, age: number, email: string): void {
    // ...
}

type ProcessParams = Parameters<typeof process>;
// [string, number, string]

// 创建包装函数
function wrapper(...args: Parameters<typeof process>): void {
    console.log("Before process");
    process(...args);
    console.log("After process");
}
```

## ReturnType

### 定义

`ReturnType<T>` 获取函数类型 `T` 的返回类型。

### 语法

```ts
type ReturnType<T extends (...args: any) => any> = T extends (...args: any) => infer R ? R : any;
```

### 示例

```ts
function getUser(id: number): { name: string; age: number } {
    return { name: "John", age: 30 };
}

type User = ReturnType<typeof getUser>;
// { name: string; age: number }

let user: User = { name: "Jane", age: 25 };
```

### 使用场景

```ts
// 提取函数返回类型
async function fetchUser(id: number): Promise<{ id: number; name: string }> {
    // ...
}

type User = ReturnType<typeof fetchUser>;
// Promise<{ id: number; name: string }>

// 提取 Promise 的泛型参数
type UserData = Awaited<ReturnType<typeof fetchUser>>;
// { id: number; name: string }
```

## 组合使用

### 提取参数和返回类型

```ts
function process(name: string, age: number): { result: string } {
    return { result: `${name} is ${age}` };
}

type ProcessParams = Parameters<typeof process>;
type ProcessReturn = ReturnType<typeof process>;

// 创建类型安全的包装函数
function wrapper(...args: ProcessParams): ProcessReturn {
    console.log("Processing...");
    return process(...args);
}
```

## 实际应用

### 1. API 函数类型提取

```ts
async function fetchUser(id: number): Promise<User> {
    // ...
}

type FetchUserParams = Parameters<typeof fetchUser>;
type FetchUserReturn = ReturnType<typeof fetchUser>;

// 创建类型安全的 API 客户端
class ApiClient {
    async fetchUser(...args: FetchUserParams): Promise<FetchUserReturn> {
        return fetchUser(...args);
    }
}
```

### 2. 函数装饰器

```ts
function logged<T extends (...args: any[]) => any>(
    fn: T
): (...args: Parameters<T>) => ReturnType<T> {
    return function(...args: Parameters<T>): ReturnType<T> {
        console.log("Calling function");
        return fn(...args);
    };
}
```

### 3. 函数组合

```ts
function compose<A, B, C>(
    f: (b: B) => C,
    g: (a: A) => B
): (a: A) => C {
    return (a: A) => f(g(a));
}

type F = (x: number) => string;
type G = (x: string) => boolean;
type Composed = ReturnType<typeof compose<Parameters<G>[0], ReturnType<G>, ReturnType<F>>>;
```

## 常见错误

### 错误 1：非函数类型

```ts
// 错误：Parameters 只能用于函数类型
type Invalid = Parameters<string>;
```

### 错误 2：类型推断失败

```ts
// 错误：无法推断返回类型
function process(value: any): any {
    return value;
}

type Return = ReturnType<typeof process>;
// any
```

## 注意事项

1. **函数类型**：Parameters 和 ReturnType 只能用于函数类型
2. **类型推断**：需要函数有明确的类型签名
3. **异步函数**：ReturnType 返回 Promise 类型
4. **类型安全**：提供类型安全

## 最佳实践

1. **使用 Parameters**：在需要提取函数参数类型时使用
2. **使用 ReturnType**：在需要提取函数返回类型时使用
3. **组合使用**：合理组合使用函数工具类型
4. **类型安全**：利用工具类型提高类型安全

## 练习

1. **Parameters**：使用 Parameters 提取函数参数类型。

2. **ReturnType**：使用 ReturnType 提取函数返回类型。

3. **组合使用**：组合使用函数工具类型。

4. **实际应用**：在实际场景中应用函数工具类型。

完成以上练习后，工具类型章节学习完成。可以继续学习下一章：条件类型。

## 总结

Parameters 和 ReturnType 是函数工具类型，用于从函数类型中提取信息。Parameters 提取参数类型，ReturnType 提取返回类型。理解这些工具类型的使用是学习 TypeScript 工具类型的关键。

## 相关资源

- [TypeScript Parameters 文档](https://www.typescriptlang.org/docs/handbook/utility-types.html#parameterstype)
- [TypeScript ReturnType 文档](https://www.typescriptlang.org/docs/handbook/utility-types.html#returntypetype)
