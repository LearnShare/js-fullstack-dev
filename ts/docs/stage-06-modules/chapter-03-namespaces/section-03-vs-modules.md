# 6.3.3 命名空间 vs 模块

## 概述

命名空间和模块都可以组织代码，但它们有不同的用途。本节介绍命名空间与模块的对比。

## 命名空间 vs 模块

### 对比

| 特性       | 命名空间（Namespace）        | 模块（Module）               |
|:-----------|:-----------------------------|:-----------------------------|
| 作用域     | 全局或文件内                  | 模块作用域                   |
| 导入方式   | 直接访问或 import             | 必须 import                  |
| 文件组织   | 单文件或多文件                | 每个模块一个文件              |
| 使用场景   | 组织相关代码、避免全局污染    | 模块化开发、代码复用         |
| 现代性     | 较旧的方式                    | 现代标准方式                 |

### 示例对比

```ts
// 命名空间
namespace MyNamespace {
    export function process(): void {}
}

// 使用命名空间
MyNamespace.process();

// 模块
// math.ts
export function process(): void {}

// 使用模块
import { process } from "./math";
process();
```

## 命名空间的特点

### 优点

1. **简单直接**：可以直接访问，不需要导入
2. **避免全局污染**：使用命名空间避免全局污染
3. **组织代码**：可以组织相关的代码

### 缺点

1. **较旧的方式**：不是现代标准方式
2. **文件组织**：不适合大型项目
3. **依赖管理**：依赖管理不如模块清晰

## 模块的特点

### 优点

1. **现代标准**：ES Modules 是 JavaScript 标准
2. **文件组织**：每个模块一个文件，结构清晰
3. **依赖管理**：依赖管理清晰
4. **工具支持**：工具支持完善

### 缺点

1. **需要导入**：必须使用 import 导入
2. **学习曲线**：需要理解模块系统

## 使用场景

### 命名空间适用场景

1. **组织相关代码**：组织相关的类型和值
2. **避免全局污染**：避免全局变量污染
3. **声明文件**：在声明文件中使用命名空间

### 模块适用场景

1. **现代项目**：现代 TypeScript/JavaScript 项目
2. **大型项目**：大型项目的代码组织
3. **代码复用**：需要代码复用的场景

## 迁移建议

### 从命名空间迁移到模块

```ts
// 命名空间方式
namespace MyLibrary {
    export function process(): void {}
}

// 模块方式
// my-library.ts
export function process(): void {}

// 使用
import { process } from "./my-library";
process();
```

## 最佳实践

### 1. 优先使用模块

```ts
// 推荐：使用模块
// utils.ts
export function format(value: any): string {
    return String(value);
}

// 使用
import { format } from "./utils";
```

### 2. 命名空间用于声明文件

```ts
// 在声明文件中使用命名空间
declare namespace jQuery {
    export function $(selector: string): JQuery;
}
```

### 3. 避免混用

避免在同一项目中混用命名空间和模块。

## 常见错误

### 错误 1：混用命名空间和模块

```ts
// 错误：混用命名空间和模块
namespace MyNamespace {
    export function process(): void {}
}

import { process } from "./my-namespace"; // 错误
```

### 错误 2：过度使用命名空间

```ts
// 错误：过度使用命名空间
namespace Utils {
    namespace String {
        namespace Format {
            export function process(): void {}
        }
    }
}

// 推荐：使用模块
// utils/string/format.ts
export function process(): void {}
```

## 注意事项

1. **优先模块**：优先使用模块而不是命名空间
2. **声明文件**：在声明文件中可以使用命名空间
3. **避免混用**：避免在同一项目中混用
4. **现代标准**：遵循现代标准使用模块

## 最佳实践总结

1. **优先使用模块**：现代项目优先使用模块
2. **命名空间用于声明文件**：在声明文件中使用命名空间
3. **避免混用**：避免在同一项目中混用
4. **遵循标准**：遵循现代标准使用模块

## 练习

1. **命名空间 vs 模块**：对比命名空间和模块的使用。

2. **迁移练习**：练习从命名空间迁移到模块。

3. **实际应用**：在实际场景中选择合适的方式。

完成以上练习后，命名空间章节学习完成。可以继续学习下一章：类型生成工具。

## 总结

命名空间和模块都可以组织代码，但模块是现代标准方式。优先使用模块，在声明文件中可以使用命名空间。理解命名空间与模块的区别是学习命名空间的关键。

## 相关资源

- [TypeScript 命名空间 vs 模块](https://www.typescriptlang.org/docs/handbook/namespaces-and-modules.html)
