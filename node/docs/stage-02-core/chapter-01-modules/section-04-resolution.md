# 2.1.4 模块解析与加载

## 1. 概述

模块解析是 Node.js 确定模块文件位置的过程。理解模块解析机制对于正确导入模块、排查模块加载错误以及优化模块查找性能至关重要。Node.js 支持多种模块解析策略，包括 CommonJS 和 ESM 的不同解析规则。

## 2. 特性说明

- **多种解析策略**：支持 CommonJS 和 ESM 两种不同的解析策略。
- **路径优先级**：按照特定顺序查找模块，确保找到正确的模块。
- **扩展名处理**：CommonJS 和 ESM 对文件扩展名的处理不同。
- **包解析**：支持从 `node_modules` 目录解析第三方包。
- **路径映射**：支持通过 `package.json` 的 `exports` 字段自定义模块解析。

## 3. 模块解析策略

### CommonJS 解析策略

CommonJS 模块解析遵循以下顺序：

| 解析类型     | 查找顺序                                     | 示例                           |
|:-------------|:---------------------------------------------|:-------------------------------|
| **核心模块** | 直接查找内置模块                              | `require('fs')`               |
| **相对路径** | 相对于当前文件的路径                          | `require('./utils')`           |
| **绝对路径** | 从根目录开始的绝对路径                        | `require('/path/to/module')`   |
| **node_modules**| 从当前目录向上查找 `node_modules`          | `require('express')`           |

### ESM 解析策略

ESM 模块解析遵循以下顺序：

| 解析类型     | 查找顺序                                     | 示例                           |
|:-------------|:---------------------------------------------|:-------------------------------|
| **核心模块** | 使用 `node:` 前缀查找内置模块                | `import fs from 'node:fs'`     |
| **相对路径** | 必须包含文件扩展名                            | `import utils from './utils.js'`|
| **绝对路径** | 使用 `file://` 协议或绝对路径                | `import config from 'file:///path/to/config.js'`|
| **node_modules**| 从当前目录向上查找 `node_modules`          | `import express from 'express'`|

## 4. 路径解析详解

### CommonJS 路径解析

```ts
// 文件: main.cjs
// 功能: CommonJS 路径解析示例

// 1. 核心模块（无需路径）
const fs = require('node:fs');

// 2. 相对路径（自动查找扩展名）
const utils = require('./utils'); // 查找 utils.js, utils.cjs, utils.json 等

// 3. 绝对路径
const config = require('/absolute/path/to/config');

// 4. node_modules
const express = require('express'); // 从 node_modules 查找
```

### ESM 路径解析

```ts
// 文件: main.ts
// 功能: ESM 路径解析示例

// 1. 核心模块（使用 node: 前缀）
import fs from 'node:fs';

// 2. 相对路径（必须包含扩展名）
import utils from './utils.js'; // 必须明确指定 .js

// 3. 绝对路径（使用 file:// 协议）
import config from 'file:///absolute/path/to/config.js';

// 4. node_modules
import express from 'express'; // 从 node_modules 查找
```

## 5. 参数说明：模块标识符

模块标识符是传递给 `require()` 或 `import` 的字符串：

| 标识符类型   | 格式                           | 说明                                     |
|:-------------|:-------------------------------|:-----------------------------------------|
| **核心模块** | `'node:fs'` 或 `'fs'`          | Node.js 内置模块。                       |
| **相对路径** | `'./utils.js'` 或 `'../config.js'`| 相对于当前文件的路径。                 |
| **绝对路径** | `'/path/to/module.js'`         | 从根目录开始的绝对路径。                 |
| **包名**     | `'express'`                    | 从 `node_modules` 查找的包名。           |
| **包子路径** | `'express/router'`             | 包的子模块路径。                         |

## 6. 返回值与状态说明

模块解析的结果：

| 结果类型     | 说明                                     | 示例                           |
|:-------------|:-----------------------------------------|:-------------------------------|
| **成功**     | 找到模块文件，返回模块导出                | `{ add, subtract }`            |
| **失败**     | 抛出 `MODULE_NOT_FOUND` 错误              | `Error: Cannot find module`    |
| **循环依赖** | 返回部分初始化的模块（CommonJS）          | `{ add: undefined }`          |

## 7. 代码示例：模块解析优先级

以下示例演示了模块解析的优先级：

```ts
// 文件结构：
// project/
//   ├── node_modules/
//   │   └── utils/
//   │       └── index.js
//   ├── utils.js
//   └── main.ts

// 文件: main.ts
// 功能: 模块解析优先级演示

// 1. 相对路径优先于 node_modules
import localUtils from './utils.js'; // 使用 ./utils.js

// 2. node_modules 查找
import packageUtils from 'utils'; // 使用 node_modules/utils

// 3. 核心模块
import fs from 'node:fs'; // 使用内置 fs 模块
```

## 8. 输出结果说明

模块解析会按照优先级查找模块：

1. **相对路径**：首先查找相对路径的模块
2. **node_modules**：如果相对路径不存在，查找 `node_modules`
3. **核心模块**：最后查找核心模块

## 9. 使用场景

### 1. 本地模块组织

使用相对路径组织本地模块：

```ts
// 项目结构
// src/
//   ├── utils/
//   │   ├── math.ts
//   │   └── string.ts
//   └── main.ts

// main.ts
import { add } from './utils/math.js';
import { capitalize } from './utils/string.js';
```

### 2. 第三方包使用

从 `node_modules` 导入第三方包：

```ts
import express from 'express';
import { z } from 'zod';
import type { User } from '@prisma/client';
```

### 3. 条件导入

根据条件动态导入模块：

```ts
// 动态导入实现条件加载
if (process.env.NODE_ENV === 'production') {
    const prodConfig = await import('./config.prod.js');
} else {
    const devConfig = await import('./config.dev.js');
}
```

## 10. 注意事项与常见错误

- **文件扩展名**：ESM 必须包含文件扩展名，CommonJS 可以省略
- **路径格式**：ESM 相对路径必须以 `./` 或 `../` 开头
- **node: 前缀**：推荐使用 `node:` 前缀导入核心模块
- **循环依赖**：避免循环依赖，可能导致未定义的行为
- **路径解析性能**：深层嵌套的 `node_modules` 查找可能影响性能

## 11. 常见问题 (FAQ)

**Q: 为什么 ESM 导入本地文件要写 `.js` 扩展名？**
A: 这是 ESM 规范的要求，确保模块路径的明确性。TypeScript 编译器会正确处理 `.ts` 到 `.js` 的映射。

**Q: CommonJS 和 ESM 的模块解析有什么区别？**
A: 主要区别在于文件扩展名的处理。CommonJS 会自动查找扩展名，ESM 必须明确指定。

**Q: 如何自定义模块解析？**
A: 可以通过 `package.json` 的 `exports` 字段自定义模块解析，或使用 TypeScript 的 `paths` 配置。

## 12. 最佳实践

- **明确路径**：使用明确的相对路径或绝对路径
- **使用 node: 前缀**：导入核心模块时使用 `node:` 前缀
- **文件扩展名**：ESM 中明确指定文件扩展名
- **避免深层嵌套**：避免过深的目录结构，影响模块查找性能
- **路径映射**：使用 `package.json` 的 `exports` 字段优化模块解析

## 13. 对比分析：CommonJS vs ESM 解析

| 维度             | CommonJS                                    | ES Modules                                  |
|:-----------------|:--------------------------------------------|:--------------------------------------------|
| **扩展名处理**   | 自动查找 `.js`, `.json`, `.node` 等         | 必须明确指定扩展名                          |
| **相对路径**     | 可以省略 `./`                               | 必须包含 `./` 或 `../`                      |
| **核心模块**     | 可以使用 `fs` 或 `node:fs`                  | 推荐使用 `node:fs`                          |
| **路径解析**     | 运行时解析                                  | 编译时解析                                  |
| **性能**         | 运行时查找，可能较慢                        | 编译时确定，性能更好                        |

## 14. 练习任务

1. **路径解析实验**：
   - 创建不同位置的模块文件
   - 尝试不同的导入路径
   - 观察模块解析的行为

2. **优先级实验**：
   - 创建同名的本地模块和 node_modules 模块
   - 测试模块解析的优先级
   - 理解解析顺序

3. **扩展名实验**：
   - 在 CommonJS 和 ESM 中测试不同的扩展名
   - 观察扩展名处理的行为
   - 理解扩展名的重要性

4. **路径映射实践**：
   - 使用 `package.json` 的 `exports` 字段
   - 配置自定义模块路径
   - 理解路径映射的作用

5. **实际应用**：
   - 在实际项目中组织模块结构
   - 优化模块解析性能
   - 掌握模块解析的最佳实践

完成以上练习后，继续学习下一章：文件系统（fs）。

## 总结

模块解析是 Node.js 模块系统的重要组成部分：

- **解析策略**：CommonJS 和 ESM 有不同的解析策略
- **路径优先级**：按照特定顺序查找模块
- **扩展名处理**：两种模块系统对扩展名的处理不同
- **最佳实践**：明确路径、使用 node: 前缀、优化解析性能

理解模块解析机制有助于正确使用模块系统和排查模块加载问题。

---

**最后更新**：2025-01-XX
