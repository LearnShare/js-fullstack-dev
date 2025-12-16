# 1.1.1 JavaScript 运行环境概述

## 概述

JavaScript 是一种解释型语言，需要在特定的运行环境中执行。本节介绍 JavaScript 运行环境的基本概念、不同环境的类型以及运行时的作用。

## 什么是运行环境

### 定义

运行环境（Runtime Environment）是执行 JavaScript 代码的软件环境，它提供了：

- JavaScript 引擎：解析和执行 JavaScript 代码
- 全局对象和 API：提供语言之外的功能
- 事件循环：处理异步操作
- 内存管理：管理变量和对象的内存

### 运行环境的组成

一个完整的 JavaScript 运行环境通常包括：

1. **JavaScript 引擎**：负责解析和执行 JavaScript 代码
2. **全局对象**：提供全局变量和函数（如 `console`、`setTimeout` 等）
3. **API 集合**：提供特定环境的功能（如 DOM API、Node.js API 等）
4. **事件循环**：处理异步操作和事件

## JavaScript 引擎

### 作用

JavaScript 引擎是运行环境的核心组件，负责：

- 解析 JavaScript 代码
- 将代码编译为机器码或字节码
- 执行编译后的代码
- 优化代码执行性能

### 主要引擎

#### V8 引擎

V8 是 Google 开发的 JavaScript 引擎，用于：

- Chrome 浏览器
- Node.js
- Deno
- 其他基于 Chromium 的浏览器

**特点**：
- 高性能
- JIT（即时编译）优化
- 垃圾回收机制

#### SpiderMonkey

SpiderMonkey 是 Mozilla 开发的 JavaScript 引擎，用于：

- Firefox 浏览器
- 服务器端应用

**特点**：
- 开源
- 持续优化
- 支持 WebAssembly

#### JavaScriptCore（Nitro）

JavaScriptCore 是 Apple 开发的 JavaScript 引擎，用于：

- Safari 浏览器
- WebKit 项目

**特点**：
- 专注于性能优化
- 支持 WebAssembly
- 内存管理优化

#### Chakra

Chakra 是 Microsoft 开发的 JavaScript 引擎，用于：

- 旧版 Edge 浏览器（已弃用，Edge 现在使用 Chromium）

## 运行环境类型

### 浏览器环境

浏览器环境是最常见的 JavaScript 运行环境。

**特点**：
- 内置 JavaScript 引擎
- 提供 DOM API
- 提供 BOM（浏览器对象模型）API
- 提供 Web API（如 Fetch、WebSocket 等）
- 安全限制（同源策略等）

**全局对象**：
- `window`：浏览器窗口对象
- `document`：DOM 文档对象
- `navigator`：浏览器信息对象
- `location`：URL 信息对象

```js
// 浏览器环境示例
console.log(window.innerWidth);   // 窗口宽度
console.log(document.title);       // 页面标题
console.log(navigator.userAgent);  // 用户代理字符串
```

### Node.js 环境

Node.js 是基于 V8 引擎的服务器端 JavaScript 运行环境。

**特点**：
- 基于 V8 引擎
- 提供文件系统、网络等服务器端 API
- 无 DOM 和 BOM
- 支持 CommonJS 和 ES Modules
- 事件驱动、非阻塞 I/O

**全局对象**：
- `global`：全局对象（类似浏览器的 `window`）
- `process`：进程对象
- `Buffer`：二进制数据处理
- `__dirname`：当前目录路径
- `__filename`：当前文件路径

```js
// Node.js 环境示例
console.log(process.version);      // Node.js 版本
console.log(__dirname);            // 当前目录
console.log(__filename);           // 当前文件路径

const fs = require('fs');
fs.readFile('file.txt', 'utf8', (err, data) => {
    if (err) throw err;
    console.log(data);
});
```

### Deno 环境

Deno 是由 Node.js 创始人开发的现代 JavaScript/TypeScript 运行时。

**特点**：
- 基于 V8 引擎
- 内置 TypeScript 支持
- 默认安全（需要显式权限）
- 标准库
- 内置工具（测试、格式化、linting）

**全局对象**：
- `Deno`：Deno 全局对象
- `window`：类似浏览器的全局对象
- 支持 Web 标准 API

```js
// Deno 环境示例
console.log(Deno.version);         // Deno 版本

// 读取文件（需要权限）
const data = await Deno.readTextFile('file.txt');
console.log(data);
```

### Bun 环境

Bun 是一个高性能的 JavaScript 运行时、打包器、测试运行器和包管理器。

**特点**：
- 极快的启动速度
- 内置包管理器
- 内置测试框架
- 内置打包工具
- 原生 TypeScript 支持

**全局对象**：
- `Bun`：Bun 全局对象
- 支持 Node.js 和 Web API

```js
// Bun 环境示例
console.log(Bun.version);          // Bun 版本

// 读取文件
const file = Bun.file('file.txt');
const text = await file.text();
console.log(text);
```

## 运行环境的对比

### 功能对比

| 特性 | 浏览器 | Node.js | Deno | Bun |
|------|--------|---------|------|-----|
| **JavaScript 引擎** | V8/SpiderMonkey/JSC | V8 | V8 | JavaScriptCore |
| **DOM API** | ✅ | ❌ | ❌ | ❌ |
| **文件系统** | ❌ | ✅ | ✅ | ✅ |
| **网络 API** | ✅ | ✅ | ✅ | ✅ |
| **TypeScript 支持** | ❌ | ❌ | ✅ | ✅ |
| **包管理器** | ❌ | npm/yarn/pnpm | ❌ | ✅ |
| **安全模型** | 同源策略 | 无限制 | 权限系统 | 无限制 |

### 使用场景

#### 浏览器环境

- 前端 Web 应用开发
- 浏览器扩展开发
- 交互式网页
- 单页应用（SPA）

#### Node.js 环境

- 服务器端应用开发
- 命令行工具开发
- 构建工具和脚本
- API 服务器

#### Deno 环境

- 现代 Web 应用开发
- 需要安全控制的场景
- TypeScript 优先的项目
- 学习和实验

#### Bun 环境

- 高性能应用
- 快速原型开发
- 全栈开发
- 需要快速启动的场景

## 运行时的作用

### 代码执行

运行时负责执行 JavaScript 代码，包括：

- 解析代码
- 编译代码
- 执行代码
- 管理内存

### API 提供

运行时提供特定环境的 API：

- **浏览器**：DOM、BOM、Web API
- **Node.js**：文件系统、网络、进程管理
- **Deno**：Web 标准 API + Deno 特定 API
- **Bun**：Node.js API + Web API + Bun 特定 API

### 事件处理

运行时提供事件循环机制，处理：

- 异步操作
- 事件回调
- 定时器
- I/O 操作

### 事件循环差异（概览）

- **浏览器**：宏任务（setTimeout、setInterval、script）、微任务（Promise.then、queueMicrotask、MutationObserver）。
- **Node.js**：事件循环阶段（timers、pending、idle/prepare、poll、check、close callbacks）以及微任务队列（Promise、process.nextTick）。与浏览器顺序存在差异，后续异步章节将详细展开。

### 内存与安全

- **内存管理**：各引擎均有 GC；注意避免全局引用、闭包泄漏、未清理的事件监听。
- **安全模型**：浏览器有同源策略与沙箱；Deno 需显式授权；Node/Bun 默认无沙箱，需自行控制权限。

### 常见 API 差异速览

| API/特性         | 浏览器 | Node.js       | Deno           | Bun              |
| :--------------- | :----: | :-----------: | :------------: | :--------------: |
| DOM              |  ✅    | ❌            | ❌             | ❌               |
| fetch            |  ✅    | ✅(18+)       | ✅             | ✅               |
| WebSocket        |  ✅    | ✅            | ✅             | ✅               |
| FileSystem       |  ⚠️(受限) | ✅ fs        | ✅ Deno APIs   | ✅ Bun APIs      |
| Crypto Web API   |  ✅    | ✅(部分/18+)  | ✅             | ✅               |
| top-level await  |  ✅    | ✅ (ESM)      | ✅             | ✅               |
| Worker           |  ✅    | ✅ (worker_threads) | ✅ | ✅ |
| 权限模型         | 同源策略 | 无（自行控制） | 显式权限       | 无（自行控制）   |

（⚠️ 浏览器文件系统 API 受限于安全策略，如 File System Access API 需用户授权且浏览器支持。）

## 选择运行环境

### 前端开发

**推荐**：浏览器环境

- 需要 DOM 操作
- 需要浏览器 API
- 用户交互为主

### 后端开发

**推荐**：Node.js

- 成熟的生态系统
- 丰富的包和工具
- 广泛采用

### 现代项目

**可选**：Deno 或 Bun

- 需要 TypeScript 支持
- 需要更好的安全性（Deno）
- 需要极高性能（Bun）

### 选择检查清单

- 是否需要 DOM/BOM？→ 浏览器。
- 是否需要文件系统、TCP/HTTP 服务？→ Node/Bun/Deno。
- 是否要求默认安全沙箱？→ Deno（权限模式）。
- 是否优先 TypeScript 开箱？→ Deno/Bun。
- 是否依赖庞大 Node 生态？→ Node（或 Bun 的兼容层）。
- 是否关注冷启动和极致性能？→ Bun 可尝试。

## 练习

1. **环境识别**：编写代码识别当前运行环境（浏览器、Node.js、Deno、Bun）。

2. **API 差异**：演示不同运行环境中 API 的差异（如文件系统、DOM、fetch 等）。

3. **环境选择**：根据项目需求选择合适的运行环境，并说明原因。

4. **全局对象**：在不同环境中访问全局对象（window、global、globalThis）。

5. **特性检测**：使用特性检测判断运行环境是否支持特定功能。

完成以上练习后，继续学习下一节，了解浏览器和 V8 引擎。

## 总结

JavaScript 运行环境是执行 JavaScript 代码的基础设施。不同的运行环境提供了不同的 API 和功能，适用于不同的开发场景。理解不同运行环境的特点和差异，有助于选择合适的开发环境，提高开发效率。

## 相关资源

- [V8 引擎文档](https://v8.dev/)
- [Node.js 官方文档](https://nodejs.org/)
- [Deno 官方文档](https://deno.land/)
- [Bun 官方文档](https://bun.sh/)
