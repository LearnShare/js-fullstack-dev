# 6.1.1 模块系统概述

## 概述

模块系统允许将代码组织成独立的模块，便于管理和复用。本节介绍模块系统的概念、作用和分类。

## 什么是模块系统

### 定义

模块系统是一种代码组织方式，允许将代码分割成独立的模块，每个模块可以导入和导出功能。

### 基本概念

```ts
// 导出
export function add(a: number, b: number): number {
    return a + b;
}

// 导入
import { add } from "./math";
```

## 模块系统的作用

### 1. 代码组织

模块系统帮助组织代码：

```ts
// math.ts
export function add(a: number, b: number): number {
    return a + b;
}

export function subtract(a: number, b: number): number {
    return a - b;
}
```

### 2. 代码复用

模块系统支持代码复用：

```ts
// utils.ts
export function formatDate(date: Date): string {
    return date.toISOString();
}

// 在其他文件中复用
import { formatDate } from "./utils";
```

### 3. 依赖管理

模块系统管理依赖：

```ts
// 导入外部依赖
import { useState } from "react";
import { Router } from "express";
```

## 模块系统分类

### 1. ES Modules (ESM)

ES Modules 是 JavaScript 的标准模块系统：

```ts
// 导出
export function add(a: number, b: number): number {
    return a + b;
}

// 导入
import { add } from "./math";
```

### 2. CommonJS (CJS)

CommonJS 是 Node.js 的模块系统：

```ts
// 导出
module.exports = {
    add: (a: number, b: number) => a + b
};

// 导入
const { add } = require("./math");
```

### 3. AMD

AMD (Asynchronous Module Definition) 是异步模块定义：

```ts
define(["dependency"], function(dependency) {
    return {
        // 模块代码
    };
});
```

## TypeScript 模块系统

### 支持多种模块系统

TypeScript 支持多种模块系统：

```ts
// ES Modules
export function add(a: number, b: number): number {
    return a + b;
}

// CommonJS
module.exports = {
    add: (a: number, b: number) => a + b
};
```

### 模块编译选项

在 `tsconfig.json` 中配置：

```json
{
  "compilerOptions": {
    "module": "ES2020",
    "moduleResolution": "node"
  }
}
```

## 使用场景

### 1. 前端项目

```ts
// 使用 ES Modules
import { Component } from "react";
import { useState } from "react";
```

### 2. Node.js 项目

```ts
// 使用 CommonJS 或 ES Modules
const express = require("express");
// 或
import express from "express";
```

### 3. 库开发

```ts
// 导出库功能
export function libraryFunction(): void {
    // ...
}
```

## 注意事项

1. **模块格式**：根据项目需求选择模块格式
2. **编译选项**：配置正确的模块编译选项
3. **类型导入**：使用类型导入避免运行时导入
4. **模块解析**：配置正确的模块解析策略

## 最佳实践

1. **使用 ES Modules**：优先使用 ES Modules
2. **类型导入**：使用类型导入导入类型
3. **模块解析**：配置正确的模块解析策略
4. **代码组织**：合理组织模块结构

## 练习

1. **模块系统概念**：理解模块系统的概念和作用。

2. **模块导出**：练习模块的导出。

3. **模块导入**：练习模块的导入。

4. **实际应用**：在实际场景中应用模块系统。

完成以上练习后，继续学习下一节，了解 ES Modules 与 TypeScript。

## 总结

模块系统允许将代码组织成独立的模块，便于管理和复用。TypeScript 支持多种模块系统，包括 ES Modules 和 CommonJS。理解模块系统的概念和作用是学习 TypeScript 工程化的关键。

## 相关资源

- [TypeScript 模块系统文档](https://www.typescriptlang.org/docs/handbook/modules.html)
