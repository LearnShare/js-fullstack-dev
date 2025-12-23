# 4.6.3 ws（原生 WebSocket）

## 1. 概述

ws 是一个轻量级的 WebSocket 库，提供了原生 WebSocket 的实现。ws 库体积小、性能高，适合需要精细控制 WebSocket 连接的场景。

## 2. 特性说明

- **轻量级**：体积小，性能高
- **原生支持**：提供原生 WebSocket API
- **服务器和客户端**：同时支持服务器和客户端
- **扩展性强**：易于扩展和定制

## 3. 安装与初始化

### 3.1 安装

```bash
npm install ws
npm install @types/ws -D
```

### 3.2 服务器端设置

```ts
import { WebSocketServer, WebSocket } from 'ws';
import { createServer } from 'node:http';

const server = createServer();
const wss = new WebSocketServer({ server });

wss.on('connection', (ws: WebSocket, request: Request): void => {
  console.log('Client connected');

  ws.on('message', (message: Buffer): void => {
    console.log('Received:', message.toString());
    ws.send(`Echo: ${message.toString()}`);
  });

  ws.on('close', (): void => {
    console.log('Client disconnected');
  });

  ws.on('error', (error: Error): void => {
    console.error('WebSocket error:', error);
  });
});

server.listen(3000, (): void => {
  console.log('WebSocket server running on port 3000');
});
```

## 4. 基本使用

### 4.1 发送和接收消息

```ts
wss.on('connection', (ws: WebSocket): void => {
  // 发送文本消息
  ws.send('Hello, Client!');

  // 发送二进制消息
  const buffer = Buffer.from('Hello');
  ws.send(buffer);

  // 接收消息
  ws.on('message', (message: Buffer, isBinary: boolean): void => {
    if (isBinary) {
      console.log('Received binary:', message);
    } else {
      console.log('Received text:', message.toString());
    }
  });
});
```

### 4.2 广播消息

```ts
wss.on('connection', (ws: WebSocket): void => {
  ws.on('message', (message: Buffer): void => {
    // 广播给所有客户端
    wss.clients.forEach((client: WebSocket): void => {
      if (client !== ws && client.readyState === WebSocket.OPEN) {
        client.send(message);
      }
    });
  });
});
```

## 5. 连接管理

### 5.1 连接状态

```ts
wss.on('connection', (ws: WebSocket): void => {
  console.log('Ready state:', ws.readyState);
  // 0: CONNECTING
  // 1: OPEN
  // 2: CLOSING
  // 3: CLOSED

  if (ws.readyState === WebSocket.OPEN) {
    ws.send('Connection is open');
  }
});
```

### 5.2 连接信息

```ts
wss.on('connection', (ws: WebSocket, request: Request): void => {
  const url = new URL(request.url || '', `http://${request.headers.host}`);
  const clientIP = request.socket.remoteAddress;
  
  console.log('Client IP:', clientIP);
  console.log('Request URL:', url.pathname);
});
```

## 6. 心跳检测

### 6.1 实现心跳

```ts
wss.on('connection', (ws: WebSocket): void => {
  let isAlive = true;

  ws.on('pong', (): void => {
    isAlive = true;
  });

  const interval = setInterval((): void => {
    if (!isAlive) {
      ws.terminate();
      clearInterval(interval);
      return;
    }

    isAlive = false;
    ws.ping();
  }, 30000);

  ws.on('close', (): void => {
    clearInterval(interval);
  });
});
```

## 7. 错误处理

### 7.1 服务器错误

```ts
wss.on('error', (error: Error): void => {
  console.error('WebSocket server error:', error);
});

wss.on('connection', (ws: WebSocket): void => {
  ws.on('error', (error: Error): void => {
    console.error('WebSocket error:', error);
  });
});
```

### 7.2 客户端错误

```ts
import WebSocket from 'ws';

const ws = new WebSocket('ws://localhost:3000');

ws.on('error', (error: Error): void => {
  console.error('Connection error:', error);
});

ws.on('close', (code: number, reason: Buffer): void => {
  console.log('Connection closed:', code, reason.toString());
});
```

## 8. 认证

### 8.1 Token 认证

```ts
import { verify } from 'jsonwebtoken';

wss.on('connection', (ws: WebSocket, request: Request): void => {
  const token = new URL(request.url || '', `http://${request.headers.host}`).searchParams.get('token');
  
  if (!token) {
    ws.close(1008, 'Authentication required');
    return;
  }

  try {
    const decoded = verify(token, process.env.JWT_SECRET!);
    ws.userId = decoded.userId;
  } catch (error) {
    ws.close(1008, 'Invalid token');
    return;
  }

  console.log('Authenticated user:', ws.userId);
});
```

## 9. 与 Express 集成

### 9.1 Express 集成

```ts
import express, { Express } from 'express';
import { createServer } from 'node:http';
import { WebSocketServer } from 'ws';

const app: Express = express();
const server = createServer(app);
const wss = new WebSocketServer({ server });

wss.on('connection', (ws: WebSocket): void => {
  console.log('Client connected');
});

server.listen(3000, (): void => {
  console.log('Server running on port 3000');
});
```

## 10. 最佳实践

### 10.1 连接管理

- 实现连接池管理
- 处理连接断开
- 限制连接数量

### 10.2 消息处理

- 验证消息格式
- 实现消息队列
- 处理消息顺序

### 10.3 性能优化

- 使用二进制消息
- 实现消息压缩
- 优化内存使用

## 11. 注意事项

- **错误处理**：实现完善的错误处理机制
- **资源管理**：管理连接和内存资源
- **安全性**：实现安全的认证机制
- **扩展性**：考虑多服务器场景

## 12. 常见问题

### 12.1 ws 和 Socket.io 的区别？

ws 是轻量级的原生 WebSocket 实现，Socket.io 提供了更多功能。

### 12.2 如何处理大量连接？

使用负载均衡和连接池管理。

### 12.3 如何实现消息持久化？

使用消息队列或数据库存储消息。

## 13. 实践任务

1. **实现基本 WebSocket 服务器**：使用 ws 实现基本的 WebSocket 服务器
2. **实现心跳检测**：实现 WebSocket 心跳检测机制
3. **实现认证**：实现 WebSocket 认证机制
4. **实现错误处理**：实现完善的错误处理机制
5. **性能优化**：优化 WebSocket 性能

---

**下一节**：[4.6.4 WebSocket 最佳实践](section-04-best-practices.md)
