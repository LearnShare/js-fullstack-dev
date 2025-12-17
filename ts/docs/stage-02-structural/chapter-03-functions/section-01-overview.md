# 2.3.1 函数类型概述

## 概述

函数类型是 TypeScript 中用于描述函数签名的类型，包括参数类型和返回值类型。本节介绍函数类型的概念、作用和优势。

## 什么是函数类型

### 定义

函数类型描述函数的签名，包括参数类型和返回值类型。

### 基本概念

```ts
// 函数类型
type AddFunction = (a: number, b: number) => number;

// 使用函数类型
let add: AddFunction = function(a, b) {
    return a + b;
};
```

## 函数类型的作用

### 1. 类型检查

函数类型提供参数和返回值的类型检查：

```ts
type Calculator = (a: number, b: number) => number;

let add: Calculator = function(a, b) {
    return a + b;
};

// 类型检查
add(1, 2);        // 正确
add("1", "2");    // 错误：参数类型不匹配
```

### 2. 代码文档

函数类型作为代码文档，清楚地说明函数的签名：

```ts
type EventHandler = (event: Event) => void;

// 函数类型清楚地说明了参数和返回值
function addEventListener(handler: EventHandler) {
    // ...
}
```

### 3. IDE 支持

函数类型提供更好的 IDE 支持：

```ts
type Handler = (name: string, age: number) => void;

let handler: Handler = function(name, age) {
    // IDE 会提供参数提示
    console.log(name, age);
};
```

### 4. 重构安全

函数类型使重构更安全：

```ts
type Handler = (name: string) => void;

// 修改函数类型时，所有使用的地方都会提示错误
type Handler = (name: string, age: number) => void; // 添加参数
```

## 函数类型的优势

### 1. 类型安全

函数类型提供编译时类型检查：

```ts
type AddFunction = (a: number, b: number) => number;

let add: AddFunction = function(a, b) {
    return a + b;
};

// 编译时检查
add(1, 2);     // 正确
add("1", "2"); // 错误
```

### 2. 代码复用

函数类型可以复用：

```ts
type Handler = (event: Event) => void;

function addClickHandler(handler: Handler) {
    // ...
}

function addKeyHandler(handler: Handler) {
    // ...
}
```

### 3. 灵活性

函数类型支持多种定义方式：

```ts
// 类型别名
type Handler = (event: Event) => void;

// 接口
interface Handler {
    (event: Event): void;
}

// 内联
function process(handler: (event: Event) => void) {
    // ...
}
```

## 函数类型 vs 函数声明

### 函数声明

```ts
function add(a: number, b: number): number {
    return a + b;
}
```

### 函数类型

```ts
type AddFunction = (a: number, b: number) => number;

let add: AddFunction = function(a, b) {
    return a + b;
};
```

### 区别

| 特性       | 函数声明           | 函数类型           |
|:-----------|:-------------------|:-------------------|
| 定义方式   | `function` 关键字   | 类型定义           |
| 使用场景   | 定义函数           | 描述函数签名       |
| 类型检查   | 有                 | 有                 |
| 复用性     | 低                 | 高                 |

## 使用场景

### 1. 回调函数

函数类型常用于定义回调函数：

```ts
type Callback = (error: Error | null, data: any) => void;

function fetchData(callback: Callback) {
    // ...
}
```

### 2. 函数库

函数类型可以定义函数库的接口：

```ts
type MathLib = {
    add: (a: number, b: number) => number;
    subtract: (a: number, b: number) => number;
    multiply: (a: number, b: number) => number;
};
```

### 3. 事件处理

函数类型可以定义事件处理函数：

```ts
type EventHandler = (event: Event) => void;

function addEventListener(type: string, handler: EventHandler) {
    // ...
}
```

## 注意事项

1. **函数类型是类型**：函数类型只在编译时存在
2. **参数名称**：函数类型中的参数名称可以省略
3. **返回值类型**：函数类型必须指定返回值类型（void 也需要）
4. **类型兼容**：函数类型遵循类型兼容规则

## 最佳实践

1. **明确类型**：为函数参数和返回值添加明确的类型
2. **使用函数类型**：对于回调函数和函数库使用函数类型
3. **复用类型**：在多个地方使用的函数签名定义类型别名
4. **保持简洁**：函数类型应该简洁明了

## 练习

1. **函数类型定义**：定义不同类型的函数类型，理解其用法。

2. **回调函数**：使用函数类型定义回调函数。

3. **函数库**：使用函数类型定义函数库的接口。

4. **类型检查**：体验函数类型的类型检查功能。

5. **实际应用**：在实际场景中应用函数类型。

完成以上练习后，继续学习下一节，了解函数类型定义。

## 总结

函数类型是 TypeScript 中用于描述函数签名的类型。函数类型提供类型检查、代码文档、IDE 支持和重构安全等优势。理解函数类型的概念和作用是学习 TypeScript 类型系统的关键。

## 相关资源

- [TypeScript 函数类型文档](https://www.typescriptlang.org/docs/handbook/2/functions.html#function-types)
