# 2.1.3 可选属性与只读属性

## 概述

接口支持可选属性和只读属性，提供更灵活的类型定义。本节介绍可选属性和只读属性的定义和使用。

## 可选属性

### 定义

可选属性使用 `?` 标记，表示该属性可以存在也可以不存在。

### 语法

```ts
interface InterfaceName {
    requiredProperty: type;
    optionalProperty?: type;
}
```

### 示例

```ts
interface User {
    name: string;
    age?: number;      // 可选属性
    email?: string;     // 可选属性
}

// 可以只提供必需属性
let user1: User = {
    name: "John"
};

// 可以提供可选属性
let user2: User = {
    name: "John",
    age: 30
};

// 可以提供所有属性
let user3: User = {
    name: "John",
    age: 30,
    email: "john@example.com"
};
```

### 使用场景

可选属性适用于：

1. **配置对象**：某些配置项可能不需要

```ts
interface Config {
    apiUrl: string;
    timeout?: number;    // 可选：有默认值
    retries?: number;    // 可选：有默认值
}
```

2. **API 响应**：某些字段可能不存在

```ts
interface ApiResponse {
    status: number;
    data?: any;         // 可选：可能为空
    message?: string;   // 可选：错误时才有
}
```

3. **用户信息**：某些信息可能不完整

```ts
interface User {
    name: string;
    age?: number;       // 可选：用户可能未填写
    email?: string;     // 可选：用户可能未填写
}
```

### 访问可选属性

访问可选属性时需要进行检查：

```ts
interface User {
    name: string;
    age?: number;
}

function getUserAge(user: User): number | undefined {
    // 可选属性可能是 undefined
    return user.age;
}

// 使用前检查
function displayUser(user: User) {
    console.log(user.name);
    if (user.age !== undefined) {
        console.log(`Age: ${user.age}`);
    }
}
```

### 默认值处理

可以为可选属性提供默认值：

```ts
interface Config {
    timeout?: number;
}

function getTimeout(config: Config): number {
    return config.timeout ?? 5000; // 默认 5000
}
```

## 只读属性

### 定义

只读属性使用 `readonly` 关键字标记，表示该属性只能在创建时赋值，之后不能修改。

### 语法

```ts
interface InterfaceName {
    readonly property: type;
}
```

### 示例

```ts
interface User {
    readonly id: number;
    name: string;
    age: number;
}

let user: User = {
    id: 1,
    name: "John",
    age: 30
};

// 可以修改普通属性
user.name = "Jane";
user.age = 31;

// 错误：不能修改只读属性
// user.id = 2; // 错误：Cannot assign to 'id' because it is a read-only property
```

### 使用场景

只读属性适用于：

1. **ID 标识符**：对象的唯一标识不应该改变

```ts
interface Entity {
    readonly id: number;
    name: string;
}
```

2. **配置常量**：某些配置值不应该被修改

```ts
interface AppConfig {
    readonly version: string;
    readonly apiUrl: string;
    timeout: number; // 可以修改
}
```

3. **不可变数据**：确保数据的不可变性

```ts
interface Point {
    readonly x: number;
    readonly y: number;
}
```

### 只读数组

数组也可以标记为只读：

```ts
interface User {
    name: string;
    readonly tags: string[]; // 只读数组
}

let user: User = {
    name: "John",
    tags: ["developer", "typescript"]
};

// 错误：不能修改只读数组
// user.tags.push("javascript"); // 错误

// 可以使用 ReadonlyArray
interface User2 {
    name: string;
    tags: ReadonlyArray<string>;
}
```

## 组合使用

### 可选 + 只读

可以同时使用可选和只读：

```ts
interface User {
    name: string;
    readonly id?: number;      // 可选且只读
    readonly createdAt?: Date; // 可选且只读
}

let user: User = {
    name: "John",
    id: 1
};

// id 一旦设置就不能修改
// user.id = 2; // 错误
```

### 完整示例

```ts
interface User {
    readonly id: number;        // 只读：ID 不能修改
    name: string;              // 必需：姓名必须提供
    age?: number;              // 可选：年龄可能不提供
    readonly createdAt: Date;  // 只读：创建时间不能修改
    updatedAt?: Date;          // 可选且可变：更新时间可选
}

let user: User = {
    id: 1,
    name: "John",
    createdAt: new Date()
};

// 可以修改
user.name = "Jane";
user.age = 30;
user.updatedAt = new Date();

// 不能修改
// user.id = 2; // 错误
// user.createdAt = new Date(); // 错误
```

## 类型检查

### 可选属性的类型

可选属性的类型是 `T | undefined`：

```ts
interface User {
    age?: number;
}

let user: User = {};

// user.age 的类型是 number | undefined
if (user.age !== undefined) {
    // 类型收窄为 number
    console.log(user.age.toFixed(2));
}
```

### 只读属性的赋值

只读属性只能在对象字面量中赋值：

```ts
interface User {
    readonly id: number;
    name: string;
}

// 正确：在对象字面量中赋值
let user: User = {
    id: 1,
    name: "John"
};

// 错误：不能单独赋值
// user.id = 2; // 错误
```

## 常见错误

### 错误 1：访问可选属性未检查

```ts
interface User {
    age?: number;
}

let user: User = {};

// 错误：可能为 undefined
console.log(user.age.toFixed(2)); // 错误
```

### 错误 2：修改只读属性

```ts
interface User {
    readonly id: number;
}

let user: User = { id: 1 };

// 错误：不能修改只读属性
user.id = 2; // 错误
```

## 注意事项

1. **可选属性类型**：可选属性的类型是 `T | undefined`
2. **只读属性赋值**：只读属性只能在创建时赋值
3. **只读数组**：只读数组不能使用修改方法（push、pop 等）
4. **组合使用**：可选和只读可以组合使用

## 最佳实践

1. **合理使用可选属性**：只在确实可选时使用，避免过度使用
2. **使用只读保护**：对于不应该修改的属性使用只读
3. **类型检查**：访问可选属性前进行类型检查
4. **默认值处理**：为可选属性提供合理的默认值

## 练习

1. **可选属性**：定义包含可选属性的接口，练习使用。

2. **只读属性**：定义包含只读属性的接口，理解只读限制。

3. **组合使用**：定义同时包含可选和只读属性的接口。

4. **类型检查**：练习访问可选属性时的类型检查。

5. **实际应用**：在实际场景中应用可选和只读属性。

完成以上练习后，继续学习下一节，了解函数类型与索引签名。

## 总结

可选属性和只读属性提供了更灵活的类型定义。可选属性使用 `?` 标记，表示属性可以不存在。只读属性使用 `readonly` 标记，表示属性只能在创建时赋值。理解可选和只读属性的使用场景，可以帮助我们更好地设计类型系统。

## 相关资源

- [TypeScript 可选属性文档](https://www.typescriptlang.org/docs/handbook/2/objects.html#optional-properties)
- [TypeScript 只读属性文档](https://www.typescriptlang.org/docs/handbook/2/objects.html#readonly-properties)
