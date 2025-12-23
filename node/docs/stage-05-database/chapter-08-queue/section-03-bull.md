# 5.8.3 Bull/BullMQ（Redis 队列）

## 1. 概述

Bull 和 BullMQ 是基于 Redis 的任务队列库，提供了简单易用的 API 和丰富的功能。Bull/BullMQ 适合轻量级任务队列和基于 Redis 的场景。

## 2. 特性说明

- **基于 Redis**：使用 Redis 作为存储
- **简单易用**：提供简单的 API
- **功能丰富**：支持延迟、重试、优先级等
- **TypeScript 支持**：完整的 TypeScript 支持

## 3. 安装与初始化

### 3.1 安装

```bash
npm install bullmq
npm install ioredis
```

### 3.2 初始化

```ts
import { Queue, Worker, QueueEvents } from 'bullmq';
import { Redis } from 'ioredis';

const connection = new Redis({
  host: 'localhost',
  port: 6379
});

const queue = new Queue('task-queue', { connection });
```

## 4. 基本使用

### 4.1 添加任务

```ts
interface TaskData {
  userId: number;
  email: string;
}

async function addTask(data: TaskData): Promise<void> {
  await queue.add('send-email', data, {
    attempts: 3,
    backoff: {
      type: 'exponential',
      delay: 2000
    }
  });
}
```

### 4.2 处理任务

```ts
const worker = new Worker('task-queue', async (job) => {
  const { userId, email } = job.data as TaskData;
  
  // 处理任务
  await sendEmail(email);
  
  return { success: true };
}, { connection });

worker.on('completed', (job): void => {
  console.log(`Job ${job.id} completed`);
});

worker.on('failed', (job, err): void => {
  console.error(`Job ${job.id} failed:`, err);
});
```

### 4.3 延迟任务

```ts
await queue.add('delayed-task', data, {
  delay: 5000 // 5 秒后执行
});
```

### 4.4 优先级任务

```ts
await queue.add('high-priority-task', data, {
  priority: 10
});

await queue.add('low-priority-task', data, {
  priority: 1
});
```

## 5. 任务管理

### 5.1 任务状态

```ts
// 获取任务
const job = await queue.getJob(jobId);

// 获取任务状态
const state = await job.getState();

// 获取任务结果
const result = await job.returnvalue;
```

### 5.2 任务控制

```ts
// 暂停队列
await queue.pause();

// 恢复队列
await queue.resume();

// 清理任务
await queue.clean(5000, 100, 'completed');
```

## 6. 最佳实践

### 6.1 任务设计

- 保持任务原子性
- 实现幂等性
- 处理任务失败
- 设置合理的重试策略

### 6.2 性能优化

- 使用连接池
- 批量处理任务
- 优化任务处理逻辑
- 监控任务性能

## 7. 注意事项

- **Redis 连接**：合理管理 Redis 连接
- **任务失败**：处理任务失败和重试
- **性能优化**：优化任务处理性能
- **监控**：监控任务队列状态

## 8. 常见问题

### 8.1 如何处理任务失败？

使用重试机制、死信队列、错误处理。

### 8.2 如何优化性能？

使用连接池、批量处理、优化任务逻辑。

### 8.3 如何监控任务队列？

使用队列事件、监控工具、日志记录。

## 9. 实践任务

1. **创建队列**：创建任务队列
2. **添加任务**：实现任务添加功能
3. **处理任务**：实现任务处理逻辑
4. **任务管理**：实现任务管理功能
5. **性能优化**：优化任务处理性能

---

**下一节**：[5.8.4 任务调度（node-cron、agenda）](section-04-scheduling.md)
