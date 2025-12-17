# 6.2.2 声明文件类型

## 概述

声明文件有不同的类型，用于不同的场景。本节介绍不同类型的声明文件。

## 声明文件类型

### 1. 全局声明文件

全局声明文件定义全局类型：

```ts
// global.d.ts
declare function globalFunction(): void;
declare const globalConstant: string;
```

### 2. 模块声明文件

模块声明文件为模块提供类型：

```ts
// my-module.d.ts
declare module "my-module" {
    export function process(): void;
}
```

### 3. 类型声明文件

类型声明文件定义类型：

```ts
// types.d.ts
export interface User {
    name: string;
    age: number;
}
```

## 全局声明文件

### 特点

- 不需要导入
- 自动可用
- 使用 `declare` 关键字

### 示例

```ts
// global.d.ts
declare const API_URL: string;
declare function log(message: string): void;

// 可以直接使用
console.log(API_URL);
log("Hello");
```

## 模块声明文件

### 特点

- 需要导入
- 为模块提供类型
- 使用 `declare module`

### 示例

```ts
// my-module.d.ts
declare module "my-module" {
    export interface Config {
        apiUrl: string;
    }
    export function init(config: Config): void;
}

// 使用
import { init, type Config } from "my-module";
```

## 类型声明文件

### 特点

- 只包含类型
- 可以导出类型
- 不包含实现

### 示例

```ts
// types.d.ts
export interface User {
    name: string;
    age: number;
}

export type Status = "active" | "inactive";
```

## 使用场景

### 1. 全局类型

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

### 2. 第三方库

```ts
// jquery.d.ts
declare module "jquery" {
    export function ajax(settings: any): void;
}
```

### 3. 类型定义

```ts
// types.d.ts
export interface ApiResponse<T> {
    data: T;
    status: number;
}
```

## 常见错误

### 错误 1：类型混淆

```ts
// 错误：混淆了声明文件类型
declare module "types" {
    // 应该使用类型声明文件
}
```

### 错误 2：缺少 declare

```ts
// 错误：全局声明需要 declare
function globalFunction(): void;

// 正确
declare function globalFunction(): void;
```

## 注意事项

1. **文件类型**：根据用途选择正确的声明文件类型
2. **declare 关键字**：全局声明需要使用 declare
3. **模块声明**：模块声明使用 declare module
4. **类型安全**：确保声明文件类型安全

## 最佳实践

1. **选择类型**：根据用途选择正确的声明文件类型
2. **明确类型**：为声明提供明确的类型
3. **文件组织**：合理组织不同类型的声明文件
4. **类型安全**：利用声明文件提高类型安全

## 练习

1. **全局声明**：编写全局声明文件。

2. **模块声明**：编写模块声明文件。

3. **类型声明**：编写类型声明文件。

4. **实际应用**：在实际场景中应用不同类型的声明文件。

完成以上练习后，继续学习下一节，了解全局声明文件。

## 总结

声明文件有不同的类型，包括全局声明文件、模块声明文件、类型声明文件。根据用途选择正确的类型。理解声明文件类型是学习声明文件的关键。

## 相关资源

- [TypeScript 声明文件类型文档](https://www.typescriptlang.org/docs/handbook/declaration-files/introduction.html)
