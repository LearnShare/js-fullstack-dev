# 阶段一：环境、运行时与工具链总览

本阶段帮助零基础学员搭建现代 JavaScript 开发所需的基础设施，确保在 Windows、macOS、Linux 等环境都能快速获得一致的运行体验。每个章节都提供操作步骤、验证方法与常见陷阱说明。

## 前置知识要求

在开始本阶段学习之前，请确保你已经：

### 必须掌握（根据 readme.md 说明）

- **通用编程概念**：变量、循环、函数的基本概念
- **计算机基础**：文件管理、命令行使用、操作系统基本操作

### 不需要掌握

以下知识**不需要**提前掌握，会在学习过程中逐步学习：

- JavaScript 语言（从零开始学习）
- 浏览器开发经验（本指南会教授）
- Node.js 开发经验（本指南会教授）

### 如何检查

完成以下检查点，确认可以开始本阶段：

1. **基础检查**
   - [ ] 了解变量的基本概念（可以来自任何编程语言）
   - [ ] 了解循环的基本概念（for、while）
   - [ ] 了解函数的基本概念
   - [ ] 能够使用命令行（Windows CMD/PowerShell、macOS Terminal、Linux Shell）

2. **学习准备**
   - [ ] 准备一台电脑（Windows/macOS/Linux 均可）
   - [ ] 准备稳定的网络连接
   - [ ] 准备学习时间（每天至少 1-2 小时）

**如果以上检查点都通过，可以开始阶段一的学习。**

**如果某些检查点未通过，建议：**
- 先学习基本的编程概念
- 学习基本的命令行操作
- 参考全局学习指南了解更多信息

## 学习时间估算

**建议学习时间：** 2-3 周

- 每天学习 2-3 小时
- 每周学习 5-6 天
- 包含环境搭建和验证时间

**时间分配建议：**
- JavaScript 发展史（1.0）：1 天
- JavaScript 运行环境（1.1）：2-3 天
- 开发工具链（1.2）：3-5 天
- 模块化与包管理（1.3）：2-3 天
- 环境验证和练习：2-3 天

## 练习建议

### 基础练习（每章完成后）

1. **环境验证**
   - 编写 Hello World 程序
   - 验证 Node.js 安装
   - 测试包管理器使用

2. **工具使用**
   - 使用 Git 管理代码
   - 使用 IDE 编写代码
   - 配置调试环境

### 综合练习（阶段完成后）

3. **环境搭建**
   - 在另一台电脑上复现环境
   - 编写环境搭建文档
   - 解决环境问题

## 章节内容

1. **[JavaScript 发展史](chapter-01-history/readme.md)**：JavaScript 的起源、发展历程、ECMAScript 标准演进和生态系统。
   - [1.0.1 JavaScript 起源与发展历程](chapter-01-history/section-01-history.md)
   - [1.0.2 ECMAScript 标准演进](chapter-01-history/section-02-ecmascript-evolution.md)
   - [1.0.3 JavaScript 生态系统](chapter-01-history/section-03-ecosystem.md)

2. **[JavaScript 运行环境](chapter-02-runtime/readme.md)**：逐步了解 JavaScript 在不同环境中的运行方式。
   - [1.1.1 JavaScript 运行环境概述](chapter-02-runtime/section-01-overview.md)
   - [1.1.2 浏览器环境与 V8 引擎](chapter-02-runtime/section-02-browser-v8.md)
   - [1.1.3 Node.js 环境](chapter-02-runtime/section-03-nodejs.md)
   - [1.1.4 其他运行时（Deno、Bun）](chapter-02-runtime/section-04-other-runtimes.md)

3. **[开发工具链](chapter-03-toolchain/readme.md)**：配置代码编辑器、包管理器、构建工具、代码质量工具和调试工具。
   - [1.2.1 开发工具链概述](chapter-03-toolchain/section-01-overview.md)
   - [1.2.2 代码编辑器与 IDE 配置](chapter-03-toolchain/section-02-editor-ide.md)
   - [1.2.3 包管理器（npm、pnpm、yarn）](chapter-03-toolchain/section-03-package-managers.md)
   - [1.2.4 构建工具（Vite、Webpack、Turbopack）](chapter-03-toolchain/section-04-build-tools.md)
   - [1.2.5 代码质量工具（ESLint、Prettier）](chapter-03-toolchain/section-05-code-quality.md)
   - [1.2.6 调试工具与技巧](chapter-03-toolchain/section-06-debugging.md)

4. **[模块化与包管理](chapter-04-modules/readme.md)**：学习 ES Modules、CommonJS 和模块打包。
   - [1.3.1 模块化与包管理概述](chapter-04-modules/section-01-overview.md)
   - [1.3.2 ES Modules (ESM)](chapter-04-modules/section-02-esm.md)
   - [1.3.3 CommonJS](chapter-04-modules/section-03-commonjs.md)
   - [1.3.4 模块打包与 Tree Shaking](chapter-04-modules/section-04-bundling.md)

完成本阶段后，你将具备：

- 能够理解 JavaScript 的发展历程和运行环境
- 独立配置开发工具链，包括编辑器、包管理器、构建工具
- 使用模块化开发，理解 ES Modules 和 CommonJS
- 明确工具链配置路径，遇到问题能主动排查并记录结果
