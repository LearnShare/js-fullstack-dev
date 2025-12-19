# 2.4.4 HTTP 客户端

## 1. 概述

HTTP 模块不仅可以创建服务器，还可以作为客户端发送 HTTP 请求。通过 `http.request()` 和 `http.get()` 方法，可以向其他服务器发送 HTTP 请求，获取数据或调用 API。理解 HTTP 客户端的使用对于构建微服务、API 调用等场景非常重要。

## 2. 特性说明

- **请求发送**：可以发送各种 HTTP 方法的请求。
- **请求配置**：支持配置请求头、请求体等。
- **响应处理**：处理服务器返回的响应数据。
- **错误处理**：处理网络错误和 HTTP 错误。
- **流式处理**：支持流式请求和响应处理。

## 3. 语法与定义

### 发送请求

```ts
// 发送 HTTP 请求
http.request(options: RequestOptions, callback?: (res: IncomingMessage) => void): ClientRequest

// 发送 GET 请求（简化版）
http.get(options: RequestOptions, callback?: (res: IncomingMessage) => void): ClientRequest
```

### 请求选项

```ts
interface RequestOptions {
    hostname?: string;
    port?: number;
    path?: string;
    method?: string;
    headers?: OutgoingHttpHeaders;
    timeout?: number;
}
```

## 4. 基本用法

### 示例 1：发送 GET 请求

```ts
// 文件: http-client-get.ts
// 功能: 发送 GET 请求

import http from 'node:http';

function getRequest(url: string): Promise<string> {
    return new Promise((resolve, reject) => {
        const urlObj = new URL(url);
        
        const options = {
            hostname: urlObj.hostname,
            port: urlObj.port || 80,
            path: urlObj.pathname + urlObj.search,
            method: 'GET'
        };
        
        const req = http.request(options, (res) => {
            let data = '';
            
            res.on('data', (chunk) => {
                data += chunk.toString();
            });
            
            res.on('end', () => {
                resolve(data);
            });
        });
        
        req.on('error', (error) => {
            reject(error);
        });
        
        req.end();
    });
}

// 使用
getRequest('http://example.com')
    .then(data => console.log(data))
    .catch(error => console.error(error));
```

### 示例 2：发送 POST 请求

```ts
// 文件: http-client-post.ts
// 功能: 发送 POST 请求

import http from 'node:http';

function postRequest(url: string, data: object): Promise<string> {
    return new Promise((resolve, reject) => {
        const urlObj = new URL(url);
        const jsonData = JSON.stringify(data);
        
        const options = {
            hostname: urlObj.hostname,
            port: urlObj.port || 80,
            path: urlObj.pathname,
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Content-Length': Buffer.byteLength(jsonData)
            }
        };
        
        const req = http.request(options, (res) => {
            let responseData = '';
            
            res.on('data', (chunk) => {
                responseData += chunk.toString();
            });
            
            res.on('end', () => {
                resolve(responseData);
            });
        });
        
        req.on('error', (error) => {
            reject(error);
        });
        
        req.write(jsonData);
        req.end();
    });
}

// 使用
postRequest('http://api.example.com/users', { name: 'Alice', age: 25 })
    .then(response => console.log(response))
    .catch(error => console.error(error));
```

### 示例 3：使用 http.get 简化 GET 请求

```ts
// 文件: http-client-get-simple.ts
// 功能: 使用 http.get 简化 GET 请求

import http from 'node:http';

function simpleGet(url: string): Promise<string> {
    return new Promise((resolve, reject) => {
        http.get(url, (res) => {
            let data = '';
            
            res.on('data', (chunk) => {
                data += chunk.toString();
            });
            
            res.on('end', () => {
                resolve(data);
            });
        }).on('error', (error) => {
            reject(error);
        });
    });
}

// 使用
simpleGet('http://example.com')
    .then(data => console.log(data))
    .catch(error => console.error(error));
```

## 5. 参数说明：request 和 get 方法

### request 参数

| 参数名       | 类型           | 说明                                     | 示例                           |
|:-------------|:---------------|:-----------------------------------------|:-------------------------------|
| **options**  | RequestOptions | 请求配置选项                             | `{ hostname: 'example.com' }`  |
| **callback** | Function       | 响应处理回调（可选）                     | `(res) => {}`                  |

### get 参数

| 参数名       | 类型           | 说明                                     | 示例                           |
|:-------------|:---------------|:-----------------------------------------|:-------------------------------|
| **options**  | RequestOptions/String | 请求配置或 URL 字符串            | `'http://example.com'`         |
| **callback** | Function       | 响应处理回调（可选）                     | `(res) => {}`                  |

## 6. 返回值与状态说明

### request/get 返回值

| 返回类型         | 说明                                     |
|:-----------------|:-----------------------------------------|
| **ClientRequest**| HTTP 客户端请求对象                       |

### 响应对象事件

| 事件名称     | 说明                                     |
|:-------------|:-----------------------------------------|
| **'data'**   | 接收到响应数据时触发                     |
| **'end'**    | 响应数据接收完成时触发                   |
| **'error'**  | 发生错误时触发                           |

## 7. 代码示例：完整的 HTTP 客户端封装

以下示例演示了如何封装一个完整的 HTTP 客户端：

```ts
// 文件: http-client-complete.ts
// 功能: 完整的 HTTP 客户端封装

import http from 'node:http';
import { URL } from 'node:url';

interface RequestOptions {
    method?: string;
    headers?: Record<string, string>;
    body?: any;
    timeout?: number;
}

class HttpClient {
    async request(url: string, options: RequestOptions = {}): Promise<any> {
        return new Promise((resolve, reject) => {
            const urlObj = new URL(url);
            const method = options.method || 'GET';
            const headers = options.headers || {};
            
            // 处理请求体
            let bodyData: string | undefined;
            if (options.body) {
                if (typeof options.body === 'object') {
                    bodyData = JSON.stringify(options.body);
                    headers['Content-Type'] = headers['Content-Type'] || 'application/json';
                } else {
                    bodyData = options.body.toString();
                }
                headers['Content-Length'] = Buffer.byteLength(bodyData).toString();
            }
            
            const requestOptions = {
                hostname: urlObj.hostname,
                port: urlObj.port || (urlObj.protocol === 'https:' ? 443 : 80),
                path: urlObj.pathname + urlObj.search,
                method: method,
                headers: headers,
                timeout: options.timeout || 5000
            };
            
            const req = http.request(requestOptions, (res) => {
                let data = '';
                
                res.on('data', (chunk) => {
                    data += chunk.toString();
                });
                
                res.on('end', () => {
                    try {
                        const contentType = res.headers['content-type'] || '';
                        if (contentType.includes('application/json')) {
                            resolve(JSON.parse(data));
                        } else {
                            resolve(data);
                        }
                    } catch (error) {
                        resolve(data);
                    }
                });
            });
            
            req.on('error', (error) => {
                reject(error);
            });
            
            req.on('timeout', () => {
                req.destroy();
                reject(new Error('Request timeout'));
            });
            
            if (bodyData) {
                req.write(bodyData);
            }
            
            req.end();
        });
    }
    
    async get(url: string, options?: Omit<RequestOptions, 'method' | 'body'>): Promise<any> {
        return this.request(url, { ...options, method: 'GET' });
    }
    
    async post(url: string, body?: any, options?: Omit<RequestOptions, 'method' | 'body'>): Promise<any> {
        return this.request(url, { ...options, method: 'POST', body });
    }
}

// 使用
const client = new HttpClient();

async function example() {
    try {
        const data = await client.get('http://api.example.com/users');
        console.log('Users:', data);
        
        const newUser = await client.post('http://api.example.com/users', {
            name: 'Alice',
            age: 25
        });
        console.log('Created user:', newUser);
    } catch (error) {
        console.error('Request failed:', error);
    }
}

example();
```

## 8. 输出结果说明

GET 请求的输出：

```json
{"users": [{"id": 1, "name": "Alice"}]}
```

POST 请求的输出：

```json
{"id": 2, "name": "Alice", "age": 25}
```

**逻辑解析**：
- GET 请求：发送请求并接收响应数据
- POST 请求：发送请求体和接收响应数据
- 自动解析 JSON 响应

## 9. 使用场景

### 1. API 调用

调用外部 API：

```ts
// API 调用示例
async function fetchUsers() {
    const client = new HttpClient();
    return await client.get('https://api.example.com/users');
}
```

### 2. 微服务通信

微服务之间的通信：

```ts
// 微服务通信示例
async function callUserService(userId: string) {
    const client = new HttpClient();
    return await client.get(`http://user-service:3000/users/${userId}`);
}
```

### 3. 数据同步

同步数据到外部服务：

```ts
// 数据同步示例
async function syncData(data: any) {
    const client = new HttpClient();
    return await client.post('https://api.example.com/sync', data);
}
```

## 10. 注意事项与常见错误

- **错误处理**：处理网络错误和 HTTP 错误状态码
- **超时设置**：设置合理的请求超时时间
- **请求头设置**：正确设置 Content-Type 和 Content-Length
- **响应解析**：根据 Content-Type 解析响应数据
- **连接管理**：注意 HTTP 连接的复用和关闭

## 11. 常见问题 (FAQ)

**Q: 如何处理 HTTPS 请求？**
A: 使用 `https` 模块而不是 `http` 模块，其他用法相同。

**Q: 如何设置请求超时？**
A: 在请求选项中设置 `timeout` 属性，或使用 `req.setTimeout()`。

**Q: 如何发送文件？**
A: 使用 `fs.createReadStream()` 创建文件流，通过 `req.write()` 或 `req.pipe()` 发送。

## 12. 最佳实践

- **使用 Promise**：将回调式 API 封装为 Promise，使用 async/await
- **错误处理**：完善的错误处理和重试机制
- **超时设置**：设置合理的超时时间
- **请求头管理**：正确设置和管理请求头
- **使用库**：实际项目中使用 axios、fetch 等库，简化开发

## 13. 对比分析：原生 HTTP vs HTTP 库

| 维度             | 原生 HTTP 模块                            | HTTP 库（如 axios）                        |
|:-----------------|:------------------------------------------|:--------------------------------------------|
| **API 设计**     | 回调式，需要手动封装                       | Promise 支持，使用简单                      |
| **功能**         | 基础功能                                  | 丰富的功能（拦截器、自动重试等）            |
| **代码量**       | 代码量较大                                | 代码简洁                                    |
| **学习价值**     | 有助于理解 HTTP 协议                      | 提高开发效率                                |

## 14. 练习任务

1. **GET 请求实践**：
   - 发送简单的 GET 请求
   - 处理响应数据
   - 解析 JSON 响应

2. **POST 请求实践**：
   - 发送 POST 请求
   - 发送 JSON 数据
   - 处理响应

3. **错误处理实践**：
   - 处理网络错误
   - 处理 HTTP 错误状态码
   - 实现重试机制

4. **实际应用**：
   - 封装 HTTP 客户端类
   - 实现 API 调用功能
   - 添加超时和错误处理

完成以上练习后，继续学习下一章：事件系统（events）。

## 总结

HTTP 客户端是 Node.js HTTP 模块的重要功能：

- **核心方法**：`http.request()` 和 `http.get()`
- **请求配置**：配置请求方法、请求头、请求体
- **响应处理**：处理响应数据和错误
- **最佳实践**：使用 Promise、错误处理、超时设置

掌握 HTTP 客户端有助于进行 API 调用和微服务通信。

---

**最后更新**：2025-01-XX
