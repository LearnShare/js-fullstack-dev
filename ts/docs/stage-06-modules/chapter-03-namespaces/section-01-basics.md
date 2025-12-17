# 6.3.1 命名空间基础

## 概述

命名空间用于组织相关的类型和值。本节介绍命名空间的概念、定义和使用。

## 什么是命名空间

### 定义

命名空间是一种组织代码的方式，将相关的类型和值组织在一起。

### 基本概念

```ts
namespace MyNamespace {
    export function process(): void {}
    export const constant = "value";
    export interface Config {
        apiUrl: string;
    }
}
```

## 命名空间定义

### 基本语法

```ts
namespace NamespaceName {
    // 命名空间内容
}
```

### 示例

```ts
namespace MathUtils {
    export function add(a: number, b: number): number {
        return a + b;
    }

    export function subtract(a: number, b: number): number {
        return a - b;
    }

    export const PI = 3.14159;
}
```

## 命名空间使用

### 访问命名空间成员

```ts
// 使用命名空间
MathUtils.add(1, 2);
MathUtils.subtract(5, 3);
console.log(MathUtils.PI);
```

### 导入命名空间

```ts
// 使用 import 导入
import { MathUtils } from "./math-utils";

MathUtils.add(1, 2);
```

## 命名空间嵌套

### 嵌套命名空间

```ts
namespace MyLibrary {
    namespace Utils {
        export function format(value: any): string {
            return String(value);
        }
    }

    namespace API {
        export function call(): void {
            // ...
        }
    }
}

// 使用嵌套命名空间
MyLibrary.Utils.format("value");
MyLibrary.API.call();
```

## 命名空间与接口

### 在命名空间中定义接口

```ts
namespace MyLibrary {
    export interface Config {
        apiUrl: string;
        timeout: number;
    }

    export function init(config: Config): void {
        // ...
    }
}
```

## 使用场景

### 1. 组织相关代码

```ts
namespace StringUtils {
    export function capitalize(str: string): string {
        return str.charAt(0).toUpperCase() + str.slice(1);
    }

    export function reverse(str: string): string {
        return str.split("").reverse().join("");
    }
}
```

### 2. 避免全局污染

```ts
// 使用命名空间避免全局污染
namespace MyLibrary {
    export function process(): void {}
}
```

### 3. 类型组织

```ts
namespace Types {
    export interface User {
        name: string;
        age: number;
    }

    export interface Config {
        apiUrl: string;
    }
}
```

## 常见错误

### 错误 1：缺少 export

```ts
// 错误：缺少 export，无法访问
namespace MyNamespace {
    function process(): void {}
}

// 正确：使用 export
namespace MyNamespace {
    export function process(): void {}
}
```

### 错误 2：命名空间冲突

```ts
// 错误：命名空间名称冲突
namespace MyNamespace {
    // ...
}

namespace MyNamespace {
    // 错误：重复声明
}
```

## 注意事项

1. **export 关键字**：需要导出的成员使用 export
2. **命名空间合并**：同名命名空间会自动合并
3. **模块化**：考虑使用模块替代命名空间
4. **类型安全**：确保命名空间类型安全

## 最佳实践

1. **使用命名空间**：在需要时使用命名空间组织代码
2. **避免全局污染**：使用命名空间避免全局污染
3. **合理嵌套**：合理使用嵌套命名空间
4. **考虑模块**：考虑使用模块替代命名空间

## 练习

1. **命名空间定义**：定义和使用命名空间。

2. **命名空间嵌套**：定义嵌套命名空间。

3. **实际应用**：在实际场景中应用命名空间。

完成以上练习后，继续学习下一节，了解命名空间合并。

## 总结

命名空间用于组织相关的类型和值。使用 `namespace` 关键字定义命名空间，需要导出的成员使用 `export`。理解命名空间的基础是学习命名空间的关键。

## 相关资源

- [TypeScript 命名空间文档](https://www.typescriptlang.org/docs/handbook/namespaces.html)
