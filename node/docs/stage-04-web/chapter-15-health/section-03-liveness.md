# 4.15.3 存活检查（Liveness）

## 1. 概述

存活检查（Liveness Probe）用于检查应用是否仍然存活和正常运行。存活检查通常检查应用的基本运行状态，如果应用无响应或出现严重问题，容器编排系统可以重启应用。

## 2. 核心概念

### 2.1 存活检查的目的

- **故障检测**：检测应用是否崩溃
- **自动恢复**：支持自动重启应用
- **状态监控**：监控应用运行状态
- **资源清理**：清理无响应的应用实例

### 2.2 存活检查的特点

- **轻量级**：检查应该轻量快速
- **基本检查**：只检查应用基本运行状态
- **不依赖外部**：不依赖外部服务
- **快速响应**：应该快速响应

## 3. 基本实现

### 3.1 Express 实现

```ts
app.get('/live', (req: Request, res: Response): void => {
  res.json({
    status: 'alive',
    timestamp: new Date().toISOString()
  });
});
```

### 3.2 详细存活检查

```ts
app.get('/live', (req: Request, res: Response): void => {
  // 检查进程是否正常运行
  const memoryUsage = process.memoryUsage();
  const heapUsed = memoryUsage.heapUsed;
  const heapTotal = memoryUsage.heapTotal;
  const heapUsagePercent = (heapUsed / heapTotal) * 100;
  
  // 如果内存使用过高，认为应用不健康
  if (heapUsagePercent > 90) {
    return res.status(503).json({
      status: 'unhealthy',
      reason: 'High memory usage',
      memoryUsage: heapUsagePercent
    });
  }
  
  res.json({
    status: 'alive',
    timestamp: new Date().toISOString(),
    memory: {
      heapUsed,
      heapTotal,
      usagePercent: heapUsagePercent
    }
  });
});
```

## 4. 存活检查策略

### 4.1 基本存活检查

```ts
app.get('/live', (req: Request, res: Response): void => {
  // 简单的存活检查，只检查应用是否响应
  res.json({ status: 'alive' });
});
```

### 4.2 资源检查

```ts
app.get('/live', (req: Request, res: Response): void => {
  const memoryUsage = process.memoryUsage();
  const cpuUsage = process.cpuUsage();
  
  // 检查资源使用情况
  const isHealthy = checkResourceHealth(memoryUsage, cpuUsage);
  
  if (isHealthy) {
    res.json({ status: 'alive' });
  } else {
    res.status(503).json({ status: 'unhealthy' });
  }
});
```

### 4.3 死锁检测

```ts
let lastRequestTime = Date.now();

app.use((req: Request, res: Response, next: NextFunction): void => {
  lastRequestTime = Date.now();
  next();
});

app.get('/live', (req: Request, res: Response): void => {
  const timeSinceLastRequest = Date.now() - lastRequestTime;
  
  // 如果超过 5 分钟没有请求，可能应用死锁
  if (timeSinceLastRequest > 5 * 60 * 1000) {
    return res.status(503).json({
      status: 'unhealthy',
      reason: 'No requests for too long'
    });
  }
  
  res.json({ status: 'alive' });
});
```

## 5. 与容器编排集成

### 5.1 Kubernetes 配置

```yaml
livenessProbe:
  httpGet:
    path: /live
    port: 3000
  initialDelaySeconds: 30
  periodSeconds: 10
  timeoutSeconds: 5
  failureThreshold: 3
```

### 5.2 Docker Compose 配置

```yaml
services:
  app:
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/live"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
```

## 6. 最佳实践

### 6.1 检查设计

- 保持检查轻量级
- 不依赖外部服务
- 快速响应

### 6.2 错误处理

- 返回明确的健康状态
- 记录不健康的原因
- 实现自动恢复

### 6.3 性能优化

- 使用缓存
- 减少检查频率
- 优化检查逻辑

## 7. 注意事项

- **轻量级**：存活检查应该轻量快速
- **独立性**：不依赖外部服务
- **准确性**：准确反映应用状态
- **监控**：集成到监控系统

## 8. 常见问题

### 8.1 存活检查和就绪检查的区别？

存活检查检查应用是否存活，就绪检查检查应用是否就绪接收流量。

### 8.2 如何处理应用不健康？

返回 503 状态码，容器编排系统可以重启应用。

### 8.3 如何优化存活检查？

保持检查轻量级，使用缓存，减少检查频率。

## 9. 实践任务

1. **实现存活检查**：实现基本的存活检查端点
2. **实现资源检查**：实现内存、CPU 等资源检查
3. **集成容器编排**：将存活检查集成到 Kubernetes 等系统
4. **优化检查性能**：优化存活检查性能
5. **实现自动恢复**：实现应用自动恢复机制

---

**阶段四完成**：恭喜完成阶段四的学习！可以继续学习阶段五：数据持久化与数据库。
