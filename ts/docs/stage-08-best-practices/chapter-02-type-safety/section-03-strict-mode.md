# 8.2.3 严格模式配置

## 概述

严格模式提供更严格的类型检查。本节介绍如何配置 TypeScript 严格模式。

## 严格模式选项

### strict

启用所有严格类型检查选项：

```json
{
  "compilerOptions": {
    "strict": true
  }
}
```

启用 `strict` 会同时启用以下选项：
- `strictNullChecks`
- `strictFunctionTypes`
- `strictBindCallApply`
- `strictPropertyInitialization`
- `noImplicitThis`
- `alwaysStrict`

### strictNullChecks

启用严格的 null 检查：

```json
{
  "compilerOptions": {
    "strictNullChecks": true
  }
}
```

```ts
// strictNullChecks: false
let value: string = null; // 允许

// strictNullChecks: true
let value: string = null; // 错误
let value: string | null = null; // 正确
```

### noImplicitAny

不允许隐式 any 类型：

```json
{
  "compilerOptions": {
    "noImplicitAny": true
  }
}
```

```ts
// noImplicitAny: false
function fn(param) { // param 的类型是 any
    return param;
}

// noImplicitAny: true
function fn(param) { // 错误：参数有隐式 any 类型
    return param;
}
function fn(param: string) { // 正确
    return param;
}
```

### strictFunctionTypes

对函数类型进行更严格的检查：

```json
{
  "compilerOptions": {
    "strictFunctionTypes": true
  }
}
```

### strictPropertyInitialization

要求类属性必须在构造函数中初始化：

```json
{
  "compilerOptions": {
    "strictPropertyInitialization": true
  }
}
```

```ts
// strictPropertyInitialization: true
class User {
    name: string; // 错误：属性未初始化
}

class User {
    name: string;
    constructor(name: string) {
        this.name = name; // 正确
    }
}
```

## 配置示例

### 完整配置

```json
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true,
    "strictBindCallApply": true,
    "strictPropertyInitialization": true,
    "noImplicitThis": true,
    "alwaysStrict": true
  }
}
```

## 使用场景

### 1. 新项目

新项目应该启用严格模式：

```json
{
  "compilerOptions": {
    "strict": true
  }
}
```

### 2. 现有项目

现有项目可以逐步启用严格模式：

```json
{
  "compilerOptions": {
    "strictNullChecks": true,
    "noImplicitAny": true
  }
}
```

## 常见错误

### 错误 1：未启用严格模式

```json
// 错误：未启用严格模式
{
  "compilerOptions": {
    "strict": false
  }
}
```

### 错误 2：部分启用

```json
// 错误：部分启用，可能导致不一致
{
  "compilerOptions": {
    "strictNullChecks": true,
    "noImplicitAny": false
  }
}
```

## 注意事项

1. **启用严格模式**：新项目应该启用严格模式
2. **逐步迁移**：现有项目可以逐步启用
3. **一致性**：保持配置一致性
4. **团队协作**：团队统一配置

## 最佳实践

1. **启用严格模式**：新项目启用严格模式
2. **逐步迁移**：现有项目逐步启用
3. **统一配置**：团队统一配置
4. **文档说明**：为配置添加文档说明

## 练习

1. **配置严格模式**：配置 TypeScript 严格模式。

2. **迁移项目**：将现有项目迁移到严格模式。

3. **实际应用**：在实际项目中应用严格模式。

完成以上练习后，类型安全最佳实践章节学习完成。可以继续学习下一章：性能优化。

## 总结

严格模式提供更严格的类型检查。启用 strict 会同时启用多个严格检查选项，新项目应该启用严格模式，现有项目可以逐步启用。理解严格模式配置是学习类型安全最佳实践的关键。

## 相关资源

- [TypeScript 严格模式文档](https://www.typescriptlang.org/docs/handbook/compiler-options.html#strict)
