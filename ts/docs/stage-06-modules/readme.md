# 阶段六：模块化与声明文件（工程化）

本阶段帮助已掌握 TypeScript 高级类型系统的开发者学习模块化和声明文件，包括模块系统、声明文件、命名空间、类型生成工具等，这是 TypeScript 工程化的核心内容。

## 前置知识要求

在开始本阶段学习之前，请确保你已经：

### 必须掌握

- **阶段一内容**：TypeScript 安装与配置、基础类型系统
- **阶段二内容**：接口、类型别名、函数类型
- **阶段三内容**：类的基础、继承与多态
- **阶段四内容**：泛型基础、泛型约束、泛型实战
- **阶段五内容**：工具类型、条件类型、映射类型、类型守卫

### 不需要掌握

以下知识**不需要**提前掌握，会在学习过程中逐步学习：

- 模块系统的深入使用（本阶段会教授）
- 声明文件的编写（本阶段会教授）
- 命名空间的使用（本阶段会教授）
- 类型生成工具的使用（本阶段会教授）

### 如何检查

完成以下检查点，确认可以开始本阶段：

1. **类型系统掌握**
   - [ ] 理解泛型的使用
   - [ ] 理解工具类型的使用
   - [ ] 理解条件类型和映射类型
   - [ ] 能够编写复杂的类型定义

2. **JavaScript 基础**
   - [ ] 理解 ES Modules 和 CommonJS
   - [ ] 理解模块导入和导出
   - [ ] 理解包管理和依赖

**如果以上检查点都通过，可以开始阶段六的学习。**

**如果某些检查点未通过，建议：**
- 复习阶段四和阶段五的内容
- 熟悉 JavaScript 模块系统
- 理解包管理和依赖的概念

## 学习时间估算

**建议学习时间**：2-3 周

- 每天学习 2-3 小时
- 每周学习 5-6 天
- 包含实践练习和巩固时间

**时间分配建议：**
- 模块系统（6.1）：2-3 天
- 声明文件（6.2）：4-5 天
- 命名空间（6.3）：2 天
- 类型生成工具（6.4）：2-3 天
- 实践练习和巩固：2-3 天

## 练习建议

### 基础练习（每章完成后）

1. **模块系统实践**
   - 使用 ES Modules 和 CommonJS
   - 配置模块解析策略
   - 使用类型导入

2. **声明文件实践**
   - 编写全局声明文件
   - 编写模块声明文件
   - 扩展第三方库类型

3. **命名空间实践**
   - 定义和使用命名空间
   - 命名空间合并

### 综合练习（阶段完成后）

4. **工程化应用**
   - 为项目配置模块系统
   - 编写完整的声明文件
   - 使用类型生成工具

## 章节内容

1. **[模块系统](chapter-01-modules/README.md)**：学习 TypeScript 模块系统，包括 ES Modules、CommonJS、模块解析策略、类型导入。
   - [6.1.1 模块系统概述](chapter-01-modules/section-01-overview.md)
   - [6.1.2 ES Modules 与 TypeScript](chapter-01-modules/section-02-esm.md)
   - [6.1.3 CommonJS 与 TypeScript](chapter-01-modules/section-03-commonjs.md)
   - [6.1.4 模块解析策略](chapter-01-modules/section-04-resolution.md)
   - [6.1.5 类型导入（import type）](chapter-01-modules/section-05-type-imports.md)

2. **[声明文件（.d.ts）](chapter-02-declarations/README.md)**：学习声明文件的编写，包括基础、类型、全局声明、模块声明、命名空间、类型扩展、DefinitelyTyped、自定义声明文件、第三方库处理、最佳实践。
   - [6.2.1 声明文件基础](chapter-02-declarations/section-01-basics.md)
   - [6.2.2 声明文件类型](chapter-02-declarations/section-02-declaration-types.md)
   - [6.2.3 全局声明文件](chapter-02-declarations/section-03-global-declarations.md)
   - [6.2.4 模块声明文件](chapter-02-declarations/section-04-module-declarations.md)
   - [6.2.5 declare module 与 declare global](chapter-02-declarations/section-05-declare-keywords.md)
   - [6.2.6 declare namespace](chapter-02-declarations/section-06-declare-namespace.md)
   - [6.2.7 类型扩展与合并](chapter-02-declarations/section-07-type-extension.md)
   - [6.2.8 DefinitelyTyped (@types/)](chapter-02-declarations/section-08-definitelytyped.md)
   - [6.2.9 编写自定义声明文件](chapter-02-declarations/section-09-custom-declarations.md)
   - [6.2.10 第三方库声明文件处理](chapter-02-declarations/section-10-third-party.md)
   - [6.2.11 声明文件最佳实践](chapter-02-declarations/section-11-best-practices.md)

3. **[命名空间（Namespace）](chapter-03-namespaces/README.md)**：学习命名空间的使用，包括基础、合并、与模块的对比。
   - [6.3.1 命名空间基础](chapter-03-namespaces/section-01-basics.md)
   - [6.3.2 命名空间合并](chapter-03-namespaces/section-02-merging.md)
   - [6.3.3 命名空间 vs 模块](chapter-03-namespaces/section-03-vs-modules.md)

4. **[类型生成工具](chapter-04-type-generation/README.md)**：学习类型生成工具的使用，包括 json-schema-to-typescript、quicktype、从 API 生成类型、openapi-typescript。
   - [6.4.1 json-schema-to-typescript](chapter-04-type-generation/section-01-json-schema.md)
   - [6.4.2 quicktype](chapter-04-type-generation/section-02-quicktype.md)
   - [6.4.3 从 API 生成类型](chapter-04-type-generation/section-03-api-types.md)
   - [6.4.4 openapi-typescript](chapter-04-type-generation/section-04-openapi.md)

完成本阶段后，你将具备：

- 能够配置和使用 TypeScript 模块系统
- 能够编写各种类型的声明文件
- 能够使用命名空间组织代码
- 能够使用类型生成工具生成类型定义
- 能够处理第三方库的类型定义
