# 3.3.2 参数属性（Parameter Properties）

## 概述

参数属性允许在构造函数参数中直接声明和初始化属性，简化类的定义。本节介绍参数属性的定义和使用。

## 什么是参数属性

### 定义

参数属性是 TypeScript 的特性，允许在构造函数参数前使用访问修饰符，自动创建并初始化属性。

### 基本概念

```ts
class Person {
    // 传统方式
    name: string;
    age: number;

    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }
}

// 使用参数属性
class Person2 {
    constructor(public name: string, public age: number) {
        // 自动创建并初始化 name 和 age 属性
    }
}
```

## 参数属性语法

### 基本语法

```ts
class ClassName {
    constructor(public param: type) {
        // 自动创建 public param 属性并初始化
    }
}
```

### 访问修饰符

参数属性支持所有访问修饰符：

```ts
class Example {
    constructor(
        public publicProp: string,
        private privateProp: string,
        protected protectedProp: string,
        readonly readonlyProp: string
    ) {
        // 自动创建并初始化所有属性
    }
}
```

## 使用示例

### public 参数属性

```ts
class Person {
    constructor(public name: string, public age: number) {
        // name 和 age 自动成为 public 属性
    }
}

let person = new Person("John", 30);
console.log(person.name); // "John"
console.log(person.age);  // 30
```

### private 参数属性

```ts
class BankAccount {
    constructor(private balance: number = 0) {
        // balance 自动成为 private 属性
    }

    getBalance(): number {
        return this.balance; // 可以访问
    }
}

let account = new BankAccount(100);
// console.log(account.balance); // 错误：不能访问私有属性
```

### protected 参数属性

```ts
class Animal {
    constructor(protected name: string) {
        // name 自动成为 protected 属性
    }
}

class Dog extends Animal {
    getName(): string {
        return this.name; // 子类可以访问
    }
}
```

### readonly 参数属性

```ts
class Person {
    constructor(public name: string, readonly id: number) {
        // id 自动成为 readonly 属性
    }
}

let person = new Person("John", 1);
console.log(person.id); // 1
// person.id = 2; // 错误：不能修改只读属性
```

## 参数属性 vs 传统方式

### 对比

| 特性       | 参数属性                 | 传统方式                 |
|:-----------|:-------------------------|:-------------------------|
| 代码量     | 少                       | 多                       |
| 可读性     | 高                       | 中等                     |
| 灵活性     | 中等                     | 高                       |
| 使用场景   | 简单属性初始化           | 复杂初始化逻辑           |

### 示例对比

```ts
// 传统方式
class Person {
    name: string;
    age: number;

    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }
}

// 参数属性
class Person2 {
    constructor(public name: string, public age: number) {
        // 更简洁
    }
}
```

## 混合使用

### 参数属性与传统属性

可以混合使用参数属性和传统属性：

```ts
class Person {
    email: string; // 传统属性

    constructor(
        public name: string,
        public age: number,
        email: string
    ) {
        this.email = email; // 传统方式初始化
    }
}
```

## 常见错误

### 错误 1：重复声明

```ts
class Person {
    name: string; // 错误：与参数属性重复

    constructor(public name: string) {
        // 错误
    }
}
```

### 错误 2：参数属性类型不匹配

```ts
class Person {
    constructor(public name: string, public age: number) {
        // ...
    }
}

// 错误：参数类型不匹配
let person = new Person("John", "30");
```

## 注意事项

1. **自动创建**：参数属性会自动创建属性
2. **不能重复**：不能同时声明参数属性和同名属性
3. **访问修饰符**：参数属性必须使用访问修饰符
4. **初始化顺序**：参数属性在构造函数执行前初始化

## 最佳实践

1. **使用参数属性**：对于简单的属性初始化使用参数属性
2. **明确类型**：为参数属性添加明确的类型注解
3. **合理使用**：在合适的情况下使用参数属性
4. **保持简洁**：使用参数属性保持代码简洁

## 练习

1. **参数属性**：使用参数属性定义类，简化代码。

2. **访问修饰符**：使用不同的访问修饰符定义参数属性。

3. **混合使用**：混合使用参数属性和传统属性。

4. **实际应用**：在实际场景中应用参数属性。

5. **对比实践**：对比参数属性和传统方式的差异。

完成以上练习后，继续学习下一节，了解私有字段。

## 总结

参数属性允许在构造函数参数中直接声明和初始化属性，简化类的定义。参数属性支持所有访问修饰符，可以自动创建属性。理解参数属性的使用可以帮助我们编写更简洁的代码。

## 相关资源

- [TypeScript 参数属性文档](https://www.typescriptlang.org/docs/handbook/2/classes.html#parameter-properties)
