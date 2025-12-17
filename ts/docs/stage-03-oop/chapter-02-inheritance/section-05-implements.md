# 3.2.5 接口实现（implements）

## 概述

类可以使用 `implements` 关键字实现接口，确保类符合接口定义的契约。本节介绍接口实现的语法和使用。

## implements 关键字

### 基本语法

```ts
class ClassName implements InterfaceName {
    // 实现接口要求的所有成员
}
```

### 示例

```ts
// 定义接口
interface Flyable {
    fly(): void;
}

// 实现接口
class Bird implements Flyable {
    fly(): void {
        console.log("Flying");
    }
}

let bird = new Bird();
bird.fly(); // "Flying"
```

## 实现多个接口

### 语法

类可以实现多个接口：

```ts
class ClassName implements Interface1, Interface2 {
    // 实现所有接口的成员
}
```

### 示例

```ts
interface Flyable {
    fly(): void;
}

interface Swimmable {
    swim(): void;
}

// 实现多个接口
class Duck implements Flyable, Swimmable {
    fly(): void {
        console.log("Flying");
    }

    swim(): void {
        console.log("Swimming");
    }
}
```

## 接口要求

### 必须实现所有成员

类必须实现接口中定义的所有成员：

```ts
interface User {
    name: string;
    age: number;
    greet(): string;
}

class Person implements User {
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
```

### 可选成员

接口中的可选成员可以不实现：

```ts
interface User {
    name: string;
    age?: number; // 可选
}

class Person implements User {
    name: string;
    // age 可以不实现
}
```

## 接口继承与实现

### 同时继承和实现

类可以同时继承类和实现接口：

```ts
class Animal {
    name: string;

    constructor(name: string) {
        this.name = name;
    }
}

interface Flyable {
    fly(): void;
}

// 同时继承和实现
class Bird extends Animal implements Flyable {
    fly(): void {
        console.log("Flying");
    }
}
```

### 顺序

`extends` 必须在 `implements` 之前：

```ts
// 正确
class Bird extends Animal implements Flyable {
    // ...
}

// 错误
class Bird implements Flyable extends Animal {
    // 错误：顺序错误
}
```

## 接口实现 vs 类继承

### 区别

| 特性       | 接口实现（implements）  | 类继承（extends）        |
|:-----------|:------------------------|:-------------------------|
| 关键字     | `implements`            | `extends`                |
| 关系       | 实现契约                | 继承实现                 |
| 数量       | 可以实现多个            | 只能继承一个             |
| 代码复用   | 不提供                  | 提供                     |

### 使用场景

#### 使用接口实现

- 需要实现多个契约
- 不需要代码复用
- 需要类型检查

#### 使用类继承

- 需要代码复用
- 需要继承实现
- is-a 关系

## 常见错误

### 错误 1：未实现所有成员

```ts
interface User {
    name: string;
    age: number;
}

class Person implements User {
    name: string;
    // 错误：缺少 age 属性
}
```

### 错误 2：类型不匹配

```ts
interface User {
    name: string;
    age: number;
}

class Person implements User {
    name: string;
    age: string; // 错误：类型不匹配
}
```

## 注意事项

1. **必须实现**：类必须实现接口中定义的所有必需成员
2. **类型匹配**：实现的成员类型必须与接口定义匹配
3. **多个接口**：类可以实现多个接口
4. **同时继承**：类可以同时继承类和实现接口

## 最佳实践

1. **使用接口**：使用接口定义类型契约
2. **实现接口**：类实现接口确保符合契约
3. **多个接口**：在需要时实现多个接口
4. **明确意图**：使用接口实现明确表达设计意图

## 练习

1. **接口实现**：定义接口，类实现接口。

2. **多个接口**：类实现多个接口。

3. **继承和实现**：类同时继承类和实现接口。

4. **类型检查**：体验接口实现的类型检查。

5. **实际应用**：在实际场景中应用接口实现。

完成以上练习后，继承与多态章节学习完成。可以继续学习下一章：现代类特性。

## 总结

类可以使用 `implements` 关键字实现接口，确保类符合接口定义的契约。类可以实现多个接口，也可以同时继承类和实现接口。理解接口实现的使用，可以帮助我们设计更好的类型系统。

## 相关资源

- [TypeScript 接口实现文档](https://www.typescriptlang.org/docs/handbook/2/classes.html#implements-clauses)
