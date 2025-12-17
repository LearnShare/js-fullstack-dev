# 5.4.1 类型守卫概述

## 概述

类型守卫用于在运行时检查类型，并在类型检查器中收窄类型。本节介绍类型守卫的概念、作用和分类。

## 什么是类型守卫

### 定义

类型守卫是一种表达式，用于在运行时检查类型，并在类型检查器中收窄类型范围。

### 基本概念

```ts
function isString(value: unknown): value is string {
    return typeof value === "string";
}

function process(value: unknown) {
    if (isString(value)) {
        // value 的类型被收窄为 string
        console.log(value.toUpperCase());
    }
}
```

## 类型守卫的作用

### 1. 类型收窄

类型守卫可以收窄类型范围：

```ts
function isNumber(value: unknown): value is number {
    return typeof value === "number";
}

function process(value: unknown) {
    if (isNumber(value)) {
        // value 的类型是 number
        return value * 2;
    }
}
```

### 2. 类型安全

类型守卫提供类型安全：

```ts
function isUser(value: unknown): value is User {
    return typeof value === "object" && value !== null && "name" in value;
}

function process(value: unknown) {
    if (isUser(value)) {
        // value 的类型是 User，可以安全访问属性
        console.log(value.name);
    }
}
```

### 3. 运行时检查

类型守卫在运行时检查类型：

```ts
function isArray(value: unknown): value is any[] {
    return Array.isArray(value);
}
```

## 类型守卫分类

### 1. 内置类型守卫

- `typeof`：检查基本类型
- `instanceof`：检查实例类型
- `in`：检查属性存在

### 2. 用户自定义类型守卫

```ts
function isString(value: unknown): value is string {
    return typeof value === "string";
}
```

### 3. 可辨识联合

```ts
type Result<T> = 
    | { success: true; data: T }
    | { success: false; error: string };
```

## 类型守卫的语法

### 类型谓词

```ts
function isType(value: unknown): value is Type {
    // 返回 boolean
}
```

### 使用

```ts
if (isType(value)) {
    // value 的类型是 Type
}
```

## 使用场景

### 1. 参数验证

```ts
function process(value: unknown) {
    if (isString(value)) {
        // 处理字符串
    } else if (isNumber(value)) {
        // 处理数字
    }
}
```

### 2. API 响应

```ts
function isApiResponse(value: unknown): value is ApiResponse {
    return typeof value === "object" && value !== null && "data" in value;
}
```

### 3. 错误处理

```ts
function isError(value: unknown): value is Error {
    return value instanceof Error;
}
```

## 注意事项

1. **类型谓词**：使用 `value is Type` 语法
2. **返回 boolean**：类型守卫必须返回 boolean
3. **类型收窄**：类型守卫会收窄类型范围
4. **运行时检查**：类型守卫在运行时检查

## 最佳实践

1. **使用类型守卫**：在需要类型收窄时使用类型守卫
2. **明确类型**：为类型守卫提供明确的类型
3. **类型安全**：利用类型守卫提高类型安全
4. **代码复用**：创建可复用的类型守卫

## 练习

1. **类型守卫概念**：理解类型守卫的概念和作用。

2. **类型收窄**：使用类型守卫收窄类型。

3. **类型安全**：利用类型守卫提高类型安全。

4. **实际应用**：在实际场景中应用类型守卫。

完成以上练习后，继续学习下一节，了解 typeof 与 instanceof。

## 总结

类型守卫用于在运行时检查类型，并在类型检查器中收窄类型。类型守卫提供类型安全、类型收窄和运行时检查。理解类型守卫的概念和作用是学习 TypeScript 高级类型系统的关键。

## 相关资源

- [TypeScript 类型守卫文档](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#using-type-predicates)
