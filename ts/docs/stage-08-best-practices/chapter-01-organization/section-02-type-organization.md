# 8.1.2 类型定义组织

## 概述

类型定义的组织方式影响代码的可维护性。本节介绍类型定义的组织方式。

## 组织方式

### 1. 按模块组织

按功能模块组织类型定义：

```
types/
├── user/
│   ├── User.ts
│   ├── UserService.ts
│   └── index.ts
├── product/
│   ├── Product.ts
│   ├── ProductService.ts
│   └── index.ts
└── index.ts
```

### 2. 按类型组织

按类型分类组织类型定义：

```
types/
├── interfaces/
│   ├── User.ts
│   ├── Product.ts
│   └── index.ts
├── types/
│   ├── ApiResponse.ts
│   ├── Config.ts
│   └── index.ts
└── enums/
    ├── Status.ts
    ├── Role.ts
    └── index.ts
```

### 3. 集中式组织

集中式组织类型定义：

```
types/
├── user.types.ts
├── product.types.ts
├── api.types.ts
└── index.ts
```

## 导出方式

### 1. 命名导出

```ts
// types/user.ts
export interface User {
    name: string;
    age: number;
}

export type UserStatus = "active" | "inactive";
```

### 2. 默认导出

```ts
// types/user.ts
interface User {
    name: string;
    age: number;
}

export default User;
```

### 3. 统一导出

```ts
// types/index.ts
export * from "./user";
export * from "./product";
export * from "./api";
```

## 使用场景

### 1. 小型项目

```
types/
├── types.ts
└── index.ts
```

### 2. 中型项目

```
types/
├── user.types.ts
├── product.types.ts
└── index.ts
```

### 3. 大型项目

```
types/
├── user/
├── product/
└── index.ts
```

## 注意事项

1. **组织清晰**：保持类型定义组织清晰
2. **避免重复**：避免类型定义重复
3. **易于查找**：便于查找类型定义
4. **统一导出**：使用统一的导出方式

## 最佳实践

1. **按模块组织**：按功能模块组织类型定义
2. **统一导出**：使用统一的导出方式
3. **避免重复**：避免类型定义重复
4. **文档注释**：为类型定义添加文档注释

## 练习

1. **类型组织**：组织类型定义。

2. **导出方式**：使用统一的导出方式。

3. **实际应用**：在实际项目中应用类型定义组织。

完成以上练习后，继续学习下一节，了解命名规范。

## 总结

类型定义的组织方式影响代码的可维护性。按模块、类型或集中式组织类型定义，使用统一的导出方式。理解类型定义的组织是学习代码组织的关键。

## 相关资源

- [TypeScript 类型定义组织最佳实践](https://www.typescriptlang.org/docs/handbook/declaration-files/introduction.html)
