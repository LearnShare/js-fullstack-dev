# 2.8.1 URL 与查询字符串概述

## 1. 概述

URL（Uniform Resource Locator）是统一资源定位符，用于标识互联网上的资源。查询字符串是 URL 的一部分，用于传递参数。Node.js 提供了 `url` 和 `querystring` 模块来处理 URL 解析、构建和查询字符串的编码解码。理解这些模块的使用对于构建 Web 应用和 API 至关重要。

## 2. 特性说明

- **URL 解析**：解析 URL 的各个组成部分（协议、主机、路径、查询字符串等）。
- **URL 构建**：从组成部分构建完整的 URL。
- **查询字符串编码**：将对象编码为查询字符串。
- **查询字符串解码**：将查询字符串解码为对象。
- **URL 规范化**：规范化 URL，处理特殊字符。

## 3. 模块导入方式

### ES Modules 方式

```ts
import { URL, URLSearchParams } from 'node:url';
import querystring from 'node:querystring';
```

### CommonJS 方式

```ts
const { URL, URLSearchParams } = require('node:url');
const querystring = require('node:querystring');
```

## 4. URL 结构

URL 的基本结构：

```
https://example.com:8080/path/to/resource?key=value&foo=bar#fragment
│     │              │   │                │              │
│     │              │   │                │              └─ 片段
│     │              │   │                └─ 查询字符串
│     │              │   └─ 路径
│     │              └─ 端口
│     └─ 主机名
└─ 协议
```

## 5. 参数说明：URL 和查询字符串 API

| API 名称      | 说明                                     | 示例                           |
|:--------------|:-----------------------------------------|:-------------------------------|
| **URL**       | URL 类，用于解析和构建 URL               | `new URL('https://example.com')`|
| **URLSearchParams**| 查询参数类，用于处理查询字符串        | `new URLSearchParams('?a=1')`  |
| **querystring.parse**| 解析查询字符串为对象                | `querystring.parse('a=1&b=2')` |
| **querystring.stringify**| 将对象编码为查询字符串            | `querystring.stringify({a:1})`  |

## 6. 返回值与状态说明

URL 和查询字符串操作的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **URL 解析** | URL 对象     | 包含 URL 各个组成部分的对象              |
| **查询解析** | Object       | 包含查询参数的对象                       |
| **查询编码** | String       | 编码后的查询字符串                       |

## 7. 代码示例：基本 URL 处理

以下示例演示了 URL 和查询字符串的基本使用：

```ts
// 文件: url-basic.ts
// 功能: 基本 URL 处理

import { URL } from 'node:url';
import querystring from 'node:querystring';

// 1. URL 解析
const url = new URL('https://example.com:8080/path?key=value#fragment');
console.log('Protocol:', url.protocol);     // https:
console.log('Hostname:', url.hostname);     // example.com
console.log('Port:', url.port);             // 8080
console.log('Pathname:', url.pathname);     // /path
console.log('Search:', url.search);         // ?key=value
console.log('Hash:', url.hash);             // #fragment

// 2. 查询字符串解析
const params = querystring.parse('key=value&foo=bar');
console.log('Params:', params);             // { key: 'value', foo: 'bar' }

// 3. 查询字符串编码
const query = querystring.stringify({ key: 'value', foo: 'bar' });
console.log('Query:', query);               // key=value&foo=bar
```

## 8. 输出结果说明

URL 处理的输出结果：

```text
Protocol: https:
Hostname: example.com
Port: 8080
Pathname: /path
Search: ?key=value
Hash: #fragment
Params: { key: 'value', foo: 'bar' }
Query: key=value&foo=bar
```

**逻辑解析**：
- URL 对象包含 URL 的各个组成部分
- 查询字符串可以解析为对象，也可以从对象编码为字符串
- 所有操作都是类型安全的

## 9. 使用场景

### 1. HTTP 请求处理

处理 HTTP 请求的 URL：

```ts
// HTTP 请求处理示例
import http from 'node:http';
import { URL } from 'node:url';

const server = http.createServer((req, res) => {
    if (!req.url) return;
    
    const url = new URL(req.url, `http://${req.headers.host}`);
    const pathname = url.pathname;
    const params = Object.fromEntries(url.searchParams);
    
    console.log('Path:', pathname);
    console.log('Params:', params);
});
```

### 2. API 参数解析

解析 API 请求参数：

```ts
// API 参数解析示例
import { URL } from 'node:url';

function parseAPIRequest(urlString: string) {
    const url = new URL(urlString);
    return {
        endpoint: url.pathname,
        params: Object.fromEntries(url.searchParams),
        method: url.searchParams.get('method') || 'GET'
    };
}
```

### 3. URL 构建

构建完整的 URL：

```ts
// URL 构建示例
import { URL } from 'node:url';

function buildURL(base: string, path: string, params: Record<string, string>) {
    const url = new URL(path, base);
    Object.entries(params).forEach(([key, value]) => {
        url.searchParams.set(key, value);
    });
    return url.toString();
}
```

## 10. 注意事项与常见错误

- **URL 编码**：注意特殊字符的 URL 编码
- **相对路径**：解析相对 URL 时需要提供 base URL
- **查询参数类型**：查询参数都是字符串，需要类型转换
- **编码格式**：注意查询字符串的编码格式（UTF-8）
- **特殊字符**：处理包含特殊字符的 URL 和查询参数

## 11. 常见问题 (FAQ)

**Q: URL 和 URLSearchParams 有什么区别？**
A: URL 用于处理完整 URL，URLSearchParams 专门用于处理查询字符串部分。

**Q: 如何解析相对 URL？**
A: 使用 `new URL(path, base)` 形式，提供 base URL。

**Q: 查询参数都是字符串吗？**
A: 是的，查询参数都是字符串，需要手动转换为数字、布尔值等类型。

## 12. 最佳实践

- **使用 URL 类**：优先使用现代的 URL 类，而非旧的 `url.parse()`
- **类型转换**：查询参数需要类型转换时，明确处理
- **URL 编码**：注意 URL 编码，使用 `encodeURIComponent()` 编码参数值
- **错误处理**：处理无效 URL 的情况
- **安全性**：验证和清理 URL，防止注入攻击

## 13. 对比分析：URL vs querystring

| 维度             | URL 模块                                  | querystring 模块                          |
|:-----------------|:------------------------------------------|:------------------------------------------|
| **功能范围**     | 处理完整 URL                              | 只处理查询字符串部分                      |
| **API 设计**     | 面向对象（URL 类）                        | 函数式 API                                |
| **推荐使用**     | ✅ 推荐（现代 API）                       | 特殊场景使用                              |

## 14. 练习任务

1. **URL 解析实践**：
   - 解析不同类型的 URL
   - 提取 URL 的各个组成部分
   - 理解 URL 结构

2. **查询字符串实践**：
   - 解析查询字符串
   - 编码查询字符串
   - 处理特殊字符

3. **URL 构建实践**：
   - 构建完整的 URL
   - 添加查询参数
   - 处理相对 URL

4. **实际应用**：
   - 在实际项目中应用 URL 处理
   - 实现 API 参数解析
   - 处理 URL 路由

完成以上练习后，继续学习下一节：URL 解析与构建。

## 总结

URL 和查询字符串处理是 Web 开发的基础：

- **URL 解析**：使用 URL 类解析 URL 的各个组成部分
- **查询字符串**：使用 URLSearchParams 或 querystring 处理查询参数
- **最佳实践**：使用现代 API，注意类型转换和 URL 编码

掌握 URL 和查询字符串处理有助于构建 Web 应用和 API。

---

**最后更新**：2025-01-XX
