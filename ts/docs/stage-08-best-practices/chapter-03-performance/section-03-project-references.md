# 8.3.3 项目引用（Project References）

## 概述

项目引用允许将 TypeScript 项目组织成更小的部分，提高编译性能。本节介绍项目引用的使用。

## 什么是项目引用

### 定义

项目引用允许一个 TypeScript 项目依赖于另一个 TypeScript 项目。

### 基本概念

```json
{
  "references": [
    { "path": "./packages/core" },
    { "path": "./packages/utils" }
  ]
}
```

## 配置项目引用

### 1. 被引用项目

配置被引用项目：

```json
// packages/core/tsconfig.json
{
  "compilerOptions": {
    "composite": true,
    "declaration": true
  }
}
```

### 2. 引用项目

配置引用项目：

```json
// tsconfig.json
{
  "references": [
    { "path": "./packages/core" },
    { "path": "./packages/utils" }
  ]
}
```

## 使用场景

### 1. 多包项目

多包项目使用项目引用：

```
project/
├── packages/
│   ├── core/
│   │   └── tsconfig.json
│   ├── utils/
│   │   └── tsconfig.json
│   └── ui/
│       └── tsconfig.json
└── tsconfig.json
```

### 2. 大型项目

大型项目使用项目引用拆分：

```
project/
├── src/
│   ├── core/
│   ├── features/
│   └── shared/
└── tsconfig.json
```

## 常见错误

### 错误 1：未启用 composite

```json
// 错误：被引用项目未启用 composite
{
  "compilerOptions": {
    "declaration": true
  }
}
```

### 错误 2：路径错误

```json
// 错误：引用路径不正确
{
  "references": [
    { "path": "./wrong-path" }
  ]
}
```

## 注意事项

1. **composite**：被引用项目需要启用 composite
2. **declaration**：被引用项目需要启用 declaration
3. **路径正确**：确保引用路径正确
4. **构建顺序**：注意项目构建顺序

## 最佳实践

1. **使用项目引用**：多包项目使用项目引用
2. **启用 composite**：被引用项目启用 composite
3. **路径正确**：确保引用路径正确
4. **构建顺序**：注意项目构建顺序

## 练习

1. **项目引用**：配置和使用项目引用。

2. **多包项目**：在多包项目中使用项目引用。

3. **实际应用**：在实际项目中应用项目引用。

完成以上练习后，性能优化章节学习完成。可以继续学习下一章：常见错误与调试。

## 总结

项目引用允许将 TypeScript 项目组织成更小的部分，提高编译性能。配置被引用项目和引用项目，使用 composite 和 declaration 选项。理解项目引用的使用是学习性能优化的关键。

## 相关资源

- [TypeScript 项目引用文档](https://www.typescriptlang.org/docs/handbook/project-references.html)
