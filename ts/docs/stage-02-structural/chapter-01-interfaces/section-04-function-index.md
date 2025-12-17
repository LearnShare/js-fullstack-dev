# 2.1.4 函数类型与索引签名

## 概述

接口不仅可以定义对象属性，还可以定义函数类型和索引签名。本节介绍接口中的函数类型定义和索引签名的使用。

## 函数类型

### 定义

接口可以定义函数类型，用于描述函数的签名。

### 语法

```ts
interface InterfaceName {
    (param1: type1, param2: type2): returnType;
}
```

### 示例

```ts
// 定义函数接口
interface Calculator {
    (a: number, b: number): number;
}

// 实现函数接口
let add: Calculator = function(a, b) {
    return a + b;
};

let multiply: Calculator = function(a, b) {
    return a * b;
};

// 使用
console.log(add(1, 2));        // 3
console.log(multiply(2, 3));   // 6
```

### 对象中的方法

接口可以定义对象中的方法：

```ts
interface User {
    name: string;
    greet(): string;           // 无参数方法
    getAge(): number;           // 无参数方法
    updateName(name: string): void; // 有参数方法
}

let user: User = {
    name: "John",
    greet() {
        return `Hello, ${this.name}!`;
    },
    getAge() {
        return 30;
    },
    updateName(name: string) {
        this.name = name;
    }
};
```

### 方法简写

可以使用方法简写语法：

```ts
interface User {
    name: string;
    greet: () => string;       // 箭头函数形式
    getAge: () => number;
    updateName: (name: string) => void;
}
```

## 索引签名

### 定义

索引签名允许接口定义动态属性，用于描述对象可以具有任意数量的属性。

### 语法

```ts
interface InterfaceName {
    [key: string]: type;
    // 或
    [key: number]: type;
}
```

### 字符串索引签名

```ts
interface StringDictionary {
    [key: string]: string;
}

let dict: StringDictionary = {
    name: "John",
    city: "New York",
    country: "USA"
    // 可以添加任意字符串键
};
```

### 数字索引签名

```ts
interface NumberDictionary {
    [key: number]: string;
}

let arr: NumberDictionary = {
    0: "first",
    1: "second",
    2: "third"
    // 可以添加任意数字键
};
```

### 混合索引签名

可以同时使用字符串和数字索引签名：

```ts
interface MixedDictionary {
    [key: string]: string | number;
    [key: number]: string;
}

let mixed: MixedDictionary = {
    name: "John",
    age: 30,
    0: "first",
    1: "second"
};
```

### 与固定属性结合

索引签名可以与固定属性结合：

```ts
interface User {
    name: string;              // 固定属性
    age: number;               // 固定属性
    [key: string]: string | number; // 索引签名
}

let user: User = {
    name: "John",
    age: 30,
    email: "john@example.com", // 动态属性
    city: "New York"           // 动态属性
};
```

### 索引签名约束

索引签名的类型必须包含所有固定属性的类型：

```ts
// 错误：索引签名类型不包含固定属性类型
interface User {
    name: string;
    age: number;
    [key: string]: string; // 错误：age 是 number，但索引签名是 string
}

// 正确：索引签名类型包含所有固定属性类型
interface User2 {
    name: string;
    age: number;
    [key: string]: string | number; // 正确
}
```

## 只读索引签名

### 定义

索引签名可以标记为只读：

```ts
interface ReadOnlyDictionary {
    readonly [key: string]: string;
}

let dict: ReadOnlyDictionary = {
    name: "John",
    city: "New York"
};

// 错误：不能修改只读索引签名的属性
// dict.name = "Jane"; // 错误
```

## 使用场景

### 函数类型使用场景

1. **回调函数**：定义回调函数的类型

```ts
interface EventHandler {
    (event: Event): void;
}

function addEventListener(handler: EventHandler) {
    // ...
}
```

2. **函数库**：定义函数库的接口

```ts
interface MathLib {
    add(a: number, b: number): number;
    subtract(a: number, b: number): number;
    multiply(a: number, b: number): number;
}
```

### 索引签名使用场景

1. **配置对象**：动态配置项

```ts
interface Config {
    apiUrl: string;
    [key: string]: string | number | boolean;
}
```

2. **数据字典**：键值对数据

```ts
interface Dictionary {
    [key: string]: string;
}
```

3. **API 响应**：动态字段

```ts
interface ApiResponse {
    status: number;
    [key: string]: any;
}
```

## 常见错误

### 错误 1：索引签名类型不匹配

```ts
interface User {
    name: string;
    age: number;
    [key: string]: string; // 错误：age 是 number
}
```

### 错误 2：修改只读索引签名

```ts
interface Dict {
    readonly [key: string]: string;
}

let dict: Dict = { name: "John" };
// dict.name = "Jane"; // 错误
```

## 注意事项

1. **函数类型**：接口中的函数类型定义函数的签名
2. **索引签名**：索引签名允许动态属性
3. **类型约束**：索引签名类型必须包含所有固定属性类型
4. **只读索引**：索引签名可以标记为只读

## 最佳实践

1. **函数类型**：使用函数类型定义回调函数和函数库
2. **索引签名**：只在需要动态属性时使用索引签名
3. **类型安全**：确保索引签名类型包含所有固定属性类型
4. **只读保护**：对不应该修改的属性使用只读索引签名

## 练习

1. **函数类型**：定义函数接口，实现不同类型的函数。

2. **对象方法**：定义包含方法的接口，实现对象方法。

3. **索引签名**：定义使用索引签名的接口，添加动态属性。

4. **混合使用**：定义同时包含固定属性和索引签名的接口。

5. **实际应用**：在实际场景中应用函数类型和索引签名。

完成以上练习后，继续学习下一节，了解接口继承与合并。

## 总结

接口可以定义函数类型和索引签名。函数类型用于描述函数的签名，索引签名允许接口定义动态属性。理解函数类型和索引签名的使用，可以帮助我们定义更灵活的类型系统。

## 相关资源

- [TypeScript 函数类型文档](https://www.typescriptlang.org/docs/handbook/2/functions.html#function-types)
- [TypeScript 索引签名文档](https://www.typescriptlang.org/docs/handbook/2/objects.html#index-signatures)
