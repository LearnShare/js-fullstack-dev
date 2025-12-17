# 3.1.4 访问修饰符（public、private、protected）

## 概述

访问修饰符控制类成员的可见性和访问权限。本节介绍 TypeScript 的三种访问修饰符：public、private、protected。

## 访问修饰符类型

### public（公共）

`public` 是默认的访问修饰符，成员可以在任何地方访问。

### private（私有）

`private` 成员只能在类内部访问。

### protected（受保护）

`protected` 成员可以在类内部和子类中访问。

## public 修饰符

### 定义

`public` 成员可以在任何地方访问（默认行为）。

### 示例

```ts
class Person {
    public name: string;
    public age: number;

    public constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }

    public greet(): string {
        return `Hello, I'm ${this.name}`;
    }
}

let person = new Person("John", 30);
console.log(person.name);        // 可以访问
console.log(person.age);         // 可以访问
console.log(person.greet());    // 可以访问
```

### 默认行为

如果不指定访问修饰符，默认为 `public`：

```ts
class Person {
    name: string;  // 默认为 public
    age: number;   // 默认为 public

    greet(): string {  // 默认为 public
        return `Hello, I'm ${this.name}`;
    }
}
```

## private 修饰符

### 定义

`private` 成员只能在类内部访问，外部无法访问。

### 示例

```ts
class BankAccount {
    private balance: number = 0;

    deposit(amount: number): void {
        if (amount > 0) {
            this.balance += amount; // 类内部可以访问
        }
    }

    withdraw(amount: number): void {
        if (amount > 0 && amount <= this.balance) {
            this.balance -= amount; // 类内部可以访问
        }
    }

    getBalance(): number {
        return this.balance; // 类内部可以访问
    }
}

let account = new BankAccount();
account.deposit(100);
console.log(account.getBalance()); // 100

// 错误：外部不能访问私有成员
// console.log(account.balance); // 错误
```

### 私有方法

```ts
class Calculator {
    private validate(value: number): boolean {
        return value >= 0;
    }

    add(a: number, b: number): number {
        if (this.validate(a) && this.validate(b)) {
            return a + b;
        }
        throw new Error("Invalid values");
    }
}
```

## protected 修饰符

### 定义

`protected` 成员可以在类内部和子类中访问，但外部不能访问。

### 示例

```ts
class Animal {
    protected name: string;

    constructor(name: string) {
        this.name = name;
    }

    protected makeSound(): void {
        console.log("Some sound");
    }
}

class Dog extends Animal {
    bark(): void {
        console.log(`${this.name} barks`); // 子类可以访问 protected 成员
        this.makeSound(); // 子类可以访问 protected 方法
    }
}

let dog = new Dog("Buddy");
dog.bark(); // "Buddy barks"

// 错误：外部不能访问 protected 成员
// console.log(dog.name); // 错误
// dog.makeSound(); // 错误
```

## 访问修饰符对比

### 对比表

| 修饰符     | 类内部 | 子类   | 外部   | 默认 |
|:-----------|:-------|:-------|:-------|:-----|
| `public`   | ✅     | ✅     | ✅     | 是   |
| `private`  | ✅     | ❌     | ❌     | 否   |
| `protected`| ✅     | ✅     | ❌     | 否   |

### 示例对比

```ts
class Example {
    public publicProp: string = "public";
    private privateProp: string = "private";
    protected protectedProp: string = "protected";

    public publicMethod(): void {
        console.log(this.publicProp);      // ✅ 可以访问
        console.log(this.privateProp);    // ✅ 可以访问
        console.log(this.protectedProp);  // ✅ 可以访问
    }
}

class SubExample extends Example {
    test(): void {
        console.log(this.publicProp);      // ✅ 可以访问
        // console.log(this.privateProp);  // ❌ 不能访问
        console.log(this.protectedProp);  // ✅ 可以访问
    }
}

let example = new Example();
console.log(example.publicProp);      // ✅ 可以访问
// console.log(example.privateProp);  // ❌ 不能访问
// console.log(example.protectedProp); // ❌ 不能访问
```

## 使用场景

### public 使用场景

- 需要外部访问的属性和方法
- API 接口方法
- 公共配置

### private 使用场景

- 内部实现细节
- 不应该被外部访问的数据
- 辅助方法

### protected 使用场景

- 需要在子类中访问的成员
- 模板方法模式
- 可扩展的类设计

## 常见错误

### 错误 1：访问私有成员

```ts
class Person {
    private name: string;

    constructor(name: string) {
        this.name = name;
    }
}

let person = new Person("John");
// console.log(person.name); // 错误：不能访问私有成员
```

### 错误 2：子类访问私有成员

```ts
class Animal {
    private name: string;
}

class Dog extends Animal {
    getName(): string {
        // return this.name; // 错误：不能访问父类的私有成员
        return "";
    }
}
```

## 注意事项

1. **默认 public**：如果不指定访问修饰符，默认为 `public`
2. **编译时检查**：访问修饰符只在编译时检查，运行时不存在
3. **类型兼容**：私有成员影响类型兼容性
4. **子类访问**：`protected` 成员可以在子类中访问

## 最佳实践

1. **最小权限原则**：使用最小必要的访问权限
2. **私有化实现**：将实现细节设为私有
3. **保护扩展点**：将需要在子类中访问的成员设为 `protected`
4. **明确意图**：使用访问修饰符明确表达设计意图

## 练习

1. **访问修饰符**：定义使用不同访问修饰符的类，理解访问控制。

2. **私有成员**：使用私有成员实现数据封装。

3. **受保护成员**：使用受保护成员实现可扩展的类设计。

4. **访问控制**：体验不同访问修饰符的访问限制。

5. **实际应用**：在实际场景中应用访问修饰符。

完成以上练习后，继续学习下一节，了解只读属性与静态成员。

## 总结

访问修饰符控制类成员的可见性和访问权限。`public` 是默认修饰符，成员可以在任何地方访问。`private` 成员只能在类内部访问。`protected` 成员可以在类内部和子类中访问。理解访问修饰符的使用可以帮助我们实现更好的封装和设计。

## 相关资源

- [TypeScript 访问修饰符文档](https://www.typescriptlang.org/docs/handbook/2/classes.html#member-visibility)
