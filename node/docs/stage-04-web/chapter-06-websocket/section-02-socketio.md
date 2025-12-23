# 4.6.2 Socket.io

## 1. 概述

Socket.io 是一个基于 WebSocket 的实时通信库，提供了自动重连、房间、命名空间等功能。Socket.io 兼容多种传输方式，包括 WebSocket、轮询等，提供了更好的兼容性和开发体验。

## 2. 特性说明

- **自动重连**：连接断开时自动重连
- **房间支持**：支持房间和命名空间
- **多传输支持**：支持 WebSocket、轮询等多种传输方式
- **事件系统**：基于事件的通信模型
- **类型安全**：支持 TypeScript

## 3. 安装与初始化

### 3.1 安装

```bash
npm install socket.io
npm install @types/socket.io -D
```

### 3.2 服务器端设置

```ts
import { createServer } from 'node:http';
import { Server, Socket } from 'socket.io';

const httpServer = createServer();
const io = new Server(httpServer, {
  cors: {
    origin: 'http://localhost:3000',
    methods: ['GET', 'POST']
  }
});

io.on('connection', (socket: Socket): void => {
  console.log('Client connected:', socket.id);

  socket.on('disconnect', (): void => {
    console.log('Client disconnected:', socket.id);
  });
});

httpServer.listen(3000, (): void => {
  console.log('Socket.io server running on port 3000');
});
```

### 3.3 与 Express 集成

```ts
import express, { Express } from 'express';
import { createServer } from 'node:http';
import { Server, Socket } from 'socket.io';

const app: Express = express();
const httpServer = createServer(app);
const io = new Server(httpServer);

io.on('connection', (socket: Socket): void => {
  console.log('Client connected:', socket.id);
});

httpServer.listen(3000, (): void => {
  console.log('Server running on port 3000');
});
```

## 4. 基本使用

### 4.1 发送和接收消息

```ts
// 服务器端
io.on('connection', (socket: Socket): void => {
  // 接收消息
  socket.on('message', (data: { text: string }): void => {
    console.log('Received:', data.text);
    
    // 发送消息给客户端
    socket.emit('message', { text: 'Hello from server' });
  });

  // 广播消息给所有客户端
  socket.on('broadcast', (data: { text: string }): void => {
    io.emit('message', data);
  });
});
```

### 4.2 客户端连接

```ts
// 客户端
import { io, Socket } from 'socket.io-client';

const socket: Socket = io('http://localhost:3000');

socket.on('connect', (): void => {
  console.log('Connected to server');
  
  // 发送消息
  socket.emit('message', { text: 'Hello from client' });
});

socket.on('message', (data: { text: string }): void => {
  console.log('Received:', data.text);
});

socket.on('disconnect', (): void => {
  console.log('Disconnected from server');
});
```

## 5. 房间和命名空间

### 5.1 房间

```ts
// 加入房间
socket.on('join-room', (roomId: string): void => {
  socket.join(roomId);
  console.log(`Socket ${socket.id} joined room ${roomId}`);
});

// 向房间发送消息
socket.on('room-message', (data: { roomId: string; text: string }): void => {
  io.to(data.roomId).emit('message', { text: data.text });
});

// 离开房间
socket.on('leave-room', (roomId: string): void => {
  socket.leave(roomId);
  console.log(`Socket ${socket.id} left room ${roomId}`);
});
```

### 5.2 命名空间

```ts
// 创建命名空间
const adminNamespace = io.of('/admin');

adminNamespace.on('connection', (socket: Socket): void => {
  console.log('Admin connected:', socket.id);
  
  socket.on('admin-message', (data: { text: string }): void => {
    adminNamespace.emit('message', data);
  });
});

// 客户端连接命名空间
const adminSocket = io('http://localhost:3000/admin');
```

## 6. 中间件

### 6.1 认证中间件

```ts
io.use((socket: Socket, next: (err?: Error) => void): void => {
  const token = socket.handshake.auth.token;
  
  if (!token || !isValidToken(token)) {
    return next(new Error('Authentication error'));
  }
  
  socket.data.user = getUserFromToken(token);
  next();
});

io.on('connection', (socket: Socket): void => {
  const user = socket.data.user;
  console.log('User connected:', user.id);
});
```

### 6.2 日志中间件

```ts
io.use((socket: Socket, next: (err?: Error) => void): void => {
  console.log('Connection attempt from:', socket.handshake.address);
  next();
});
```

## 7. 错误处理

### 7.1 服务器端错误处理

```ts
io.on('connection', (socket: Socket): void => {
  socket.on('error', (error: Error): void => {
    console.error('Socket error:', error);
  });

  socket.on('disconnect', (reason: string): void => {
    console.log('Disconnect reason:', reason);
  });
});
```

### 7.2 客户端错误处理

```ts
socket.on('connect_error', (error: Error): void => {
  console.error('Connection error:', error);
});

socket.on('disconnect', (reason: string): void => {
  if (reason === 'io server disconnect') {
    // 服务器主动断开，需要手动重连
    socket.connect();
  }
});
```

## 8. 最佳实践

### 8.1 连接管理

- 实现连接池管理
- 处理连接断开和重连
- 限制连接数量

### 8.2 消息处理

- 验证消息格式
- 实现消息队列
- 处理消息顺序

### 8.3 性能优化

- 使用房间减少广播范围
- 实现消息压缩
- 使用二进制消息

## 9. 注意事项

- **CORS 配置**：正确配置 CORS
- **认证安全**：实现安全的认证机制
- **资源管理**：管理连接和内存资源
- **错误处理**：实现完善的错误处理

## 10. 常见问题

### 10.1 如何处理大量连接？

使用 Redis 适配器实现多服务器支持，使用负载均衡。

### 10.2 如何实现消息持久化？

使用消息队列或数据库存储消息。

### 10.3 Socket.io 和原生 WebSocket 的区别？

Socket.io 提供了更多功能，如自动重连、房间、命名空间等。

## 11. 实践任务

1. **实现基本聊天**：实现基本的实时聊天功能
2. **实现房间功能**：实现房间加入和离开功能
3. **实现认证**：实现 Socket.io 认证机制
4. **实现错误处理**：实现完善的错误处理机制
5. **性能优化**：优化 Socket.io 性能

---

**下一节**：[4.6.3 ws（原生 WebSocket）](section-03-ws.md)
