# 9.8.4 滚动更新

## 1. 概述

滚动更新是逐步替换旧实例的部署策略，一次替换一个或几个实例，保持服务运行，逐步完成更新。滚动更新是 Kubernetes 的默认部署策略。

## 2. 工作原理

### 2.1 基本流程

```
1. 创建新版本实例 1
2. 等待新实例就绪
3. 停止旧版本实例 1
4. 创建新版本实例 2
5. 等待新实例就绪
6. 停止旧版本实例 2
7. 重复直到所有实例更新
```

### 2.2 实例替换

```
初始状态：3 个旧版本实例
    |
步骤 1：2 个旧版本 + 1 个新版本
    |
步骤 2：1 个旧版本 + 2 个新版本
    |
步骤 3：3 个新版本
```

## 3. Kubernetes 实现

### 3.1 Deployment 配置

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1        # 最多额外实例数
      maxUnavailable: 0  # 最多不可用实例数
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: app
        image: my-app:v2.0
        ports:
        - containerPort: 3000
        readinessProbe:
          httpGet:
            path: /health
            port: 3000
          initialDelaySeconds: 10
          periodSeconds: 5
```

### 3.2 滚动更新命令

```bash
# 更新镜像
kubectl set image deployment/my-app app=my-app:v2.0

# 查看更新状态
kubectl rollout status deployment/my-app

# 暂停更新
kubectl rollout pause deployment/my-app

# 恢复更新
kubectl rollout resume deployment/my-app

# 回滚
kubectl rollout undo deployment/my-app
```

## 4. Docker Swarm 实现

### 4.1 服务更新

```bash
# 更新服务
docker service update --image my-app:v2.0 my-app

# 滚动更新配置
docker service update \
  --update-parallelism 1 \
  --update-delay 10s \
  --update-failure-action rollback \
  my-app
```

## 5. 自定义实现

### 5.1 滚动更新脚本

```ts
// rolling-update.ts
interface RollingUpdateConfig {
  totalInstances: number;
  batchSize: number;
  healthCheckUrl: string;
  waitTime: number;
}

async function rollingUpdate(config: RollingUpdateConfig): Promise<void> {
  const batches = Math.ceil(config.totalInstances / config.batchSize);
  
  for (let i = 0; i < batches; i++) {
    const start = i * config.batchSize;
    const end = Math.min(start + config.batchSize, config.totalInstances);
    
    console.log(`Updating instances ${start} to ${end - 1}...`);
    
    // 1. 启动新实例
    await startNewInstances(start, end);
    
    // 2. 等待健康检查
    await waitForHealthCheck(start, end, config.healthCheckUrl);
    
    // 3. 停止旧实例
    await stopOldInstances(start, end);
    
    // 4. 等待一段时间
    await sleep(config.waitTime);
  }
  
  console.log('Rolling update completed');
}

async function startNewInstances(start: number, end: number): Promise<void> {
  // 启动新版本实例
  for (let i = start; i < end; i++) {
    await execAsync(`docker run -d --name app-new-${i} my-app:v2.0`);
  }
}

async function waitForHealthCheck(start: number, end: number, url: string): Promise<void> {
  // 等待所有新实例健康
  for (let i = start; i < end; i++) {
    let healthy = false;
    while (!healthy) {
      try {
        const response = await fetch(`http://app-new-${i}:3000${url}`);
        healthy = response.ok;
      } catch {
        await sleep(1000);
      }
    }
  }
}
```

## 6. 最佳实践

### 6.1 更新配置

- 设置合理的批次大小
- 配置健康检查
- 设置更新延迟
- 实现自动回滚

### 6.2 监控验证

- 监控更新过程
- 验证新实例健康
- 检查服务可用性
- 准备回滚方案

## 7. 注意事项

- **批次大小**：设置合理的批次大小
- **健康检查**：实现健康检查
- **数据一致性**：处理数据一致性问题
- **回滚准备**：准备回滚方案

## 8. 常见问题

### 8.1 如何设置批次大小？

根据实例数量、风险承受能力、更新速度选择。

### 8.2 如何处理更新失败？

实现自动回滚、健康检查、监控告警。

### 8.3 如何优化更新速度？

增加批次大小、减少等待时间、优化健康检查。

## 9. 实践任务

1. **实现滚动更新**：实现滚动更新流程
2. **配置更新策略**：配置更新参数
3. **健康检查**：实现健康检查
4. **监控验证**：监控和验证更新
5. **持续优化**：持续优化更新流程

---

**下一章**：[9.9 回滚与灾难恢复](../chapter-09-rollback/readme.md)
