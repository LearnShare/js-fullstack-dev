# 6.2.11 声明文件最佳实践

## 概述

本节总结声明文件编写的最佳实践，帮助编写高质量的类型定义。

## 最佳实践

### 1. 类型准确性

确保类型定义准确反映库的实际行为：

```ts
// 好的实践：准确的类型定义
declare module "library" {
    export function process(value: string): string;
    export function process(value: number): number;
}

// 不好的实践：使用 any
declare module "library" {
    export function process(value: any): any;
}
```

### 2. 完整的类型覆盖

为库的所有公共 API 提供类型定义：

```ts
// 好的实践：完整的类型定义
declare module "library" {
    export interface Config {
        apiUrl: string;
        timeout: number;
    }

    export function init(config: Config): void;
    export function process(): void;
    export class Library {
        method(): void;
    }
}
```

### 3. 使用泛型

使用泛型提供灵活的类型支持：

```ts
// 好的实践：使用泛型
declare module "library" {
    export interface ApiResponse<T> {
        data: T;
        status: number;
    }

    export function fetch<T>(): Promise<ApiResponse<T>>;
}
```

### 4. 文档注释

为类型定义添加文档注释：

```ts
// 好的实践：添加文档注释
declare module "library" {
    /**
     * 初始化库
     * @param config 配置对象
     */
    export function init(config: Config): void;

    /**
     * 处理数据
     * @param value 输入值
     * @returns 处理后的值
     */
    export function process(value: string): string;
}
```

### 5. 文件组织

合理组织声明文件：

```
types/
├── global.d.ts          # 全局声明
├── modules/             # 模块声明
│   ├── library-a.d.ts
│   └── library-b.d.ts
└── extensions/          # 类型扩展
    └── express.d.ts
```

## 常见模式

### 1. 函数库模式

```ts
declare module "function-library" {
    export function function1(): void;
    export function function2(): void;
}
```

### 2. 类库模式

```ts
declare module "class-library" {
    export class MyClass {
        constructor(config: Config);
        method(): void;
    }
}
```

### 3. 对象库模式

```ts
declare module "object-library" {
    export interface Config {
        option: string;
    }

    export const config: Config;
}
```

### 4. 混合库模式

```ts
declare module "mixed-library" {
    export function init(): void;
    export class Library {
        method(): void;
    }
    export interface Options {
        option: string;
    }
}
```

## 避免的错误

### 错误 1：使用 any

```ts
// 错误：使用 any
declare module "library" {
    export function process(value: any): any;
}

// 正确：使用具体类型
declare module "library" {
    export function process(value: string): string;
}
```

### 错误 2：类型不准确

```ts
// 错误：类型不准确
declare module "library" {
    export function process(value: string): number;
}

// 正确：准确的类型
declare module "library" {
    export function process(value: string): string;
}
```

### 错误 3：缺少导出

```ts
// 错误：缺少 export
declare module "library" {
    function process(): void;
}

// 正确：使用 export
declare module "library" {
    export function process(): void;
}
```

## 测试类型定义

### 1. 类型检查

确保类型定义通过类型检查：

```ts
import library from "library";

// 应该通过类型检查
library.process("value");
```

### 2. 实际使用

在实际项目中使用类型定义，验证是否正确。

### 3. 类型测试工具

使用类型测试工具验证类型定义：

```ts
// 使用类型测试工具
import { expectType } from "tsd";

expectType<string>(library.process("value"));
```

## 贡献类型定义

### 1. 提交到 DefinitelyTyped

为缺失的类型定义贡献代码：

1. Fork DefinitelyTyped 仓库
2. 创建类型定义文件
3. 提交 Pull Request

### 2. 维护类型定义

维护自己编写的类型定义，确保与库版本同步。

## 使用场景

### 1. 项目内部

为项目内部库编写类型定义：

```ts
// types/internal-library.d.ts
declare module "@company/internal-library" {
    export function process(): void;
}
```

### 2. 第三方库

为第三方库编写或扩展类型定义：

```ts
// types/third-party.d.ts
declare module "third-party" {
    export function process(): void;
}
```

### 3. 全局扩展

扩展全局类型：

```ts
// types/global.d.ts
declare global {
    interface Window {
        myAPI: {
            call(): void;
        };
    }
}

export {};
```

## 注意事项

1. **类型准确**：确保类型定义准确
2. **完整覆盖**：为所有公共 API 提供类型定义
3. **文档注释**：添加文档注释
4. **测试验证**：测试类型定义是否正确

## 最佳实践总结

1. **类型准确性**：确保类型定义准确反映库的行为
2. **完整覆盖**：为所有公共 API 提供类型定义
3. **使用泛型**：使用泛型提供灵活的类型支持
4. **文档注释**：为类型定义添加文档注释
5. **文件组织**：合理组织声明文件
6. **测试验证**：测试类型定义是否正确
7. **贡献代码**：为缺失的类型定义贡献代码

## 练习

1. **编写声明文件**：按照最佳实践编写声明文件。

2. **类型准确性**：确保类型定义准确。

3. **文档注释**：为类型定义添加文档注释。

4. **实际应用**：在实际场景中应用最佳实践。

完成以上练习后，声明文件章节学习完成。可以继续学习下一章：命名空间。

## 总结

声明文件最佳实践包括类型准确性、完整覆盖、使用泛型、文档注释、文件组织等。遵循最佳实践可以编写高质量的类型定义。理解声明文件最佳实践是学习声明文件的关键。

## 相关资源

- [TypeScript 声明文件最佳实践](https://www.typescriptlang.org/docs/handbook/declaration-files/do-s-and-don-ts.html)
