# 9.2.2 GitHub Actions

## 1. 概述

GitHub Actions 是 GitHub 提供的 CI/CD 平台，可以直接在 GitHub 仓库中配置自动化工作流。GitHub Actions 提供了丰富的 Actions 市场和灵活的配置方式。

## 2. 基本配置

### 2.1 工作流文件

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run tests
        run: npm test
      
      - name: Run linter
        run: npm run lint
```

### 2.2 工作流触发

```yaml
on:
  # Push 事件
  push:
    branches: [main]
    paths:
      - 'src/**'
      - 'package.json'
  
  # Pull Request 事件
  pull_request:
    branches: [main]
  
  # 定时触发
  schedule:
    - cron: '0 0 * * *'
  
  # 手动触发
  workflow_dispatch:
    inputs:
      environment:
        description: 'Deployment environment'
        required: true
        type: choice
        options:
          - staging
          - production
```

## 3. 构建和测试

### 3.1 Node.js 应用

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    
    strategy:
      matrix:
        node-version: [16, 18, 20]
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Use Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v3
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'
      
      - run: npm ci
      - run: npm test
      - run: npm run build
```

### 3.2 Docker 构建

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v2
      
      - name: Login to Docker Hub
        uses: docker/login-action@v2
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}
      
      - name: Build and push
        uses: docker/build-push-action@v4
        with:
          context: .
          push: true
          tags: user/app:latest
```

## 4. 部署

### 4.1 部署到服务器

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    needs: test
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Deploy to server
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.HOST }}
          username: ${{ secrets.USERNAME }}
          key: ${{ secrets.SSH_KEY }}
          script: |
            cd /app
            git pull
            npm ci --production
            pm2 restart app
```

### 4.2 部署到云平台

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    needs: build
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Deploy to Vercel
        uses: amondnet/vercel-action@v20
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.ORG_ID }}
          vercel-project-id: ${{ secrets.PROJECT_ID }}
```

## 5. 高级特性

### 5.1 环境变量和密钥

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    env:
      NODE_ENV: production
      DATABASE_URL: ${{ secrets.DATABASE_URL }}
    
    steps:
      - name: Use secrets
        run: |
          echo "Using secret: ${{ secrets.API_KEY }}"
```

### 5.2 条件执行

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
      - name: Deploy
        if: github.event_name == 'push'
        run: echo "Deploying..."
```

### 5.3 并行执行

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm test
  
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm run lint
  
  build:
    needs: [test, lint]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm run build
```

## 6. 最佳实践

### 6.1 工作流设计

- 快速反馈
- 并行执行
- 使用缓存
- 失败快速修复

### 6.2 安全实践

- 使用 Secrets 管理密钥
- 最小权限原则
- 定期更新 Actions
- 审查第三方 Actions

## 7. 注意事项

- **安全性**：保护 Secrets
- **性能**：优化工作流性能
- **成本**：控制运行时间
- **维护**：定期更新 Actions

## 8. 常见问题

### 8.1 如何管理 Secrets？

使用 GitHub Secrets，按环境分离。

### 8.2 如何优化工作流性能？

使用缓存、并行执行、优化步骤。

### 8.3 如何处理部署失败？

实现自动回滚、健康检查、通知机制。

## 9. 实践任务

1. **配置工作流**：配置 GitHub Actions 工作流
2. **实现 CI**：实现持续集成
3. **实现 CD**：实现持续部署
4. **安全加固**：实现安全最佳实践
5. **持续优化**：持续优化工作流

---

**下一节**：[9.2.3 GitLab CI](section-03-gitlab-ci.md)
