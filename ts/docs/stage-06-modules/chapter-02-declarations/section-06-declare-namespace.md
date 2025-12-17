# 6.2.6 declare namespace

## 概述

`declare namespace` 用于声明命名空间。本节介绍 `declare namespace` 的使用。

## declare namespace

### 定义

`declare namespace` 用于声明命名空间，组织相关的类型和值。

### 基本语法

```ts
declare namespace NamespaceName {
    // 命名空间内容
}
```

### 示例

```ts
declare namespace jQuery {
    function ajax(settings: any): void;

    interface AjaxSettings {
        url: string;
        method?: string;
    }
}
```

## 命名空间嵌套

### 嵌套命名空间

```ts
declare namespace MyLibrary {
    namespace Utils {
        function format(value: any): string;
    }

    namespace API {
        function call(): void;
    }
}
```

### 使用

```ts
MyLibrary.Utils.format("value");
MyLibrary.API.call();
```

## 命名空间与接口

### 在命名空间中定义接口

```ts
declare namespace MyLibrary {
    interface Config {
        apiUrl: string;
        timeout: number;
    }

    function init(config: Config): void;
}
```

## 使用场景

### 1. 第三方库

```ts
declare namespace jQuery {
    function $(selector: string): JQuery;
    interface JQuery {
        text(): string;
        html(html: string): JQuery;
    }
}
```

### 2. 全局对象

```ts
declare namespace MyGlobal {
    const version: string;
    function init(): void;
}
```

### 3. 类型组织

```ts
declare namespace Types {
    interface User {
        name: string;
    }

    interface Config {
        apiUrl: string;
    }
}
```

## 常见错误

### 错误 1：缺少 declare

```ts
// 错误：声明命名空间需要 declare
namespace MyNamespace {
    // 错误
}

// 正确
declare namespace MyNamespace {
    // 正确
}
```

### 错误 2：命名空间冲突

```ts
// 错误：命名空间名称冲突
declare namespace MyNamespace {
    // ...
}

declare namespace MyNamespace {
    // 错误：重复声明
}
```

## 注意事项

1. **declare 关键字**：声明命名空间需要使用 declare
2. **命名空间合并**：同名命名空间会合并
3. **类型安全**：确保命名空间声明类型安全
4. **模块化**：考虑使用模块替代命名空间

## 最佳实践

1. **使用 declare namespace**：在需要时使用 declare namespace
2. **命名空间组织**：合理组织命名空间结构
3. **类型安全**：确保命名空间声明类型安全
4. **考虑模块**：考虑使用模块替代命名空间

## 练习

1. **declare namespace**：使用 declare namespace 声明命名空间。

2. **命名空间嵌套**：定义嵌套命名空间。

3. **实际应用**：在实际场景中应用 declare namespace。

完成以上练习后，继续学习下一节，了解类型扩展与合并。

## 总结

`declare namespace` 用于声明命名空间，组织相关的类型和值。可以使用嵌套命名空间，同名命名空间会合并。理解 declare namespace 的使用是学习声明文件的关键。

## 相关资源

- [TypeScript declare namespace 文档](https://www.typescriptlang.org/docs/handbook/declaration-files/templates/module-d-ts.html#namespace)
