# 4.6.4 WebSocket 最佳实践

## 1. 概述

WebSocket 最佳实践包括连接管理、消息处理、错误处理、性能优化等方面。遵循最佳实践可以提升 WebSocket 应用的稳定性、性能和可维护性。

## 2. 连接管理

### 2.1 连接池管理

```ts
import { WebSocketServer, WebSocket } from 'ws';

class ConnectionManager {
  private connections: Map<string, WebSocket> = new Map();

  addConnection(id: string, ws: WebSocket): void {
    this.connections.set(id, ws);
    
    ws.on('close', (): void => {
      this.connections.delete(id);
    });
  }

  getConnection(id: string): WebSocket | undefined {
    return this.connections.get(id);
  }

  broadcast(message: string): void {
    this.connections.forEach((ws: WebSocket): void => {
      if (ws.readyState === WebSocket.OPEN) {
        ws.send(message);
      }
    });
  }

  getConnectionCount(): number {
    return this.connections.size;
  }
}

const manager = new ConnectionManager();
```

### 2.2 连接限制

```ts
const MAX_CONNECTIONS = 1000;
let connectionCount = 0;

wss.on('connection', (ws: WebSocket): void => {
  if (connectionCount >= MAX_CONNECTIONS) {
    ws.close(1008, 'Server at capacity');
    return;
  }

  connectionCount++;
  
  ws.on('close', (): void => {
    connectionCount--;
  });
});
```

## 3. 消息处理

### 3.1 消息验证

```ts
interface Message {
  type: string;
  data: unknown;
}

function validateMessage(message: unknown): message is Message {
  return (
    typeof message === 'object' &&
    message !== null &&
    'type' in message &&
    'data' in message &&
    typeof (message as Message).type === 'string'
  );
}

wss.on('connection', (ws: WebSocket): void => {
  ws.on('message', (data: Buffer): void => {
    try {
      const message = JSON.parse(data.toString());
      
      if (!validateMessage(message)) {
        ws.send(JSON.stringify({ error: 'Invalid message format' }));
        return;
      }

      // 处理消息
      handleMessage(ws, message);
    } catch (error) {
      ws.send(JSON.stringify({ error: 'Invalid JSON' }));
    }
  });
});
```

### 3.2 消息队列

```ts
class MessageQueue {
  private queue: Array<{ ws: WebSocket; message: string }> = [];
  private processing = false;

  add(ws: WebSocket, message: string): void {
    this.queue.push({ ws, message });
    this.process();
  }

  private async process(): Promise<void> {
    if (this.processing || this.queue.length === 0) {
      return;
    }

    this.processing = true;

    while (this.queue.length > 0) {
      const { ws, message } = this.queue.shift()!;
      
      if (ws.readyState === WebSocket.OPEN) {
        await this.sendMessage(ws, message);
      }
    }

    this.processing = false;
  }

  private async sendMessage(ws: WebSocket, message: string): Promise<void> {
    return new Promise((resolve): void => {
      ws.send(message, (error?: Error): void => {
        if (error) {
          console.error('Send error:', error);
        }
        resolve();
      });
    });
  }
}
```

## 4. 错误处理

### 4.1 统一错误处理

```ts
class WebSocketError extends Error {
  constructor(
    public code: number,
    message: string
  ) {
    super(message);
    this.name = 'WebSocketError';
  }
}

function handleError(ws: WebSocket, error: Error): void {
  if (error instanceof WebSocketError) {
    ws.close(error.code, error.message);
  } else {
    console.error('Unexpected error:', error);
    ws.close(1011, 'Internal server error');
  }
}

wss.on('connection', (ws: WebSocket): void => {
  ws.on('error', (error: Error): void => {
    handleError(ws, error);
  });
});
```

### 4.2 重连机制

```ts
// 客户端重连
class ReconnectingWebSocket {
  private ws: WebSocket | null = null;
  private url: string;
  private reconnectInterval = 1000;
  private maxReconnectInterval = 30000;
  private reconnectDecay = 1.5;

  constructor(url: string) {
    this.url = url;
    this.connect();
  }

  private connect(): void {
    this.ws = new WebSocket(this.url);

    this.ws.on('open', (): void => {
      this.reconnectInterval = 1000;
    });

    this.ws.on('close', (): void => {
      setTimeout((): void => {
        this.reconnectInterval = Math.min(
          this.reconnectInterval * this.reconnectDecay,
          this.maxReconnectInterval
        );
        this.connect();
      }, this.reconnectInterval);
    });
  }
}
```

## 5. 性能优化

### 5.1 消息压缩

```ts
import { gzip, gunzip } from 'node:zlib';
import { promisify } from 'node:util';

const gzipAsync = promisify(gzip);
const gunzipAsync = promisify(gunzip);

async function sendCompressed(ws: WebSocket, message: string): Promise<void> {
  const compressed = await gzipAsync(Buffer.from(message));
  ws.send(compressed);
}

async function receiveCompressed(data: Buffer): Promise<string> {
  const decompressed = await gunzipAsync(data);
  return decompressed.toString();
}
```

### 5.2 二进制消息

```ts
// 使用二进制消息减少大小
interface Message {
  type: number; // 使用数字代替字符串
  data: Buffer;
}

function encodeMessage(type: number, data: Buffer): Buffer {
  const typeBuffer = Buffer.allocUnsafe(1);
  typeBuffer.writeUInt8(type, 0);
  return Buffer.concat([typeBuffer, data]);
}

function decodeMessage(buffer: Buffer): { type: number; data: Buffer } {
  const type = buffer.readUInt8(0);
  const data = buffer.slice(1);
  return { type, data };
}
```

## 6. 安全性

### 6.1 认证和授权

```ts
import { verify } from 'jsonwebtoken';

wss.on('connection', async (ws: WebSocket, request: Request): Promise<void> => {
  const token = new URL(request.url || '', `http://${request.headers.host}`).searchParams.get('token');
  
  if (!token) {
    ws.close(1008, 'Authentication required');
    return;
  }

  try {
    const decoded = verify(token, process.env.JWT_SECRET!) as { userId: string; role: string };
    ws.userId = decoded.userId;
    ws.role = decoded.role;
  } catch (error) {
    ws.close(1008, 'Invalid token');
    return;
  }

  // 授权检查
  ws.on('message', (data: Buffer): void => {
    const message = JSON.parse(data.toString());
    
    if (message.type === 'admin-action' && ws.role !== 'admin') {
      ws.send(JSON.stringify({ error: 'Unauthorized' }));
      return;
    }

    handleMessage(ws, message);
  });
});
```

### 6.2 速率限制

```ts
class RateLimiter {
  private requests: Map<string, number[]> = new Map();
  private maxRequests: number;
  private windowMs: number;

  constructor(maxRequests: number, windowMs: number) {
    this.maxRequests = maxRequests;
    this.windowMs = windowMs;
  }

  check(identifier: string): boolean {
    const now = Date.now();
    const requests = this.requests.get(identifier) || [];
    const recentRequests = requests.filter((time: number) => now - time < this.windowMs);

    if (recentRequests.length >= this.maxRequests) {
      return false;
    }

    recentRequests.push(now);
    this.requests.set(identifier, recentRequests);
    return true;
  }
}

const rateLimiter = new RateLimiter(100, 60000); // 100 requests per minute

wss.on('connection', (ws: WebSocket, request: Request): void => {
  const clientIP = request.socket.remoteAddress || 'unknown';
  
  ws.on('message', (): void => {
    if (!rateLimiter.check(clientIP)) {
      ws.close(1008, 'Rate limit exceeded');
      return;
    }

    // 处理消息
  });
});
```

## 7. 监控和日志

### 7.1 连接监控

```ts
class WebSocketMonitor {
  private connections: Map<string, { connectedAt: number; messageCount: number }> = new Map();

  addConnection(id: string): void {
    this.connections.set(id, {
      connectedAt: Date.now(),
      messageCount: 0
    });
  }

  incrementMessage(id: string): void {
    const conn = this.connections.get(id);
    if (conn) {
      conn.messageCount++;
    }
  }

  removeConnection(id: string): void {
    this.connections.delete(id);
  }

  getStats(): { total: number; averageAge: number; averageMessages: number } {
    const connections = Array.from(this.connections.values());
    const total = connections.length;
    const averageAge = connections.reduce((sum, conn) => sum + (Date.now() - conn.connectedAt), 0) / total;
    const averageMessages = connections.reduce((sum, conn) => sum + conn.messageCount, 0) / total;

    return { total, averageAge, averageMessages };
  }
}
```

## 8. 最佳实践总结

### 8.1 连接管理

- 实现连接池管理
- 限制连接数量
- 处理连接断开

### 8.2 消息处理

- 验证消息格式
- 实现消息队列
- 处理消息顺序

### 8.3 错误处理

- 统一错误处理
- 实现重连机制
- 记录错误日志

### 8.4 性能优化

- 使用消息压缩
- 使用二进制消息
- 优化内存使用

### 8.5 安全性

- 实现认证和授权
- 实现速率限制
- 使用 WSS

## 9. 注意事项

- **资源管理**：管理连接和内存资源
- **错误处理**：实现完善的错误处理机制
- **安全性**：实现安全的认证和授权
- **监控**：监控连接和性能指标

## 10. 常见问题

### 10.1 如何处理大量连接？

使用连接池管理、负载均衡和 Redis 适配器。

### 10.2 如何实现消息持久化？

使用消息队列或数据库存储消息。

### 10.3 如何优化性能？

使用消息压缩、二进制消息和连接池管理。

## 11. 实践任务

1. **实现连接管理**：实现连接池管理和连接限制
2. **实现消息队列**：实现消息队列处理机制
3. **实现错误处理**：实现统一的错误处理机制
4. **实现性能优化**：优化消息传输和内存使用
5. **实现安全机制**：实现认证、授权和速率限制

---

**下一章**：[4.7 文件上传处理](../chapter-07-file-upload/readme.md)
