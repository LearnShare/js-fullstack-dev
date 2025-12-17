# 5.3.3 键重映射（Key Remapping）

## 概述

键重映射允许在映射类型中重命名或转换键。本节介绍键重映射的使用。

## 什么是键重映射

### 定义

键重映射允许在映射类型中使用 `as` 关键字重命名或转换键。

### 基本语法

```ts
type MappedType<T> = {
    [P in keyof T as NewKey]: T[P];
};
```

### 示例

```ts
type AddPrefix<T> = {
    [P in keyof T as `prefix_${string & P}`]: T[P];
};

interface User {
    name: string;
    age: number;
}

type PrefixedUser = AddPrefix<User>;
// { prefix_name: string; prefix_age: number; }
```

## 键重命名

### 添加前缀

```ts
type AddPrefix<T, Prefix extends string> = {
    [P in keyof T as `${Prefix}${string & P}`]: T[P];
};

interface User {
    name: string;
    age: number;
}

type PrefixedUser = AddPrefix<User, "user_">;
// { user_name: string; user_age: number; }
```

### 添加后缀

```ts
type AddSuffix<T, Suffix extends string> = {
    [P in keyof T as `${string & P}${Suffix}`]: T[P];
};

interface User {
    name: string;
    age: number;
}

type SuffixedUser = AddSuffix<User, "_prop">;
// { name_prop: string; age_prop: number; }
```

## 键过滤

### 排除特定键

```ts
type Omit<T, K extends keyof T> = {
    [P in keyof T as P extends K ? never : P]: T[P];
};

interface User {
    name: string;
    age: number;
    email: string;
}

type UserWithoutEmail = Omit<User, "email">;
// { name: string; age: number; }
```

### 选择特定键

```ts
type Pick<T, K extends keyof T> = {
    [P in K]: T[P];
};

interface User {
    name: string;
    age: number;
    email: string;
}

type UserNameAge = Pick<User, "name" | "age">;
// { name: string; age: number; }
```

## 键转换

### 转换为大写

```ts
type UppercaseKeys<T> = {
    [P in keyof T as Uppercase<string & P>]: T[P];
};

interface User {
    name: string;
    age: number;
}

type UppercaseUser = UppercaseKeys<User>;
// { NAME: string; AGE: number; }
```

### 转换为小写

```ts
type LowercaseKeys<T> = {
    [P in keyof T as Lowercase<string & P>]: T[P];
};
```

## 使用场景

### 1. API 转换

```ts
type ApiResponse<T> = {
    [P in keyof T as `api_${string & P}`]: T[P];
};
```

### 2. 数据库字段

```ts
type DbFields<T> = {
    [P in keyof T as `db_${string & P}`]: T[P];
};
```

### 3. 表单字段

```ts
type FormFields<T> = {
    [P in keyof T as `form_${string & P}`]: T[P];
};
```

## 常见错误

### 错误 1：键类型错误

```ts
// 错误：键必须是 string | number | symbol
type Invalid<T> = {
    [P in keyof T as boolean]: T[P];
};
```

### 错误 2：模板字面量错误

```ts
// 错误：模板字面量类型使用错误
type Invalid<T> = {
    [P in keyof T as `prefix_${P}`]: T[P];
    // P 需要转换为 string
};
```

## 注意事项

1. **as 关键字**：使用 `as` 关键字进行键重映射
2. **类型转换**：键需要转换为 string 类型
3. **模板字面量**：可以使用模板字面量类型
4. **类型安全**：键重映射提供类型安全

## 最佳实践

1. **使用键重映射**：在需要重命名键时使用键重映射
2. **类型转换**：确保键类型正确
3. **模板字面量**：使用模板字面量类型创建新键
4. **类型安全**：利用键重映射提高类型安全

## 练习

1. **键重命名**：使用键重映射重命名键。

2. **键过滤**：使用键重映射过滤键。

3. **键转换**：使用键重映射转换键。

4. **实际应用**：在实际场景中应用键重映射。

完成以上练习后，继续学习下一节，了解模板字面量类型。

## 总结

键重映射允许在映射类型中重命名或转换键。可以使用 `as` 关键字和模板字面量类型。理解键重映射的使用是学习 TypeScript 高级类型系统的关键。

## 相关资源

- [TypeScript 键重映射文档](https://www.typescriptlang.org/docs/handbook/2/mapped-types.html#key-remapping-via-as)
