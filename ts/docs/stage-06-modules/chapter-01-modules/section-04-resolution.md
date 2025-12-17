# 6.1.4 模块解析策略

## 概述

模块解析策略决定了 TypeScript 如何查找模块。本节介绍模块解析策略的配置和使用。

## 模块解析策略

### 1. node

Node.js 风格的模块解析：

```json
{
  "compilerOptions": {
    "moduleResolution": "node"
  }
}
```

### 2. bundler

打包器风格的模块解析：

```json
{
  "compilerOptions": {
    "moduleResolution": "bundler"
  }
}
```

### 3. classic

TypeScript 经典模块解析（已废弃）：

```json
{
  "compilerOptions": {
    "moduleResolution": "classic"
  }
}
```

## node 解析策略

### 解析顺序

1. 检查 `node_modules`
2. 检查 `package.json` 的 `main` 字段
3. 检查 `package.json` 的 `types` 字段
4. 检查文件扩展名

### 示例

```ts
// 解析 node_modules 中的模块
import express from "express";

// 解析相对路径
import { add } from "./math";

// 解析绝对路径（配置 baseUrl）
import { utils } from "src/utils";
```

## bundler 解析策略

### 特点

- 不检查文件扩展名
- 不检查 `package.json` 的 `main` 字段
- 依赖打包器解析

### 使用场景

```ts
// 用于现代打包器（Vite、Webpack 等）
import { Component } from "react";
import { utils } from "./utils";
```

## 路径映射

### baseUrl

设置基础路径：

```json
{
  "compilerOptions": {
    "baseUrl": "."
  }
}
```

### paths

配置路径映射：

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "utils/*": ["src/utils/*"]
    }
  }
}
```

### 使用

```ts
import { utils } from "@/utils";
import { helper } from "utils/helper";
```

## 使用场景

### 1. Node.js 项目

```json
{
  "compilerOptions": {
    "moduleResolution": "node"
  }
}
```

### 2. 前端项目（使用打包器）

```json
{
  "compilerOptions": {
    "moduleResolution": "bundler"
  }
}
```

### 3. 路径别名

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    }
  }
}
```

## 常见错误

### 错误 1：解析策略不匹配

```ts
// 错误：moduleResolution 配置不正确
// 导致模块无法解析
import { add } from "./math";
```

### 错误 2：路径映射错误

```ts
// 错误：paths 配置不正确
import { utils } from "@/utils";
```

## 注意事项

1. **解析策略**：根据项目选择正确的解析策略
2. **路径映射**：配置正确的路径映射
3. **baseUrl**：设置正确的基础路径
4. **文件扩展名**：根据配置决定是否包含扩展名

## 最佳实践

1. **使用 node**：Node.js 项目使用 node 解析策略
2. **使用 bundler**：使用打包器的项目使用 bundler 解析策略
3. **路径别名**：使用路径别名简化导入路径
4. **配置正确**：确保解析策略配置正确

## 练习

1. **模块解析**：配置不同的模块解析策略。

2. **路径映射**：配置和使用路径映射。

3. **路径别名**：使用路径别名简化导入。

4. **实际应用**：在实际场景中应用模块解析策略。

完成以上练习后，继续学习下一节，了解类型导入。

## 总结

模块解析策略决定了 TypeScript 如何查找模块。可以选择 node、bundler 等解析策略，可以配置路径映射和路径别名。理解模块解析策略的配置是学习 TypeScript 模块系统的关键。

## 相关资源

- [TypeScript 模块解析文档](https://www.typescriptlang.org/docs/handbook/module-resolution.html)
