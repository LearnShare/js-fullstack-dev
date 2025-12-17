# 8.2.2 使用 unknown 代替 any

## 概述

`unknown` 是 `any` 的类型安全替代。本节介绍如何使用 unknown 代替 any。

## unknown vs any

### 对比

| 特性       | any              | unknown          |
|:-----------|:-----------------|:-----------------|
| 类型安全   | 无               | 有               |
| 直接使用   | 可以             | 需要类型检查     |
| 推荐使用   | 不推荐           | 推荐             |
| 使用场景   | 迁移代码、第三方库 | 动态数据、API 响应 |

### 示例对比

```ts
// 使用 any（不推荐）
function process(data: any) {
    return data.value; // 可能出错
}

// 使用 unknown（推荐）
function process(data: unknown) {
    if (typeof data === "object" && data !== null && "value" in data) {
        return (data as { value: any }).value;
    }
    throw new Error("Invalid data");
}
```

## 使用 unknown

### 1. 类型检查

使用 unknown 时必须进行类型检查：

```ts
function process(data: unknown) {
    if (typeof data === "string") {
        return data.toUpperCase();
    }
    if (typeof data === "number") {
        return data * 2;
    }
    throw new Error("Unsupported type");
}
```

### 2. 类型守卫

使用类型守卫处理 unknown：

```ts
function isUser(data: unknown): data is { name: string; age: number } {
    return (
        typeof data === "object" &&
        data !== null &&
        "name" in data &&
        "age" in data &&
        typeof (data as any).name === "string" &&
        typeof (data as any).age === "number"
    );
}

function process(data: unknown) {
    if (isUser(data)) {
        return data.name; // 类型安全
    }
    throw new Error("Invalid user data");
}
```

### 3. 类型断言

在确认类型后使用类型断言：

```ts
function process(data: unknown) {
    if (typeof data === "object" && data !== null) {
        const obj = data as { value: string };
        return obj.value.toUpperCase();
    }
    throw new Error("Invalid data");
}
```

## 使用场景

### 1. API 响应

```ts
async function fetchData(): Promise<unknown> {
    const response = await fetch("/api/data");
    return response.json();
}

async function useData() {
    const data = await fetchData();
    
    if (typeof data === "object" && data !== null && "users" in data) {
        const users = (data as { users: User[] }).users;
        // 使用 users
    }
}
```

### 2. 动态数据

```ts
function processDynamicData(data: unknown) {
    if (typeof data === "string") {
        return data.toUpperCase();
    }
    if (typeof data === "number") {
        return data * 2;
    }
    if (Array.isArray(data)) {
        return data.length;
    }
    throw new Error("Unsupported data type");
}
```

### 3. 配置对象

```ts
function loadConfig(config: unknown): Config {
    if (
        typeof config === "object" &&
        config !== null &&
        "apiUrl" in config &&
        typeof (config as any).apiUrl === "string"
    ) {
        return config as Config;
    }
    throw new Error("Invalid config");
}
```

## 常见错误

### 错误 1：直接使用 unknown

```ts
// 错误：不能直接使用 unknown
function process(data: unknown) {
    return data.value; // 错误
}
```

### 错误 2：类型检查不完整

```ts
// 错误：类型检查不完整
function process(data: unknown) {
    if (typeof data === "object") {
        return data.value; // 错误：data 可能是 null
    }
}
```

## 注意事项

1. **类型检查**：使用 unknown 时必须进行类型检查
2. **类型守卫**：使用类型守卫提高类型安全
3. **类型断言**：在确认类型后使用类型断言
4. **错误处理**：处理类型不匹配的情况

## 最佳实践

1. **使用 unknown**：使用 unknown 代替 any
2. **类型检查**：进行充分的类型检查
3. **类型守卫**：使用类型守卫提高类型安全
4. **错误处理**：处理类型不匹配的情况

## 练习

1. **使用 unknown**：练习使用 unknown 代替 any。

2. **类型检查**：进行充分的类型检查。

3. **实际应用**：在实际项目中使用 unknown。

完成以上练习后，继续学习下一节，了解严格模式配置。

## 总结

使用 unknown 代替 any 可以提高类型安全。使用 unknown 时必须进行类型检查，可以使用类型守卫和类型断言。理解如何使用 unknown 是学习类型安全最佳实践的关键。

## 相关资源

- [TypeScript unknown 类型文档](https://www.typescriptlang.org/docs/handbook/2/functions.html#unknown)
