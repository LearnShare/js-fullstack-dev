# TypeScript 架构与类型系统指南

**适用对象**：已掌握上述 JavaScript 内容，希望在大型项目中获得类型安全和开发体验的开发者。  
**目标**：从类型标注开始，掌握接口、泛型、工具类型，最终能够看懂并编写复杂的类型体操，构建健壮的后端/前端架构。  
**版本**：2025 版  
**适用 TypeScript 版本**：TypeScript 5.6+

---

## 文档说明

本指南采用分阶段、分章节的结构，每个阶段和章节都是独立的文档文件，便于学习和查阅。所有内容面向已掌握 JavaScript 基础的开发者设计，提供详细的概念解释、语法说明、参数列表、完整示例代码和练习任务。

---

## 目录结构

### 阶段一：环境、配置与基础类型（入门）

- [阶段一总览](docs/stage-01-foundation/readme.md)
- [1.0 TypeScript 发展史](docs/stage-01-foundation/chapter-01-history/readme.md)
  - [1.0.1 TypeScript 起源与发展历程](docs/stage-01-foundation/chapter-01-history/section-01-history.md)
  - [1.0.2 TypeScript 版本演进（1.0 - 5.6）](docs/stage-01-foundation/chapter-01-history/section-02-version-evolution.md)
  - [1.0.3 TypeScript 生态系统](docs/stage-01-foundation/chapter-01-history/section-03-ecosystem.md)
- [1.1 TypeScript 安装与配置](docs/stage-01-foundation/chapter-02-setup/readme.md)
  - [1.1.1 TypeScript 安装](docs/stage-01-foundation/chapter-02-setup/section-01-installation.md)
  - [1.1.2 tsconfig.json 详解](docs/stage-01-foundation/chapter-02-setup/section-02-tsconfig.md)
  - [1.1.3 编译器选项](docs/stage-01-foundation/chapter-02-setup/section-03-compiler-options.md)
  - [1.1.4 IDE 配置（VSCode、WebStorm）](docs/stage-01-foundation/chapter-02-setup/section-04-ide-config.md)
  - [1.1.5 TypeScript 直接执行工具](docs/stage-01-foundation/chapter-02-setup/section-05-direct-execution.md)
  - [1.1.6 编译操作与实践](docs/stage-01-foundation/chapter-02-setup/section-06-compilation.md)
- [1.2 基础类型系统](docs/stage-01-foundation/chapter-03-basic-types/readme.md)
  - [1.2.1 基础类型系统概述](docs/stage-01-foundation/chapter-03-basic-types/section-01-overview.md)
  - [1.2.2 原始类型（string、number、boolean）](docs/stage-01-foundation/chapter-03-basic-types/section-02-primitives.md)
  - [1.2.3 数组与元组](docs/stage-01-foundation/chapter-03-basic-types/section-03-arrays-tuples.md)
  - [1.2.4 枚举类型](docs/stage-01-foundation/chapter-03-basic-types/section-04-enums.md)
  - [1.2.5 特殊类型（any、unknown、void、never）](docs/stage-01-foundation/chapter-03-basic-types/section-05-special-types.md)
  - [1.2.6 类型推断与类型注解](docs/stage-01-foundation/chapter-03-basic-types/section-06-inference.md)
  - [1.2.7 类型断言](docs/stage-01-foundation/chapter-03-basic-types/section-07-type-assertions.md)
- [1.3 第一个 TypeScript 程序](docs/stage-01-foundation/chapter-04-first-program/readme.md)
  - [1.3.1 第一个 TypeScript 程序实践](docs/stage-01-foundation/chapter-04-first-program/section-01-practice.md)

### 阶段二：结构化类型系统（核心）

- [阶段二总览](docs/stage-02-structural/readme.md)
- [2.1 接口（Interface）](docs/stage-02-structural/chapter-01-interfaces/readme.md)
  - [2.1.1 接口概述](docs/stage-02-structural/chapter-01-interfaces/section-01-overview.md)
  - [2.1.2 接口基础](docs/stage-02-structural/chapter-01-interfaces/section-02-basics.md)
  - [2.1.3 可选属性与只读属性](docs/stage-02-structural/chapter-01-interfaces/section-03-optional-readonly.md)
  - [2.1.4 函数类型与索引签名](docs/stage-02-structural/chapter-01-interfaces/section-04-function-index.md)
  - [2.1.5 接口继承与合并](docs/stage-02-structural/chapter-01-interfaces/section-05-inheritance-merge.md)
- [2.2 类型别名（Type Alias）](docs/stage-02-structural/chapter-02-type-aliases/readme.md)
  - [2.2.1 类型别名概述](docs/stage-02-structural/chapter-02-type-aliases/section-01-overview.md)
  - [2.2.2 类型别名基础](docs/stage-02-structural/chapter-02-type-aliases/section-02-basics.md)
  - [2.2.3 联合类型与交叉类型](docs/stage-02-structural/chapter-02-type-aliases/section-03-union-intersection.md)
  - [2.2.4 字面量类型](docs/stage-02-structural/chapter-02-type-aliases/section-04-literal-types.md)
  - [2.2.5 Interface vs Type](docs/stage-02-structural/chapter-02-type-aliases/section-05-interface-vs-type.md)
- [2.3 函数类型](docs/stage-02-structural/chapter-03-functions/readme.md)
  - [2.3.1 函数类型概述](docs/stage-02-structural/chapter-03-functions/section-01-overview.md)
  - [2.3.2 函数类型定义](docs/stage-02-structural/chapter-03-functions/section-02-definitions.md)
  - [2.3.3 可选参数与默认参数](docs/stage-02-structural/chapter-03-functions/section-03-optional-default.md)
  - [2.3.4 剩余参数与函数重载](docs/stage-02-structural/chapter-03-functions/section-04-rest-overloads.md)
  - [2.3.5 函数签名类型](docs/stage-02-structural/chapter-03-functions/section-05-signatures.md)
- [2.4 类型兼容性基础](docs/stage-02-structural/chapter-04-compatibility/readme.md)
  - [2.4.1 类型兼容性概述](docs/stage-02-structural/chapter-04-compatibility/section-01-overview.md)
  - [2.4.2 结构化类型系统](docs/stage-02-structural/chapter-04-compatibility/section-02-structural-types.md)
  - [2.4.3 类型兼容性规则基础](docs/stage-02-structural/chapter-04-compatibility/section-03-compatibility-rules.md)

### 阶段三：面向对象与类（OOP）

- [阶段三总览](docs/stage-03-oop/readme.md)
- [3.1 类的基础](docs/stage-03-oop/chapter-01-classes/readme.md)
  - [3.1.1 类的基础概述](docs/stage-03-oop/chapter-01-classes/section-01-overview.md)
  - [3.1.2 类声明与实例化](docs/stage-03-oop/chapter-01-classes/section-02-declarations.md)
  - [3.1.3 构造函数](docs/stage-03-oop/chapter-01-classes/section-03-constructors.md)
  - [3.1.4 访问修饰符（public、private、protected）](docs/stage-03-oop/chapter-01-classes/section-04-modifiers.md)
  - [3.1.5 只读属性与静态成员](docs/stage-03-oop/chapter-01-classes/section-05-readonly-static.md)
- [3.2 继承与多态](docs/stage-03-oop/chapter-02-inheritance/readme.md)
  - [3.2.1 继承与多态概述](docs/stage-03-oop/chapter-02-inheritance/section-01-overview.md)
  - [3.2.2 类继承（extends）](docs/stage-03-oop/chapter-02-inheritance/section-02-extends.md)
  - [3.2.3 super 关键字](docs/stage-03-oop/chapter-02-inheritance/section-03-super.md)
  - [3.2.4 抽象类与抽象方法](docs/stage-03-oop/chapter-02-inheritance/section-04-abstract.md)
  - [3.2.5 接口实现（implements）](docs/stage-03-oop/chapter-02-inheritance/section-05-implements.md)
- [3.3 现代类特性](docs/stage-03-oop/chapter-03-modern/readme.md)
  - [3.3.1 现代类特性概述](docs/stage-03-oop/chapter-03-modern/section-01-overview.md)
  - [3.3.2 参数属性（Parameter Properties）](docs/stage-03-oop/chapter-03-modern/section-02-parameter-properties.md)
  - [3.3.3 私有字段（Private Fields）](docs/stage-03-oop/chapter-03-modern/section-03-private-fields.md)
  - [3.3.4 装饰器（Decorators）](docs/stage-03-oop/chapter-03-modern/section-04-decorators.md)
  - [3.3.5 装饰器深入](docs/stage-03-oop/chapter-03-modern/section-05-decorators-advanced.md)
  - [3.3.6 装饰器元数据](docs/stage-03-oop/chapter-03-modern/section-06-decorator-metadata.md)
  - [3.3.7 自定义装饰器](docs/stage-03-oop/chapter-03-modern/section-07-custom-decorators.md)
  - [3.3.8 装饰器组合](docs/stage-03-oop/chapter-03-modern/section-08-decorator-composition.md)

### 阶段四：泛型（Generics）

- [阶段四总览](docs/stage-04-generics/readme.md)
- [4.1 泛型基础](docs/stage-04-generics/chapter-01-basics/readme.md)
  - [4.1.1 泛型概述](docs/stage-04-generics/chapter-01-basics/section-01-overview.md)
  - [4.1.2 泛型函数](docs/stage-04-generics/chapter-01-basics/section-02-functions.md)
  - [4.1.3 泛型接口](docs/stage-04-generics/chapter-01-basics/section-03-interfaces.md)
  - [4.1.4 泛型类](docs/stage-04-generics/chapter-01-basics/section-04-classes.md)
- [4.2 泛型约束](docs/stage-04-generics/chapter-02-constraints/readme.md)
  - [4.2.1 泛型约束概述](docs/stage-04-generics/chapter-02-constraints/section-01-overview.md)
  - [4.2.2 extends 约束](docs/stage-04-generics/chapter-02-constraints/section-02-extends.md)
  - [4.2.3 keyof 操作符](docs/stage-04-generics/chapter-02-constraints/section-03-keyof.md)
  - [4.2.4 条件类型约束](docs/stage-04-generics/chapter-02-constraints/section-04-conditional.md)
- [4.3 泛型实战](docs/stage-04-generics/chapter-03-practice/readme.md)
  - [4.3.1 API 响应类型封装](docs/stage-04-generics/chapter-03-practice/section-01-api-response.md)
  - [4.3.2 工具函数类型化](docs/stage-04-generics/chapter-03-practice/section-02-utility-functions.md)
  - [4.3.3 数据结构类型化](docs/stage-04-generics/chapter-03-practice/section-03-data-structures.md)
- [4.4 泛型工具类型](docs/stage-04-generics/chapter-04-utility-types/readme.md)
  - [4.4.1 泛型工具类型概述](docs/stage-04-generics/chapter-04-utility-types/section-01-overview.md)
  - [4.4.2 泛型相关的工具类型](docs/stage-04-generics/chapter-04-utility-types/section-02-generic-utilities.md)
  - [4.4.3 泛型约束工具](docs/stage-04-generics/chapter-04-utility-types/section-03-constraint-tools.md)

### 阶段五：高级类型系统（进阶）

- [阶段五总览](docs/stage-05-advanced/readme.md)
- [5.1 工具类型（Utility Types）](docs/stage-05-advanced/chapter-01-utilities/readme.md)
  - [5.1.1 工具类型概述](docs/stage-05-advanced/chapter-01-utilities/section-01-overview.md)
  - [5.1.2 基础工具类型（Partial、Required、Readonly）](docs/stage-05-advanced/chapter-01-utilities/section-02-basic.md)
  - [5.1.3 选择工具类型（Pick、Omit）](docs/stage-05-advanced/chapter-01-utilities/section-03-pick-omit.md)
  - [5.1.4 构造工具类型（Record、Exclude、Extract）](docs/stage-05-advanced/chapter-01-utilities/section-04-construct.md)
  - [5.1.5 函数工具类型（Parameters、ReturnType）](docs/stage-05-advanced/chapter-01-utilities/section-05-function.md)
- [5.2 条件类型（Conditional Types）](docs/stage-05-advanced/chapter-02-conditional/readme.md)
  - [5.2.1 条件类型概述](docs/stage-05-advanced/chapter-02-conditional/section-01-overview.md)
  - [5.2.2 条件类型基础](docs/stage-05-advanced/chapter-02-conditional/section-02-basics.md)
  - [5.2.3 分布式条件类型](docs/stage-05-advanced/chapter-02-conditional/section-03-distributive.md)
  - [5.2.4 infer 关键字](docs/stage-05-advanced/chapter-02-conditional/section-04-infer.md)
- [5.3 映射类型（Mapped Types）](docs/stage-05-advanced/chapter-03-mapped/readme.md)
  - [5.3.1 映射类型概述](docs/stage-05-advanced/chapter-03-mapped/section-01-overview.md)
  - [5.3.2 映射类型基础](docs/stage-05-advanced/chapter-03-mapped/section-02-basics.md)
  - [5.3.3 键重映射（Key Remapping）](docs/stage-05-advanced/chapter-03-mapped/section-03-key-remapping.md)
  - [5.3.4 模板字面量类型](docs/stage-05-advanced/chapter-03-mapped/section-04-template-literals.md)
- [5.4 类型守卫（Type Guards）](docs/stage-05-advanced/chapter-04-guards/readme.md)
  - [5.4.1 类型守卫概述](docs/stage-05-advanced/chapter-04-guards/section-01-overview.md)
  - [5.4.2 typeof 与 instanceof](docs/stage-05-advanced/chapter-04-guards/section-02-typeof-instanceof.md)
  - [5.4.3 用户自定义类型守卫](docs/stage-05-advanced/chapter-04-guards/section-03-custom-guards.md)
  - [5.4.4 可辨识联合（Discriminated Unions）](docs/stage-05-advanced/chapter-04-guards/section-04-discriminated-unions.md)
- [5.5 类型体操（Type Gymnastics）](docs/stage-05-advanced/chapter-05-gymnastics/readme.md)
  - [5.5.1 类型体操概述](docs/stage-05-advanced/chapter-05-gymnastics/section-01-overview.md)
  - [5.5.2 复杂类型推导](docs/stage-05-advanced/chapter-05-gymnastics/section-02-complex-inference.md)
  - [5.5.3 类型递归](docs/stage-05-advanced/chapter-05-gymnastics/section-03-recursive-types.md)
  - [5.5.4 实际应用案例](docs/stage-05-advanced/chapter-05-gymnastics/section-04-practical-cases.md)
- [5.6 类型兼容性](docs/stage-05-advanced/chapter-06-compatibility/readme.md)
  - [5.6.1 类型兼容性概述](docs/stage-05-advanced/chapter-06-compatibility/section-01-overview.md)
  - [5.6.2 结构化类型系统深入](docs/stage-05-advanced/chapter-06-compatibility/section-02-structural-types.md)
  - [5.6.3 协变与逆变](docs/stage-05-advanced/chapter-06-compatibility/section-03-variance.md)
  - [5.6.4 类型兼容性规则](docs/stage-05-advanced/chapter-06-compatibility/section-04-compatibility-rules.md)

### 阶段六：模块化与声明文件（工程化）

- [阶段六总览](docs/stage-06-modules/readme.md)
- [6.1 模块系统](docs/stage-06-modules/chapter-01-modules/readme.md)
  - [6.1.1 模块系统概述](docs/stage-06-modules/chapter-01-modules/section-01-overview.md)
  - [6.1.2 ES Modules 与 TypeScript](docs/stage-06-modules/chapter-01-modules/section-02-esm.md)
  - [6.1.3 CommonJS 与 TypeScript](docs/stage-06-modules/chapter-01-modules/section-03-commonjs.md)
  - [6.1.4 模块解析策略](docs/stage-06-modules/chapter-01-modules/section-04-resolution.md)
  - [6.1.5 类型导入（import type）](docs/stage-06-modules/chapter-01-modules/section-05-type-imports.md)
- [6.2 声明文件（.d.ts）](docs/stage-06-modules/chapter-02-declarations/readme.md)
  - [6.2.1 声明文件基础](docs/stage-06-modules/chapter-02-declarations/section-01-basics.md)
  - [6.2.2 声明文件类型](docs/stage-06-modules/chapter-02-declarations/section-02-declaration-types.md)
  - [6.2.3 全局声明文件](docs/stage-06-modules/chapter-02-declarations/section-03-global-declarations.md)
  - [6.2.4 模块声明文件](docs/stage-06-modules/chapter-02-declarations/section-04-module-declarations.md)
  - [6.2.5 declare module 与 declare global](docs/stage-06-modules/chapter-02-declarations/section-05-declare-keywords.md)
  - [6.2.6 declare namespace](docs/stage-06-modules/chapter-02-declarations/section-06-declare-namespace.md)
  - [6.2.7 类型扩展与合并](docs/stage-06-modules/chapter-02-declarations/section-07-type-extension.md)
  - [6.2.8 DefinitelyTyped (@types/)](docs/stage-06-modules/chapter-02-declarations/section-08-definitelytyped.md)
  - [6.2.9 编写自定义声明文件](docs/stage-06-modules/chapter-02-declarations/section-09-custom-declarations.md)
  - [6.2.10 第三方库声明文件处理](docs/stage-06-modules/chapter-02-declarations/section-10-third-party.md)
  - [6.2.11 声明文件最佳实践](docs/stage-06-modules/chapter-02-declarations/section-11-best-practices.md)
- [6.3 命名空间（Namespace）](docs/stage-06-modules/chapter-03-namespaces/readme.md)
  - [6.3.1 命名空间基础](docs/stage-06-modules/chapter-03-namespaces/section-01-basics.md)
  - [6.3.2 命名空间合并](docs/stage-06-modules/chapter-03-namespaces/section-02-merging.md)
  - [6.3.3 命名空间 vs 模块](docs/stage-06-modules/chapter-03-namespaces/section-03-vs-modules.md)
- [6.4 类型生成工具](docs/stage-06-modules/chapter-04-type-generation/readme.md)
  - [6.4.1 json-schema-to-typescript](docs/stage-06-modules/chapter-04-type-generation/section-01-json-schema.md)
  - [6.4.2 quicktype](docs/stage-06-modules/chapter-04-type-generation/section-02-quicktype.md)
  - [6.4.3 从 API 生成类型](docs/stage-06-modules/chapter-04-type-generation/section-03-api-types.md)
  - [6.4.4 openapi-typescript](docs/stage-06-modules/chapter-04-type-generation/section-04-openapi.md)

### 阶段七：TypeScript 5.x 新特性（最新）

- [阶段七总览](docs/stage-07-latest/readme.md)
- [7.1 TypeScript 5.0 新特性](docs/stage-07-latest/chapter-01-ts50/readme.md)
  - [7.1.1 const 类型参数](docs/stage-07-latest/chapter-01-ts50/section-01-const-type-params.md)
  - [7.1.2 装饰器元数据](docs/stage-07-latest/chapter-01-ts50/section-02-decorator-metadata.md)
  - [7.1.3 其他改进](docs/stage-07-latest/chapter-01-ts50/section-03-other-improvements.md)
- [7.2 TypeScript 5.1-5.6 新特性](docs/stage-07-latest/chapter-02-ts51-56/readme.md)
  - [7.2.1 TypeScript 5.1 新特性](docs/stage-07-latest/chapter-02-ts51-56/section-01-ts51.md)
  - [7.2.2 TypeScript 5.2 新特性](docs/stage-07-latest/chapter-02-ts51-56/section-02-ts52.md)
  - [7.2.3 TypeScript 5.3-5.6 新特性](docs/stage-07-latest/chapter-02-ts51-56/section-03-ts53-56.md)
- [7.3 TypeScript 未来发展方向](docs/stage-07-latest/chapter-03-future/readme.md)
  - [7.3.1 技术路线图](docs/stage-07-latest/chapter-03-future/section-01-roadmap.md)
  - [7.3.2 社区动态](docs/stage-07-latest/chapter-03-future/section-02-community.md)
  - [7.3.3 发展趋势](docs/stage-07-latest/chapter-03-future/section-03-trends.md)

### 阶段八：最佳实践与性能优化（生产级）

- [阶段八总览](docs/stage-08-best-practices/readme.md)
- [8.1 代码组织](docs/stage-08-best-practices/chapter-01-organization/readme.md)
  - [8.1.1 项目结构](docs/stage-08-best-practices/chapter-01-organization/section-01-project-structure.md)
  - [8.1.2 类型定义组织](docs/stage-08-best-practices/chapter-01-organization/section-02-type-organization.md)
  - [8.1.3 命名规范](docs/stage-08-best-practices/chapter-01-organization/section-03-naming-conventions.md)
- [8.2 类型安全最佳实践](docs/stage-08-best-practices/chapter-02-type-safety/readme.md)
  - [8.2.1 避免 any](docs/stage-08-best-practices/chapter-02-type-safety/section-01-avoid-any.md)
  - [8.2.2 使用 unknown 代替 any](docs/stage-08-best-practices/chapter-02-type-safety/section-02-use-unknown.md)
  - [8.2.3 严格模式配置](docs/stage-08-best-practices/chapter-02-type-safety/section-03-strict-mode.md)
- [8.3 性能优化](docs/stage-08-best-practices/chapter-03-performance/readme.md)
  - [8.3.1 编译性能优化](docs/stage-08-best-practices/chapter-03-performance/section-01-compilation.md)
  - [8.3.2 类型检查性能](docs/stage-08-best-practices/chapter-03-performance/section-02-type-checking.md)
  - [8.3.3 项目引用（Project References）](docs/stage-08-best-practices/chapter-03-performance/section-03-project-references.md)
- [8.4 常见错误与调试](docs/stage-08-best-practices/chapter-04-debugging/readme.md)
  - [8.4.1 常见类型错误](docs/stage-08-best-practices/chapter-04-debugging/section-01-common-errors.md)
  - [8.4.2 类型错误调试技巧](docs/stage-08-best-practices/chapter-04-debugging/section-02-debugging-tips.md)
  - [8.4.3 类型错误解决方案](docs/stage-08-best-practices/chapter-04-debugging/section-03-solutions.md)
- [8.5 类型测试](docs/stage-08-best-practices/chapter-05-type-testing/readme.md)
  - [8.5.1 tsd 类型测试](docs/stage-08-best-practices/chapter-05-type-testing/section-01-tsd.md)
  - [8.5.2 dtslint 类型测试](docs/stage-08-best-practices/chapter-05-type-testing/section-02-dtslint.md)
  - [8.5.3 类型测试最佳实践](docs/stage-08-best-practices/chapter-05-type-testing/section-03-best-practices.md)
- [8.6 与构建工具集成](docs/stage-08-best-practices/chapter-06-build-tools/readme.md)
  - [8.6.1 Vite + TypeScript](docs/stage-08-best-practices/chapter-06-build-tools/section-01-vite.md)
  - [8.6.2 Webpack + TypeScript](docs/stage-08-best-practices/chapter-06-build-tools/section-02-webpack.md)
  - [8.6.3 Turbopack + TypeScript](docs/stage-08-best-practices/chapter-06-build-tools/section-03-turbopack.md)
- [8.7 TypeScript 在全栈开发中的应用](docs/stage-08-best-practices/chapter-07-fullstack/readme.md)
  - [8.7.1 全栈开发概述](docs/stage-08-best-practices/chapter-07-fullstack/section-01-overview.md)
  - [8.7.2 前后端类型共享](docs/stage-08-best-practices/chapter-07-fullstack/section-02-type-sharing.md)
  - [8.7.3 API 类型定义](docs/stage-08-best-practices/chapter-07-fullstack/section-03-api-types.md)
  - [8.7.4 类型安全的全栈开发](docs/stage-08-best-practices/chapter-07-fullstack/section-04-type-safe-fullstack.md)
- [8.8 TypeScript 与测试框架集成](docs/stage-08-best-practices/chapter-08-testing/readme.md)
  - [8.8.1 测试框架概述](docs/stage-08-best-practices/chapter-08-testing/section-01-overview.md)
  - [8.8.2 Jest + TypeScript](docs/stage-08-best-practices/chapter-08-testing/section-02-jest.md)
  - [8.8.3 Vitest + TypeScript](docs/stage-08-best-practices/chapter-08-testing/section-03-vitest.md)
  - [8.8.4 类型测试](docs/stage-08-best-practices/chapter-08-testing/section-04-type-testing.md)
  - [8.8.5 Mock 类型](docs/stage-08-best-practices/chapter-08-testing/section-05-mock-types.md)

---

## 学习路径建议

### 初学者路径

1. **阶段一**：搭建 TypeScript 环境，掌握基础类型
2. **阶段二**：学习结构化类型系统（接口、类型别名）
3. **阶段三**：掌握面向对象编程（类、继承）
4. **阶段四**：深入学习泛型
5. **阶段五**：掌握高级类型系统
6. **阶段六**：学习模块化与声明文件
7. **阶段七**：了解最新特性
8. **阶段八**：掌握最佳实践

### 有经验开发者路径

- 可直接跳转到感兴趣的阶段
- 建议重点学习阶段四（泛型）、阶段五（高级类型）、阶段八（最佳实践）

---

## 文档特点

- **面向有 JS 基础的开发者**：假设已掌握 JavaScript 基础
- **内容详实**：提供完整的语法、参数说明和使用示例
- **示例丰富**：每个知识点都配有完整的代码示例
- **实践导向**：每章都包含练习任务，帮助巩固学习
- **结构清晰**：按阶段、章节、小节分层组织，便于查阅
- **技术前沿**：反映 TypeScript 5.6+ 最新特性

---

## 版本信息

- **版本**：2025.1
- **创建日期**：2025-12-11
- **适用 TypeScript 版本**：TypeScript 5.6+
- **最后更新**：2025-12-19
