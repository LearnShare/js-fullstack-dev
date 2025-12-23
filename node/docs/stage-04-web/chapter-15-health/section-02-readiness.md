# 4.15.2 就绪检查（Readiness）

## 1. 概述

就绪检查（Readiness Probe）用于检查应用是否已经就绪，可以开始接收和处理请求。就绪检查通常检查应用初始化、依赖服务连接等，确保应用完全启动后才开始接收流量。

## 2. 核心概念

### 2.1 就绪检查的目的

- **启动检查**：检查应用是否完全启动
- **依赖检查**：检查依赖服务是否可用
- **流量控制**：控制何时开始接收流量
- **滚动更新**：支持滚动更新场景

### 2.2 就绪检查的时机

- **应用启动**：应用启动后检查
- **依赖连接**：检查数据库、Redis 等连接
- **配置加载**：检查配置是否加载完成
- **服务注册**：检查服务是否注册完成

## 3. 基本实现

### 3.1 Express 实现

```ts
let isReady = false;

async function initializeApp(): Promise<void> {
  // 初始化数据库连接
  await connectDatabase();
  
  // 初始化 Redis 连接
  await connectRedis();
  
  // 加载配置
  await loadConfiguration();
  
  isReady = true;
}

app.get('/ready', (req: Request, res: Response): void => {
  if (isReady) {
    res.json({ status: 'ready' });
  } else {
    res.status(503).json({ status: 'not ready' });
  }
});

// 启动应用
initializeApp().then((): void => {
  app.listen(3000, (): void => {
    console.log('Server running on port 3000');
  });
});
```

### 3.2 详细就绪检查

```ts
interface ReadinessStatus {
  ready: boolean;
  checks: {
    database: boolean;
    redis: boolean;
    configuration: boolean;
  };
}

async function checkReadiness(): Promise<ReadinessStatus> {
  const checks = {
    database: false,
    redis: false,
    configuration: false
  };
  
  // 检查数据库
  try {
    await checkDatabaseConnection();
    checks.database = true;
  } catch (error) {
    console.error('Database check failed:', error);
  }
  
  // 检查 Redis
  try {
    await checkRedisConnection();
    checks.redis = true;
  } catch (error) {
    console.error('Redis check failed:', error);
  }
  
  // 检查配置
  try {
    validateConfiguration();
    checks.configuration = true;
  } catch (error) {
    console.error('Configuration check failed:', error);
  }
  
  const ready = Object.values(checks).every((check: boolean) => check);
  
  return { ready, checks };
}

app.get('/ready', async (req: Request, res: Response): Promise<void> => {
  const status = await checkReadiness();
  
  if (status.ready) {
    res.json({ status: 'ready', checks: status.checks });
  } else {
    res.status(503).json({ status: 'not ready', checks: status.checks });
  }
});
```

## 4. 依赖检查

### 4.1 数据库检查

```ts
async function checkDatabaseConnection(): Promise<boolean> {
  try {
    await db.query('SELECT 1');
    return true;
  } catch (error) {
    return false;
  }
}
```

### 4.2 Redis 检查

```ts
async function checkRedisConnection(): Promise<boolean> {
  try {
    await redis.ping();
    return true;
  } catch (error) {
    return false;
  }
}
```

### 4.3 外部服务检查

```ts
async function checkExternalService(): Promise<boolean> {
  try {
    const response = await fetch('https://api.external-service.com/health');
    return response.ok;
  } catch (error) {
    return false;
  }
}
```

## 5. 最佳实践

### 5.1 检查策略

- 检查所有关键依赖
- 快速失败
- 提供详细状态信息

### 5.2 性能优化

- 使用缓存减少检查频率
- 异步检查多个依赖
- 设置超时时间

### 5.3 错误处理

- 记录检查失败原因
- 提供清晰的错误信息
- 实现重试机制

## 6. 注意事项

- **准确性**：确保就绪检查准确反映应用状态
- **性能**：就绪检查应该快速响应
- **依赖**：检查所有关键依赖
- **监控**：集成到监控系统

## 7. 常见问题

### 7.1 就绪检查和健康检查的区别？

就绪检查检查应用是否就绪接收流量，健康检查检查应用是否正常运行。

### 7.2 如何处理依赖不可用？

返回 503 状态码，包含不可用的依赖信息。

### 7.3 如何优化就绪检查性能？

使用缓存、异步检查、设置合理的超时时间。

## 8. 实践任务

1. **实现就绪检查**：实现基本的就绪检查端点
2. **实现依赖检查**：实现数据库、Redis 等依赖检查
3. **实现详细状态**：实现详细的就绪状态信息
4. **优化检查性能**：优化就绪检查性能
5. **集成容器编排**：将就绪检查集成到 Kubernetes 等容器编排系统

---

**下一节**：[4.15.3 存活检查（Liveness）](section-03-liveness.md)
