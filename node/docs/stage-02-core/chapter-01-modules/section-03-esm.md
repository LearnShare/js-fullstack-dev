# 2.1.3 ES Modules (ESM)

## 1. 概述

ES Modules (ESM) 是 JavaScript 的官方模块系统，也是 Node.js 推荐的现代模块系统。ESM 使用 `import` 和 `export` 语法，支持静态分析、Tree Shaking 和 Top-level await 等现代特性。在 Node.js 22+ 环境下，ESM 已成为构建新项目的首选。

## 2. 特性说明

- **静态分析**：模块依赖在编译时确定，支持更好的工具支持。
- **Tree Shaking**：未使用的导出会被自动移除，减小打包体积。
- **异步加载**：模块加载是异步的，适合现代应用场景。
- **Top-level await**：支持在模块顶层使用 `await`。
- **浏览器兼容**：现代浏览器原生支持，无需构建工具。
- **类型安全**：与 TypeScript 完美集成，提供更好的类型检查。

## 3. 语法与定义

### 模块导出

ESM 使用 `export` 关键字导出模块：

```ts
// 命名导出
export function add(a: number, b: number): number {
    return a + b;
}

export function subtract(a: number, b: number): number {
    return a - b;
}

// 默认导出
export default function calculate(a: number, b: number): number {
    return a + b;
}

// 导出类
export class Calculator {
    add(a: number, b: number): number {
        return a + b;
    }
}
```

### 模块导入

ESM 使用 `import` 关键字导入模块：

```ts
// 命名导入
import { add, subtract } from './math.js';

// 默认导入
import calculate from './math.js';

// 混合导入
import calculate, { add, subtract } from './math.js';

// 导入所有
import * as math from './math.js';

// 类型导入
import type { User } from './types.js';
```

## 4. 基本用法

### 示例 1：命名导出和导入

```ts
// 文件: utils.ts
// 功能: 工具函数模块

export function formatDate(date: Date): string {
    return date.toISOString();
}

export function formatCurrency(amount: number): string {
    return `$${amount.toFixed(2)}`;
}
```

```ts
// 文件: main.ts
// 功能: 使用工具函数

import { formatDate, formatCurrency } from './utils.js';

const date = new Date();
console.log(formatDate(date));
console.log(formatCurrency(100.5));
```

### 示例 2：默认导出和导入

```ts
// 文件: user.ts
// 功能: 用户类模块

export default class User {
    constructor(public name: string, public age: number) {}

    greet(): string {
        return `Hello, I'm ${this.name}, ${this.age} years old.`;
    }
}
```

```ts
// 文件: main.ts
// 功能: 使用用户类

import User from './user.js';

const user = new User('Alice', 25);
console.log(user.greet());
```

### 示例 3：Top-level await

```ts
// 文件: config.ts
// 功能: 异步加载配置

const config = await fetch('/api/config').then(res => res.json());

export default config;
```

```ts
// 文件: main.ts
// 功能: 使用配置

import config from './config.js';

console.log(config);
```

## 5. 参数说明：import 语句

`import` 语句的语法：

| 语法形式           | 示例                           | 说明                                     |
|:-------------------|:-------------------------------|:-----------------------------------------|
| **命名导入**       | `import { a, b } from './m.js'`| 导入模块的命名导出。                     |
| **默认导入**       | `import a from './m.js'`       | 导入模块的默认导出。                     |
| **命名空间导入**   | `import * as m from './m.js'`  | 导入整个模块作为命名空间。               |
| **类型导入**       | `import type { T } from './m.js'`| 仅导入类型，不导入值。                 |
| **副作用导入**     | `import './m.js'`              | 仅执行模块，不导入任何内容。             |

## 6. 返回值与状态说明

`import` 语句返回 Promise（对于动态导入）或直接返回值（对于静态导入）：

| 导入方式     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **静态导入** | 直接返回值   | 模块导出值，同步获取。                   |
| **动态导入** | `Promise<T>` | 返回 Promise，需要 await。               |

## 7. 代码示例：动态导入

ESM 支持动态导入，适合按需加载模块：

```ts
// 文件: main.ts
// 功能: 动态导入模块

async function loadModule() {
    // 动态导入
    const { add, subtract } = await import('./math.js');
    
    console.log(add(1, 2));      // 3
    console.log(subtract(5, 2)); // 3
}

loadModule();
```

## 8. 输出结果说明

```text
3
3
```

**逻辑解析**：
- 动态 `import()` 返回 Promise，需要使用 `await` 或 `.then()`
- 适合按需加载、条件导入等场景
- 不会阻塞主线程，提高应用启动速度

## 9. 使用场景

### 1. 现代 Node.js 项目

在现代 Node.js 项目中使用 ESM：

```ts
// 现代 Express 应用（使用 ESM）
import express from 'express';
const app = express();

app.get('/', (req, res) => {
    res.send('Hello World');
});

app.listen(3000);
```

### 2. 与前端代码共享

与前端代码共享模块：

```ts
// 共享类型定义
// 文件: shared/types.ts
export interface User {
    id: number;
    name: string;
}

// 后端使用
import type { User } from './shared/types.js';

// 前端使用
import type { User } from './shared/types.js';
```

### 3. Tree Shaking 优化

利用 Tree Shaking 减小打包体积：

```ts
// 只导入需要的函数
import { add } from './math.js'; // subtract 不会被包含

// 而不是导入整个模块
import * as math from './math.js'; // 所有导出都会被包含
```

## 10. 注意事项与常见错误

- **文件扩展名**：导入本地文件必须包含 `.js` 扩展名（即使源文件是 `.ts`）
- **package.json 配置**：必须在 `package.json` 中设置 `"type": "module"`
- **路径解析**：相对路径必须以 `./` 或 `../` 开头
- **默认导出**：每个模块只能有一个默认导出
- **循环依赖**：ESM 支持循环依赖，但需要正确设计模块结构

## 11. 常见问题 (FAQ)

**Q: 为什么导入 TypeScript 文件要写 `.js` 扩展名？**
A: 这是 ESM 规范的要求。TypeScript 编译器会正确处理 `.ts` 到 `.js` 的映射，确保编译后的代码路径正确。

**Q: ESM 可以导入 CommonJS 模块吗？**
A: 可以，但有限制。CommonJS 模块只能作为默认导入，不能使用命名导入。

**Q: 如何判断项目是否使用 ESM？**
A: 检查 `package.json` 中的 `"type": "module"` 字段，或检查文件扩展名（`.mjs` 或 `"type": "module"` 下的 `.js`）。

## 12. 最佳实践

- **优先使用 ESM**：新项目优先使用 ES Modules
- **明确扩展名**：导入本地文件时明确指定 `.js` 扩展名
- **使用 node: 前缀**：导入核心模块时使用 `node:` 前缀
- **类型导入**：使用 `import type` 进行类型导入，避免运行时导入
- **Tree Shaking**：使用命名导入而非命名空间导入，充分利用 Tree Shaking

## 13. 对比分析：ESM vs CommonJS

| 维度             | ES Modules                                  | CommonJS                                    |
|:-----------------|:--------------------------------------------|:--------------------------------------------|
| **语法**         | `import` / `export`                         | `require()` / `module.exports`              |
| **加载时机**     | 编译时静态分析                              | 运行时动态加载                              |
| **同步/异步**    | 异步                                        | 同步                                        |
| **Tree Shaking** | 支持                                        | 不支持                                      |
| **Top-level await** | 支持                                    | 不支持                                      |
| **浏览器支持**    | 现代浏览器原生支持                          | 需要构建工具                                |
| **类型安全**     | 与 TypeScript 完美集成                      | 需要额外配置                                |

## 14. 练习任务

1. **模块导出实践**：
   - 创建工具函数模块，使用 `export` 导出
   - 尝试不同的导出方式（命名导出、默认导出）
   - 理解导出方式的区别

2. **模块导入实践**：
   - 创建主文件，使用 `import` 导入模块
   - 尝试不同的导入方式（命名导入、默认导入、命名空间导入）
   - 理解导入方式的区别

3. **动态导入实践**：
   - 使用动态 `import()` 实现按需加载
   - 实现条件导入逻辑
   - 理解动态导入的使用场景

4. **Top-level await**：
   - 在模块顶层使用 `await`
   - 实现异步配置加载
   - 理解 Top-level await 的优势

5. **实际应用**：
   - 在实际项目中使用 ESM 组织代码
   - 利用 Tree Shaking 优化打包体积
   - 掌握 ESM 的最佳实践

完成以上练习后，继续学习下一节：模块解析与加载。

## 总结

ES Modules 是 Node.js 的现代模块系统：

- **语法**：使用 `import` 和 `export`
- **特点**：静态分析、Tree Shaking、Top-level await
- **适用场景**：新项目、现代应用、与前端代码共享
- **最佳实践**：明确扩展名、使用类型导入、充分利用 Tree Shaking

掌握 ESM 有助于构建现代化的 Node.js 应用。

---

**最后更新**：2025-01-XX
