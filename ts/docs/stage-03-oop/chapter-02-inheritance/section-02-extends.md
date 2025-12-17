# 3.2.2 类继承（extends）

## 概述

类继承使用 `extends` 关键字实现，允许子类继承父类的属性和方法。本节介绍类继承的语法、使用和特性。

## extends 关键字

### 基本语法

```ts
class ChildClass extends ParentClass {
    // 子类的属性和方法
}
```

### 示例

```ts
// 父类
class Animal {
    name: string;

    constructor(name: string) {
        this.name = name;
    }

    eat(): void {
        console.log(`${this.name} is eating`);
    }
}

// 子类
class Dog extends Animal {
    breed: string;

    constructor(name: string, breed: string) {
        super(name);
        this.breed = breed;
    }

    bark(): void {
        console.log(`${this.name} is barking`);
    }
}

let dog = new Dog("Buddy", "Golden Retriever");
dog.eat();  // 继承自 Animal
dog.bark(); // Dog 自己的方法
```

## 继承的属性

### 公共属性

子类继承父类的公共属性：

```ts
class Animal {
    public name: string;

    constructor(name: string) {
        this.name = name;
    }
}

class Dog extends Animal {
    breed: string;

    constructor(name: string, breed: string) {
        super(name);
        this.breed = breed;
    }
}

let dog = new Dog("Buddy", "Golden Retriever");
console.log(dog.name);  // 可以访问继承的属性
```

### 受保护属性

子类可以访问父类的受保护属性：

```ts
class Animal {
    protected name: string;

    constructor(name: string) {
        this.name = name;
    }
}

class Dog extends Animal {
    getName(): string {
        return this.name; // 子类可以访问 protected 属性
    }
}
```

### 私有属性

子类不能访问父类的私有属性：

```ts
class Animal {
    private name: string;

    constructor(name: string) {
        this.name = name;
    }
}

class Dog extends Animal {
    getName(): string {
        // return this.name; // 错误：不能访问父类的私有属性
        return "";
    }
}
```

## 继承的方法

### 公共方法

子类继承父类的公共方法：

```ts
class Animal {
    eat(): void {
        console.log("Eating");
    }
}

class Dog extends Animal {
    bark(): void {
        console.log("Barking");
    }
}

let dog = new Dog();
dog.eat();  // 继承自 Animal
dog.bark(); // Dog 自己的方法
```

### 方法重写

子类可以重写父类的方法：

```ts
class Animal {
    makeSound(): void {
        console.log("Some sound");
    }
}

class Dog extends Animal {
    makeSound(): void {
        console.log("Woof!"); // 重写父类方法
    }
}

let dog = new Dog();
dog.makeSound(); // "Woof!"
```

## 继承链

### 多级继承

继承可以形成多级继承链：

```ts
class Animal {
    name: string;

    constructor(name: string) {
        this.name = name;
    }
}

class Mammal extends Animal {
    warmBlooded: boolean = true;
}

class Dog extends Mammal {
    breed: string;

    constructor(name: string, breed: string) {
        super(name);
        this.breed = breed;
    }
}

let dog = new Dog("Buddy", "Golden Retriever");
console.log(dog.name);         // 继承自 Animal
console.log(dog.warmBlooded);  // 继承自 Mammal
console.log(dog.breed);        // Dog 自己的属性
```

## 构造函数继承

### super 调用

子类构造函数必须调用 `super()`：

```ts
class Animal {
    name: string;

    constructor(name: string) {
        this.name = name;
    }
}

class Dog extends Animal {
    breed: string;

    constructor(name: string, breed: string) {
        super(name); // 必须调用 super
        this.breed = breed;
    }
}
```

### 无构造函数

如果父类没有构造函数，子类可以不调用 `super()`：

```ts
class Animal {
    name: string = "Unknown";
}

class Dog extends Animal {
    breed: string = "Unknown";
    // 可以不定义构造函数
}
```

## 访问修饰符与继承

### public 继承

```ts
class Animal {
    public name: string;
}

class Dog extends Animal {
    // name 仍然是 public
}
```

### protected 继承

```ts
class Animal {
    protected name: string;
}

class Dog extends Animal {
    getName(): string {
        return this.name; // 可以访问
    }
}
```

### private 继承

```ts
class Animal {
    private name: string;
}

class Dog extends Animal {
    getName(): string {
        // return this.name; // 错误：不能访问
        return "";
    }
}
```

## 常见错误

### 错误 1：未调用 super

```ts
class Animal {
    name: string;

    constructor(name: string) {
        this.name = name;
    }
}

class Dog extends Animal {
    breed: string;

    constructor(name: string, breed: string) {
        // 错误：必须调用 super
        this.breed = breed;
    }
}
```

### 错误 2：访问私有成员

```ts
class Animal {
    private name: string;
}

class Dog extends Animal {
    getName(): string {
        // return this.name; // 错误：不能访问私有成员
        return "";
    }
}
```

## 注意事项

1. **单一继承**：TypeScript 只支持单一继承
2. **super 调用**：子类构造函数必须调用 `super()`
3. **访问控制**：子类可以访问 `public` 和 `protected` 成员
4. **方法重写**：子类可以重写父类方法

## 最佳实践

1. **合理继承**：只在 is-a 关系时使用继承
2. **调用 super**：子类构造函数必须调用 `super()`
3. **访问控制**：合理使用访问修饰符
4. **避免深度继承**：避免过深的继承层次

## 练习

1. **类继承**：定义父类和子类，实现类继承。

2. **属性继承**：理解不同访问修饰符的属性继承。

3. **方法继承**：理解方法的继承和重写。

4. **继承链**：创建多级继承链。

5. **实际应用**：在实际场景中应用类继承。

完成以上练习后，继续学习下一节，了解 super 关键字。

## 总结

类继承使用 `extends` 关键字实现，允许子类继承父类的属性和方法。子类可以访问 `public` 和 `protected` 成员，可以重写父类方法。理解类继承的使用是学习面向对象编程的关键。

## 相关资源

- [TypeScript 类继承文档](https://www.typescriptlang.org/docs/handbook/2/classes.html#extends-clauses)
