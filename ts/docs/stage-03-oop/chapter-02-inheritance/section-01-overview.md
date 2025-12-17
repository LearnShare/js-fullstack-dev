# 3.2.1 继承与多态概述

## 概述

继承是面向对象编程的核心特性，允许子类继承父类的属性和方法。多态允许使用父类类型引用子类对象。本节介绍继承和多态的概念、作用和优势。

## 什么是继承

### 定义

继承是一种机制，允许子类继承父类的属性和方法，并可以添加或重写自己的属性和方法。

### 基本概念

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

## 继承的作用

### 1. 代码复用

继承允许子类复用父类的代码：

```ts
class Animal {
    name: string;

    constructor(name: string) {
        this.name = name;
    }

    eat(): void {
        console.log(`${this.name} is eating`);
    }
}

// 多个子类复用父类代码
class Dog extends Animal {
    bark(): void {
        console.log("Woof!");
    }
}

class Cat extends Animal {
    meow(): void {
        console.log("Meow!");
    }
}
```

### 2. 扩展功能

子类可以添加新的属性和方法：

```ts
class Animal {
    name: string;
}

class Dog extends Animal {
    breed: string; // 新增属性

    bark(): void { // 新增方法
        console.log("Woof!");
    }
}
```

### 3. 方法重写

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
```

## 什么是多态

### 定义

多态是指同一个接口可以有不同的实现，或者使用父类类型引用子类对象。

### 基本概念

```ts
class Animal {
    makeSound(): void {
        console.log("Some sound");
    }
}

class Dog extends Animal {
    makeSound(): void {
        console.log("Woof!");
    }
}

class Cat extends Animal {
    makeSound(): void {
        console.log("Meow!");
    }
}

// 多态：使用父类类型引用子类对象
let animals: Animal[] = [
    new Dog(),
    new Cat()
];

animals.forEach(animal => {
    animal.makeSound(); // 调用各自的重写方法
});
```

## 多态的作用

### 1. 统一接口

多态提供统一的接口：

```ts
class Shape {
    area(): number {
        return 0;
    }
}

class Circle extends Shape {
    radius: number;

    constructor(radius: number) {
        super();
        this.radius = radius;
    }

    area(): number {
        return Math.PI * this.radius ** 2;
    }
}

class Rectangle extends Shape {
    width: number;
    height: number;

    constructor(width: number, height: number) {
        super();
        this.width = width;
        this.height = height;
    }

    area(): number {
        return this.width * this.height;
    }
}

// 多态：统一处理不同类型的形状
function calculateTotalArea(shapes: Shape[]): number {
    return shapes.reduce((total, shape) => total + shape.area(), 0);
}
```

### 2. 灵活性

多态提供灵活性：

```ts
class Animal {
    move(): void {
        console.log("Moving");
    }
}

class Dog extends Animal {
    move(): void {
        console.log("Running");
    }
}

class Fish extends Animal {
    move(): void {
        console.log("Swimming");
    }
}

// 可以替换使用
let animal: Animal = new Dog();
animal.move(); // "Running"

animal = new Fish();
animal.move(); // "Swimming"
```

## 继承 vs 组合

### 区别

| 特性       | 继承（Inheritance）      | 组合（Composition）      |
|:-----------|:-------------------------|:-------------------------|
| 关系       | "是一个"（is-a）         | "有一个"（has-a）        |
| 耦合度     | 高                       | 低                       |
| 灵活性     | 低                       | 高                       |
| 使用场景   | 类型层次结构             | 功能组合                 |

### 选择建议

#### 使用继承

- 子类是父类的特殊类型（is-a 关系）
- 需要多态
- 需要方法重写

#### 使用组合

- 需要功能组合（has-a 关系）
- 需要低耦合
- 需要灵活性

## 注意事项

1. **单一继承**：TypeScript 只支持单一继承（一个类只能继承一个父类）
2. **super 调用**：子类构造函数必须调用 `super()`
3. **方法重写**：子类可以重写父类方法
4. **访问修饰符**：`protected` 成员可以在子类中访问

## 最佳实践

1. **合理使用继承**：只在 is-a 关系时使用继承
2. **避免深度继承**：避免过深的继承层次
3. **使用多态**：利用多态提供统一的接口
4. **考虑组合**：在合适的情况下使用组合替代继承

## 练习

1. **继承实现**：定义父类和子类，实现类继承。

2. **方法重写**：在子类中重写父类方法，理解重写机制。

3. **多态实践**：使用多态处理不同类型的对象。

4. **继承链**：创建多级继承链，理解继承关系。

5. **实际应用**：在实际场景中应用继承和多态。

完成以上练习后，继续学习下一节，了解类继承（extends）。

## 总结

继承允许子类继承父类的属性和方法，实现代码复用和功能扩展。多态允许使用父类类型引用子类对象，提供统一的接口。理解继承和多态的概念和作用是学习面向对象编程的关键。

## 相关资源

- [TypeScript 继承文档](https://www.typescriptlang.org/docs/handbook/2/classes.html#extends-clauses)
