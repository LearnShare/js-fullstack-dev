# 4.9.4 环境变量管理

## 1. 概述

环境变量是配置管理的重要方式，通过环境变量可以安全地传递配置信息，特别是敏感信息。环境变量管理涉及环境变量的定义、加载、验证和使用。

## 2. 核心概念

### 2.1 环境变量的优势

- **安全性**：不在代码中暴露敏感信息
- **灵活性**：不同环境使用不同配置
- **标准化**：遵循 12-Factor App 原则
- **简单性**：易于设置和使用

### 2.2 环境变量的类型

- **系统环境变量**：操作系统级别的环境变量
- **应用环境变量**：应用级别的环境变量
- **.env 文件**：本地开发使用的环境变量文件

## 3. dotenv 使用

### 3.1 安装

```bash
npm install dotenv
```

### 3.2 基本使用

```ts
import { config } from 'dotenv';

// 加载 .env 文件
config();

const port = process.env.PORT ? parseInt(process.env.PORT) : 3000;
const dbUrl = process.env.DATABASE_URL || 'postgresql://localhost:5432/mydb';
```

### 3.3 .env 文件

```bash
# .env
PORT=3000
DATABASE_URL=postgresql://localhost:5432/mydb
REDIS_URL=redis://localhost:6379
JWT_SECRET=your-secret-key
NODE_ENV=development
```

### 3.4 多环境 .env 文件

```bash
# .env.development
PORT=3000
DATABASE_URL=postgresql://localhost:5432/mydb_dev

# .env.production
PORT=8080
DATABASE_URL=postgresql://prod-server:5432/mydb
```

```ts
import { config } from 'dotenv';

const env = process.env.NODE_ENV || 'development';
config({ path: `.env.${env}` });
```

## 4. 环境变量验证

### 4.1 基本验证

```ts
function getEnv(key: string, defaultValue?: string): string {
  const value = process.env[key];
  
  if (!value && defaultValue === undefined) {
    throw new Error(`Environment variable ${key} is required`);
  }
  
  return value || defaultValue!;
}

const port = parseInt(getEnv('PORT', '3000'));
const dbUrl = getEnv('DATABASE_URL');
```

### 4.2 类型验证

```ts
function getEnvNumber(key: string, defaultValue?: number): number {
  const value = process.env[key];
  
  if (!value && defaultValue === undefined) {
    throw new Error(`Environment variable ${key} is required`);
  }
  
  const numValue = value ? parseInt(value) : defaultValue!;
  
  if (isNaN(numValue)) {
    throw new Error(`Environment variable ${key} must be a number`);
  }
  
  return numValue;
}

function getEnvBoolean(key: string, defaultValue?: boolean): boolean {
  const value = process.env[key];
  
  if (!value && defaultValue === undefined) {
    throw new Error(`Environment variable ${key} is required`);
  }
  
  if (value) {
    return value.toLowerCase() === 'true';
  }
  
  return defaultValue!;
}
```

### 4.3 Schema 验证

```ts
import { z } from 'zod';

const envSchema = z.object({
  PORT: z.string().transform((val) => parseInt(val, 10)),
  DATABASE_URL: z.string().url(),
  JWT_SECRET: z.string().min(32),
  NODE_ENV: z.enum(['development', 'production', 'test']),
  REDIS_URL: z.string().url().optional()
});

type Env = z.infer<typeof envSchema>;

function validateEnv(): Env {
  try {
    return envSchema.parse(process.env);
  } catch (error) {
    if (error instanceof z.ZodError) {
      console.error('Environment variable validation failed:');
      error.errors.forEach((err) => {
        console.error(`  ${err.path.join('.')}: ${err.message}`);
      });
    }
    throw error;
  }
}

const env = validateEnv();
```

## 5. 环境变量管理

### 5.1 环境变量定义

```ts
// config/env.ts
interface EnvConfig {
  port: number;
  nodeEnv: string;
  databaseUrl: string;
  jwtSecret: string;
  redisUrl?: string;
}

function loadEnv(): EnvConfig {
  return {
    port: parseInt(process.env.PORT || '3000', 10),
    nodeEnv: process.env.NODE_ENV || 'development',
    databaseUrl: process.env.DATABASE_URL || '',
    jwtSecret: process.env.JWT_SECRET || '',
    redisUrl: process.env.REDIS_URL
  };
}

export const env = loadEnv();
```

### 5.2 环境变量使用

```ts
import { env } from './config/env';

const app = express();

app.listen(env.port, (): void => {
  console.log(`Server running on port ${env.port}`);
});
```

## 6. 敏感信息管理

### 6.1 密钥管理

```ts
// 使用环境变量存储密钥
const jwtSecret = process.env.JWT_SECRET;
if (!jwtSecret) {
  throw new Error('JWT_SECRET environment variable is required');
}
```

### 6.2 密钥轮换

```ts
// 支持多个密钥（用于密钥轮换）
const jwtSecrets = [
  process.env.JWT_SECRET_CURRENT,
  process.env.JWT_SECRET_PREVIOUS
].filter(Boolean) as string[];

if (jwtSecrets.length === 0) {
  throw new Error('At least one JWT_SECRET is required');
}
```

## 7. 最佳实践

### 7.1 .env 文件管理

- 不在版本控制中提交 .env 文件
- 提供 .env.example 文件
- 为不同环境创建不同的 .env 文件

### 7.2 环境变量命名

- 使用大写字母和下划线
- 使用有意义的名称
- 使用命名空间前缀

### 7.3 验证和文档

- 启动时验证必填环境变量
- 提供环境变量文档
- 使用类型定义

## 8. 注意事项

- **安全性**：不在代码中硬编码敏感信息
- **验证**：启动时验证必填环境变量
- **文档**：提供环境变量文档
- **默认值**：提供合理的默认值

## 9. 常见问题

### 9.1 如何处理 .env 文件？

使用 dotenv 加载 .env 文件，不在版本控制中提交。

### 9.2 如何验证环境变量？

使用 Zod 或其他验证库验证环境变量。

### 9.3 如何管理多环境配置？

为每个环境创建不同的 .env 文件或使用环境变量前缀。

## 10. 实践任务

1. **创建 .env 文件**：创建 .env 和 .env.example 文件
2. **实现环境变量加载**：使用 dotenv 加载环境变量
3. **实现环境变量验证**：实现环境变量验证机制
4. **实现类型安全**：实现类型安全的环境变量访问
5. **优化环境变量管理**：优化环境变量组织和管理

---

**下一章**：[4.10 中间件深入](../chapter-10-middleware/readme.md)
