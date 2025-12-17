# 3.1.2 类声明与实例化

## 概述

本节介绍 TypeScript 类的声明方式和实例化方法，包括类声明、类表达式和实例创建。

## 类声明

### 基本语法

```ts
class ClassName {
    // 属性
    property: type;

    // 方法
    method(): returnType {
        // 方法体
    }
}
```

### 示例

```ts
// 类声明
class Person {
    name: string;
    age: number;

    greet(): string {
        return `Hello, I'm ${this.name}`;
    }
}
```

### 类表达式

类也可以使用表达式形式定义：

```ts
// 匿名类表达式
const Person = class {
    name: string;
    age: number;
};

// 命名类表达式
const Person = class PersonClass {
    name: string;
    age: number;
};
```

## 实例化

### 使用 new 关键字

使用 `new` 关键字创建类的实例：

```ts
class Person {
    name: string;
    age: number;
}

// 创建实例
let person = new Person();
```

### 实例属性初始化

可以在声明时初始化属性：

```ts
class Person {
    name: string = "Guest";
    age: number = 0;
}

let person = new Person();
console.log(person.name); // "Guest"
console.log(person.age);  // 0
```

### 通过构造函数初始化

通过构造函数初始化属性：

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
console.log(person.name); // "John"
console.log(person.age);  // 30
```

## 属性声明

### 基本属性

```ts
class Person {
    name: string;
    age: number;
    email: string;
}
```

### 可选属性

```ts
class Person {
    name: string;
    age?: number;  // 可选属性
    email?: string; // 可选属性
}
```

### 只读属性

```ts
class Person {
    readonly id: number;
    name: string;

    constructor(id: number, name: string) {
        this.id = id;
        this.name = name;
    }
}
```

## 方法定义

### 实例方法

```ts
class Person {
    name: string;

    greet(): string {
        return `Hello, I'm ${this.name}`;
    }

    introduce(other: Person): string {
        return `${this.name} meets ${other.name}`;
    }
}
```

### 方法中的 this

在方法中，`this` 指向当前实例：

```ts
class Person {
    name: string;

    getName(): string {
        return this.name; // this 指向当前实例
    }
}
```

## 类型注解

### 属性类型注解

```ts
class Person {
    name: string;        // 明确类型
    age: number;         // 明确类型
    isActive: boolean;    // 明确类型
}
```

### 方法类型注解

```ts
class Calculator {
    add(a: number, b: number): number {
        return a + b;
    }

    process(value: string): string {
        return value.toUpperCase();
    }
}
```

## 常见错误

### 错误 1：未初始化属性

```ts
class Person {
    name: string;
    age: number;
}

let person = new Person();
console.log(person.name); // 错误：属性可能未初始化
```

### 错误 2：类型不匹配

```ts
class Person {
    name: string;
    age: number;
}

let person = new Person();
person.name = "John";
person.age = "30"; // 错误：类型不匹配
```

## 注意事项

1. **类不会被提升**：类声明不会被提升，必须先声明后使用
2. **必须使用 new**：类必须使用 `new` 关键字实例化
3. **this 绑定**：方法中的 `this` 指向调用该方法的实例
4. **属性初始化**：属性可以在声明时或构造函数中初始化

## 最佳实践

1. **明确类型**：为类属性添加明确的类型注解
2. **使用构造函数**：通过构造函数初始化属性
3. **合理组织**：将相关的属性和方法组织在类中
4. **避免未初始化**：确保属性在使用前已初始化

## 练习

1. **类声明**：定义不同类型的类，练习类声明。

2. **实例化**：创建类的实例，访问实例属性和方法。

3. **属性初始化**：练习属性的不同初始化方式。

4. **方法定义**：定义不同类型的类方法。

5. **类型检查**：体验类的类型检查功能。

完成以上练习后，继续学习下一节，了解构造函数。

## 总结

类声明使用 `class` 关键字，实例化使用 `new` 关键字。类可以包含属性和方法，属性需要类型注解，方法中的 `this` 指向当前实例。理解类声明和实例化是学习 TypeScript 面向对象编程的基础。

## 相关资源

- [TypeScript 类文档](https://www.typescriptlang.org/docs/handbook/2/classes.html)
