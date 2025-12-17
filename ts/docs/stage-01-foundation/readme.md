# 阶段一：环境、配置与基础类型（入门）

本阶段帮助已掌握 JavaScript 基础的开发者搭建 TypeScript 开发环境，学习 TypeScript 的基础配置和类型系统，为后续深入学习打下坚实基础。

## 前置知识要求

在开始本阶段学习之前，请确保你已经：

### 必须掌握

- **JavaScript 基础**：变量、函数、对象、数组等基本概念
- **ES6+ 特性**：箭头函数、解构赋值、模板字符串、Promise、async/await 等
- **计算机基础**：文件管理、命令行使用、操作系统基本操作

### 不需要掌握

以下知识**不需要**提前掌握，会在学习过程中逐步学习：

- TypeScript 语言（从零开始学习）
- 类型系统概念（本指南会教授）
- 高级类型特性（后续阶段学习）

### 如何检查

完成以下检查点，确认可以开始本阶段：

1. **JavaScript 基础检查**
   - [ ] 能够编写基本的 JavaScript 代码
   - [ ] 理解变量、函数、对象、数组的使用
   - [ ] 熟悉 ES6+ 语法特性
   - [ ] 能够使用 Node.js 运行 JavaScript 文件

2. **学习准备**
   - [ ] 准备一台电脑（Windows/macOS/Linux 均可）
   - [ ] 已安装 Node.js（建议 v18+）
   - [ ] 准备稳定的网络连接
   - [ ] 准备学习时间（每天至少 1-2 小时）

**如果以上检查点都通过，可以开始阶段一的学习。**

**如果某些检查点未通过，建议：**
- 先完成 JavaScript 基础学习
- 熟悉 ES6+ 特性
- 参考 JavaScript 学习指南

## 学习时间估算

**建议学习时间：** 1-2 周

- 每天学习 2-3 小时
- 每周学习 5-6 天
- 包含环境搭建和实践练习时间

**时间分配建议：**
- TypeScript 发展史（1.0）：0.5-1 天
- TypeScript 安装与配置（1.1）：2-3 天
- 基础类型系统（1.2）：3-4 天
- 实践练习和巩固：1-2 天

## 练习建议

### 基础练习（每章完成后）

1. **环境验证**
   - 安装 TypeScript
   - 创建第一个 TypeScript 文件
   - 编译和运行 TypeScript 代码
   - 配置 tsconfig.json

2. **类型实践**
   - 使用基础类型编写代码
   - 练习类型注解和类型推断
   - 理解类型错误提示

### 综合练习（阶段完成后）

3. **类型系统应用**
   - 将现有 JavaScript 代码迁移到 TypeScript
   - 为函数和变量添加类型注解
   - 理解类型检查的好处

## 章节内容

1. **[TypeScript 发展史](chapter-01-history/README.md)**：TypeScript 的起源、发展历程、版本演进和生态系统。
   - [1.0.1 TypeScript 起源与发展历程](chapter-01-history/section-01-history.md)
   - [1.0.2 TypeScript 版本演进（1.0 - 5.6）](chapter-01-history/section-02-version-evolution.md)
   - [1.0.3 TypeScript 生态系统](chapter-01-history/section-03-ecosystem.md)

2. **[TypeScript 安装与配置](chapter-02-setup/README.md)**：安装 TypeScript、配置 tsconfig.json、了解编译器选项、配置 IDE、使用直接执行工具、掌握编译操作。
   - [1.1.1 TypeScript 安装](chapter-02-setup/section-01-installation.md)
   - [1.1.2 tsconfig.json 详解](chapter-02-setup/section-02-tsconfig.md)
   - [1.1.3 编译器选项](chapter-02-setup/section-03-compiler-options.md)
   - [1.1.4 IDE 配置（VSCode、WebStorm）](chapter-02-setup/section-04-ide-config.md)
   - [1.1.5 TypeScript 直接执行工具](chapter-02-setup/section-05-direct-execution.md)
   - [1.1.6 编译操作与实践](chapter-02-setup/section-06-compilation.md)

3. **[基础类型系统](chapter-03-basic-types/README.md)**：学习 TypeScript 的基础类型系统，包括原始类型、数组、元组、枚举、特殊类型等。
   - [1.2.1 基础类型系统概述](chapter-03-basic-types/section-01-overview.md)
   - [1.2.2 原始类型（string、number、boolean）](chapter-03-basic-types/section-02-primitives.md)
   - [1.2.3 数组与元组](chapter-03-basic-types/section-03-arrays-tuples.md)
   - [1.2.4 枚举类型](chapter-03-basic-types/section-04-enums.md)
   - [1.2.5 特殊类型（any、unknown、void、never）](chapter-03-basic-types/section-05-special-types.md)
   - [1.2.6 类型推断与类型注解](chapter-03-basic-types/section-06-inference.md)
   - [1.2.7 类型断言](chapter-03-basic-types/section-07-type-assertions.md)

完成本阶段后，你将具备：

- 能够理解 TypeScript 的发展历程和特点
- 独立配置 TypeScript 开发环境，包括安装、配置、IDE 设置
- 使用 TypeScript 直接执行工具进行开发
- 掌握 TypeScript 编译操作和配置
- 理解 TypeScript 的基础类型系统，能够使用基础类型编写代码
- 明确类型系统的基本概念，为后续学习打下基础
