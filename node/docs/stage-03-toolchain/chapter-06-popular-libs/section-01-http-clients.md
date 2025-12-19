# 3.6.1 HTTP 客户端库

## 1. 概述

HTTP 客户端库用于发送 HTTP 请求，是 Node.js 开发中常用的库。虽然 Node.js 提供了原生的 `http` 和 `https` 模块，但使用第三方库可以简化开发，提供更好的 API 和功能。理解 HTTP 客户端库的使用对于 API 调用和网络请求非常重要。

## 2. 特性说明

- **简化 API**：提供更简洁的 API，易于使用。
- **Promise 支持**：原生支持 Promise，可以使用 async/await。
- **请求拦截**：支持请求和响应拦截器。
- **自动转换**：自动处理 JSON 转换。
- **错误处理**：更好的错误处理机制。

## 3. 主流 HTTP 客户端库

| 库名         | 特点                                     | 适用场景                       |
|:-------------|:-----------------------------------------|:-------------------------------|
| **axios**    | 功能丰富、使用广泛、浏览器和 Node.js 支持 | 通用场景，推荐使用             |
| **undici**   | Node.js 官方推荐、高性能                 | Node.js 项目、追求性能         |
| **node-fetch**| Fetch API 的 Node.js 实现                | 熟悉 Fetch API 的开发者        |
| **got**      | 功能强大、支持流式处理                   | 需要高级功能的场景             |

## 4. 基本用法

### 示例 1：axios

```ts
// 文件: http-axios.ts
// 功能: axios 使用示例

import axios from 'axios';

// GET 请求
async function fetchData() {
    const response = await axios.get('https://api.example.com/data');
    return response.data;
}

// POST 请求
async function createData(data: any) {
    const response = await axios.post('https://api.example.com/data', data);
    return response.data;
}

// 配置实例
const api = axios.create({
    baseURL: 'https://api.example.com',
    timeout: 5000,
    headers: {
        'Content-Type': 'application/json'
    }
});

// 使用实例
const response = await api.get('/users');
```

### 示例 2：undici

```ts
// 文件: http-undici.ts
// 功能: undici 使用示例

import { request } from 'undici';

// GET 请求
async function fetchData() {
    const { statusCode, headers, body } = await request('https://api.example.com/data');
    const data = await body.json();
    return data;
}

// POST 请求
async function createData(data: any) {
    const { statusCode, body } = await request('https://api.example.com/data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    return await body.json();
}
```

### 示例 3：node-fetch

```ts
// 文件: http-node-fetch.ts
// 功能: node-fetch 使用示例

import fetch from 'node-fetch';

// GET 请求
async function fetchData() {
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();
    return data;
}

// POST 请求
async function createData(data: any) {
    const response = await fetch('https://api.example.com/data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    return await response.json();
}
```

## 5. 参数说明：HTTP 客户端库参数

### axios 参数

| 参数名       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **url**      | String   | 请求 URL                                 | `'https://api.example.com/data'`|
| **method**   | String   | HTTP 方法                                | `'GET'`, `'POST'`              |
| **data**     | Any      | 请求体数据                               | `{ name: 'Alice' }`            |
| **headers**  | Object   | 请求头                                  | `{ 'Content-Type': 'application/json' }`|
| **timeout**  | Number   | 超时时间（毫秒）                         | `5000`                         |

## 6. 返回值与状态说明

HTTP 客户端库操作的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **请求**     | Promise      | 返回 Promise，resolve 为响应对象         |
| **响应**     | Object       | 包含 status、headers、data 等属性       |

## 7. 代码示例：完整的 HTTP 客户端封装

以下示例演示了如何封装完整的 HTTP 客户端：

```ts
// 文件: http-client-complete.ts
// 功能: 完整的 HTTP 客户端封装

import axios, { AxiosInstance, AxiosError } from 'axios';

class HttpClient {
    private client: AxiosInstance;
    
    constructor(baseURL: string) {
        this.client = axios.create({
            baseURL,
            timeout: 10000,
            headers: {
                'Content-Type': 'application/json'
            }
        });
        
        // 请求拦截器
        this.client.interceptors.request.use(
            (config) => {
                // 添加认证 token
                const token = this.getToken();
                if (token) {
                    config.headers.Authorization = `Bearer ${token}`;
                }
                return config;
            },
            (error) => Promise.reject(error)
        );
        
        // 响应拦截器
        this.client.interceptors.response.use(
            (response) => response,
            (error: AxiosError) => {
                // 统一错误处理
                if (error.response) {
                    console.error('Response error:', error.response.status);
                } else if (error.request) {
                    console.error('Request error:', error.message);
                }
                return Promise.reject(error);
            }
        );
    }
    
    private getToken(): string | null {
        // 获取 token 的逻辑
        return null;
    }
    
    async get<T>(url: string, config?: any): Promise<T> {
        const response = await this.client.get<T>(url, config);
        return response.data;
    }
    
    async post<T>(url: string, data?: any, config?: any): Promise<T> {
        const response = await this.client.post<T>(url, data, config);
        return response.data;
    }
    
    async put<T>(url: string, data?: any, config?: any): Promise<T> {
        const response = await this.client.put<T>(url, data, config);
        return response.data;
    }
    
    async delete<T>(url: string, config?: any): Promise<T> {
        const response = await this.client.delete<T>(url, config);
        return response.data;
    }
}

// 使用
const client = new HttpClient('https://api.example.com');

async function example() {
    try {
        const users = await client.get('/users');
        const user = await client.post('/users', { name: 'Alice' });
        console.log('Users:', users);
        console.log('Created user:', user);
    } catch (error) {
        console.error('Error:', error);
    }
}

example();
```

## 8. 输出结果说明

HTTP 客户端请求的输出结果：

```text
Users: [{ id: 1, name: 'Alice' }]
Created user: { id: 2, name: 'Alice' }
```

**逻辑解析**：
- 自动处理 JSON 转换
- 统一错误处理
- 请求和响应拦截器

## 9. 使用场景

### 1. API 调用

调用外部 API：

```ts
// API 调用示例
const client = new HttpClient('https://api.example.com');
const data = await client.get('/data');
```

### 2. 微服务通信

微服务之间的通信：

```ts
// 微服务通信示例
const userService = new HttpClient('http://user-service:3000');
const user = await userService.get(`/users/${userId}`);
```

### 3. 数据同步

同步数据到外部服务：

```ts
// 数据同步示例
const syncService = new HttpClient('https://sync.example.com');
await syncService.post('/sync', data);
```

## 10. 注意事项与常见错误

- **错误处理**：完善的错误处理，处理网络错误和 HTTP 错误
- **超时设置**：设置合理的超时时间
- **重试机制**：实现重试机制处理临时失败
- **请求拦截**：使用拦截器统一处理请求和响应
- **性能考虑**：注意请求的性能和并发控制

## 11. 常见问题 (FAQ)

**Q: axios 和 undici 如何选择？**
A: axios 功能丰富，使用广泛；undici 是 Node.js 官方推荐，性能更好。

**Q: 如何处理请求超时？**
A: 设置 `timeout` 参数，或使用拦截器处理超时错误。

**Q: 如何实现请求重试？**
A: 使用拦截器或第三方库（如 axios-retry）实现重试机制。

## 12. 最佳实践

- **使用库**：优先使用 HTTP 客户端库，而非原生模块
- **错误处理**：完善的错误处理和重试机制
- **请求拦截**：使用拦截器统一处理请求和响应
- **性能优化**：合理设置超时和并发控制
- **类型安全**：使用 TypeScript 提供类型安全

## 13. 对比分析：HTTP 客户端库选择

| 维度             | axios                                  | undici                                 | node-fetch                            |
|:-----------------|:---------------------------------------|:---------------------------------------|:--------------------------------------|
| **功能**         | 功能丰富                               | 高性能                                 | Fetch API 兼容                        |
| **性能**         | 中等                                   | 高                                     | 中等                                  |
| **使用广泛度**   | 最广泛                                 | 增长中                                 | 广泛                                  |
| **推荐使用**     | ✅ 推荐（通用场景）                     | Node.js 项目、追求性能                 | 熟悉 Fetch API                        |

## 14. 练习任务

1. **HTTP 客户端实践**：
   - 使用不同的 HTTP 客户端库
   - 理解各库的特点
   - 实现 API 调用

2. **封装实践**：
   - 封装 HTTP 客户端类
   - 实现请求和响应拦截器
   - 实现错误处理和重试

3. **实际应用**：
   - 在实际项目中应用 HTTP 客户端库
   - 实现 API 调用功能
   - 优化请求性能

完成以上练习后，继续学习下一节：工具函数库。

## 总结

HTTP 客户端库是 Node.js 开发的重要工具：

- **核心功能**：简化 API、Promise 支持、请求拦截、自动转换
- **主流库**：axios、undici、node-fetch
- **最佳实践**：使用库、错误处理、请求拦截、性能优化

掌握 HTTP 客户端库有助于快速开发 Node.js 应用。

---

**最后更新**：2025-01-XX
