# 3.2.4 抽象类与抽象方法

## 概述

抽象类是不能被实例化的类，用于定义类的模板。抽象方法是没有实现的方法，必须在子类中实现。本节介绍抽象类和抽象方法的定义和使用。

## 抽象类

### 定义

抽象类使用 `abstract` 关键字定义，不能被实例化，只能被继承。

### 语法

```ts
abstract class AbstractClass {
    // 属性和方法
}
```

### 示例

```ts
abstract class Animal {
    name: string;

    constructor(name: string) {
        this.name = name;
    }

    abstract makeSound(): void; // 抽象方法
}

// 错误：不能实例化抽象类
// let animal = new Animal("Animal"); // 错误

// 正确：继承抽象类
class Dog extends Animal {
    makeSound(): void {
        console.log("Woof!");
    }
}

let dog = new Dog("Buddy");
dog.makeSound(); // "Woof!"
```

## 抽象方法

### 定义

抽象方法使用 `abstract` 关键字定义，没有方法体，必须在子类中实现。

### 语法

```ts
abstract class AbstractClass {
    abstract methodName(): returnType;
}
```

### 示例

```ts
abstract class Shape {
    abstract area(): number;
    abstract perimeter(): number;
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

    perimeter(): number {
        return 2 * Math.PI * this.radius;
    }
}
```

## 抽象类 vs 接口

### 区别

| 特性           | 抽象类                 | 接口                     |
|:---------------|:-----------------------|:-------------------------|
| 实例化         | 不能                   | 不能                     |
| 实现           | 可以有实现             | 不能有实现（抽象方法除外）|
| 构造函数       | 有                     | 没有                     |
| 访问修饰符     | 支持                   | 不支持                   |
| 继承           | 类继承                 | 接口继承                 |
| 实现           | 类实现                 | 类实现                   |

### 使用场景

#### 使用抽象类

- 需要提供部分实现
- 需要构造函数
- 需要访问修饰符
- 需要共享代码

#### 使用接口

- 只需要定义契约
- 不需要实现
- 需要声明合并
- 需要多重实现

## 抽象属性

### 定义

抽象类可以定义抽象属性（TypeScript 4.0+）：

```ts
abstract class Animal {
    abstract name: string;
    abstract age: number;
}

class Dog extends Animal {
    name: string;
    age: number;

    constructor(name: string, age: number) {
        super();
        this.name = name;
        this.age = age;
    }
}
```

## 常见错误

### 错误 1：实例化抽象类

```ts
abstract class Animal {
    name: string;
}

// 错误：不能实例化抽象类
let animal = new Animal("Animal");
```

### 错误 2：未实现抽象方法

```ts
abstract class Animal {
    abstract makeSound(): void;
}

class Dog extends Animal {
    // 错误：未实现抽象方法
    // makeSound(): void { }
}
```

## 注意事项

1. **不能实例化**：抽象类不能被实例化
2. **必须实现**：子类必须实现所有抽象方法
3. **可以有实现**：抽象类可以包含非抽象方法
4. **构造函数**：抽象类可以有构造函数

## 最佳实践

1. **使用抽象类**：当需要提供部分实现时使用抽象类
2. **明确抽象方法**：明确标记抽象方法，确保子类实现
3. **合理设计**：合理设计抽象类的层次结构
4. **考虑接口**：在合适的情况下考虑使用接口

## 练习

1. **抽象类定义**：定义抽象类，包含抽象方法。

2. **抽象类继承**：继承抽象类，实现抽象方法。

3. **抽象属性**：定义和使用抽象属性。

4. **抽象类设计**：设计抽象类层次结构。

5. **实际应用**：在实际场景中应用抽象类。

完成以上练习后，继续学习下一节，了解接口实现。

## 总结

抽象类是不能被实例化的类，用于定义类的模板。抽象方法是没有实现的方法，必须在子类中实现。理解抽象类和抽象方法的使用，可以帮助我们设计更好的类层次结构。

## 相关资源

- [TypeScript 抽象类文档](https://www.typescriptlang.org/docs/handbook/2/classes.html#abstract-classes-and-members)
