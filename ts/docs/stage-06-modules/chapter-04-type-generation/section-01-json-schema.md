# 6.4.1 json-schema-to-typescript

## 概述

json-schema-to-typescript 可以从 JSON Schema 生成 TypeScript 类型定义。本节介绍 json-schema-to-typescript 的使用。

## 什么是 json-schema-to-typescript

### 定义

json-schema-to-typescript 是一个工具，可以从 JSON Schema 自动生成 TypeScript 类型定义。

### 作用

- 从 JSON Schema 生成类型定义
- 保持类型与 Schema 同步
- 减少手动编写类型的工作

## 安装

### 使用 npm

```bash
npm install --save-dev json-schema-to-typescript
```

### 使用 yarn

```bash
yarn add -D json-schema-to-typescript
```

### 使用 pnpm

```bash
pnpm add -D json-schema-to-typescript
```

## 基本使用

### JSON Schema 示例

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "age": {
      "type": "number"
    }
  },
  "required": ["name"]
}
```

### 生成类型定义

```bash
json2ts schema.json -o types.ts
```

### 生成的类型

```ts
export interface RootObject {
    name: string;
    age?: number;
}
```

## 命令行使用

### 基本命令

```bash
json2ts schema.json -o types.ts
```

### 选项

- `-o, --output`：输出文件路径
- `--bannerComment`：添加文件头注释
- `--declareExternallyReferenced`：声明外部引用
- `--enableConstEnums`：启用常量枚举

### 示例

```bash
json2ts schema.json -o types.ts --bannerComment "/* eslint-disable */"
```

## 编程方式使用

### 基本用法

```ts
import { compile } from "json-schema-to-typescript";

const schema = {
    type: "object",
    properties: {
        name: { type: "string" },
        age: { type: "number" }
    }
};

const types = await compile(schema, "RootObject");
console.log(types);
```

## 使用场景

### 1. API 响应类型

从 API 响应的 JSON Schema 生成类型：

```ts
// 生成的类型
export interface ApiResponse {
    data: User[];
    status: number;
}
```

### 2. 配置类型

从配置文件的 JSON Schema 生成类型：

```ts
// 生成的类型
export interface Config {
    apiUrl: string;
    timeout: number;
}
```

### 3. 数据模型类型

从数据模型的 JSON Schema 生成类型：

```ts
// 生成的类型
export interface User {
    name: string;
    age: number;
}
```

## 常见错误

### 错误 1：Schema 格式错误

```json
// 错误：JSON Schema 格式错误
{
  "type": "object"
  // 缺少逗号
}
```

### 错误 2：输出路径错误

```bash
# 错误：输出路径不存在
json2ts schema.json -o nonexistent/types.ts
```

## 注意事项

1. **Schema 格式**：确保 JSON Schema 格式正确
2. **输出路径**：确保输出路径存在
3. **类型同步**：保持类型与 Schema 同步
4. **工具版本**：使用最新版本的工具

## 最佳实践

1. **使用 JSON Schema**：为数据定义 JSON Schema
2. **自动生成**：使用工具自动生成类型
3. **版本控制**：将生成的类型纳入版本控制
4. **类型同步**：保持类型与 Schema 同步

## 练习

1. **安装工具**：安装 json-schema-to-typescript。

2. **生成类型**：从 JSON Schema 生成类型定义。

3. **实际应用**：在实际场景中使用 json-schema-to-typescript。

完成以上练习后，继续学习下一节，了解 quicktype。

## 总结

json-schema-to-typescript 可以从 JSON Schema 生成 TypeScript 类型定义。使用命令行或编程方式生成类型，保持类型与 Schema 同步。理解 json-schema-to-typescript 的使用是学习类型生成工具的关键。

## 相关资源

- [json-schema-to-typescript GitHub](https://github.com/bcherny/json-schema-to-typescript)
