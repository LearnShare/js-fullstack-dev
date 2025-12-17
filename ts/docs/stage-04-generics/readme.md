# 阶段四：泛型（Generics）

本阶段帮助已掌握 TypeScript 面向对象编程的开发者深入学习泛型，包括泛型基础、泛型约束、泛型实战等，这是 TypeScript 类型系统的核心内容。

## 前置知识要求

在开始本阶段学习之前，请确保你已经：

### 必须掌握

- **阶段一内容**：TypeScript 安装与配置、基础类型系统
- **阶段二内容**：接口、类型别名、函数类型
- **阶段三内容**：类的基础、继承与多态
- **JavaScript 基础**：函数、数组、对象的基本概念

### 不需要掌握

以下知识**不需要**提前掌握，会在学习过程中逐步学习：

- 泛型的高级用法（本阶段会教授）
- 泛型约束（本阶段会教授）
- 泛型实战应用（本阶段会教授）

### 如何检查

完成以下检查点，确认可以开始本阶段：

1. **类型系统掌握**
   - [ ] 理解接口的定义和使用
   - [ ] 理解类型别名的定义和使用
   - [ ] 理解函数类型的定义和使用
   - [ ] 理解类的基础和继承

2. **JavaScript 基础**
   - [ ] 理解函数的基本概念
   - [ ] 理解数组和对象的基本操作
   - [ ] 理解函数参数和返回值

**如果以上检查点都通过，可以开始阶段四的学习。**

**如果某些检查点未通过，建议：**
- 复习阶段二和阶段三的内容
- 熟悉 JavaScript 函数和数组操作
- 理解类型系统的基本概念

## 学习时间估算

**建议学习时间**：2-3 周

- 每天学习 2-3 小时
- 每周学习 5-6 天
- 包含实践练习和巩固时间

**时间分配建议：**
- 泛型基础（4.1）：3-4 天
- 泛型约束（4.2）：3-4 天
- 泛型实战（4.3）：3-4 天
- 实践练习和巩固：2-3 天

## 练习建议

### 基础练习（每章完成后）

1. **泛型基础实践**
   - 定义和使用泛型函数
   - 定义和使用泛型接口
   - 定义和使用泛型类

2. **泛型约束实践**
   - 使用 extends 约束
   - 使用 keyof 操作符
   - 使用条件类型约束

3. **泛型实战实践**
   - API 响应类型封装
   - 工具函数类型化
   - 数据结构类型化

### 综合练习（阶段完成后）

4. **泛型应用**
   - 设计泛型工具函数
   - 实现泛型数据结构
   - 构建类型安全的 API 封装

## 章节内容

1. **[泛型基础](chapter-01-basics/README.md)**：学习 TypeScript 泛型的基础，包括泛型概述、泛型函数、泛型接口、泛型类。
   - [4.1.1 泛型概述](chapter-01-basics/section-01-overview.md)
   - [4.1.2 泛型函数](chapter-01-basics/section-02-functions.md)
   - [4.1.3 泛型接口](chapter-01-basics/section-03-interfaces.md)
   - [4.1.4 泛型类](chapter-01-basics/section-04-classes.md)

2. **[泛型约束](chapter-02-constraints/README.md)**：学习 TypeScript 泛型约束，包括约束概述、extends 约束、keyof 操作符、条件类型约束。
   - [4.2.1 泛型约束概述](chapter-02-constraints/section-01-overview.md)
   - [4.2.2 extends 约束](chapter-02-constraints/section-02-extends.md)
   - [4.2.3 keyof 操作符](chapter-02-constraints/section-03-keyof.md)
   - [4.2.4 条件类型约束](chapter-02-constraints/section-04-conditional.md)

3. **[泛型实战](chapter-03-practice/README.md)**：学习 TypeScript 泛型的实际应用，包括 API 响应类型封装、工具函数类型化、数据结构类型化。
   - [4.3.1 API 响应类型封装](chapter-03-practice/section-01-api-response.md)
   - [4.3.2 工具函数类型化](chapter-03-practice/section-02-utility-functions.md)
   - [4.3.3 数据结构类型化](chapter-03-practice/section-03-data-structures.md)

完成本阶段后，你将具备：

- 能够定义和使用泛型函数、接口和类
- 理解泛型约束的作用和使用
- 掌握 keyof 操作符的使用
- 能够使用泛型构建类型安全的代码
- 能够在实际项目中应用泛型
