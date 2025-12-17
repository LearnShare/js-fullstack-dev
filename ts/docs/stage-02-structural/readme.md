# 阶段二：结构化类型系统（核心）

本阶段帮助已掌握 TypeScript 基础类型的开发者深入学习结构化类型系统，包括接口、类型别名和函数类型，这是 TypeScript 类型系统的核心内容。

## 前置知识要求

在开始本阶段学习之前，请确保你已经：

### 必须掌握

- **阶段一内容**：TypeScript 安装与配置、基础类型系统
- **基础类型**：string、number、boolean、array、tuple、enum 等
- **类型注解**：类型推断和类型注解的使用
- **类型断言**：类型断言的基本用法

### 不需要掌握

以下知识**不需要**提前掌握，会在学习过程中逐步学习：

- 接口的高级特性（本阶段会教授）
- 类型别名的复杂用法（本阶段会教授）
- 函数类型的复杂场景（本阶段会教授）

### 如何检查

完成以下检查点，确认可以开始本阶段：

1. **基础类型掌握**
   - [ ] 理解原始类型（string、number、boolean）的使用
   - [ ] 理解数组和元组类型的区别
   - [ ] 理解枚举类型的使用
   - [ ] 理解特殊类型（any、unknown、void、never）的使用场景

2. **类型系统基础**
   - [ ] 能够使用类型注解
   - [ ] 理解类型推断的工作原理
   - [ ] 能够使用类型断言
   - [ ] 理解类型检查的作用

**如果以上检查点都通过，可以开始阶段二的学习。**

**如果某些检查点未通过，建议：**
- 复习阶段一的基础类型系统内容
- 练习类型注解和类型推断的使用
- 理解类型系统的基本概念

## 学习时间估算

**建议学习时间：** 2-3 周

- 每天学习 2-3 小时
- 每周学习 5-6 天
- 包含实践练习和巩固时间

**时间分配建议：**
- 接口（2.1）：4-5 天
- 类型别名（2.2）：3-4 天
- 函数类型（2.3）：3-4 天
- 实践练习和巩固：2-3 天

## 练习建议

### 基础练习（每章完成后）

1. **接口实践**
   - 定义和使用接口
   - 实现接口的可选属性和只读属性
   - 使用接口继承和合并

2. **类型别名实践**
   - 创建和使用类型别名
   - 使用联合类型和交叉类型
   - 理解字面量类型

3. **函数类型实践**
   - 定义函数类型
   - 使用可选参数和默认参数
   - 理解函数重载

### 综合练习（阶段完成后）

4. **类型系统应用**
   - 为实际项目定义接口和类型
   - 使用类型系统构建类型安全的代码
   - 理解结构化类型系统的工作原理

## 章节内容

1. **[接口（Interface）](chapter-01-interfaces/README.md)**：学习 TypeScript 接口的定义、使用、继承和合并。
   - [2.1.1 接口概述](chapter-01-interfaces/section-01-overview.md)
   - [2.1.2 接口基础](chapter-01-interfaces/section-02-basics.md)
   - [2.1.3 可选属性与只读属性](chapter-01-interfaces/section-03-optional-readonly.md)
   - [2.1.4 函数类型与索引签名](chapter-01-interfaces/section-04-function-index.md)
   - [2.1.5 接口继承与合并](chapter-01-interfaces/section-05-inheritance-merge.md)

2. **[类型别名（Type Alias）](chapter-02-type-aliases/README.md)**：学习类型别名的定义、联合类型、交叉类型和字面量类型。
   - [2.2.1 类型别名概述](chapter-02-type-aliases/section-01-overview.md)
   - [2.2.2 类型别名基础](chapter-02-type-aliases/section-02-basics.md)
   - [2.2.3 联合类型与交叉类型](chapter-02-type-aliases/section-03-union-intersection.md)
   - [2.2.4 字面量类型](chapter-02-type-aliases/section-04-literal-types.md)
   - [2.2.5 Interface vs Type](chapter-02-type-aliases/section-05-interface-vs-type.md)

3. **[函数类型](chapter-03-functions/README.md)**：学习函数类型的定义、可选参数、默认参数、剩余参数和函数重载。
   - [2.3.1 函数类型概述](chapter-03-functions/section-01-overview.md)
   - [2.3.2 函数类型定义](chapter-03-functions/section-02-definitions.md)
   - [2.3.3 可选参数与默认参数](chapter-03-functions/section-03-optional-default.md)
   - [2.3.4 剩余参数与函数重载](chapter-03-functions/section-04-rest-overloads.md)
   - [2.3.5 函数签名类型](chapter-03-functions/section-05-signatures.md)

完成本阶段后，你将具备：

- 能够定义和使用接口，理解接口的作用和优势
- 掌握类型别名的使用，理解联合类型和交叉类型
- 理解函数类型的定义和使用
- 能够使用结构化类型系统构建类型安全的代码
- 明确接口和类型别名的区别和使用场景
