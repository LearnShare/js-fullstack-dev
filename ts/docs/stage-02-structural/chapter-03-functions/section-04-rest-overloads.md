# 2.3.4 剩余参数与函数重载

## 概述

剩余参数允许函数接收不定数量的参数，函数重载允许为同一个函数定义多个签名。本节介绍剩余参数和函数重载的定义和使用。

## 剩余参数

### 定义

剩余参数使用 `...` 语法，将多个参数收集到一个数组中。

### 语法

```ts
function functionName(...rest: type[]): returnType {
    // 函数体
}
```

### 示例

```ts
// 剩余参数
function sum(...numbers: number[]): number {
    return numbers.reduce((acc, n) => acc + n, 0);
}

sum(1, 2, 3);           // 6
sum(1, 2, 3, 4, 5);     // 15
sum();                  // 0
```

### 与其他参数组合

剩余参数必须放在最后：

```ts
function greet(greeting: string, ...names: string[]): string {
    return `${greeting}, ${names.join(", ")}!`;
}

greet("Hello", "John", "Jane", "Bob");
// "Hello, John, Jane, Bob!"
```

### 类型注解

剩余参数的类型必须是数组类型：

```ts
// 正确
function process(...items: string[]): void {
    // ...
}

// 错误：不是数组类型
function process(...item: string): void {
    // 错误
}
```

## 函数重载

### 定义

函数重载允许为同一个函数定义多个签名，根据参数类型和数量选择不同的实现。

### 语法

```ts
// 重载签名
function functionName(param1: type1): returnType1;
function functionName(param1: type1, param2: type2): returnType2;

// 实现签名
function functionName(param1: type1, param2?: type2): returnType1 | returnType2 {
    // 实现
}
```

### 示例

```ts
// 函数重载
function process(value: string): string;
function process(value: number): number;
function process(value: string | number): string | number {
    if (typeof value === "string") {
        return value.toUpperCase();
    } else {
        return value * 2;
    }
}

process("hello");  // "HELLO"
process(10);       // 20
```

### 多个重载

```ts
// 多个重载
function createUser(name: string): User;
function createUser(name: string, age: number): User;
function createUser(name: string, age?: number): User {
    return {
        name,
        age: age ?? 0
    };
}
```

### 重载顺序

重载签名必须按照从具体到抽象的顺序：

```ts
// 正确：从具体到抽象
function process(value: string): string;
function process(value: number): number;
function process(value: string | number): string | number {
    // ...
}

// 错误：顺序错误
function process(value: string | number): string | number;
function process(value: string): string;
// 错误：更具体的签名应该在前面
```

## 剩余参数 vs 函数重载

### 区别

| 特性       | 剩余参数                 | 函数重载                 |
|:-----------|:-------------------------|:-------------------------|
| 语法       | `...rest: type[]`        | 多个函数签名             |
| 参数数量   | 不定                     | 固定（多个签名）         |
| 类型       | 数组类型                 | 多种类型                 |
| 使用场景   | 参数数量不定             | 参数类型或数量不同       |

### 选择建议

- **参数数量不定**：使用剩余参数
- **参数类型不同**：使用函数重载
- **参数数量固定但类型不同**：使用函数重载

## 使用场景

### 剩余参数使用场景

1. **求和函数**

```ts
function sum(...numbers: number[]): number {
    return numbers.reduce((acc, n) => acc + n, 0);
}
```

2. **日志函数**

```ts
function log(...messages: string[]): void {
    console.log(messages.join(" "));
}
```

### 函数重载使用场景

1. **不同类型处理**

```ts
function parse(value: string): string;
function parse(value: number): number;
function parse(value: string | number): string | number {
    // ...
}
```

2. **不同参数数量**

```ts
function create(config: string): User;
function create(name: string, age: number): User;
function create(configOrName: string, age?: number): User {
    // ...
}
```

## 常见错误

### 错误 1：剩余参数不在最后

```ts
// 错误：剩余参数必须在最后
function process(...items: string[], last: string) {
    // 错误
}
```

### 错误 2：重载签名顺序错误

```ts
// 错误：更具体的签名应该在前面
function process(value: string | number): string | number;
function process(value: string): string;
// 错误
```

## 注意事项

1. **剩余参数位置**：剩余参数必须放在参数列表的最后
2. **重载顺序**：函数重载必须按照从具体到抽象的顺序
3. **实现签名**：函数重载必须有实现签名
4. **类型兼容**：重载签名的返回类型应该兼容

## 最佳实践

1. **使用剩余参数**：当参数数量不定时使用剩余参数
2. **使用函数重载**：当参数类型或数量不同时使用函数重载
3. **保持顺序**：函数重载保持从具体到抽象的顺序
4. **明确类型**：为剩余参数和重载签名添加明确的类型

## 练习

1. **剩余参数**：定义使用剩余参数的函数，练习使用。

2. **函数重载**：定义函数重载，理解重载的工作原理。

3. **参数组合**：练习剩余参数与其他参数的组合使用。

4. **重载顺序**：理解函数重载的顺序要求。

5. **实际应用**：在实际场景中应用剩余参数和函数重载。

完成以上练习后，继续学习下一节，了解函数签名类型。

## 总结

剩余参数和函数重载提供了更灵活的函数定义。剩余参数使用 `...` 语法收集多个参数，函数重载允许为同一个函数定义多个签名。理解剩余参数和函数重载的使用场景，可以帮助我们更好地设计函数接口。

## 相关资源

- [TypeScript 剩余参数文档](https://www.typescriptlang.org/docs/handbook/2/functions.html#rest-parameters)
- [TypeScript 函数重载文档](https://www.typescriptlang.org/docs/handbook/2/functions.html#function-overloads)
