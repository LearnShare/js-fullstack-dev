# 8.1.1 项目结构

## 概述

良好的项目结构有助于代码组织和维护。本节介绍 TypeScript 项目的结构组织。

## 基本项目结构

### 标准结构

```
project/
├── src/
│   ├── components/
│   ├── utils/
│   ├── types/
│   └── index.ts
├── tests/
├── dist/
├── node_modules/
├── tsconfig.json
├── package.json
└── README.md
```

### 详细结构

```
project/
├── src/
│   ├── components/        # 组件
│   │   ├── Button/
│   │   │   ├── Button.tsx
│   │   │   ├── Button.test.tsx
│   │   │   └── index.ts
│   │   └── index.ts
│   ├── utils/             # 工具函数
│   │   ├── format.ts
│   │   ├── validate.ts
│   │   └── index.ts
│   ├── types/             # 类型定义
│   │   ├── user.ts
│   │   ├── api.ts
│   │   └── index.ts
│   ├── services/          # 服务
│   │   ├── api.ts
│   │   └── index.ts
│   └── index.ts           # 入口文件
├── tests/                 # 测试
│   ├── unit/
│   └── integration/
├── dist/                  # 编译输出
├── types/                 # 全局类型定义
│   └── global.d.ts
├── tsconfig.json
├── package.json
└── README.md
```

## 组织原则

### 1. 按功能组织

按功能模块组织代码：

```
src/
├── users/
│   ├── User.ts
│   ├── UserService.ts
│   └── user.types.ts
├── products/
│   ├── Product.ts
│   ├── ProductService.ts
│   └── product.types.ts
```

### 2. 按层次组织

按层次组织代码：

```
src/
├── models/        # 数据模型
├── services/      # 业务逻辑
├── controllers/   # 控制器
└── views/         # 视图
```

### 3. 按类型组织

按文件类型组织代码：

```
src/
├── components/
├── utils/
├── types/
└── services/
```

## 使用场景

### 1. 小型项目

```
project/
├── src/
│   ├── index.ts
│   └── types.ts
├── tsconfig.json
└── package.json
```

### 2. 中型项目

```
project/
├── src/
│   ├── components/
│   ├── utils/
│   ├── types/
│   └── index.ts
├── tsconfig.json
└── package.json
```

### 3. 大型项目

```
project/
├── packages/
│   ├── core/
│   ├── ui/
│   └── utils/
├── tsconfig.json
└── package.json
```

## 注意事项

1. **结构清晰**：保持项目结构清晰
2. **易于维护**：便于代码维护
3. **可扩展性**：考虑项目扩展性
4. **团队协作**：考虑团队协作需求

## 最佳实践

1. **按功能组织**：按功能模块组织代码
2. **保持简洁**：保持项目结构简洁
3. **统一规范**：遵循统一的组织规范
4. **文档说明**：为项目结构添加文档说明

## 练习

1. **项目结构**：设计一个 TypeScript 项目结构。

2. **组织代码**：按照最佳实践组织代码。

3. **实际应用**：在实际项目中应用项目结构。

完成以上练习后，继续学习下一节，了解类型定义组织。

## 总结

良好的项目结构有助于代码组织和维护。按功能、层次或类型组织代码，保持结构清晰、易于维护。理解项目结构的组织是学习代码组织的关键。

## 相关资源

- [TypeScript 项目结构最佳实践](https://www.typescriptlang.org/docs/handbook/project-references.html)
