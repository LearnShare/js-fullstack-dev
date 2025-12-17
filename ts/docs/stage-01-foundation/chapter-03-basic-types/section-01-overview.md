# 1.2.1 基础类型系统概述

## 概述

TypeScript 的类型系统是 TypeScript 的核心特性，提供了静态类型检查能力。本节介绍 TypeScript 类型系统的基本概念、作用和优势。

## 什么是类型系统

### 定义

类型系统是一组规则，用于检查程序中值的使用是否符合其类型的预期。

### 静态类型 vs 动态类型

#### 静态类型（TypeScript）

类型在编译时确定，编译时进行类型检查：

```ts
let message: string = "Hello";
message = 123; // 编译错误：类型 'number' 不能赋值给类型 'string'
```

#### 动态类型（JavaScript）

类型在运行时确定，运行时进行类型检查：

```js
let message = "Hello";
message = 123; // 运行时允许，但可能导致错误
```

## TypeScript 类型系统的优势

### 1. 类型安全

在编译时发现类型错误，避免运行时错误：

```ts
function add(a: number, b: number): number {
    return a + b;
}

add(1, 2);     // 正确
add("1", "2"); // 编译错误：参数类型不匹配
```

### 2. 更好的开发体验

#### 代码补全

IDE 可以根据类型提供准确的代码补全：

```ts
let user = {
    name: "John",
    age: 30
};

user. // IDE 会提示 name 和 age
```

#### 错误提示

IDE 可以实时显示类型错误：

```ts
let value: string = 123; // 红色波浪线提示错误
```

#### 重构支持

类型系统使重构更安全：

```ts
interface User {
    name: string;
    age: number;
}

function getUser(): User {
    return { name: "John", age: 30 };
}

// 修改 User 接口时，所有使用的地方都会提示错误
```

### 3. 文档化

类型即文档，代码更易理解：

```ts
// 类型清楚地说明了函数的参数和返回值
function calculateTotal(price: number, quantity: number): number {
    return price * quantity;
}
```

### 4. 可维护性

大型项目中，类型系统帮助维护代码：

- 明确接口契约
- 减少错误传播
- 便于团队协作

## TypeScript 类型分类

### 基础类型

#### 原始类型

- `string`：字符串
- `number`：数字
- `boolean`：布尔值
- `null`：空值
- `undefined`：未定义
- `symbol`：符号
- `bigint`：大整数

#### 对象类型

- `object`：对象
- `array`：数组
- `tuple`：元组
- `enum`：枚举
- `function`：函数

### 特殊类型

- `any`：任意类型
- `unknown`：未知类型
- `void`：无返回值
- `never`：永不存在的值

### 高级类型

- `union`：联合类型
- `intersection`：交叉类型
- `literal`：字面量类型
- `generic`：泛型

## 类型注解

### 语法

使用冒号 `:` 后跟类型名称：

```ts
let variable: type = value;
```

### 示例

```ts
// 变量类型注解
let name: string = "John";
let age: number = 30;
let isActive: boolean = true;

// 函数参数和返回值类型注解
function greet(name: string): string {
    return `Hello, ${name}!`;
}

// 对象类型注解
let user: { name: string; age: number } = {
    name: "John",
    age: 30
};
```

## 类型推断

### 定义

TypeScript 可以根据值自动推断类型，无需显式注解。

### 示例

```ts
// TypeScript 推断 name 为 string 类型
let name = "John";

// TypeScript 推断 age 为 number 类型
let age = 30;

// TypeScript 推断 isActive 为 boolean 类型
let isActive = true;
```

### 何时使用类型注解

1. **函数参数**：函数参数通常需要类型注解
2. **函数返回值**：复杂函数建议添加返回类型注解
3. **对象字面量**：复杂对象建议添加类型注解
4. **明确意图**：当类型推断不够明确时

## 类型检查

### 编译时检查

TypeScript 在编译时进行类型检查：

```ts
let value: string = 123; // 编译错误
```

### 类型错误

类型错误不会阻止编译，但会显示错误信息：

```bash
tsc script.ts
# 输出：error TS2322: Type 'number' is not assignable to type 'string'.
```

### 严格模式

启用严格模式可以获得更严格的类型检查：

```json
{
  "compilerOptions": {
    "strict": true
  }
}
```

## 类型系统的工作方式

### 1. 类型注解

开发者显式指定类型：

```ts
let count: number = 10;
```

### 2. 类型推断

TypeScript 自动推断类型：

```ts
let count = 10; // 推断为 number
```

### 3. 类型检查

TypeScript 检查类型使用是否正确：

```ts
let count: number = 10;
count = "ten"; // 错误：类型不匹配
```

### 4. 类型擦除

编译后，类型信息会被移除：

```ts
// TypeScript
let count: number = 10;

// 编译后的 JavaScript
let count = 10;
```

## 注意事项

1. **类型是编译时的**：类型信息在编译后会被移除
2. **类型不是运行时检查**：类型错误不会在运行时抛出异常
3. **类型可以渐进式采用**：可以逐步为代码添加类型
4. **类型系统是可选的**：可以使用 `any` 跳过类型检查（不推荐）

## 最佳实践

1. **启用严格模式**：始终启用 `strict` 模式
2. **明确类型**：尽量使用明确的类型，避免 `any`
3. **利用类型推断**：在类型明确的地方利用类型推断
4. **类型即文档**：使用类型作为代码文档

## 练习

1. **类型注解**：为变量、函数参数和返回值添加类型注解。

2. **类型推断**：观察 TypeScript 如何推断类型，理解推断规则。

3. **类型错误**：故意制造类型错误，观察错误提示。

4. **严格模式**：启用严格模式，体验更严格的类型检查。

5. **类型文档**：使用类型作为代码文档，提升代码可读性。

完成以上练习后，继续学习下一节，了解原始类型。

## 总结

TypeScript 的类型系统提供了静态类型检查能力，可以在编译时发现错误，提升代码质量和开发体验。理解类型系统的基本概念是学习 TypeScript 的基础。类型系统包括类型注解、类型推断、类型检查等机制，帮助开发者编写更安全、更易维护的代码。

## 相关资源

- [TypeScript 类型系统文档](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html)
- [TypeScript 类型推断](https://www.typescriptlang.org/docs/handbook/type-inference.html)
