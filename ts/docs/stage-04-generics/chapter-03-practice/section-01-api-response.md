# 4.3.1 API 响应类型封装

## 概述

使用泛型封装 API 响应类型，提供类型安全的 API 调用。本节介绍如何使用泛型封装 API 响应类型。

## 基本响应类型

### 定义响应接口

```ts
interface ApiResponse<T> {
    data: T;
    status: number;
    message: string;
}

// 使用
type UserResponse = ApiResponse<{
    id: number;
    name: string;
    email: string;
}>;
```

### 错误响应类型

```ts
interface ApiError {
    code: string;
    message: string;
}

interface ApiResponse<T> {
    data: T | null;
    error: ApiError | null;
    status: number;
}
```

## 分页响应类型

### 定义分页接口

```ts
interface PaginatedResponse<T> {
    data: T[];
    pagination: {
        page: number;
        pageSize: number;
        total: number;
        totalPages: number;
    };
}

// 使用
type UsersResponse = PaginatedResponse<{
    id: number;
    name: string;
    email: string;
}>;
```

## API 函数封装

### 基本封装

```ts
async function fetchApi<T>(
    url: string
): Promise<ApiResponse<T>> {
    const response = await fetch(url);
    const data = await response.json();
    return data;
}

// 使用
const userResponse = await fetchApi<{
    id: number;
    name: string;
}>(`/api/users/1`);
```

### 带参数的封装

```ts
async function fetchApi<T>(
    url: string,
    options?: RequestInit
): Promise<ApiResponse<T>> {
    const response = await fetch(url, options);
    const data = await response.json();
    return data;
}
```

## 使用场景

### 1. 用户 API

```ts
interface User {
    id: number;
    name: string;
    email: string;
}

async function getUser(id: number): Promise<ApiResponse<User>> {
    return fetchApi<User>(`/api/users/${id}`);
}
```

### 2. 列表 API

```ts
async function getUsers(): Promise<PaginatedResponse<User>> {
    return fetchApi<PaginatedResponse<User>>(`/api/users`);
}
```

### 3. 创建 API

```ts
interface CreateUserRequest {
    name: string;
    email: string;
}

async function createUser(
    data: CreateUserRequest
): Promise<ApiResponse<User>> {
    return fetchApi<User>(`/api/users`, {
        method: "POST",
        body: JSON.stringify(data),
    });
}
```

## 常见错误

### 错误 1：类型不匹配

```ts
// 错误：响应类型不匹配
const response = await fetchApi<string>(`/api/users/1`);
// response.data 应该是 User，不是 string
```

### 错误 2：缺少类型参数

```ts
// 错误：缺少类型参数
const response = await fetchApi(`/api/users/1`);
// response.data 的类型是 unknown
```

## 注意事项

1. **类型参数**：为 API 函数提供明确的类型参数
2. **错误处理**：处理 API 错误响应
3. **类型安全**：确保响应类型与实际数据匹配
4. **代码复用**：使用泛型提高代码复用

## 最佳实践

1. **明确类型**：为 API 响应提供明确的类型
2. **错误处理**：处理 API 错误情况
3. **类型安全**：利用泛型提高类型安全
4. **代码复用**：使用泛型封装通用 API 函数

## 练习

1. **响应类型**：定义不同类型的 API 响应类型。

2. **API 封装**：封装不同类型的 API 函数。

3. **错误处理**：实现 API 错误处理。

4. **实际应用**：在实际项目中应用 API 响应类型封装。

完成以上练习后，继续学习下一节，了解工具函数类型化。

## 总结

使用泛型封装 API 响应类型可以提供类型安全的 API 调用。可以定义基本响应类型、分页响应类型，并使用泛型封装 API 函数。理解 API 响应类型封装是学习 TypeScript 泛型实战的关键。

## 相关资源

- [TypeScript 泛型文档](https://www.typescriptlang.org/docs/handbook/2/generics.html)
