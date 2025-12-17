# 7.1.1 const 类型参数

## 概述

const 类型参数是 TypeScript 5.0 引入的新特性，允许在泛型中使用 const 断言，获得更精确的类型推断。

## 什么是 const 类型参数

### 定义

const 类型参数使用 `const` 关键字修饰泛型参数，使类型推断更加精确。

### 基本语法

```ts
function process<const T>(value: T): T {
    return value;
}
```

## 使用场景

### 1. 数组类型推断

```ts
// 不使用 const 类型参数
function getArray<T>(value: T): T[] {
    return [value];
}

const arr1 = getArray([1, 2, 3]);
// arr1 类型：number[]

// 使用 const 类型参数
function getArrayConst<const T>(value: T): T {
    return value;
}

const arr2 = getArrayConst([1, 2, 3]);
// arr2 类型：readonly [1, 2, 3]
```

### 2. 对象类型推断

```ts
// 不使用 const 类型参数
function getObject<T>(value: T): T {
    return value;
}

const obj1 = getObject({ name: "John", age: 30 });
// obj1 类型：{ name: string; age: number; }

// 使用 const 类型参数
function getObjectConst<const T>(value: T): T {
    return value;
}

const obj2 = getObjectConst({ name: "John", age: 30 });
// obj2 类型：{ readonly name: "John"; readonly age: 30; }
```

### 3. 字面量类型推断

```ts
// 不使用 const 类型参数
function processValue<T>(value: T): T {
    return value;
}

const val1 = processValue("hello");
// val1 类型：string

// 使用 const 类型参数
function processValueConst<const T>(value: T): T {
    return value;
}

const val2 = processValueConst("hello");
// val2 类型："hello"
```

## 与 const 断言的区别

### const 断言

```ts
// 使用 const 断言
const arr = [1, 2, 3] as const;
// arr 类型：readonly [1, 2, 3]
```

### const 类型参数

```ts
// 使用 const 类型参数
function process<const T>(value: T): T {
    return value;
}

const arr = process([1, 2, 3]);
// arr 类型：readonly [1, 2, 3]
```

## 使用场景

### 1. API 响应类型

```ts
function fetchData<const T>(url: string): Promise<T> {
    return fetch(url).then(res => res.json());
}

const data = await fetchData({ users: [{ name: "John" }] });
// data 类型：{ readonly users: readonly [{ readonly name: "John" }] }
```

### 2. 配置对象类型

```ts
function createConfig<const T extends Record<string, any>>(config: T): T {
    return config;
}

const config = createConfig({
    apiUrl: "https://api.example.com",
    timeout: 5000
});
// config 类型：{ readonly apiUrl: "https://api.example.com"; readonly timeout: 5000; }
```

## 常见错误

### 错误 1：过度使用

```ts
// 错误：不需要 const 类型参数
function add<const T>(a: T, b: T): T {
    return a + b; // 错误
}
```

### 错误 2：类型不兼容

```ts
// 错误：const 类型参数可能导致类型不兼容
function process<const T>(value: T): T {
    return value;
}

const result = process([1, 2, 3]);
result.push(4); // 错误：readonly 数组不能 push
```

## 注意事项

1. **使用场景**：在需要精确类型推断时使用
2. **只读性**：const 类型参数会产生只读类型
3. **性能**：不影响运行时性能
4. **兼容性**：需要 TypeScript 5.0+

## 最佳实践

1. **精确推断**：在需要精确类型推断时使用 const 类型参数
2. **API 响应**：用于 API 响应类型定义
3. **配置对象**：用于配置对象的类型定义
4. **避免过度使用**：不要在不必要的地方使用

## 练习

1. **const 类型参数**：练习使用 const 类型参数。

2. **类型推断**：对比使用和不使用 const 类型参数的类型推断。

3. **实际应用**：在实际场景中应用 const 类型参数。

完成以上练习后，继续学习下一节，了解装饰器元数据。

## 总结

const 类型参数允许在泛型中使用 const 断言，获得更精确的类型推断。使用 `const` 关键字修饰泛型参数，适用于需要精确类型推断的场景。理解 const 类型参数的使用是学习 TypeScript 5.0 新特性的关键。

## 相关资源

- [TypeScript 5.0 const 类型参数](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-0.html#const-type-parameters)
