# 6.2.9 编写自定义声明文件

## 概述

当库没有类型定义时，需要编写自定义声明文件。本节介绍如何编写自定义声明文件。

## 何时编写自定义声明文件

### 场景

1. **库没有类型定义**：库没有 @types/ 包
2. **类型定义不完整**：现有类型定义不完整
3. **自定义扩展**：需要扩展库的类型
4. **内部库**：为内部库编写类型定义

## 声明文件结构

### 基本结构

```ts
// my-library.d.ts
declare module "my-library" {
    export function process(): void;
    export interface Config {
        apiUrl: string;
    }
}
```

### 全局声明

```ts
// global.d.ts
declare function globalFunction(): void;
declare const globalConstant: string;
```

## 编写步骤

### 1. 分析库的 API

分析库的 API 结构：

```ts
// 分析库的使用方式
import myLibrary from "my-library";
myLibrary.process();
myLibrary.init({ apiUrl: "https://api.example.com" });
```

### 2. 定义类型

根据 API 定义类型：

```ts
// my-library.d.ts
declare module "my-library" {
    export interface Config {
        apiUrl: string;
        timeout?: number;
    }

    export function init(config: Config): void;
    export function process(): void;
}
```

### 3. 测试类型

测试类型定义是否正确：

```ts
import myLibrary from "my-library";

// 应该通过类型检查
myLibrary.init({ apiUrl: "https://api.example.com" });
myLibrary.process();
```

## 常见模式

### 1. 函数库

```ts
// utils.d.ts
declare module "utils" {
    export function formatDate(date: Date): string;
    export function parseDate(dateString: string): Date;
}
```

### 2. 类库

```ts
// calculator.d.ts
declare module "calculator" {
    export class Calculator {
        add(a: number, b: number): number;
        subtract(a: number, b: number): number;
    }
}
```

### 3. 对象库

```ts
// config.d.ts
declare module "config" {
    export interface Config {
        apiUrl: string;
        timeout: number;
    }

    export const config: Config;
}
```

### 4. 混合库

```ts
// library.d.ts
declare module "library" {
    export function init(): void;
    export class Library {
        method(): void;
    }
    export interface Options {
        option: string;
    }
}
```

## 高级技巧

### 1. 泛型支持

```ts
// api.d.ts
declare module "api" {
    export interface ApiResponse<T> {
        data: T;
        status: number;
    }

    export function fetch<T>(): Promise<ApiResponse<T>>;
}
```

### 2. 函数重载

```ts
// utils.d.ts
declare module "utils" {
    export function process(value: string): string;
    export function process(value: number): number;
    export function process(value: boolean): boolean;
}
```

### 3. 条件类型

```ts
// types.d.ts
declare module "types" {
    export type Result<T> = T extends string ? string : number;
}
```

## 使用场景

### 1. 无类型库

```ts
// 为没有类型定义的库编写声明文件
declare module "untyped-library" {
    export function process(): void;
}
```

### 2. 扩展类型

```ts
// 扩展现有类型定义
declare module "existing-library" {
    interface ExistingInterface {
        newProperty: string;
    }
}
```

### 3. 内部库

```ts
// 为内部库编写类型定义
declare module "@company/internal-library" {
    export function internalFunction(): void;
}
```

## 常见错误

### 错误 1：类型不准确

```ts
// 错误：类型定义不准确
declare module "library" {
    export function process(value: any): any;
}

// 正确：提供准确的类型
declare module "library" {
    export function process(value: string): string;
}
```

### 错误 2：缺少导出

```ts
// 错误：缺少 export
declare module "library" {
    function process(): void; // 错误：需要 export
}

// 正确
declare module "library" {
    export function process(): void;
}
```

## 注意事项

1. **类型准确**：确保类型定义准确
2. **导出声明**：需要导出的内容使用 export
3. **文件位置**：声明文件放在合适的位置
4. **类型安全**：确保类型定义类型安全

## 最佳实践

1. **分析 API**：仔细分析库的 API 结构
2. **类型准确**：提供准确的类型定义
3. **文档注释**：为类型添加文档注释
4. **测试验证**：测试类型定义是否正确

## 练习

1. **编写声明文件**：为无类型库编写声明文件。

2. **类型定义**：练习不同类型的类型定义。

3. **高级技巧**：使用泛型、函数重载等高级技巧。

4. **实际应用**：在实际场景中编写自定义声明文件。

完成以上练习后，继续学习下一节，了解第三方库声明文件处理。

## 总结

编写自定义声明文件为没有类型定义的库提供类型支持。需要分析库的 API 结构，定义准确的类型，并测试类型定义。理解自定义声明文件的编写是学习声明文件的关键。

## 相关资源

- [TypeScript 声明文件编写指南](https://www.typescriptlang.org/docs/handbook/declaration-files/introduction.html)
