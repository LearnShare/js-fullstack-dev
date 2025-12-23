# 4.9.3 convict

## 1. 概述

convict 是一个配置管理库，提供了配置验证、类型安全、默认值支持等功能。convict 通过 Schema 定义配置结构，自动验证配置的正确性，提供类型安全的配置访问。

## 2. 特性说明

- **配置验证**：基于 Schema 的配置验证
- **类型安全**：提供类型安全的配置访问
- **默认值**：支持默认值定义
- **环境变量**：支持环境变量覆盖
- **格式转换**：自动转换配置格式

## 3. 安装与初始化

### 3.1 安装

```bash
npm install convict
```

### 3.2 基本使用

```ts
import convict from 'convict';

const config = convict({
  env: {
    doc: 'The application environment',
    format: ['production', 'development', 'test'],
    default: 'development',
    env: 'NODE_ENV'
  },
  server: {
    port: {
      doc: 'The server port',
      format: 'port',
      default: 3000,
      env: 'PORT'
    },
    host: {
      doc: 'The server host',
      format: 'String',
      default: 'localhost',
      env: 'HOST'
    }
  }
});

config.validate({ allowed: 'strict' });

const port = config.get('server.port');
const host = config.get('server.host');
```

## 4. Schema 定义

### 4.1 基本 Schema

```ts
const config = convict({
  env: {
    doc: 'The application environment',
    format: ['production', 'development', 'test'],
    default: 'development',
    env: 'NODE_ENV'
  },
  port: {
    doc: 'The server port',
    format: 'port',
    default: 3000,
    env: 'PORT'
  }
});
```

### 4.2 嵌套 Schema

```ts
const config = convict({
  server: {
    port: {
      doc: 'The server port',
      format: 'port',
      default: 3000,
      env: 'PORT'
    },
    host: {
      doc: 'The server host',
      format: 'String',
      default: 'localhost',
      env: 'HOST'
    }
  },
  database: {
    url: {
      doc: 'The database URL',
      format: 'String',
      default: 'postgresql://localhost:5432/mydb',
      env: 'DATABASE_URL',
      sensitive: true
    },
    pool: {
      min: {
        doc: 'Minimum pool size',
        format: 'int',
        default: 2,
        env: 'DB_POOL_MIN'
      },
      max: {
        doc: 'Maximum pool size',
        format: 'int',
        default: 10,
        env: 'DB_POOL_MAX'
      }
    }
  }
});
```

## 5. 格式验证

### 5.1 内置格式

```ts
const config = convict({
  port: {
    format: 'port', // 端口号
    default: 3000
  },
  url: {
    format: 'url', // URL
    default: 'http://localhost:3000'
  },
  email: {
    format: 'email', // 邮箱
    default: 'admin@example.com'
  },
  int: {
    format: 'int', // 整数
    default: 100
  },
  nat: {
    format: 'nat', // 自然数
    default: 1
  }
});
```

### 5.2 自定义格式

```ts
import convict from 'convict';

convict.addFormat({
  name: 'positive-number',
  validate: (value: unknown): void => {
    if (typeof value !== 'number' || value <= 0) {
      throw new Error('Must be a positive number');
    }
  },
  coerce: (value: unknown): number => {
    return typeof value === 'string' ? parseFloat(value) : value as number;
  }
});

const config = convict({
  timeout: {
    format: 'positive-number',
    default: 5000
  }
});
```

## 6. 配置加载

### 6.1 从文件加载

```ts
const config = convict({
  // Schema 定义
});

// 加载配置文件
config.loadFile('./config/production.json');
config.validate({ allowed: 'strict' });
```

### 6.2 从对象加载

```ts
const config = convict({
  // Schema 定义
});

// 从对象加载
config.load({
  server: {
    port: 8080
  }
});

config.validate({ allowed: 'strict' });
```

## 7. 配置访问

### 7.1 基本访问

```ts
// 获取配置值
const port = config.get('server.port');
const host = config.get('server.host');

// 获取嵌套配置
const minPool = config.get('database.pool.min');
```

### 7.2 类型安全访问

```ts
// 使用类型断言
const port = config.get('server.port') as number;
const dbUrl = config.get('database.url') as string;
```

## 8. 配置验证

### 8.1 严格验证

```ts
// 严格验证：不允许未定义的配置
config.validate({ allowed: 'strict' });
```

### 8.2 宽松验证

```ts
// 宽松验证：允许未定义的配置
config.validate({ allowed: 'warn' });
```

### 8.3 自定义验证

```ts
config.validate({
  allowed: 'strict',
  output: (warning: string): void => {
    console.warn('Config warning:', warning);
  }
});
```

## 9. 最佳实践

### 9.1 Schema 定义

- 提供清晰的文档说明
- 使用合适的格式验证
- 提供合理的默认值

### 9.2 配置组织

- 按功能模块组织配置
- 使用嵌套结构
- 标记敏感配置

### 9.3 验证策略

- 启动时严格验证
- 提供清晰的错误信息
- 处理验证错误

## 10. 注意事项

- **格式验证**：使用合适的格式验证
- **类型安全**：使用类型断言确保类型安全
- **敏感信息**：标记敏感配置
- **验证时机**：在应用启动时验证配置

## 11. 常见问题

### 11.1 如何定义自定义格式？

使用 `convict.addFormat()` 添加自定义格式。

### 11.2 如何实现配置验证？

使用 `config.validate()` 方法验证配置。

### 11.3 如何标记敏感配置？

在 Schema 定义中使用 `sensitive: true`。

## 12. 实践任务

1. **定义 Schema**：定义完整的配置 Schema
2. **实现配置验证**：实现配置验证机制
3. **实现自定义格式**：实现自定义格式验证
4. **实现配置加载**：实现从文件和对象加载配置
5. **优化配置管理**：优化配置组织和管理

---

**下一节**：[4.9.4 环境变量管理](section-04-env-vars.md)
