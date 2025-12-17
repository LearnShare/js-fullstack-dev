# 5.4.2 typeof 与 instanceof

## 概述

`typeof` 和 `instanceof` 是内置的类型守卫。本节介绍它们的使用。

## typeof

### 定义

`typeof` 操作符用于检查基本类型。

### 支持的类型

```ts
typeof value === "string"
typeof value === "number"
typeof value === "boolean"
typeof value === "undefined"
typeof value === "object"
typeof value === "function"
typeof value === "symbol"
typeof value === "bigint"
```

### 示例

```ts
function process(value: unknown) {
    if (typeof value === "string") {
        // value 的类型是 string
        console.log(value.toUpperCase());
    } else if (typeof value === "number") {
        // value 的类型是 number
        console.log(value * 2);
    }
}
```

### 使用场景

```ts
function isString(value: unknown): value is string {
    return typeof value === "string";
}

function isNumber(value: unknown): value is number {
    return typeof value === "number";
}
```

## instanceof

### 定义

`instanceof` 操作符用于检查实例类型。

### 示例

```ts
class User {
    name: string;
}

function process(value: unknown) {
    if (value instanceof User) {
        // value 的类型是 User
        console.log(value.name);
    }
}
```

### 使用场景

```ts
function isError(value: unknown): value is Error {
    return value instanceof Error;
}

function isDate(value: unknown): value is Date {
    return value instanceof Date;
}
```

## typeof vs instanceof

### 区别

| 特性       | typeof                    | instanceof                |
|:-----------|:--------------------------|:--------------------------|
| 检查类型   | 基本类型                  | 实例类型                  |
| 使用场景   | 基本类型检查              | 类实例检查                |
| 返回值     | 字符串                    | boolean                   |

### 示例对比

```ts
// typeof：检查基本类型
if (typeof value === "string") {
    // value 是 string
}

// instanceof：检查实例类型
if (value instanceof User) {
    // value 是 User 的实例
}
```

## in 操作符

### 定义

`in` 操作符用于检查属性是否存在。

### 示例

```ts
interface User {
    name: string;
    age: number;
}

function process(value: unknown) {
    if ("name" in value && "age" in value) {
        // value 可能有 name 和 age 属性
        console.log((value as User).name);
    }
}
```

### 使用场景

```ts
function hasProperty<T, K extends string>(
    obj: T,
    key: K
): obj is T & Record<K, unknown> {
    return key in obj;
}
```

## 组合使用

### 多个检查

```ts
function process(value: unknown) {
    if (typeof value === "object" && value !== null) {
        if ("name" in value) {
            // value 是对象且有 name 属性
        }
    }
}
```

## 常见错误

### 错误 1：typeof 使用错误

```ts
// 错误：typeof 不能用于检查对象类型
if (typeof value === "User") {
    // 错误
}

// 正确：使用 instanceof
if (value instanceof User) {
    // 正确
}
```

### 错误 2：instanceof 使用错误

```ts
// 错误：instanceof 不能用于基本类型
if (value instanceof string) {
    // 错误
}

// 正确：使用 typeof
if (typeof value === "string") {
    // 正确
}
```

## 注意事项

1. **typeof 限制**：typeof 只能检查基本类型
2. **instanceof 限制**：instanceof 只能检查实例类型
3. **null 检查**：typeof null 返回 "object"
4. **类型收窄**：typeof 和 instanceof 会收窄类型

## 最佳实践

1. **使用 typeof**：在检查基本类型时使用 typeof
2. **使用 instanceof**：在检查实例类型时使用 instanceof
3. **null 检查**：检查对象时同时检查 null
4. **类型安全**：利用类型守卫提高类型安全

## 练习

1. **typeof**：使用 typeof 检查基本类型。

2. **instanceof**：使用 instanceof 检查实例类型。

3. **in 操作符**：使用 in 操作符检查属性。

4. **实际应用**：在实际场景中应用 typeof 和 instanceof。

完成以上练习后，继续学习下一节，了解用户自定义类型守卫。

## 总结

typeof 和 instanceof 是内置的类型守卫。typeof 用于检查基本类型，instanceof 用于检查实例类型。理解它们的使用是学习类型守卫的关键。

## 相关资源

- [TypeScript typeof 文档](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#typeof-type-guards)
- [TypeScript instanceof 文档](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#instanceof-narrowing)
