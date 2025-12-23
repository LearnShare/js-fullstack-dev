# 4.9.2 node-config

## 1. 概述

node-config 是一个强大的 Node.js 配置管理库，支持多环境配置、配置文件合并、环境变量覆盖等功能。node-config 提供了灵活的配置管理方式，适合复杂的应用场景。

## 2. 特性说明

- **多环境支持**：支持开发、测试、生产等环境
- **配置合并**：支持配置文件合并和覆盖
- **环境变量覆盖**：支持环境变量覆盖配置
- **类型安全**：支持 TypeScript 类型定义

## 3. 安装与初始化

### 3.1 安装

```bash
npm install config
npm install @types/config -D
```

### 3.2 项目结构

```
config/
├── default.json       # 默认配置
├── development.json   # 开发环境配置
├── production.json    # 生产环境配置
└── test.json          # 测试环境配置
```

### 3.3 基本使用

```ts
import config from 'config';

const port = config.get<number>('server.port');
const dbUrl = config.get<string>('database.url');
```

## 4. 配置文件

### 4.1 默认配置

```json
// config/default.json
{
  "server": {
    "port": 3000,
    "host": "localhost"
  },
  "database": {
    "url": "postgresql://localhost:5432/mydb",
    "pool": {
      "min": 2,
      "max": 10
    }
  },
  "redis": {
    "host": "localhost",
    "port": 6379
  }
}
```

### 4.2 环境配置

```json
// config/development.json
{
  "server": {
    "port": 3000,
    "host": "localhost"
  },
  "database": {
    "url": "postgresql://localhost:5432/mydb_dev"
  },
  "logLevel": "debug"
}
```

```json
// config/production.json
{
  "server": {
    "port": 8080,
    "host": "0.0.0.0"
  },
  "database": {
    "url": "postgresql://prod-server:5432/mydb"
  },
  "logLevel": "info"
}
```

## 5. 配置访问

### 5.1 基本访问

```ts
import config from 'config';

// 获取配置值
const port = config.get<number>('server.port');
const host = config.get<string>('server.host');

// 检查配置是否存在
if (config.has('database.url')) {
  const dbUrl = config.get<string>('database.url');
}
```

### 5.2 嵌套配置

```ts
// 访问嵌套配置
const dbUrl = config.get<string>('database.url');
const minPool = config.get<number>('database.pool.min');
const maxPool = config.get<number>('database.pool.max');
```

### 5.3 默认值

```ts
// 使用默认值
const port = config.get<number>('server.port', 3000);
const timeout = config.get<number>('server.timeout', 5000);
```

## 6. 环境变量覆盖

### 6.1 环境变量命名

```bash
# 使用双下划线表示嵌套
export SERVER__PORT=8080
export DATABASE__URL=postgresql://prod:5432/mydb
export DATABASE__POOL__MIN=5
```

### 6.2 环境变量使用

```ts
// 环境变量会自动覆盖配置文件中的值
const port = config.get<number>('server.port'); // 从环境变量获取
const dbUrl = config.get<string>('database.url'); // 从环境变量获取
```

## 7. 自定义配置源

### 7.1 环境变量配置源

```ts
// config/custom-environment-variables.json
{
  "server": {
    "port": "PORT",
    "host": "HOST"
  },
  "database": {
    "url": "DATABASE_URL"
  }
}
```

### 7.2 命令行配置源

```ts
// 使用命令行参数
// NODE_CONFIG='{"server":{"port":8080}}' node app.js
```

## 8. 配置验证

### 8.1 启动时验证

```ts
import config from 'config';

function validateConfig(): void {
  const required = ['server.port', 'database.url'];
  
  for (const key of required) {
    if (!config.has(key)) {
      throw new Error(`Missing required config: ${key}`);
    }
  }
}

validateConfig();
```

### 8.2 类型验证

```ts
function getConfig<T>(key: string, defaultValue?: T): T {
  if (!config.has(key) && defaultValue === undefined) {
    throw new Error(`Config key ${key} is required`);
  }
  return config.get<T>(key, defaultValue);
}

const port = getConfig<number>('server.port');
const dbUrl = getConfig<string>('database.url');
```

## 9. 最佳实践

### 9.1 配置组织

- 按功能模块组织配置
- 使用嵌套结构
- 提供清晰的配置文档

### 9.2 环境管理

- 为每个环境创建配置文件
- 使用环境变量覆盖敏感配置
- 提供合理的默认值

### 9.3 安全性

- 不在配置文件中存储敏感信息
- 使用环境变量存储敏感配置
- 实现配置验证

## 10. 注意事项

- **环境变量**：注意环境变量的命名规则
- **配置合并**：理解配置合并的优先级
- **类型安全**：使用 TypeScript 类型定义
- **验证**：实现配置验证机制

## 11. 常见问题

### 11.1 如何设置环境？

使用 NODE_ENV 环境变量：`NODE_ENV=production node app.js`

### 11.2 环境变量如何覆盖配置？

使用双下划线表示嵌套：`SERVER__PORT=8080`

### 11.3 如何实现配置验证？

在应用启动时验证必填配置，使用类型检查。

## 12. 实践任务

1. **创建配置文件**：创建多环境配置文件
2. **实现配置访问**：实现配置访问和类型安全
3. **实现环境变量覆盖**：使用环境变量覆盖配置
4. **实现配置验证**：实现配置验证机制
5. **优化配置管理**：优化配置组织和管理

---

**下一节**：[4.9.3 convict](section-03-convict.md)
