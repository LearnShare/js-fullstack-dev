# 3.1.5 只读属性与静态成员

## 概述

只读属性确保属性值不会被修改，静态成员属于类本身而不是实例。本节介绍只读属性和静态成员的定义和使用。

## 只读属性

### 定义

只读属性使用 `readonly` 关键字标记，只能在声明时或构造函数中赋值。

### 语法

```ts
class ClassName {
    readonly property: type;
}
```

### 示例

```ts
class Person {
    readonly id: number;
    name: string;

    constructor(id: number, name: string) {
        this.id = id;      // 构造函数中可以赋值
        this.name = name;
    }
}

let person = new Person(1, "John");
console.log(person.id);   // 1

// 错误：不能修改只读属性
// person.id = 2; // 错误
```

### 声明时初始化

只读属性可以在声明时初始化：

```ts
class Person {
    readonly id: number = Math.random();
    name: string;
}
```

### 只读属性与 const

| 特性       | readonly 属性            | const 变量               |
|:-----------|:-------------------------|:-------------------------|
| 作用域     | 类属性                   | 变量                     |
| 赋值时机   | 声明时或构造函数中       | 声明时                   |
| 使用场景   | 类属性                   | 常量值                   |

## 静态成员

### 定义

静态成员属于类本身，而不是类的实例。使用 `static` 关键字定义。

### 静态属性

```ts
class MathUtils {
    static PI: number = 3.14159;
    static E: number = 2.71828;
}

// 通过类名访问
console.log(MathUtils.PI); // 3.14159
console.log(MathUtils.E);  // 2.71828

// 不能通过实例访问
let utils = new MathUtils();
// console.log(utils.PI); // 错误
```

### 静态方法

```ts
class MathUtils {
    static add(a: number, b: number): number {
        return a + b;
    }

    static multiply(a: number, b: number): number {
        return a * b;
    }
}

// 通过类名调用
console.log(MathUtils.add(1, 2));        // 3
console.log(MathUtils.multiply(2, 3));    // 6
```

### 静态方法中的 this

静态方法中的 `this` 指向类本身：

```ts
class Counter {
    static count: number = 0;

    static increment(): void {
        this.count++; // this 指向 Counter 类
    }

    static getCount(): number {
        return this.count;
    }
}

Counter.increment();
console.log(Counter.getCount()); // 1
```

## 静态成员 vs 实例成员

### 区别

| 特性       | 静态成员                 | 实例成员                 |
|:-----------|:-------------------------|:-------------------------|
| 定义       | `static` 关键字          | 无关键字                 |
| 访问方式   | 类名.成员                | 实例.成员                |
| 内存       | 类级别，所有实例共享     | 实例级别，每个实例独立   |
| this 指向  | 类本身                   | 实例                     |

### 示例对比

```ts
class Example {
    // 实例成员
    instanceProp: string = "instance";
    instanceMethod(): void {
        console.log(this.instanceProp); // this 指向实例
    }

    // 静态成员
    static staticProp: string = "static";
    static staticMethod(): void {
        console.log(this.staticProp); // this 指向类
    }
}

// 实例成员访问
let example = new Example();
console.log(example.instanceProp);
example.instanceMethod();

// 静态成员访问
console.log(Example.staticProp);
Example.staticMethod();
```

## 只读静态属性

### 定义

静态属性可以标记为只读：

```ts
class Config {
    static readonly API_URL: string = "https://api.example.com";
    static readonly VERSION: string = "1.0.0";
}

// 可以访问
console.log(Config.API_URL);

// 错误：不能修改
// Config.API_URL = "https://other.com"; // 错误
```

## 使用场景

### 只读属性使用场景

1. **ID 标识符**

```ts
class Entity {
    readonly id: number;
    name: string;

    constructor(id: number, name: string) {
        this.id = id;
        this.name = name;
    }
}
```

2. **配置常量**

```ts
class AppConfig {
    readonly version: string = "1.0.0";
    readonly apiUrl: string = "https://api.example.com";
}
```

### 静态成员使用场景

1. **工具类**

```ts
class StringUtils {
    static capitalize(str: string): string {
        return str.charAt(0).toUpperCase() + str.slice(1);
    }

    static reverse(str: string): string {
        return str.split("").reverse().join("");
    }
}
```

2. **单例模式**

```ts
class Database {
    private static instance: Database;

    private constructor() {}

    static getInstance(): Database {
        if (!Database.instance) {
            Database.instance = new Database();
        }
        return Database.instance;
    }
}
```

3. **常量定义**

```ts
class Constants {
    static readonly MAX_SIZE: number = 1000;
    static readonly DEFAULT_TIMEOUT: number = 5000;
}
```

## 常见错误

### 错误 1：修改只读属性

```ts
class Person {
    readonly id: number;

    constructor(id: number) {
        this.id = id;
    }
}

let person = new Person(1);
// person.id = 2; // 错误：不能修改只读属性
```

### 错误 2：通过实例访问静态成员

```ts
class MathUtils {
    static PI: number = 3.14159;
}

let utils = new MathUtils();
// console.log(utils.PI); // 错误：应该使用 MathUtils.PI
```

### 错误 3：在静态方法中使用 this 访问实例成员

```ts
class Example {
    instanceProp: string = "instance";

    static staticMethod(): void {
        // console.log(this.instanceProp); // 错误：静态方法中不能访问实例成员
    }
}
```

## 注意事项

1. **只读属性赋值**：只读属性只能在声明时或构造函数中赋值
2. **静态成员访问**：静态成员通过类名访问，不能通过实例访问
3. **this 指向**：静态方法中的 `this` 指向类本身
4. **内存共享**：静态成员在所有实例间共享

## 最佳实践

1. **使用只读属性**：对于不应该修改的属性使用只读
2. **使用静态成员**：对于不需要实例的成员使用静态
3. **明确意图**：使用 `readonly` 和 `static` 明确表达设计意图
4. **合理使用**：避免过度使用静态成员

## 练习

1. **只读属性**：定义包含只读属性的类，理解只读限制。

2. **静态成员**：定义包含静态属性和静态方法的类。

3. **访问方式**：练习静态成员和实例成员的访问方式。

4. **实际应用**：在实际场景中应用只读属性和静态成员。

5. **设计模式**：使用静态成员实现单例模式等设计模式。

完成以上练习后，类的基础章节学习完成。可以继续学习下一章：继承与多态。

## 总结

只读属性使用 `readonly` 关键字标记，只能在声明时或构造函数中赋值。静态成员使用 `static` 关键字定义，属于类本身而不是实例。理解只读属性和静态成员的使用，可以帮助我们更好地设计类。

## 相关资源

- [TypeScript 只读属性文档](https://www.typescriptlang.org/docs/handbook/2/classes.html#readonly)
- [TypeScript 静态成员文档](https://www.typescriptlang.org/docs/handbook/2/classes.html#static-members)
