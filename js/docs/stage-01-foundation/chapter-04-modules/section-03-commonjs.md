# 1.3.3 CommonJS

## 概述

CommonJS 是 Node.js 早期采用的同步模块系统，使用 `require` 导入、`module.exports`/`exports` 导出。尽管 ES Modules（ESM）已成为标准，CommonJS 仍在 Node.js 生态中大量存在，了解其机制、缓存、解析规则和与 ESM 的互操作是必备技能。

## 基本语法

### 导出

#### module.exports

```js
// math.js
function add(a, b) {
  return a + b;
}

function subtract(a, b) {
  return a - b;
}

module.exports = {
  add,
  subtract
};
```

#### exports 别名

```js
// math.js
exports.add = function(a, b) {
  return a + b;
};

exports.subtract = function(a, b) {
  return a - b;
};

// 注意：exports 是 module.exports 的引用
// 重新赋值 exports = {} 会断开引用，导致导出丢失
```

### 导入

#### require()

```js
// main.js
const math = require('./math.js');

console.log(math.add(1, 2));
console.log(math.subtract(5, 3));
```

#### 解构导入

```js
// main.js
const { add, subtract } = require('./math.js');

console.log(add(1, 2));
```

### 动态 require

```js
// 动态路径（不利于静态分析与 Tree Shaking）
function loadModule(name) {
  return require(`./modules/${name}.js`);
}

const mod = loadModule('math');
```

## 模块解析与查找顺序

CommonJS 的 `require()` 解析流程（简化）：
1. **核心模块**：如 `fs`、`path`，优先返回。
2. **文件或目录**：相对/绝对路径；尝试 `.js`、`.json`、`.node` 扩展名；目录下查找 `package.json` 的 `main` 或 `index.js`。
3. **node_modules**：自下而上查找最近的 `node_modules` 目录。

示例：
```js
const fs = require('fs');              // 核心模块
const util = require('./utils');       // 本地文件
const lib = require('some-lib');       // node_modules
```

## 模块缓存机制

- 首次加载模块会执行并缓存其导出对象，后续 `require` 返回同一实例。
- 缓存键为解析后的绝对路径。
- 修改 `module.exports` 仅影响后续新 require；已获取的引用保持不变。

查看缓存：
```js
console.log(Object.keys(require.cache));
```

清除缓存（谨慎）：
```js
delete require.cache[require.resolve('./math.js')];
```

## module.exports 与 exports 的区别

- `exports` 是 `module.exports` 的引用快捷方式。
- 直接重新赋值 `exports = {}` 会断开引用，导致导出失效。

正确用法：
```js
exports.add = () => {};
// 或
module.exports = { add: () => {} };
```

错误用法：
```js
exports = { add: () => {} }; // 导出丢失
```

## 常用内置变量

- `__filename`：当前模块的绝对路径。
- `__dirname`：当前模块所在目录的绝对路径。
- `module`：当前模块对象。
- `exports`：导出引用。
- `require`：导入函数，具备 `resolve`、`cache` 等属性。

示例：
```js
console.log(__filename);
console.log(__dirname);
```

## CommonJS 与 ESM 互操作

### 在 ESM 中导入 CommonJS

```js
// ESM 文件
import pkg from './cjs-module.cjs';
// 或使用 createRequire
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const cjs = require('./cjs-module.cjs');
```

### 在 CommonJS 中导入 ESM

```js
// CJS 文件
async function loadESM() {
  const esm = await import('./esm-module.mjs');
  console.log(esm.default);
}
loadESM();
```

### 注意事项

- ESM 导入 CJS 时，默认导入拿到的是 `module.exports`。
- CJS require ESM 需要使用动态 `import()`，因为 ESM 是异步加载。

## 与 ES Modules 的主要差异

| 对比点       | CommonJS                      | ES Modules                     |
| :----------- | :---------------------------- | :----------------------------- |
| 语法         | require / module.exports      | import / export                |
| 加载         | 同步                          | 静态、可异步                   |
| 分析与优化   | 难静态分析，Tree Shaking 困难 | 静态分析友好，Tree Shaking 佳  |
| 作用域       | 每个文件为模块作用域          | 每个文件为模块作用域           |
| this         | 顶层 this 指向 exports        | 顶层 this 为 undefined         |
| 互操作       | 需要桥接                      | 原生标准                       |

## 常见陷阱与解决方案

- **循环依赖**：两个模块互相 `require`，可能得到不完整导出。解决：重构为共享的第三模块，或延迟访问导出。
- **重新赋值 exports**：导致导出丢失。解决：使用 `module.exports = ...` 或保持对 exports 的属性赋值。
- **动态 require**：不利于打包与 Tree Shaking。解决：改用静态导入或明确分支 require。
- **路径解析**：省略扩展名可能导致歧义。解决：显式扩展名或使用工具链约定。
- **缓存副作用**：模块有副作用且被缓存，后续 require 不会再执行。解决：将副作用与可复用逻辑分离。

## 实战示例：配置文件加载器

```js
// config-loader.js
const fs = require('fs');
const path = require('path');

function loadConfig(name) {
  const file = path.resolve(__dirname, `${name}.json`);
  if (!fs.existsSync(file)) {
    throw new Error(`Config not found: ${name}`);
  }
  return JSON.parse(fs.readFileSync(file, 'utf-8'));
}

module.exports = { loadConfig };
```

```js
// main.js
const { loadConfig } = require('./config-loader');
const config = loadConfig('app');
console.log(config);
```

## 调试与测试

- 使用 `require.resolve(id)` 查看解析到的绝对路径。
- 配合 `--require` 预加载（如注册 ts-node、dotenv）。
- 测试时可使用 `proxyquire`/`rewiremock` 替换依赖。

## 迁移建议

- 新项目优先使用 ESM；保留 CJS 仅用于兼容旧依赖或 Node 原生需求。
- 库发布时可同时产出 CJS 与 ESM（双入口），在 `package.json` 中使用 `main`/`module`/`exports` 字段声明。
- 渐进迁移：先保证无循环依赖、显式扩展名，逐步将文件改为 ESM。

## 练习

1. 编写一个 CommonJS 模块，导出多个函数，再通过解构导入并调用。
2. 演示循环依赖导致的导出不完整问题，并通过重构消除循环。
3. 使用 `require.resolve` 打印模块解析路径，理解查找顺序。
4. 编写一个同时支持 ESM 导入的 CommonJS 模块，并在 ESM 中调用。
5. 为一个副作用模块声明为单独入口，避免与逻辑模块耦合，观察缓存行为。

## 总结

CommonJS 仍在 Node.js 生态中大量存在，理解其导入导出语法、解析与缓存机制、与 ESM 的互操作以及常见陷阱，能帮助你在维护遗留代码、编写工具脚本或发布兼容包时做出正确决策。
