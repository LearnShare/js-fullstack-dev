# 3.2.3 super 关键字

## 概述

`super` 关键字用于在子类中访问父类的构造函数和方法。本节介绍 `super` 关键字的使用场景和注意事项。

## super 的作用

### 定义

`super` 关键字用于：
1. 调用父类的构造函数
2. 调用父类的方法

## 调用父类构造函数

### 基本用法

在子类构造函数中使用 `super()` 调用父类构造函数：

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
        super(name); // 调用父类构造函数
        this.breed = breed;
    }
}
```

### 必须调用

如果父类有构造函数，子类构造函数必须调用 `super()`：

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
        // 错误：必须调用 super()
        this.breed = breed;
    }
}
```

### 调用顺序

`super()` 必须在访问 `this` 之前调用：

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
        super(name); // 必须先调用 super
        this.breed = breed; // 然后才能使用 this
    }
}
```

## 调用父类方法

### 基本用法

使用 `super.methodName()` 调用父类方法：

```ts
class Animal {
    makeSound(): void {
        console.log("Some sound");
    }
}

class Dog extends Animal {
    makeSound(): void {
        super.makeSound(); // 调用父类方法
        console.log("Woof!");
    }
}

let dog = new Dog();
dog.makeSound();
// 输出：
// "Some sound"
// "Woof!"
```

### 方法重写中的 super

在重写的方法中调用父类方法：

```ts
class Animal {
    move(): void {
        console.log("Moving");
    }
}

class Dog extends Animal {
    move(): void {
        super.move(); // 调用父类方法
        console.log("Running");
    }
}
```

## super 的使用场景

### 1. 构造函数调用

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
        super(name); // 调用父类构造函数
        this.breed = breed;
    }
}
```

### 2. 方法扩展

```ts
class Animal {
    eat(): void {
        console.log("Eating");
    }
}

class Dog extends Animal {
    eat(): void {
        super.eat(); // 先执行父类方法
        console.log("Eating dog food"); // 然后扩展
    }
}
```

### 3. 部分重写

```ts
class Animal {
    describe(): string {
        return `I am an animal`;
    }
}

class Dog extends Animal {
    breed: string;

    constructor(breed: string) {
        super();
        this.breed = breed;
    }

    describe(): string {
        return `${super.describe()} and I am a ${this.breed}`;
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
        // 错误：必须调用 super()
        this.breed = breed;
    }
}
```

### 错误 2：在 super 之前使用 this

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
        this.breed = breed; // 错误：必须在 super 之后
        super(name);
    }
}
```

### 错误 3：在静态方法中使用 super

```ts
class Animal {
    static getName(): string {
        return "Animal";
    }
}

class Dog extends Animal {
    static getName(): string {
        return super.getName(); // 错误：静态方法中不能使用 super
    }
}
```

## 注意事项

1. **必须调用**：如果父类有构造函数，子类必须调用 `super()`
2. **调用顺序**：`super()` 必须在访问 `this` 之前调用
3. **静态方法**：静态方法中不能使用 `super`
4. **方法调用**：`super.methodName()` 用于调用父类方法

## 最佳实践

1. **及时调用**：在子类构造函数中及时调用 `super()`
2. **正确顺序**：确保 `super()` 在 `this` 之前调用
3. **方法扩展**：使用 `super` 扩展父类方法而不是完全替换
4. **理解作用**：理解 `super` 的作用和使用场景

## 练习

1. **super 调用**：在子类构造函数中调用 `super()`。

2. **方法调用**：使用 `super` 调用父类方法。

3. **方法扩展**：在重写的方法中使用 `super` 扩展父类方法。

4. **调用顺序**：理解 `super()` 的调用顺序要求。

5. **实际应用**：在实际场景中应用 `super` 关键字。

完成以上练习后，继续学习下一节，了解抽象类与抽象方法。

## 总结

`super` 关键字用于在子类中访问父类的构造函数和方法。在子类构造函数中必须调用 `super()`，在重写的方法中可以使用 `super.methodName()` 调用父类方法。理解 `super` 关键字的使用是学习类继承的关键。

## 相关资源

- [TypeScript super 关键字文档](https://www.typescriptlang.org/docs/handbook/2/classes.html#overriding-methods)
