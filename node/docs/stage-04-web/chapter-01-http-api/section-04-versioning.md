# 4.1.4 API 版本控制

## 1. 概述

API 版本控制是管理 API 演进的重要机制，允许在不破坏现有客户端的情况下引入新功能和修改。合理的版本控制策略可以确保 API 的稳定性和可维护性。本节介绍 API 版本控制的策略、实现方法和最佳实践。

## 2. 版本控制的必要性

### 2.1 为什么需要版本控制

- **向后兼容**：新版本可能引入破坏性变更
- **渐进式迁移**：给客户端时间迁移到新版本
- **多版本共存**：同时支持多个 API 版本
- **清晰演进**：明确 API 的演进路径

### 2.2 何时需要版本控制

- **破坏性变更**：修改现有行为或删除功能
- **数据结构变更**：修改请求或响应格式
- **行为变更**：修改业务逻辑或验证规则
- **安全更新**：修复安全漏洞

## 3. 版本控制策略

### 3.1 URL 路径版本控制

**优点**：

- 清晰明确，易于理解
- 支持多版本共存
- 易于路由和代理配置

**缺点**：

- URL 中包含版本号，不够优雅
- 需要修改 URL 才能切换版本

**示例**：

```
/api/v1/users
/api/v2/users
```

**实现示例**：

```ts
import { createServer, IncomingMessage, ServerResponse } from 'node:http';
import { parse } from 'node:url';

const server = createServer((req: IncomingMessage, res: ServerResponse) => {
  const { pathname } = parse(req.url || '');
  res.setHeader('Content-Type', 'application/json');

  // 提取版本号
  const versionMatch = pathname?.match(/^\/api\/v(\d+)\//);
  if (!versionMatch) {
    res.statusCode = 400;
    res.end(JSON.stringify({ error: { message: 'Invalid API version' } }));
    return;
  }

  const version = parseInt(versionMatch[1]);
  const path = pathname?.replace(`/api/v${version}`, '') || '';

  // 根据版本路由
  if (version === 1) {
    handleV1(path, req, res);
  } else if (version === 2) {
    handleV2(path, req, res);
  } else {
    res.statusCode = 400;
    res.end(JSON.stringify({ error: { message: 'Unsupported API version' } }));
  }
});

function handleV1(path: string, req: IncomingMessage, res: ServerResponse) {
  if (path === '/users') {
    res.statusCode = 200;
    res.end(JSON.stringify({ data: [], version: 'v1' }));
  }
}

function handleV2(path: string, req: IncomingMessage, res: ServerResponse) {
  if (path === '/users') {
    res.statusCode = 200;
    res.end(JSON.stringify({ data: [], meta: { version: 'v2' } }));
  }
}

server.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});
```

### 3.2 请求头版本控制

**优点**：

- URL 保持简洁
- 不影响 URL 结构
- 支持内容协商

**缺点**：

- 不够直观
- 需要客户端明确指定版本

**示例**：

```
Accept: application/vnd.api+json;version=1
Accept: application/vnd.api+json;version=2
```

**实现示例**：

```ts
import { createServer, IncomingMessage, ServerResponse } from 'node:http';
import { parse } from 'node:url';

const server = createServer((req: IncomingMessage, res: ServerResponse) => {
  const { pathname } = parse(req.url || '');
  res.setHeader('Content-Type', 'application/json');

  // 从 Accept 头部提取版本
  const acceptHeader = req.headers.accept || '';
  const versionMatch = acceptHeader.match(/version=(\d+)/);
  const version = versionMatch ? parseInt(versionMatch[1]) : 1;

  // 根据版本路由
  if (version === 1) {
    handleV1(pathname || '', req, res);
  } else if (version === 2) {
    handleV2(pathname || '', req, res);
  } else {
    res.statusCode = 400;
    res.end(JSON.stringify({ error: { message: 'Unsupported API version' } }));
  }
});

function handleV1(path: string, req: IncomingMessage, res: ServerResponse) {
  if (path === '/api/users') {
    res.statusCode = 200;
    res.end(JSON.stringify({ data: [], version: 'v1' }));
  }
}

function handleV2(path: string, req: IncomingMessage, res: ServerResponse) {
  if (path === '/api/users') {
    res.statusCode = 200;
    res.end(JSON.stringify({ data: [], meta: { version: 'v2' } }));
  }
}

server.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});
```

### 3.3 查询参数版本控制（不推荐）

**优点**：

- 简单易用
- 不需要修改 URL 路径

**缺点**：

- 不够标准
- 容易与业务查询参数混淆
- 不利于缓存

**示例**：

```
/api/users?version=1
/api/users?version=2
```

## 4. 版本号规范

### 4.1 语义化版本控制

使用语义化版本号（Semantic Versioning）：

- **主版本号（Major）**：破坏性变更
- **次版本号（Minor）**：新功能，向后兼容
- **修订版本号（Patch）**：错误修复，向后兼容

**示例**：

```
v1.0.0  # 初始版本
v1.1.0  # 添加新功能
v1.1.1  # 修复错误
v2.0.0  # 破坏性变更
```

### 4.2 简化版本号

对于 API 版本控制，通常只使用主版本号：

```
v1
v2
v3
```

## 5. 版本迁移策略

### 5.1 弃用策略

- **通知期**：提前通知客户端即将弃用
- **过渡期**：同时支持新旧版本
- **弃用期**：标记为已弃用，但继续支持
- **移除期**：完全移除旧版本

**示例**：

```ts
interface ApiVersion {
  version: string;
  status: 'current' | 'deprecated' | 'sunset';
  sunsetDate?: string;
  migrationGuide?: string;
}

const apiVersions: ApiVersion[] = [
  {
    version: 'v1',
    status: 'deprecated',
    sunsetDate: '2025-12-31',
    migrationGuide: 'https://api.example.com/docs/migration/v1-to-v2'
  },
  {
    version: 'v2',
    status: 'current'
  }
];
```

### 5.2 版本兼容性

- **向后兼容**：新版本兼容旧版本客户端
- **向前兼容**：旧版本服务器兼容新版本客户端（通常不支持）
- **渐进式迁移**：逐步迁移到新版本

## 6. 代码示例

### 6.1 版本控制中间件

```ts
import { IncomingMessage, ServerResponse } from 'node:http';

interface VersionConfig {
  defaultVersion: string;
  supportedVersions: string[];
}

export function versionMiddleware(config: VersionConfig) {
  return (req: IncomingMessage, res: ServerResponse, next: () => void) => {
    // 从 URL 路径提取版本
    const pathMatch = req.url?.match(/^\/api\/v(\d+)\//);
    let version = config.defaultVersion;

    if (pathMatch) {
      version = `v${pathMatch[1]}`;
    } else {
      // 从 Accept 头部提取版本
      const acceptHeader = req.headers.accept || '';
      const versionMatch = acceptHeader.match(/version=(\d+)/);
      if (versionMatch) {
        version = `v${versionMatch[1]}`;
      }
    }

    // 检查版本是否支持
    if (!config.supportedVersions.includes(version)) {
      res.statusCode = 400;
      res.setHeader('Content-Type', 'application/json');
      res.end(JSON.stringify({
        error: {
          message: 'Unsupported API version',
          supportedVersions: config.supportedVersions
        }
      }));
      return;
    }

    // 将版本信息附加到请求对象
    (req as any).apiVersion = version;
    next();
  };
}

// 使用示例
const middleware = versionMiddleware({
  defaultVersion: 'v1',
  supportedVersions: ['v1', 'v2']
});
```

### 6.2 版本路由处理

```ts
import { IncomingMessage, ServerResponse } from 'node:http';
import { parse } from 'node:url';

type VersionHandler = (path: string, req: IncomingMessage, res: ServerResponse) => void;

interface VersionRouter {
  [version: string]: VersionHandler;
}

const versionRouter: VersionRouter = {
  v1: (path: string, req: IncomingMessage, res: ServerResponse) => {
    if (path === '/users') {
      res.statusCode = 200;
      res.setHeader('Content-Type', 'application/json');
      res.end(JSON.stringify({
        data: [],
        version: 'v1'
      }));
    }
  },
  v2: (path: string, req: IncomingMessage, res: ServerResponse) => {
    if (path === '/users') {
      res.statusCode = 200;
      res.setHeader('Content-Type', 'application/json');
      res.end(JSON.stringify({
        data: [],
        meta: { version: 'v2' }
      }));
    }
  }
};

export function routeByVersion(
  version: string,
  path: string,
  req: IncomingMessage,
  res: ServerResponse
) {
  const handler = versionRouter[version];
  if (handler) {
    handler(path, req, res);
  } else {
    res.statusCode = 400;
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify({
      error: { message: 'Unsupported API version' }
    }));
  }
}
```

## 7. 最佳实践

### 7.1 版本控制原则

- **明确版本策略**：选择一种版本控制策略并保持一致
- **文档化**：为每个版本维护文档
- **向后兼容**：尽量保持向后兼容
- **弃用计划**：明确弃用旧版本的策略和时间表

### 7.2 版本选择建议

- **URL 路径版本控制**：最常用，推荐用于大多数场景
- **请求头版本控制**：适用于需要保持 URL 简洁的场景
- **查询参数版本控制**：不推荐，除非有特殊需求

### 7.3 版本管理建议

- **语义化版本**：使用语义化版本号
- **版本文档**：为每个版本维护独立的文档
- **迁移指南**：提供版本迁移指南
- **测试覆盖**：为每个版本编写测试用例

## 8. 注意事项

- **版本数量**：避免同时维护过多版本
- **弃用策略**：明确弃用旧版本的策略和时间表
- **兼容性测试**：确保新版本不破坏现有客户端
- **文档同步**：保持版本文档的及时更新

## 9. 常见问题

### 9.1 如何处理默认版本？

如果没有指定版本，使用最新稳定版本或默认版本：

```ts
const defaultVersion = 'v2';
const version = extractVersion(req) || defaultVersion;
```

### 9.2 如何通知客户端版本变更？

使用响应头通知客户端：

```ts
res.setHeader('X-API-Version', 'v2');
res.setHeader('X-API-Deprecated-Versions', 'v1');
res.setHeader('X-API-Sunset-Date', '2025-12-31');
```

### 9.3 如何处理版本弃用？

返回警告信息，但继续支持：

```ts
if (version === 'v1') {
  res.setHeader('X-API-Deprecated', 'true');
  res.setHeader('X-API-Sunset-Date', '2025-12-31');
  res.setHeader('X-API-Migration-Guide', 'https://api.example.com/docs/migration/v1-to-v2');
}
```

---

**下一节**：[4.1.5 API 文档（OpenAPI/Swagger）](section-05-documentation.md)
