# 3.3.4 装饰器（Decorators）

## 概述

装饰器是一种特殊类型的声明，可以附加到类、方法、属性、参数等上，提供元编程能力。本节介绍装饰器的基本概念和使用。

## 什么是装饰器

### 定义

装饰器是一种设计模式，允许在不修改原代码的情况下增强功能。

### 基本概念

```ts
// 装饰器函数
function logged(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    const original = descriptor.value;
    descriptor.value = function(...args: any[]) {
        console.log(`Calling ${propertyKey}`);
        return original.apply(this, args);
    };
}

// 使用装饰器
class Calculator {
    @logged
    add(a: number, b: number): number {
        return a + b;
    }
}
```

## 装饰器类型

### 类装饰器

类装饰器应用于类：

```ts
function sealed(constructor: Function) {
    Object.seal(constructor);
    Object.seal(constructor.prototype);
}

@sealed
class Greeter {
    greeting: string;
    constructor(message: string) {
        this.greeting = message;
    }
}
```

### 方法装饰器

方法装饰器应用于方法：

```ts
function logged(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    const original = descriptor.value;
    descriptor.value = function(...args: any[]) {
        console.log(`Calling ${propertyKey}`);
        return original.apply(this, args);
    };
}

class Calculator {
    @logged
    add(a: number, b: number): number {
        return a + b;
    }
}
```

### 属性装饰器

属性装饰器应用于属性：

```ts
function format(target: any, propertyKey: string) {
    // 属性装饰器逻辑
}

class User {
    @format
    name: string;
}
```

### 参数装饰器

参数装饰器应用于参数：

```ts
function validate(target: any, propertyKey: string, parameterIndex: number) {
    // 参数装饰器逻辑
}

class User {
    create(@validate name: string) {
        // ...
    }
}
```

## 装饰器配置

### 启用装饰器

在 `tsconfig.json` 中启用装饰器：

```json
{
  "compilerOptions": {
    "experimentalDecorators": true
  }
}
```

### TypeScript 5.0+ 装饰器

TypeScript 5.0+ 支持新的装饰器标准：

```json
{
  "compilerOptions": {
    "experimentalDecorators": true,
    "emitDecoratorMetadata": true
  }
}
```

## 装饰器执行顺序

### 执行顺序

装饰器的执行顺序：

1. 参数装饰器
2. 方法/属性装饰器
3. 类装饰器

### 示例

```ts
function classDecorator(constructor: Function) {
    console.log("Class decorator");
}

function methodDecorator(target: any, propertyKey: string) {
    console.log("Method decorator");
}

@classDecorator
class Example {
    @methodDecorator
    method() {
        // ...
    }
}
```

## 使用场景

### 1. 日志记录

```ts
function log(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    const original = descriptor.value;
    descriptor.value = function(...args: any[]) {
        console.log(`Calling ${propertyKey} with`, args);
        const result = original.apply(this, args);
        console.log(`Result:`, result);
        return result;
    };
}
```

### 2. 性能监控

```ts
function measure(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    const original = descriptor.value;
    descriptor.value = function(...args: any[]) {
        const start = performance.now();
        const result = original.apply(this, args);
        const end = performance.now();
        console.log(`${propertyKey} took ${end - start}ms`);
        return result;
    };
}
```

### 3. 验证

```ts
function validate(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    const original = descriptor.value;
    descriptor.value = function(...args: any[]) {
        // 验证逻辑
        return original.apply(this, args);
    };
}
```

## 常见错误

### 错误 1：未启用装饰器

```ts
// 错误：需要启用 experimentalDecorators
@logged
class Example {
    // ...
}
```

### 错误 2：装饰器参数错误

```ts
// 错误：装饰器参数不正确
function decorator(wrong: any) {
    // 错误
}
```

## 注意事项

1. **启用配置**：需要启用 `experimentalDecorators`
2. **执行顺序**：理解装饰器的执行顺序
3. **TypeScript 版本**：不同版本的装饰器语法可能不同
4. **运行时支持**：某些装饰器需要运行时支持

## 最佳实践

1. **合理使用**：在合适的情况下使用装饰器
2. **明确意图**：使用装饰器明确表达意图
3. **避免过度**：避免过度使用装饰器
4. **版本兼容**：注意 TypeScript 版本要求

## 练习

1. **装饰器定义**：定义不同类型的装饰器。

2. **装饰器使用**：在类、方法、属性上使用装饰器。

3. **执行顺序**：理解装饰器的执行顺序。

4. **实际应用**：在实际场景中应用装饰器。

5. **配置检查**：检查装饰器的配置是否正确。

完成以上练习后，继续学习下一节，了解装饰器深入。

## 总结

装饰器是一种特殊类型的声明，可以附加到类、方法、属性等上。装饰器提供元编程能力，可以增强类的功能。理解装饰器的基本概念和使用是学习 TypeScript 高级特性的关键。

## 相关资源

- [TypeScript 装饰器文档](https://www.typescriptlang.org/docs/handbook/decorators.html)
