# 2.1.2 接口基础

## 概述

本节介绍接口的基本定义和使用方法，包括接口的语法、属性定义和基本用法。

## 接口定义

### 基本语法

```ts
interface InterfaceName {
    property1: type1;
    property2: type2;
    // ...
}
```

### 示例

```ts
// 定义用户接口
interface User {
    name: string;
    age: number;
    email: string;
}
```

## 使用接口

### 类型注解

使用接口作为类型注解：

```ts
interface User {
    name: string;
    age: number;
    email: string;
}

// 变量类型注解
let user: User = {
    name: "John",
    age: 30,
    email: "john@example.com"
};
```

### 函数参数

接口可以作为函数参数类型：

```ts
interface User {
    name: string;
    age: number;
}

function greet(user: User): string {
    return `Hello, ${user.name}!`;
}

greet({
    name: "John",
    age: 30
});
```

### 函数返回值

接口可以作为函数返回值类型：

```ts
interface User {
    name: string;
    age: number;
}

function createUser(name: string, age: number): User {
    return {
        name,
        age
    };
}
```

## 属性类型

### 基础类型

```ts
interface User {
    name: string;      // 字符串
    age: number;       // 数字
    isActive: boolean; // 布尔值
}
```

### 数组类型

```ts
interface User {
    name: string;
    tags: string[]; // 字符串数组
}
```

### 对象类型

```ts
interface Address {
    street: string;
    city: string;
}

interface User {
    name: string;
    address: Address; // 对象类型
}
```

### 联合类型

```ts
interface User {
    name: string;
    status: "active" | "inactive" | "pending"; // 联合类型
}
```

### 任意类型

```ts
interface Config {
    name: string;
    data: any; // 任意类型（不推荐）
}
```

## 接口实现

### 对象字面量

对象字面量可以直接实现接口：

```ts
interface User {
    name: string;
    age: number;
}

// 对象字面量实现接口
let user: User = {
    name: "John",
    age: 30
};
```

### 类实现

类可以实现接口：

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

## 属性访问

### 点号访问

```ts
interface User {
    name: string;
    age: number;
}

let user: User = {
    name: "John",
    age: 30
};

console.log(user.name); // "John"
console.log(user.age);  // 30
```

### 方括号访问

```ts
let user: User = {
    name: "John",
    age: 30
};

console.log(user["name"]); // "John"

// 动态属性访问
let key: keyof User = "name";
console.log(user[key]); // "John"
```

## 类型检查

### 必需属性

接口中定义的属性都是必需的：

```ts
interface User {
    name: string;
    age: number;
}

// 错误：缺少 age 属性
let user: User = {
    name: "John"
};

// 正确：包含所有必需属性
let user2: User = {
    name: "John",
    age: 30
};
```

### 额外属性

默认情况下，对象不能有接口未定义的属性：

```ts
interface User {
    name: string;
    age: number;
}

// 错误：有额外属性
let user: User = {
    name: "John",
    age: 30,
    email: "john@example.com" // 错误：接口中没有 email
};
```

### 类型断言

可以使用类型断言绕过额外属性检查：

```ts
let user = {
    name: "John",
    age: 30,
    email: "john@example.com"
} as User;
```

## 嵌套接口

### 定义

接口可以嵌套定义：

```ts
interface Address {
    street: string;
    city: string;
    zipCode: string;
}

interface User {
    name: string;
    age: number;
    address: Address; // 嵌套接口
}

let user: User = {
    name: "John",
    age: 30,
    address: {
        street: "123 Main St",
        city: "New York",
        zipCode: "10001"
    }
};
```

### 内联定义

也可以内联定义嵌套对象：

```ts
interface User {
    name: string;
    age: number;
    address: {
        street: string;
        city: string;
        zipCode: string;
    };
}
```

## 常见错误

### 错误 1：缺少必需属性

```ts
interface User {
    name: string;
    age: number;
}

// 错误：缺少 age 属性
let user: User = {
    name: "John"
};
```

### 错误 2：类型不匹配

```ts
interface User {
    name: string;
    age: number;
}

// 错误：age 类型不匹配
let user: User = {
    name: "John",
    age: "30" // 错误：应该是 number
};
```

### 错误 3：额外属性

```ts
interface User {
    name: string;
    age: number;
}

// 错误：有额外属性
let user: User = {
    name: "John",
    age: 30,
    email: "john@example.com" // 错误
};
```

## 注意事项

1. **接口是类型**：接口只在编译时存在，运行时会被移除
2. **必需属性**：接口中定义的属性默认都是必需的
3. **额外属性**：默认不允许额外属性，可以使用类型断言绕过
4. **结构化类型**：只要对象具有接口要求的属性，就认为它实现了该接口

## 最佳实践

1. **明确命名**：使用清晰的接口名称，通常使用名词
2. **合理组织**：将相关的属性组织在一起
3. **避免过度嵌套**：避免过深的嵌套结构
4. **使用类型别名**：对于复杂的内联类型，考虑使用类型别名

## 练习

1. **接口定义**：定义一个产品接口，包含名称、价格、描述等属性。

2. **接口使用**：创建符合接口定义的对象，体验类型检查。

3. **嵌套接口**：定义包含嵌套对象的接口。

4. **类型检查**：故意制造类型错误，理解错误信息。

5. **接口实现**：使用类实现接口，理解接口的作用。

完成以上练习后，继续学习下一节，了解可选属性与只读属性。

## 总结

接口是 TypeScript 中定义对象形状的方式。接口提供类型检查，确保对象符合接口定义。理解接口的基本定义和使用是学习 TypeScript 类型系统的关键。

## 相关资源

- [TypeScript 接口文档](https://www.typescriptlang.org/docs/handbook/2/objects.html#interfaces)
