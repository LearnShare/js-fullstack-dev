# 8.5.2 日志系统（Winston、Pino）

## 1. 概述

日志系统是可观测性的基础，通过记录系统事件和状态，可以帮助开发者理解系统行为、定位问题。Winston 和 Pino 是 Node.js 中常用的日志库。

## 2. Winston

### 2.1 安装与配置

```bash
npm install winston
```

```ts
import winston from 'winston';

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.json()
  ),
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ filename: 'error.log', level: 'error' }),
    new winston.transports.File({ filename: 'combined.log' })
  ]
});
```

### 2.2 使用

```ts
logger.info('User logged in', { userId: 123, ip: '192.168.1.1' });
logger.error('Database error', { error: err.message, stack: err.stack });
logger.warn('High memory usage', { memory: process.memoryUsage() });
```

## 3. Pino

### 3.1 安装与配置

```bash
npm install pino
npm install pino-pretty  # 开发环境美化输出
```

```ts
import pino from 'pino';

const logger = pino({
  level: 'info',
  transport: process.env.NODE_ENV === 'development' ? {
    target: 'pino-pretty',
    options: {
      colorize: true
    }
  } : undefined
});
```

### 3.2 使用

```ts
logger.info({ userId: 123, ip: '192.168.1.1' }, 'User logged in');
logger.error({ err }, 'Database error');
logger.warn({ memory: process.memoryUsage() }, 'High memory usage');
```

## 4. 日志级别

### 4.1 级别定义

```ts
enum LogLevel {
  ERROR = 0,
  WARN = 1,
  INFO = 2,
  DEBUG = 3,
  TRACE = 4
}
```

### 4.2 级别使用

```ts
// 错误：系统错误，需要立即处理
logger.error('Database connection failed', { error });

// 警告：潜在问题，需要关注
logger.warn('High CPU usage', { cpu: 90 });

// 信息：重要事件，用于跟踪
logger.info('User registered', { userId });

// 调试：调试信息，开发时使用
logger.debug('Processing request', { requestId });

// 追踪：详细追踪信息
logger.trace('Function called', { function: 'processData' });
```

## 5. 结构化日志

### 5.1 日志格式

```ts
// Winston 结构化日志
logger.info({
  timestamp: new Date().toISOString(),
  level: 'info',
  message: 'User logged in',
  userId: 123,
  ip: '192.168.1.1',
  userAgent: 'Mozilla/5.0...'
});

// Pino 结构化日志
logger.info({
  userId: 123,
  ip: '192.168.1.1',
  userAgent: 'Mozilla/5.0...'
}, 'User logged in');
```

### 5.2 日志上下文

```ts
class LoggerWithContext {
  constructor(private baseLogger: any, private context: Record<string, any>) {}
  
  child(context: Record<string, any>): LoggerWithContext {
    return new LoggerWithContext(this.baseLogger, { ...this.context, ...context });
  }
  
  info(message: string, meta?: Record<string, any>): void {
    this.baseLogger.info({ ...this.context, ...meta }, message);
  }
}

// 使用
const requestLogger = logger.child({ requestId: 'req-123' });
requestLogger.info('Processing request');
```

## 6. 最佳实践

### 6.1 日志设计

- 使用结构化日志
- 包含足够的上下文
- 设置合理的日志级别
- 避免记录敏感信息

### 6.2 性能考虑

- 使用异步日志
- 批量写入
- 控制日志量
- 使用采样

## 7. 注意事项

- **性能影响**：注意日志的性能开销
- **存储成本**：控制日志存储成本
- **隐私安全**：避免记录敏感信息
- **日志轮转**：实现日志轮转

## 8. 常见问题

### 8.1 如何选择日志库？

根据性能需求、功能需求、团队经验选择。

### 8.2 如何处理大量日志？

使用日志聚合、采样、归档。

### 8.3 如何优化日志性能？

使用异步日志、批量写入、控制日志级别。

## 9. 实践任务

1. **配置日志**：配置日志系统
2. **结构化日志**：实现结构化日志
3. **日志级别**：设置合理的日志级别
4. **性能优化**：优化日志性能
5. **持续改进**：持续改进日志系统

---

**下一节**：[8.5.3 日志轮转](section-03-log-rotation.md)
