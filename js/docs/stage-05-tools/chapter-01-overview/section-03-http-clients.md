# 5.1.3 HTTP 客户端库

## 概述

HTTP 客户端库用于发送 HTTP 请求。本节介绍常用的 HTTP 客户端库，包括 Axios、Fetch API 等，以及它们的使用方法和特点。

## Fetch API

### 简介

Fetch API 是现代浏览器原生提供的 HTTP 请求 API，基于 Promise，API 简洁。

### 基本使用

```js
// GET 请求
fetch('https://api.example.com/data')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));

// POST 请求
fetch('https://api.example.com/data', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ name: 'John', age: 30 })
})
    .then(response => response.json())
    .then(data => console.log(data));
```

### 请求配置

**语法格式**：`fetch(url[, options])`

**参数说明**：

| 参数名    | 类型   | 说明           | 是否必需 | 默认值 |
|:----------|:-------|:---------------|:---------|:-------|
| `url`     | string | 请求 URL        | 是       | -      |
| `options` | object | 请求配置对象    | 否       | -      |

**options 对象属性**：

| 属性名      | 类型   | 说明                           | 默认值     |
|:------------|:-------|:-------------------------------|:-----------|
| `method`    | string | HTTP 方法（GET、POST 等）     | 'GET'      |
| `headers`   | object | 请求头                          | {}         |
| `body`      | string | 请求体                          | -          |
| `mode`      | string | 请求模式（cors、no-cors 等）  | 'cors'     |
| `credentials` | string | 是否发送 Cookie              | 'same-origin' |
| `cache`     | string | 缓存策略                        | 'default'  |

### 错误处理

```js
fetch('https://api.example.com/data')
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
```

### 使用 async/await

```js
async function fetchData() {
    try {
        const response = await fetch('https://api.example.com/data');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error('Error:', error);
    }
}
```

## Axios

### 简介

Axios 是一个流行的 HTTP 客户端库，提供了更丰富的功能和更好的错误处理。

### 安装

```bash
npm install axios
```

### 基本使用

```js
import axios from 'axios';

// GET 请求
axios.get('https://api.example.com/data')
    .then(response => console.log(response.data))
    .catch(error => console.error('Error:', error));

// POST 请求
axios.post('https://api.example.com/data', {
    name: 'John',
    age: 30
})
    .then(response => console.log(response.data))
    .catch(error => console.error('Error:', error));
```

### 请求配置

```js
// 使用配置对象
axios({
    method: 'POST',
    url: 'https://api.example.com/data',
    headers: {
        'Content-Type': 'application/json',
    },
    data: {
        name: 'John',
        age: 30
    }
})
    .then(response => console.log(response.data));
```

### 创建实例

```js
// 创建 axios 实例
const api = axios.create({
    baseURL: 'https://api.example.com',
    timeout: 5000,
    headers: {
        'Content-Type': 'application/json',
    }
});

// 使用实例
api.get('/users')
    .then(response => console.log(response.data));
```

### 请求拦截器

```js
// 请求拦截器
axios.interceptors.request.use(config => {
    // 添加认证令牌
    config.headers.Authorization = `Bearer ${token}`;
    return config;
}, error => {
    return Promise.reject(error);
});

// 响应拦截器
axios.interceptors.response.use(response => {
    return response;
}, error => {
    if (error.response?.status === 401) {
        // 处理未授权错误
    }
    return Promise.reject(error);
});
```

### 错误处理

```js
axios.get('https://api.example.com/data')
    .catch(error => {
        if (error.response) {
            // 服务器返回了错误状态码
            console.error('Error data:', error.response.data);
            console.error('Error status:', error.response.status);
        } else if (error.request) {
            // 请求已发送但没有收到响应
            console.error('No response received');
        } else {
            // 请求配置出错
            console.error('Error:', error.message);
        }
    });
```

## 库对比

| 特性          | Fetch API      | Axios          |
|:--------------|:---------------|:---------------|
| 浏览器支持    | 现代浏览器     | 所有浏览器     |
| 请求拦截器    | 不支持         | 支持           |
| 响应拦截器    | 不支持         | 支持           |
| 自动 JSON     | 需要手动调用   | 自动处理       |
| 请求取消      | AbortController | 支持 CancelToken |
| 体积          | 原生，无额外体积 | 约 13KB       |
| 错误处理      | 需要手动检查   | 更完善         |

## 选择建议

1. **简单请求**：使用 Fetch API
2. **需要拦截器**：使用 Axios
3. **需要更好错误处理**：使用 Axios
4. **减少依赖**：使用 Fetch API

## 注意事项

1. **错误处理**：Fetch 需要手动检查 response.ok
2. **请求取消**：Fetch 使用 AbortController，Axios 使用 CancelToken
3. **JSON 处理**：Fetch 需要手动调用 json()，Axios 自动处理
4. **浏览器兼容**：Fetch 需要现代浏览器，Axios 兼容性更好

## 最佳实践

1. **统一使用**：项目内统一使用一个 HTTP 客户端
2. **错误处理**：实现统一的错误处理机制
3. **请求拦截**：使用拦截器添加认证令牌等
4. **响应拦截**：使用响应拦截器处理错误和格式化数据

## 练习

1. **Fetch 基础**：使用 Fetch API 实现 GET 和 POST 请求。

2. **Axios 实例**：创建 Axios 实例，配置 baseURL 和默认 headers。

3. **请求拦截**：使用 Axios 拦截器实现自动添加认证令牌。

4. **错误处理**：实现统一的错误处理机制，处理网络错误和业务错误。

5. **请求取消**：实现请求取消功能，避免重复请求。

完成以上练习后，继续学习下一节，了解测试框架。

## 总结

Fetch API 是浏览器原生的 HTTP 请求 API，Axios 提供了更丰富的功能。Fetch API 简洁、无额外依赖；Axios 功能完善、错误处理更好。根据项目需求选择合适的 HTTP 客户端。

## 相关资源

- [MDN：Fetch API](https://developer.mozilla.org/zh-CN/docs/Web/API/Fetch_API)
- [Axios 官网](https://axios-http.com/)
- [Axios GitHub](https://github.com/axios/axios)
