# 8.1.1 性能指标

## 1. 概述

性能指标是衡量应用性能的量化指标，包括响应时间、吞吐量、资源使用等。理解性能指标对于性能优化至关重要。

## 2. 核心指标

### 2.1 响应时间（Response Time）

**定义**：从请求发送到响应接收的时间。

**类型**：
- **平均响应时间**：所有请求的平均响应时间
- **P50 响应时间**：50% 请求的响应时间（中位数）
- **P95 响应时间**：95% 请求的响应时间
- **P99 响应时间**：99% 请求的响应时间
- **最大响应时间**：最慢请求的响应时间

**测量**：
```ts
interface ResponseTimeMetrics {
  average: number;
  p50: number;
  p95: number;
  p99: number;
  max: number;
}

function calculateResponseTimeMetrics(times: number[]): ResponseTimeMetrics {
  const sorted = [...times].sort((a: number, b: number) => a - b);
  const sum = sorted.reduce((a: number, b: number) => a + b, 0);
  
  return {
    average: sum / sorted.length,
    p50: sorted[Math.floor(sorted.length * 0.5)],
    p95: sorted[Math.floor(sorted.length * 0.95)],
    p99: sorted[Math.floor(sorted.length * 0.99)],
    max: sorted[sorted.length - 1]
  };
}
```

### 2.2 吞吐量（Throughput）

**定义**：单位时间内处理的请求数。

**类型**：
- **请求/秒（RPS）**：每秒处理的请求数
- **事务/秒（TPS）**：每秒处理的事务数
- **字节/秒**：每秒传输的字节数

**测量**：
```ts
function calculateThroughput(requests: number, duration: number): number {
  return requests / (duration / 1000); // 请求/秒
}
```

### 2.3 并发数（Concurrency）

**定义**：同时处理的请求数。

**类型**：
- **并发用户数**：同时访问的用户数
- **并发连接数**：同时建立的连接数
- **并发请求数**：同时处理的请求数

### 2.4 错误率（Error Rate）

**定义**：错误请求占总请求的比例。

**计算**：`错误请求数 / 总请求数`

**测量**：
```ts
function calculateErrorRate(total: number, errors: number): number {
  return errors / total;
}
```

## 3. 资源指标

### 3.1 CPU 使用率

**定义**：CPU 使用的时间比例。

**测量**：
```ts
import { cpus } from 'node:os';

function getCPUUsage(): number {
  const cpus = require('os').cpus();
  let totalIdle = 0;
  let totalTick = 0;
  
  for (const cpu of cpus) {
    for (const type in cpu.times) {
      totalTick += cpu.times[type as keyof typeof cpu.times];
    }
    totalIdle += cpu.times.idle;
  }
  
  const idle = totalIdle / cpus.length;
  const total = totalTick / cpus.length;
  const usage = 100 - ~~(100 * idle / total);
  
  return usage;
}
```

### 3.2 内存使用

**定义**：应用使用的内存量。

**测量**：
```ts
import { memoryUsage } from 'node:process';

function getMemoryUsage(): {
  rss: number;
  heapTotal: number;
  heapUsed: number;
  external: number;
} {
  return memoryUsage();
}

// 使用
const usage = getMemoryUsage();
console.log(`Heap Used: ${(usage.heapUsed / 1024 / 1024).toFixed(2)} MB`);
```

### 3.3 网络 I/O

**定义**：网络传输的数据量。

**测量**：
```ts
import { networkInterfaces } from 'node:os';

function getNetworkStats(): Record<string, any> {
  const interfaces = networkInterfaces();
  // 收集网络统计信息
  return {};
}
```

## 4. 性能目标

### 4.1 Web 应用目标

- **首屏渲染**：< 1 秒
- **API 响应时间**：P95 < 200ms
- **页面加载时间**：< 3 秒
- **错误率**：< 0.1%

### 4.2 API 服务目标

- **响应时间**：P95 < 100ms
- **吞吐量**：> 1000 RPS
- **错误率**：< 0.01%
- **可用性**：> 99.9%

## 5. 指标监控

### 5.1 实时监控

```ts
class PerformanceMonitor {
  private metrics: Map<string, number[]> = new Map();
  
  recordMetric(name: string, value: number): void {
    if (!this.metrics.has(name)) {
      this.metrics.set(name, []);
    }
    this.metrics.get(name)!.push(value);
    
    // 保留最近 1000 个值
    const values = this.metrics.get(name)!;
    if (values.length > 1000) {
      values.shift();
    }
  }
  
  getMetrics(name: string): ResponseTimeMetrics | null {
    const values = this.metrics.get(name);
    if (!values || values.length === 0) {
      return null;
    }
    return calculateResponseTimeMetrics(values);
  }
}

// 使用
const monitor = new PerformanceMonitor();

app.use((req: Request, res: Response, next: NextFunction): void => {
  const start = Date.now();
  
  res.on('finish', (): void => {
    const duration = Date.now() - start;
    monitor.recordMetric('response_time', duration);
  });
  
  next();
});
```

## 6. 最佳实践

### 6.1 指标选择

- 选择关键指标
- 设置合理目标
- 持续监控
- 定期审查

### 6.2 指标分析

- 分析趋势
- 识别异常
- 对比基准
- 提出优化

## 7. 注意事项

- **指标选择**：选择关键性能指标
- **目标设定**：设置合理的性能目标
- **持续监控**：持续监控性能指标
- **结果分析**：深入分析性能数据

## 8. 常见问题

### 8.1 如何选择性能指标？

根据应用类型、业务需求、用户期望选择。

### 8.2 如何设定性能目标？

根据业务需求、历史数据、SLA 设定。

### 8.3 如何监控性能指标？

使用监控工具、实时收集、定期分析。

## 9. 相关资源

- [性能指标](https://en.wikipedia.org/wiki/Performance_indicator)
- [Web 性能](https://web.dev/performance/)

---

**下一节**：[8.1.2 性能分析工具](section-02-profiling.md)
