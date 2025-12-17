# 1.2.4 枚举类型

## 概述

枚举（Enum）是 TypeScript 提供的一种数据类型，用于定义一组命名常量。本节介绍枚举的定义、使用和特性。

## 数字枚举

### 定义

数字枚举是最常见的枚举类型，成员的值是数字。

### 基本语法

```ts
enum Direction {
    Up,
    Down,
    Left,
    Right
}
```

### 默认值

默认情况下，枚举成员从 0 开始递增：

```ts
enum Direction {
    Up,    // 0
    Down,  // 1
    Left,  // 2
    Right  // 3
}

console.log(Direction.Up);    // 0
console.log(Direction.Down);  // 1
console.log(Direction.Left);  // 2
console.log(Direction.Right); // 3
```

### 自定义起始值

可以指定起始值：

```ts
enum Direction {
    Up = 1,
    Down,   // 2
    Left,   // 3
    Right   // 4
}
```

### 完全自定义值

可以为每个成员指定值：

```ts
enum Status {
    Pending = 100,
    Approved = 200,
    Rejected = 300
}
```

### 使用示例

```ts
enum Direction {
    Up,
    Down,
    Left,
    Right
}

// 使用枚举
let direction: Direction = Direction.Up;

// 在函数中使用
function move(direction: Direction) {
    switch (direction) {
        case Direction.Up:
            console.log("向上移动");
            break;
        case Direction.Down:
            console.log("向下移动");
            break;
        case Direction.Left:
            console.log("向左移动");
            break;
        case Direction.Right:
            console.log("向右移动");
            break;
    }
}

move(Direction.Up);
```

## 字符串枚举

### 定义

字符串枚举的成员值是字符串。

### 基本语法

```ts
enum Color {
    Red = "red",
    Green = "green",
    Blue = "blue"
}
```

### 使用示例

```ts
enum Color {
    Red = "red",
    Green = "green",
    Blue = "blue"
}

let color: Color = Color.Red;
console.log(color); // "red"
```

### 特点

- 字符串枚举必须为每个成员指定值
- 字符串枚举提供更好的可读性和调试体验
- 字符串枚举在编译后不会生成反向映射

## 异构枚举

### 定义

异构枚举包含数字和字符串成员（不推荐使用）。

### 示例

```ts
enum Mixed {
    No = 0,
    Yes = "yes"
}
```

## 常量枚举

### 定义

常量枚举使用 `const enum` 关键字，在编译时会被内联。

### 语法

```ts
const enum Direction {
    Up,
    Down,
    Left,
    Right
}
```

### 特点

- 编译时会被完全移除
- 只能使用常量枚举表达式
- 不能有计算成员

### 使用示例

```ts
const enum Direction {
    Up,
    Down,
    Left,
    Right
}

let direction = Direction.Up;
// 编译后：let direction = 0;
```

## 计算成员

### 定义

枚举成员可以是计算值（非常量枚举）。

### 示例

```ts
enum FileAccess {
    None,
    Read = 1 << 1,
    Write = 1 << 2,
    ReadWrite = Read | Write
}
```

## 反向映射

### 数字枚举的反向映射

数字枚举会生成反向映射：

```ts
enum Direction {
    Up,
    Down,
    Left,
    Right
}

// 正向访问
console.log(Direction.Up);    // 0

// 反向访问
console.log(Direction[0]);    // "Up"
```

### 字符串枚举没有反向映射

```ts
enum Color {
    Red = "red",
    Green = "green"
}

// 正向访问
console.log(Color.Red);       // "red"

// 反向访问（不存在）
// console.log(Color["red"]); // undefined
```

## 枚举作为类型

### 类型注解

枚举可以作为类型使用：

```ts
enum Status {
    Pending,
    Approved,
    Rejected
}

// 使用枚举作为类型
let status: Status = Status.Pending;

// 函数参数和返回值
function processStatus(status: Status): string {
    switch (status) {
        case Status.Pending:
            return "处理中";
        case Status.Approved:
            return "已批准";
        case Status.Rejected:
            return "已拒绝";
    }
}
```

## 枚举成员类型

### 字面量类型

枚举成员可以作为字面量类型：

```ts
enum Direction {
    Up,
    Down
}

// 只能使用枚举成员
let up: Direction.Up = Direction.Up;
```

## 编译后的代码

### 数字枚举

```ts
// TypeScript
enum Direction {
    Up,
    Down
}

// 编译后的 JavaScript
var Direction;
(function (Direction) {
    Direction[Direction["Up"] = 0] = "Up";
    Direction[Direction["Down"] = 1] = "Down";
})(Direction || (Direction = {}));
```

### 字符串枚举

```ts
// TypeScript
enum Color {
    Red = "red",
    Green = "green"
}

// 编译后的 JavaScript
var Color;
(function (Color) {
    Color["Red"] = "red";
    Color["Green"] = "green";
})(Color || (Color = {}));
```

### 常量枚举

```ts
// TypeScript
const enum Direction {
    Up,
    Down
}

let direction = Direction.Up;

// 编译后的 JavaScript
var direction = 0; // 枚举被完全移除
```

## 常见错误

### 错误 1：类型不匹配

```ts
enum Status {
    Pending,
    Approved
}

let status: Status = "Pending"; // 错误：类型 'string' 不能赋值给类型 'Status'
```

### 错误 2：未定义的成员

```ts
enum Direction {
    Up,
    Down
}

let direction: Direction = Direction.Left; // 错误：'Left' 不存在
```

## 注意事项

1. **数字枚举默认从 0 开始**：如果不指定值，从 0 开始递增
2. **字符串枚举必须指定值**：字符串枚举的每个成员都必须有值
3. **常量枚举会被内联**：常量枚举在编译时会被完全移除
4. **反向映射**：只有数字枚举有反向映射

## 最佳实践

1. **使用字符串枚举**：字符串枚举提供更好的可读性和调试体验
2. **避免异构枚举**：尽量避免使用异构枚举
3. **常量枚举优化**：不需要反向映射时使用常量枚举
4. **明确类型**：使用枚举作为类型，提高类型安全

## 练习

1. **数字枚举**：创建数字枚举，练习使用和访问。

2. **字符串枚举**：创建字符串枚举，对比与数字枚举的区别。

3. **常量枚举**：使用常量枚举，观察编译后的代码。

4. **类型注解**：使用枚举作为类型，为函数参数和返回值添加类型注解。

5. **反向映射**：练习数字枚举的反向映射。

完成以上练习后，继续学习下一节，了解特殊类型。

## 总结

枚举是 TypeScript 中用于定义命名常量的数据类型。数字枚举和字符串枚举是最常用的类型。枚举可以作为类型使用，提供类型安全。理解枚举的特性和使用场景，可以帮助我们更好地使用 TypeScript 的类型系统。

## 相关资源

- [TypeScript 枚举文档](https://www.typescriptlang.org/docs/handbook/enums.html)
