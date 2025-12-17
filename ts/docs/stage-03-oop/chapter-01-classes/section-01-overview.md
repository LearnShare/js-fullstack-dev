# 3.1.1 类的基础概述

## 概述

类是 TypeScript 面向对象编程的基础，用于定义对象的模板。本节介绍类的概念、作用和优势。

## 什么是类

### 定义

类是一种用于创建对象的模板，定义了对象的属性和方法。

### 基本概念

```ts
// 类定义
class Person {
    name: string;
    age: number;

    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }

    greet(): string {
        return `Hello, I'm ${this.name}`;
    }
}

// 创建对象（实例）
let person = new Person("John", 30);
console.log(person.greet()); // "Hello, I'm John"
```

## 类的作用

### 1. 封装

类将数据和方法封装在一起：

```ts
class BankAccount {
    private balance: number = 0;

    deposit(amount: number): void {
        if (amount > 0) {
            this.balance += amount;
        }
    }

    withdraw(amount: number): void {
        if (amount > 0 && amount <= this.balance) {
            this.balance -= amount;
        }
    }

    getBalance(): number {
        return this.balance;
    }
}
```

### 2. 代码复用

类可以创建多个实例，复用代码：

```ts
class User {
    name: string;
    email: string;

    constructor(name: string, email: string) {
        this.name = name;
        this.email = email;
    }
}

// 创建多个实例
let user1 = new User("John", "john@example.com");
let user2 = new User("Jane", "jane@example.com");
```

### 3. 类型安全

类提供类型安全：

```ts
class Point {
    x: number;
    y: number;

    constructor(x: number, y: number) {
        this.x = x;
        this.y = y;
    }
}

let point = new Point(10, 20);
// point.x = "10"; // 错误：类型不匹配
```

### 4. IDE 支持

类提供更好的 IDE 支持：

```ts
class User {
    name: string;
    age: number;
}

let user = new User();
user. // IDE 会提示 name 和 age
```

## 类的优势

### 1. 面向对象编程

类支持面向对象编程的核心概念：

- **封装**：将数据和方法封装在一起
- **继承**：类可以继承其他类
- **多态**：子类可以重写父类方法

### 2. 类型检查

类提供编译时类型检查：

```ts
class User {
    name: string;
    age: number;
}

let user = new User();
user.name = "John"; // 正确
user.age = "30";    // 错误：类型不匹配
```

### 3. 代码组织

类帮助组织代码：

```ts
// 相关的数据和方法组织在一起
class Calculator {
    private result: number = 0;

    add(value: number): void {
        this.result += value;
    }

    subtract(value: number): void {
        this.result -= value;
    }

    getResult(): number {
        return this.result;
    }
}
```

## 类 vs 接口

### 区别

| 特性       | 类（Class）              | 接口（Interface）        |
|:-----------|:-------------------------|:-------------------------|
| 实例化     | 可以实例化               | 不能实例化               |
| 实现       | 可以实现接口             | 可以被类实现             |
| 运行时     | 运行时存在               | 编译时存在               |
| 构造函数   | 有                       | 没有                     |
| 方法实现   | 有                       | 没有（抽象方法除外）     |

### 使用场景

#### 使用类

- 需要创建实例
- 需要方法实现
- 需要构造函数
- 需要访问修饰符

#### 使用接口

- 定义类型契约
- 不需要实现
- 需要声明合并
- 需要扩展第三方库

## 类 vs 对象字面量

### 区别

| 特性       | 类（Class）              | 对象字面量               |
|:-----------|:-------------------------|:-------------------------|
| 实例化     | 可以创建多个实例         | 单个对象                 |
| 类型检查   | 编译时类型检查           | 编译时类型检查           |
| 继承       | 支持继承                 | 不支持                   |
| 构造函数   | 有                       | 没有                     |

### 使用场景

#### 使用类

- 需要创建多个实例
- 需要继承
- 需要构造函数
- 需要访问修饰符

#### 使用对象字面量

- 单个对象
- 配置对象
- 数据对象
- 不需要继承

## 注意事项

1. **类是模板**：类定义了对象的模板，不是对象本身
2. **需要实例化**：使用 `new` 关键字创建类的实例
3. **this 关键字**：类方法中使用 `this` 引用当前实例
4. **类型检查**：类提供编译时类型检查

## 最佳实践

1. **使用类组织代码**：将相关的数据和方法组织在类中
2. **使用访问修饰符**：合理使用访问修饰符控制访问
3. **明确类型**：为类属性添加明确的类型注解
4. **单一职责**：每个类应该有单一的职责

## 练习

1. **类定义**：定义一个用户类，包含姓名、年龄等属性。

2. **类实例化**：创建类的实例，调用类的方法。

3. **封装实践**：使用访问修饰符实现数据封装。

4. **类型检查**：体验类的类型检查功能。

5. **实际应用**：在实际场景中应用类。

完成以上练习后，继续学习下一节，了解类声明与实例化。

## 总结

类是 TypeScript 面向对象编程的基础，用于定义对象的模板。类提供封装、代码复用、类型安全和 IDE 支持等优势。理解类的概念和作用是学习 TypeScript 面向对象编程的关键。

## 相关资源

- [TypeScript 类文档](https://www.typescriptlang.org/docs/handbook/2/classes.html)
