# 4.1.2 HTTP 协议详解

## 1. 概述

HTTP 协议是 Web 应用的基础，理解 HTTP 协议的详细工作原理对于构建高质量的 Web 服务至关重要。本节深入介绍 HTTP 协议的请求和响应结构、头部字段、状态码、缓存机制、连接管理等内容。

## 2. HTTP 请求详解

### 2.1 请求结构

HTTP 请求由以下部分组成：

```
请求行
请求头（多行）
空行
请求体（可选）
```

### 2.2 请求行

请求行包含三个部分：

- **HTTP 方法**：GET、POST、PUT、DELETE 等
- **请求 URI**：资源的路径和查询参数
- **HTTP 版本**：HTTP/1.1 或 HTTP/2

**示例**：

```http
GET /api/users?page=1 HTTP/1.1
```

### 2.3 请求头

请求头包含元数据信息，常见请求头包括：

| 请求头              | 说明                           | 示例                           |
|:--------------------|:-------------------------------|:-------------------------------|
| **Host**            | 服务器主机名和端口             | `Host: api.example.com`       |
| **User-Agent**      | 客户端信息                     | `User-Agent: Mozilla/5.0...`  |
| **Accept**          | 接受的媒体类型                 | `Accept: application/json`     |
| **Accept-Language** | 接受的语言                     | `Accept-Language: zh-CN,en`    |
| **Content-Type**    | 请求体的媒体类型               | `Content-Type: application/json` |
| **Content-Length**  | 请求体的长度（字节）           | `Content-Length: 1024`         |
| **Authorization**   | 认证信息                       | `Authorization: Bearer token` |
| **Cookie**          | 客户端 Cookie                  | `Cookie: session=abc123`      |
| **Referer**         | 来源页面                       | `Referer: https://example.com` |
| **Origin**          | 请求来源（用于 CORS）          | `Origin: https://example.com`  |

### 2.4 请求体

请求体包含实际的数据，常见格式包括：

- **JSON**：`Content-Type: application/json`
- **表单数据**：`Content-Type: application/x-www-form-urlencoded`
- **多部分表单**：`Content-Type: multipart/form-data`
- **XML**：`Content-Type: application/xml`
- **文本**：`Content-Type: text/plain`

**示例**：

```http
POST /api/users HTTP/1.1
Host: api.example.com
Content-Type: application/json
Content-Length: 45

{"name":"John","email":"john@example.com"}
```

## 3. HTTP 响应详解

### 3.1 响应结构

HTTP 响应由以下部分组成：

```
状态行
响应头（多行）
空行
响应体（可选）
```

### 3.2 状态行

状态行包含三个部分：

- **HTTP 版本**：HTTP/1.1 或 HTTP/2
- **状态码**：三位数字状态码
- **状态描述**：状态码的文字描述

**示例**：

```http
HTTP/1.1 200 OK
```

### 3.3 响应头

响应头包含元数据信息，常见响应头包括：

| 响应头              | 说明                           | 示例                           |
|:--------------------|:-------------------------------|:-------------------------------|
| **Content-Type**    | 响应体的媒体类型               | `Content-Type: application/json` |
| **Content-Length**  | 响应体的长度（字节）           | `Content-Length: 1024`         |
| **Content-Encoding**| 内容编码                       | `Content-Encoding: gzip`       |
| **Cache-Control**   | 缓存控制                       | `Cache-Control: max-age=3600` |
| **ETag**            | 实体标签（用于缓存验证）       | `ETag: "abc123"`               |
| **Last-Modified**   | 最后修改时间（用于缓存验证）   | `Last-Modified: Wed, 21 Oct 2015 07:28:00 GMT` |
| **Location**        | 重定向目标 URL                 | `Location: /api/users/123`     |
| **Set-Cookie**      | 设置 Cookie                    | `Set-Cookie: session=abc123; Path=/` |
| **Access-Control-Allow-Origin** | CORS 允许的来源 | `Access-Control-Allow-Origin: *` |

### 3.4 响应体

响应体包含实际的数据，格式与请求体类似。

**示例**：

```http
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 45

{"id":1,"name":"John","email":"john@example.com"}
```

## 4. HTTP 状态码详解

### 4.1 1xx 信息性状态码

| 状态码 | 名称              | 说明                     |
|:-------|:------------------|:-------------------------|
| **100**| Continue          | 继续，客户端应继续请求   |
| **101**| Switching Protocols | 切换协议             |

### 4.2 2xx 成功状态码

| 状态码 | 名称           | 说明                     |
|:-------|:---------------|:-------------------------|
| **200**| OK             | 请求成功                 |
| **201**| Created        | 资源创建成功             |
| **202**| Accepted       | 请求已接受，但未处理完成 |
| **204**| No Content     | 请求成功，无返回内容     |
| **206**| Partial Content| 部分内容（用于范围请求） |

### 4.3 3xx 重定向状态码

| 状态码 | 名称              | 说明                     |
|:-------|:------------------|:-------------------------|
| **301**| Moved Permanently | 永久重定向             |
| **302**| Found            | 临时重定向               |
| **304**| Not Modified     | 未修改（用于缓存验证）   |
| **307**| Temporary Redirect| 临时重定向（保持方法）   |
| **308**| Permanent Redirect| 永久重定向（保持方法）  |

### 4.4 4xx 客户端错误状态码

| 状态码 | 名称                | 说明                     |
|:-------|:--------------------|:-------------------------|
| **400**| Bad Request        | 请求参数错误             |
| **401**| Unauthorized       | 未授权，需要认证         |
| **403**| Forbidden          | 禁止访问                 |
| **404**| Not Found          | 资源不存在               |
| **405**| Method Not Allowed | 方法不允许               |
| **409**| Conflict           | 资源冲突                 |
| **422**| Unprocessable Entity | 请求格式正确但语义错误 |
| **429**| Too Many Requests  | 请求过多（限流）         |

### 4.5 5xx 服务器错误状态码

| 状态码 | 名称                    | 说明                     |
|:-------|:------------------------|:-------------------------|
| **500**| Internal Server Error  | 服务器内部错误           |
| **502**| Bad Gateway            | 网关错误                 |
| **503**| Service Unavailable   | 服务不可用               |
| **504**| Gateway Timeout        | 网关超时                 |

## 5. HTTP 缓存机制

### 5.1 缓存控制头

| 头部字段          | 说明                           | 示例                           |
|:------------------|:-------------------------------|:-------------------------------|
| **Cache-Control** | 缓存控制指令                   | `Cache-Control: max-age=3600` |
| **Expires**       | 过期时间（HTTP/1.0）           | `Expires: Wed, 21 Oct 2015 07:28:00 GMT` |
| **ETag**          | 实体标签（用于缓存验证）       | `ETag: "abc123"`               |
| **Last-Modified** | 最后修改时间（用于缓存验证）   | `Last-Modified: Wed, 21 Oct 2015 07:28:00 GMT` |

### 5.2 Cache-Control 指令

| 指令              | 说明                           | 示例                           |
|:------------------|:-------------------------------|:-------------------------------|
| **max-age**       | 缓存最大生存时间（秒）         | `max-age=3600`                 |
| **no-cache**      | 必须重新验证                   | `no-cache`                     |
| **no-store**      | 不缓存                         | `no-store`                     |
| **private**       | 仅客户端缓存                   | `private`                      |
| **public**        | 可被任何缓存缓存               | `public`                       |
| **must-revalidate**| 过期后必须重新验证           | `must-revalidate`              |

### 5.3 缓存验证

客户端可以使用以下头部进行缓存验证：

- **If-None-Match**：与 ETag 比较
- **If-Modified-Since**：与 Last-Modified 比较

**示例**：

```http
GET /api/users/123 HTTP/1.1
If-None-Match: "abc123"
```

如果资源未修改，服务器返回 `304 Not Modified`。

## 6. HTTP 连接管理

### 6.1 持久连接

HTTP/1.1 默认使用持久连接（Keep-Alive），可以在同一个 TCP 连接上发送多个请求。

**Connection 头部**：

- `Connection: keep-alive`：保持连接
- `Connection: close`：关闭连接

### 6.2 管道化

HTTP/1.1 支持管道化（Pipelining），可以在收到响应前发送多个请求。但由于实现复杂，实际使用较少。

### 6.3 HTTP/2 多路复用

HTTP/2 支持多路复用，可以在同一个连接上并行发送多个请求和响应，提高性能。

## 7. CORS（跨域资源共享）

### 7.1 CORS 头部

| 响应头                          | 说明                           | 示例                           |
|:--------------------------------|:-------------------------------|:-------------------------------|
| **Access-Control-Allow-Origin** | 允许的来源                     | `Access-Control-Allow-Origin: *` |
| **Access-Control-Allow-Methods**| 允许的方法                     | `Access-Control-Allow-Methods: GET, POST` |
| **Access-Control-Allow-Headers**| 允许的头部                     | `Access-Control-Allow-Headers: Content-Type` |
| **Access-Control-Max-Age**      | 预检请求缓存时间（秒）         | `Access-Control-Max-Age: 3600` |

### 7.2 预检请求

对于复杂请求（如 POST 带自定义头部），浏览器会先发送 OPTIONS 预检请求。

**示例**：

```http
OPTIONS /api/users HTTP/1.1
Origin: https://example.com
Access-Control-Request-Method: POST
Access-Control-Request-Headers: Content-Type
```

## 8. 内容协商

### 8.1 Accept 头部

客户端使用 `Accept` 头部指定接受的媒体类型：

```http
Accept: application/json, application/xml, text/plain
```

### 8.2 Accept-Language 头部

客户端使用 `Accept-Language` 头部指定接受的语言：

```http
Accept-Language: zh-CN, en;q=0.9
```

### 8.3 Accept-Encoding 头部

客户端使用 `Accept-Encoding` 头部指定接受的编码：

```http
Accept-Encoding: gzip, deflate, br
```

## 9. 代码示例

### 9.1 创建 HTTP 服务器

```ts
import { createServer, IncomingMessage, ServerResponse } from 'node:http';

const server = createServer((req: IncomingMessage, res: ServerResponse) => {
  // 设置响应头
  res.setHeader('Content-Type', 'application/json');
  res.setHeader('Cache-Control', 'max-age=3600');

  // 处理请求
  if (req.method === 'GET' && req.url === '/api/users') {
    res.statusCode = 200;
    res.end(JSON.stringify({ users: [] }));
  } else {
    res.statusCode = 404;
    res.end(JSON.stringify({ error: 'Not Found' }));
  }
});

server.listen(3000, (): void => {
  console.log('Server running on http://localhost:3000');
});
```

### 9.2 发送 HTTP 请求

```ts
import { request, RequestOptions } from 'node:http';

const options: RequestOptions = {
  hostname: 'api.example.com',
  port: 443,
  path: '/api/users',
  method: 'GET',
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  }
};

import { IncomingMessage } from 'node:http';

const req = request(options, (res: IncomingMessage): void => {
  let data = '';

  res.on('data', (chunk: Buffer): void => {
    data += chunk.toString();
  });

  res.on('end', (): void => {
    console.log(JSON.parse(data));
  });
});

req.on('error', (error: Error): void => {
  console.error(error);
});

req.end();
```

## 10. 注意事项

- **安全性**：注意防止常见攻击，如 XSS、CSRF、SQL 注入等
- **性能**：合理使用缓存和压缩，减少网络传输
- **错误处理**：使用标准状态码，提供清晰的错误信息
- **版本兼容**：注意 HTTP/1.1 和 HTTP/2 的差异

## 11. 最佳实践

- **使用 HTTPS**：在生产环境使用 HTTPS 加密传输
- **合理使用缓存**：根据资源特性设置合适的缓存策略
- **压缩响应**：使用 gzip 或 brotli 压缩响应体
- **设置超时**：为请求和响应设置合理的超时时间
- **监控和日志**：记录请求和响应日志，便于问题排查

---

**下一节**：[4.1.3 RESTful API 设计原则](section-03-restful.md)
