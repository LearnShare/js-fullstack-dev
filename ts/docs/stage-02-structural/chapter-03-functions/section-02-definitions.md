# 2.3.2 函数类型定义

## 概述

本节介绍函数类型的各种定义方式，包括函数声明、函数表达式、箭头函数和函数类型别名。

## 函数声明

### 基本语法

```ts
function functionName(param1: type1, param2: type2): returnType {
    // 函数体
}
```

### 示例

```ts
// 函数声明
function add(a: number, b: number): number {
    return a + b;
}

// 使用
let result: number = add(1, 2);
```

### 无返回值

```ts
function log(message: string): void {
    console.log(message);
}
```

## 函数表达式

### 基本语法

```ts
const functionName = function(param1: type1, param2: type2): returnType {
    // 函数体
};
```

### 示例

```ts
// 函数表达式
const add = function(a: number, b: number): number {
    return a + b;
};

// 使用
let result: number = add(1, 2);
```

### 类型注解

```ts
// 显式类型注解
const add: (a: number, b: number) => number = function(a, b) {
    return a + b;
};
```

## 箭头函数

### 基本语法

```ts
const functionName = (param1: type1, param2: type2): returnType => {
    // 函数体
};
```

### 示例

```ts
// 箭头函数
const add = (a: number, b: number): number => {
    return a + b;
};

// 简写（单表达式）
const multiply = (a: number, b: number): number => a * b;
```

### 类型注解

```ts
// 显式类型注解
const add: (a: number, b: number) => number = (a, b) => {
    return a + b;
};
```

## 函数类型别名

### 使用 type

```ts
// 定义函数类型别名
type AddFunction = (a: number, b: number) => number;

// 使用类型别名
const add: AddFunction = function(a, b) {
    return a + b;
};

// 或使用箭头函数
const add2: AddFunction = (a, b) => a + b;
```

### 使用 interface

```ts
// 定义函数接口
interface AddFunction {
    (a: number, b: number): number;
}

// 使用接口
const add: AddFunction = function(a, b) {
    return a + b;
};
```

## 方法定义

### 对象方法

```ts
const calculator = {
    add(a: number, b: number): number {
        return a + b;
    },
    multiply(a: number, b: number): number {
        return a * b;
    }
};
```

### 类方法

```ts
class Calculator {
    add(a: number, b: number): number {
        return a + b;
    }
    
    multiply(a: number, b: number): number {
        return a * b;
    }
}
```

## 函数类型推断

### 自动推断

TypeScript 可以自动推断函数类型：

```ts
// 推断返回值为 number
function add(a: number, b: number) {
    return a + b;
}

// 推断为 (a: number, b: number) => number
const multiply = (a: number, b: number) => a * b;
```

### 显式注解

建议为函数参数和返回值添加显式类型注解：

```ts
// 推荐：显式类型注解
function add(a: number, b: number): number {
    return a + b;
}
```

## 常见错误

### 错误 1：参数类型不匹配

```ts
function add(a: number, b: number): number {
    return a + b;
}

// 错误：参数类型不匹配
add("1", "2"); // 错误
```

### 错误 2：返回值类型不匹配

```ts
function add(a: number, b: number): number {
    return "result"; // 错误：返回值类型不匹配
}
```

## 注意事项

1. **参数类型**：函数参数应该添加类型注解
2. **返回值类型**：函数返回值应该添加类型注解（void 也需要）
3. **类型推断**：TypeScript 可以推断函数类型，但建议显式注解
4. **函数类型别名**：对于复用的函数类型，使用类型别名

## 最佳实践

1. **显式类型注解**：为函数参数和返回值添加显式类型注解
2. **使用类型别名**：对于复用的函数类型使用类型别名
3. **保持一致性**：在项目中保持函数定义的一致性
4. **明确返回值**：明确函数的返回值类型

## 练习

1. **函数声明**：使用函数声明定义不同类型的函数。

2. **函数表达式**：使用函数表达式定义函数，练习类型注解。

3. **箭头函数**：使用箭头函数定义函数，对比与函数表达式的区别。

4. **函数类型别名**：定义函数类型别名，在多个地方使用。

5. **类型推断**：观察 TypeScript 如何推断函数类型。

完成以上练习后，继续学习下一节，了解可选参数与默认参数。

## 总结

函数类型有多种定义方式，包括函数声明、函数表达式、箭头函数和函数类型别名。理解各种定义方式的区别和使用场景，可以帮助我们更好地使用 TypeScript 的函数类型系统。

## 相关资源

- [TypeScript 函数类型文档](https://www.typescriptlang.org/docs/handbook/2/functions.html#function-types)
