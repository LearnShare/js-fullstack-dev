# 4.1.2 泛型函数

## 概述

泛型函数允许在函数定义时使用类型参数，在使用时指定具体类型。本节介绍泛型函数的定义和使用。

## 泛型函数定义

### 基本语法

```ts
function functionName<T>(param: T): T {
    // 函数体
}
```

### 示例

```ts
// 基本泛型函数
function identity<T>(value: T): T {
    return value;
}

let result1 = identity<string>("Hello");
let result2 = identity<number>(42);
let result3 = identity<boolean>(true);
```

## 类型推断

### 自动推断

TypeScript 可以自动推断泛型类型：

```ts
function identity<T>(value: T): T {
    return value;
}

// 可以省略类型参数，TypeScript 会自动推断
let result1 = identity("Hello");  // T 推断为 string
let result2 = identity(42);      // T 推断为 number
let result3 = identity(true);    // T 推断为 boolean
```

### 显式指定

也可以显式指定类型参数：

```ts
function identity<T>(value: T): T {
    return value;
}

let result = identity<string>("Hello"); // 显式指定类型
```

## 多个类型参数

### 定义

泛型函数可以有多个类型参数：

```ts
function pair<T, U>(first: T, second: U): [T, U] {
    return [first, second];
}

let result = pair<string, number>("Hello", 42);
// result 的类型是 [string, number]
```

### 示例

```ts
function map<T, U>(arr: T[], fn: (item: T) => U): U[] {
    return arr.map(fn);
}

let numbers = [1, 2, 3];
let strings = map(numbers, (n) => n.toString());
// strings 的类型是 string[]
```

## 泛型函数表达式

### 函数表达式

```ts
const identity = function<T>(value: T): T {
    return value;
};
```

### 箭头函数

```ts
const identity = <T>(value: T): T => {
    return value;
};
```

## 泛型函数重载

### 定义

泛型函数可以重载：

```ts
function process<T>(value: T): T;
function process<T>(value: T[]): T[];
function process<T>(value: T | T[]): T | T[] {
    if (Array.isArray(value)) {
        return value;
    }
    return value;
}
```

## 使用场景

### 1. 数组操作

```ts
function getFirst<T>(arr: T[]): T | undefined {
    return arr[0];
}

function getLast<T>(arr: T[]): T | undefined {
    return arr[arr.length - 1];
}
```

### 2. 对象操作

```ts
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key];
}

let user = { name: "John", age: 30 };
let name = getProperty(user, "name"); // 类型为 string
```

### 3. 工具函数

```ts
function swap<T>(arr: T[], i: number, j: number): void {
    [arr[i], arr[j]] = [arr[j], arr[i]];
}
```

## 常见错误

### 错误 1：类型参数使用错误

```ts
// 错误：类型参数应该在函数名后
function identity(value: T): T {
    return value;
}

// 正确
function identity<T>(value: T): T {
    return value;
}
```

### 错误 2：类型推断失败

```ts
function process<T>(value: T): T {
    return value;
}

// 错误：无法推断类型
let result = process(null);
```

## 注意事项

1. **类型参数位置**：类型参数应该在函数名后
2. **类型推断**：TypeScript 可以自动推断类型参数
3. **多个参数**：可以有多个类型参数
4. **约束**：可以使用 extends 约束类型参数

## 最佳实践

1. **使用泛型**：在需要类型安全时使用泛型
2. **类型推断**：利用类型推断简化代码
3. **明确类型**：在类型推断失败时显式指定类型
4. **合理命名**：为类型参数使用有意义的名称

## 练习

1. **泛型函数**：定义不同类型的泛型函数。

2. **类型推断**：体验 TypeScript 的类型推断功能。

3. **多个参数**：定义使用多个类型参数的泛型函数。

4. **实际应用**：在实际场景中应用泛型函数。

完成以上练习后，继续学习下一节，了解泛型接口。

## 总结

泛型函数允许在函数定义时使用类型参数，在使用时指定具体类型。TypeScript 可以自动推断类型参数，也可以显式指定。理解泛型函数的定义和使用是学习 TypeScript 泛型的关键。

## 相关资源

- [TypeScript 泛型函数文档](https://www.typescriptlang.org/docs/handbook/2/generics.html#generic-functions)
