# 5.8.2 RabbitMQ

## 1. 概述

RabbitMQ 是一个功能丰富的消息队列系统，支持多种消息协议，提供了可靠的消息传递和丰富的功能。RabbitMQ 适合企业级应用和复杂的消息处理场景。

## 2. 特性说明

- **多种协议**：支持 AMQP、MQTT、STOMP 等
- **可靠性**：保证消息可靠传递
- **路由灵活**：支持多种路由模式
- **管理界面**：提供 Web 管理界面

## 3. 安装与连接

### 3.1 安装

```bash
# macOS
brew install rabbitmq

# Ubuntu
sudo apt-get install rabbitmq-server

# Windows
# 下载安装包从官网安装
```

### 3.2 Node.js 连接

```bash
npm install amqplib
npm install @types/amqplib -D
```

```ts
import amqp, { Connection, Channel } from 'amqplib';

async function connectRabbitMQ(): Promise<Connection> {
  const connection = await amqp.connect('amqp://localhost');
  return connection;
}

async function createChannel(connection: Connection): Promise<Channel> {
  return await connection.createChannel();
}
```

## 4. 基本使用

### 4.1 工作队列

```ts
// 生产者
async function sendMessage(queue: string, message: string): Promise<void> {
  const connection = await connectRabbitMQ();
  const channel = await createChannel(connection);
  
  await channel.assertQueue(queue, { durable: true });
  channel.sendToQueue(queue, Buffer.from(message), { persistent: true });
  
  await channel.close();
  await connection.close();
}

// 消费者
async function consumeMessage(queue: string, callback: (msg: string) => Promise<void>): Promise<void> {
  const connection = await connectRabbitMQ();
  const channel = await createChannel(connection);
  
  await channel.assertQueue(queue, { durable: true });
  channel.prefetch(1); // 每次只处理一个消息
  
  channel.consume(queue, async (msg) => {
    if (msg) {
      const content = msg.content.toString();
      await callback(content);
      channel.ack(msg);
    }
  });
}
```

### 4.2 发布订阅

```ts
// 发布者
async function publishMessage(exchange: string, routingKey: string, message: string): Promise<void> {
  const connection = await connectRabbitMQ();
  const channel = await createChannel(connection);
  
  await channel.assertExchange(exchange, 'topic', { durable: true });
  channel.publish(exchange, routingKey, Buffer.from(message));
  
  await channel.close();
  await connection.close();
}

// 订阅者
async function subscribeMessage(exchange: string, routingKey: string, callback: (msg: string) => Promise<void>): Promise<void> {
  const connection = await connectRabbitMQ();
  const channel = await createChannel(connection);
  
  await channel.assertExchange(exchange, 'topic', { durable: true });
  const queue = await channel.assertQueue('', { exclusive: true });
  await channel.bindQueue(queue.queue, exchange, routingKey);
  
  channel.consume(queue.queue, async (msg) => {
    if (msg) {
      const content = msg.content.toString();
      await callback(content);
      channel.ack(msg);
    }
  });
}
```

## 5. 最佳实践

### 5.1 消息确认

- 使用消息确认机制
- 处理消息失败
- 实现重试机制

### 5.2 连接管理

- 使用连接池
- 处理连接错误
- 实现重连机制

## 6. 注意事项

- **消息可靠性**：使用持久化和确认机制
- **连接管理**：合理管理连接和通道
- **错误处理**：实现完善的错误处理
- **性能优化**：优化消息处理性能

## 7. 常见问题

### 7.1 如何保证消息可靠性？

使用持久化、消息确认、重试机制。

### 7.2 如何处理消息失败？

实现重试机制、死信队列。

### 7.3 如何优化性能？

使用连接池、批量处理、优化消息大小。

## 8. 实践任务

1. **连接 RabbitMQ**：建立 RabbitMQ 连接
2. **工作队列**：实现工作队列
3. **发布订阅**：实现发布订阅
4. **消息确认**：实现消息确认机制
5. **错误处理**：实现完善的错误处理

---

**下一节**：[5.8.3 Bull/BullMQ（Redis 队列）](section-03-bull.md)
