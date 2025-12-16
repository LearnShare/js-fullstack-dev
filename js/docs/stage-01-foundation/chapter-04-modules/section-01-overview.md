# 1.3.1 模块化与包管理概述

## 概述

模块化是将代码组织成职责明确、可复用、可测试、可组合的独立单元的编程方法。它是现代前端和 Node.js 工程化的基石，直接影响可维护性、可测试性、性能和团队协作。本节梳理模块化演进、主流模块系统特点、选择策略与最佳实践。

## 模块化核心价值

- **隔离与复用**：避免全局污染，提升可复用性。
- **依赖可视化**：明确模块边界和依赖关系，便于拆分与优化。
- **团队协作**：不同成员可并行开发各自模块，接口契约清晰。
- **可测试性**：模块可独立单测/集成测试。
- **性能与可部署性**：模块化是打包、代码分割、Tree Shaking 的前提。

## 模块化演进简史

### 全局脚本时代
```js
// 全局污染示例
var globalVar = 'value';
function globalFunction() {
  // ...
}
```
缺陷：命名冲突、依赖不可控、不可按需加载。

### IIFE / Module Pattern
```js
var MyModule = (function() {
  var privateVar = 'private';
  function privateFn() {}
  return {
    publicMethod() { return privateVar; }
  };
})();
```
优点：私有作用域、减少冲突；缺陷：依赖管理仍弱。

### AMD (RequireJS)
```js
define(['dep1', 'dep2'], function(d1, d2) {
  return { method() {} };
});
```
异步加载，适合浏览器早期按需加载；需要加载器，生态已弱化。

### CommonJS (CJS)
```js
// 导出
module.exports = { fn() {} };
// 导入
const { fn } = require('./module');
```
同步加载，Node.js 原生；对静态分析较弱。

### ES Modules (ESM)
```js
// module.js
export function fn() {}
// main.js
import { fn } from './module.js';
```
静态、可分析、Tree Shaking 友好，浏览器/Node 原生支持。

## 主流模块系统对比

| 特性           | ES Modules                 | CommonJS                   | AMD                      |
| :------------- | :------------------------- | :------------------------- | :----------------------- |
| 加载方式       | 静态、可异步               | 同步                       | 异步                     |
| Tree Shaking   | 友好                       | 困难                       | 一般                     |
| 适用场景       | 现代前端、Node 新项目      | 旧版 Node/遗留依赖         | 旧浏览器按需加载         |
| 语法           | import/export              | require/module.exports     | define/require           |
| 原生支持       | 浏览器、Node 16+           | Node 原生                  | 需加载器                 |

选择建议：
- 浏览器/前端：优先 ESM。
- Node：新项目用 ESM；遗留兼容使用 CJS 或双入口。
- 旧环境：必要时使用 AMD（逐步淘汰）。

## 包管理与依赖策略

- **包管理器**：npm/pnpm/yarn；建议 pnpm（去重好、磁盘占用小）。
- **语义化版本**：`^1.2.3`（小版本兼容），`~1.2.3`（仅补丁），锁定版本用于可重复构建。
- **依赖分类**：dependencies / devDependencies / peerDependencies / optionalDependencies。
- **锁文件**：`package-lock.json`/`pnpm-lock.yaml`/`yarn.lock`，务必提交。
- **镜像与缓存**：合理配置 registry，加速安装。

## 模块选择与决策树

1. **运行环境**：浏览器优先 ESM；Node 新项目优先 ESM，如需旧包可局部 CJS。
2. **产物需求**：应用 → 优先 Vite/ESM；库 → 产出 ESM + CJS 双格式。
3. **加载方式**：需懒加载/分包 → ESM + 动态 import；纯后端同步 → 可 CJS。
4. **生态兼容**：依赖若仅 CJS，Node 场景可直接用；浏览器需打包。

## 模块边界与设计原则

- **单一职责**：每个模块聚焦一个职责。
- **清晰接口**：仅导出需要的 API，隐藏实现。
- **避免循环依赖**：重构为中间层或拆分职责。
- **稳定契约**：导出 API 稳定，变更遵守 SemVer。
- **副作用管理**：避免在模块顶层做副作用；若必须，分离为独立入口并在 `package.json` 声明 `sideEffects`。

示例——单一职责与清晰接口：
```js
// math.js
export function add(a, b) { return a + b; }
export function subtract(a, b) { return a - b; }

// utils.js（反例：混合无关职责）
export function add(a, b) {}
export function formatDate(date) {}
export function validateEmail(email) {}
```

避免循环依赖：
```js
// moduleA.js
import { funcB } from './moduleB.js';
export function funcA() { funcB(); }

// moduleB.js
// import { funcA } from './moduleA.js'; // 循环
export function funcB() { /* ... */ }

// 解决：提取公共逻辑到 moduleShared.js
```

## 模块系统与构建

- **Tree Shaking 前提**：ESM + 无副作用。
- **代码分割**：动态导入实现懒加载；路由/组件级分包。
- **格式输出**：浏览器优先 ESM；Node/库常需 ESM + CJS。
- **声明 sideEffects**：`"sideEffects": false` 或列出有副作用的文件。

## 常见问题与排查

- **循环依赖**：导出为空或部分；重构依赖图。
- **未写扩展名 (Node ESM)**：需要显式 `.js/.mjs/.cjs`。
- **混用 CJS/ESM**：默认导出/命名导出行为差异，注意互操作。
- **副作用 Tree Shaking 失败**：声明 sideEffects，避免顶层执行逻辑。

## 练习

1. 将一个全局脚本重构为 ESM 模块，拆分为职责清晰的文件。
2. 构造一个循环依赖示例并重构消除循环。
3. 在 `package.json` 声明 `sideEffects: false`，观察构建体积变化。
4. 使用动态 `import()` 为路由实现懒加载，并验证分包情况。
5. 为一个小型库同时产出 ESM 与 CJS，并在 Node/浏览器中分别验证导入。

## 总结

模块化奠定了现代 JavaScript 工程的基础。理解模块系统演进、ESM/CJS/AMD 的差异与选型原则，结合包管理、依赖治理、Tree Shaking 与代码分割的最佳实践，能显著提升代码的可维护性、性能和可扩展性。

## 相关资源

- [MDN ES Modules 文档](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Modules)
- [Node.js 模块文档](https://nodejs.org/api/modules.html)
