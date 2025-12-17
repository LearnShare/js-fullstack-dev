# 5.6.4 类型兼容性规则

## 概述

本节详细介绍 TypeScript 类型兼容性的各种规则，包括基本类型、对象类型、函数类型、数组类型等。

## 基本类型兼容性

### 相同类型

```ts
let a: number = 1;
let b: number = a; // 兼容
```

### 字面量类型

```ts
let a: 1 = 1;
let b: number = a; // 兼容：字面量类型可以赋值给基础类型
```

### 联合类型

```ts
let a: number = 1;
let b: number | string = a; // 兼容

let c: string = "hello";
let d: number | string = c; // 兼容
```

## 对象类型兼容性

### 属性兼容性

```ts
interface Source {
    x: number;
    y: number;
}

interface Target {
    x: number;
}

let source: Source = { x: 1, y: 2 };
let target: Target = source; // 兼容：Target 的属性都在 Source 中
```

### 额外属性

```ts
interface Point {
    x: number;
    y: number;
}

let point: Point = { x: 1, y: 2, z: 3 }; // 兼容：可以包含额外属性
```

### 可选属性

```ts
interface Source {
    x: number;
    y?: number;
}

interface Target {
    x: number;
}

let source: Source = { x: 1 };
let target: Target = source; // 兼容
```

## 函数类型兼容性

### 参数数量

```ts
let func1: (x: number) => number;
let func2: (x: number, y: number) => number;

func1 = func2; // 不兼容：参数数量不同
func2 = func1; // 兼容：可以忽略额外参数
```

### 参数类型

```ts
let func1: (x: Animal) => void;
let func2: (x: Dog) => void;

func1 = func2; // 不兼容：参数类型不匹配（需要逆变）
func2 = func1; // 兼容：参数逆变
```

### 返回值类型

```ts
let func1: () => Dog;
let func2: () => Animal;

func1 = func2; // 不兼容：返回值类型不匹配
func2 = func1; // 兼容：返回值协变
```

## 数组类型兼容性

### 元素类型

```ts
let arr1: number[];
let arr2: (number | string)[];

arr1 = arr2; // 不兼容：元素类型不匹配
arr2 = arr1; // 兼容：元素协变
```

### 只读数组

```ts
let arr1: number[] = [1, 2, 3];
let arr2: readonly number[] = arr1; // 兼容

// arr1 = arr2; // 不兼容：只读数组不能赋值给可变数组
```

## 泛型兼容性

### 相同泛型参数

```ts
let arr1: Array<number>;
let arr2: Array<number>;

arr1 = arr2; // 兼容：相同泛型参数
```

### 不同泛型参数

```ts
let arr1: Array<number>;
let arr2: Array<string>;

// arr1 = arr2; // 不兼容：泛型参数不同
```

## 使用场景

### 1. 类型赋值

```ts
interface Animal {
    name: string;
}

interface Dog extends Animal {
    breed: string;
}

let animal: Animal;
let dog: Dog = { name: "Dog", breed: "Golden" };
animal = dog; // 兼容
```

### 2. 函数参数

```ts
function process(animal: Animal): void {
    // ...
}

let dog: Dog = { name: "Dog", breed: "Golden" };
process(dog); // 兼容
```

### 3. 数组赋值

```ts
let dogs: Dog[] = [{ name: "Dog", breed: "Golden" }];
let animals: Animal[] = dogs; // 兼容：数组协变
```

## 常见错误

### 错误 1：参数类型不匹配

```ts
function process(handler: (animal: Animal) => void): void {
    // ...
}

let dogHandler = (dog: Dog) => {
    console.log(dog.breed);
};

// process(dogHandler); // 不兼容：参数类型不匹配
```

### 错误 2：返回值类型不匹配

```ts
function getAnimal(): Animal {
    return { name: "Animal" };
}

let getDog: () => Dog = getAnimal; // 不兼容：返回值类型不匹配
```

## 注意事项

1. **结构化类型**：TypeScript 使用结构化类型系统
2. **函数兼容性**：函数有特殊的兼容性规则
3. **协变逆变**：理解协变和逆变
4. **类型安全**：类型兼容性提供类型安全

## 最佳实践

1. **理解规则**：理解各种类型兼容性规则
2. **函数兼容性**：注意函数类型的兼容性规则
3. **协变逆变**：理解协变和逆变的应用
4. **类型安全**：利用类型兼容性提高类型安全

## 练习

1. **基本类型**：练习基本类型兼容性。

2. **对象类型**：练习对象类型兼容性。

3. **函数类型**：练习函数类型兼容性。

4. **实际应用**：在实际场景中应用类型兼容性规则。

完成以上练习后，类型兼容性章节学习完成。阶段五学习完成，可以继续学习阶段六：模块化与声明文件。

## 总结

类型兼容性规则包括基本类型、对象类型、函数类型、数组类型等。函数类型有特殊的兼容性规则（参数逆变、返回值协变）。理解类型兼容性规则是学习 TypeScript 类型系统的关键。

## 相关资源

- [TypeScript 类型兼容性文档](https://www.typescriptlang.org/docs/handbook/type-compatibility.html)
