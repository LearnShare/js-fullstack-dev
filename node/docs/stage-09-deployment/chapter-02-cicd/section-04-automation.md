# 9.2.4 自动化测试与部署

## 1. 概述

自动化测试与部署是 CI/CD 的核心，通过自动化测试保证代码质量，通过自动化部署加快交付速度。本章介绍如何实现自动化测试和部署流程。

## 2. 自动化测试

### 2.1 测试流程

```yaml
# GitHub Actions
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run unit tests
        run: npm run test:unit
      
      - name: Run integration tests
        run: npm run test:integration
      
      - name: Run E2E tests
        run: npm run test:e2e
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage/coverage-final.json
```

### 2.2 测试矩阵

```yaml
test:
  strategy:
    matrix:
      node-version: [16, 18, 20]
      os: [ubuntu-latest, windows-latest, macos-latest]
  runs-on: ${{ matrix.os }}
  steps:
    - uses: actions/setup-node@v3
      with:
        node-version: ${{ matrix.node-version }}
    - run: npm test
```

## 3. 自动化构建

### 3.1 构建流程

```yaml
build:
  needs: test
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v3
    - uses: actions/setup-node@v3
    
    - name: Build application
      run: npm run build
    
    - name: Build Docker image
      run: |
        docker build -t my-app:${{ github.sha }} .
        docker tag my-app:${{ github.sha }} my-app:latest
    
    - name: Push to registry
      run: |
        echo ${{ secrets.DOCKER_PASSWORD }} | docker login -u ${{ secrets.DOCKER_USERNAME }} --password-stdin
        docker push my-app:${{ github.sha }}
        docker push my-app:latest
```

## 4. 自动化部署

### 4.1 部署脚本

```ts
// deploy.ts
import { exec } from 'node:child_process';
import { promisify } from 'node:util';

const execAsync = promisify(exec);

interface DeployConfig {
  environment: 'staging' | 'production';
  version: string;
}

async function deploy(config: DeployConfig): Promise<void> {
  const { environment, version } = config;
  
  console.log(`Deploying ${version} to ${environment}`);
  
  // 1. 拉取最新代码
  await execAsync('git pull origin main');
  
  // 2. 安装依赖
  await execAsync('npm ci --production');
  
  // 3. 运行数据库迁移
  await execAsync('npm run migrate');
  
  // 4. 重启应用
  await execAsync('pm2 restart app');
  
  // 5. 健康检查
  await healthCheck(environment);
  
  console.log('Deployment completed');
}

async function healthCheck(environment: string): Promise<void> {
  const url = environment === 'production' 
    ? 'https://api.example.com/health'
    : 'https://staging-api.example.com/health';
  
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error('Health check failed');
  }
}
```

### 4.2 部署工作流

```yaml
deploy:
  needs: build
  runs-on: ubuntu-latest
  environment: production
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
          git pull origin main
          npm ci --production
          npm run migrate
          pm2 restart app
    
    - name: Health check
      run: |
        sleep 10
        curl -f https://api.example.com/health || exit 1
```

## 5. 回滚机制

### 5.1 自动回滚

```ts
async function rollback(environment: string): Promise<void> {
  console.log(`Rolling back ${environment}`);
  
  // 1. 获取上一个版本
  const previousVersion = await getPreviousVersion(environment);
  
  // 2. 部署上一个版本
  await deploy({ environment, version: previousVersion });
  
  // 3. 验证回滚
  await healthCheck(environment);
  
  console.log('Rollback completed');
}
```

### 5.2 回滚工作流

```yaml
rollback:
  runs-on: ubuntu-latest
  environment: production
  steps:
    - name: Rollback
      run: |
        # 回滚逻辑
        pm2 restart app --update-env
```

## 6. 通知机制

### 6.1 通知实现

```ts
async function sendNotification(
  type: 'success' | 'failure',
  message: string
): Promise<void> {
  // 发送到 Slack
  await fetch(process.env.SLACK_WEBHOOK_URL!, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      text: `Deployment ${type}: ${message}`
    })
  });
  
  // 发送邮件
  // ...
}
```

## 7. 最佳实践

### 7.1 自动化设计

- 快速反馈
- 自动化所有步骤
- 实现回滚机制
- 监控部署状态

### 7.2 安全实践

- 保护密钥
- 最小权限
- 审计日志
- 定期审查

## 8. 注意事项

- **测试覆盖**：保证测试覆盖率
- **部署安全**：注意部署安全
- **回滚机制**：实现回滚机制
- **监控告警**：监控部署状态

## 9. 常见问题

### 9.1 如何实现零停机部署？

使用蓝绿部署、金丝雀部署、滚动更新。

### 9.2 如何处理部署失败？

实现自动回滚、健康检查、通知机制。

### 9.3 如何优化部署速度？

使用缓存、并行执行、优化步骤。

## 10. 实践任务

1. **自动化测试**：实现自动化测试流程
2. **自动化构建**：实现自动化构建流程
3. **自动化部署**：实现自动化部署流程
4. **回滚机制**：实现回滚机制
5. **持续优化**：持续优化自动化流程

---

**下一章**：[9.3 部署平台](../chapter-03-platforms/readme.md)
