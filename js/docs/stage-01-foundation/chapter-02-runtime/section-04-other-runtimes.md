# 1.1.4 其他运行时（Deno、Bun）

## 概述

除了 Node.js，还有一些新兴的 JavaScript 运行时，如 Deno 和 Bun。本节介绍这些现代运行时的特点、安装和使用方法。

## Deno

### Deno 简介

Deno 是由 Node.js 创始人 Ryan Dahl 开发的现代 JavaScript/TypeScript 运行时，旨在解决 Node.js 的一些设计问题。

### 主要特点

#### 1. 安全性

Deno 默认安全，需要显式授予权限。

```js
// 需要 --allow-read 权限
const data = await Deno.readTextFile('file.txt');

// 需要 --allow-net 权限
const response = await fetch('https://api.example.com/data');
```

#### 2. TypeScript 支持

Deno 内置 TypeScript 支持，无需额外配置。

```typescript
// 直接运行 TypeScript 文件
// deno run app.ts

interface User {
    name: string;
    age: number;
}

const user: User = {
    name: "John",
    age: 30
};

console.log(user);
```

#### 3. Web 标准 API

Deno 实现了 Web 标准 API，如 Fetch、WebSocket 等。

```js
// 使用 Fetch API（无需安装）
const response = await fetch('https://api.example.com/data');
const data = await response.json();
```

#### 4. 标准库

Deno 提供了标准库，无需外部依赖。

```js
// 使用标准库
import { serve } from "https://deno.land/std@0.208.0/http/server.ts";

serve((req) => {
    return new Response("Hello, Deno!");
}, { port: 8000 });
```

#### 5. 内置工具

Deno 内置了测试、格式化、linting 等工具。

```bash
# 运行测试
deno test

# 格式化代码
deno fmt

# Linting
deno lint
```

### Deno 安装

#### Windows

```powershell
# 使用 PowerShell
irm https://deno.land/install.ps1 | iex

# 使用 Scoop
scoop install deno

# 使用 Chocolatey
choco install deno
```

#### macOS/Linux

```bash
# 使用安装脚本
curl -fsSL https://deno.land/install.sh | sh

# 使用 Homebrew（macOS）
brew install deno
```

### Deno 基本使用

#### 运行脚本

```bash
# 运行 JavaScript 文件
deno run app.js

# 运行 TypeScript 文件
deno run app.ts

# 带权限运行
deno run --allow-read --allow-net app.ts

# 允许所有权限（不推荐）
deno run -A app.ts
```

#### 权限标志

```bash
# --allow-read：允许读取文件
deno run --allow-read app.ts

# --allow-write：允许写入文件
deno run --allow-write app.ts

# --allow-net：允许网络访问
deno run --allow-net app.ts

# --allow-env：允许访问环境变量
deno run --allow-env app.ts

# --allow-run：允许运行子进程
deno run --allow-run app.ts
```

#### 示例：HTTP 服务器

```typescript
// server.ts
import { serve } from "https://deno.land/std@0.208.0/http/server.ts";

serve((req) => {
    return new Response("Hello, Deno!", {
        headers: { "content-type": "text/plain" }
    });
}, { port: 8000 });

console.log("Server running at http://localhost:8000/");
```

运行：

```bash
deno run --allow-net server.ts
```

### Deno 与 Node.js 的对比

| 特性 | Node.js | Deno |
|------|---------|------|
| **TypeScript 支持** | 需要配置 | 内置支持 |
| **包管理器** | npm/yarn/pnpm | 无（使用 URL 导入） |
| **安全性** | 无限制 | 默认安全，需要权限 |
| **标准库** | 需要安装 | 内置 |
| **工具链** | 需要安装 | 内置（测试、格式化、linting） |
| **Web 标准** | 部分支持 | 完整支持 |
| **Node.js 兼容性** | 原生支持 | 通过兼容层支持 |

## Bun

### Bun 简介

Bun 是一个高性能的 JavaScript 运行时、打包器、测试运行器和包管理器，使用 Zig 和 JavaScriptCore 引擎编写。

### 主要特点

#### 1. 极快的性能

Bun 的启动速度和执行速度都非常快。

```bash
# 启动速度对比（示例）
# Node.js: ~50ms
# Bun: ~5ms
```

#### 2. 内置工具

Bun 内置了包管理器、打包器、测试运行器等工具。

```bash
# 包管理器
bun install

# 打包器
bun build

# 测试运行器
bun test
```

#### 3. TypeScript 支持

Bun 原生支持 TypeScript，无需编译。

```typescript
// 直接运行 TypeScript 文件
// bun run app.ts

interface User {
    name: string;
    age: number;
}

const user: User = {
    name: "John",
    age: 30
};

console.log(user);
```

#### 4. Node.js 兼容性

Bun 兼容 Node.js API 和 npm 包。

```js
// 可以使用 Node.js API
const fs = require('fs');
const data = fs.readFileSync('file.txt', 'utf8');

// 可以使用 npm 包
const express = require('express');
```

#### 5. Web API 支持

Bun 实现了 Web 标准 API。

```js
// 使用 Fetch API
const response = await fetch('https://api.example.com/data');
const data = await response.json();
```

### Bun 安装

#### Windows

```powershell
# 使用 PowerShell
powershell -c "irm bun.sh/install.ps1 | iex"
```

#### macOS/Linux

```bash
# 使用安装脚本
curl -fsSL https://bun.sh/install | bash

# 使用 Homebrew（macOS）
brew install bun
```

### Bun 基本使用

#### 运行脚本

```bash
# 运行 JavaScript 文件
bun run app.js

# 运行 TypeScript 文件
bun run app.ts

# 运行 package.json 中的脚本
bun run start
```

#### 包管理

```bash
# 安装包
bun install package-name

# 安装所有依赖
bun install

# 添加依赖
bun add package-name

# 添加开发依赖
bun add -d package-name

# 移除依赖
bun remove package-name
```

#### 打包

```bash
# 打包为单个文件
bun build ./index.ts --outdir ./dist

# 打包为可执行文件
bun build ./index.ts --compile --outfile ./app
```

#### 测试

```bash
# 运行测试
bun test

# 测试文件示例
// test.test.ts
import { test, expect } from "bun:test";

test("addition", () => {
    expect(1 + 1).toBe(2);
});
```

#### 示例：HTTP 服务器

```typescript
// server.ts
const server = Bun.serve({
    port: 3000,
    fetch(request) {
        return new Response("Hello, Bun!");
    }
});

console.log(`Server running at http://localhost:${server.port}/`);
```

运行：

```bash
bun run server.ts
```

### Bun 与 Node.js 的对比

| 特性 | Node.js | Bun |
|------|---------|-----|
| **引擎** | V8 | JavaScriptCore |
| **启动速度** | 较慢 | 极快 |
| **执行速度** | 快 | 极快 |
| **包管理器** | npm/yarn/pnpm | 内置 |
| **打包器** | 需要 Webpack/Vite 等 | 内置 |
| **测试框架** | 需要 Jest/Vitest 等 | 内置 |
| **TypeScript 支持** | 需要配置 | 原生支持 |
| **Node.js 兼容性** | 原生支持 | 高度兼容 |

## 运行时选择建议

### 选择 Node.js 的场景

- 需要成熟的生态系统
- 需要广泛的第三方包支持
- 团队已有 Node.js 经验
- 需要与现有 Node.js 项目集成
- 企业级项目

### 选择 Deno 的场景

- 需要更好的安全性
- TypeScript 优先的项目
- 需要 Web 标准 API
- 学习和实验新特性
- 需要内置工具链

### 选择 Bun 的场景

- 需要极高性能
- 快速原型开发
- 全栈开发（前后端统一）
- 需要快速启动
- 新项目，无历史包袱

## 总结

Deno 和 Bun 是 Node.js 的现代替代方案，各有特点。Deno 注重安全性和 Web 标准，Bun 注重性能和开发体验。选择合适的运行时取决于项目需求、团队经验和性能要求。

## 相关资源

- [Deno 官方文档](https://deno.land/)
- [Bun 官方文档](https://bun.sh/)
- [Deno vs Node.js 对比](https://deno.land/manual/node)
- [Bun vs Node.js 性能对比](https://bun.sh/docs/runtime/benchmarks)
