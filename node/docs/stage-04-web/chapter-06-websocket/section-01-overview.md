# 4.6.1 WebSocket 概述

## 1. 概述

WebSocket 是一种在单个 TCP 连接上进行全双工通信的协议，允许服务器和客户端之间进行实时双向数据传输。WebSocket 解决了 HTTP 协议无法实现实时通信的问题。

## 2. 核心概念

### 2.1 WebSocket 协议

WebSocket 协议基于 TCP，通过 HTTP 握手建立连接，然后升级为 WebSocket 协议，实现全双工通信。

### 2.2 WebSocket 特点

- **全双工通信**：客户端和服务器可以同时发送和接收数据
- **低延迟**：相比 HTTP 轮询，延迟更低
- **持久连接**：保持连接，减少握手开销
- **实时性**：支持实时数据传输

## 3. WebSocket vs HTTP

### 3.1 HTTP 轮询

```
客户端 → HTTP 请求 → 服务器
客户端 ← HTTP 响应 ← 服务器
（重复）
```

**缺点**：
- 需要频繁建立连接
- 延迟高
- 服务器负载高

### 3.2 WebSocket

```
客户端 ←→ WebSocket 连接 ←→ 服务器
（持久连接，双向通信）
```

**优点**：
- 持久连接
- 低延迟
- 服务器负载低

## 4. WebSocket 握手

### 4.1 客户端请求

```http
GET /socket.io/?EIO=4&transport=websocket HTTP/1.1
Host: localhost:3000
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
Sec-WebSocket-Version: 13
```

### 4.2 服务器响应

```http
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
```

## 5. WebSocket 消息格式

### 5.1 文本消息

```ts
// 发送文本消息
socket.send('Hello, Server!');

// 接收文本消息
socket.on('message', (message: string): void => {
  console.log('Received:', message);
});
```

### 5.2 二进制消息

```ts
// 发送二进制消息
const buffer = Buffer.from('Hello');
socket.send(buffer);

// 接收二进制消息
socket.on('message', (data: Buffer): void => {
  console.log('Received:', data.toString());
});
```

## 6. WebSocket 状态

### 6.1 连接状态

- **CONNECTING (0)**：连接中
- **OPEN (1)**：已连接
- **CLOSING (2)**：关闭中
- **CLOSED (3)**：已关闭

### 6.2 状态检查

```ts
if (socket.readyState === WebSocket.OPEN) {
  socket.send('Message');
}
```

## 7. WebSocket 事件

### 7.1 客户端事件

- **open**：连接建立
- **message**：接收消息
- **error**：发生错误
- **close**：连接关闭

### 7.2 服务器事件

- **connection**：新连接
- **message**：接收消息
- **close**：连接关闭
- **error**：发生错误

## 8. 适用场景

### 8.1 适合的场景

- **实时聊天**：即时通讯应用
- **实时通知**：推送通知
- **实时协作**：多人协作编辑
- **实时数据**：股票行情、游戏状态

### 8.2 不适合的场景

- **简单请求**：简单的 HTTP 请求即可
- **静态内容**：不需要实时更新的内容
- **低频率更新**：更新频率很低的数据

## 9. 注意事项

- **连接管理**：需要管理连接的生命周期
- **错误处理**：实现完善的错误处理机制
- **安全性**：使用 WSS（WebSocket Secure）
- **扩展性**：考虑多服务器场景

## 10. 常见问题

### 10.1 WebSocket 和 HTTP 的区别？

WebSocket 是持久连接，支持全双工通信；HTTP 是请求-响应模式。

### 10.2 如何处理 WebSocket 连接断开？

实现重连机制，监听 close 事件并重新连接。

### 10.3 WebSocket 是否支持跨域？

支持，但需要在服务器端配置 CORS。

## 11. 相关资源

- [WebSocket 规范](https://tools.ietf.org/html/rfc6455)
- [MDN WebSocket 文档](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)

---

**下一节**：[4.6.2 Socket.io](section-02-socketio.md)
