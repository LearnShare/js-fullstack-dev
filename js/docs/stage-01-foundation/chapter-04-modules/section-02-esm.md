# 1.3.2 ES Modules (ESM)

## 概述

ES Modules（ESM）是 ES6 引入的标准模块系统，提供静态导入/导出、编译期可分析、与浏览器和 Node.js 原生支持的模块规范。理解 ESM 对现代前端、Node.js、打包与 Tree Shaking 都至关重要。

## 核心特性

- **静态结构**：`import`/`export` 必须在顶层，便于静态分析与 Tree Shaking。
- **按需加载**：支持 `import()` 动态导入，实现代码分割和懒加载。
- **模块作用域**：每个文件是独立作用域，避免全局污染。
- **Live Binding**：导出值是活绑定，更新后导入侧可见。
- **异步模块**：加载可异步，浏览器与 Node.js 均支持。

## 导出

### 命名导出

```js
// math.js
export function add(a, b) {
  return a + b;
}

export function subtract(a, b) {
  return a - b;
}

export const PI = 3.14159;
```

### 默认导出

```js
// User.js
export default class User {
  constructor(name) {
    this.name = name;
  }
}
```

### 混合导出

```js
// utils.js
export function helper() {
  // ...
}

export default function main() {
  // ...
}
```

### 重新导出

```js
// index.js
export { add, subtract } from './math.js';
export { default as User } from './User.js';
```

## 导入

### 命名导入

```js
// main.js
import { add, subtract, PI } from './math.js';

console.log(add(1, 2));
console.log(PI);
```

### 默认导入

```js
import User from './User.js';
const user = new User('John');
```

### 混合导入

```js
import User, { helper } from './utils.js';
```

### 命名空间导入

```js
import * as Math from './math.js';

console.log(Math.add(1, 2));
console.log(Math.PI);
```

## 动态导入 import()

- 返回 Promise，可在运行时按需加载。
- 适用于代码分割、懒加载、基于路由或交互的加载场景。

```js
async function loadModule() {
  const module = await import('./module.js');
  module.doSomething();
}
```

## 顶层 await

ES2022 支持顶层 await，可在模块顶层直接使用：

```js
// data.js (ESM)
const data = await fetch('https://example.com/data').then(r => r.json());
export { data };
```

注意：顶层 await 会让该模块的依赖方也变为异步，需评估加载顺序影响。

## 浏览器中使用 ESM

### 内联模块

```html
<script type="module">
  import { add } from './math.js';
  console.log(add(1, 2));
</script>
```

### 外部模块

```html
<script type="module" src="./main.js"></script>
```

### 模块特性

- `type="module"` 脚本默认延迟执行（defer）。
- 模块有独立作用域，`this` 为 `undefined`。
- 跨域模块需正确的 CORS 头。

## Node.js 中使用 ESM

### 启用方式

1) 在 `package.json` 中声明：
```json
{
  "type": "module"
}
```
2) 或使用 `.mjs` 扩展名。

### 导入本地文件

必须带扩展名或可解析的路径：
```js
import { add } from './math.js'; // 需写 .js
```

### __dirname/__filename 替代

ESM 中没有 `__dirname`/`__filename`，可用：
```js
import { fileURLToPath } from 'url';
import { dirname } from 'path';
const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
```

## 与 CommonJS 的互操作

### 在 ESM 中导入 CJS

```js
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const cjs = require('./cjs-module.cjs');
```

### 在 CJS 中导入 ESM

```js
async function loadESM() {
  const esm = await import('./esm-module.mjs');
  console.log(esm.default);
}
loadESM();
```

### 互操作注意点

- ESM 默认导入 CJS 获得 `module.exports`。
- CJS `require` ESM 需使用动态 `import()`，因为 ESM 是异步。
- 尽量避免混用；新项目优先 ESM，旧项目逐步迁移。

## ESM 相较 CJS 的优势

| 维度         | ESM                              | CJS                         |
| :----------- | :------------------------------- | :-------------------------- |
| 导入导出     | import / export                  | require / module.exports    |
| 分析优化     | 静态分析友好，Tree Shaking 佳    | 动态，Tree Shaking 困难     |
| 加载方式     | 可异步，原生浏览器支持           | 同步，主要在 Node           |
| 互操作       | 可桥接 CJS                       | 可桥接 ESM（需动态 import） |
| this         | 顶层 this 为 undefined           | 顶层 this 指向 exports      |

## 常见陷阱与排查

- **缺少文件扩展名**：Node ESM 导入必须写扩展名或使用解析方案。
- **顶层 await 导致阻塞**：评估依赖链，避免在核心入口滥用。
- **混用 CJS/ESM**：路径、默认导出行为可能不同，需明确格式。
- **相对路径与 URL**：ESM `import` 接受 URL 语义，注意大小写与路径。

## 打包与 Tree Shaking 关系

- ESM 的静态结构使打包器能进行 Tree Shaking、Scope Hoisting。
- 避免在 ESM 中使用动态导入路径（字符串拼接）以免失去静态分析。
- 在库中声明 `sideEffects`，配合 ESM 导出，提升摇树效果。

## 示例：基于动态导入的代码分割

```js
// router.js
const routes = {
  home: () => import('./pages/home.js'),
  about: () => import('./pages/about.js')
};

export async function loadPage(name) {
  if (!routes[name]) throw new Error('Page not found');
  const page = await routes[name]();
  return page.render();
}
```

## 练习

1. 编写一个包含命名导出与默认导出的模块，并在主文件中以多种方式导入。
2. 在浏览器使用 `<script type=\"module\">`，演示模块作用域与延迟执行。
3. 在 Node.js 中创建 `type: module` 项目，演示顶层 await 与 `fileURLToPath` 获取路径。
4. 编写一个动态导入示例，实现按路由懒加载。
5. 将一个 CommonJS 模块改写为 ESM，并验证互操作方式。

## 总结

ES Modules 是现代 JavaScript 的标准模块系统，具备静态、可分析、可优化的特性。掌握导入导出、动态导入、顶层 await、与 CommonJS 的互操作以及在浏览器/Node 的差异，是迈向高质量工程化项目的必备能力。

## 相关资源

- [MDN ES Modules 文档](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Modules)
- [ES Modules 规范](https://tc39.es/ecma262/#sec-modules)
