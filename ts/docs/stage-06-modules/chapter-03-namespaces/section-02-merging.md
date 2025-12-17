# 6.3.2 命名空间合并

## 概述

同名命名空间会自动合并。本节介绍命名空间合并的规则。

## 命名空间合并

### 基本规则

同名命名空间会自动合并：

```ts
namespace MyNamespace {
    export function function1(): void {}
}

namespace MyNamespace {
    export function function2(): void {}
}

// MyNamespace 包含 function1 和 function2
MyNamespace.function1();
MyNamespace.function2();
```

### 合并顺序

命名空间按声明顺序合并：

```ts
namespace MyNamespace {
    export const value1 = "first";
}

namespace MyNamespace {
    export const value2 = "second";
}

// MyNamespace 包含 value1 和 value2
console.log(MyNamespace.value1); // "first"
console.log(MyNamespace.value2); // "second"
```

## 接口合并

### 命名空间中的接口

命名空间中的接口也会合并：

```ts
namespace MyNamespace {
    export interface Config {
        apiUrl: string;
    }
}

namespace MyNamespace {
    export interface Config {
        timeout: number;
    }
}

// Config 包含 apiUrl 和 timeout
const config: MyNamespace.Config = {
    apiUrl: "https://api.example.com",
    timeout: 5000
};
```

## 类与命名空间合并

### 类与命名空间合并

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

## 函数与命名空间合并

### 函数与命名空间合并

命名空间可以与函数合并：

```ts
function myFunction(): void {}

namespace myFunction {
    export const version = "1.0.0";
}

// 函数和命名空间属性
myFunction();
console.log(myFunction.version);
```

## 枚举与命名空间合并

### 枚举与命名空间合并

命名空间可以与枚举合并：

```ts
enum Color {
    Red,
    Green,
    Blue
}

namespace Color {
    export function getName(color: Color): string {
        switch (color) {
            case Color.Red:
                return "红色";
            case Color.Green:
                return "绿色";
            case Color.Blue:
                return "蓝色";
        }
    }
}

// 枚举值和命名空间方法
const color = Color.Red;
console.log(Color.getName(color));
```

## 使用场景

### 1. 扩展类

```ts
class MyClass {
    method(): void {}
}

namespace MyClass {
    export function staticMethod(): void {}
    export interface Options {
        option: string;
    }
}
```

### 2. 扩展函数

```ts
function myFunction(): void {}

namespace myFunction {
    export const version = "1.0.0";
    export interface Config {
        apiUrl: string;
    }
}
```

### 3. 扩展枚举

```ts
enum Status {
    Active,
    Inactive
}

namespace Status {
    export function getLabel(status: Status): string {
        switch (status) {
            case Status.Active:
                return "活跃";
            case Status.Inactive:
                return "非活跃";
        }
    }
}
```

## 常见错误

### 错误 1：类型冲突

```ts
// 错误：类型冲突
namespace MyNamespace {
    export const value: string = "value";
}

namespace MyNamespace {
    export const value: number = 123; // 错误：类型冲突
}
```

### 错误 2：非导出成员冲突

```ts
// 错误：非导出成员不会合并
namespace MyNamespace {
    function process(): void {}
}

namespace MyNamespace {
    function process(): void {} // 错误：重复声明
}
```

## 注意事项

1. **自动合并**：同名命名空间会自动合并
2. **类型冲突**：合并时不能有类型冲突
3. **导出成员**：只有导出成员会合并
4. **合并顺序**：按声明顺序合并

## 最佳实践

1. **使用合并**：合理使用命名空间合并扩展类型
2. **避免冲突**：避免类型定义冲突
3. **明确导出**：明确哪些成员需要导出
4. **文档注释**：为合并的命名空间添加文档注释

## 练习

1. **命名空间合并**：练习命名空间的合并。

2. **类与命名空间**：练习类与命名空间的合并。

3. **枚举与命名空间**：练习枚举与命名空间的合并。

4. **实际应用**：在实际场景中应用命名空间合并。

完成以上练习后，继续学习下一节，了解命名空间与模块的对比。

## 总结

同名命名空间会自动合并。命名空间可以与类、函数、枚举合并，扩展它们的功能。理解命名空间合并是学习命名空间的关键。

## 相关资源

- [TypeScript 声明合并文档](https://www.typescriptlang.org/docs/handbook/declaration-merging.html)
