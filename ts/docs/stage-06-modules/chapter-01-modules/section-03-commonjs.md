# 6.1.3 CommonJS 与 TypeScript

## 概述

CommonJS 是 Node.js 的模块系统。本节介绍 CommonJS 在 TypeScript 中的使用。

## CommonJS 语法

### 导出

#### module.exports

```ts
// math.ts
function add(a: number, b: number): number {
    return a + b;
}

module.exports = {
    add
};
```

#### exports

```ts
// utils.ts
exports.formatDate = (date: Date): string => {
    return date.toISOString();
};

exports.helper = (): void => {
    // ...
};
```

### 导入

#### require

```ts
const { add } = require("./math");
const math = require("./math");
```

## TypeScript 配置

### module 选项

在 `tsconfig.json` 中配置：

```json
{
  "compilerOptions": {
    "module": "CommonJS"
  }
}
```

### esModuleInterop

启用 ES Modules 和 CommonJS 互操作：

```json
{
  "compilerOptions": {
    "module": "CommonJS",
    "esModuleInterop": true
  }
}
```

## ES Modules 与 CommonJS 互操作

### 导入 CommonJS 模块

```ts
// 使用 esModuleInterop
import express from "express";
// 或
import * as express from "express";
```

### 导出为 CommonJS

```ts
// 使用 export = 语法
export = {
    add: (a: number, b: number) => a + b
};
```

## 使用场景

### 1. Node.js 项目

```ts
// 使用 CommonJS
const express = require("express");
const fs = require("fs");
```

### 2. 传统项目

```ts
// 使用 CommonJS 兼容传统项目
module.exports = {
    // ...
};
```

### 3. 库开发

```ts
// 导出为 CommonJS
module.exports = {
    libraryFunction: () => {
        // ...
    }
};
```

## 常见错误

### 错误 1：模块格式不匹配

```ts
// 错误：module 配置为 ES Modules，但使用了 CommonJS
module.exports = {};
```

### 错误 2：导入方式错误

```ts
// 错误：在 CommonJS 中使用 import
import { add } from "./math";

// 正确：使用 require
const { add } = require("./math");
```

## 注意事项

1. **模块格式**：确保 module 配置正确
2. **esModuleInterop**：启用互操作支持
3. **导入方式**：根据模块格式选择导入方式
4. **类型定义**：为 CommonJS 模块提供类型定义

## 最佳实践

1. **使用 ES Modules**：优先使用 ES Modules
2. **互操作**：启用 esModuleInterop 支持互操作
3. **类型定义**：为 CommonJS 模块提供类型定义
4. **迁移**：逐步迁移到 ES Modules

## 练习

1. **CommonJS**：使用 CommonJS 导出和导入。

2. **互操作**：练习 ES Modules 和 CommonJS 互操作。

3. **类型定义**：为 CommonJS 模块编写类型定义。

4. **实际应用**：在实际场景中应用 CommonJS。

完成以上练习后，继续学习下一节，了解模块解析策略。

## 总结

CommonJS 是 Node.js 的模块系统。TypeScript 支持 CommonJS，可以配置互操作。理解 CommonJS 的使用是学习 TypeScript 模块系统的关键。

## 相关资源

- [TypeScript CommonJS 文档](https://www.typescriptlang.org/docs/handbook/modules.html#commonjs)
