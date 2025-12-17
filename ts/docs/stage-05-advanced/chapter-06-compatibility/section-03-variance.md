# 5.6.3 协变与逆变

## 概述

协变和逆变描述了类型兼容性的方向性。本节介绍协变和逆变的概念和应用。

## 什么是协变

### 定义

协变是指子类型可以赋值给父类型。

### 基本概念

```ts
interface Animal {
    name: string;
}

interface Dog extends Animal {
    breed: string;
}

let animal: Animal;
let dog: Dog = { name: "Dog", breed: "Golden" };

animal = dog; // 协变：Dog 可以赋值给 Animal
```

## 什么是逆变

### 定义

逆变是指父类型可以赋值给子类型（在函数参数中）。

### 基本概念

```ts
type AnimalHandler = (animal: Animal) => void;
type DogHandler = (dog: Dog) => void;

let animalHandler: AnimalHandler = (animal) => {
    console.log(animal.name);
};

let dogHandler: DogHandler = animalHandler; // 逆变：AnimalHandler 可以赋值给 DogHandler
```

## 函数类型兼容性

### 参数逆变

函数参数是逆变的：

```ts
type Func1 = (x: Animal) => void;
type Func2 = (x: Dog) => void;

let func1: Func1 = (animal) => {
    console.log(animal.name);
};

let func2: Func2 = func1; // 兼容：参数逆变
```

### 返回值协变

函数返回值是协变的：

```ts
type Func1 = () => Dog;
type Func2 = () => Animal;

let func1: Func1 = () => ({ name: "Dog", breed: "Golden" });
let func2: Func2 = func1; // 兼容：返回值协变
```

## 数组协变

### 数组元素协变

数组元素是协变的：

```ts
let dogs: Dog[] = [{ name: "Dog", breed: "Golden" }];
let animals: Animal[] = dogs; // 兼容：数组协变
```

## 使用场景

### 1. 函数参数

```ts
function processAnimals(handler: (animal: Animal) => void): void {
    handler({ name: "Animal" });
}

let dogHandler = (dog: Dog) => {
    console.log(dog.breed);
};

// processAnimals(dogHandler); // 不兼容：参数需要逆变
```

### 2. 函数返回值

```ts
function getAnimal(): Animal {
    return { name: "Animal" };
}

function getDog(): Dog {
    return { name: "Dog", breed: "Golden" };
}

let animalFunc: () => Animal = getDog; // 兼容：返回值协变
```

## 常见错误

### 错误 1：不理解逆变

```ts
type AnimalHandler = (animal: Animal) => void;
type DogHandler = (dog: Dog) => void;

let dogHandler: DogHandler = (dog) => {
    console.log(dog.breed);
};

// 错误：不理解逆变
// let animalHandler: AnimalHandler = dogHandler;
```

### 错误 2：数组协变问题

```ts
let dogs: Dog[] = [{ name: "Dog", breed: "Golden" }];
let animals: Animal[] = dogs;

animals.push({ name: "Cat" }); // 运行时错误：dogs 数组中混入了非 Dog 对象
```

## 注意事项

1. **参数逆变**：函数参数是逆变的
2. **返回值协变**：函数返回值是协变的
3. **数组协变**：数组元素是协变的
4. **类型安全**：理解协变和逆变有助于类型安全

## 最佳实践

1. **理解协变逆变**：理解协变和逆变的概念
2. **函数参数**：注意函数参数的逆变
3. **函数返回值**：注意函数返回值的协变
4. **类型安全**：利用协变和逆变提高类型安全

## 练习

1. **协变**：理解协变的概念和应用。

2. **逆变**：理解逆变的概念和应用。

3. **函数兼容性**：理解函数类型的协变和逆变。

4. **实际应用**：在实际场景中应用协变和逆变。

完成以上练习后，继续学习下一节，了解类型兼容性规则。

## 总结

协变是指子类型可以赋值给父类型，逆变是指父类型可以赋值给子类型（在函数参数中）。函数参数是逆变的，返回值是协变的。理解协变和逆变是学习类型兼容性的关键。

## 相关资源

- [TypeScript 协变与逆变文档](https://www.typescriptlang.org/docs/handbook/type-compatibility.html#variance)
