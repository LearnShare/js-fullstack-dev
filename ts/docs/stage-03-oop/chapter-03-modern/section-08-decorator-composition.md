# 3.3.8 装饰器组合

## 概述

装饰器可以组合使用，多个装饰器可以同时应用于同一个目标。本节介绍装饰器组合的使用和注意事项。

## 装饰器组合

### 基本语法

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

多个装饰器的执行顺序是从下到上（装饰器工厂）和从上到下（装饰器应用）：

```ts
function first() {
    console.log("first factory");
    return function(target: any, propertyKey: string) {
        console.log("first applied");
    };
}

function second() {
    console.log("second factory");
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
// "second factory"
// "first factory"
// "second applied"
// "first applied"
```

## 组合模式

### 日志 + 性能监控

```ts
class Service {
    @log
    @measure
    process(data: any) {
        // 同时记录日志和性能
    }
}
```

### 验证 + 缓存

```ts
class Calculator {
    @validate
    @cache
    calculate(n: number): number {
        // 先验证，再缓存
    }
}
```

## 装饰器链

### 链式执行

装饰器按顺序执行，形成装饰器链：

```ts
function step1(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    console.log("Step 1");
    return descriptor;
}

function step2(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    console.log("Step 2");
    return descriptor;
}

class Example {
    @step1
    @step2
    method() {
        // ...
    }
}
```

## 注意事项

1. **执行顺序**：理解装饰器的执行顺序
2. **返回值**：装饰器可以修改描述符
3. **副作用**：注意装饰器的副作用
4. **性能**：多个装饰器可能影响性能

## 最佳实践

1. **合理组合**：合理组合装饰器，避免冲突
2. **明确顺序**：明确装饰器的执行顺序
3. **文档说明**：为装饰器组合添加文档说明
4. **测试验证**：测试装饰器组合的效果

## 练习

1. **装饰器组合**：组合使用多个装饰器。

2. **执行顺序**：理解装饰器的执行顺序。

3. **实际应用**：在实际场景中应用装饰器组合。

4. **最佳实践**：按照最佳实践组合装饰器。

完成以上练习后，现代类特性章节学习完成。阶段三学习完成，可以继续学习阶段四：泛型。

## 总结

装饰器可以组合使用，多个装饰器可以同时应用于同一个目标。理解装饰器组合的执行顺序和注意事项，可以帮助我们更好地使用装饰器增强类的功能。

## 相关资源

- [TypeScript 装饰器文档](https://www.typescriptlang.org/docs/handbook/decorators.html)
