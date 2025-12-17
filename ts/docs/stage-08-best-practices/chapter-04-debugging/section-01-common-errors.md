# 8.4.1 常见类型错误

## 概述

识别常见类型错误有助于快速解决问题。本节介绍常见类型错误。

## 常见错误类型

### 1. 类型不匹配

```ts
// 错误：类型不匹配
let value: string = 123; // 错误：Type 'number' is not assignable to type 'string'
```

### 2. 未定义属性

```ts
// 错误：未定义属性
interface User {
    name: string;
}

const user: User = {
    name: "John",
    age: 30 // 错误：Property 'age' does not exist on type 'User'
};
```

### 3. null/undefined 错误

```ts
// 错误：可能为 null
function process(value: string | null) {
    return value.toUpperCase(); // 错误：Object is possibly 'null'
}
```

### 4. any 类型错误

```ts
// 错误：隐式 any
function process(param) { // 错误：Parameter 'param' implicitly has an 'any' type
    return param;
}
```

## 使用场景

### 1. 开发阶段

在开发阶段识别和修复类型错误：

```ts
// 修复类型错误
function process(value: string | null) {
    if (value === null) {
        throw new Error("Value cannot be null");
    }
    return value.toUpperCase();
}
```

### 2. 代码审查

在代码审查中检查类型错误：

```ts
// 检查类型定义
interface User {
    name: string;
    age: number;
}
```

## 注意事项

1. **错误信息**：仔细阅读错误信息
2. **类型定义**：检查类型定义是否正确
3. **null 检查**：处理 null/undefined 情况
4. **避免 any**：避免使用 any

## 最佳实践

1. **识别错误**：快速识别常见类型错误
2. **修复错误**：及时修复类型错误
3. **类型定义**：确保类型定义正确
4. **错误处理**：处理 null/undefined 情况

## 练习

1. **识别错误**：识别常见类型错误。

2. **修复错误**：修复类型错误。

3. **实际应用**：在实际项目中识别和修复类型错误。

完成以上练习后，继续学习下一节，了解类型错误调试技巧。

## 总结

识别常见类型错误有助于快速解决问题。类型不匹配、未定义属性、null/undefined 错误、any 类型错误是常见的类型错误。理解常见类型错误是学习调试的关键。

## 相关资源

- [TypeScript 错误信息](https://www.typescriptlang.org/docs/handbook/error-messages.html)
