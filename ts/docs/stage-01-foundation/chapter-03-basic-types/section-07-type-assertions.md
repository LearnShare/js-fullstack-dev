# 1.2.7 类型断言

## 概述

类型断言（Type Assertion）是告诉 TypeScript 编译器某个值的类型的方式。类型断言不会改变运行时的值，只影响编译时的类型检查。本节介绍类型断言的语法、使用场景和注意事项。

## 类型断言语法

### 方式一：as 语法（推荐）

```ts
let value: unknown = "hello";
let str: string = value as string;
```

### 方式二：尖括号语法

```ts
let value: unknown = "hello";
let str: string = <string>value;
```

**注意**：在 JSX 中，尖括号语法可能与 JSX 语法冲突，因此推荐使用 `as` 语法。

## 基本用法

### 断言为具体类型

```ts
let value: unknown = "hello";

// 断言为 string
let str: string = value as string;
console.log(str.toUpperCase()); // "HELLO"
```

### 断言为 any

```ts
let value: unknown = "hello";

// 断言为 any（不推荐）
let anyValue: any = value as any;
```

### 断言为联合类型

```ts
let value: string | number = "hello";

// 断言为 string
let str: string = value as string;

// 断言为 number（可能不安全）
let num: number = value as number;
```

## 使用场景

### 1. DOM 操作

```ts
// 获取 DOM 元素
let element = document.getElementById("myButton") as HTMLButtonElement;

// 使用元素
element.addEventListener("click", () => {
    console.log("Button clicked");
});
```

### 2. 类型收窄

```ts
function processValue(value: string | number) {
    if (typeof value === "string") {
        // 类型收窄后，value 是 string
        console.log(value.toUpperCase());
    } else {
        // 类型收窄后，value 是 number
        console.log(value.toFixed(2));
    }
}
```

### 3. 第三方库类型

```ts
// 第三方库返回 any
let data: any = externalLibrary.getData();

// 断言为具体类型
let userData = data as { name: string; age: number };
console.log(userData.name);
```

### 4. 类型转换

```ts
// 数字转字符串
let num: number = 123;
let str: string = num.toString();

// 字符串转数字（需要验证）
let strNum: string = "123";
let numValue: number = parseInt(strNum, 10);
```

## 双重断言

### 定义

双重断言先断言为 `any` 或 `unknown`，再断言为目标类型。

### 语法

```ts
let value: string = "hello";

// 双重断言：string -> any -> number
let num: number = value as any as number;
```

### 使用场景

双重断言通常用于类型系统无法直接转换的情况，但应该谨慎使用：

```ts
// 不推荐：双重断言可能不安全
let value: string = "hello";
let num: number = value as any as number; // 运行时可能出错
```

## 类型断言 vs 类型转换

### 区别

| 特性       | 类型断言           | 类型转换           |
|:-----------|:-------------------|:-------------------|
| 运行时     | 不改变值           | 可能改变值         |
| 编译时     | 影响类型检查       | 不涉及类型系统     |
| 安全性     | 需要开发者保证     | 运行时可能失败     |
| 使用场景   | 类型系统           | 运行时转换         |

### 示例

```ts
// 类型断言：告诉 TypeScript 类型，不改变运行时值
let value: unknown = "123";
let str: string = value as string; // 运行时仍然是 "123"

// 类型转换：运行时转换值
let num: number = Number(value); // 运行时转换为 123
```

## 类型断言 vs 类型守卫

### 类型守卫（推荐）

类型守卫是运行时检查，更安全：

```ts
function isString(value: unknown): value is string {
    return typeof value === "string";
}

let value: unknown = "hello";

if (isString(value)) {
    // 类型收窄为 string
    console.log(value.toUpperCase()); // 安全
}
```

### 类型断言

类型断言是编译时断言，不进行运行时检查：

```ts
let value: unknown = "hello";

// 类型断言：不进行运行时检查
let str: string = value as string;
console.log(str.toUpperCase()); // 可能不安全
```

### 推荐做法

**优先使用类型守卫**，类型断言作为备选：

```ts
// ✅ 推荐：使用类型守卫
function processValue(value: unknown) {
    if (typeof value === "string") {
        console.log(value.toUpperCase());
    }
}

// ⚠️ 谨慎使用：类型断言
function processValue(value: unknown) {
    let str = value as string; // 需要确保 value 确实是 string
    console.log(str.toUpperCase());
}
```

## 常见错误

### 错误 1：不安全的断言

```ts
let value: string = "hello";

// 不安全的断言：value 不是 number
let num: number = value as number; // 编译通过，但运行时可能出错
```

### 错误 2：过度使用断言

```ts
// 不推荐：过度使用断言
let value: string = "hello";
let str: string = value as string; // 不必要的断言

// 推荐：直接使用
let value: string = "hello";
let str: string = value;
```

### 错误 3：忽略类型检查

```ts
// 不推荐：使用 any 跳过类型检查
let value: any = getData();
let str: string = value as string;

// 推荐：使用 unknown 和类型守卫
let value: unknown = getData();
if (typeof value === "string") {
    let str: string = value;
}
```

## 注意事项

1. **类型断言不改变运行时值**：类型断言只影响编译时类型检查
2. **需要开发者保证正确性**：类型断言需要开发者确保类型正确
3. **优先使用类型守卫**：类型守卫更安全，优先使用
4. **避免过度使用**：不要过度使用类型断言，应该修复类型问题

## 最佳实践

1. **优先使用类型守卫**：使用类型守卫进行运行时检查
2. **谨慎使用断言**：只在确定类型正确时使用断言
3. **避免双重断言**：尽量避免使用双重断言
4. **修复类型问题**：应该修复类型问题，而不是使用断言绕过

## 练习

1. **基本断言**：练习使用 `as` 语法进行类型断言。

2. **DOM 操作**：使用类型断言处理 DOM 元素。

3. **类型守卫 vs 断言**：对比类型守卫和类型断言，理解它们的区别。

4. **不安全断言**：体验不安全的类型断言可能导致的问题。

5. **最佳实践**：按照最佳实践使用类型断言，优先使用类型守卫。

完成以上练习后，基础类型系统章节学习完成。可以继续学习阶段二：结构化类型系统。

## 总结

类型断言是告诉 TypeScript 编译器某个值的类型的方式。类型断言不会改变运行时的值，只影响编译时的类型检查。应该谨慎使用类型断言，优先使用类型守卫进行运行时检查。理解类型断言的使用场景和注意事项，可以帮助我们更好地使用 TypeScript 的类型系统。

## 相关资源

- [TypeScript 类型断言文档](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions)
