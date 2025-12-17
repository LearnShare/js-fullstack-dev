# 3.1.3 构造函数

## 概述

构造函数是类的特殊方法，用于初始化类的实例。本节介绍构造函数的定义、使用和参数处理。

## 构造函数定义

### 基本语法

```ts
class ClassName {
    constructor(param1: type1, param2: type2) {
        // 初始化代码
    }
}
```

### 示例

```ts
class Person {
    name: string;
    age: number;

    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }
}

let person = new Person("John", 30);
```

## 构造函数参数

### 必需参数

```ts
class Person {
    name: string;
    age: number;

    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }
}

// 必须提供所有参数
let person = new Person("John", 30);
```

### 可选参数

```ts
class Person {
    name: string;
    age?: number;

    constructor(name: string, age?: number) {
        this.name = name;
        if (age !== undefined) {
            this.age = age;
        }
    }
}

// 可以只提供必需参数
let person1 = new Person("John");
let person2 = new Person("John", 30);
```

### 默认参数

```ts
class Person {
    name: string;
    age: number;

    constructor(name: string, age: number = 0) {
        this.name = name;
        this.age = age;
    }
}

// 使用默认值
let person1 = new Person("John");      // age 默认为 0
let person2 = new Person("John", 30);  // age 为 30
```

### 剩余参数

```ts
class Person {
    name: string;
    tags: string[];

    constructor(name: string, ...tags: string[]) {
        this.name = name;
        this.tags = tags;
    }
}

let person = new Person("John", "developer", "typescript");
```

## 构造函数中的初始化

### 属性初始化

```ts
class Person {
    name: string;
    age: number;
    email: string;

    constructor(name: string, age: number, email: string) {
        this.name = name;
        this.age = age;
        this.email = email;
    }
}
```

### 计算属性

```ts
class Person {
    name: string;
    age: number;
    birthYear: number;

    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
        this.birthYear = new Date().getFullYear() - age;
    }
}
```

### 调用其他方法

```ts
class Person {
    name: string;
    normalizedName: string;

    constructor(name: string) {
        this.name = name;
        this.normalizedName = this.normalize(name);
    }

    private normalize(name: string): string {
        return name.toLowerCase().trim();
    }
}
```

## 默认构造函数

### 无构造函数

如果没有定义构造函数，TypeScript 会自动提供一个空的构造函数：

```ts
class Person {
    name: string = "Guest";
    age: number = 0;
}

// 等价于
class Person {
    name: string = "Guest";
    age: number = 0;

    constructor() {
        // 空构造函数
    }
}
```

## 构造函数重载

### 定义

TypeScript 支持构造函数重载：

```ts
class Person {
    name: string;
    age: number;

    // 重载签名
    constructor(name: string);
    constructor(name: string, age: number);
    // 实现签名
    constructor(name: string, age?: number) {
        this.name = name;
        this.age = age ?? 0;
    }
}

let person1 = new Person("John");
let person2 = new Person("John", 30);
```

## 构造函数中的 this

### this 指向

在构造函数中，`this` 指向正在创建的实例：

```ts
class Person {
    name: string;

    constructor(name: string) {
        this.name = name; // this 指向正在创建的实例
    }
}
```

### 访问实例成员

构造函数中可以访问实例成员：

```ts
class Person {
    name: string;
    greeting: string;

    constructor(name: string) {
        this.name = name;
        this.greeting = `Hello, ${this.name}!`;
    }
}
```

## 常见错误

### 错误 1：参数类型不匹配

```ts
class Person {
    name: string;
    age: number;

    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }
}

// 错误：参数类型不匹配
let person = new Person("John", "30");
```

### 错误 2：缺少必需参数

```ts
class Person {
    name: string;
    age: number;

    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }
}

// 错误：缺少必需参数
let person = new Person("John");
```

## 注意事项

1. **构造函数名称**：构造函数必须命名为 `constructor`
2. **只能有一个**：每个类只能有一个构造函数（可以有重载）
3. **this 指向**：构造函数中的 `this` 指向正在创建的实例
4. **返回值**：构造函数不能有返回值类型注解

## 最佳实践

1. **明确参数类型**：为构造函数参数添加明确的类型注解
2. **使用默认参数**：为可选参数提供合理的默认值
3. **初始化所有属性**：在构造函数中初始化所有必需属性
4. **避免复杂逻辑**：构造函数中避免复杂的业务逻辑

## 练习

1. **构造函数定义**：定义不同类型的构造函数，练习参数处理。

2. **参数类型**：练习必需参数、可选参数和默认参数的使用。

3. **构造函数重载**：定义构造函数重载，理解重载的工作原理。

4. **属性初始化**：在构造函数中初始化不同类型的属性。

5. **实际应用**：在实际场景中应用构造函数。

完成以上练习后，继续学习下一节，了解访问修饰符。

## 总结

构造函数是类的特殊方法，用于初始化类的实例。构造函数可以接收参数，支持可选参数、默认参数和剩余参数。理解构造函数的使用是学习 TypeScript 面向对象编程的关键。

## 相关资源

- [TypeScript 构造函数文档](https://www.typescriptlang.org/docs/handbook/2/classes.html#constructors)
