# 5.4.3 用户自定义类型守卫

## 概述

用户自定义类型守卫允许创建自己的类型检查函数。本节介绍如何创建和使用自定义类型守卫。

## 自定义类型守卫

### 定义

自定义类型守卫是返回类型谓词的函数。

### 语法

```ts
function isType(value: unknown): value is Type {
    // 返回 boolean
}
```

### 示例

```ts
function isString(value: unknown): value is string {
    return typeof value === "string";
}

function process(value: unknown) {
    if (isString(value)) {
        // value 的类型是 string
        console.log(value.toUpperCase());
    }
}
```

## 对象类型守卫

### 检查对象结构

```ts
interface User {
    name: string;
    age: number;
}

function isUser(value: unknown): value is User {
    return (
        typeof value === "object" &&
        value !== null &&
        "name" in value &&
        "age" in value &&
        typeof (value as any).name === "string" &&
        typeof (value as any).age === "number"
    );
}
```

### 使用

```ts
function process(value: unknown) {
    if (isUser(value)) {
        // value 的类型是 User
        console.log(value.name, value.age);
    }
}
```

## 数组类型守卫

### 检查数组

```ts
function isStringArray(value: unknown): value is string[] {
    return Array.isArray(value) && value.every(item => typeof item === "string");
}

function process(value: unknown) {
    if (isStringArray(value)) {
        // value 的类型是 string[]
        value.forEach(str => console.log(str.toUpperCase()));
    }
}
```

## 联合类型守卫

### 检查联合类型

```ts
type StringOrNumber = string | number;

function isStringOrNumber(value: unknown): value is StringOrNumber {
    return typeof value === "string" || typeof value === "number";
}

function process(value: unknown) {
    if (isStringOrNumber(value)) {
        // value 的类型是 string | number
        if (typeof value === "string") {
            console.log(value.toUpperCase());
        } else {
            console.log(value * 2);
        }
    }
}
```

## 泛型类型守卫

### 泛型类型守卫

```ts
function isArrayOf<T>(
    value: unknown,
    check: (item: unknown) => item is T
): value is T[] {
    return Array.isArray(value) && value.every(check);
}

function isString(value: unknown): value is string {
    return typeof value === "string";
}

function process(value: unknown) {
    if (isArrayOf(value, isString)) {
        // value 的类型是 string[]
    }
}
```

## 使用场景

### 1. API 响应验证

```ts
interface ApiResponse<T> {
    data: T;
    status: number;
}

function isApiResponse<T>(
    value: unknown,
    checkData: (data: unknown) => data is T
): value is ApiResponse<T> {
    return (
        typeof value === "object" &&
        value !== null &&
        "data" in value &&
        "status" in value &&
        typeof (value as any).status === "number" &&
        checkData((value as any).data)
    );
}
```

### 2. 表单验证

```ts
interface FormData {
    name: string;
    email: string;
}

function isValidFormData(value: unknown): value is FormData {
    return (
        typeof value === "object" &&
        value !== null &&
        "name" in value &&
        "email" in value &&
        typeof (value as any).name === "string" &&
        typeof (value as any).email === "string"
    );
}
```

## 常见错误

### 错误 1：类型谓词错误

```ts
// 错误：类型谓词语法不正确
function isString(value: unknown): boolean {
    return typeof value === "string";
}

// 正确
function isString(value: unknown): value is string {
    return typeof value === "string";
}
```

### 错误 2：检查不充分

```ts
// 错误：检查不充分
function isUser(value: unknown): value is User {
    return typeof value === "object";
    // 没有检查 null 和属性
}

// 正确
function isUser(value: unknown): value is User {
    return (
        typeof value === "object" &&
        value !== null &&
        "name" in value &&
        "age" in value
    );
}
```

## 注意事项

1. **类型谓词**：使用 `value is Type` 语法
2. **返回 boolean**：类型守卫必须返回 boolean
3. **充分检查**：确保检查充分
4. **类型安全**：利用类型守卫提高类型安全

## 最佳实践

1. **创建类型守卫**：在需要类型收窄时创建类型守卫
2. **充分检查**：确保类型检查充分
3. **类型安全**：利用类型守卫提高类型安全
4. **代码复用**：创建可复用的类型守卫

## 练习

1. **自定义类型守卫**：创建不同类型的自定义类型守卫。

2. **对象检查**：创建检查对象结构的类型守卫。

3. **数组检查**：创建检查数组的类型守卫。

4. **实际应用**：在实际场景中应用自定义类型守卫。

完成以上练习后，继续学习下一节，了解可辨识联合。

## 总结

用户自定义类型守卫允许创建自己的类型检查函数。使用类型谓词语法 `value is Type`，必须返回 boolean。理解自定义类型守卫的使用是学习类型守卫的关键。

## 相关资源

- [TypeScript 类型守卫文档](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#using-type-predicates)
