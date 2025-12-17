# 6.2.4 模块声明文件

## 概述

模块声明文件为模块提供类型定义。本节介绍模块声明文件的编写。

## 模块声明文件

### 定义

模块声明文件使用 `declare module` 为模块提供类型定义。

### 基本语法

```ts
// my-module.d.ts
declare module "my-module" {
    export function process(): void;
    export interface Config {
        apiUrl: string;
    }
}
```

## declare module

### 基本用法

```ts
declare module "module-name" {
    // 模块内容
}
```

### 示例

```ts
// jquery.d.ts
declare module "jquery" {
    export function ajax(settings: {
        url: string;
        method?: string;
        data?: any;
    }): void;

    export interface JQuery {
        text(): string;
        html(html: string): JQuery;
    }
}
```

## 模块导出

### 命名导出

```ts
declare module "my-module" {
    export function process(): void;
    export const constant: string;
    export interface Config {
        apiUrl: string;
    }
}
```

### 默认导出

```ts
declare module "my-module" {
    export default class MyClass {
        method(): void;
    }
}
```

### 混合导出

```ts
declare module "my-module" {
    export function process(): void;
    export default class MyClass {
        method(): void;
    }
}
```

## 使用场景

### 1. 第三方库类型

```ts
// third-party.d.ts
declare module "third-party-library" {
    export function init(config: any): void;
    export interface Options {
        apiUrl: string;
    }
}
```

### 2. 无类型模块

```ts
// untyped-module.d.ts
declare module "untyped-module" {
    const content: any;
    export default content;
}
```

### 3. 文件模块

```ts
// file-module.d.ts
declare module "*.json" {
    const content: any;
    export default content;
}

declare module "*.css" {
    const content: string;
    export default content;
}
```

## 常见错误

### 错误 1：模块名错误

```ts
// 错误：模块名不正确
declare module "my-module" {
    // 模块名必须与实际模块名匹配
}
```

### 错误 2：缺少导出

```ts
// 错误：没有导出
declare module "my-module" {
    function process(): void; // 错误：需要 export
}

// 正确
declare module "my-module" {
    export function process(): void;
}
```

## 注意事项

1. **模块名匹配**：模块名必须与实际模块名匹配
2. **导出声明**：模块内容需要导出
3. **类型定义**：只包含类型定义，不包含实现
4. **类型安全**：确保模块声明类型安全

## 最佳实践

1. **使用 declare module**：为模块提供类型定义
2. **明确类型**：为模块内容提供明确的类型
3. **文件组织**：合理组织模块声明文件
4. **类型安全**：确保模块声明类型安全

## 练习

1. **模块声明**：编写模块声明文件。

2. **模块导出**：练习模块的导出声明。

3. **文件模块**：为文件模块编写声明。

4. **实际应用**：在实际场景中应用模块声明文件。

完成以上练习后，继续学习下一节，了解 declare module 与 declare global。

## 总结

模块声明文件使用 `declare module` 为模块提供类型定义。模块名必须与实际模块名匹配，模块内容需要导出。理解模块声明文件的编写是学习声明文件的关键。

## 相关资源

- [TypeScript 模块声明文档](https://www.typescriptlang.org/docs/handbook/declaration-files/templates/module-d-ts.html)
