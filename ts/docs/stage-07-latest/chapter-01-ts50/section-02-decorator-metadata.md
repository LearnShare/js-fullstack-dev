# 7.1.2 装饰器元数据

## 概述

装饰器元数据是 TypeScript 5.0 引入的新特性，允许装饰器访问和修改元数据。本节介绍装饰器元数据的使用。

## 什么是装饰器元数据

### 定义

装饰器元数据允许装饰器访问和修改类的元数据，提供更强大的元编程能力。

### 基本概念

```ts
import "reflect-metadata";

class MyClass {
    @decorator
    method(): void {}
}
```

## 启用装饰器元数据

### tsconfig.json 配置

```json
{
  "compilerOptions": {
    "experimentalDecorators": true,
    "emitDecoratorMetadata": true
  }
}
```

### 安装 reflect-metadata

```bash
npm install reflect-metadata
```

## 使用装饰器元数据

### 1. 定义元数据

```ts
import "reflect-metadata";

function decorator(target: any, propertyKey: string) {
    Reflect.defineMetadata("key", "value", target, propertyKey);
}

class MyClass {
    @decorator
    method(): void {}
}
```

### 2. 读取元数据

```ts
import "reflect-metadata";

const metadata = Reflect.getMetadata("key", MyClass.prototype, "method");
console.log(metadata); // "value"
```

### 3. 检查元数据

```ts
import "reflect-metadata";

const hasMetadata = Reflect.hasMetadata("key", MyClass.prototype, "method");
console.log(hasMetadata); // true
```

## 使用场景

### 1. 依赖注入

```ts
import "reflect-metadata";

function Injectable(target: any) {
    return target;
}

function Inject(token: string) {
    return function(target: any, propertyKey: string, parameterIndex: number) {
        Reflect.defineMetadata("inject", token, target, propertyKey);
    };
}

@Injectable
class MyService {
    constructor(@Inject("dependency") private dependency: any) {}
}
```

### 2. 路由定义

```ts
import "reflect-metadata";

function Route(path: string) {
    return function(target: any, propertyKey: string) {
        Reflect.defineMetadata("route", path, target, propertyKey);
    };
}

class MyController {
    @Route("/users")
    getUsers(): void {}
}
```

### 3. 验证规则

```ts
import "reflect-metadata";

function Required(target: any, propertyKey: string) {
    Reflect.defineMetadata("required", true, target, propertyKey);
}

class User {
    @Required
    name: string;
}
```

## 常见错误

### 错误 1：未启用元数据

```ts
// 错误：未启用 emitDecoratorMetadata
// tsconfig.json 需要设置 "emitDecoratorMetadata": true
```

### 错误 2：未安装 reflect-metadata

```ts
// 错误：未安装 reflect-metadata
// 需要：npm install reflect-metadata
```

## 注意事项

1. **配置启用**：需要在 tsconfig.json 中启用 emitDecoratorMetadata
2. **安装依赖**：需要安装 reflect-metadata
3. **导入顺序**：需要在文件顶部导入 reflect-metadata
4. **性能影响**：元数据访问可能有性能影响

## 最佳实践

1. **使用元数据**：在需要元编程时使用装饰器元数据
2. **依赖注入**：使用元数据实现依赖注入
3. **框架集成**：在框架中使用元数据
4. **性能考虑**：注意元数据访问的性能影响

## 练习

1. **装饰器元数据**：练习使用装饰器元数据。

2. **依赖注入**：使用元数据实现依赖注入。

3. **实际应用**：在实际场景中应用装饰器元数据。

完成以上练习后，继续学习下一节，了解其他改进。

## 总结

装饰器元数据允许装饰器访问和修改类的元数据，提供更强大的元编程能力。需要启用 emitDecoratorMetadata 和安装 reflect-metadata。理解装饰器元数据的使用是学习 TypeScript 5.0 新特性的关键。

## 相关资源

- [TypeScript 5.0 装饰器元数据](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-0.html#decorator-metadata)
- [reflect-metadata](https://github.com/rbuckton/reflect-metadata)
