# 5.11.3 性能指标监控

## 1. 概述

性能指标监控是数据库监控的重要组成部分，通过监控关键性能指标可以及时发现性能问题、优化数据库配置、预防故障。

## 2. 关键指标

### 2.1 查询性能指标

```ts
interface QueryMetrics {
  totalQueries: number;
  avgQueryTime: number;
  slowQueries: number;
  queryThroughput: number;
}

async function getQueryMetrics(): Promise<QueryMetrics> {
  const stats = await db.query(`
    SELECT 
      SUM(calls) as total_queries,
      AVG(mean_time) as avg_query_time,
      COUNT(*) FILTER (WHERE mean_time > 1000) as slow_queries
    FROM pg_stat_statements
  `);
  
  return {
    totalQueries: stats[0].total_queries,
    avgQueryTime: stats[0].avg_query_time,
    slowQueries: stats[0].slow_queries,
    queryThroughput: stats[0].total_queries / 60 // 每分钟查询数
  };
}
```

### 2.2 连接指标

```ts
interface ConnectionMetrics {
  totalConnections: number;
  activeConnections: number;
  idleConnections: number;
  waitingConnections: number;
}

async function getConnectionMetrics(): Promise<ConnectionMetrics> {
  const stats = await db.query(`
    SELECT 
      COUNT(*) as total,
      COUNT(*) FILTER (WHERE state = 'active') as active,
      COUNT(*) FILTER (WHERE state = 'idle') as idle,
      COUNT(*) FILTER (WHERE wait_event_type = 'Lock') as waiting
    FROM pg_stat_activity
  `);
  
  return {
    totalConnections: stats[0].total,
    activeConnections: stats[0].active,
    idleConnections: stats[0].idle,
    waitingConnections: stats[0].waiting
  };
}
```

### 2.3 资源使用指标

```ts
interface ResourceMetrics {
  cpuUsage: number;
  memoryUsage: number;
  diskIO: number;
  networkIO: number;
}

async function getResourceMetrics(): Promise<ResourceMetrics> {
  // 使用系统监控工具获取资源指标
  const cpuUsage = await getCPUUsage();
  const memoryUsage = await getMemoryUsage();
  const diskIO = await getDiskIO();
  const networkIO = await getNetworkIO();
  
  return {
    cpuUsage,
    memoryUsage,
    diskIO,
    networkIO
  };
}
```

## 3. 监控实现

### 3.1 定期收集指标

```ts
import cron from 'node-cron';

const metrics: Array<{ timestamp: Date; metrics: QueryMetrics }> = [];

cron.schedule('*/1 * * * *', async (): Promise<void> => {
  const queryMetrics = await getQueryMetrics();
  const connectionMetrics = await getConnectionMetrics();
  const resourceMetrics = await getResourceMetrics();
  
  metrics.push({
    timestamp: new Date(),
    metrics: {
      ...queryMetrics,
      ...connectionMetrics,
      ...resourceMetrics
    }
  });
  
  // 保留最近 24 小时的数据
  const oneDayAgo = Date.now() - 24 * 60 * 60 * 1000;
  const filtered = metrics.filter((m: { timestamp: Date }) => m.timestamp.getTime() > oneDayAgo);
  metrics.length = 0;
  metrics.push(...filtered);
});
```

### 3.2 告警机制

```ts
async function checkMetrics(): Promise<void> {
  const queryMetrics = await getQueryMetrics();
  const connectionMetrics = await getConnectionMetrics();
  
  // 慢查询告警
  if (queryMetrics.slowQueries > 10) {
    await sendAlert('High number of slow queries detected');
  }
  
  // 连接数告警
  if (connectionMetrics.totalConnections > connectionMetrics.activeConnections * 0.9) {
    await sendAlert('High connection usage detected');
  }
  
  // 平均查询时间告警
  if (queryMetrics.avgQueryTime > 1000) {
    await sendAlert('High average query time detected');
  }
}
```

## 4. 可视化监控

### 4.1 Prometheus 集成

```ts
import { Registry, Counter, Gauge, Histogram } from 'prom-client';

const register = new Registry();

const queryCounter = new Counter({
  name: 'db_queries_total',
  help: 'Total number of database queries',
  registers: [register]
});

const queryDuration = new Histogram({
  name: 'db_query_duration_seconds',
  help: 'Database query duration',
  registers: [register]
});

async function recordQuery(duration: number): Promise<void> {
  queryCounter.inc();
  queryDuration.observe(duration);
}
```

### 4.2 Grafana 集成

```ts
// 提供指标端点
app.get('/metrics', async (req: Request, res: Response): Promise<void> => {
  res.set('Content-Type', register.contentType);
  res.end(await register.metrics());
});
```

## 5. 最佳实践

### 5.1 指标选择

- 选择关键指标监控
- 避免过度监控
- 定期审查指标
- 根据业务需求调整

### 5.2 告警设置

- 设置合理的告警阈值
- 避免告警风暴
- 实现告警升级
- 定期审查告警

## 6. 注意事项

- **监控开销**：注意监控对性能的影响
- **指标选择**：选择关键指标监控
- **告警设置**：设置合理的告警阈值
- **数据分析**：定期分析监控数据

## 7. 常见问题

### 7.1 监控哪些指标？

根据业务需求选择关键指标，如查询性能、连接状态、资源使用。

### 7.2 如何设置告警？

根据历史数据和业务需求设置告警阈值。

### 7.3 如何优化监控？

选择关键指标、优化监控频率、使用高效监控工具。

## 8. 实践任务

1. **收集指标**：实现性能指标收集
2. **监控实现**：实现定期监控
3. **告警机制**：实现告警机制
4. **可视化**：实现监控可视化
5. **性能优化**：根据监控结果优化性能

---

**阶段五完成**：恭喜完成阶段五的学习！可以继续学习阶段六：认证、授权与安全。
