# 2.3.3 可选参数与默认参数

## 概述

TypeScript 支持可选参数和默认参数，提供更灵活的函数定义。本节介绍可选参数和默认参数的定义和使用。

## 可选参数

### 定义

可选参数使用 `?` 标记，表示该参数可以传递也可以不传递。

### 语法

```ts
function functionName(param1: type1, param2?: type2): returnType {
    // 函数体
}
```

### 示例

```ts
// 可选参数
function greet(name: string, title?: string): string {
    if (title) {
        return `Hello, ${title} ${name}!`;
    }
    return `Hello, ${name}!`;
}

greet("John");              // "Hello, John!"
greet("John", "Mr");        // "Hello, Mr John!"
```

### 可选参数类型

可选参数的类型是 `T | undefined`：

```ts
function process(value?: string) {
    // value 的类型是 string | undefined
    if (value !== undefined) {
        console.log(value.toUpperCase());
    }
}
```

### 多个可选参数

```ts
function createUser(name: string, age?: number, email?: string) {
    return {
        name,
        age: age ?? 0,
        email: email ?? ""
    };
}

createUser("John");
createUser("John", 30);
createUser("John", 30, "john@example.com");
```

## 默认参数

### 定义

默认参数在参数后使用 `=` 指定默认值，当参数未传递时使用默认值。

### 语法

```ts
function functionName(param1: type1, param2: type2 = defaultValue): returnType {
    // 函数体
}
```

### 示例

```ts
// 默认参数
function greet(name: string, title: string = "Mr"): string {
    return `Hello, ${title} ${name}!`;
}

greet("John");              // "Hello, Mr John!"
greet("John", "Dr");        // "Hello, Dr John!"
```

### 默认参数类型推断

TypeScript 可以根据默认值推断参数类型：

```ts
// 推断 title 为 string 类型
function greet(name: string, title = "Mr") {
    return `Hello, ${title} ${name}!`;
}
```

### 表达式作为默认值

```ts
function createId(prefix: string = "ID", timestamp: number = Date.now()) {
    return `${prefix}-${timestamp}`;
}
```

### 函数调用作为默认值

```ts
function getDefaultName() {
    return "Guest";
}

function greet(name: string = getDefaultName()) {
    return `Hello, ${name}!`;
}
```

## 可选参数 vs 默认参数

### 区别

| 特性       | 可选参数（?）            | 默认参数（=）            |
|:-----------|:-------------------------|:-------------------------|
| 语法       | `param?: type`           | `param: type = value`    |
| 类型       | `T | undefined`         | `T`                      |
| 默认值     | `undefined`              | 指定的默认值             |
| 使用场景   | 参数可能不存在           | 参数有合理的默认值       |

### 示例对比

```ts
// 可选参数
function greet1(name: string, title?: string) {
    // title 的类型是 string | undefined
    return title ? `Hello, ${title} ${name}!` : `Hello, ${name}!`;
}

// 默认参数
function greet2(name: string, title: string = "Mr") {
    // title 的类型是 string
    return `Hello, ${title} ${name}!`;
}
```

## 参数顺序

### 规则

可选参数和默认参数必须放在必需参数之后：

```ts
// 正确：可选参数在最后
function greet(name: string, title?: string) {
    // ...
}

// 错误：可选参数不能在必需参数之前
function greet(title?: string, name: string) {
    // 错误
}
```

### 多个可选/默认参数

```ts
// 所有可选参数
function createUser(name: string, age?: number, email?: string) {
    // ...
}

// 混合使用
function process(data: string, options?: object, callback?: () => void) {
    // ...
}
```

## 使用场景

### 可选参数使用场景

1. **配置对象**

```ts
function fetchData(url: string, options?: RequestInit) {
    // ...
}
```

2. **回调函数**

```ts
function process(data: any, callback?: (result: any) => void) {
    // ...
}
```

### 默认参数使用场景

1. **默认配置**

```ts
function createConfig(apiUrl: string, timeout: number = 5000) {
    // ...
}
```

2. **默认值**

```ts
function greet(name: string, greeting: string = "Hello") {
    return `${greeting}, ${name}!`;
}
```

## 常见错误

### 错误 1：可选参数在必需参数之前

```ts
// 错误：可选参数不能在必需参数之前
function greet(title?: string, name: string) {
    // 错误
}
```

### 错误 2：访问可选参数未检查

```ts
function process(value?: string) {
    // 错误：可能为 undefined
    console.log(value.toUpperCase()); // 错误
}
```

## 注意事项

1. **参数顺序**：可选参数和默认参数必须在必需参数之后
2. **类型检查**：访问可选参数前需要进行类型检查
3. **默认值类型**：TypeScript 可以根据默认值推断参数类型
4. **选择原则**：根据实际需求选择可选参数或默认参数

## 最佳实践

1. **使用默认参数**：当参数有合理的默认值时使用默认参数
2. **使用可选参数**：当参数可能不存在时使用可选参数
3. **类型检查**：访问可选参数前进行类型检查
4. **参数顺序**：保持参数顺序的合理性

## 练习

1. **可选参数**：定义包含可选参数的函数，练习使用。

2. **默认参数**：定义包含默认参数的函数，理解默认值的作用。

3. **类型检查**：练习访问可选参数时的类型检查。

4. **参数顺序**：理解可选参数和默认参数的顺序要求。

5. **实际应用**：在实际场景中应用可选参数和默认参数。

完成以上练习后，继续学习下一节，了解剩余参数与函数重载。

## 总结

可选参数和默认参数提供了更灵活的函数定义。可选参数使用 `?` 标记，类型为 `T | undefined`。默认参数使用 `=` 指定默认值，类型为 `T`。理解可选参数和默认参数的区别和使用场景，可以帮助我们更好地设计函数接口。

## 相关资源

- [TypeScript 可选参数文档](https://www.typescriptlang.org/docs/handbook/2/functions.html#optional-parameters)
- [TypeScript 默认参数文档](https://www.typescriptlang.org/docs/handbook/2/functions.html#default-parameters)
