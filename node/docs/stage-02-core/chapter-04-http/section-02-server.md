# 2.4.2 创建 HTTP 服务器

## 1. 概述

创建 HTTP 服务器是使用 HTTP 模块的核心功能。通过 `http.createServer()` 方法可以创建一个 HTTP 服务器实例，监听指定端口并处理客户端请求。理解如何创建和配置 HTTP 服务器是 Web 开发的基础。

## 2. 特性说明

- **服务器创建**：使用 `createServer()` 创建服务器实例。
- **端口监听**：使用 `listen()` 方法监听指定端口。
- **请求处理**：通过回调函数处理每个请求。
- **事件监听**：可以监听服务器事件（如错误、连接等）。
- **配置选项**：支持多种服务器配置选项。

## 3. 语法与定义

### 创建服务器

```ts
// 创建 HTTP 服务器
http.createServer(requestListener?: RequestListener): Server

// 监听端口
server.listen(port?: number, hostname?: string, backlog?: number, listeningListener?: () => void): Server
```

### 请求监听器类型

```ts
type RequestListener = (req: IncomingMessage, res: ServerResponse) => void;
```

## 4. 基本用法

### 示例 1：基本服务器

```ts
// 文件: http-server-basic.ts
// 功能: 基本 HTTP 服务器

import http from 'node:http';

const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello, World!');
});

server.listen(3000, () => {
    console.log('Server running at http://localhost:3000');
});
```

### 示例 2：带错误处理的服务器

```ts
// 文件: http-server-error.ts
// 功能: 带错误处理的 HTTP 服务器

import http from 'node:http';

const server = http.createServer((req, res) => {
    try {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end('Hello, World!');
    } catch (error) {
        res.writeHead(500, { 'Content-Type': 'text/plain' });
        res.end('Internal Server Error');
    }
});

server.on('error', (error: NodeJS.ErrnoException) => {
    if (error.code === 'EADDRINUSE') {
        console.error('Port 3000 is already in use');
    } else {
        console.error('Server error:', error);
    }
});

server.listen(3000, () => {
    console.log('Server running at http://localhost:3000');
});
```

### 示例 3：路由处理

```ts
// 文件: http-server-routing.ts
// 功能: 带路由的 HTTP 服务器

import http from 'node:http';
import { URL } from 'node:url';

const server = http.createServer((req, res) => {
    const url = new URL(req.url || '/', `http://${req.headers.host}`);
    const pathname = url.pathname;
    
    if (pathname === '/') {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end('<h1>Home</h1>');
    } else if (pathname === '/about') {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end('<h1>About</h1>');
    } else if (pathname === '/api/data') {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ message: 'Hello, API!' }));
    } else {
        res.writeHead(404, { 'Content-Type': 'text/html' });
        res.end('<h1>404 Not Found</h1>');
    }
});

server.listen(3000, () => {
    console.log('Server running at http://localhost:3000');
});
```

## 5. 参数说明：createServer 和 listen

### createServer 参数

| 参数名           | 类型             | 说明                                     | 示例                           |
|:-----------------|:-----------------|:-----------------------------------------|:-------------------------------|
| **requestListener**| RequestListener | 请求处理回调函数（可选）。               | `(req, res) => {}`            |

### listen 参数

| 参数名           | 类型     | 说明                                     | 示例                           |
|:-----------------|:---------|:-----------------------------------------|:-------------------------------|
| **port**         | Number   | 监听端口号。                             | `3000`                         |
| **hostname**     | String   | 主机名（可选）。                         | `'localhost'`                  |
| **backlog**      | Number   | 最大等待连接数（可选）。                 | `511`                          |
| **listeningListener**| Function | 监听成功回调（可选）。                 | `() => console.log('Listening')`|

## 6. 返回值与状态说明

### createServer 返回值

| 返回类型 | 说明                                     |
|:---------|:-----------------------------------------|
| **Server**| HTTP 服务器实例。                        |

### 服务器事件

| 事件名称     | 说明                                     |
|:-------------|:-----------------------------------------|
| **'request'**| 收到请求时触发。                         |
| **'error'**  | 发生错误时触发。                         |
| **'listening'**| 服务器开始监听时触发。                   |
| **'close'**  | 服务器关闭时触发。                       |

## 7. 代码示例：完整服务器配置

以下示例演示了如何配置一个完整的 HTTP 服务器：

```ts
// 文件: http-server-complete.ts
// 功能: 完整的 HTTP 服务器配置

import http from 'node:http';

const server = http.createServer((req, res) => {
    // 设置 CORS 头
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
    
    // 处理 OPTIONS 预检请求
    if (req.method === 'OPTIONS') {
        res.writeHead(200);
        res.end();
        return;
    }
    
    // 处理请求
    if (req.method === 'GET' && req.url === '/api/hello') {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ message: 'Hello, API!' }));
    } else {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('Not Found');
    }
});

// 错误处理
server.on('error', (error: NodeJS.ErrnoException) => {
    console.error('Server error:', error);
});

// 监听成功
server.on('listening', () => {
    const address = server.address();
    console.log(`Server listening on ${address?.address}:${address?.port}`);
});

// 启动服务器
const PORT = process.env.PORT || 3000;
server.listen(PORT, '0.0.0.0', () => {
    console.log(`Server running on port ${PORT}`);
});
```

## 8. 输出结果说明

服务器启动时的输出：

```text
Server listening on 0.0.0.0:3000
Server running on port 3000
```

访问 `/api/hello` 时的响应：

```json
{"message":"Hello, API!"}
```

**逻辑解析**：
- 服务器监听所有网络接口（0.0.0.0）
- 处理 CORS 预检请求
- 根据请求方法和路径返回不同响应

## 9. 使用场景

### 1. 开发测试服务器

创建简单的开发测试服务器：

```ts
// 开发测试服务器
const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ status: 'ok' }));
});

server.listen(3000);
```

### 2. 静态文件服务器

创建简单的静态文件服务器：

```ts
// 静态文件服务器
import fsPromises from 'node:fs/promises';
import path from 'node:path';

const server = http.createServer(async (req, res) => {
    const filePath = path.join(__dirname, 'public', req.url || '/');
    try {
        const content = await fsPromises.readFile(filePath);
        res.writeHead(200);
        res.end(content);
    } catch {
        res.writeHead(404);
        res.end('File Not Found');
    }
});
```

### 3. API 网关

创建简单的 API 网关：

```ts
// API 网关
const server = http.createServer((req, res) => {
    // 路由到不同的后端服务
    const target = determineTarget(req.url);
    proxyRequest(req, res, target);
});
```

## 10. 注意事项与常见错误

- **端口占用**：确保端口未被占用，处理 `EADDRINUSE` 错误
- **响应头顺序**：在调用 `writeHead()` 后再设置响应头
- **错误处理**：处理服务器错误和请求处理错误
- **连接管理**：注意 HTTP 连接的关闭和复用
- **安全考虑**：设置适当的安全头（CORS、CSP 等）

## 11. 常见问题 (FAQ)

**Q: 如何停止服务器？**
A: 调用 `server.close()` 方法停止服务器。

**Q: 如何处理端口已被占用？**
A: 检查错误码 `EADDRINUSE`，尝试使用其他端口或关闭占用端口的进程。

**Q: 如何获取服务器监听的地址？**
A: 使用 `server.address()` 方法获取服务器地址信息。

## 12. 最佳实践

- **错误处理**：完善的错误处理和日志记录
- **配置管理**：使用环境变量管理端口等配置
- **安全头设置**：设置适当的安全响应头
- **性能优化**：使用连接池、压缩等优化性能
- **代码组织**：将路由处理逻辑分离到独立模块

## 13. 对比分析：原生 HTTP vs Web 框架

| 维度             | 原生 HTTP 模块                            | Web 框架（如 Express）                    |
|:-----------------|:------------------------------------------|:------------------------------------------|
| **路由处理**     | 需要手动实现                               | 提供路由系统                              |
| **中间件**       | 需要手动实现                               | 提供中间件系统                            |
| **请求解析**     | 需要手动解析                               | 自动解析请求体                            |
| **代码量**       | 代码量较大                                 | 代码简洁                                  |
| **学习价值**     | 有助于理解底层原理                         | 提高开发效率                              |

## 14. 练习任务

1. **服务器创建实践**：
   - 创建基本的 HTTP 服务器
   - 处理不同的请求路径
   - 返回不同类型的响应

2. **错误处理实践**：
   - 处理端口占用错误
   - 处理请求处理错误
   - 实现错误日志记录

3. **路由实现实践**：
   - 实现简单的路由系统
   - 处理不同的 HTTP 方法
   - 实现参数解析

4. **实际应用**：
   - 创建简单的 API 服务器
   - 实现静态文件服务
   - 添加安全头设置

完成以上练习后，继续学习下一节：处理请求与响应。

## 总结

创建 HTTP 服务器是 Web 开发的基础：

- **核心方法**：`createServer()` 和 `listen()`
- **请求处理**：通过回调函数处理请求
- **事件系统**：监听服务器事件
- **最佳实践**：错误处理、配置管理、安全考虑

掌握 HTTP 服务器创建有助于理解 Web 开发原理。

---

**最后更新**：2025-01-XX
