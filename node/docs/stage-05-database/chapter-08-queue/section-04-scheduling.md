# 5.8.4 任务调度（node-cron、agenda）

## 1. 概述

任务调度用于在指定时间执行任务，支持定时任务、周期性任务等。node-cron 和 agenda 是 Node.js 中常用的任务调度工具。

## 2. node-cron

### 2.1 安装

```bash
npm install node-cron
npm install @types/node-cron -D
```

### 2.2 基本使用

```ts
import cron from 'node-cron';

// 每分钟执行
cron.schedule('* * * * *', (): void => {
  console.log('Running every minute');
});

// 每天凌晨执行
cron.schedule('0 0 * * *', (): void => {
  console.log('Running daily at midnight');
});

// 每周一执行
cron.schedule('0 0 * * 1', (): void => {
  console.log('Running every Monday');
});
```

### 2.3 高级用法

```ts
// 带时区的任务
cron.schedule('0 0 * * *', (): void => {
  console.log('Running at midnight in Asia/Shanghai');
}, {
  scheduled: true,
  timezone: 'Asia/Shanghai'
});

// 启动和停止
const task = cron.schedule('* * * * *', (): void => {
  console.log('Running');
});

task.start();
task.stop();
```

## 3. agenda

### 3.1 安装

```bash
npm install agenda
```

### 3.2 基本使用

```ts
import Agenda from 'agenda';
import { MongoClient } from 'mongodb';

const mongoClient = new MongoClient(process.env.MONGODB_URI!);
await mongoClient.connect();

const agenda = new Agenda({
  mongo: mongoClient.db('agenda')
});

// 定义任务
agenda.define('send email', async (job): Promise<void> => {
  const { to, subject, body } = job.attrs.data;
  await sendEmail(to, subject, body);
});

// 调度任务
await agenda.start();
await agenda.every('1 minute', 'send email', { to: 'user@example.com' });

// 一次性任务
await agenda.schedule('in 1 hour', 'send email', { to: 'user@example.com' });
```

## 4. 最佳实践

### 4.1 任务设计

- 保持任务简单
- 实现错误处理
- 记录任务日志
- 避免长时间任务

### 4.2 调度管理

- 合理设置调度时间
- 处理任务冲突
- 监控任务执行
- 实现任务重试

## 5. 注意事项

- **时区处理**：注意时区问题
- **任务冲突**：处理任务冲突
- **错误处理**：实现完善的错误处理
- **性能影响**：注意任务对性能的影响

## 6. 常见问题

### 6.1 如何处理时区？

使用时区配置，统一使用 UTC 时间。

### 6.2 如何处理任务失败？

实现错误处理和重试机制。

### 6.3 如何监控任务？

使用日志记录、监控工具、任务状态跟踪。

## 7. 实践任务

1. **定时任务**：实现定时任务功能
2. **周期性任务**：实现周期性任务
3. **任务管理**：实现任务管理功能
4. **错误处理**：实现完善的错误处理
5. **监控**：实现任务监控功能

---

**下一章**：[5.9 数据库连接池](../chapter-09-connection-pool/readme.md)
