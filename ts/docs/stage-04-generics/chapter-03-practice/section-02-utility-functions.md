# 4.3.2 工具函数类型化

## 概述

使用泛型类型化工具函数，提供类型安全的工具函数。本节介绍如何使用泛型类型化工具函数。

## 数组工具函数

### 获取第一个元素

```ts
function getFirst<T>(arr: T[]): T | undefined {
    return arr[0];
}

let numbers = [1, 2, 3];
let first = getFirst(numbers); // 类型为 number | undefined
```

### 获取最后一个元素

```ts
function getLast<T>(arr: T[]): T | undefined {
    return arr[arr.length - 1];
}
```

### 数组去重

```ts
function unique<T>(arr: T[]): T[] {
    return Array.from(new Set(arr));
}
```

## 对象工具函数

### 获取属性

```ts
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key];
}

let user = { name: "John", age: 30 };
let name = getProperty(user, "name"); // 类型为 string
```

### 设置属性

```ts
function setProperty<T, K extends keyof T>(
    obj: T,
    key: K,
    value: T[K]
): void {
    obj[key] = value;
}
```

### 选择属性

```ts
function pick<T, K extends keyof T>(
    obj: T,
    keys: K[]
): Pick<T, K> {
    const result = {} as Pick<T, K>;
    for (const key of keys) {
        result[key] = obj[key];
    }
    return result;
}
```

## 函数工具函数

### 防抖

```ts
function debounce<T extends (...args: any[]) => any>(
    fn: T,
    delay: number
): (...args: Parameters<T>) => void {
    let timeoutId: NodeJS.Timeout;
    return function(...args: Parameters<T>) {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => fn(...args), delay);
    };
}
```

### 节流

```ts
function throttle<T extends (...args: any[]) => any>(
    fn: T,
    delay: number
): (...args: Parameters<T>) => void {
    let lastCall = 0;
    return function(...args: Parameters<T>) {
        const now = Date.now();
        if (now - lastCall >= delay) {
            lastCall = now;
            fn(...args);
        }
    };
}
```

## 类型转换函数

### 类型转换

```ts
function cast<T>(value: any): T {
    return value as T;
}
```

### 类型检查

```ts
function isType<T>(
    value: any,
    check: (val: any) => val is T
): value is T {
    return check(value);
}
```

## 使用场景

### 1. 数据处理

```ts
function map<T, U>(arr: T[], fn: (item: T) => U): U[] {
    return arr.map(fn);
}

function filter<T>(arr: T[], fn: (item: T) => boolean): T[] {
    return arr.filter(fn);
}
```

### 2. 对象操作

```ts
function merge<T, U>(target: T, source: U): T & U {
    return { ...target, ...source };
}
```

### 3. 函数组合

```ts
function compose<T, U, V>(
    f: (x: U) => V,
    g: (x: T) => U
): (x: T) => V {
    return (x) => f(g(x));
}
```

## 常见错误

### 错误 1：类型推断失败

```ts
// 错误：类型推断失败
function process(value: any) {
    return value;
}

// 正确：使用泛型
function process<T>(value: T): T {
    return value;
}
```

### 错误 2：类型约束错误

```ts
// 错误：类型约束不正确
function getProperty<T>(obj: T, key: string): any {
    return obj[key];
}

// 正确：使用 keyof 约束
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key];
}
```

## 注意事项

1. **类型参数**：为工具函数提供明确的类型参数
2. **类型约束**：使用类型约束提高类型安全
3. **类型推断**：利用类型推断简化代码
4. **代码复用**：使用泛型提高代码复用

## 最佳实践

1. **明确类型**：为工具函数提供明确的类型
2. **类型安全**：利用泛型提高类型安全
3. **代码复用**：使用泛型封装通用工具函数
4. **类型推断**：利用类型推断简化使用

## 练习

1. **数组工具**：定义不同类型的数组工具函数。

2. **对象工具**：定义不同类型的对象工具函数。

3. **函数工具**：定义不同类型的函数工具函数。

4. **实际应用**：在实际项目中应用工具函数类型化。

完成以上练习后，继续学习下一节，了解数据结构类型化。

## 总结

使用泛型类型化工具函数可以提供类型安全的工具函数。可以定义数组工具函数、对象工具函数、函数工具函数等。理解工具函数类型化是学习 TypeScript 泛型实战的关键。

## 相关资源

- [TypeScript 泛型文档](https://www.typescriptlang.org/docs/handbook/2/generics.html)
