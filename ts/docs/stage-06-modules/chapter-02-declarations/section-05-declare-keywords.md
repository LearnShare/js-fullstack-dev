# 6.2.5 declare module 与 declare global

## 概述

`declare module` 和 `declare global` 是声明文件中的关键字。本节介绍它们的使用和区别。

## declare module

### 定义

`declare module` 用于为模块提供类型定义。

### 语法

```ts
declare module "module-name" {
    // 模块内容
}
```

### 示例

```ts
declare module "my-module" {
    export function process(): void;
    export interface Config {
        apiUrl: string;
    }
}
```

## declare global

### 定义

`declare global` 用于扩展全局类型。

### 语法

```ts
declare global {
    // 全局类型扩展
}

export {}; // 使文件成为模块
```

### 示例

```ts
declare global {
    interface Window {
        myAPI: {
            call(): void;
        };
    }

    interface Document {
        customMethod(): void;
    }
}

export {};
```

## 区别

### 对比

| 特性       | declare module            | declare global            |
|:-----------|:--------------------------|:--------------------------|
| 作用       | 为模块提供类型            | 扩展全局类型              |
| 使用场景   | 第三方库、文件模块        | 扩展全局对象              |
| 需要 export| 不需要                    | 需要 export {}            |
| 模块名     | 需要指定模块名            | 不需要                    |

### 示例对比

```ts
// declare module：为模块提供类型
declare module "jquery" {
    export function ajax(settings: any): void;
}

// declare global：扩展全局类型
declare global {
    interface Window {
        myAPI: any;
    }
}

export {};
```

## 组合使用

### 同时使用

```ts
// 扩展全局类型
declare global {
    interface Window {
        myAPI: any;
    }
}

// 为模块提供类型
declare module "my-module" {
    export function process(): void;
}

export {};
```

## 使用场景

### 1. declare module

```ts
// 第三方库类型
declare module "third-party" {
    export function init(): void;
}

// 文件模块类型
declare module "*.json" {
    const content: any;
    export default content;
}
```

### 2. declare global

```ts
// 扩展全局对象
declare global {
    interface Window {
        myProperty: string;
    }
}

export {};
```

## 常见错误

### 错误 1：declare global 缺少 export

```ts
// 错误：declare global 需要 export {}
declare global {
    interface Window {
        myAPI: any;
    }
}

// 正确
declare global {
    interface Window {
        myAPI: any;
    }
}

export {};
```

### 错误 2：混淆使用

```ts
// 错误：混淆了 declare module 和 declare global
declare module global {
    // 错误
}

// 正确
declare global {
    // 正确
}
```

## 注意事项

1. **declare module**：用于为模块提供类型
2. **declare global**：用于扩展全局类型
3. **export {}**：declare global 需要 export {}
4. **类型安全**：确保声明类型安全

## 最佳实践

1. **选择正确**：根据用途选择正确的关键字
2. **declare module**：为模块提供类型时使用
3. **declare global**：扩展全局类型时使用
4. **类型安全**：确保声明类型安全

## 练习

1. **declare module**：使用 declare module 为模块提供类型。

2. **declare global**：使用 declare global 扩展全局类型。

3. **组合使用**：组合使用 declare module 和 declare global。

4. **实际应用**：在实际场景中应用这些关键字。

完成以上练习后，继续学习下一节，了解 declare namespace。

## 总结

`declare module` 用于为模块提供类型定义，`declare global` 用于扩展全局类型。理解它们的区别和使用是学习声明文件的关键。

## 相关资源

- [TypeScript declare module 文档](https://www.typescriptlang.org/docs/handbook/declaration-files/templates/module-d-ts.html)
- [TypeScript declare global 文档](https://www.typescriptlang.org/docs/handbook/declaration-files/templates/global-d-ts.html)
