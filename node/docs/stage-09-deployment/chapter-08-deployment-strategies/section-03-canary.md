# 9.8.3 金丝雀部署

## 1. 概述

金丝雀部署是将新版本逐步部署到生产环境的策略，先部署到少量实例，逐步增加流量，监控表现，实现风险可控的部署。

## 2. 工作原理

### 2.1 基本流程

```
1. 部署新版本到少量实例（如 10%）
2. 将 10% 流量路由到新版本
3. 监控新版本表现（错误率、响应时间等）
4. 如果表现良好，逐步增加流量（20%、50%、100%）
5. 如果出现问题，立即回滚
```

### 2.2 流量分配

```
负载均衡器
    |
    ├─> 90% -> 旧版本实例
    └─> 10% -> 新版本实例（金丝雀）
```

## 3. 实现方式

### 3.1 Nginx 配置

```nginx
upstream app {
    # 旧版本：90%
    server app-v1:3000 weight=9;
    # 新版本：10%
    server app-v2:3000 weight=1;
}

server {
    listen 80;
    location / {
        proxy_pass http://app;
    }
}
```

### 3.2 自动化脚本

```ts
// deploy-canary.ts
interface CanaryConfig {
  initialTraffic: number;  // 初始流量百分比
  stepTraffic: number;      // 每次增加的流量
  monitoringDuration: number; // 监控时长（秒）
  errorThreshold: number;  // 错误率阈值
}

async function canaryDeploy(config: CanaryConfig): Promise<void> {
  let currentTraffic = config.initialTraffic;
  
  while (currentTraffic <= 100) {
    // 1. 设置流量分配
    await setTrafficSplit(currentTraffic, 100 - currentTraffic);
    
    // 2. 监控新版本
    console.log(`Monitoring with ${currentTraffic}% traffic...`);
    const metrics = await monitor(config.monitoringDuration);
    
    // 3. 检查指标
    if (metrics.errorRate > config.errorThreshold) {
      console.error('Error rate too high, rolling back...');
      await rollback();
      return;
    }
    
    // 4. 如果未达到 100%，增加流量
    if (currentTraffic < 100) {
      currentTraffic += config.stepTraffic;
      await sleep(60000); // 等待 1 分钟
    } else {
      break;
    }
  }
  
  console.log('Canary deployment completed successfully');
}

async function setTrafficSplit(newTraffic: number, oldTraffic: number): Promise<void> {
  // 更新负载均衡器配置
  // 例如：更新 Nginx 配置或 Kubernetes Service
}

async function monitor(duration: number): Promise<{ errorRate: number; avgResponseTime: number }> {
  // 收集监控指标
  return {
    errorRate: 0.01,
    avgResponseTime: 200
  };
}
```

## 4. Kubernetes 实现

### 4.1 使用 Istio

```yaml
# 部署新版本
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-v2
spec:
  replicas: 1
  selector:
    matchLabels:
      app: my-app
      version: v2
  template:
    metadata:
      labels:
        app: my-app
        version: v2
    spec:
      containers:
      - name: app
        image: my-app:v2.0

---
# 流量分配
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: app
spec:
  hosts:
  - app
  http:
  - match:
    - headers:
        user-agent:
          regex: ".*Chrome.*"
    route:
    - destination:
        host: app
        subset: v2
      weight: 10
    - destination:
        host: app
        subset: v1
      weight: 90
  - route:
    - destination:
        host: app
        subset: v1
      weight: 100
```

## 5. 监控指标

### 5.1 关键指标

```ts
interface CanaryMetrics {
  errorRate: number;        // 错误率
  responseTime: number;     // 响应时间
  throughput: number;       // 吞吐量
  cpuUsage: number;         // CPU 使用率
  memoryUsage: number;      // 内存使用率
}

async function collectMetrics(): Promise<CanaryMetrics> {
  // 从监控系统收集指标
  return {
    errorRate: 0.01,
    responseTime: 200,
    throughput: 1000,
    cpuUsage: 50,
    memoryUsage: 60
  };
}
```

## 6. 最佳实践

### 6.1 部署流程

- 逐步增加流量
- 持续监控指标
- 设置告警阈值
- 准备快速回滚

### 6.2 监控验证

- 监控关键指标
- 对比新旧版本
- 设置合理阈值
- 及时响应异常

## 7. 注意事项

- **监控指标**：监控关键指标
- **流量控制**：精确控制流量分配
- **回滚机制**：实现快速回滚
- **验证时间**：给足够时间验证

## 8. 常见问题

### 8.1 如何选择初始流量？

根据风险、用户量、监控能力选择，通常 1-10%。

### 8.2 如何判断是否继续？

根据错误率、响应时间、业务指标判断。

### 8.3 如何处理数据不一致？

使用版本兼容、数据迁移、数据同步。

## 9. 实践任务

1. **实现金丝雀部署**：实现金丝雀部署流程
2. **流量控制**：实现流量分配控制
3. **监控指标**：实现监控指标收集
4. **自动决策**：实现自动决策逻辑
5. **持续优化**：持续优化部署流程

---

**下一节**：[9.8.4 滚动更新](section-04-rolling-update.md)
