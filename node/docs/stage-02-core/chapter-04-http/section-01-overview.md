# 2.4.1 HTTP 模块概述

## 1. 概述

HTTP 模块是 Node.js 的核心模块之一，提供了创建 HTTP 服务器和客户端的能力。虽然在实际开发中通常使用 Express、Fastify 等 Web 框架，但理解原生 HTTP 模块的工作原理对于深入理解 Web 开发至关重要。

## 2. 特性说明

- **服务器创建**：可以创建 HTTP 服务器，监听端口并处理请求。
- **客户端功能**：可以发送 HTTP 请求，作为客户端使用。
- **流式处理**：请求和响应都是 Stream，支持流式数据处理。
- **事件驱动**：基于事件系统，通过事件处理请求和响应。
- **低层控制**：提供对 HTTP 协议的底层控制。

## 3. 模块导入方式

### ES Modules 方式

```ts
import http from 'node:http';
import https from 'node:https';
```

### CommonJS 方式

```ts
const http = require('node:http');
const https = require('node:https');
```

## 4. HTTP 协议基础

HTTP（HyperText Transfer Protocol）是用于传输超文本的协议：

| 概念         | 说明                                     |
|:-------------|:-----------------------------------------|
| **请求方法** | GET、POST、PUT、DELETE 等                 |
| **状态码**   | 200（成功）、404（未找到）、500（错误）等 |
| **请求头**   | Content-Type、Authorization 等             |
| **响应头**   | Content-Type、Set-Cookie 等               |
| **请求体**   | POST/PUT 请求的数据                       |
| **响应体**   | 服务器返回的数据                          |

## 5. 参数说明：HTTP 模块常用 API

| API 名称      | 说明                                     | 示例                           |
|:--------------|:-----------------------------------------|:-------------------------------|
| **createServer**| 创建 HTTP 服务器                        | `http.createServer(handler)`   |
| **request**   | 发送 HTTP 请求                           | `http.request(options, callback)`|
| **get**       | 发送 GET 请求（简化版）                   | `http.get(url, callback)`      |

## 6. 返回值与状态说明

HTTP 操作的返回结果：

| 返回类型     | 说明                                     |
|:-------------|:-----------------------------------------|
| **Server**   | HTTP 服务器实例                           |
| **ClientRequest**| HTTP 客户端请求对象                   |
| **IncomingMessage**| HTTP 请求/响应消息对象              |

## 7. 代码示例：最简单的 HTTP 服务器

以下示例演示了如何创建最简单的 HTTP 服务器：

```ts
// 文件: http-simple.ts
// 功能: 最简单的 HTTP 服务器

import http from 'node:http';

const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello, Node.js!');
});

server.listen(3000, () => {
    console.log('Server running at http://localhost:3000');
});
```

## 8. 输出结果说明

访问 `http://localhost:3000` 时的输出：

```text
Hello, Node.js!
```

**逻辑解析**：
- `createServer()` 创建服务器实例
- 回调函数处理每个请求
- `writeHead()` 设置响应头
- `end()` 结束响应并发送数据
- `listen()` 启动服务器监听端口

## 9. 使用场景

### 1. 学习 HTTP 协议

理解 HTTP 协议的工作原理：

```ts
// 学习 HTTP 协议
const server = http.createServer((req, res) => {
    console.log('Method:', req.method);
    console.log('URL:', req.url);
    console.log('Headers:', req.headers);
    res.end('OK');
});
```

### 2. 简单 API 服务器

创建简单的 API 服务器：

```ts
// 简单 API 服务器
const server = http.createServer((req, res) => {
    if (req.url === '/api/users' && req.method === 'GET') {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ users: [] }));
    } else {
        res.writeHead(404);
        res.end('Not Found');
    }
});
```

### 3. 代理服务器

创建代理服务器：

```ts
// 代理服务器
const server = http.createServer((req, res) => {
    const proxyReq = http.request({
        hostname: 'example.com',
        path: req.url,
        method: req.method
    }, (proxyRes) => {
        res.writeHead(proxyRes.statusCode!, proxyRes.headers);
        proxyRes.pipe(res);
    });
    
    req.pipe(proxyReq);
});
```

## 10. 注意事项与常见错误

- **端口占用**：确保端口未被占用
- **错误处理**：处理服务器错误和请求错误
- **请求体解析**：手动解析请求体（使用 Stream）
- **响应头设置**：在发送响应体前设置响应头
- **连接管理**：注意 HTTP 连接的关闭和复用

## 11. 常见问题 (FAQ)

**Q: HTTP 和 HTTPS 有什么区别？**
A: HTTPS 是 HTTP 的安全版本，使用 TLS/SSL 加密。使用 `https` 模块创建 HTTPS 服务器。

**Q: 如何处理 POST 请求的数据？**
A: 通过 `req` 对象（IncomingMessage）读取数据流，手动解析请求体。

**Q: 如何设置 CORS 头？**
A: 在响应头中设置 `Access-Control-Allow-Origin` 等 CORS 相关头。

## 12. 最佳实践

- **使用框架**：实际项目中使用 Express 等框架，简化开发
- **错误处理**：完善的错误处理和日志记录
- **安全考虑**：注意安全头设置（如 Helmet.js）
- **性能优化**：使用连接池、压缩等优化性能
- **理解底层**：理解 HTTP 模块有助于理解 Web 框架

## 13. 对比分析：HTTP 模块 vs Web 框架

| 维度             | HTTP 模块                                  | Web 框架（如 Express）                        |
|:-----------------|:-------------------------------------------|:----------------------------------------------|
| **复杂度**       | 需要手动处理很多细节                        | 提供高级抽象，简化开发                        |
| **控制力**       | 完全控制 HTTP 协议                          | 框架封装，控制力有限                          |
| **学习价值**     | 有助于理解 HTTP 协议                        | 提高开发效率                                  |
| **适用场景**     | 学习、简单服务器、代理                      | 实际项目开发                                  |

## 14. 练习任务

1. **HTTP 服务器实践**：
   - 创建简单的 HTTP 服务器
   - 处理不同的请求方法和路径
   - 返回不同的响应内容

2. **请求处理实践**：
   - 读取请求头信息
   - 处理 GET 和 POST 请求
   - 解析查询字符串

3. **响应处理实践**：
   - 设置不同的响应头
   - 返回 JSON 数据
   - 处理错误响应

4. **实际应用**：
   - 创建简单的 API 服务器
   - 实现路由功能
   - 处理静态文件

完成以上练习后，继续学习下一节：创建 HTTP 服务器。

## 总结

HTTP 模块是 Node.js Web 开发的基础：

- **核心功能**：创建服务器和客户端
- **事件驱动**：基于事件系统处理请求
- **流式处理**：请求和响应使用 Stream
- **学习价值**：理解 HTTP 协议和 Web 框架底层

掌握 HTTP 模块有助于深入理解 Web 开发。

---

**最后更新**：2025-01-XX
