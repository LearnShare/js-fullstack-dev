# 4.1.4 泛型类

## 概述

泛型类允许在类定义时使用类型参数，在使用时指定具体类型。本节介绍泛型类的定义和使用。

## 泛型类定义

### 基本语法

```ts
class ClassName<T> {
    // 类成员
}
```

### 示例

```ts
// 基本泛型类
class Box<T> {
    private value: T;

    constructor(value: T) {
        this.value = value;
    }

    getValue(): T {
        return this.value;
    }

    setValue(value: T): void {
        this.value = value;
    }
}

let numberBox = new Box<number>(42);
let stringBox = new Box<string>("Hello");
```

## 多个类型参数

### 定义

泛型类可以有多个类型参数：

```ts
class Pair<T, U> {
    private first: T;
    private second: U;

    constructor(first: T, second: U) {
        this.first = first;
        this.second = second;
    }

    getFirst(): T {
        return this.first;
    }

    getSecond(): U {
        return this.second;
    }
}

let pair = new Pair<string, number>("Hello", 42);
```

## 泛型类继承

### 继承泛型类

```ts
class Container<T> {
    protected value: T;

    constructor(value: T) {
        this.value = value;
    }
}

class Box<T> extends Container<T> {
    getValue(): T {
        return this.value;
    }
}
```

### 继承时指定类型

```ts
class NumberBox extends Box<number> {
    // NumberBox 是 Box<number> 的子类
}
```

## 静态成员

### 静态方法

泛型类的静态方法不能使用类的类型参数：

```ts
class Box<T> {
    private value: T;

    constructor(value: T) {
        this.value = value;
    }

    // 静态方法需要自己的类型参数
    static create<U>(value: U): Box<U> {
        return new Box(value);
    }
}
```

## 使用场景

### 1. 容器类

```ts
class Stack<T> {
    private items: T[] = [];

    push(item: T): void {
        this.items.push(item);
    }

    pop(): T | undefined {
        return this.items.pop();
    }

    peek(): T | undefined {
        return this.items[this.items.length - 1];
    }
}
```

### 2. 缓存类

```ts
class Cache<T> {
    private data: Map<string, T> = new Map();

    set(key: string, value: T): void {
        this.data.set(key, value);
    }

    get(key: string): T | undefined {
        return this.data.get(key);
    }
}
```

### 3. 响应类

```ts
class ApiResponse<T> {
    data: T;
    status: number;
    message: string;

    constructor(data: T, status: number, message: string) {
        this.data = data;
        this.status = status;
        this.message = message;
    }
}
```

## 常见错误

### 错误 1：类型参数使用错误

```ts
// 错误：类型参数应该在类名后
class Box {
    value: T;
}

// 正确
class Box<T> {
    value: T;
}
```

### 错误 2：静态成员使用类型参数

```ts
class Box<T> {
    // 错误：静态成员不能使用类的类型参数
    static create(value: T): Box<T> {
        return new Box(value);
    }
}

// 正确
class Box<T> {
    static create<U>(value: U): Box<U> {
        return new Box(value);
    }
}
```

## 注意事项

1. **类型参数位置**：类型参数应该在类名后
2. **多个参数**：可以有多个类型参数
3. **静态成员**：静态成员不能使用类的类型参数
4. **继承**：泛型类可以继承其他类

## 最佳实践

1. **使用泛型**：在需要类型安全时使用泛型类
2. **明确类型**：为类型参数使用有意义的名称
3. **静态方法**：静态方法需要自己的类型参数
4. **合理设计**：合理设计泛型类的结构

## 练习

1. **泛型类**：定义不同类型的泛型类。

2. **多个参数**：定义使用多个类型参数的泛型类。

3. **类继承**：定义继承泛型类的类。

4. **静态方法**：定义泛型类的静态方法。

5. **实际应用**：在实际场景中应用泛型类。

完成以上练习后，泛型基础章节学习完成。可以继续学习下一章：泛型约束。

## 总结

泛型类允许在类定义时使用类型参数，在使用时指定具体类型。泛型类可以有多个类型参数，可以继承其他类，但静态成员不能使用类的类型参数。理解泛型类的定义和使用是学习 TypeScript 泛型的关键。

## 相关资源

- [TypeScript 泛型类文档](https://www.typescriptlang.org/docs/handbook/2/generics.html#generic-classes)
