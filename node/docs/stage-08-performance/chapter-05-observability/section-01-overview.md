# 8.5.1 可观测性概述

## 1. 概述

可观测性（Observability）是系统的一种属性，通过外部输出（日志、指标、追踪）来理解系统内部状态。可观测性包括三个支柱：日志（Logs）、指标（Metrics）、追踪（Traces）。

## 2. 三大支柱

### 2.1 日志（Logs）

**定义**：记录系统事件和状态。

**特点**：
- 离散事件
- 时间序列
- 详细上下文
- 用于调试和分析

**示例**：
```ts
logger.info('User logged in', { userId: 123, ip: '192.168.1.1' });
logger.error('Database connection failed', { error: err.message });
```

### 2.2 指标（Metrics）

**定义**：数值型数据，表示系统状态。

**特点**：
- 聚合数据
- 时间序列
- 高效存储
- 用于监控和告警

**示例**：
```ts
metrics.increment('requests.total');
metrics.histogram('response.time', duration);
metrics.gauge('active.connections', count);
```

### 2.3 追踪（Traces）

**定义**：请求在系统中的完整路径。

**特点**：
- 分布式追踪
- 请求上下文
- 性能分析
- 用于问题定位

**示例**：
```ts
const span = tracer.startSpan('user.login');
span.setAttribute('user.id', userId);
// 执行操作
span.end();
```

## 3. 可观测性价值

### 3.1 问题定位

- 快速定位问题
- 理解系统行为
- 分析性能瓶颈
- 优化系统性能

### 3.2 系统监控

- 实时监控系统状态
- 预警潜在问题
- 分析系统趋势
- 支持决策制定

## 4. 可观测性工具

### 4.1 日志工具

- **Winston**：Node.js 日志库
- **Pino**：高性能日志库
- **Bunyan**：结构化日志库

### 4.2 指标工具

- **Prometheus**：指标收集和存储
- **Grafana**：指标可视化
- **StatsD**：指标收集

### 4.3 追踪工具

- **OpenTelemetry**：分布式追踪标准
- **Jaeger**：分布式追踪系统
- **Zipkin**：分布式追踪系统

### 4.4 错误追踪

- **Sentry**：错误监控和追踪
- **Rollbar**：错误监控
- **Bugsnag**：错误监控

## 5. 最佳实践

### 5.1 日志实践

- 使用结构化日志
- 设置合理的日志级别
- 包含足够的上下文
- 避免记录敏感信息

### 5.2 指标实践

- 选择关键指标
- 设置合理的采样率
- 使用标签分类
- 设置告警阈值

### 5.3 追踪实践

- 追踪关键操作
- 设置合理的采样率
- 包含业务上下文
- 关联日志和指标

## 6. 注意事项

- **性能影响**：注意可观测性的性能开销
- **数据量**：控制数据量，避免存储成本过高
- **隐私安全**：避免记录敏感信息
- **工具选择**：根据需求选择合适的工具

## 7. 常见问题

### 7.1 如何选择可观测性工具？

根据需求、预算、团队技能选择。

### 7.2 如何处理大量日志？

使用日志聚合、采样、归档。

### 7.3 如何平衡可观测性和性能？

使用采样、异步处理、批量发送。

## 8. 相关资源

- [可观测性](https://en.wikipedia.org/wiki/Observability)
- [OpenTelemetry](https://opentelemetry.io/)

---

**下一节**：[8.5.2 日志系统（Winston、Pino）](section-02-logging.md)
