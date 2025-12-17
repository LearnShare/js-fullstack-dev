# 2.2.5 Interface vs Type

## 概述

接口（Interface）和类型别名（Type Alias）都可以定义对象类型，但它们有不同的特性和使用场景。本节详细对比接口和类型别名的区别，帮助选择合适的工具。

## 基本对比

### 相似点

接口和类型别名都可以定义对象类型：

```ts
// 接口
interface User {
    name: string;
    age: number;
}

// 类型别名
type User = {
    name: string;
    age: number;
};
```

### 区别总结

| 特性           | 接口（Interface）         | 类型别名（Type Alias）    |
|:---------------|:--------------------------|:-------------------------|
| 扩展方式       | `extends`                 | `&`（交叉类型）           |
| 合并           | 支持声明合并              | 不支持                   |
| 实现           | 可以被类实现              | 不能                     |
| 复杂类型       | 不支持联合、交叉等        | 支持                     |
| 使用场景       | 对象形状定义              | 复杂类型定义             |
| 性能           | 稍快                      | 稍慢                     |

## 详细对比

### 1. 扩展方式

#### 接口：extends

```ts
interface Animal {
    name: string;
}

interface Dog extends Animal {
    breed: string;
}
```

#### 类型别名：交叉类型

```ts
type Animal = {
    name: string;
};

type Dog = Animal & {
    breed: string;
};
```

### 2. 声明合并

#### 接口：支持合并

```ts
interface User {
    name: string;
}

interface User {
    age: number;
}

// 合并后的 User 包含 name 和 age
let user: User = {
    name: "John",
    age: 30
};
```

#### 类型别名：不支持合并

```ts
type User = {
    name: string;
};

// 错误：重复定义
type User = {
    age: number;
};
```

### 3. 类实现

#### 接口：可以被类实现

```ts
interface Flyable {
    fly(): void;
}

class Bird implements Flyable {
    fly() {
        console.log("Flying");
    }
}
```

#### 类型别名：不能实现

```ts
type Flyable = {
    fly(): void;
};

// 错误：不能实现类型别名
class Bird implements Flyable {
    // ...
}
```

### 4. 复杂类型支持

#### 接口：不支持

```ts
// 接口不支持联合类型
// interface Status = "pending" | "approved"; // 错误
```

#### 类型别名：支持

```ts
// 类型别名支持联合类型
type Status = "pending" | "approved" | "rejected";

// 类型别名支持交叉类型
type UserWithRole = User & { role: string };

// 类型别名支持条件类型
type NonNullable<T> = T extends null | undefined ? never : T;
```

## 使用场景

### 接口适用场景

1. **对象形状定义**

```ts
interface User {
    name: string;
    age: number;
}
```

2. **类实现**

```ts
interface Drawable {
    draw(): void;
}

class Circle implements Drawable {
    draw() {
        // ...
    }
}
```

3. **扩展第三方库**

```ts
// 扩展 Window 接口
interface Window {
    myCustomProperty: string;
}
```

### 类型别名适用场景

1. **联合类型**

```ts
type Status = "pending" | "approved" | "rejected";
```

2. **交叉类型**

```ts
type UserWithTimestamp = User & {
    createdAt: Date;
    updatedAt: Date;
};
```

3. **复杂类型计算**

```ts
type Keys = "name" | "age";
type User = {
    [K in Keys]: string;
};
```

4. **函数类型**

```ts
type EventHandler = (event: Event) => void;
```

## 选择建议

### 使用接口的情况

1. ✅ 定义对象形状
2. ✅ 需要类实现
3. ✅ 需要扩展第三方库
4. ✅ 需要声明合并

### 使用类型别名的情况

1. ✅ 定义联合类型
2. ✅ 定义交叉类型
3. ✅ 定义复杂类型
4. ✅ 定义函数类型
5. ✅ 进行类型计算

## 最佳实践

1. **优先使用接口**：定义对象形状时优先使用接口
2. **使用类型别名**：定义复杂类型时使用类型别名
3. **保持一致**：在项目中保持使用的一致性
4. **根据需求选择**：根据实际需求选择合适的工具

## 迁移建议

### 从接口迁移到类型别名

```ts
// 接口
interface User {
    name: string;
}

// 迁移为类型别名
type User = {
    name: string;
};
```

### 从类型别名迁移到接口

```ts
// 类型别名
type User = {
    name: string;
};

// 迁移为接口
interface User {
    name: string;
}
```

**注意**：迁移时需要考虑声明合并、类实现等特性。

## 常见问题

### 问题 1：应该使用接口还是类型别名？

**答案**：根据使用场景选择。定义对象形状时使用接口，定义复杂类型时使用类型别名。

### 问题 2：可以混用吗？

**答案**：可以，但建议保持一致。在同一个项目中，对于相似的类型定义保持一致性。

## 注意事项

1. **接口支持合并**：接口支持声明合并，类型别名不支持
2. **类型别名更灵活**：类型别名支持更多类型操作
3. **性能差异**：接口的性能稍好，但差异很小
4. **选择原则**：根据实际需求选择合适的工具

## 练习

1. **接口使用**：使用接口定义对象形状，练习接口的各种特性。

2. **类型别名使用**：使用类型别名定义复杂类型，练习类型别名的各种特性。

3. **对比实践**：对比接口和类型别名在相同场景下的使用。

4. **选择练习**：根据实际场景选择合适的工具。

5. **迁移实践**：练习在接口和类型别名之间迁移。

完成以上练习后，类型别名章节学习完成。可以继续学习下一章：函数类型。

## 总结

接口和类型别名都可以定义对象类型，但它们有不同的特性和使用场景。接口适合定义对象形状、类实现和扩展第三方库，类型别名适合定义复杂类型、联合类型和交叉类型。理解接口和类型别名的区别，可以帮助我们选择合适的工具。

## 相关资源

- [TypeScript 接口文档](https://www.typescriptlang.org/docs/handbook/2/objects.html#interfaces)
- [TypeScript 类型别名文档](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-aliases)
