# 8.5.3 日志轮转

## 1. 概述

日志轮转是管理日志文件的重要机制，通过定期轮转日志文件，可以控制日志文件大小、管理存储空间、便于日志归档和清理。

## 2. Winston 日志轮转

### 2.1 使用 winston-daily-rotate-file

```bash
npm install winston-daily-rotate-file
```

```ts
import winston from 'winston';
import DailyRotateFile from 'winston-daily-rotate-file';

const logger = winston.createLogger({
  transports: [
    new DailyRotateFile({
      filename: 'application-%DATE%.log',
      datePattern: 'YYYY-MM-DD',
      maxSize: '20m',
      maxFiles: '14d',
      zippedArchive: true
    })
  ]
});
```

### 2.2 配置选项

```ts
new DailyRotateFile({
  filename: 'app-%DATE%.log',
  datePattern: 'YYYY-MM-DD-HH',  // 按小时轮转
  maxSize: '20m',                  // 最大文件大小
  maxFiles: '14d',                 // 保留 14 天
  zippedArchive: true,             // 压缩旧文件
  auditFile: './logs/.audit.json'  // 审计文件
});
```

## 3. Pino 日志轮转

### 3.1 使用 pino-roll

```bash
npm install pino-roll
```

```ts
import pino from 'pino';
import { createWriteStream } from 'pino-roll';

const stream = createWriteStream({
  file: 'app.log',
  size: '20m',
  interval: '1d'
});

const logger = pino(stream);
```

### 3.2 使用 logrotate

```bash
# /etc/logrotate.d/node-app
/path/to/app/logs/*.log {
    daily
    rotate 14
    compress
    delaycompress
    notifempty
    create 0640 app app
    sharedscripts
    postrotate
        killall -USR2 node
    endscript
}
```

## 4. 自定义日志轮转

### 4.1 实现轮转逻辑

```ts
import { createWriteStream, WriteStream } from 'node:fs';
import { stat, rename } from 'node:fs/promises';

class LogRotator {
  private stream: WriteStream;
  private currentSize: number = 0;
  private maxSize: number;
  private filePath: string;
  
  constructor(filePath: string, maxSize: number = 20 * 1024 * 1024) {
    this.filePath = filePath;
    this.maxSize = maxSize;
    this.stream = createWriteStream(filePath, { flags: 'a' });
    this.checkSize();
  }
  
  async write(data: string): Promise<void> {
    this.stream.write(data);
    this.currentSize += Buffer.byteLength(data);
    
    if (this.currentSize >= this.maxSize) {
      await this.rotate();
    }
  }
  
  private async rotate(): Promise<void> {
    this.stream.end();
    
    const timestamp = new Date().toISOString().replace(/:/g, '-');
    const rotatedPath = `${this.filePath}.${timestamp}`;
    
    await rename(this.filePath, rotatedPath);
    
    this.stream = createWriteStream(this.filePath, { flags: 'a' });
    this.currentSize = 0;
  }
  
  private async checkSize(): Promise<void> {
    try {
      const stats = await stat(this.filePath);
      this.currentSize = stats.size;
    } catch (error) {
      // 文件不存在
    }
  }
}
```

## 5. 最佳实践

### 5.1 轮转策略

- 按大小轮转：控制单个文件大小
- 按时间轮转：定期轮转
- 组合策略：大小和时间结合

### 5.2 文件管理

- 压缩旧文件：节省空间
- 定期清理：删除过期文件
- 归档重要日志：长期保存

## 6. 注意事项

- **文件锁定**：处理文件锁定问题
- **性能影响**：注意轮转的性能开销
- **存储空间**：控制日志存储空间
- **备份策略**：重要日志需要备份

## 7. 常见问题

### 7.1 如何选择轮转策略？

根据日志量、存储空间、保留需求选择。

### 7.2 如何处理轮转时的写入？

使用缓冲、异步处理、信号通知。

### 7.3 如何优化轮转性能？

使用异步操作、批量处理、压缩旧文件。

## 8. 实践任务

1. **配置轮转**：配置日志轮转
2. **实现轮转**：实现自定义轮转
3. **文件管理**：管理日志文件
4. **性能优化**：优化轮转性能
5. **持续改进**：持续改进轮转策略

---

**下一节**：[8.5.4 指标监控（Prometheus）](section-04-metrics.md)
