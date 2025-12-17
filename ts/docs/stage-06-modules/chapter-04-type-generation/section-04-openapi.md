# 6.4.4 openapi-typescript

## 概述

openapi-typescript 可以从 OpenAPI/Swagger 规范生成 TypeScript 类型定义。本节介绍 openapi-typescript 的使用。

## 什么是 openapi-typescript

### 定义

openapi-typescript 是一个工具，可以从 OpenAPI/Swagger 规范自动生成 TypeScript 类型定义。

### 作用

- 从 OpenAPI 规范生成类型定义
- 保持类型与 API 规范同步
- 减少手动编写类型的工作

## 安装

### 使用 npm

```bash
npm install --save-dev openapi-typescript
```

### 使用 yarn

```bash
yarn add -D openapi-typescript
```

### 使用 pnpm

```bash
pnpm add -D openapi-typescript
```

## 基本使用

### 从 OpenAPI 规范生成类型

```bash
openapi-typescript https://api.example.com/openapi.json -o api-types.ts
```

### 从本地文件生成类型

```bash
openapi-typescript openapi.json -o api-types.ts
```

## 命令行使用

### 基本命令

```bash
openapi-typescript [input] -o [output]
```

### 选项

- `-o, --output`：输出文件路径
- `--auth`：API 认证信息
- `--header`：HTTP 请求头

### 示例

```bash
openapi-typescript https://api.example.com/openapi.json -o api-types.ts --auth "Bearer token"
```

## 生成的类型

### OpenAPI 规范示例

```json
{
  "openapi": "3.0.0",
  "paths": {
    "/users": {
      "get": {
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "data": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/User"
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "User": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "age": {
            "type": "number"
          }
        }
      }
    }
  }
}
```

### 生成的类型

```ts
export interface paths {
    "/users": {
        get: {
            responses: {
                200: {
                    content: {
                        "application/json": {
                            schema: {
                                data: components["schemas"]["User"][];
                            };
                        };
                    };
                };
            };
        };
    };
}

export interface components {
    schemas: {
        User: {
            name: string;
            age: number;
        };
    };
}
```

## 使用场景

### 1. REST API 类型

从 REST API 的 OpenAPI 规范生成类型：

```bash
openapi-typescript https://api.example.com/openapi.json -o api-types.ts
```

### 2. API 客户端类型

生成 API 客户端的类型定义：

```ts
import type { paths } from "./api-types";

type GetUsersResponse = paths["/users"]["get"]["responses"]["200"]["content"]["application/json"]["schema"];

async function getUsers(): Promise<GetUsersResponse> {
    const response = await fetch("https://api.example.com/users");
    return await response.json();
}
```

### 3. API 规范同步

保持类型与 API 规范同步：

```bash
# 定期更新类型
openapi-typescript https://api.example.com/openapi.json -o api-types.ts
```

## 自动化流程

### 使用脚本

```bash
#!/bin/bash
# generate-api-types.sh

# 生成类型
openapi-typescript https://api.example.com/openapi.json -o api-types.ts
```

### 使用 npm 脚本

```json
{
  "scripts": {
    "generate:api-types": "openapi-typescript https://api.example.com/openapi.json -o api-types.ts"
  }
}
```

## 常见错误

### 错误 1：OpenAPI 规范格式错误

```bash
# 错误：OpenAPI 规范格式不正确
openapi-typescript invalid.json -o api-types.ts
```

### 错误 2：网络错误

```bash
# 错误：无法访问 OpenAPI 规范 URL
openapi-typescript https://invalid-url.com/openapi.json -o api-types.ts
```

## 注意事项

1. **规范格式**：确保 OpenAPI 规范格式正确
2. **网络访问**：确保可以访问 OpenAPI 规范 URL
3. **类型同步**：保持类型与 API 规范同步
4. **工具版本**：使用最新版本的工具

## 最佳实践

1. **使用 openapi-typescript**：从 OpenAPI 规范生成类型
2. **自动化**：使用脚本自动化类型生成
3. **版本控制**：将生成的类型纳入版本控制
4. **类型同步**：保持类型与 API 规范同步

## 练习

1. **安装工具**：安装 openapi-typescript。

2. **生成类型**：从 OpenAPI 规范生成类型定义。

3. **实际应用**：在实际场景中使用 openapi-typescript。

完成以上练习后，类型生成工具章节学习完成。阶段六学习完成。

## 总结

openapi-typescript 可以从 OpenAPI/Swagger 规范生成 TypeScript 类型定义。使用命令行生成类型，保持类型与 API 规范同步。理解 openapi-typescript 的使用是学习类型生成工具的关键。

## 相关资源

- [openapi-typescript GitHub](https://github.com/drwpow/openapi-typescript)
