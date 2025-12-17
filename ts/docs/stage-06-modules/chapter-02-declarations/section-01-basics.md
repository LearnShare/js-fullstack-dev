# 6.2.1 声明文件基础

## 概述

声明文件用于为 JavaScript 代码提供类型定义。本节介绍声明文件的概念、作用和语法。

## 什么是声明文件

### 定义

声明文件是 `.d.ts` 文件，包含类型声明，不包含实现代码。

### 基本概念

```ts
// math.d.ts
export function add(a: number, b: number): number;
export function subtract(a: number, b: number): number;
```

### 作用

声明文件为 JavaScript 代码提供类型信息：

```ts
// math.js
export function add(a, b) {
    return a + b;
}

// math.d.ts
export function add(a: number, b: number): number;
```

## 声明文件语法

### declare 关键字

使用 `declare` 关键字声明：

```ts
declare function add(a: number, b: number): number;
declare const PI: number;
declare class Calculator {
    add(a: number, b: number): number;
}
```

### 导出声明

```ts
// 命名导出
export function add(a: number, b: number): number;

// 默认导出
export default class Calculator {
    add(a: number, b: number): number;
}
```

## 声明文件类型

### 1. 全局声明文件

```ts
// global.d.ts
declare global {
    interface Window {
        myProperty: string;
    }
}
```

### 2. 模块声明文件

```ts
// module.d.ts
declare module "my-module" {
    export function process(): void;
}
```

### 3. 类型声明文件

```ts
// types.d.ts
export interface User {
    name: string;
    age: number;
}
```

## 使用场景

### 1. 为 JavaScript 库提供类型

```ts
// jquery.d.ts
declare namespace jQuery {
    function ajax(settings: any): void;
}
```

### 2. 扩展全局类型

```ts
// global.d.ts
declare global {
    interface Window {
        myAPI: {
            call(): void;
        };
    }
}
```

### 3. 模块类型定义

```ts
// my-module.d.ts
declare module "my-module" {
    export function process(): void;
}
```

## 常见错误

### 错误 1：包含实现代码

```ts
// 错误：声明文件不能包含实现
export function add(a: number, b: number): number {
    return a + b; // 错误
}

// 正确：只包含类型声明
export function add(a: number, b: number): number;
```

### 错误 2：缺少 declare

```ts
// 错误：全局声明需要 declare
function globalFunction(): void;

// 正确
declare function globalFunction(): void;
```

## 注意事项

1. **只包含类型**：声明文件只包含类型声明
2. **declare 关键字**：全局声明需要使用 declare
3. **文件扩展名**：使用 `.d.ts` 扩展名
4. **类型安全**：声明文件提供类型安全

## 最佳实践

1. **使用声明文件**：为 JavaScript 代码提供类型定义
2. **明确类型**：为声明提供明确的类型
3. **文件组织**：合理组织声明文件
4. **类型安全**：利用声明文件提高类型安全

## 练习

1. **声明文件概念**：理解声明文件的概念和作用。

2. **基本语法**：练习声明文件的基本语法。

3. **类型声明**：编写不同类型的声明。

4. **实际应用**：在实际场景中应用声明文件。

完成以上练习后，继续学习下一节，了解声明文件类型。

## 总结

声明文件用于为 JavaScript 代码提供类型定义。使用 `.d.ts` 扩展名，只包含类型声明。理解声明文件的基础是学习 TypeScript 工程化的关键。

## 相关资源

- [TypeScript 声明文件文档](https://www.typescriptlang.org/docs/handbook/declaration-files/introduction.html)
