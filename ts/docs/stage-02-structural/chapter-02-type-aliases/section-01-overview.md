# 2.2.1 类型别名概述

## 概述

类型别名（Type Alias）是 TypeScript 中用于创建类型名称的方式，可以为类型创建新的名称。本节介绍类型别名的概念、作用和优势。

## 什么是类型别名

### 定义

类型别名使用 `type` 关键字为类型创建新的名称，可以简化复杂类型的定义。

### 基本语法

```ts
type AliasName = Type;
```

### 示例

```ts
// 为 string 创建别名
type Name = string;

// 使用类型别名
let userName: Name = "John";

// 为对象类型创建别名
type User = {
    name: string;
    age: number;
};

let user: User = {
    name: "John",
    age: 30
};
```

## 类型别名的作用

### 1. 简化复杂类型

类型别名可以简化复杂类型的定义：

```ts
// 复杂类型
let user: {
    name: string;
    age: number;
    address: {
        street: string;
        city: string;
    };
} = {
    name: "John",
    age: 30,
    address: {
        street: "123 Main St",
        city: "New York"
    }
};

// 使用类型别名简化
type Address = {
    street: string;
    city: string;
};

type User = {
    name: string;
    age: number;
    address: Address;
};

let user2: User = {
    name: "John",
    age: 30,
    address: {
        street: "123 Main St",
        city: "New York"
    }
};
```

### 2. 提高可读性

类型别名可以提高代码的可读性：

```ts
// 不清晰
function process(data: { id: number; value: string }[]): void {
    // ...
}

// 使用类型别名更清晰
type DataItem = {
    id: number;
    value: string;
};

function process(data: DataItem[]): void {
    // ...
}
```

### 3. 代码复用

类型别名可以复用类型定义：

```ts
type ID = string | number;

interface User {
    id: ID;
    name: string;
}

interface Product {
    id: ID;
    title: string;
}
```

### 4. 支持复杂类型

类型别名支持联合类型、交叉类型等复杂类型：

```ts
// 联合类型
type Status = "pending" | "approved" | "rejected";

// 交叉类型
type UserWithTimestamp = User & {
    createdAt: Date;
    updatedAt: Date;
};
```

## 类型别名的优势

### 1. 灵活性

类型别名比接口更灵活，支持更多类型：

```ts
// 联合类型
type StringOrNumber = string | number;

// 元组类型
type Point = [number, number];

// 函数类型
type Handler = (event: Event) => void;
```

### 2. 复杂类型支持

类型别名支持复杂的类型操作：

```ts
// 条件类型
type NonNullable<T> = T extends null | undefined ? never : T;

// 映射类型
type Readonly<T> = {
    readonly [P in keyof T]: T[P];
};
```

### 3. 类型计算

类型别名支持类型计算：

```ts
type Keys = "name" | "age" | "email";

type User = {
    [K in Keys]: string;
};
```

## 类型别名 vs 接口

### 相似点

类型别名和接口都可以定义对象类型：

```ts
// 类型别名
type User = {
    name: string;
    age: number;
};

// 接口
interface User {
    name: string;
    age: number;
}
```

### 区别

| 特性           | 类型别名                 | 接口                     |
|:---------------|:-------------------------|:-------------------------|
| 扩展方式       | &（交叉类型）            | extends                  |
| 合并           | 不支持                   | 支持声明合并             |
| 实现           | 不能                     | 可以被类实现             |
| 复杂类型       | 支持联合、交叉、条件等   | 不支持                   |
| 使用场景       | 复杂类型定义             | 对象形状定义             |

## 使用场景

### 1. 复杂类型定义

类型别名适合定义复杂类型：

```ts
// 联合类型
type Status = "pending" | "approved" | "rejected";

// 交叉类型
type UserWithRole = User & { role: string };

// 函数类型
type EventHandler = (event: Event) => void;
```

### 2. 类型计算

类型别名适合进行类型计算：

```ts
type Keys = "name" | "age";

type User = {
    [K in Keys]: string;
};
```

### 3. 简化重复类型

类型别名可以简化重复的类型定义：

```ts
type ID = string | number;

// 在多个地方使用
interface User {
    id: ID;
}

interface Product {
    id: ID;
}
```

## 注意事项

1. **类型别名是类型**：类型别名只在编译时存在，运行时会被移除
2. **不能合并**：类型别名不支持声明合并
3. **不能实现**：类型别名不能被类实现
4. **支持复杂类型**：类型别名支持联合、交叉、条件等复杂类型

## 最佳实践

1. **使用类型别名定义复杂类型**：优先使用类型别名定义复杂类型
2. **使用接口定义对象形状**：优先使用接口定义对象形状
3. **合理命名**：使用清晰的类型别名名称
4. **避免过度使用**：避免过度使用类型别名，保持代码简洁

## 练习

1. **类型别名定义**：定义不同类型的类型别名，理解其用法。

2. **简化复杂类型**：使用类型别名简化复杂的类型定义。

3. **类型复用**：定义可复用的类型别名，在多个地方使用。

4. **复杂类型**：定义联合类型、交叉类型等复杂类型别名。

5. **实际应用**：在实际场景中应用类型别名。

完成以上练习后，继续学习下一节，了解类型别名基础。

## 总结

类型别名是 TypeScript 中用于创建类型名称的方式，可以简化复杂类型的定义。类型别名支持联合类型、交叉类型等复杂类型，比接口更灵活。理解类型别名的概念和作用是学习 TypeScript 类型系统的关键。

## 相关资源

- [TypeScript 类型别名文档](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-aliases)
