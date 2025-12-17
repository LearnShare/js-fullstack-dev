# 2.2.3 联合类型与交叉类型

## 概述

联合类型和交叉类型是 TypeScript 中组合类型的两种方式。本节介绍联合类型和交叉类型的定义、使用和区别。

## 联合类型

### 定义

联合类型使用 `|` 操作符，表示值可以是多种类型中的一种。

### 语法

```ts
type UnionType = Type1 | Type2 | Type3;
```

### 基本用法

```ts
// 联合类型
type StringOrNumber = string | number;

let value: StringOrNumber = "hello";
value = 42; // 也可以赋值数字
```

### 类型收窄

使用联合类型时，需要进行类型收窄：

```ts
type StringOrNumber = string | number;

function process(value: StringOrNumber) {
    if (typeof value === "string") {
        // 类型收窄为 string
        console.log(value.toUpperCase());
    } else {
        // 类型收窄为 number
        console.log(value.toFixed(2));
    }
}
```

### 字面量联合类型

```ts
type Status = "pending" | "approved" | "rejected";

let status: Status = "pending";
// status = "invalid"; // 错误
```

### 对象联合类型

```ts
type Circle = {
    kind: "circle";
    radius: number;
};

type Rectangle = {
    kind: "rectangle";
    width: number;
    height: number;
};

type Shape = Circle | Rectangle;

function getArea(shape: Shape): number {
    if (shape.kind === "circle") {
        return Math.PI * shape.radius ** 2;
    } else {
        return shape.width * shape.height;
    }
}
```

## 交叉类型

### 定义

交叉类型使用 `&` 操作符，表示值必须同时满足所有类型。

### 语法

```ts
type IntersectionType = Type1 & Type2 & Type3;
```

### 基本用法

```ts
type A = {
    a: string;
};

type B = {
    b: number;
};

type AB = A & B;

let ab: AB = {
    a: "hello",
    b: 42
};
```

### 对象交叉类型

```ts
type User = {
    name: string;
    age: number;
};

type Timestamp = {
    createdAt: Date;
    updatedAt: Date;
};

type UserWithTimestamp = User & Timestamp;

let user: UserWithTimestamp = {
    name: "John",
    age: 30,
    createdAt: new Date(),
    updatedAt: new Date()
};
```

### 函数交叉类型

```ts
type A = (x: number) => number;
type B = (x: string) => string;

type AB = A & B; // 实际上不可用，因为参数类型冲突
```

## 联合类型 vs 交叉类型

### 区别

| 特性       | 联合类型（|）        | 交叉类型（&）         |
|:-----------|:----------------------|:----------------------|
| 含义       | 可以是其中一种类型    | 必须同时满足所有类型  |
| 操作符     | `|`                  | `&`                    |
| 使用场景   | 多种可能的类型        | 组合多个类型          |
| 类型收窄   | 需要类型收窄          | 不需要                |

### 示例对比

```ts
// 联合类型：可以是 string 或 number
type StringOrNumber = string | number;

// 交叉类型：必须同时是 User 和 Timestamp
type UserWithTimestamp = User & Timestamp;
```

## 使用场景

### 联合类型使用场景

1. **多种可能的类型**

```ts
type ID = string | number;

function getById(id: ID) {
    // ...
}
```

2. **状态类型**

```ts
type Status = "loading" | "success" | "error";
```

3. **可空类型**

```ts
type MaybeString = string | null | undefined;
```

### 交叉类型使用场景

1. **组合类型**

```ts
type UserWithRole = User & { role: string };
```

2. **混入模式**

```ts
type Timestamped = {
    createdAt: Date;
    updatedAt: Date;
};

type UserWithTimestamp = User & Timestamped;
```

## 常见错误

### 错误 1：联合类型未收窄

```ts
type StringOrNumber = string | number;

function process(value: StringOrNumber) {
    // 错误：未进行类型收窄
    console.log(value.toUpperCase()); // 错误
}
```

### 错误 2：交叉类型冲突

```ts
type A = { x: string };
type B = { x: number };

type AB = A & B; // x 的类型是 never（string & number）
```

## 注意事项

1. **联合类型需要收窄**：使用联合类型时需要进行类型收窄
2. **交叉类型组合**：交叉类型用于组合多个类型
3. **类型冲突**：交叉类型中冲突的属性类型会变成 never
4. **实际应用**：根据实际需求选择联合类型或交叉类型

## 最佳实践

1. **使用联合类型表示多种可能**：当值可以是多种类型时使用联合类型
2. **使用交叉类型组合类型**：当需要组合多个类型时使用交叉类型
3. **进行类型收窄**：使用联合类型时进行类型收窄
4. **避免类型冲突**：避免交叉类型中的类型冲突

## 练习

1. **联合类型**：定义和使用联合类型，练习类型收窄。

2. **交叉类型**：定义和使用交叉类型，组合多个类型。

3. **类型收窄**：使用类型守卫进行类型收窄。

4. **实际应用**：在实际场景中应用联合类型和交叉类型。

5. **类型组合**：组合使用联合类型和交叉类型。

完成以上练习后，继续学习下一节，了解字面量类型。

## 总结

联合类型和交叉类型是 TypeScript 中组合类型的两种方式。联合类型使用 `|` 表示可以是多种类型中的一种，交叉类型使用 `&` 表示必须同时满足所有类型。理解联合类型和交叉类型的区别和使用场景，可以帮助我们更好地设计类型系统。

## 相关资源

- [TypeScript 联合类型文档](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#union-types)
- [TypeScript 交叉类型文档](https://www.typescriptlang.org/docs/handbook/2/objects.html#intersection-types)
