# 6.2.8 DefinitelyTyped (@types/)

## 概述

DefinitelyTyped 是 TypeScript 类型定义的仓库，为 JavaScript 库提供类型定义。本节介绍 DefinitelyTyped 的使用。

## 什么是 DefinitelyTyped

### 定义

DefinitelyTyped 是一个 GitHub 仓库，包含大量 JavaScript 库的 TypeScript 类型定义。

### 作用

DefinitelyTyped 为没有内置类型定义的 JavaScript 库提供类型支持。

### 仓库地址

- GitHub: https://github.com/DefinitelyTyped/DefinitelyTyped
- npm: 通过 `@types/` 前缀发布

## 安装类型定义

### 使用 npm

```bash
npm install --save-dev @types/jquery
npm install --save-dev @types/node
npm install --save-dev @types/react
```

### 使用 yarn

```bash
yarn add -D @types/jquery
yarn add -D @types/node
yarn add -D @types/react
```

### 使用 pnpm

```bash
pnpm add -D @types/jquery
pnpm add -D @types/node
pnpm add -D @types/react
```

## 使用类型定义

### 自动识别

安装 `@types/` 包后，TypeScript 会自动识别类型定义：

```ts
// 安装 @types/jquery 后
import $ from "jquery";

$.ajax({
    url: "/api/data",
    method: "GET"
});
```

### 手动引用

某些情况下需要手动引用类型定义：

```ts
/// <reference types="node" />

import * as fs from "fs";
```

## 查找类型定义

### npm 搜索

在 npm 上搜索 `@types/` 包：

```bash
npm search @types/jquery
```

### TypeScript 官网

在 TypeScript 官网搜索类型定义：

- https://www.typescriptlang.org/dt/search

### GitHub 仓库

在 DefinitelyTyped 仓库中查找：

- https://github.com/DefinitelyTyped/DefinitelyTyped

## 类型定义版本

### 版本对应

`@types/` 包的版本通常对应库的版本：

```bash
# jQuery 3.x 的类型定义
npm install --save-dev @types/jquery@^3.0.0

# jQuery 2.x 的类型定义
npm install --save-dev @types/jquery@^2.0.0
```

### 版本管理

TypeScript 会自动选择兼容的类型定义版本。

## 常见库的类型定义

### 前端库

```bash
npm install --save-dev @types/react
npm install --save-dev @types/react-dom
npm install --save-dev @types/vue
npm install --save-dev @types/angular
```

### Node.js 库

```bash
npm install --save-dev @types/node
npm install --save-dev @types/express
npm install --save-dev @types/koa
```

### 工具库

```bash
npm install --save-dev @types/lodash
npm install --save-dev @types/underscore
npm install --save-dev @types/jquery
```

## 使用场景

### 1. 使用第三方库

```ts
// 安装 @types/express
import express from "express";
const app = express();
```

### 2. Node.js 开发

```ts
// 安装 @types/node
import * as fs from "fs";
import * as path from "path";
```

### 3. React 开发

```ts
// 安装 @types/react
import React from "react";
import { useState } from "react";
```

## 常见错误

### 错误 1：类型定义不存在

```ts
// 错误：某些库可能没有类型定义
import someLibrary from "some-library";
// 需要自己编写类型定义
```

### 错误 2：版本不匹配

```ts
// 错误：类型定义版本与库版本不匹配
// 可能导致类型错误
```

## 注意事项

1. **类型定义**：确保安装正确的类型定义版本
2. **自动识别**：TypeScript 会自动识别 @types/ 包
3. **版本对应**：类型定义版本应与库版本对应
4. **缺失类型**：某些库可能没有类型定义，需要自己编写

## 最佳实践

1. **使用 DefinitelyTyped**：优先使用 DefinitelyTyped 的类型定义
2. **版本对应**：确保类型定义版本与库版本对应
3. **自动安装**：使用工具自动安装类型定义
4. **贡献类型**：为缺失的类型定义贡献代码

## 练习

1. **安装类型定义**：为常用库安装类型定义。

2. **使用类型定义**：在实际项目中使用类型定义。

3. **查找类型定义**：练习查找和安装类型定义。

4. **实际应用**：在实际场景中应用 DefinitelyTyped。

完成以上练习后，继续学习下一节，了解编写自定义声明文件。

## 总结

DefinitelyTyped 是 TypeScript 类型定义的仓库，为 JavaScript 库提供类型定义。通过 `@types/` 前缀安装类型定义，TypeScript 会自动识别。理解 DefinitelyTyped 的使用是学习声明文件的关键。

## 相关资源

- [DefinitelyTyped GitHub](https://github.com/DefinitelyTyped/DefinitelyTyped)
- [TypeScript 类型定义搜索](https://www.typescriptlang.org/dt/search)
