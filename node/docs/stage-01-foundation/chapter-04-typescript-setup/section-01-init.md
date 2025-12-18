# 1.4.1 ESM 架构下的 TS 项目初始化

## 1. 概述

在 2025 年的 Node.js 开发环境下，TypeScript 已成为事实上的行业标准。随着 Node.js 22.x 引入了实验性的原生类型剥离（Type Stripping）支持，TypeScript 在 Node.js 中的运行逻辑正从“必须预编译”向“直接运行”演进。然而，对于生产级应用，基于 ES Modules (ESM) 的标准工程化初始化依然是构建健壮后端的首要步骤。本节将详细解析如何在 Node.js 环境下从零构建一个符合现代 ESM 规范的 TypeScript 开发工程。

## 2. 特性说明

- **强类型契约**：在开发阶段通过类型推断与显式标注发现 90% 以上的低级逻辑错误。
- **现代模块化支持**：完全兼容 Node.js 原生的 ES Modules (ESM) 加载规范。
- **工程化基石**：为后续集成 ESLint、Vitest 及自动构建流水线提供标准化基础。
- **自适应解析**：通过最新的 `NodeNext` 模块解析策略，实现对现代包管理生态的完美适配。

## 3. 项目初始化核心步骤

构建一个标准化的 TypeScript 工程涉及以下物理环节与逻辑配置。

| 步骤序号         | 执行动作                               | 逻辑职责说明                                     |
|:-----------------|:---------------------------------------|:-------------------------------------------------|
| **1. 基础初始化**| `npm init -y`                          | 生成 `package.json` 清单，确定项目根域。         |
| **2. 安装编译器**| `npm add -D typescript @types/node`    | 引入 TS 核心引擎及 Node.js 全局类型定义。        |
| **3. 编译器配置**| `npx tsc --init`                       | 生成 `tsconfig.json` 控制中枢。                  |
| **4. 模块模式切换**| `"type": "module"`                     | 在 `package.json` 中声明项目采用 ESM 逻辑。      |

## 4. 参数说明：初始化常用 Flag

在执行初始化指令时，常用的命令行参数及其逻辑作用如下。

| 指令参数         | 类型     | 逻辑说明                                         | 推荐场景                       |
|:-----------------|:---------|:-------------------------------------------------|:-------------------------------|
| `init -y`        | Flag     | 略过交互式问答，直接生成默认配置。               | 快速原型开发。                 |
| `install -D`     | Flag     | 将依赖记录为开发依赖（devDeps），不进入生产构建。| 安装编译器、类型定义库。       |
| `tsc --init`     | N/A      | 创建带有详尽注释说明的配置文件模板。             | 项目初始启动阶段。             |

## 5. 返回值与状态说明：配置文件关键字段

初始化后，`package.json` 中的以下字段决定了项目的运行底座。

| 字段名           | 推荐值   | 逻辑含义                                         |
|:-----------------|:---------|:-------------------------------------------------|
| `"type"`         | `module` | 声明所有 `.js` 文件按 ES Modules 逻辑解析。      |
| `"engines"`      | `>=22.0` | 显式声明项目兼容的最低 Node.js 物理版本。        |
| `"devDependencies"`| Object  | 存放 `typescript` 及 `@types/node` 的版本锚点。  |

## 6. 代码示例：现代项目结构配置

以下代码演示了在 ESM 模式下，如何正确编写一个 TypeScript 入口文件。

```ts
// 文件: src/index.ts
// 功能: 演示在 ESM & TypeScript 环境下的模块导入逻辑

// 注意：在 ESM 模式下，TS 源码中导入本地文件必须显式写 .js 后缀
import { versions } from 'node:process';
import { platform } from 'node:os';

interface SystemReport {
  nodeVer: string;
  osPlatform: string;
}

const report: SystemReport = {
  nodeVer: versions.node,
  osPlatform: platform()
};

console.log(`[INFO] 系统环境初始化成功: ${JSON.stringify(report)}`);
```

## 7. 输出结果说明

```text
[INFO] 系统环境初始化成功: {"nodeVer":"22.12.0","osPlatform":"linux"}
```

**逻辑解析**：
1. `import` 语句使用了 `node:` 前缀，这是现代 Node.js 的最佳实践。
2. 即使我们在 `.ts` 文件中编写代码，V8 运行时通过 `tsx` 或 `tsc` 最终执行时，也会按照 ESM 的路径查找规则进行解析。

## 8. 注意事项与常见错误

- **扩展名陷阱**：在 ESM 项目中，导入本地 `.ts` 文件时必须写成 `import './file.js'`（即使物理文件是 `.ts`）。这是初学者最常犯的错误。
- **类型冲突**：如果全局安装了旧版 TypeScript，建议使用 `npx tsc` 确保调用的是项目局部的最新版本。
- **模块声明缺失**：若未在 `package.json` 中设置 `"type": "module"`，Node.js 会默认使用 CommonJS 解析，导致 `import` 语句报错。

## 9. 常见问题 (FAQ)

**Q: 为什么 TS 源码要写 .js 后缀？这不是反直觉吗？**
A: 这是 TypeScript 团队为了对齐标准 ESM 规范而做出的设计。它确保了编译器不需要通过猜测来修改你的代码路径，从而保持了编译产物与源码的路径一致性。

**Q: Node.js 22.6+ 提供的 --experimental-strip-types 能替代 tsc 吗？**
A: 目前不能。该功能仅支持“剥离”类型，不支持 Enum、Namespace 等需要生成实际 JS 代码的特性，且不支持装饰器。生产环境仍建议使用标准的编译流程。

## 10. 最佳实践

- **严格模式优先**：在初始化后，立即确保 `tsconfig.json` 中的 `strict: true` 为开启状态。
- ** node: 前缀强制化**：所有的内置模块导入都应加上 `node:` 协议头，以区分社区包并提升加载性能。
- **忽略编译产物**：在 `.gitignore` 中加入 `dist/` 或 `out/`，避免将编译后的 JS 文件提交到版本库。

## 11. 对比分析：CommonJS vs ESM 初始化

| 维度             | CommonJS (Legacy)                                | ESM (Modern)                                     |
|:-----------------|:-------------------------------------------------|:-------------------------------------------------|
| **package.json** | 无需设置或设为 `commonjs`。                      | **必须显式设置 `"type": "module"`。**            |
| **导入语法**     | `require()`。                                    | `import` / `export`。                            |
| **路径解析**     | 支持自动寻找 `.js`/`.ts` 扩展名。                | **强制要求完整的文件扩展名。**                   |
| **Top-level await**| 不支持。                                       | **完美支持。**                                   |

## 12. 练习任务

1. **动手初始化**：创建一个名为 `node-ts-esm` 的目录，完成从 `npm init` 到成功运行 `index.ts` 的全部过程。
2. **逻辑冲突实验**：尝试删除 `package.json` 中的 `"type": "module"`，并运行代码，记录并解释报出的 `SyntaxError`。
3. **原生实验**：在 Node.js 22.12+ 环境下，不进行编译，尝试使用 `node --experimental-strip-types index.ts` 运行代码。
