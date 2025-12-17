# 2.1.5 接口继承与合并

## 概述

接口支持继承和声明合并，可以扩展和组合接口定义。本节介绍接口继承和声明合并的使用。

## 接口继承

### 定义

接口可以通过 `extends` 关键字继承其他接口，获得父接口的所有成员。

### 语法

```ts
interface ChildInterface extends ParentInterface {
    // 子接口的额外成员
}
```

### 单继承

```ts
// 父接口
interface Animal {
    name: string;
    age: number;
}

// 子接口
interface Dog extends Animal {
    breed: string;
}

// 实现子接口
let dog: Dog = {
    name: "Buddy",
    age: 3,
    breed: "Golden Retriever"
};
```

### 多继承

接口可以继承多个接口：

```ts
interface Flyable {
    fly(): void;
}

interface Swimmable {
    swim(): void;
}

// 多继承
interface Duck extends Flyable, Swimmable {
    name: string;
}

let duck: Duck = {
    name: "Donald",
    fly() {
        console.log("Flying");
    },
    swim() {
        console.log("Swimming");
    }
};
```

### 继承链

接口可以形成继承链：

```ts
interface Animal {
    name: string;
}

interface Mammal extends Animal {
    warmBlooded: boolean;
}

interface Dog extends Mammal {
    breed: string;
}

let dog: Dog = {
    name: "Buddy",
    warmBlooded: true,
    breed: "Golden Retriever"
};
```

### 覆盖属性

子接口可以覆盖父接口的属性类型（必须是兼容类型）：

```ts
interface Base {
    value: string | number;
}

interface Derived extends Base {
    value: string; // 覆盖为更具体的类型
}

let derived: Derived = {
    value: "hello" // 只能是 string
};
```

## 接口合并

### 定义

TypeScript 支持接口声明合并，多个同名接口声明会自动合并为一个接口。

### 语法

```ts
// 第一个声明
interface User {
    name: string;
}

// 第二个声明（自动合并）
interface User {
    age: number;
}

// 合并后的 User 包含 name 和 age
let user: User = {
    name: "John",
    age: 30
};
```

### 属性合并

同名属性必须类型兼容：

```ts
interface User {
    name: string;
}

interface User {
    name: string; // 相同类型，可以合并
    age: number;
}
```

如果类型不兼容，会报错：

```ts
interface User {
    name: string;
}

interface User {
    name: number; // 错误：类型不兼容
}
```

### 方法合并

方法会合并为函数重载：

```ts
interface Calculator {
    add(a: number, b: number): number;
}

interface Calculator {
    add(a: string, b: string): string; // 方法重载
    subtract(a: number, b: number): number;
}

// 合并后的 Calculator 有两个 add 重载
let calc: Calculator = {
    add(a: any, b: any): any {
        return a + b;
    },
    subtract(a: number, b: number): number {
        return a - b;
    }
};
```

### 与继承的区别

| 特性       | 继承（extends）        | 合并（声明合并）       |
|:-----------|:-----------------------|:-----------------------|
| 语法       | `extends`              | 同名接口声明           |
| 关系       | 父子关系               | 同一接口的不同声明     |
| 使用场景   | 扩展接口               | 扩展第三方库接口       |
| 可见性     | 明确继承关系           | 自动合并               |

## 使用场景

### 接口继承使用场景

1. **类型层次**：建立类型层次结构

```ts
interface Vehicle {
    speed: number;
}

interface Car extends Vehicle {
    wheels: number;
}

interface Plane extends Vehicle {
    wings: number;
}
```

2. **代码复用**：复用公共属性

```ts
interface BaseEntity {
    id: number;
    createdAt: Date;
}

interface User extends BaseEntity {
    name: string;
}

interface Product extends BaseEntity {
    title: string;
}
```

### 接口合并使用场景

1. **扩展第三方库**：扩展第三方库的类型定义

```ts
// 第三方库的接口
interface Window {
    // ...
}

// 扩展 Window 接口
interface Window {
    myCustomProperty: string;
}
```

2. **模块扩展**：扩展模块的类型定义

```ts
// 原始定义
interface Config {
    apiUrl: string;
}

// 扩展定义（可能在不同文件中）
interface Config {
    timeout: number;
}
```

## 常见错误

### 错误 1：类型不兼容的合并

```ts
interface User {
    name: string;
}

interface User {
    name: number; // 错误：类型不兼容
}
```

### 错误 2：循环继承

```ts
interface A extends B {
    // ...
}

interface B extends A {
    // 错误：循环继承
}
```

## 注意事项

1. **继承关系**：接口继承建立明确的父子关系
2. **合并规则**：接口合并要求同名属性类型兼容
3. **方法重载**：合并的方法会形成函数重载
4. **避免循环**：避免循环继承

## 最佳实践

1. **使用继承**：建立清晰的类型层次结构
2. **使用合并**：扩展第三方库和模块的类型
3. **避免过度合并**：避免过度使用接口合并
4. **明确关系**：优先使用继承，合并作为补充

## 练习

1. **接口继承**：定义接口继承关系，建立类型层次。

2. **多继承**：练习接口的多继承。

3. **接口合并**：定义同名接口，观察自动合并。

4. **方法重载**：通过接口合并创建方法重载。

5. **实际应用**：在实际场景中应用接口继承和合并。

完成以上练习后，接口章节学习完成。可以继续学习下一章：类型别名。

## 总结

接口支持继承和声明合并。接口继承通过 `extends` 关键字建立类型层次，接口合并通过同名接口声明自动合并。理解接口继承和合并的使用场景，可以帮助我们更好地组织类型系统。

## 相关资源

- [TypeScript 接口继承文档](https://www.typescriptlang.org/docs/handbook/2/objects.html#extending-types)
- [TypeScript 声明合并文档](https://www.typescriptlang.org/docs/handbook/declaration-merging.html)
