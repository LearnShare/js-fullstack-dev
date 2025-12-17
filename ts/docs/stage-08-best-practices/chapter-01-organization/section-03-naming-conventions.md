# 8.1.3 命名规范

## 概述

遵循命名规范有助于代码的可读性和维护性。本节介绍 TypeScript 的命名规范。

## 命名规范

### 1. 变量和函数

使用驼峰命名法（camelCase）：

```ts
const userName = "John";
const userAge = 30;

function getUserName(): string {
    return userName;
}
```

### 2. 类和接口

使用帕斯卡命名法（PascalCase）：

```ts
class UserService {
    // ...
}

interface UserConfig {
    // ...
}
```

### 3. 类型别名

使用帕斯卡命名法（PascalCase）：

```ts
type UserStatus = "active" | "inactive";
type ApiResponse<T> = {
    data: T;
    status: number;
};
```

### 4. 常量

使用大写下划线命名法（UPPER_SNAKE_CASE）：

```ts
const API_URL = "https://api.example.com";
const MAX_RETRY_COUNT = 3;
```

### 5. 私有成员

使用下划线前缀（_private）：

```ts
class MyClass {
    private _privateProperty: string;
    
    private _privateMethod(): void {
        // ...
    }
}
```

## 命名约定

### 1. 布尔值

使用 `is`、`has`、`can` 等前缀：

```ts
const isActive = true;
const hasPermission = false;
const canEdit = true;
```

### 2. 数组

使用复数形式：

```ts
const users: User[] = [];
const products: Product[] = [];
```

### 3. 事件处理函数

使用 `on` 或 `handle` 前缀：

```ts
function onClick(): void {}
function handleSubmit(): void {}
```

### 4. 异步函数

使用明确的命名：

```ts
async function fetchUser(): Promise<User> {}
async function loadData(): Promise<void> {}
```

## 使用场景

### 1. 变量命名

```ts
const userName = "John";
const userAge = 30;
const isActive = true;
```

### 2. 函数命名

```ts
function getUserName(): string {}
function setUserName(name: string): void {}
function hasPermission(): boolean {}
```

### 3. 类命名

```ts
class UserService {}
class ProductController {}
class ApiClient {}
```

## 注意事项

1. **一致性**：保持命名一致性
2. **可读性**：使用有意义的命名
3. **避免缩写**：避免使用难以理解的缩写
4. **遵循规范**：遵循团队或项目的命名规范

## 最佳实践

1. **遵循规范**：遵循 TypeScript 命名规范
2. **一致性**：保持命名一致性
3. **可读性**：使用有意义的命名
4. **文档注释**：为重要的命名添加文档注释

## 练习

1. **命名规范**：练习遵循命名规范。

2. **命名约定**：使用命名约定。

3. **实际应用**：在实际项目中应用命名规范。

完成以上练习后，代码组织章节学习完成。可以继续学习下一章：类型安全最佳实践。

## 总结

遵循命名规范有助于代码的可读性和维护性。使用驼峰命名法、帕斯卡命名法等，遵循命名约定。理解命名规范是学习代码组织的关键。

## 相关资源

- [TypeScript 命名规范](https://www.typescriptlang.org/docs/handbook/declaration-files/do-s-and-don-ts.html)
