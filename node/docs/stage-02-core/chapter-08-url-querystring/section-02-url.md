# 2.8.2 URL 解析与构建

## 1. 概述

URL 解析与构建是处理 Web 请求的基础。Node.js 的 `url` 模块提供了 URL 类，用于解析和构建 URL。理解 URL 的组成部分和如何操作 URL 对于构建 Web 应用和 API 至关重要。

## 2. 特性说明

- **URL 解析**：将 URL 字符串解析为各个组成部分。
- **URL 构建**：从组成部分构建完整的 URL。
- **相对 URL**：支持解析相对 URL（需要 base URL）。
- **URL 修改**：可以修改 URL 的各个组成部分。
- **URL 规范化**：自动规范化 URL，处理特殊字符。

## 3. 语法与定义

### URL 类

```ts
// 解析 URL
new URL(input: string, base?: string): URL

// URL 对象属性
url.protocol: string      // 协议（如 'https:'）
url.hostname: string      // 主机名
url.port: string          // 端口
url.pathname: string      // 路径
url.search: string        // 查询字符串（含 ?）
url.hash: string          // 片段（含 #）
url.searchParams: URLSearchParams  // 查询参数对象
```

## 4. 基本用法

### 示例 1：URL 解析

```ts
// 文件: url-parse.ts
// 功能: URL 解析

import { URL } from 'node:url';

const urlString = 'https://example.com:8080/api/users?id=1&name=Alice#section';
const url = new URL(urlString);

console.log('Protocol:', url.protocol);       // https:
console.log('Hostname:', url.hostname);       // example.com
console.log('Port:', url.port);               // 8080
console.log('Host:', url.host);                // example.com:8080
console.log('Pathname:', url.pathname);       // /api/users
console.log('Search:', url.search);           // ?id=1&name=Alice
console.log('Hash:', url.hash);               // #section
console.log('Origin:', url.origin);           // https://example.com:8080
```

### 示例 2：相对 URL 解析

```ts
// 文件: url-relative.ts
// 功能: 相对 URL 解析

import { URL } from 'node:url';

const base = 'https://example.com/api/v1';
const relative = '/users?id=1';

// 解析相对 URL
const url = new URL(relative, base);
console.log('Absolute URL:', url.href);
// https://example.com/api/v1/users?id=1
```

### 示例 3：URL 构建

```ts
// 文件: url-build.ts
// 功能: URL 构建

import { URL } from 'node:url';

// 从组成部分构建 URL
const url = new URL('https://example.com');
url.pathname = '/api/users';
url.searchParams.set('id', '1');
url.searchParams.set('name', 'Alice');
url.hash = 'details';

console.log('Built URL:', url.href);
// https://example.com/api/users?id=1&name=Alice#details
```

## 5. 参数说明：URL 构造函数

### URL 构造函数参数

| 参数名       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **input**    | String   | URL 字符串（绝对或相对）                 | `'https://example.com'` 或 `'/path'`|
| **base**     | String   | 基础 URL（解析相对 URL 时必需）          | `'https://example.com'`        |

## 6. 返回值与状态说明

URL 操作的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **new URL()**| URL          | 返回 URL 对象                            |
| **url.href** | String       | 返回完整的 URL 字符串                    |
| **url.toString()**| String   | 返回完整的 URL 字符串（同 href）        |

## 7. 代码示例：URL 工具函数

以下示例演示了如何构建 URL 工具函数：

```ts
// 文件: url-utilities.ts
// 功能: URL 工具函数

import { URL } from 'node:url';

class URLBuilder {
    private url: URL;
    
    constructor(base: string) {
        this.url = new URL(base);
    }
    
    setPath(path: string): this {
        this.url.pathname = path;
        return this;
    }
    
    addParam(key: string, value: string): this {
        this.url.searchParams.set(key, value);
        return this;
    }
    
    addParams(params: Record<string, string>): this {
        Object.entries(params).forEach(([key, value]) => {
            this.url.searchParams.set(key, value);
        });
        return this;
    }
    
    setHash(hash: string): this {
        this.url.hash = hash;
        return this;
    }
    
    build(): string {
        return this.url.href;
    }
    
    getURL(): URL {
        return new URL(this.url.href);
    }
}

// 使用
const builder = new URLBuilder('https://api.example.com');
const url = builder
    .setPath('/users')
    .addParams({ page: '1', limit: '10' })
    .setHash('results')
    .build();

console.log('Built URL:', url);
```

## 8. 输出结果说明

URL 构建的输出结果：

```text
Built URL: https://api.example.com/users?page=1&limit=10#results
```

**逻辑解析**：
- 使用链式调用构建 URL
- 自动处理 URL 编码
- 返回完整的 URL 字符串

## 9. 使用场景

### 1. API 请求构建

构建 API 请求 URL：

```ts
// API 请求构建示例
function buildAPIUrl(endpoint: string, params: Record<string, string>): string {
    const url = new URL(endpoint, 'https://api.example.com');
    Object.entries(params).forEach(([key, value]) => {
        url.searchParams.set(key, value);
    });
    return url.href;
}
```

### 2. URL 路由解析

解析 URL 路由：

```ts
// URL 路由解析示例
function parseRoute(urlString: string) {
    const url = new URL(urlString);
    const segments = url.pathname.split('/').filter(Boolean);
    return {
        segments,
        params: Object.fromEntries(url.searchParams),
        hash: url.hash.slice(1) // 移除 #
    };
}
```

### 3. URL 验证和清理

验证和清理 URL：

```ts
// URL 验证和清理示例
function validateAndCleanURL(urlString: string): string | null {
    try {
        const url = new URL(urlString);
        // 验证协议
        if (!['http:', 'https:'].includes(url.protocol)) {
            return null;
        }
        // 清理路径
        url.pathname = url.pathname.replace(/\/+/g, '/');
        return url.href;
    } catch {
        return null;
    }
}
```

## 10. 注意事项与常见错误

- **相对 URL**：解析相对 URL 时必须提供 base URL
- **URL 编码**：URL 会自动编码，但需要注意特殊字符
- **协议要求**：URL 必须包含协议（http: 或 https:）
- **端口处理**：端口是字符串类型，注意类型转换
- **路径规范化**：注意路径的规范化（如 `//` 会被处理）

## 11. 常见问题 (FAQ)

**Q: 如何解析相对 URL？**
A: 使用 `new URL(path, base)` 形式，提供 base URL。

**Q: URL 对象可以修改吗？**
A: 可以，直接修改 URL 对象的属性即可。

**Q: 如何获取查询参数？**
A: 使用 `url.searchParams` 对象，它提供了 `get()`、`set()` 等方法。

## 12. 最佳实践

- **使用 URL 类**：优先使用现代的 URL 类
- **相对 URL**：解析相对 URL 时提供 base URL
- **参数管理**：使用 URLSearchParams 管理查询参数
- **错误处理**：处理无效 URL 的情况
- **URL 验证**：验证 URL 的有效性和安全性

## 13. 对比分析：URL vs url.parse

| 维度             | URL 类（现代）                            | url.parse()（旧 API）                    |
|:-----------------|:------------------------------------------|:------------------------------------------|
| **API 设计**     | 面向对象                                  | 函数式                                    |
| **类型安全**     | 更好的类型支持                            | 类型支持较差                              |
| **推荐使用**     | ✅ 推荐                                   | ❌ 已废弃                                 |
| **功能**         | 功能完整                                  | 功能有限                                  |

## 14. 练习任务

1. **URL 解析实践**：
   - 解析不同类型的 URL
   - 提取 URL 的各个组成部分
   - 理解 URL 结构

2. **URL 构建实践**：
   - 从组成部分构建 URL
   - 添加查询参数
   - 处理相对 URL

3. **URL 工具实践**：
   - 实现 URL 工具函数
   - 实现 URL 验证功能
   - 实现 URL 清理功能

4. **实际应用**：
   - 在实际项目中应用 URL 处理
   - 实现 API 请求构建
   - 处理 URL 路由

完成以上练习后，继续学习下一节：查询字符串处理。

## 总结

URL 解析与构建是 Web 开发的基础：

- **URL 类**：使用现代的 URL 类解析和构建 URL
- **组成部分**：理解 URL 的各个组成部分
- **相对 URL**：解析相对 URL 时需要 base URL
- **最佳实践**：使用 URL 类，注意错误处理和验证

掌握 URL 解析与构建有助于处理 Web 请求。

---

**最后更新**：2025-01-XX
