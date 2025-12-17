# 1.2.3 数组与元组

## 概述

数组和元组是 TypeScript 中用于存储多个值的数据结构。本节介绍数组类型和元组类型的定义、使用和区别。

## 数组类型

### 定义

数组类型表示具有相同类型元素的集合。

### 语法

#### 方式一：类型 + 方括号

```ts
let numbers: number[] = [1, 2, 3, 4, 5];
let names: string[] = ["John", "Jane", "Bob"];
```

#### 方式二：Array 泛型

```ts
let numbers: Array<number> = [1, 2, 3, 4, 5];
let names: Array<string> = ["John", "Jane", "Bob"];
```

### 基本用法

```ts
// 数字数组
let scores: number[] = [85, 90, 78, 92];

// 字符串数组
let fruits: string[] = ["apple", "banana", "orange"];

// 布尔数组
let flags: boolean[] = [true, false, true];

// 空数组
let empty: number[] = [];
```

### 数组操作

```ts
let numbers: number[] = [1, 2, 3];

// 访问元素
let first: number = numbers[0]; // 1

// 修改元素
numbers[0] = 10;

// 添加元素
numbers.push(4);

// 获取长度
let length: number = numbers.length;
```

### 只读数组

使用 `readonly` 关键字创建只读数组：

```ts
let numbers: readonly number[] = [1, 2, 3];
// numbers.push(4); // 错误：只读数组不能修改
// numbers[0] = 10; // 错误：只读数组不能修改
```

或使用 `ReadonlyArray`：

```ts
let numbers: ReadonlyArray<number> = [1, 2, 3];
```

### 多维数组

```ts
// 二维数组
let matrix: number[][] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

// 三维数组
let cube: number[][][] = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
];
```

## 元组类型

### 定义

元组类型表示固定长度和类型的数组。

### 语法

```ts
let tuple: [string, number] = ["John", 30];
```

### 基本用法

```ts
// 二元组
let person: [string, number] = ["John", 30];

// 三元组
let point: [number, number, number] = [1, 2, 3];

// 不同类型
let mixed: [string, number, boolean] = ["hello", 42, true];
```

### 访问元素

```ts
let person: [string, number] = ["John", 30];

// 通过索引访问
let name: string = person[0]; // "John"
let age: number = person[1];   // 30
```

### 解构赋值

```ts
let person: [string, number] = ["John", 30];

// 解构
let [name, age] = person;
console.log(name); // "John"
console.log(age);  // 30
```

### 可选元素

TypeScript 3.0+ 支持可选元素：

```ts
let optional: [string, number?] = ["hello"];
let optional2: [string, number?] = ["hello", 42];
```

### 剩余元素

TypeScript 3.0+ 支持剩余元素：

```ts
let rest: [string, ...number[]] = ["hello", 1, 2, 3, 4];
```

### 标记元组（TypeScript 4.0+）

TypeScript 4.0+ 支持标记元组元素：

```ts
let point: [x: number, y: number] = [10, 20];
```

## 数组 vs 元组

### 区别

| 特性     | 数组           | 元组               |
|:---------|:---------------|:-------------------|
| 长度     | 可变           | 固定               |
| 类型     | 相同类型       | 可以不同类型       |
| 用途     | 存储同类型数据 | 存储固定结构数据   |
| 灵活性   | 高             | 低                 |
| 类型安全 | 中等           | 高                 |

### 使用场景

#### 数组适用场景

- 存储同类型的多个值
- 长度不固定的集合
- 需要动态添加/删除元素

```ts
// 存储用户 ID 列表
let userIds: number[] = [1, 2, 3, 4, 5];

// 存储商品名称
let products: string[] = ["apple", "banana", "orange"];
```

#### 元组适用场景

- 存储固定结构的数据
- 函数返回多个值
- 需要精确类型控制

```ts
// 坐标点
let point: [number, number] = [10, 20];

// 用户信息（姓名、年龄、是否激活）
let user: [string, number, boolean] = ["John", 30, true];

// 函数返回多个值
function getUser(): [string, number] {
    return ["John", 30];
}
```

## 类型注解示例

### 函数参数

```ts
// 数组参数
function processNumbers(numbers: number[]): number {
    return numbers.reduce((sum, num) => sum + num, 0);
}

// 元组参数
function processPoint(point: [number, number]): number {
    return point[0] + point[1];
}
```

### 函数返回值

```ts
// 返回数组
function getNumbers(): number[] {
    return [1, 2, 3, 4, 5];
}

// 返回元组
function getUser(): [string, number] {
    return ["John", 30];
}
```

### 对象属性

```ts
interface User {
    name: string;
    tags: string[];
    coordinates: [number, number];
}

let user: User = {
    name: "John",
    tags: ["developer", "typescript"],
    coordinates: [10, 20]
};
```

## 类型推断

### 数组推断

```ts
// 推断为 number[]
let numbers = [1, 2, 3];

// 推断为 string[]
let names = ["John", "Jane"];
```

### 元组推断

```ts
// 推断为 [string, number]
let person = ["John", 30];

// 使用 as const 推断为字面量元组
let point = [10, 20] as const; // readonly [10, 20]
```

## 常见错误

### 错误 1：类型不匹配

```ts
let numbers: number[] = [1, 2, 3];
numbers.push("4"); // 错误：类型 'string' 不能赋值给类型 'number'
```

### 错误 2：元组长度不匹配

```ts
let person: [string, number] = ["John"]; // 错误：缺少元素
let person2: [string, number] = ["John", 30, true]; // 错误：元素过多
```

### 错误 3：只读数组修改

```ts
let numbers: readonly number[] = [1, 2, 3];
numbers.push(4); // 错误：只读数组不能修改
```

## 注意事项

1. **数组类型**：数组类型表示可变长度的同类型集合
2. **元组类型**：元组类型表示固定长度和类型的集合
3. **只读数组**：使用 `readonly` 创建只读数组
4. **类型推断**：TypeScript 可以推断数组和元组类型

## 最佳实践

1. **数组用于同类型集合**：使用数组存储同类型的多个值
2. **元组用于固定结构**：使用元组存储固定结构的数据
3. **明确类型**：为数组和元组添加明确的类型注解
4. **只读数组**：不需要修改时使用只读数组

## 练习

1. **数组操作**：创建不同类型的数组，进行添加、删除、查找等操作。

2. **元组使用**：创建元组类型，练习访问、解构等操作。

3. **类型注解**：为函数参数和返回值添加数组或元组类型注解。

4. **只读数组**：使用只读数组，理解只读数组的限制。

5. **类型推断**：观察 TypeScript 如何推断数组和元组类型。

完成以上练习后，继续学习下一节，了解枚举类型。

## 总结

数组和元组是 TypeScript 中重要的数据结构。数组用于存储同类型的可变长度集合，元组用于存储固定长度和类型的集合。理解数组和元组的区别和使用场景，可以帮助我们更好地使用 TypeScript 的类型系统。

## 相关资源

- [TypeScript 数组类型文档](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#arrays)
- [TypeScript 元组类型文档](https://www.typescriptlang.org/docs/handbook/2/objects.html#tuple-types)
