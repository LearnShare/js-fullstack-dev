# 3.3.3 私有字段（Private Fields）

## 概述

私有字段使用 `#` 语法，提供真正的运行时私有，比 `private` 修饰符更严格。本节介绍私有字段的定义和使用。

## 什么是私有字段

### 定义

私有字段使用 `#` 前缀标记，提供真正的运行时私有，外部无法访问。

### 基本概念

```ts
class BankAccount {
    #balance: number = 0; // 私有字段

    deposit(amount: number): void {
        if (amount > 0) {
            this.#balance += amount;
        }
    }

    getBalance(): number {
        return this.#balance;
    }
}

let account = new BankAccount();
account.deposit(100);
console.log(account.getBalance()); // 100

// 错误：外部不能访问私有字段
// console.log(account.#balance); // 错误
```

## 私有字段 vs private 修饰符

### 区别

| 特性       | 私有字段（#）            | private 修饰符           |
|:-----------|:-------------------------|:-------------------------|
| 语法       | `#fieldName`             | `private fieldName`      |
| 运行时     | 真正的私有               | 编译时私有               |
| 子类访问   | 不能                     | 不能                     |
| 类型检查   | 编译时和运行时           | 仅编译时                 |

### 示例对比

```ts
// private 修饰符（编译时私有）
class Example1 {
    private value: number = 0;
}

// 运行时可以访问（通过类型断言）
let ex1 = new Example1();
console.log((ex1 as any).value); // 可以访问

// 私有字段（运行时私有）
class Example2 {
    #value: number = 0;
}

let ex2 = new Example2();
// console.log((ex2 as any).#value); // 错误：运行时也无法访问
```

## 私有字段使用

### 基本用法

```ts
class Person {
    #name: string;
    #age: number;

    constructor(name: string, age: number) {
        this.#name = name;
        this.#age = age;
    }

    getName(): string {
        return this.#name;
    }
}
```

### 私有方法

私有字段也可以用于方法：

```ts
class Calculator {
    #validate(value: number): boolean {
        return value >= 0;
    }

    add(a: number, b: number): number {
        if (this.#validate(a) && this.#validate(b)) {
            return a + b;
        }
        throw new Error("Invalid values");
    }
}
```

### 静态私有字段

私有字段可以是静态的：

```ts
class Counter {
    static #count: number = 0;

    static increment(): void {
        Counter.#count++;
    }

    static getCount(): number {
        return Counter.#count;
    }
}
```

## 继承中的私有字段

### 子类不能访问

子类不能访问父类的私有字段：

```ts
class Animal {
    #name: string;

    constructor(name: string) {
        this.#name = name;
    }
}

class Dog extends Animal {
    getName(): string {
        // return this.#name; // 错误：不能访问父类的私有字段
        return "";
    }
}
```

### 每个类独立的私有字段

每个类的私有字段是独立的：

```ts
class Animal {
    #name: string = "Animal";
}

class Dog extends Animal {
    #name: string = "Dog"; // 独立的私有字段

    getName(): string {
        return this.#name; // 返回 "Dog"
    }
}
```

## 使用场景

### 1. 真正的私有

需要运行时私有时使用私有字段：

```ts
class SecureData {
    #secret: string;

    constructor(secret: string) {
        this.#secret = secret;
    }
}
```

### 2. 避免命名冲突

私有字段可以避免命名冲突：

```ts
class Example {
    #value: number = 0;
    value: string = ""; // 可以同时存在
}
```

## 常见错误

### 错误 1：外部访问私有字段

```ts
class Person {
    #name: string;

    constructor(name: string) {
        this.#name = name;
    }
}

let person = new Person("John");
// console.log(person.#name); // 错误：不能访问私有字段
```

### 错误 2：子类访问父类私有字段

```ts
class Animal {
    #name: string;
}

class Dog extends Animal {
    getName(): string {
        // return this.#name; // 错误：不能访问父类的私有字段
        return "";
    }
}
```

## 注意事项

1. **运行时私有**：私有字段是真正的运行时私有
2. **不能继承**：子类不能访问父类的私有字段
3. **独立字段**：每个类的私有字段是独立的
4. **TypeScript 版本**：需要 TypeScript 3.8+

## 最佳实践

1. **使用私有字段**：需要真正的私有时使用私有字段
2. **避免冲突**：使用私有字段避免命名冲突
3. **合理使用**：根据实际需求选择私有字段或 private 修饰符
4. **版本要求**：确保 TypeScript 版本支持

## 练习

1. **私有字段**：定义使用私有字段的类，理解私有限制。

2. **私有方法**：定义私有方法，理解私有方法的使用。

3. **继承测试**：测试子类访问父类私有字段的限制。

4. **对比实践**：对比私有字段和 private 修饰符的差异。

5. **实际应用**：在实际场景中应用私有字段。

完成以上练习后，继续学习下一节，了解装饰器。

## 总结

私有字段使用 `#` 语法，提供真正的运行时私有。私有字段比 `private` 修饰符更严格，子类不能访问父类的私有字段。理解私有字段的使用可以帮助我们实现更强的封装。

## 相关资源

- [TypeScript 私有字段文档](https://www.typescriptlang.org/docs/handbook/2/classes.html#private-fields)
