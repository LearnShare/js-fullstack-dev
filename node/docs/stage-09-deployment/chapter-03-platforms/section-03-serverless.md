# 9.3.3 Serverless（AWS Lambda、Cloudflare Workers）

## 1. 概述

Serverless 是无服务器计算模式，开发者只需编写函数代码，平台负责执行和管理。AWS Lambda 和 Cloudflare Workers 是流行的 Serverless 平台。

## 2. AWS Lambda

### 2.1 特点

- **按需执行**：按请求计费
- **自动扩展**：自动处理并发
- **事件驱动**：支持多种触发器
- **集成服务**：与 AWS 服务集成

### 2.2 函数实现

```ts
// handler.ts
import { APIGatewayProxyEvent, APIGatewayProxyResult } from 'aws-lambda';

export const handler = async (
  event: APIGatewayProxyEvent
): Promise<APIGatewayProxyResult> => {
  const { httpMethod, path, body } = event;
  
  if (httpMethod === 'GET' && path === '/api/users') {
    const users = await getUsers();
    return {
      statusCode: 200,
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(users)
    };
  }
  
  return {
    statusCode: 404,
    body: JSON.stringify({ message: 'Not found' })
  };
};
```

### 2.3 部署配置

```yaml
# serverless.yml
service: my-app

provider:
  name: aws
  runtime: nodejs18.x
  region: us-east-1
  environment:
    DATABASE_URL: ${env:DATABASE_URL}

functions:
  api:
    handler: handler.handler
    events:
      - http:
          path: /{proxy+}
          method: ANY
```

### 2.4 部署命令

```bash
# 安装 Serverless Framework
npm install -g serverless

# 部署
serverless deploy

# 部署单个函数
serverless deploy function -f api
```

## 3. Cloudflare Workers

### 3.1 特点

- **边缘计算**：在全球边缘运行
- **低延迟**：接近用户的低延迟
- **按请求计费**：按请求数量计费
- **Web 标准**：支持 Web API

### 3.2 Worker 实现

```ts
// worker.ts
export default {
  async fetch(request: Request): Promise<Response> {
    const url = new URL(request.url);
    
    if (url.pathname === '/api/users') {
      const users = await getUsers();
      return new Response(JSON.stringify(users), {
        headers: { 'Content-Type': 'application/json' }
      });
    }
    
    return new Response('Not found', { status: 404 });
  }
};

async function getUsers(): Promise<any[]> {
  // 从数据库或 API 获取用户
  return [];
}
```

### 3.3 部署配置

```toml
# wrangler.toml
name = "my-app"
main = "worker.ts"
compatibility_date = "2024-01-01"

[env.production]
vars = { DATABASE_URL = "postgresql://..." }
```

### 3.4 部署命令

```bash
# 安装 Wrangler CLI
npm install -g wrangler

# 登录
wrangler login

# 部署
wrangler deploy

# 部署到生产环境
wrangler deploy --env production
```

## 4. Serverless 最佳实践

### 4.1 函数设计

- 保持函数简单
- 避免长时间运行
- 使用缓存
- 优化冷启动

### 4.2 性能优化

- 减少依赖大小
- 使用连接池
- 实现缓存
- 优化打包

## 5. 注意事项

- **冷启动**：注意冷启动延迟
- **超时限制**：注意执行时间限制
- **内存限制**：注意内存限制
- **成本控制**：注意请求成本

## 6. 常见问题

### 6.1 如何处理数据库连接？

使用连接池、外部数据库、Serverless 数据库。

### 6.2 如何优化冷启动？

减少依赖、使用预热、优化代码。

### 6.3 如何选择 Serverless 平台？

根据需求、价格、性能、功能选择。

## 7. 实践任务

1. **选择平台**：选择合适的 Serverless 平台
2. **实现函数**：实现 Serverless 函数
3. **配置部署**：配置部署设置
4. **性能优化**：优化函数性能
5. **持续优化**：持续优化函数

---

**下一节**：[9.3.4 IaaS（AWS EC2、DigitalOcean）](section-04-iaas.md)
