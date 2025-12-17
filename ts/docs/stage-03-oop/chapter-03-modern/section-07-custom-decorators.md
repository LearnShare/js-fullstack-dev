# 3.3.7 自定义装饰器

## 概述

自定义装饰器允许我们创建自己的装饰器函数，实现特定的功能。本节介绍如何创建和使用自定义装饰器。

## 创建自定义装饰器

### 基本步骤

1. 定义装饰器函数
2. 实现装饰器逻辑
3. 应用装饰器

### 示例

```ts
// 定义装饰器
function logged(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    const original = descriptor.value;
    descriptor.value = function(...args: any[]) {
        console.log(`Calling ${propertyKey} with`, args);
        const result = original.apply(this, args);
        console.log(`Result:`, result);
        return result;
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

## 日志装饰器

### 实现

```ts
function log(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    const original = descriptor.value;
    descriptor.value = function(...args: any[]) {
        console.log(`[LOG] ${propertyKey} called with:`, args);
        try {
            const result = original.apply(this, args);
            console.log(`[LOG] ${propertyKey} returned:`, result);
            return result;
        } catch (error) {
            console.error(`[LOG] ${propertyKey} threw:`, error);
            throw error;
        }
    };
}
```

## 性能监控装饰器

### 实现

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

## 验证装饰器

### 实现

```ts
function validate(rules: ValidationRule[]) {
    return function(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
        const original = descriptor.value;
        descriptor.value = function(...args: any[]) {
            // 验证逻辑
            for (const rule of rules) {
                if (!rule.validate(args[rule.index])) {
                    throw new Error(rule.message);
                }
            }
            return original.apply(this, args);
        };
    };
}
```

## 只读装饰器

### 实现

```ts
function readonly(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    descriptor.writable = false;
    return descriptor;
}
```

## 缓存装饰器

### 实现

```ts
function cache(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    const original = descriptor.value;
    const cache = new Map();

    descriptor.value = function(...args: any[]) {
        const key = JSON.stringify(args);
        if (cache.has(key)) {
            return cache.get(key);
        }
        const result = original.apply(this, args);
        cache.set(key, result);
        return result;
    };
}
```

## 装饰器组合

### 组合使用

可以组合多个装饰器：

```ts
class Calculator {
    @log
    @measure
    @cache
    expensiveCalculation(n: number): number {
        // 复杂计算
        return n * n;
    }
}
```

## 使用场景

### 1. 日志记录

```ts
@log
class Service {
    @log
    process(data: any) {
        // ...
    }
}
```

### 2. 性能监控

```ts
@measure
class ApiService {
    @measure
    fetchData() {
        // ...
    }
}
```

### 3. 验证

```ts
class UserService {
    @validate([
        { index: 0, validate: (v) => typeof v === 'string', message: 'Name must be string' }
    ])
    createUser(name: string) {
        // ...
    }
}
```

## 常见错误

### 错误 1：装饰器参数错误

```ts
// 错误：参数类型不正确
function decorator(wrong: any) {
    // 错误
}
```

### 错误 2：未保存原始方法

```ts
// 错误：未保存原始方法
function decorator(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    descriptor.value = function() {
        // 无法调用原始方法
    };
}
```

## 注意事项

1. **保存原始方法**：装饰器应该保存原始方法
2. **正确参数**：装饰器参数类型必须正确
3. **返回值**：方法装饰器可以返回新的描述符
4. **执行顺序**：理解装饰器的执行顺序

## 最佳实践

1. **保存原始方法**：始终保存原始方法以便调用
2. **使用工厂**：使用装饰器工厂传递参数
3. **类型安全**：为装饰器添加类型注解
4. **文档说明**：为自定义装饰器添加文档说明

## 练习

1. **创建装饰器**：创建不同类型的自定义装饰器。

2. **装饰器工厂**：创建装饰器工厂，传递参数。

3. **装饰器组合**：组合使用多个装饰器。

4. **实际应用**：在实际场景中应用自定义装饰器。

5. **最佳实践**：按照最佳实践创建装饰器。

完成以上练习后，继续学习下一节，了解装饰器组合。

## 总结

自定义装饰器允许我们创建自己的装饰器函数，实现特定的功能。创建装饰器时应该保存原始方法，使用装饰器工厂传递参数，并添加类型注解。理解自定义装饰器的创建和使用，可以帮助我们实现更强大的功能增强。

## 相关资源

- [TypeScript 装饰器文档](https://www.typescriptlang.org/docs/handbook/decorators.html)
