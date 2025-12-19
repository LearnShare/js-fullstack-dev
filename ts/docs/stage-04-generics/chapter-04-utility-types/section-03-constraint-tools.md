# 4.4.3 泛型约束工具

## 概述

泛型约束工具是用于泛型约束的工具类型，帮助我们在泛型操作中更好地处理类型约束。本节介绍与泛型约束相关的工具类型。

## keyof 操作符

### 定义

`keyof` 操作符获取对象类型的所有键的联合类型。

### 基本用法

```ts
interface User {
    id: number;
    name: string;
    email: string;
}

type UserKeys = keyof User;
// 等价于："id" | "name" | "email"

let key: UserKeys = "id";  // ✅
let key2: UserKeys = "name";  // ✅
// let key3: UserKeys = "age";  // ❌ 不兼容
```

### 使用场景

#### 1. 类型安全的属性访问

```ts
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key];
}

interface User {
    name: string;
    age: number;
}

let user: User = { name: "John", age: 30 };
let name = getProperty(user, "name");  // string
let age = getProperty(user, "age");  // number
// let invalid = getProperty(user, "email");  // ❌ 类型错误
```

#### 2. 属性选择

```ts
// 使用 keyof 选择属性
type Pick<T, K extends keyof T> = {
    [P in K]: T[P];
};

interface User {
    id: number;
    name: string;
    email: string;
}

type UserName = Pick<User, "name">;
// 等价于：{ name: string }
```

## extends 约束工具

### 定义

`extends` 关键字用于泛型约束，限制泛型参数必须满足特定条件。

### 基本用法

```ts
// 约束泛型参数必须具有特定属性
interface HasLength {
    length: number;
}

function getLength<T extends HasLength>(item: T): number {
    return item.length;
}

getLength("hello");  // ✅ string 有 length 属性
getLength([1, 2, 3]);  // ✅ array 有 length 属性
// getLength(42);  // ❌ number 没有 length 属性
```

### 使用场景

#### 1. 属性约束

```ts
// 约束泛型参数必须具有特定属性
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key];
}

interface User {
    name: string;
    age: number;
}

let user: User = { name: "John", age: 30 };
let name = getProperty(user, "name");  // ✅
```

#### 2. 类型约束

```ts
// 约束泛型参数必须是特定类型
function merge<T extends object, U extends object>(obj1: T, obj2: U): T & U {
    return { ...obj1, ...obj2 };
}

let result = merge({ a: 1 }, { b: 2 });  // ✅
// let result2 = merge(1, 2);  // ❌ 不兼容
```

## 条件类型约束

### 定义

条件类型约束使用条件类型来约束泛型参数。

### 基本用法

```ts
// 条件类型约束
type NonFunctionPropertyNames<T> = {
    [K in keyof T]: T[K] extends Function ? never : K;
}[keyof T];

interface User {
    id: number;
    name: string;
    getName(): string;
}

type UserProps = NonFunctionPropertyNames<User>;
// 等价于："id" | "name"
```

### 使用场景

#### 1. 属性过滤

```ts
// 过滤掉函数属性
type NonFunctionProps<T> = {
    [K in keyof T]: T[K] extends Function ? never : K;
}[keyof T];

interface Config {
    apiUrl: string;
    timeout: number;
    init(): void;
}

type ConfigProps = NonFunctionProps<Config>;
// 等价于："apiUrl" | "timeout"
```

#### 2. 类型判断

```ts
// 判断类型是否为数组
type IsArray<T> = T extends any[] ? true : false;

type Test1 = IsArray<number[]>;  // true
type Test2 = IsArray<string>;  // false
```

## 泛型约束工具组合

### 组合使用

可以组合多个约束工具实现复杂的类型操作：

```ts
// 组合 keyof 和 extends
function updateProperty<T, K extends keyof T>(
    obj: T,
    key: K,
    value: T[K]
): T {
    return { ...obj, [key]: value };
}

interface User {
    name: string;
    age: number;
}

let user: User = { name: "John", age: 30 };
let updated = updateProperty(user, "age", 31);  // ✅
// let updated2 = updateProperty(user, "age", "31");  // ❌ 类型错误
```

### 实际应用

```ts
// API 更新请求
interface User {
    id: number;
    name: string;
    email: string;
}

// 创建更新类型，排除 id，所有属性可选
type UpdateUser = Partial<Omit<User, "id">>;

function updateUser(id: number, updates: UpdateUser): User {
    // ...
    return { id, ...updates } as User;
}
```

## 注意事项

1. **约束限制**：泛型约束必须合理，不能过于严格或过于宽松
2. **类型推断**：约束可以帮助 TypeScript 更好地推断类型
3. **性能考虑**：复杂的约束可能影响编译性能
4. **可读性**：过度使用约束可能降低代码可读性
5. **类型安全**：合理使用约束可以提高类型安全

## 最佳实践

1. **合理约束**：根据实际需求设置合理的约束
2. **类型推断**：利用约束帮助 TypeScript 推断类型
3. **类型别名**：为复杂的约束创建类型别名
4. **文档说明**：为复杂的约束添加注释
5. **类型安全**：利用约束提高类型安全

## 练习任务

1. **keyof 操作符**：
   - 使用 `keyof` 获取对象类型的键
   - 创建类型安全的属性访问函数
   - 理解 `keyof` 的作用

2. **extends 约束**：
   - 使用 `extends` 约束泛型参数
   - 创建具有属性约束的函数
   - 理解 `extends` 约束的作用

3. **条件类型约束**：
   - 使用条件类型创建约束
   - 过滤类型属性
   - 理解条件类型约束的作用

4. **约束工具组合**：
   - 组合多个约束工具
   - 创建复杂的类型操作
   - 理解约束工具组合的效果

5. **实际应用**：
   - 使用约束工具创建类型安全的 API
   - 使用约束工具处理配置对象
   - 理解约束工具在实际开发中的应用

完成以上练习后，继续学习阶段五：高级类型系统。

## 总结

泛型约束工具提供了强大的类型约束能力：

- **keyof**：获取对象类型的键
- **extends**：约束泛型参数
- **条件类型**：创建条件约束
- **组合使用**：组合多个工具实现复杂操作

掌握泛型约束工具有助于编写更安全、更灵活的 TypeScript 代码。

---

**最后更新**：2025-01-XX
