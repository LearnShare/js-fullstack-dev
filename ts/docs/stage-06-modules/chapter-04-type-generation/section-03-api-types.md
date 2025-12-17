# 6.4.3 从 API 生成类型

## 概述

可以从 API 响应自动生成 TypeScript 类型定义。本节介绍从 API 生成类型的方法。

## 方法

### 1. 使用 quicktype

从 API 响应 JSON 生成类型：

```bash
# 获取 API 响应
curl https://api.example.com/users > users.json

# 生成类型
quicktype users.json -o api-types.ts
```

### 2. 使用 json-schema-to-typescript

如果 API 提供 JSON Schema：

```bash
# 获取 JSON Schema
curl https://api.example.com/schema > schema.json

# 生成类型
json2ts schema.json -o api-types.ts
```

### 3. 使用 openapi-typescript

如果 API 提供 OpenAPI 规范：

```bash
# 从 OpenAPI 规范生成类型
openapi-typescript https://api.example.com/openapi.json -o api-types.ts
```

## 工作流程

### 1. 获取 API 响应

```bash
# 使用 curl 获取 API 响应
curl https://api.example.com/users > users.json
```

### 2. 生成类型定义

```bash
# 使用 quicktype 生成类型
quicktype users.json -o api-types.ts
```

### 3. 使用生成的类型

```ts
import { User } from "./api-types";

async function fetchUsers(): Promise<User[]> {
    const response = await fetch("https://api.example.com/users");
    const users: User[] = await response.json();
    return users;
}
```

## 自动化流程

### 使用脚本

```bash
#!/bin/bash
# generate-api-types.sh

# 获取 API 响应
curl https://api.example.com/users > users.json

# 生成类型
quicktype users.json -o api-types.ts

# 清理临时文件
rm users.json
```

### 使用 npm 脚本

```json
{
  "scripts": {
    "generate:api-types": "curl https://api.example.com/users > users.json && quicktype users.json -o api-types.ts && rm users.json"
  }
}
```

## 使用场景

### 1. REST API

从 REST API 响应生成类型：

```bash
# 获取 API 响应
curl https://api.example.com/users > users.json

# 生成类型
quicktype users.json -o api-types.ts
```

### 2. GraphQL API

从 GraphQL Schema 生成类型：

```bash
# 获取 GraphQL Schema
curl https://api.example.com/graphql -d '{ __schema { types { name } } }' > schema.json

# 生成类型
quicktype schema.json -o graphql-types.ts
```

### 3. OpenAPI API

从 OpenAPI 规范生成类型：

```bash
# 从 OpenAPI 规范生成类型
openapi-typescript https://api.example.com/openapi.json -o api-types.ts
```

## 常见错误

### 错误 1：API 响应格式不一致

```ts
// 错误：API 响应格式可能不一致
// 需要处理多种响应格式
```

### 错误 2：类型不准确

```ts
// 错误：生成的类型可能不准确
// 需要手动调整类型定义
```

## 注意事项

1. **API 响应**：确保 API 响应格式正确
2. **类型准确性**：检查生成的类型是否准确
3. **类型同步**：保持类型与 API 同步
4. **错误处理**：处理 API 错误响应

## 最佳实践

1. **自动化**：使用脚本自动化类型生成
2. **类型检查**：检查生成的类型是否准确
3. **版本控制**：将生成的类型纳入版本控制
4. **类型同步**：保持类型与 API 同步

## 练习

1. **从 API 生成类型**：练习从 API 响应生成类型定义。

2. **自动化流程**：设置自动化类型生成流程。

3. **实际应用**：在实际场景中从 API 生成类型。

完成以上练习后，继续学习下一节，了解 openapi-typescript。

## 总结

可以从 API 响应自动生成 TypeScript 类型定义。使用 quicktype、json-schema-to-typescript 或 openapi-typescript 生成类型，保持类型与 API 同步。理解从 API 生成类型是学习类型生成工具的关键。

## 相关资源

- [quicktype GitHub](https://github.com/quicktype/quicktype)
- [openapi-typescript GitHub](https://github.com/drwpow/openapi-typescript)
