# 2.4.3 类型兼容性规则基础

## 概述

类型兼容性规则决定了 TypeScript 如何判断两个类型是否兼容。本节介绍基本的类型兼容性规则，包括对象类型、函数类型、数组类型等的兼容性规则。

## 对象类型兼容性

### 基本规则

对象类型的兼容性基于属性：

- **必需属性**：源类型必须包含目标类型的所有必需属性
- **可选属性**：目标类型的可选属性不影响兼容性
- **额外属性**：源类型可以有额外属性

### 示例

```ts
interface Target {
    name: string;
    age?: number;  // 可选属性
}

interface Source {
    name: string;
    age: number;
    email: string;  // 额外属性
}

let source: Source = { name: "John", age: 30, email: "john@example.com" };
let target: Target = source;  // ✅ 兼容

// 检查过程：
// 1. Target 需要 name: string ✅ Source 有
// 2. Target 的 age 是可选的，不影响兼容性 ✅
// 3. Source 的额外属性 email 不影响兼容性 ✅
```

### 属性类型必须匹配

属性类型必须完全匹配：

```ts
interface A {
    value: number;
}

interface B {
    value: string;  // 类型不匹配
}

let a: A = { value: 1 };
// let b: B = a;  // ❌ 不兼容：value 类型不匹配
```

## 函数类型兼容性

### 基本规则

函数类型的兼容性基于参数和返回值：

- **参数兼容性**：目标函数的参数类型必须兼容源函数的参数类型（逆变）
- **返回值兼容性**：源函数的返回值类型必须兼容目标函数的返回值类型（协变）

### 参数兼容性（逆变）

目标函数的参数类型必须兼容源函数的参数类型：

```ts
// 参数兼容性示例
type Handler = (x: number) => void;

// 兼容：string 可以赋值给 number 的父类型（这里 number 是更具体的类型）
let handler1: Handler = (x: number) => { console.log(x); };  // ✅

// 不兼容：Handler 需要 (number) => void，不能是 (string) => void
// let handler2: Handler = (x: string) => { console.log(x); };  // ❌

// 更复杂的例子
type Process = (data: { id: number }) => void;

let process1: Process = (data: { id: number }) => { };  // ✅
let process2: Process = (data: { id: number; name: string }) => { };  // ✅ 兼容：额外属性
```

### 返回值兼容性（协变）

源函数的返回值类型必须兼容目标函数的返回值类型：

```ts
// 返回值兼容性示例
type GetValue = () => number;

let getValue1: GetValue = () => 10;  // ✅
let getValue2: GetValue = () => 10.5;  // ✅ number 兼容 number

// 不兼容：返回 string 不能赋值给返回 number 的类型
// let getValue3: GetValue = () => "10";  // ❌
```

### 参数数量

目标函数可以接受更少的参数：

```ts
type Handler = (x: number, y: number) => void;

// 兼容：可以忽略参数
let handler1: Handler = (x: number) => { console.log(x); };  // ✅

// 兼容：可以忽略所有参数
let handler2: Handler = () => { };  // ✅

// 不兼容：不能有更多参数
// let handler3: Handler = (x: number, y: number, z: number) => { };  // ❌
```

## 数组类型兼容性

### 基本规则

数组类型的兼容性基于元素类型：

```ts
// 数组兼容性
let numbers: number[] = [1, 2, 3];
let values: (number | string)[] = [1, 2, "3"];

// number[] 可以赋值给 (number | string)[]
values = numbers;  // ✅ 兼容

// (number | string)[] 不能赋值给 number[]
// numbers = values;  // ❌ 不兼容：可能包含 string
```

### 只读数组兼容性

只读数组可以赋值给普通数组：

```ts
let readonlyNumbers: readonly number[] = [1, 2, 3];
let numbers: number[] = readonlyNumbers;  // ✅ 兼容

// 普通数组不能赋值给只读数组
// let readonly: readonly number[] = numbers;  // ❌ 不兼容
```

## 联合类型兼容性

### 基本规则

联合类型的兼容性基于所有成员类型：

```ts
type A = string | number;
type B = string | number | boolean;

let a: A = "hello";
let b: B = a;  // ✅ 兼容：A 的所有成员都在 B 中

// B 不能赋值给 A（可能包含 boolean）
// a = b;  // ❌ 不兼容
```

## 交叉类型兼容性

### 基本规则

交叉类型的兼容性要求同时满足所有类型：

```ts
interface A {
    a: string;
}

interface B {
    b: number;
}

type AB = A & B;

let ab: AB = { a: "test", b: 10 };

// AB 可以赋值给 A
let a: A = ab;  // ✅ 兼容

// AB 可以赋值给 B
let b: B = ab;  // ✅ 兼容

// A 不能赋值给 AB（缺少 b）
// ab = a;  // ❌ 不兼容
```

## 类型兼容性检查

### 使用场景

类型兼容性在以下场景中发挥作用：

1. **变量赋值**：检查赋值是否兼容
2. **函数调用**：检查参数类型是否兼容
3. **函数返回**：检查返回值类型是否兼容
4. **接口实现**：检查类是否实现接口
5. **类型断言**：检查断言是否合理

### 示例

```ts
interface User {
    name: string;
    age: number;
}

// 1. 变量赋值
let user: User = { name: "John", age: 30 };  // ✅ 兼容

// 2. 函数参数
function greet(user: User): void {
    console.log(user.name);
}

greet({ name: "Jane", age: 25 });  // ✅ 兼容

// 3. 函数返回
function createUser(): User {
    return { name: "Bob", age: 35 };  // ✅ 兼容
}

// 4. 接口实现
class UserImpl implements User {
    name: string;
    age: number;
    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }
}

let userImpl: User = new UserImpl("Alice", 28);  // ✅ 兼容
```

## 注意事项

1. **结构化匹配**：TypeScript 只检查结构，不检查类型名称
2. **必需属性**：源类型必须包含目标类型的所有必需属性
3. **可选属性**：目标类型的可选属性不影响兼容性
4. **额外属性**：源类型可以有额外属性
5. **函数参数**：函数参数兼容性遵循逆变规则
6. **函数返回值**：函数返回值兼容性遵循协变规则

## 最佳实践

1. **理解规则**：理解基本的类型兼容性规则
2. **利用结构化类型**：利用结构化类型系统编写灵活代码
3. **明确类型定义**：虽然结构化类型灵活，但仍应明确定义类型
4. **函数类型**：注意函数参数的逆变和返回值的协变
5. **类型安全**：利用类型兼容性确保类型安全

## 练习任务

1. **对象类型兼容**：
   - 定义包含必需和可选属性的接口
   - 创建具有不同属性组合的对象
   - 测试哪些对象可以赋值给接口类型

2. **函数类型兼容**：
   - 定义函数类型
   - 创建不同参数和返回值的函数
   - 测试哪些函数可以赋值给函数类型

3. **数组类型兼容**：
   - 定义不同类型的数组
   - 测试数组之间的兼容性
   - 理解数组元素类型的兼容性规则

4. **联合类型兼容**：
   - 定义不同的联合类型
   - 测试联合类型之间的兼容性
   - 理解联合类型的兼容性规则

5. **实际应用**：
   - 编写一个函数，接收配置对象
   - 利用类型兼容性，允许传递包含额外属性的配置
   - 理解类型兼容性在实际开发中的应用

完成以上练习后，继续学习阶段三：面向对象与类。

## 总结

类型兼容性规则是 TypeScript 类型系统的基础：

- **对象类型**：基于属性结构，必需属性必须匹配
- **函数类型**：参数逆变，返回值协变
- **数组类型**：基于元素类型
- **联合类型**：基于所有成员类型
- **交叉类型**：必须同时满足所有类型

理解类型兼容性规则有助于更好地使用 TypeScript 的类型系统。

---

**最后更新**：2025-01-XX
