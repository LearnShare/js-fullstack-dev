# 4.1.5 API 文档（OpenAPI/Swagger）

## 1. 概述

API 文档是 API 开发的重要组成部分，良好的文档可以帮助开发者快速理解和使用 API。OpenAPI（原 Swagger）是最流行的 API 文档标准，提供了统一的 API 描述格式和丰富的工具生态。本节介绍如何使用 OpenAPI/Swagger 编写和维护 API 文档。

## 2. OpenAPI 规范

### 2.1 OpenAPI 简介

OpenAPI 是一个用于描述 RESTful API 的规范，最初由 Swagger 发展而来。OpenAPI 规范使用 YAML 或 JSON 格式描述 API，包括端点、参数、响应、认证等信息。

### 2.2 OpenAPI 版本

| 版本      | 发布时间 | 说明                           |
|:----------|:---------|:-------------------------------|
| **Swagger 2.0** | 2014     | 最初的 Swagger 规范            |
| **OpenAPI 3.0** | 2017     | 正式更名为 OpenAPI 3.0         |
| **OpenAPI 3.1** | 2021     | 最新版本，支持 JSON Schema 2020-12 |

### 2.3 OpenAPI 工具生态

- **Swagger UI**：交互式 API 文档界面
- **Swagger Editor**：在线编辑 OpenAPI 文档
- **Swagger Codegen**：从 OpenAPI 文档生成客户端代码
- **OpenAPI Generator**：更强大的代码生成工具

## 3. OpenAPI 文档结构

### 3.1 基本结构

```yaml
openapi: 3.1.0
info:
  title: User API
  version: 1.0.0
  description: User management API
servers:
  - url: https://api.example.com/v1
paths:
  /users:
    get:
      summary: Get user list
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
```

### 3.2 主要组成部分

| 部分         | 说明                           |
|:-------------|:-------------------------------|
| **openapi**  | OpenAPI 规范版本               |
| **info**     | API 基本信息                   |
| **servers**  | 服务器地址列表                 |
| **paths**    | API 端点定义                   |
| **components**| 可重用组件（schemas、parameters 等） |
| **security** | 安全定义                       |
| **tags**     | 标签分组                       |

## 4. 编写 OpenAPI 文档

### 4.1 基本信息

```yaml
openapi: 3.1.0
info:
  title: User API
  version: 1.0.0
  description: |
    User management API for managing users and their profiles.
  contact:
    name: API Support
    email: support@example.com
  license:
    name: MIT
    url: https://opensource.org/licenses/MIT
servers:
  - url: https://api.example.com/v1
    description: Production server
  - url: https://staging-api.example.com/v1
    description: Staging server
```

### 4.2 路径定义

```yaml
paths:
  /users:
    get:
      summary: Get user list
      description: Retrieve a list of users
      tags:
        - Users
      parameters:
        - name: page
          in: query
          schema:
            type: integer
            default: 1
        - name: limit
          in: query
          schema:
            type: integer
            default: 20
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/User'
                  pagination:
                    $ref: '#/components/schemas/Pagination'
    post:
      summary: Create user
      description: Create a new user
      tags:
        - Users
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateUserRequest'
      responses:
        '201':
          description: User created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
  /users/{id}:
    get:
      summary: Get user by ID
      tags:
        - Users
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '404':
          description: User not found
```

### 4.3 组件定义

```yaml
components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: integer
          example: 1
        name:
          type: string
          example: John Doe
        email:
          type: string
          format: email
          example: john@example.com
        createdAt:
          type: string
          format: date-time
      required:
        - id
        - name
        - email
    CreateUserRequest:
      type: object
      properties:
        name:
          type: string
          minLength: 1
          maxLength: 100
        email:
          type: string
          format: email
      required:
        - name
        - email
    Pagination:
      type: object
      properties:
        page:
          type: integer
        limit:
          type: integer
        total:
          type: integer
        totalPages:
          type: integer
    Error:
      type: object
      properties:
        error:
          type: object
          properties:
            code:
              type: string
            message:
              type: string
            details:
              type: array
              items:
                type: object
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
```

### 4.4 安全定义

```yaml
security:
  - BearerAuth: []

paths:
  /users:
    get:
      security:
        - BearerAuth: []
      # ...
```

## 5. 使用 Swagger UI

### 5.1 安装 Swagger UI

```bash
npm install swagger-ui-express
npm install --save-dev @types/swagger-ui-express
```

### 5.2 集成 Swagger UI

```ts
import express, { Express } from 'express';
import swaggerUi from 'swagger-ui-express';
import swaggerDocument from './swagger.json';

const app: Express = express();

app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocument));

app.listen(3000, (): void => {
  console.log('Server running on http://localhost:3000');
  console.log('API docs available at http://localhost:3000/api-docs');
});
```

### 5.3 从代码生成文档

使用 `swagger-jsdoc` 从代码注释生成 OpenAPI 文档：

```bash
npm install swagger-jsdoc
npm install --save-dev @types/swagger-jsdoc
```

```ts
import swaggerJsdoc from 'swagger-jsdoc';

const options: swaggerJsdoc.Options = {
  definition: {
    openapi: '3.1.0',
    info: {
      title: 'User API',
      version: '1.0.0',
      description: 'User management API'
    },
    servers: [
      {
        url: 'http://localhost:3000',
        description: 'Development server'
      }
    ]
  },
  apis: ['./src/routes/*.ts']
};

const swaggerSpec = swaggerJsdoc(options);
```

### 5.4 代码注释示例

```ts
/**
 * @swagger
 * /users:
 *   get:
 *     summary: Get user list
 *     tags: [Users]
 *     parameters:
 *       - in: query
 *         name: page
 *         schema:
 *           type: integer
 *         description: Page number
 *     responses:
 *       200:
 *         description: Success
 *         content:
 *           application/json:
 *             schema:
 *               type: object
 */
app.get('/users', (req: Request, res: Response) => {
  // ...
});
```

## 6. 使用 TypeScript 类型生成 OpenAPI

### 6.1 安装工具

```bash
npm install --save-dev typescript-json-schema
npm install --save-dev openapi-typescript-codegen
```

### 6.2 从 TypeScript 类型生成 JSON Schema

```ts
// types/user.ts
export interface User {
  id: number;
  name: string;
  email: string;
  createdAt: Date;
}

export interface CreateUserRequest {
  name: string;
  email: string;
}
```

```bash
typescript-json-schema types/user.ts User --required > schemas/user.json
```

### 6.3 使用工具生成 OpenAPI 文档

使用 `tsoa` 从 TypeScript 装饰器生成 OpenAPI 文档：

```bash
npm install tsoa
```

```ts
import { Controller, Get, Post, Route, Body, Path } from 'tsoa';

@Route('users')
export class UsersController extends Controller {
  @Get()
  public async getUsers(
    @Query() page: number = 1,
    @Query() limit: number = 20
  ): Promise<{ data: User[]; pagination: Pagination }> {
    // ...
  }

  @Post()
  public async createUser(@Body() request: CreateUserRequest): Promise<User> {
    // ...
  }
}
```

## 7. API 文档最佳实践

### 7.1 文档编写原则

- **完整性**：覆盖所有端点和参数
- **准确性**：确保文档与实现一致
- **清晰性**：使用清晰的描述和示例
- **及时性**：保持文档的及时更新

### 7.2 文档结构建议

- **按功能分组**：使用 tags 对端点进行分组
- **提供示例**：为每个端点和参数提供示例
- **错误说明**：详细说明可能的错误响应
- **认证说明**：明确说明认证要求

### 7.3 文档维护建议

- **代码即文档**：从代码生成文档，保持同步
- **版本控制**：为文档使用版本控制
- **审查流程**：建立文档审查流程
- **自动化测试**：使用文档进行 API 测试

## 8. 代码示例

### 8.1 完整的 OpenAPI 文档示例

```yaml
openapi: 3.1.0
info:
  title: User API
  version: 1.0.0
  description: User management API
servers:
  - url: https://api.example.com/v1
paths:
  /users:
    get:
      summary: Get user list
      tags: [Users]
      parameters:
        - name: page
          in: query
          schema:
            type: integer
            default: 1
        - name: limit
          in: query
          schema:
            type: integer
            default: 20
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/User'
                  pagination:
                    $ref: '#/components/schemas/Pagination'
    post:
      summary: Create user
      tags: [Users]
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateUserRequest'
      responses:
        '201':
          description: User created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: integer
        name:
          type: string
        email:
          type: string
          format: email
      required:
        - id
        - name
        - email
    CreateUserRequest:
      type: object
      properties:
        name:
          type: string
        email:
          type: string
          format: email
      required:
        - name
        - email
    Pagination:
      type: object
      properties:
        page:
          type: integer
        limit:
          type: integer
        total:
          type: integer
        totalPages:
          type: integer
    Error:
      type: object
      properties:
        error:
          type: object
          properties:
            code:
              type: string
            message:
              type: string
```

## 9. 注意事项

- **文档同步**：确保文档与代码实现保持同步
- **版本管理**：为文档使用版本控制
- **示例准确性**：确保示例代码可以实际运行
- **安全信息**：不要在文档中暴露敏感信息

## 10. 常见问题

### 10.1 如何保持文档与代码同步？

- 使用代码生成文档的工具（如 tsoa、swagger-jsdoc）
- 建立文档审查流程
- 使用自动化测试验证文档

### 10.2 如何处理文档版本？

- 为文档使用版本控制
- 在文档中明确标注版本
- 提供版本迁移指南

### 10.3 如何生成客户端代码？

使用 OpenAPI Generator：

```bash
npx @openapitools/openapi-generator-cli generate \
  -i openapi.yaml \
  -g typescript-axios \
  -o ./client
```

---

**下一章**：[4.2 Web 框架概览](../chapter-02-frameworks/readme.md)
