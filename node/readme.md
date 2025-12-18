# Node.js 全栈开发指南 (TypeScript First)

**适用对象**：已掌握 JavaScript 和 TypeScript 基础，希望从零开始掌握 Node.js 全栈开发的开发者。  
**目标**：从 Node.js 运行时架构出发，掌握后端开发、数据库操作、API 设计、安全、性能优化和部署，最终具备独立设计与开发企业级全栈应用的能力。  
**版本**：2025 版  
**适用 Node.js 版本**：Node.js 22+  
**代码语言**：TypeScript (NodeNext)

---

## 文档说明

本指南采用分阶段、分章节的结构，每个阶段和章节都是独立的文档文件。所有内容面向已掌握 JavaScript/TypeScript 基础的开发者，提供深度原理分析、API 全解析、参数表格、完整示例代码和练习任务。

### 编写规范与要求

- **完全使用 ESM 与 TypeScript**：所有代码示例必须完全基于 ES Modules (ESM) 和 TypeScript (NodeNext) 编写。
- **内容关联与引用**：参考 `js/` 和 `ts/` 目录中已有的内容，避免重复解释基础概念。
- **标准化格式**：遵循严格的 Markdown 语法，包括标题空行、表格物理对齐、标准列表符号等。
- **内容完整性**：每个章节应包含概述、特性、语法、参数、返回值、示例、输出、注意、FAQ、实践、对比、练习。

---

## 目录结构

### 阶段一：Node.js 运行时与架构（基础）

- [阶段一总览](docs/stage-01-foundation/readme.md)
- [1.1 Node.js 发展史](docs/stage-01-foundation/chapter-01-history/readme.md)
  - [1.1.1 Node.js 起源与技术背景](docs/stage-01-foundation/chapter-01-history/section-01-history.md)
  - [1.1.2 Node.js 版本发布策略与演进逻辑](docs/stage-01-foundation/chapter-01-history/section-02-version-evolution.md)
  - [1.1.3 Node.js 生态组成与技术定位分析](docs/stage-01-foundation/chapter-01-history/section-03-ecosystem.md)
- [1.2 Node.js 运行时架构](docs/stage-01-foundation/chapter-02-runtime/readme.md)
  - [1.2.1 Node.js 运行时架构概述](docs/stage-01-foundation/chapter-02-runtime/section-01-overview.md)
  - [1.2.2 V8 引擎工作流水线与内存逻辑](docs/stage-01-foundation/chapter-02-runtime/section-02-v8.md)
  - [1.2.3 Libuv 异步调度与事件循环](docs/stage-01-foundation/chapter-02-runtime/section-03-libuv.md)
  - [1.2.4 单线程非阻塞模型与任务调度](docs/stage-01-foundation/chapter-02-runtime/section-04-event-driven.md)
  - [1.2.5 Worker Threads 并行计算机制](docs/stage-01-foundation/chapter-02-runtime/section-05-worker-threads.md)
- [1.3 Node.js 安装与版本管理](docs/stage-01-foundation/chapter-03-installation/readme.md)
  - [1.3.1 Node.js 物理安装逻辑](docs/stage-01-foundation/chapter-03-installation/section-01-installation.md)
  - [1.3.2 版本管理器 (nvm/fnm) 工作原理](docs/stage-01-foundation/chapter-03-installation/section-02-version-managers.md)
  - [1.3.3 环境逻辑验证与 CLI 基础](docs/stage-01-foundation/chapter-03-installation/section-03-verification.md)
- [1.4 TypeScript 项目初始化](docs/stage-01-foundation/chapter-04-typescript-setup/readme.md)
  - [1.4.1 ESM 架构下的 TS 项目初始化](docs/stage-01-foundation/chapter-04-typescript-setup/section-01-init.md)
  - [1.4.2 tsconfig.json 与 NodeNext 解析逻辑](docs/stage-01-foundation/chapter-04-typescript-setup/section-02-tsconfig.md)
  - [1.4.3 运行时工具 (tsx/ts-node) 机制对比](docs/stage-01-foundation/chapter-04-typescript-setup/section-03-ts-node-tsx.md)
  - [1.4.4 生产环境构建与运行](docs/stage-01-foundation/chapter-04-typescript-setup/section-04-build-run.md)

### 阶段二：核心模块与基础 API（核心能力）

- [阶段二总览](docs/stage-02-core/readme.md)
- [2.1 模块系统](docs/stage-02-core/chapter-01-modules/readme.md)
- [2.2 文件系统 (fs)](docs/stage-02-core/chapter-02-fs/readme.md)
- [2.3 路径处理 (path)](docs/stage-02-core/chapter-03-path/readme.md)
- [2.4 网络编程 (http)](docs/stage-02-core/chapter-04-http/readme.md)
- [2.5 事件驱动 (events)](docs/stage-02-core/chapter-05-events/readme.md)
- [2.6 二进制与流 (Buffer & Stream)](docs/stage-02-core/chapter-06-buffer-stream/readme.md)

### 阶段三：包管理与工程化（工具链）

### 阶段四：Web 框架与 API 开发

### 阶段五：数据持久化与数据库

---

## 学习路径建议

- **基础阶段**：完成阶段一、二，掌握 Node.js 运行机制与核心 API。
- **工程阶段**：完成阶段三、四、五，具备构建企业级后端应用的能力。
- **专家阶段**：攻克阶段六至阶段十，掌握安全、性能、架构与前沿技术。

---

## 版本信息

- **版本**：2025.12
- **最后更新**：2025-12-18
