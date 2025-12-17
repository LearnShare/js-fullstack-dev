# 6.2.7 类型扩展与合并

## 概述

类型扩展与合并允许扩展现有类型，添加新的属性或方法。本节介绍类型扩展和合并的使用。

## 类型扩展

### 接口扩展

使用 `extends` 扩展接口：

```ts
interface Base {
    name: string;
}

interface Extended extends Base {
    age: number;
}

// Extended 包含 name 和 age
const user: Extended = {
    name: "John",
    age: 30
};
```

### 类型别名扩展

使用交叉类型扩展类型别名：

```ts
type Base = {
    name: string;
};

type Extended = Base & {
    age: number;
};

// Extended 包含 name 和 age
const user: Extended = {
    name: "John",
    age: 30
};
```

## 类型合并

### 接口合并

同名接口会自动合并：

```ts
interface User {
    name: string;
}

interface User {
    age: number;
}

// User 包含 name 和 age
const user: User = {
    name: "John",
    age: 30
};
```

### 命名空间合并

同名命名空间会自动合并：

```ts
namespace MyLibrary {
    export function init(): void {}
}

namespace MyLibrary {
    export function process(): void {}
}

// MyLibrary 包含 init 和 process
MyLibrary.init();
MyLibrary.process();
```

### 命名空间与类合并

命名空间可以与类合并：

```ts
class MyClass {
    method(): void {}
}

namespace MyClass {
    export function staticMethod(): void {}
}

// 类方法和静态方法
const instance = new MyClass();
instance.method();
MyClass.staticMethod();
```

## 模块扩展

### 扩展模块类型

使用 `declare module` 扩展模块类型：

```ts
// 扩展 express 模块
declare module "express" {
    interface Request {
        user?: {
            id: string;
            name: string;
        };
    }
}

// 使用扩展的类型
import { Request } from "express";
const req: Request = {};
req.user = { id: "1", name: "John" };
```

### 扩展全局类型

使用 `declare global` 扩展全局类型：

```ts
declare global {
    interface Window {
        myAPI: {
            call(): void;
        };
    }
}

// 使用扩展的类型
window.myAPI.call();
```

## 使用场景

### 1. 扩展第三方库

```ts
// 扩展第三方库类型
declare module "third-party" {
    interface Config {
        customOption: string;
    }
}
```

### 2. 扩展全局对象

```ts
// 扩展全局对象
declare global {
    interface Document {
        customMethod(): void;
    }
}

export {};
```

### 3. 类型组织

```ts
// 使用接口合并组织类型
interface User {
    name: string;
}

interface User {
    age: number;
}
```

## 常见错误

### 错误 1：类型冲突

```ts
// 错误：类型冲突
interface User {
    name: string;
}

interface User {
    name: number; // 错误：与第一个定义冲突
}
```

### 错误 2：扩展顺序错误

```ts
// 错误：扩展顺序错误
interface Extended extends Base {
    // ...
}

interface Base {
    // 错误：Base 在 Extended 之后定义
}
```

## 注意事项

1. **接口合并**：同名接口会自动合并
2. **类型冲突**：合并时不能有类型冲突
3. **扩展顺序**：被扩展的类型需要先定义
4. **模块扩展**：使用 declare module 扩展模块类型

## 最佳实践

1. **使用接口合并**：合理使用接口合并组织类型
2. **扩展第三方库**：使用模块扩展扩展第三方库类型
3. **类型安全**：确保类型扩展类型安全
4. **避免冲突**：避免类型定义冲突

## 练习

1. **类型扩展**：练习接口和类型别名的扩展。

2. **类型合并**：练习接口和命名空间的合并。

3. **模块扩展**：扩展第三方库和全局类型。

4. **实际应用**：在实际场景中应用类型扩展和合并。

完成以上练习后，继续学习下一节，了解 DefinitelyTyped。

## 总结

类型扩展与合并允许扩展现有类型，添加新的属性或方法。接口和命名空间会自动合并，可以使用模块扩展扩展第三方库类型。理解类型扩展和合并是学习声明文件的关键。

## 相关资源

- [TypeScript 声明合并文档](https://www.typescriptlang.org/docs/handbook/declaration-merging.html)
