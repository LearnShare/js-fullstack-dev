# 8.5.4 指标监控（Prometheus）

## 1. 概述

指标监控是可观测性的重要组成部分，通过收集和存储数值型数据，可以监控系统状态、分析趋势、设置告警。Prometheus 是广泛使用的指标监控系统。

## 2. Prometheus 基础

### 2.1 指标类型

- **Counter**：只增不减的计数器
- **Gauge**：可增可减的仪表盘
- **Histogram**：直方图，用于统计分布
- **Summary**：摘要，用于统计分位数

### 2.2 安装客户端

```bash
npm install prom-client
```

## 3. 指标定义

### 3.1 Counter

```ts
import { Counter } from 'prom-client';

const httpRequestsTotal = new Counter({
  name: 'http_requests_total',
  help: 'Total number of HTTP requests',
  labelNames: ['method', 'status']
});

// 使用
httpRequestsTotal.inc({ method: 'GET', status: '200' });
```

### 3.2 Gauge

```ts
import { Gauge } from 'prom-client';

const activeConnections = new Gauge({
  name: 'active_connections',
  help: 'Number of active connections'
});

// 使用
activeConnections.set(100);
activeConnections.inc();
activeConnections.dec();
```

### 3.3 Histogram

```ts
import { Histogram } from 'prom-client';

const httpRequestDuration = new Histogram({
  name: 'http_request_duration_seconds',
  help: 'Duration of HTTP requests in seconds',
  buckets: [0.1, 0.5, 1, 2, 5]
});

// 使用
const end = httpRequestDuration.startTimer();
// 执行操作
end();
```

## 4. Express 集成

### 4.1 中间件

```ts
import express, { Express, Request, Response } from 'express';
import { Registry, Counter, Histogram } from 'prom-client';

const register = new Registry();

const httpRequestsTotal = new Counter({
  name: 'http_requests_total',
  help: 'Total number of HTTP requests',
  labelNames: ['method', 'status'],
  registers: [register]
});

const httpRequestDuration = new Histogram({
  name: 'http_request_duration_seconds',
  help: 'Duration of HTTP requests',
  registers: [register]
});

const app: Express = express();

// 指标中间件
app.use((req: Request, res: Response, next): void => {
  const end = httpRequestDuration.startTimer();
  
  res.on('finish', (): void => {
    httpRequestsTotal.inc({ method: req.method, status: res.statusCode.toString() });
    end();
  });
  
  next();
});

// 指标端点
app.get('/metrics', async (req: Request, res: Response): Promise<void> => {
  res.set('Content-Type', register.contentType);
  res.end(await register.metrics());
});
```

## 5. 自定义指标

### 5.1 业务指标

```ts
const userRegistrations = new Counter({
  name: 'user_registrations_total',
  help: 'Total number of user registrations',
  labelNames: ['source']
});

const orderValue = new Histogram({
  name: 'order_value',
  help: 'Order value distribution',
  buckets: [10, 50, 100, 500, 1000, 5000]
});

// 使用
userRegistrations.inc({ source: 'web' });
orderValue.observe(150);
```

## 6. Grafana 可视化

### 6.1 配置数据源

```yaml
# grafana-datasource.yml
apiVersion: 1
datasources:
  - name: Prometheus
    type: prometheus
    access: proxy
    url: http://prometheus:9090
```

### 6.2 创建仪表板

使用 Grafana 创建仪表板，可视化 Prometheus 指标。

## 7. 最佳实践

### 7.1 指标设计

- 选择关键指标
- 使用有意义的标签
- 设置合理的采样率
- 避免指标爆炸

### 7.2 告警配置

- 设置合理的阈值
- 配置告警规则
- 设置通知渠道
- 定期审查告警

## 8. 注意事项

- **指标数量**：控制指标数量
- **标签基数**：避免高基数标签
- **存储成本**：考虑存储成本
- **性能影响**：注意性能开销

## 9. 常见问题

### 9.1 如何选择指标？

根据业务需求、系统特性、监控目标选择。

### 9.2 如何处理高基数标签？

避免使用高基数标签，使用日志记录详细信息。

### 9.3 如何优化指标性能？

使用批量收集、异步处理、合理采样。

## 10. 实践任务

1. **指标定义**：定义业务指标
2. **指标收集**：实现指标收集
3. **可视化**：配置 Grafana 可视化
4. **告警配置**：配置告警规则
5. **持续优化**：持续优化指标系统

---

**下一节**：[8.5.5 链路追踪（OpenTelemetry）](section-05-tracing.md)
