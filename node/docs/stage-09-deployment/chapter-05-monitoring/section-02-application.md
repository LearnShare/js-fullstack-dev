# 9.5.2 应用监控

## 1. 概述

应用监控是监控应用层面的指标，包括性能、错误、业务指标等。应用监控可以帮助开发者理解应用行为、定位问题、优化性能。

## 2. 性能监控

### 2.1 响应时间监控

```ts
import { performance } from 'node:perf_hooks';

class ResponseTimeMonitor {
  private timings: Map<string, number[]> = new Map();
  
  record(endpoint: string, duration: number): void {
    if (!this.timings.has(endpoint)) {
      this.timings.set(endpoint, []);
    }
    this.timings.get(endpoint)!.push(duration);
  }
  
  getMetrics(endpoint: string): {
    avg: number;
    p95: number;
    p99: number;
  } | null {
    const times = this.timings.get(endpoint);
    if (!times || times.length === 0) {
      return null;
    }
    
    const sorted = [...times].sort((a, b) => a - b);
    return {
      avg: sorted.reduce((a, b) => a + b, 0) / sorted.length,
      p95: sorted[Math.floor(sorted.length * 0.95)],
      p99: sorted[Math.floor(sorted.length * 0.99)]
    };
  }
}

// 使用
const monitor = new ResponseTimeMonitor();

app.use((req: Request, res: Response, next: NextFunction): void => {
  const start = performance.now();
  
  res.on('finish', (): void => {
    const duration = performance.now() - start;
    monitor.record(req.path, duration);
  });
  
  next();
});
```

### 2.2 错误率监控

```ts
class ErrorRateMonitor {
  private errors: Map<string, number> = new Map();
  private requests: Map<string, number> = new Map();
  
  recordRequest(endpoint: string): void {
    this.requests.set(endpoint, (this.requests.get(endpoint) || 0) + 1);
  }
  
  recordError(endpoint: string): void {
    this.errors.set(endpoint, (this.errors.get(endpoint) || 0) + 1);
  }
  
  getErrorRate(endpoint: string): number {
    const requests = this.requests.get(endpoint) || 0;
    const errors = this.errors.get(endpoint) || 0;
    return requests > 0 ? errors / requests : 0;
  }
}
```

## 3. 业务指标监控

### 3.1 业务指标

```ts
class BusinessMetrics {
  private metrics: Map<string, number> = new Map();
  
  increment(metric: string, value: number = 1): void {
    this.metrics.set(metric, (this.metrics.get(metric) || 0) + value);
  }
  
  set(metric: string, value: number): void {
    this.metrics.set(metric, value);
  }
  
  get(metric: string): number {
    return this.metrics.get(metric) || 0;
  }
}

// 使用
const metrics = new BusinessMetrics();

app.post('/api/orders', async (req: Request, res: Response): Promise<void> => {
  // 处理订单
  metrics.increment('orders.total');
  metrics.increment('orders.value', req.body.amount);
});
```

## 4. 健康检查

### 4.1 健康检查端点

```ts
app.get('/health', async (req: Request, res: Response): Promise<void> => {
  const health = {
    status: 'healthy',
    timestamp: new Date().toISOString(),
    uptime: process.uptime(),
    memory: process.memoryUsage(),
    checks: {
      database: await checkDatabase(),
      redis: await checkRedis()
    }
  };
  
  const isHealthy = health.checks.database && health.checks.redis;
  res.status(isHealthy ? 200 : 503).json(health);
});

async function checkDatabase(): Promise<boolean> {
  try {
    await db.query('SELECT 1');
    return true;
  } catch {
    return false;
  }
}
```

## 5. 最佳实践

### 5.1 监控设计

- 监控关键指标
- 设置合理采样
- 使用结构化数据
- 实现实时监控

### 5.2 性能优化

- 异步收集指标
- 批量发送数据
- 使用缓存
- 优化存储

## 6. 注意事项

- **性能影响**：注意监控的性能开销
- **数据量**：控制监控数据量
- **隐私保护**：保护用户隐私
- **成本控制**：控制监控成本

## 7. 常见问题

### 7.1 如何选择监控指标？

根据业务需求、性能要求、成本预算选择。

### 7.2 如何处理大量监控数据？

使用采样、聚合、归档。

### 7.3 如何优化监控性能？

异步收集、批量发送、使用缓存。

## 8. 实践任务

1. **实现监控**：实现应用监控
2. **性能监控**：监控应用性能
3. **业务指标**：监控业务指标
4. **健康检查**：实现健康检查
5. **持续优化**：持续优化监控系统

---

**下一节**：[9.5.3 基础设施监控](section-03-infrastructure.md)
