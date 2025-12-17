# 3.3.6 装饰器元数据

## 概述

装饰器元数据允许在装饰器中存储和访问元数据信息。本节介绍装饰器元数据的使用。

## 什么是装饰器元数据

### 定义

装饰器元数据是存储在装饰器中的附加信息，可以在运行时访问。

### 启用元数据

在 `tsconfig.json` 中启用元数据：

```json
{
  "compilerOptions": {
    "experimentalDecorators": true,
    "emitDecoratorMetadata": true
  }
}
```

## 使用元数据

### reflect-metadata

需要安装 `reflect-metadata` 包：

```bash
npm install reflect-metadata
```

### 基本使用

```ts
import "reflect-metadata";

function log(target: any, propertyKey: string) {
    const types = Reflect.getMetadata("design:type", target, propertyKey);
    const paramTypes = Reflect.getMetadata("design:paramtypes", target, propertyKey);
    const returnType = Reflect.getMetadata("design:returntype", target, propertyKey);
}

class Example {
    @log
    method(param: string): number {
        return 0;
    }
}
```

## 元数据类型

### design:type

获取属性或方法的类型：

```ts
import "reflect-metadata";

function type(target: any, propertyKey: string) {
    const type = Reflect.getMetadata("design:type", target, propertyKey);
    console.log(type); // 类型信息
}
```

### design:paramtypes

获取参数类型：

```ts
import "reflect-metadata";

function paramTypes(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    const paramTypes = Reflect.getMetadata("design:paramtypes", target, propertyKey);
    console.log(paramTypes); // 参数类型数组
}
```

### design:returntype

获取返回值类型：

```ts
import "reflect-metadata";

function returnType(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    const returnType = Reflect.getMetadata("design:returntype", target, propertyKey);
    console.log(returnType); // 返回值类型
}
```

## 自定义元数据

### 设置元数据

```ts
import "reflect-metadata";

function setMetadata(key: string, value: any) {
    return function(target: any, propertyKey: string) {
        Reflect.defineMetadata(key, value, target, propertyKey);
    };
}
```

### 获取元数据

```ts
import "reflect-metadata";

function getMetadata(key: string, target: any, propertyKey: string) {
    return Reflect.getMetadata(key, target, propertyKey);
}
```

## 使用场景

### 1. 依赖注入

```ts
import "reflect-metadata";

function inject(target: any, propertyKey: string, parameterIndex: number) {
    const paramTypes = Reflect.getMetadata("design:paramtypes", target, propertyKey);
    const type = paramTypes[parameterIndex];
    // 依赖注入逻辑
}
```

### 2. 验证

```ts
import "reflect-metadata";

function validate(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    const paramTypes = Reflect.getMetadata("design:paramtypes", target, propertyKey);
    // 验证逻辑
}
```

## 注意事项

1. **需要安装**：需要安装 `reflect-metadata` 包
2. **启用配置**：需要启用 `emitDecoratorMetadata`
3. **导入顺序**：需要先导入 `reflect-metadata`
4. **类型信息**：元数据包含类型信息

## 最佳实践

1. **启用元数据**：在需要时启用装饰器元数据
2. **使用 reflect-metadata**：使用 reflect-metadata 访问元数据
3. **合理使用**：在合适的情况下使用元数据
4. **性能考虑**：考虑元数据的性能影响

## 练习

1. **启用元数据**：配置 TypeScript 启用装饰器元数据。

2. **使用元数据**：使用 reflect-metadata 访问元数据。

3. **自定义元数据**：设置和获取自定义元数据。

4. **实际应用**：在实际场景中应用装饰器元数据。

5. **依赖注入**：使用元数据实现依赖注入。

完成以上练习后，继续学习下一节，了解自定义装饰器。

## 总结

装饰器元数据允许在装饰器中存储和访问元数据信息。需要启用 `emitDecoratorMetadata` 并使用 `reflect-metadata` 包。理解装饰器元数据的使用，可以帮助我们实现更强大的装饰器功能。

## 相关资源

- [TypeScript 装饰器元数据文档](https://www.typescriptlang.org/docs/handbook/decorators.html#metadata)
- [reflect-metadata 文档](https://github.com/rbuckton/reflect-metadata)
