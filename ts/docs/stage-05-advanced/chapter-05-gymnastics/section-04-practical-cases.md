# 5.5.4 实际应用案例

## 概述

本节介绍类型体操在实际项目中的应用案例，包括工具类型、API 类型、状态管理等。

## 工具类型应用

### 深度只读

```ts
type DeepReadonly<T> = {
    readonly [P in keyof T]: T[P] extends object
        ? T[P] extends Function
            ? T[P]
            : DeepReadonly<T[P]>
        : T[P];
};

interface Config {
    api: {
        baseUrl: string;
        timeout: number;
    };
    features: {
        enabled: boolean;
    };
}

type ReadonlyConfig = DeepReadonly<Config>;
```

### 路径类型

```ts
type Paths<T> = T extends object
    ? {
          [K in keyof T]: K extends string
              ? T[K] extends object
                  ? K | `${K}.${Paths<T[K]>}`
                  : K
              : never;
      }[keyof T]
    : never;

interface User {
    name: string;
    address: {
        city: string;
        country: string;
    };
}

type UserPaths = Paths<User>;
// "name" | "address" | "address.city" | "address.country"
```

## API 类型应用

### 请求类型提取

```ts
type ApiRequest<T> = T extends (...args: any[]) => Promise<infer R>
    ? R extends { data: infer D }
        ? D
        : never
    : never;

async function getUser(id: number): Promise<{ data: User }> {
    // ...
}

type UserRequest = ApiRequest<typeof getUser>; // User
```

### 响应类型封装

```ts
type ApiResponse<T> = {
    data: T;
    status: number;
    message: string;
};

type ExtractApiData<T> = T extends ApiResponse<infer D> ? D : never;

type UserResponse = ApiResponse<User>;
type UserData = ExtractApiData<UserResponse>; // User
```

## 状态管理应用

### 状态类型

```ts
type State = {
    user: {
        name: string;
        profile: {
            age: number;
            email: string;
        };
    };
    settings: {
        theme: string;
    };
};

type StatePaths = Paths<State>;
// "user" | "user.name" | "user.profile" | "user.profile.age" | "user.profile.email" | "settings" | "settings.theme"
```

### 状态更新类型

```ts
type StateUpdate<T> = DeepPartial<T>;

type UserStateUpdate = StateUpdate<State["user"]>;
// {
//     name?: string;
//     profile?: {
//         age?: number;
//         email?: string;
//     };
// }
```

## 表单处理应用

### 表单字段类型

```ts
type FormFields<T> = {
    [K in keyof T]: {
        value: T[K];
        error?: string;
    };
};

interface UserForm {
    name: string;
    email: string;
    age: number;
}

type UserFormFields = FormFields<UserForm>;
// {
//     name: { value: string; error?: string };
//     email: { value: string; error?: string };
//     age: { value: number; error?: string };
// }
```

### 表单验证类型

```ts
type ValidationRules<T> = {
    [K in keyof T]?: (value: T[K]) => boolean | string;
};

type FormErrors<T> = Partial<Record<keyof T, string>>;
```

## 路由类型应用

### 路由参数提取

```ts
type RouteParams<T extends string> = T extends `${string}:${infer Param}/${infer Rest}`
    ? Param extends `${infer Name}?`
        ? { [K in Name]?: string } & RouteParams<Rest>
        : { [K in Param]: string } & RouteParams<Rest>
    : T extends `${string}:${infer Param}`
    ? Param extends `${infer Name}?`
        ? { [K in Name]?: string }
        : { [K in Param]: string }
    : {};

type UserRoute = RouteParams<"/users/:id/posts/:postId">;
// { id: string; postId: string }
```

## 常见错误

### 错误 1：过度复杂

```ts
// 错误：类型体操过于复杂
type OverlyComplex<T> = T extends infer U
    ? U extends object
        ? U extends Function
            ? U
            : {
                  [K in keyof U]: U[K] extends object
                      ? U[K] extends Function
                          ? U[K]
                          : OverlyComplex<U[K]>
                      : U[K];
              }
        : U
    : never;

// 正确：保持简洁
type Simple<T> = {
    [P in keyof T]: T[P];
};
```

### 错误 2：性能问题

```ts
// 错误：可能导致编译性能问题
type VeryDeep<T, Depth extends number[] = []> = Depth["length"] extends 10
    ? T
    : {
          [P in keyof T]: T[P] extends object
              ? VeryDeep<T[P], [...Depth, any]>
              : T[P];
      };

// 正确：限制递归深度
type LimitedDepth<T> = {
    [P in keyof T]: T[P] extends object
        ? T[P] extends Function
            ? T[P]
            : Partial<T[P]>
        : T[P];
};
```

## 注意事项

1. **复杂度**：避免过度复杂的类型体操
2. **性能**：考虑编译性能影响
3. **可读性**：保持类型体操可读性
4. **实用性**：确保类型体操有实际用途

## 最佳实践

1. **保持简洁**：尽量保持类型体操简洁
2. **实际应用**：在实际项目中应用类型体操
3. **性能考虑**：考虑编译性能影响
4. **文档说明**：为复杂类型体操添加文档

## 练习

1. **工具类型**：创建实用的工具类型。

2. **API 类型**：使用类型体操处理 API 类型。

3. **状态管理**：使用类型体操处理状态类型。

4. **实际应用**：在实际项目中应用类型体操。

完成以上练习后，类型体操章节学习完成。可以继续学习下一章：类型兼容性。

## 总结

类型体操在实际项目中有广泛应用，包括工具类型、API 类型、状态管理等。保持类型体操简洁实用，考虑编译性能。理解类型体操的实际应用是学习 TypeScript 高级类型系统的关键。

## 相关资源

- [TypeScript 类型体操挑战](https://github.com/type-challenges/type-challenges)
