# 4.1.3 泛型接口

## 概述

泛型接口允许在接口定义时使用类型参数，在使用时指定具体类型。本节介绍泛型接口的定义和使用。

## 泛型接口定义

### 基本语法

```ts
interface InterfaceName<T> {
    // 接口成员
}
```

### 示例

```ts
// 基本泛型接口
interface Box<T> {
    value: T;
    getValue(): T;
}

let numberBox: Box<number> = {
    value: 42,
    getValue() {
        return this.value;
    }
};
```

## 多个类型参数

### 定义

泛型接口可以有多个类型参数：

```ts
interface Pair<T, U> {
    first: T;
    second: U;
}

let pair: Pair<string, number> = {
    first: "Hello",
    second: 42
};
```

### 示例

```ts
interface Map<K, V> {
    get(key: K): V | undefined;
    set(key: K, value: V): void;
}
```

## 泛型接口继承

### 继承泛型接口

```ts
interface Container<T> {
    value: T;
}

interface Box<T> extends Container<T> {
    getValue(): T;
}
```

### 继承时指定类型

```ts
interface ReadonlyArray<T> {
    readonly [n: number]: T;
}

interface StringArray extends ReadonlyArray<string> {
    // StringArray 是 ReadonlyArray<string> 的子类型
}
```

## 泛型接口实现

### 类实现泛型接口

```ts
interface Container<T> {
    value: T;
    getValue(): T;
}

class Box<T> implements Container<T> {
    value: T;

    constructor(value: T) {
        this.value = value;
    }

    getValue(): T {
        return this.value;
    }
}
```

## 使用场景

### 1. 容器类型

```ts
interface Stack<T> {
    push(item: T): void;
    pop(): T | undefined;
    peek(): T | undefined;
}
```

### 2. 响应类型

```ts
interface ApiResponse<T> {
    data: T;
    status: number;
    message: string;
}
```

### 3. 回调接口

```ts
interface Callback<T> {
    (value: T): void;
}

function process<T>(value: T, callback: Callback<T>): void {
    callback(value);
}
```

## 常见错误

### 错误 1：类型参数使用错误

```ts
// 错误：类型参数应该在接口名后
interface Box {
    value: T;
}

// 正确
interface Box<T> {
    value: T;
}
```

### 错误 2：类型不匹配

```ts
interface Box<T> {
    value: T;
}

// 错误：类型不匹配
let box: Box<number> = {
    value: "Hello"
};
```

## 注意事项

1. **类型参数位置**：类型参数应该在接口名后
2. **多个参数**：可以有多个类型参数
3. **继承**：泛型接口可以继承其他接口
4. **实现**：类可以实现泛型接口

## 最佳实践

1. **使用泛型**：在需要类型安全时使用泛型接口
2. **明确类型**：为类型参数使用有意义的名称
3. **合理设计**：合理设计泛型接口的结构
4. **继承关系**：利用继承关系组织接口

## 练习

1. **泛型接口**：定义不同类型的泛型接口。

2. **多个参数**：定义使用多个类型参数的泛型接口。

3. **接口继承**：定义继承泛型接口的接口。

4. **接口实现**：实现泛型接口的类。

5. **实际应用**：在实际场景中应用泛型接口。

完成以上练习后，继续学习下一节，了解泛型类。

## 总结

泛型接口允许在接口定义时使用类型参数，在使用时指定具体类型。泛型接口可以有多个类型参数，可以继承其他接口，也可以被类实现。理解泛型接口的定义和使用是学习 TypeScript 泛型的关键。

## 相关资源

- [TypeScript 泛型接口文档](https://www.typescriptlang.org/docs/handbook/2/generics.html#generic-interfaces)
