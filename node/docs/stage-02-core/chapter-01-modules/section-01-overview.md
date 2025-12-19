# 2.1.1 模块系统概述

## 1. 概述

Node.js 的模块系统允许开发者将代码组织成可重用的模块，实现代码的模块化和复用。Node.js 支持两种模块系统：CommonJS（传统）和 ES Modules（现代）。理解模块系统的工作原理对于构建大型 Node.js 应用至关重要。

## 2. 特性说明

- **代码组织**：将代码分割成独立的模块，提高代码的可维护性和可复用性。
- **命名空间隔离**：每个模块拥有独立的作用域，避免全局变量污染。
- **依赖管理**：通过导入和导出机制管理模块间的依赖关系。
- **按需加载**：模块按需加载，提高应用启动速度。
- **循环依赖处理**：Node.js 提供了循环依赖的处理机制。

## 3. 模块系统类型

Node.js 支持两种模块系统：

| 模块系统     | 引入时间 | 语法特点                                     | 适用场景                       |
|:-------------|:---------|:---------------------------------------------|:-------------------------------|
| **CommonJS** | Node.js 早期 | `require()` / `module.exports`               | 传统 Node.js 项目、向后兼容。  |
| **ES Modules**| Node.js 12+ | `import` / `export`                          | 现代项目、与前端代码统一。     |

## 4. 模块系统选择

### CommonJS 适用场景

- 传统 Node.js 项目
- 需要向后兼容的代码库
- 使用大量 CommonJS 依赖的项目

### ES Modules 适用场景

- 新项目（推荐）
- 需要与前端代码共享模块
- 需要静态分析和 Tree Shaking
- 使用现代构建工具的项目

## 5. 模块解析机制

Node.js 的模块解析遵循以下规则：

| 模块类型     | 解析方式                                     | 示例                           |
|:-------------|:---------------------------------------------|:-------------------------------|
| **核心模块** | 直接使用模块名                                | `import fs from 'node:fs'`     |
| **本地模块** | 使用相对路径或绝对路径                        | `import utils from './utils.js'`|
| **node_modules**| 从 `node_modules` 目录查找                  | `import express from 'express'`|

## 6. 代码示例：模块系统基础

以下示例演示了 CommonJS 和 ESM 的基本用法。

### CommonJS 示例

```ts
// 文件: math.cjs
// 功能: CommonJS 模块导出

function add(a: number, b: number): number {
    return a + b;
}

function subtract(a: number, b: number): number {
    return a - b;
}

module.exports = {
    add,
    subtract
};
```

```ts
// 文件: main.cjs
// 功能: CommonJS 模块导入

const { add, subtract } = require('./math.cjs');

console.log(add(1, 2));      // 3
console.log(subtract(5, 2)); // 3
```

### ES Modules 示例

```ts
// 文件: math.ts
// 功能: ES Modules 模块导出

export function add(a: number, b: number): number {
    return a + b;
}

export function subtract(a: number, b: number): number {
    return a - b;
}
```

```ts
// 文件: main.ts
// 功能: ES Modules 模块导入

import { add, subtract } from './math.js';

console.log(add(1, 2));      // 3
console.log(subtract(5, 2)); // 3
```

## 7. 输出结果说明

两种模块系统的输出结果相同：

```text
3
3
```

**逻辑解析**：
- CommonJS 使用 `require()` 和 `module.exports` 进行模块导入导出
- ESM 使用 `import` 和 `export` 进行模块导入导出
- 两种方式都能实现模块化，但 ESM 是未来的标准

## 8. 注意事项与常见错误

- **文件扩展名**：ESM 模式下，导入本地文件必须包含 `.js` 扩展名（即使源文件是 `.ts`）
- **package.json 配置**：使用 ESM 需要在 `package.json` 中设置 `"type": "module"`
- **混合使用**：尽量避免在同一项目中混合使用 CommonJS 和 ESM
- **循环依赖**：注意避免模块间的循环依赖，可能导致未定义的行为
- **路径解析**：ESM 使用 URL 风格的路径解析，相对路径必须以 `./` 或 `../` 开头

## 9. 常见问题 (FAQ)

**Q: CommonJS 和 ESM 可以混用吗？**
A: 可以，但不推荐。CommonJS 可以导入 ESM，但 ESM 不能直接导入 CommonJS（需要使用 `createRequire` 或默认导入）。

**Q: 为什么 ESM 导入本地文件要写 `.js` 扩展名？**
A: 这是 ESM 规范的要求，确保模块路径的明确性和一致性。TypeScript 编译器会正确处理 `.ts` 到 `.js` 的映射。

**Q: 如何判断项目使用的是哪种模块系统？**
A: 检查 `package.json` 中的 `"type"` 字段。如果设置为 `"module"`，则使用 ESM；否则使用 CommonJS。

## 10. 最佳实践

- **优先使用 ESM**：新项目优先使用 ES Modules，这是未来的标准
- **统一模块系统**：在同一项目中统一使用一种模块系统
- **使用 node: 前缀**：导入 Node.js 核心模块时使用 `node:` 前缀（如 `node:fs`）
- **明确路径**：使用明确的相对路径或绝对路径，避免隐式路径解析
- **类型定义**：为模块导出添加 TypeScript 类型定义

## 11. 对比分析：CommonJS vs ES Modules

| 维度             | CommonJS                                    | ES Modules                                  |
|:-----------------|:--------------------------------------------|:--------------------------------------------|
| **语法**         | `require()` / `module.exports`              | `import` / `export`                         |
| **加载时机**     | 运行时动态加载                              | 编译时静态分析                              |
| **Tree Shaking** | 不支持                                      | 支持                                        |
| **循环依赖**     | 支持，但可能导致未定义行为                  | 支持，更安全                                |
| **Top-level await** | 不支持                                  | 支持                                        |
| **浏览器兼容**   | 需要构建工具转换                            | 现代浏览器原生支持                          |

## 12. 练习任务

1. **模块导出实践**：
   - 创建一个工具函数模块，导出多个函数
   - 使用 CommonJS 和 ESM 两种方式实现
   - 对比两种方式的差异

2. **模块导入实践**：
   - 创建主文件，导入工具函数模块
   - 使用不同的导入方式（命名导入、默认导入）
   - 理解导入方式的区别

3. **路径解析实验**：
   - 尝试不同的模块路径（相对路径、绝对路径、node_modules）
   - 观察模块解析的行为
   - 理解模块解析的优先级

4. **循环依赖实验**：
   - 创建两个相互依赖的模块
   - 观察循环依赖的行为
   - 理解如何避免循环依赖

5. **实际应用**：
   - 在实际项目中组织模块结构
   - 使用模块系统实现代码复用
   - 理解模块系统在大型项目中的作用

完成以上练习后，继续学习下一节：CommonJS 模块。

## 总结

模块系统是 Node.js 的核心特性：

- **两种系统**：CommonJS（传统）和 ES Modules（现代）
- **代码组织**：通过模块实现代码的模块化和复用
- **依赖管理**：通过导入导出管理模块间的依赖
- **最佳实践**：新项目优先使用 ES Modules

理解模块系统有助于构建可维护的大型 Node.js 应用。

---

**最后更新**：2025-01-XX
