# 2.3.5 函数签名类型

## 概述

函数签名类型是用于描述函数类型的类型，可以在接口、类型别名等地方使用。本节介绍函数签名类型的定义和使用。

## 函数签名类型

### 定义

函数签名类型描述函数的类型，包括参数类型和返回值类型。

### 语法

```ts
type FunctionType = (param1: type1, param2: type2) => returnType;
```

### 示例

```ts
// 函数签名类型
type AddFunction = (a: number, b: number) => number;

// 使用函数签名类型
let add: AddFunction = function(a, b) {
    return a + b;
};
```

## 在接口中使用

### 定义

接口中可以定义函数签名类型：

```ts
interface Calculator {
    add: (a: number, b: number) => number;
    subtract: (a: number, b: number) => number;
    multiply: (a: number, b: number) => number;
}
```

### 使用

```ts
let calculator: Calculator = {
    add: (a, b) => a + b,
    subtract: (a, b) => a - b,
    multiply: (a, b) => a * b
};
```

### 方法简写

接口中可以使用方法简写：

```ts
interface Calculator {
    add(a: number, b: number): number;
    subtract(a: number, b: number): number;
    multiply(a: number, b: number): number;
}
```

## 在类型别名中使用

### 定义

类型别名中可以定义函数签名类型：

```ts
type EventHandler = (event: Event) => void;
type Callback = (error: Error | null, data: any) => void;
```

### 使用

```ts
function addEventListener(handler: EventHandler) {
    // ...
}

function fetchData(callback: Callback) {
    // ...
}
```

## 函数签名类型参数

### 参数名称

函数签名类型中的参数名称可以省略：

```ts
// 有参数名称
type Handler = (event: Event) => void;

// 无参数名称（也可以）
type Handler2 = (Event) => void; // 不推荐
```

### 可选参数

函数签名类型支持可选参数：

```ts
type Handler = (event: Event, options?: object) => void;
```

### 剩余参数

函数签名类型支持剩余参数：

```ts
type SumFunction = (...numbers: number[]) => number;
```

## 函数签名类型推断

### 自动推断

TypeScript 可以自动推断函数签名类型：

```ts
// 推断为 (a: number, b: number) => number
const add = (a: number, b: number) => a + b;
```

### 显式注解

建议为函数签名类型添加显式注解：

```ts
type AddFunction = (a: number, b: number) => number;

const add: AddFunction = (a, b) => a + b;
```

## 函数签名类型组合

### 联合类型

函数签名类型可以使用联合类型：

```ts
type Handler = ((event: MouseEvent) => void) | ((event: KeyboardEvent) => void);
```

### 交叉类型

函数签名类型可以使用交叉类型（通常不适用）：

```ts
// 交叉类型通常不适用于函数签名
type A = (x: number) => number;
type B = (x: string) => string;
type AB = A & B; // 实际上不可用
```

## 使用场景

### 1. 回调函数

函数签名类型常用于定义回调函数：

```ts
type Callback = (result: any) => void;

function process(callback: Callback) {
    // ...
}
```

### 2. 事件处理

函数签名类型可以定义事件处理函数：

```ts
type EventHandler = (event: Event) => void;

function addEventListener(type: string, handler: EventHandler) {
    // ...
}
```

### 3. 函数库接口

函数签名类型可以定义函数库的接口：

```ts
interface MathLib {
    add: (a: number, b: number) => number;
    subtract: (a: number, b: number) => number;
}
```

## 常见错误

### 错误 1：函数签名类型不匹配

```ts
type Handler = (event: Event) => void;

// 错误：参数类型不匹配
let handler: Handler = (e: MouseEvent) => {
    // 错误
};
```

### 错误 2：返回值类型不匹配

```ts
type AddFunction = (a: number, b: number) => number;

// 错误：返回值类型不匹配
let add: AddFunction = (a, b) => {
    return "result"; // 错误
};
```

## 注意事项

1. **函数签名类型是类型**：函数签名类型只在编译时存在
2. **参数名称可选**：函数签名类型中的参数名称可以省略
3. **类型兼容**：函数签名类型遵循类型兼容规则
4. **支持复杂参数**：函数签名类型支持可选参数和剩余参数

## 最佳实践

1. **使用函数签名类型**：对于复用的函数类型使用函数签名类型
2. **明确类型**：为函数签名类型添加明确的类型注解
3. **合理命名**：使用清晰的函数签名类型名称
4. **保持简洁**：函数签名类型应该简洁明了

## 练习

1. **函数签名类型定义**：定义不同类型的函数签名类型。

2. **接口中使用**：在接口中定义函数签名类型。

3. **类型别名中使用**：在类型别名中定义函数签名类型。

4. **回调函数**：使用函数签名类型定义回调函数。

5. **实际应用**：在实际场景中应用函数签名类型。

完成以上练习后，函数类型章节学习完成。阶段二学习完成，可以继续学习阶段三：面向对象与类。

## 总结

函数签名类型是用于描述函数类型的类型，可以在接口、类型别名等地方使用。函数签名类型支持可选参数、剩余参数等复杂参数。理解函数签名类型的定义和使用，可以帮助我们更好地设计函数接口。

## 相关资源

- [TypeScript 函数签名类型文档](https://www.typescriptlang.org/docs/handbook/2/functions.html#function-types)
