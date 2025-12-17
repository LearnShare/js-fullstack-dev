# 6.1.5 类型导入（import type）

## 概述

类型导入允许只导入类型，不会在运行时包含导入的代码。本节介绍类型导入的使用。

## 什么是类型导入

### 定义

类型导入使用 `import type` 语法，只导入类型信息，不会在运行时包含导入的代码。

### 基本语法

```ts
import type { TypeName } from "./types";
```

### 示例

```ts
// types.ts
export interface User {
    name: string;
    age: number;
}

export type Status = "active" | "inactive";

// 使用类型导入
import type { User, Status } from "./types";

function process(user: User, status: Status): void {
    // ...
}
```

## 类型导入 vs 值导入

### 区别

| 特性       | 类型导入（import type）  | 值导入（import）        |
|:-----------|:-------------------------|:------------------------|
| 运行时     | 不包含在运行时           | 包含在运行时            |
| 使用场景   | 只导入类型               | 导入值和类型            |
| 编译后     | 被移除                   | 保留                    |

### 示例对比

```ts
// 类型导入：编译后会被移除
import type { User } from "./types";

// 值导入：编译后保留
import { User } from "./types";
```

## 使用场景

### 1. 只导入类型

```ts
import type { User, ApiResponse } from "./types";

function process(user: User): ApiResponse<User> {
    // ...
}
```

### 2. 避免循环依赖

```ts
// 使用类型导入避免循环依赖
import type { User } from "./user";
```

### 3. 减少打包体积

```ts
// 类型导入不会增加打包体积
import type { Config } from "./config";
```

## 混合导入

### 类型和值混合

```ts
// 导入值和类型
import { process, type User } from "./utils";

// 或分开导入
import { process } from "./utils";
import type { User } from "./utils";
```

## 常见错误

### 错误 1：类型导入用作值

```ts
// 错误：类型导入不能用作值
import type { User } from "./types";
let user = new User(); // 错误

// 正确：使用值导入
import { User } from "./types";
let user = new User();
```

### 错误 2：值导入用作类型

```ts
// 可以，但不推荐
import { User } from "./types";
let user: User = { name: "John", age: 30 };

// 推荐：使用类型导入
import type { User } from "./types";
let user: User = { name: "John", age: 30 };
```

## 注意事项

1. **类型导入**：只导入类型，不包含运行时代码
2. **不能用作值**：类型导入不能用作值
3. **编译移除**：类型导入在编译后会被移除
4. **减少体积**：使用类型导入可以减少打包体积

## 最佳实践

1. **使用类型导入**：在只导入类型时使用类型导入
2. **减少体积**：使用类型导入减少打包体积
3. **避免循环依赖**：使用类型导入避免循环依赖
4. **明确意图**：使用类型导入明确表达意图

## 练习

1. **类型导入**：使用类型导入导入类型。

2. **混合导入**：练习类型和值的混合导入。

3. **实际应用**：在实际场景中应用类型导入。

4. **打包优化**：使用类型导入优化打包体积。

完成以上练习后，模块系统章节学习完成。可以继续学习下一章：声明文件。

## 总结

类型导入允许只导入类型，不会在运行时包含导入的代码。使用 `import type` 语法，可以减少打包体积，避免循环依赖。理解类型导入的使用是学习 TypeScript 模块系统的关键。

## 相关资源

- [TypeScript 类型导入文档](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-8.html#type-only-imports-and-export)
