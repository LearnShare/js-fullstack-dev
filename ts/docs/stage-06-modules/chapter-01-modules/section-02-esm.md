# 6.1.2 ES Modules 与 TypeScript

## 概述

ES Modules 是 JavaScript 的标准模块系统。本节介绍 ES Modules 在 TypeScript 中的使用。

## ES Modules 语法

### 导出

#### 命名导出

```ts
// math.ts
export function add(a: number, b: number): number {
    return a + b;
}

export function subtract(a: number, b: number): number {
    return a - b;
}

export const PI = 3.14159;
```

#### 默认导出

```ts
// calculator.ts
export default class Calculator {
    add(a: number, b: number): number {
        return a + b;
    }
}
```

#### 混合导出

```ts
// utils.ts
export function formatDate(date: Date): string {
    return date.toISOString();
}

export default function helper(): void {
    // ...
}
```

### 导入

#### 命名导入

```ts
import { add, subtract, PI } from "./math";
```

#### 默认导入

```ts
import Calculator from "./calculator";
```

#### 混合导入

```ts
import Calculator, { formatDate } from "./utils";
```

#### 命名空间导入

```ts
import * as Math from "./math";
Math.add(1, 2);
```

#### 重命名导入

```ts
import { add as addNumbers } from "./math";
```

## TypeScript 配置

### module 选项

在 `tsconfig.json` 中配置：

```json
{
  "compilerOptions": {
    "module": "ES2020"
  }
}
```

### 支持的模块格式

- `ES2020`：ES2020 模块
- `ESNext`：最新的 ES 模块
- `ES2015`：ES2015 模块
- `ES6`：ES6 模块（同 ES2015）

## 使用场景

### 1. 前端项目

```ts
// 使用 ES Modules
import { useState, useEffect } from "react";
import { Component } from "react";
```

### 2. 现代 Node.js

```ts
// package.json
{
  "type": "module"
}

// 使用 ES Modules
import express from "express";
```

### 3. 库开发

```ts
// 导出库功能
export function libraryFunction(): void {
    // ...
}

export default class Library {
    // ...
}
```

## 常见错误

### 错误 1：模块格式不匹配

```ts
// 错误：module 配置不正确
// tsconfig.json: "module": "CommonJS"
// 但使用了 ES Modules 语法
export function add() {}
```

### 错误 2：导入路径错误

```ts
// 错误：导入路径不正确
import { add } from "math"; // 缺少 ./ 或 /

// 正确
import { add } from "./math";
```

## 注意事项

1. **模块格式**：确保 module 配置正确
2. **导入路径**：使用正确的导入路径
3. **文件扩展名**：根据配置决定是否包含扩展名
4. **类型导入**：使用类型导入导入类型

## 最佳实践

1. **使用 ES Modules**：优先使用 ES Modules
2. **明确导出**：使用明确的导出方式
3. **类型导入**：使用类型导入导入类型
4. **路径配置**：配置正确的路径解析

## 练习

1. **ES Modules**：使用 ES Modules 导出和导入。

2. **命名导出**：练习命名导出和导入。

3. **默认导出**：练习默认导出和导入。

4. **实际应用**：在实际场景中应用 ES Modules。

完成以上练习后，继续学习下一节，了解 CommonJS 与 TypeScript。

## 总结

ES Modules 是 JavaScript 的标准模块系统。TypeScript 支持 ES Modules，可以配置不同的模块格式。理解 ES Modules 的使用是学习 TypeScript 模块系统的关键。

## 相关资源

- [TypeScript ES Modules 文档](https://www.typescriptlang.org/docs/handbook/modules.html)
