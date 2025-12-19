# 2.4.3 处理请求与响应

## 1. 概述

处理 HTTP 请求和响应是 HTTP 服务器的核心功能。理解如何读取请求信息、解析请求数据、构建响应内容，是掌握 HTTP 模块的关键。本章详细介绍请求对象（IncomingMessage）和响应对象（ServerResponse）的使用。

## 2. 特性说明

- **请求信息读取**：读取请求方法、URL、请求头等信息。
- **请求体解析**：解析 POST/PUT 请求的请求体数据。
- **响应头设置**：设置响应状态码和响应头。
- **响应体发送**：发送响应数据（文本、JSON、文件等）。
- **流式处理**：请求和响应都支持流式数据处理。

## 3. 语法与定义

### 请求对象（IncomingMessage）

```ts
interface IncomingMessage extends stream.Readable {
    method?: string;
    url?: string;
    headers: IncomingHttpHeaders;
    statusCode?: number;
    statusMessage?: string;
}
```

### 响应对象（ServerResponse）

```ts
interface ServerResponse extends stream.Writable {
    statusCode: number;
    statusMessage: string;
    writeHead(statusCode: number, headers?: OutgoingHttpHeaders): void;
    setHeader(name: string, value: string | number | string[]): void;
    getHeader(name: string): string | number | string[] | undefined;
    end(chunk?: any, encoding?: string, callback?: () => void): void;
}
```

## 4. 基本用法

### 示例 1：读取请求信息

```ts
// 文件: http-request-info.ts
// 功能: 读取请求信息

import http from 'node:http';

const server = http.createServer((req, res) => {
    // 请求方法
    console.log('Method:', req.method);
    
    // 请求 URL
    console.log('URL:', req.url);
    
    // 请求头
    console.log('Headers:', req.headers);
    
    // 用户代理
    console.log('User-Agent:', req.headers['user-agent']);
    
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Request info logged');
});

server.listen(3000);
```

### 示例 2：解析查询字符串

```ts
// 文件: http-query-string.ts
// 功能: 解析查询字符串

import http from 'node:http';
import { URL } from 'node:url';

const server = http.createServer((req, res) => {
    if (!req.url) {
        res.writeHead(400);
        res.end('Bad Request');
        return;
    }
    
    const url = new URL(req.url, `http://${req.headers.host}`);
    const params = Object.fromEntries(url.searchParams);
    
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify(params));
});

server.listen(3000);
```

### 示例 3：处理 POST 请求体

```ts
// 文件: http-post-body.ts
// 功能: 处理 POST 请求体

import http from 'node:http';

const server = http.createServer((req, res) => {
    if (req.method !== 'POST') {
        res.writeHead(405, { 'Content-Type': 'text/plain' });
        res.end('Method Not Allowed');
        return;
    }
    
    let body = '';
    
    // 读取请求体
    req.on('data', (chunk) => {
        body += chunk.toString();
    });
    
    req.on('end', () => {
        try {
            const data = JSON.parse(body);
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ received: data }));
        } catch (error) {
            res.writeHead(400, { 'Content-Type': 'text/plain' });
            res.end('Invalid JSON');
        }
    });
    
    req.on('error', (error) => {
        res.writeHead(500, { 'Content-Type': 'text/plain' });
        res.end('Internal Server Error');
    });
});

server.listen(3000);
```

## 5. 参数说明：请求和响应方法

### 请求对象常用属性

| 属性名       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **method**   | String   | HTTP 请求方法                            | `'GET'`, `'POST'`              |
| **url**      | String   | 请求 URL                                 | `'/api/users?id=1'`             |
| **headers**  | Object   | 请求头对象                               | `{ 'content-type': 'application/json' }`|
| **statusCode**| Number  | 响应状态码（客户端请求时）               | `200`, `404`                    |

### 响应对象常用方法

| 方法名       | 说明                                     | 示例                           |
|:-------------|:-----------------------------------------|:-------------------------------|
| **writeHead**| 设置响应状态码和头                        | `res.writeHead(200, headers)`  |
| **setHeader**| 设置单个响应头                            | `res.setHeader('Content-Type', 'application/json')`|
| **write**    | 写入响应数据                              | `res.write('data')`            |
| **end**      | 结束响应并发送数据                        | `res.end('data')`              |

## 6. 返回值与状态说明

### 请求处理返回值

| 返回类型     | 说明                                     |
|:-------------|:-----------------------------------------|
| **数据流**   | 请求体是 Readable Stream                  |
| **错误事件** | 请求处理错误时触发 error 事件            |

### 响应发送返回值

| 返回类型     | 说明                                     |
|:-------------|:-----------------------------------------|
| **布尔值**   | `write()` 返回是否成功写入                |
| **void**     | `end()` 无返回值，结束响应                |

## 7. 代码示例：完整的请求响应处理

以下示例演示了如何完整处理请求和响应：

```ts
// 文件: http-complete-handler.ts
// 功能: 完整的请求响应处理

import http from 'node:http';
import { URL } from 'node:url';

const server = http.createServer((req, res) => {
    // 解析 URL
    if (!req.url) {
        res.writeHead(400);
        res.end('Bad Request');
        return;
    }
    
    const url = new URL(req.url, `http://${req.headers.host}`);
    const pathname = url.pathname;
    
    // 处理不同的请求方法
    if (req.method === 'GET') {
        handleGet(req, res, pathname, url);
    } else if (req.method === 'POST') {
        handlePost(req, res, pathname);
    } else {
        res.writeHead(405, { 'Content-Type': 'text/plain' });
        res.end('Method Not Allowed');
    }
});

function handleGet(req: http.IncomingMessage, res: http.ServerResponse, pathname: string, url: URL) {
    if (pathname === '/api/users') {
        const id = url.searchParams.get('id');
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ id, name: 'User' }));
    } else {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('Not Found');
    }
}

function handlePost(req: http.IncomingMessage, res: http.ServerResponse, pathname: string) {
    if (pathname === '/api/users') {
        let body = '';
        
        req.on('data', (chunk) => {
            body += chunk.toString();
        });
        
        req.on('end', () => {
            try {
                const data = JSON.parse(body);
                res.writeHead(201, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ created: data }));
            } catch {
                res.writeHead(400, { 'Content-Type': 'text/plain' });
                res.end('Invalid JSON');
            }
        });
    } else {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('Not Found');
    }
}

server.listen(3000, () => {
    console.log('Server running at http://localhost:3000');
});
```

## 8. 输出结果说明

GET 请求 `/api/users?id=1` 的响应：

```json
{"id":"1","name":"User"}
```

POST 请求 `/api/users` 的响应：

```json
{"created":{"name":"Alice","age":25}}
```

**逻辑解析**：
- GET 请求：从查询字符串获取参数
- POST 请求：从请求体读取 JSON 数据
- 根据路径和方法返回不同响应

## 9. 使用场景

### 1. RESTful API

实现 RESTful API：

```ts
// RESTful API 示例
const server = http.createServer((req, res) => {
    const method = req.method;
    const url = new URL(req.url || '/', `http://${req.headers.host}`);
    
    if (method === 'GET' && url.pathname === '/api/users') {
        // 获取用户列表
    } else if (method === 'POST' && url.pathname === '/api/users') {
        // 创建用户
    } else if (method === 'PUT' && url.pathname.startsWith('/api/users/')) {
        // 更新用户
    } else if (method === 'DELETE' && url.pathname.startsWith('/api/users/')) {
        // 删除用户
    }
});
```

### 2. 文件上传

处理文件上传：

```ts
// 文件上传示例
import fsPromises from 'node:fs/promises';

const server = http.createServer((req, res) => {
    if (req.method === 'POST' && req.url === '/upload') {
        const writeStream = fsPromises.createWriteStream('./uploaded-file');
        req.pipe(writeStream);
        
        req.on('end', () => {
            res.writeHead(200);
            res.end('File uploaded');
        });
    }
});
```

### 3. 流式响应

发送流式响应：

```ts
// 流式响应示例
import fs from 'node:fs';

const server = http.createServer((req, res) => {
    if (req.url === '/stream') {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        const readStream = fs.createReadStream('./large-file.txt');
        readStream.pipe(res);
    }
});
```

## 10. 注意事项与常见错误

- **响应头顺序**：在调用 `writeHead()` 后再调用 `setHeader()` 会报错
- **请求体读取**：请求体是 Stream，需要监听 data 事件读取
- **错误处理**：处理请求和响应过程中的错误
- **数据编码**：注意数据的编码格式（UTF-8、Buffer 等）
- **连接关闭**：确保响应正确结束，避免连接泄漏

## 11. 常见问题 (FAQ)

**Q: 如何获取 POST 请求的 JSON 数据？**
A: 监听 `data` 事件收集数据，在 `end` 事件中解析 JSON。

**Q: 如何设置响应状态码？**
A: 使用 `writeHead(statusCode)` 或设置 `res.statusCode` 属性。

**Q: 如何发送文件？**
A: 使用 `fs.createReadStream()` 创建文件流，通过 `pipe()` 发送到响应。

## 12. 最佳实践

- **错误处理**：完善的错误处理和日志记录
- **数据验证**：验证请求数据的格式和内容
- **响应头设置**：设置适当的响应头（Content-Type、CORS 等）
- **流式处理**：处理大文件时使用流式处理
- **代码组织**：将请求处理逻辑分离到独立函数

## 13. 对比分析：请求处理方式

| 方式           | 特点                                     | 适用场景                       |
|:---------------|:-----------------------------------------|:-------------------------------|
| **事件监听**   | 流式处理，适合大文件                      | 文件上传、流式数据             |
| **一次性读取** | 简单直接，适合小数据                      | JSON 数据、表单数据            |
| **管道处理**   | 高效，零拷贝                              | 文件传输、代理转发             |

## 14. 练习任务

1. **请求信息读取实践**：
   - 读取请求方法、URL、请求头
   - 解析查询字符串
   - 获取客户端信息

2. **请求体处理实践**：
   - 处理 POST 请求的 JSON 数据
   - 处理表单数据
   - 处理文件上传

3. **响应构建实践**：
   - 设置不同的响应状态码
   - 返回 JSON 数据
   - 发送文件内容

4. **实际应用**：
   - 实现简单的 RESTful API
   - 处理文件上传
   - 实现流式响应

完成以上练习后，继续学习下一节：HTTP 客户端。

## 总结

处理请求与响应是 HTTP 服务器的核心：

- **请求对象**：读取请求方法、URL、请求头、请求体
- **响应对象**：设置状态码、响应头、发送响应数据
- **流式处理**：请求和响应都支持流式数据处理
- **最佳实践**：错误处理、数据验证、响应头设置

掌握请求响应处理有助于构建功能完整的 Web 服务器。

---

**最后更新**：2025-01-XX
