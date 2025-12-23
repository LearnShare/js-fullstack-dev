# 代码格式规范

## 代码示例要求

### 基本要求

**必须遵守**：
- 代码示例必须完整、可运行
- 提供语法格式、参数说明
- 每个知识点都配有完整的代码示例
- 默认使用 ASCII 字符

### 代码完整性

**要求**：
- 代码示例必须包含必要的上下文
- 不能是伪代码或片段（除非明确标注为片段）
- 必须包含必要的导入语句

**示例**：

```ts
import { createServer } from 'node:http';

function calculateSum(a: number, b: number): number {
  return a + b;
}

console.log(calculateSum(5, 3));  // 8
```

## TypeScript 代码规范

### TypeScript First

**必须遵守**：
- **所有代码示例必须 100% 使用 TypeScript 编写**
- 代码语言标签使用 `ts`（不是 `typescript`）
- 禁止使用 `js` 或 `javascript` 标签

### 类型注解

**必须遵守**：
- 所有函数参数必须有类型注解
- 所有变量必须有类型注解（除非类型可以明确推断）
- 所有接口和类型定义必须完整
- 所有类属性必须有类型注解
- 所有函数返回值类型应明确标注

**示例**：

```ts
// 文件: src/utils/helper.ts
// 功能: 用户服务类

interface User {
  id: number;
  name: string;
  email: string;
}

class UserService {
  private users: User[] = [];

  public addUser(user: User): void {
    this.users.push(user);
  }

  public getUserById(id: number): User | undefined {
    return this.users.find((user: User) => user.id === id);
  }
}
```

### ES Modules (ESM)

**必须遵守**：
- 强制使用 ES Modules 规范
- 必须使用 `import` 而非 `require`
- 所有导入语句使用 ESM 语法

**示例**：

```ts
// ✅ 正确
import express from 'express';
import { readFile } from 'node:fs/promises';

// ❌ 错误
const express = require('express');
const { readFile } = require('fs/promises');
```

### Node.js 内置模块

**必须遵守**：
- 所有 Node.js 内置模块必须使用 `node:` 前缀
- 包括：`node:http`、`node:fs`、`node:path`、`node:crypto`、`node:os`、`node:process`、`node:events`、`node:stream`、`node:buffer`、`node:url`、`node:querystring`、`node:util`、`node:child_process`、`node:cluster` 等

**示例**：

```ts
// ✅ 正确
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
import { join } from 'node:path';

// ❌ 错误
import { createServer } from 'http';
import { readFile } from 'fs/promises';
import { join } from 'path';
```

### 类型导入

**必须遵守**：
- 代码中使用的所有类型、接口、类都必须从相应包导入
- 确保所有使用的类型都已正确导入

**示例**：

```ts
// ✅ 正确
import type { FastifyRequest, FastifyReply } from 'fastify';
import { Request, Response, NextFunction } from 'express';

// ❌ 错误（缺少类型导入）
function handler(request, reply) {  // 缺少类型注解
  // ...
}
```

## 代码注释

### 注释原则

**规则**：
- 仅在必要时添加简洁注释，解释复杂逻辑
- 避免显而易见的注释
- 代码块内可添加路径、行号、上下文注释（见 Markdown 格式规范）

### 注释格式

**代码块标注**（推荐）：
- 在代码块内使用注释标注文件路径、行号、上下文
- 使用 `// 文件:` 标注文件路径
- 使用 `// 行号:` 标注行号范围
- 使用 `// 功能:` 标注功能说明

**示例**：

```ts
// 文件: src/utils/helper.ts
// 行号: 10-15
// 功能: 格式化日期

function formatDate(date: Date): string {
  return date.toISOString();
}
```

## 代码示例组织

### 示例结构

**推荐结构**：
1. 导入语句（使用 `node:` 前缀和 ESM 语法）
2. 类型定义（如需要）
3. 主要代码逻辑
4. 使用示例
5. 输出说明（注释形式）

**示例**：

```ts
// 文件: src/app.ts
// 功能: Express 应用示例

import express, { Request, Response } from 'express';

const app = express();

app.get('/', (req: Request, res: Response): void => {
  res.json({ message: 'Hello World' });
});

app.listen(3000, (): void => {
  console.log('Server running on port 3000');
});
```

### 完整示例类

**规则**：
- 复杂示例应使用完整的类结构
- 包含必要的属性和方法
- 提供使用示例

**示例**：

```ts
// 文件: src/services/calculator.ts
// 功能: 计算器服务类

class Calculator {
  public add(a: number, b: number): number {
    return a + b;
  }

  public multiply(a: number, b: number): number {
    return a * b;
  }
}

// 使用示例
const calc = new Calculator();
console.log(calc.add(5, 3));        // 8
console.log(calc.multiply(4, 7));  // 28
```

---

**最后更新**：2025-12-22
