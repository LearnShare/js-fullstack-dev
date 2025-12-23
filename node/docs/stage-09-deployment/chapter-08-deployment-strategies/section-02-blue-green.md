# 9.8.2 蓝绿部署

## 1. 概述

蓝绿部署是维护两个相同生产环境的部署策略，新版本部署到空闲环境，然后切换流量，实现零停机部署和快速回滚。

## 2. 工作原理

### 2.1 基本流程

```
1. 当前生产环境（蓝）运行旧版本
2. 在绿环境部署新版本
3. 测试绿环境
4. 切换流量到绿环境
5. 监控新版本
6. 保留蓝环境用于回滚
```

### 2.2 架构图

```
负载均衡器
    |
    ├─> 蓝环境（旧版本）
    └─> 绿环境（新版本）
```

## 3. 实现方式

### 3.1 Docker Compose

```yaml
# docker-compose.blue.yml
version: '3.8'
services:
  app-blue:
    image: my-app:v1.0
    ports:
      - "3001:3000"
    environment:
      - ENV=blue

# docker-compose.green.yml
version: '3.8'
services:
  app-green:
    image: my-app:v2.0
    ports:
      - "3002:3000"
    environment:
      - ENV=green
```

### 3.2 Nginx 配置

```nginx
# 初始配置：流量到蓝环境
upstream app {
    server localhost:3001;
}

server {
    listen 80;
    location / {
        proxy_pass http://app;
    }
}

# 切换后：流量到绿环境
upstream app {
    server localhost:3002;
}
```

### 3.3 自动化脚本

```ts
// deploy-blue-green.ts
import { exec } from 'node:child_process';
import { promisify } from 'node:util';

const execAsync = promisify(exec);

async function blueGreenDeploy(newVersion: string): Promise<void> {
  // 1. 部署新版本到绿环境
  console.log('Deploying to green environment...');
  await execAsync(`docker-compose -f docker-compose.green.yml up -d`);
  
  // 2. 健康检查
  console.log('Health checking green environment...');
  const healthy = await healthCheck('http://localhost:3002/health');
  if (!healthy) {
    throw new Error('Green environment health check failed');
  }
  
  // 3. 切换流量
  console.log('Switching traffic to green...');
  await switchTraffic('green');
  
  // 4. 监控新版本
  console.log('Monitoring new version...');
  await monitor(300); // 监控 5 分钟
  
  // 5. 停止蓝环境（可选）
  // await execAsync('docker-compose -f docker-compose.blue.yml down');
}

async function healthCheck(url: string): Promise<boolean> {
  try {
    const response = await fetch(url);
    return response.ok;
  } catch {
    return false;
  }
}

async function switchTraffic(environment: 'blue' | 'green'): Promise<void> {
  const port = environment === 'blue' ? 3001 : 3002;
  // 更新 Nginx 配置或负载均衡器配置
  await execAsync(`sed -i 's/server localhost:.*;/server localhost:${port};/' /etc/nginx/nginx.conf`);
  await execAsync('nginx -s reload');
}
```

## 4. Kubernetes 实现

### 4.1 服务配置

```yaml
# blue-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-blue
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
      version: blue
  template:
    metadata:
      labels:
        app: my-app
        version: blue
    spec:
      containers:
      - name: app
        image: my-app:v1.0
        ports:
        - containerPort: 3000

---
apiVersion: v1
kind: Service
metadata:
  name: app-service
spec:
  selector:
    app: my-app
    version: blue  # 切换到 green 时修改
  ports:
  - port: 80
    targetPort: 3000
```

## 5. 最佳实践

### 5.1 部署流程

- 自动化部署流程
- 实现健康检查
- 监控新版本
- 准备回滚方案

### 5.2 资源管理

- 合理管理资源
- 及时清理旧环境
- 监控资源使用
- 优化资源成本

## 6. 注意事项

- **资源需求**：需要双倍资源
- **数据一致性**：处理数据一致性问题
- **切换时机**：选择合适的切换时机
- **回滚准备**：保留旧环境用于回滚

## 7. 常见问题

### 7.1 如何处理数据库迁移？

使用数据库迁移工具、版本兼容、数据同步。

### 7.2 如何切换流量？

使用负载均衡器、Nginx、Kubernetes Service。

### 7.3 何时清理旧环境？

在确认新版本稳定后，保留一段时间再清理。

## 8. 实践任务

1. **实现蓝绿部署**：实现蓝绿部署流程
2. **自动化切换**：实现自动化流量切换
3. **健康检查**：实现健康检查
4. **监控验证**：监控和验证部署
5. **持续优化**：持续优化部署流程

---

**下一节**：[9.8.3 金丝雀部署](section-03-canary.md)
