# 3.3.5 装饰器深入

## 概述

本节深入介绍装饰器的高级用法，包括装饰器工厂、装饰器组合、装饰器参数等。

## 装饰器工厂

### 定义

装饰器工厂是返回装饰器函数的函数，允许传递参数。

### 语法

```ts
function decoratorFactory(...args: any[]) {
    return function(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
        // 装饰器逻辑
    };
}
```

### 示例

```ts
// 装饰器工厂
function logged(message: string) {
    return function(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
        const original = descriptor.value;
        descriptor.value = function(...args: any[]) {
            console.log(message);
            return original.apply(this, args);
        };
    };
}

class Calculator {
    @logged("Adding numbers")
    add(a: number, b: number): number {
        return a + b;
    }
}
```

## 装饰器组合

### 多个装饰器

可以同时使用多个装饰器：

```ts
class Example {
    @decorator1
    @decorator2
    @decorator3
    method() {
        // ...
    }
}
```

### 执行顺序

多个装饰器的执行顺序是从下到上：

```ts
function first() {
    console.log("first");
    return function(target: any, propertyKey: string) {
        console.log("first applied");
    };
}

function second() {
    console.log("second");
    return function(target: any, propertyKey: string) {
        console.log("second applied");
    };
}

class Example {
    @first()
    @second()
    method() {
        // ...
    }
}

// 输出：
// "second"
// "first"
// "second applied"
// "first applied"
```

## 装饰器参数

### 类装饰器参数

类装饰器接收构造函数：

```ts
function classDecorator(constructor: Function) {
    // 可以修改构造函数
}
```

### 方法装饰器参数

方法装饰器接收目标对象、属性名和属性描述符：

```ts
function methodDecorator(
    target: any,
    propertyKey: string,
    descriptor: PropertyDescriptor
) {
    // target: 类的原型
    // propertyKey: 方法名
    // descriptor: 属性描述符
}
```

### 属性装饰器参数

属性装饰器接收目标对象和属性名：

```ts
function propertyDecorator(target: any, propertyKey: string) {
    // target: 类的原型
    // propertyKey: 属性名
}
```

## 装饰器返回值

### 方法装饰器返回值

方法装饰器可以返回新的属性描述符：

```ts
function readonly(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    descriptor.writable = false;
    return descriptor;
}
```

### 类装饰器返回值

类装饰器可以返回新的构造函数：

```ts
function classDecorator<T extends { new (...args: any[]): {} }>(constructor: T) {
    return class extends constructor {
        newProperty = "new";
    };
}
```

## 使用场景

### 1. 依赖注入

```ts
function inject(dependency: any) {
    return function(target: any, propertyKey: string) {
        // 依赖注入逻辑
    };
}
```

### 2. 路由装饰器

```ts
function route(path: string) {
    return function(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
        // 路由注册逻辑
    };
}
```

### 3. 验证装饰器

```ts
function validate(rules: ValidationRule[]) {
    return function(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
        // 验证逻辑
    };
}
```

## 常见错误

### 错误 1：装饰器参数错误

```ts
// 错误：装饰器参数不正确
function decorator(wrong: any) {
    // 错误
}
```

### 错误 2：装饰器返回值错误

```ts
// 错误：返回值类型不正确
function decorator(target: any, propertyKey: string) {
    return "wrong"; // 错误
}
```

## 注意事项

1. **参数类型**：装饰器参数类型必须正确
2. **执行顺序**：多个装饰器从下到上执行
3. **返回值**：装饰器可以返回新的描述符或构造函数
4. **版本兼容**：注意 TypeScript 版本要求

## 最佳实践

1. **使用工厂**：使用装饰器工厂传递参数
2. **明确顺序**：理解装饰器的执行顺序
3. **合理组合**：合理组合多个装饰器
4. **类型安全**：为装饰器添加类型注解

## 练习

1. **装饰器工厂**：创建装饰器工厂，传递参数。

2. **装饰器组合**：组合使用多个装饰器。

3. **执行顺序**：理解装饰器的执行顺序。

4. **返回值**：使用装饰器返回值修改行为。

5. **实际应用**：在实际场景中应用装饰器。

完成以上练习后，继续学习下一节，了解装饰器元数据。

## 总结

装饰器工厂允许传递参数，装饰器可以组合使用。理解装饰器的高级用法，可以帮助我们更好地使用装饰器增强类的功能。

## 相关资源

- [TypeScript 装饰器文档](https://www.typescriptlang.org/docs/handbook/decorators.html)
