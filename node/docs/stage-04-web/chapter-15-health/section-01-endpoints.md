# 4.15.1 健康检查端点

## 1. 概述

健康检查端点是用于检查应用运行状态的 API 端点。健康检查端点通常返回应用的基本状态信息，帮助监控系统和运维工具了解应用的运行情况。

## 2. 核心概念

### 2.1 健康检查的目的

- **状态监控**：监控应用运行状态
- **自动化运维**：支持自动化运维操作
- **故障检测**：快速检测应用故障
- **负载均衡**：支持负载均衡器健康检查

### 2.2 健康检查的类型

- **基本健康检查**：检查应用是否运行
- **就绪检查**：检查应用是否就绪接收请求
- **存活检查**：检查应用是否存活

## 3. 基本实现

### 3.1 Express 实现

```ts
import express, { Express, Request, Response } from 'express';

const app: Express = express();

app.get('/health', (req: Request, res: Response): void => {
  res.json({
    status: 'ok',
    timestamp: new Date().toISOString(),
    uptime: process.uptime()
  });
});

app.listen(3000, (): void => {
  console.log('Server running on port 3000');
});
```

### 3.2 Fastify 实现

```ts
import { FastifyInstance, FastifyRequest, FastifyReply } from 'fastify';

export default async function (fastify: FastifyInstance): Promise<void> {
  fastify.get('/health', async (request: FastifyRequest, reply: FastifyReply): Promise<void> => {
    reply.send({
      status: 'ok',
      timestamp: new Date().toISOString(),
      uptime: process.uptime()
    });
  });
}
```

## 4. 详细健康检查

### 4.1 系统信息

```ts
import { cpus, totalmem, freemem } from 'node:os';

app.get('/health', (req: Request, res: Response): void => {
  const memoryUsage = process.memoryUsage();
  const cpuUsage = process.cpuUsage();
  
  res.json({
    status: 'ok',
    timestamp: new Date().toISOString(),
    uptime: process.uptime(),
    system: {
      cpu: {
        count: cpus().length,
        usage: cpuUsage
      },
      memory: {
        total: totalmem(),
        free: freemem(),
        process: memoryUsage
      }
    }
  });
});
```

### 4.2 服务状态

```ts
interface ServiceStatus {
  name: string;
  status: 'ok' | 'error';
  message?: string;
}

async function checkServices(): Promise<ServiceStatus[]> {
  const services: ServiceStatus[] = [];
  
  // 检查数据库
  try {
    await checkDatabase();
    services.push({ name: 'database', status: 'ok' });
  } catch (error) {
    services.push({ name: 'database', status: 'error', message: (error as Error).message });
  }
  
  // 检查 Redis
  try {
    await checkRedis();
    services.push({ name: 'redis', status: 'ok' });
  } catch (error) {
    services.push({ name: 'redis', status: 'error', message: (error as Error).message });
  }
  
  return services;
}

app.get('/health', async (req: Request, res: Response): Promise<void> => {
  const services = await checkServices();
  const allHealthy = services.every((s: ServiceStatus) => s.status === 'ok');
  
  res.status(allHealthy ? 200 : 503).json({
    status: allHealthy ? 'ok' : 'degraded',
    timestamp: new Date().toISOString(),
    services
  });
});
```

## 5. 健康检查响应

### 5.1 成功响应

```json
{
  "status": "ok",
  "timestamp": "2025-12-22T10:00:00.000Z",
  "uptime": 3600,
  "version": "1.0.0"
}
```

### 5.2 失败响应

```json
{
  "status": "error",
  "timestamp": "2025-12-22T10:00:00.000Z",
  "services": [
    {
      "name": "database",
      "status": "error",
      "message": "Connection timeout"
    }
  ]
}
```

## 6. 最佳实践

### 6.1 端点设计

- 使用 `/health` 作为健康检查端点
- 返回 JSON 格式响应
- 包含状态和时间戳

### 6.2 性能考虑

- 健康检查应该快速响应
- 避免在健康检查中执行耗时操作
- 使用缓存减少检查频率

### 6.3 安全性

- 健康检查端点可以公开访问
- 不包含敏感信息
- 考虑实现访问限制

## 7. 注意事项

- **性能**：健康检查应该快速响应
- **准确性**：确保健康检查准确反映应用状态
- **可维护性**：保持健康检查代码清晰
- **监控**：集成到监控系统

## 8. 常见问题

### 8.1 健康检查应该检查什么？

检查应用基本状态、关键服务连接、系统资源等。

### 8.2 如何处理健康检查失败？

返回适当的 HTTP 状态码（如 503），包含错误信息。

### 8.3 如何优化健康检查性能？

使用缓存、异步检查、减少检查频率。

## 9. 实践任务

1. **实现基本健康检查**：实现基本的健康检查端点
2. **实现详细健康检查**：实现包含系统信息的健康检查
3. **实现服务检查**：实现数据库、Redis 等服务检查
4. **优化健康检查**：优化健康检查性能和准确性
5. **集成监控**：将健康检查集成到监控系统

---

**下一节**：[4.15.2 就绪检查（Readiness）](section-02-readiness.md)
