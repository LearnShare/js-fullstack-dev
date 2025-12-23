# 8.5.5 链路追踪（OpenTelemetry）

## 1. 概述

链路追踪是分布式系统中追踪请求完整路径的技术，通过记录请求在各个服务中的执行情况，可以帮助开发者理解系统行为、定位性能问题。

## 2. OpenTelemetry 基础

### 2.1 安装

```bash
npm install @opentelemetry/api
npm install @opentelemetry/sdk-node
npm install @opentelemetry/instrumentation-http
npm install @opentelemetry/instrumentation-express
```

### 2.2 初始化

```ts
import { NodeSDK } from '@opentelemetry/sdk-node';
import { getNodeAutoInstrumentations } from '@opentelemetry/auto-instrumentations-node';
import { JaegerExporter } from '@opentelemetry/exporter-jaeger';

const sdk = new NodeSDK({
  traceExporter: new JaegerExporter({
    endpoint: 'http://localhost:14268/api/traces'
  }),
  instrumentations: [getNodeAutoInstrumentations()]
});

sdk.start();
```

## 3. 手动追踪

### 3.1 创建 Span

```ts
import { trace } from '@opentelemetry/api';

const tracer = trace.getTracer('my-service');

async function processOrder(orderId: number): Promise<void> {
  const span = tracer.startSpan('processOrder');
  span.setAttribute('order.id', orderId);
  
  try {
    await validateOrder(orderId);
    await processPayment(orderId);
    await updateInventory(orderId);
    span.setStatus({ code: SpanStatusCode.OK });
  } catch (error) {
    span.setStatus({ 
      code: SpanStatusCode.ERROR, 
      message: (error as Error).message 
    });
    span.recordException(error as Error);
    throw error;
  } finally {
    span.end();
  }
}
```

### 3.2 嵌套 Span

```ts
async function processOrder(orderId: number): Promise<void> {
  const parentSpan = tracer.startSpan('processOrder');
  
  try {
    const validateSpan = tracer.startSpan('validateOrder', {
      parent: parentSpan
    });
    await validateOrder(orderId);
    validateSpan.end();
    
    const paymentSpan = tracer.startSpan('processPayment', {
      parent: parentSpan
    });
    await processPayment(orderId);
    paymentSpan.end();
  } finally {
    parentSpan.end();
  }
}
```

## 4. Express 集成

### 4.1 自动追踪

```ts
import express, { Express } from 'express';
import { trace, context } from '@opentelemetry/api';

const app: Express = express();

app.use((req, res, next) => {
  const span = trace.getActiveSpan();
  if (span) {
    span.setAttribute('http.method', req.method);
    span.setAttribute('http.url', req.url);
  }
  next();
});
```

## 5. 数据库追踪

### 5.1 追踪数据库查询

```ts
async function queryDatabase(sql: string, params: any[]): Promise<any> {
  const span = tracer.startSpan('db.query');
  span.setAttribute('db.statement', sql);
  span.setAttribute('db.params', JSON.stringify(params));
  
  try {
    const result = await db.query(sql, params);
    span.setAttribute('db.rows', result.length);
    return result;
  } catch (error) {
    span.recordException(error as Error);
    throw error;
  } finally {
    span.end();
  }
}
```

## 6. 最佳实践

### 6.1 追踪设计

- 追踪关键操作
- 设置合理的采样率
- 包含业务上下文
- 关联日志和指标

### 6.2 性能考虑

- 使用采样减少开销
- 异步发送追踪数据
- 批量发送数据
- 监控追踪性能

## 7. 注意事项

- **性能影响**：注意追踪的性能开销
- **数据量**：控制追踪数据量
- **采样策略**：设置合理的采样率
- **隐私安全**：避免追踪敏感信息

## 8. 常见问题

### 8.1 如何选择采样率？

根据系统负载、存储成本、需求确定。

### 8.2 如何处理追踪数据？

使用追踪后端、可视化工具、分析工具。

### 8.3 如何优化追踪性能？

使用采样、异步处理、批量发送。

## 9. 实践任务

1. **配置追踪**：配置 OpenTelemetry
2. **实现追踪**：实现链路追踪
3. **可视化**：配置追踪可视化
4. **性能优化**：优化追踪性能
5. **持续改进**：持续改进追踪系统

---

**下一节**：[8.5.6 错误追踪（Sentry）](section-06-error-tracking.md)
