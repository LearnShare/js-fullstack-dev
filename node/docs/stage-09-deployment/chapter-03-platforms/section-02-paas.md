# 9.3.2 PaaS（Vercel、Railway、Render）

## 1. 概述

PaaS（Platform as a Service）平台提供了简化的部署体验，开发者只需关注应用代码，平台负责基础设施管理。Vercel、Railway、Render 是流行的 Node.js PaaS 平台。

## 2. Vercel

### 2.1 特点

- **零配置部署**：自动检测框架
- **边缘网络**：全球 CDN
- **Serverless Functions**：支持 Serverless
- **自动 HTTPS**：自动配置 SSL

### 2.2 部署配置

```json
// vercel.json
{
  "version": 2,
  "builds": [
    {
      "src": "package.json",
      "use": "@vercel/node"
    }
  ],
  "routes": [
    {
      "src": "/api/(.*)",
      "dest": "/api/$1"
    },
    {
      "src": "/(.*)",
      "dest": "/$1"
    }
  ],
  "env": {
    "DATABASE_URL": "@database-url"
  }
}
```

### 2.3 部署命令

```bash
# 安装 Vercel CLI
npm i -g vercel

# 部署
vercel

# 生产部署
vercel --prod
```

## 3. Railway

### 3.1 特点

- **简单部署**：Git 推送即部署
- **自动构建**：自动检测构建命令
- **环境变量**：简单管理环境变量
- **数据库集成**：内置数据库服务

### 3.2 部署配置

```json
// railway.json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS",
    "buildCommand": "npm run build"
  },
  "deploy": {
    "startCommand": "npm start",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

### 3.3 环境变量

```bash
# Railway 自动检测环境变量
# 在 Railway 控制台配置
DATABASE_URL=postgresql://...
REDIS_URL=redis://...
```

## 4. Render

### 4.1 特点

- **自动部署**：Git 推送即部署
- **Docker 支持**：支持 Docker 部署
- **持久磁盘**：支持持久存储
- **自动 HTTPS**：自动配置 SSL

### 4.2 部署配置

```yaml
# render.yaml
services:
  - type: web
    name: my-app
    env: node
    buildCommand: npm install && npm run build
    startCommand: npm start
    envVars:
      - key: NODE_ENV
        value: production
      - key: DATABASE_URL
        fromDatabase:
          name: my-db
          property: connectionString
```

## 5. 部署最佳实践

### 5.1 配置优化

- 使用环境变量
- 配置构建缓存
- 优化构建时间
- 设置健康检查

### 5.2 性能优化

- 使用 CDN
- 优化静态资源
- 启用压缩
- 使用缓存

## 6. 注意事项

- **环境变量**：安全管理环境变量
- **构建优化**：优化构建时间
- **成本控制**：注意平台成本
- **监控告警**：配置监控告警

## 7. 常见问题

### 7.1 如何选择 PaaS 平台？

根据需求、价格、功能、团队经验选择。

### 7.2 如何处理数据库连接？

使用平台提供的数据库服务或外部数据库。

### 7.3 如何优化部署速度？

使用构建缓存、优化依赖、并行构建。

## 8. 实践任务

1. **选择平台**：选择合适的 PaaS 平台
2. **配置部署**：配置部署设置
3. **部署应用**：部署应用到平台
4. **监控管理**：监控和管理应用
5. **持续优化**：持续优化部署配置

---

**下一节**：[9.3.3 Serverless（AWS Lambda、Cloudflare Workers）](section-03-serverless.md)
