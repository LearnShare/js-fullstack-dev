# 6.2.3 全局声明文件

## 概述

全局声明文件定义全局可用的类型。本节介绍全局声明文件的编写。

## 全局声明文件

### 定义

全局声明文件定义全局可用的类型，不需要导入即可使用。

### 基本语法

```ts
// global.d.ts
declare function globalFunction(): void;
declare const globalConstant: string;
declare var globalVariable: number;
```

## declare 关键字

### 函数声明

```ts
declare function process(data: any): void;
declare function calculate(a: number, b: number): number;
```

### 变量声明

```ts
declare const API_URL: string;
declare var globalConfig: {
    apiUrl: string;
    timeout: number;
};
```

### 类声明

```ts
declare class GlobalClass {
    method(): void;
}
```

### 接口声明

```ts
declare interface GlobalInterface {
    property: string;
}
```

## declare global

### 扩展全局类型

```ts
// global.d.ts
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

export {}; // 使文件成为模块
```

### 使用

```ts
// 可以直接使用
window.myAPI.call();
document.customMethod();
```

## 使用场景

### 1. 全局变量

```ts
// global.d.ts
declare const __VERSION__: string;
declare const __BUILD_TIME__: string;
```

### 2. 全局函数

```ts
// global.d.ts
declare function log(message: string): void;
declare function error(message: string): void;
```

### 3. 扩展全局对象

```ts
// global.d.ts
declare global {
    interface Window {
        myProperty: string;
    }
}

export {};
```

## 常见错误

### 错误 1：缺少 declare

```ts
// 错误：全局声明需要 declare
function globalFunction(): void;

// 正确
declare function globalFunction(): void;
```

### 错误 2：declare global 缺少 export

```ts
// 错误：declare global 需要 export {} 使文件成为模块
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

## 注意事项

1. **declare 关键字**：全局声明需要使用 declare
2. **declare global**：扩展全局类型需要使用 declare global
3. **export {}**：declare global 需要 export {} 使文件成为模块
4. **类型安全**：确保全局声明类型安全

## 最佳实践

1. **使用 declare**：全局声明使用 declare 关键字
2. **declare global**：扩展全局类型使用 declare global
3. **文件组织**：合理组织全局声明文件
4. **类型安全**：确保全局声明类型安全

## 练习

1. **全局声明**：编写全局函数和变量声明。

2. **declare global**：使用 declare global 扩展全局类型。

3. **实际应用**：在实际场景中应用全局声明文件。

完成以上练习后，继续学习下一节，了解模块声明文件。

## 总结

全局声明文件定义全局可用的类型。使用 `declare` 关键字声明全局类型，使用 `declare global` 扩展全局类型。理解全局声明文件的编写是学习声明文件的关键。

## 相关资源

- [TypeScript 全局声明文档](https://www.typescriptlang.org/docs/handbook/declaration-files/templates/global-d-ts.html)
