# 2.1.1 接口概述

## 概述

接口（Interface）是 TypeScript 中用于定义对象形状的结构化类型。本节介绍接口的概念、作用和优势。

## 什么是接口

### 定义

接口是一种类型契约，用于描述对象应该具有的属性和方法。

### 基本概念

```ts
// 接口定义
interface User {
    name: string;
    age: number;
}

// 使用接口
let user: User = {
    name: "John",
    age: 30
};
```

## 接口的作用

### 1. 类型检查

接口提供编译时类型检查，确保对象符合接口定义：

```ts
interface User {
    name: string;
    age: number;
}

// 正确：符合接口定义
let user: User = {
    name: "John",
    age: 30
};

// 错误：缺少必需属性
let user2: User = {
    name: "John"
    // 错误：缺少 age 属性
};
```

### 2. 代码文档

接口作为代码文档，清楚地说明对象的结构：

```ts
interface ApiResponse {
    status: number;
    data: any;
    message: string;
}

// 接口清楚地说明了 API 响应的结构
function handleResponse(response: ApiResponse) {
    // ...
}
```

### 3. IDE 支持

接口提供更好的 IDE 支持：

```ts
interface User {
    name: string;
    age: number;
    email: string;
}

let user: User = {
    name: "John",
    age: 30,
    email: "john@example.com"
};

// IDE 会提供自动补全
user. // 提示：name, age, email
```

### 4. 重构安全

接口使重构更安全：

```ts
interface User {
    name: string;
    age: number;
}

// 修改接口时，所有使用的地方都会提示错误
interface User {
    name: string;
    age: number;
    email: string; // 新增属性
}

// 所有 User 类型的对象都需要添加 email 属性
```

## 接口的优势

### 1. 结构化类型系统

TypeScript 使用结构化类型系统（Duck Typing），只要对象具有接口要求的属性，就认为它实现了该接口：

```ts
interface Point {
    x: number;
    y: number;
}

// 对象字面量直接符合接口
let point: Point = {
    x: 10,
    y: 20
};

// 已有的对象也可以符合接口
let obj = {
    x: 10,
    y: 20,
    z: 30 // 额外的属性也可以
};

let point2: Point = obj; // 正确：obj 具有 x 和 y 属性
```

### 2. 可扩展性

接口支持继承和合并，可以轻松扩展：

```ts
// 基础接口
interface Animal {
    name: string;
}

// 扩展接口
interface Dog extends Animal {
    breed: string;
}

// 接口合并
interface User {
    name: string;
}

interface User {
    age: number;
}

// 合并后的 User 包含 name 和 age
```

### 3. 可选和只读属性

接口支持可选属性和只读属性：

```ts
interface User {
    name: string;
    age?: number;        // 可选属性
    readonly id: number; // 只读属性
}
```

## 接口 vs 类型别名

### 相似点

接口和类型别名都可以定义对象类型：

```ts
// 接口
interface User {
    name: string;
    age: number;
}

// 类型别名
type User = {
    name: string;
    age: number;
};
```

### 区别

| 特性           | 接口                 | 类型别名             |
|:---------------|:---------------------|:---------------------|
| 扩展方式       | extends              | &（交叉类型）        |
| 合并           | 支持声明合并         | 不支持               |
| 实现           | 可以被类实现         | 不能                 |
| 复杂类型       | 不支持联合、交叉等   | 支持                 |
| 使用场景       | 对象形状定义         | 复杂类型定义         |

## 使用场景

### 1. 对象形状定义

接口最适合定义对象的形状：

```ts
interface Config {
    apiUrl: string;
    timeout: number;
    retries: number;
}
```

### 2. 函数参数和返回值

接口可以用于函数参数和返回值：

```ts
interface User {
    name: string;
    age: number;
}

function getUser(): User {
    return {
        name: "John",
        age: 30
    };
}

function processUser(user: User) {
    // ...
}
```

### 3. 类实现

接口可以被类实现：

```ts
interface Flyable {
    fly(): void;
}

class Bird implements Flyable {
    fly() {
        console.log("Flying");
    }
}
```

## 注意事项

1. **接口是类型**：接口只在编译时存在，运行时会被移除
2. **结构化类型**：TypeScript 使用结构化类型系统，关注形状而非名称
3. **可选属性**：使用 `?` 标记可选属性
4. **只读属性**：使用 `readonly` 标记只读属性

## 最佳实践

1. **使用接口定义对象**：优先使用接口定义对象形状
2. **明确命名**：使用清晰的接口名称
3. **合理使用可选属性**：只在必要时使用可选属性
4. **利用继承**：使用接口继承避免重复定义

## 练习

1. **接口定义**：定义一个用户接口，包含姓名、年龄、邮箱等属性。

2. **接口使用**：创建符合接口定义的对象，体验类型检查。

3. **IDE 支持**：使用接口，观察 IDE 的自动补全和错误提示。

4. **接口扩展**：使用接口继承扩展基础接口。

5. **接口合并**：尝试接口声明合并，理解合并规则。

完成以上练习后，继续学习下一节，了解接口基础。

## 总结

接口是 TypeScript 结构化类型系统的核心，用于定义对象的形状。接口提供类型检查、代码文档、IDE 支持和重构安全等优势。理解接口的概念和作用是学习 TypeScript 类型系统的关键。

## 相关资源

- [TypeScript 接口文档](https://www.typescriptlang.org/docs/handbook/2/objects.html#interfaces)
