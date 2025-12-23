# 9.5.3 基础设施监控

## 1. 概述

基础设施监控是监控服务器、网络、数据库等基础设施的状态，包括资源使用、性能指标、可用性等。基础设施监控可以帮助运维团队及时发现和解决基础设施问题。

## 2. 服务器监控

### 2.1 资源监控

```ts
import { cpus, totalmem, freemem } from 'node:os';
import { memoryUsage } from 'node:process';

interface ServerMetrics {
  cpu: {
    usage: number;
    cores: number;
  };
  memory: {
    total: number;
    used: number;
    free: number;
    usage: number;
  };
  disk: {
    total: number;
    used: number;
    free: number;
  };
}

function getServerMetrics(): ServerMetrics {
  const cpuUsage = getCPUUsage();
  const memTotal = totalmem();
  const memFree = freemem();
  const memUsed = memTotal - memFree;
  
  return {
    cpu: {
      usage: cpuUsage,
      cores: cpus().length
    },
    memory: {
      total: memTotal,
      used: memUsed,
      free: memFree,
      usage: (memUsed / memTotal) * 100
    },
    disk: {
      total: 0, // 需要额外工具获取
      used: 0,
      free: 0
    }
  };
}

function getCPUUsage(): number {
  // 计算 CPU 使用率
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
  return 100 - ~~(100 * idle / total);
}
```

## 3. Prometheus 集成

### 3.1 暴露指标

```ts
import express, { Express } from 'express';
import { Registry, Gauge, Counter } from 'prom-client';

const register = new Registry();

const cpuUsage = new Gauge({
  name: 'server_cpu_usage_percent',
  help: 'CPU usage percentage',
  registers: [register]
});

const memoryUsage = new Gauge({
  name: 'server_memory_usage_bytes',
  help: 'Memory usage in bytes',
  registers: [register]
});

const app: Express = express();

// 更新指标
setInterval(() => {
  const metrics = getServerMetrics();
  cpuUsage.set(metrics.cpu.usage);
  memoryUsage.set(metrics.memory.used);
}, 5000);

// 暴露指标端点
app.get('/metrics', async (req, res): Promise<void> => {
  res.set('Content-Type', register.contentType);
  res.end(await register.metrics());
});
```

## 4. 数据库监控

### 4.1 数据库指标

```ts
async function getDatabaseMetrics(): Promise<{
  connections: number;
  queries: number;
  slowQueries: number;
}> {
  const result = await db.query(`
    SELECT 
      count(*) as connections,
      sum(query_count) as queries,
      sum(slow_query_count) as slow_queries
    FROM pg_stat_activity
  `);
  
  return result.rows[0];
}
```

## 5. 容器监控

### 5.1 Docker 监控

```ts
import { exec } from 'node:child_process';
import { promisify } from 'node:util';

const execAsync = promisify(exec);

async function getContainerMetrics(containerId: string): Promise<{
  cpu: number;
  memory: number;
}> {
  const { stdout } = await execAsync(`docker stats ${containerId} --no-stream --format "{{.CPUPerc}},{{.MemUsage}}"`);
  const [cpu, memory] = stdout.trim().split(',');
  
  return {
    cpu: parseFloat(cpu.replace('%', '')),
    memory: parseFloat(memory.split('/')[0].replace('MiB', '').trim())
  };
}
```

## 6. 最佳实践

### 6.1 监控设计

- 监控关键资源
- 设置合理阈值
- 实现多维度监控
- 建立监控仪表板

### 6.2 告警配置

- 设置资源告警
- 配置性能告警
- 实现可用性告警
- 分级告警

## 7. 注意事项

- **资源消耗**：注意监控的资源消耗
- **数据存储**：控制监控数据存储
- **告警阈值**：设置合理的告警阈值
- **成本控制**：控制监控成本

## 8. 常见问题

### 8.1 如何选择监控工具？

根据需求、预算、团队技能选择。

### 8.2 如何设置告警阈值？

根据历史数据、资源容量、业务需求设置。

### 8.3 如何处理监控数据？

使用时间序列数据库、聚合数据、定期归档。

## 9. 实践任务

1. **实现监控**：实现基础设施监控
2. **资源监控**：监控服务器资源
3. **数据库监控**：监控数据库性能
4. **容器监控**：监控容器状态
5. **持续优化**：持续优化监控系统

---

**下一节**：[9.5.4 告警系统](section-04-alerts.md)
