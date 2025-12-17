# 阶段三：面向对象与类（OOP）

本阶段帮助已掌握 TypeScript 结构化类型系统的开发者深入学习面向对象编程，包括类的基础、继承与多态、现代类特性等，这是 TypeScript 面向对象编程的核心内容。

## 前置知识要求

在开始本阶段学习之前，请确保你已经：

### 必须掌握

- **阶段一内容**：TypeScript 安装与配置、基础类型系统
- **阶段二内容**：接口、类型别名、函数类型
- **JavaScript 基础**：对象、函数、this 关键字的基本概念
- **ES6 Class**：JavaScript ES6 类语法的基本使用

### 不需要掌握

以下知识**不需要**提前掌握，会在学习过程中逐步学习：

- TypeScript 类的高级特性（本阶段会教授）
- 装饰器的使用（本阶段会教授）
- 抽象类和接口实现（本阶段会教授）

### 如何检查

完成以下检查点，确认可以开始本阶段：

1. **类型系统掌握**
   - [ ] 理解接口的定义和使用
   - [ ] 理解类型别名的定义和使用
   - [ ] 理解函数类型的定义和使用
   - [ ] 能够使用接口和类型别名定义类型

2. **JavaScript 基础**
   - [ ] 理解 JavaScript 对象的基本概念
   - [ ] 理解 this 关键字的基本行为
   - [ ] 熟悉 ES6 Class 语法
   - [ ] 理解继承的基本概念

**如果以上检查点都通过，可以开始阶段三的学习。**

**如果某些检查点未通过，建议：**
- 复习阶段二的接口和类型别名内容
- 熟悉 JavaScript ES6 Class 语法
- 理解面向对象编程的基本概念

## 学习时间估算

**建议学习时间**：2-3 周

- 每天学习 2-3 小时
- 每周学习 5-6 天
- 包含实践练习和巩固时间

**时间分配建议：**
- 类的基础（3.1）：3-4 天
- 继承与多态（3.2）：3-4 天
- 现代类特性（3.3）：4-5 天
- 实践练习和巩固：2-3 天

## 练习建议

### 基础练习（每章完成后）

1. **类的基础实践**
   - 定义和使用类
   - 使用访问修饰符
   - 使用只读属性和静态成员

2. **继承实践**
   - 实现类继承
   - 使用 super 关键字
   - 实现接口

3. **现代特性实践**
   - 使用参数属性
   - 使用私有字段
   - 使用装饰器

### 综合练习（阶段完成后）

4. **面向对象应用**
   - 设计类层次结构
   - 实现多态
   - 使用装饰器增强类功能

## 章节内容

1. **[类的基础](chapter-01-classes/README.md)**：学习 TypeScript 类的基础，包括类声明、构造函数、访问修饰符、只读属性和静态成员。
   - [3.1.1 类的基础概述](chapter-01-classes/section-01-overview.md)
   - [3.1.2 类声明与实例化](chapter-01-classes/section-02-declarations.md)
   - [3.1.3 构造函数](chapter-01-classes/section-03-constructors.md)
   - [3.1.4 访问修饰符（public、private、protected）](chapter-01-classes/section-04-modifiers.md)
   - [3.1.5 只读属性与静态成员](chapter-01-classes/section-05-readonly-static.md)

2. **[继承与多态](chapter-02-inheritance/README.md)**：学习 TypeScript 类的继承、多态、抽象类和接口实现。
   - [3.2.1 继承与多态概述](chapter-02-inheritance/section-01-overview.md)
   - [3.2.2 类继承（extends）](chapter-02-inheritance/section-02-extends.md)
   - [3.2.3 super 关键字](chapter-02-inheritance/section-03-super.md)
   - [3.2.4 抽象类与抽象方法](chapter-02-inheritance/section-04-abstract.md)
   - [3.2.5 接口实现（implements）](chapter-02-inheritance/section-05-implements.md)

3. **[现代类特性](chapter-03-modern/README.md)**：学习 TypeScript 的现代类特性，包括参数属性、私有字段、装饰器等。
   - [3.3.1 现代类特性概述](chapter-03-modern/section-01-overview.md)
   - [3.3.2 参数属性（Parameter Properties）](chapter-03-modern/section-02-parameter-properties.md)
   - [3.3.3 私有字段（Private Fields）](chapter-03-modern/section-03-private-fields.md)
   - [3.3.4 装饰器（Decorators）](chapter-03-modern/section-04-decorators.md)
   - [3.3.5 装饰器深入](chapter-03-modern/section-04-decorators-advanced.md)
   - [3.3.6 装饰器元数据](chapter-03-modern/section-05-decorator-metadata.md)
   - [3.3.7 自定义装饰器](chapter-03-modern/section-06-custom-decorators.md)
   - [3.3.8 装饰器组合](chapter-03-modern/section-07-decorator-composition.md)

完成本阶段后，你将具备：

- 能够定义和使用 TypeScript 类
- 理解访问修饰符的作用和使用
- 掌握类继承和多态的实现
- 理解抽象类和接口实现
- 掌握现代类特性，包括参数属性、私有字段、装饰器等
- 能够使用面向对象编程构建类型安全的代码
