# 2.8.3 查询字符串处理

## 1. 概述

查询字符串是 URL 中用于传递参数的部分，格式为 `?key=value&key2=value2`。Node.js 提供了 `querystring` 模块和 `URLSearchParams` 类来处理查询字符串的编码和解码。理解查询字符串的处理对于构建 Web 应用和 API 至关重要。

## 2. 特性说明

- **查询解析**：将查询字符串解析为对象。
- **查询编码**：将对象编码为查询字符串。
- **参数管理**：支持添加、删除、修改查询参数。
- **URL 编码**：自动处理 URL 编码和解码。
- **类型处理**：注意查询参数都是字符串类型。

## 3. 语法与定义

### querystring 模块

```ts
// 解析查询字符串
querystring.parse(str: string, sep?: string, eq?: string, options?: object): object

// 编码为查询字符串
querystring.stringify(obj: object, sep?: string, eq?: string, options?: object): string
```

### URLSearchParams 类

```ts
// 创建 URLSearchParams
new URLSearchParams(init?: string | object): URLSearchParams

// 操作方法
params.get(name: string): string | null
params.set(name: string, value: string): void
params.append(name: string, value: string): void
params.delete(name: string): void
params.has(name: string): boolean
params.toString(): string
```

## 4. 基本用法

### 示例 1：querystring 模块

```ts
// 文件: querystring-basic.ts
// 功能: querystring 模块基本用法

import querystring from 'node:querystring';

// 解析查询字符串
const query = 'name=Alice&age=25&city=Beijing';
const params = querystring.parse(query);
console.log('Parsed:', params);
// { name: 'Alice', age: '25', city: 'Beijing' }

// 编码为查询字符串
const obj = { name: 'Alice', age: 25, city: 'Beijing' };
const encoded = querystring.stringify(obj);
console.log('Encoded:', encoded);
// name=Alice&age=25&city=Beijing

// URL 编码处理
const encoded2 = querystring.stringify({ name: 'Alice Smith', city: 'New York' });
console.log('URL Encoded:', encoded2);
// name=Alice%20Smith&city=New%20York
```

### 示例 2：URLSearchParams 类

```ts
// 文件: querystring-urlsearchparams.ts
// 功能: URLSearchParams 类用法

import { URLSearchParams } from 'node:url';

// 从字符串创建
const params1 = new URLSearchParams('name=Alice&age=25');
console.log('Name:', params1.get('name'));        // Alice
console.log('Age:', params1.get('age'));          // 25

// 从对象创建
const params2 = new URLSearchParams({ name: 'Bob', age: '30' });
console.log('Params:', params2.toString());       // name=Bob&age=30

// 添加参数
params2.append('city', 'Shanghai');
params2.set('age', '31'); // 更新现有参数
console.log('Updated:', params2.toString());

// 删除参数
params2.delete('city');
console.log('After delete:', params2.toString());

// 检查参数
console.log('Has name:', params2.has('name'));     // true
console.log('Has city:', params2.has('city'));    // false
```

### 示例 3：处理数组参数

```ts
// 文件: querystring-array.ts
// 功能: 处理数组参数

import querystring from 'node:querystring';

// 解析包含数组的查询字符串
const query = 'tags=javascript&tags=nodejs&tags=typescript';
const params = querystring.parse(query);
console.log('Tags:', params.tags); // ['javascript', 'nodejs', 'typescript']

// 编码数组参数
const obj = {
    name: 'Alice',
    tags: ['javascript', 'nodejs', 'typescript']
};
const encoded = querystring.stringify(obj);
console.log('Encoded:', encoded);
```

## 5. 参数说明：查询字符串方法参数

### parse 方法参数

| 参数名       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **str**      | String   | 查询字符串（不含 ?）                     | `'name=Alice&age=25'`          |
| **sep**      | String   | 分隔符（默认 `&`）                       | `';'`                          |
| **eq**       | String   | 等号（默认 `=`）                         | `':'`                           |
| **options**  | Object   | 选项（如 `decodeURIComponent`）         | `{ decodeURIComponent: ... }`  |

### stringify 方法参数

| 参数名       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **obj**      | Object   | 要编码的对象                             | `{ name: 'Alice' }`            |
| **sep**      | String   | 分隔符（默认 `&`）                       | `';'`                          |
| **eq**       | String   | 等号（默认 `=`）                         | `':'`                           |
| **options**  | Object   | 选项（如 `encodeURIComponent`）          | `{ encodeURIComponent: ... }`  |

## 6. 返回值与状态说明

查询字符串操作的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **parse**    | Object       | 返回包含查询参数的对象                   |
| **stringify**| String       | 返回编码后的查询字符串                   |
| **get**      | String/null  | 返回参数值或 null                        |
| **has**      | Boolean      | 返回参数是否存在                         |

## 7. 代码示例：完整的查询字符串工具

以下示例演示了如何构建完整的查询字符串工具：

```ts
// 文件: querystring-complete.ts
// 功能: 完整的查询字符串工具

import { URLSearchParams } from 'node:url';

class QueryStringManager {
    private params: URLSearchParams;
    
    constructor(query?: string | Record<string, string>) {
        this.params = new URLSearchParams(query);
    }
    
    get(key: string): string | null {
        return this.params.get(key);
    }
    
    getNumber(key: string): number | null {
        const value = this.params.get(key);
        return value ? parseInt(value, 10) : null;
    }
    
    getBoolean(key: string): boolean | null {
        const value = this.params.get(key);
        if (value === null) return null;
        return value === 'true' || value === '1';
    }
    
    set(key: string, value: string | number | boolean): this {
        this.params.set(key, String(value));
        return this;
    }
    
    append(key: string, value: string): this {
        this.params.append(key, value);
        return this;
    }
    
    delete(key: string): this {
        this.params.delete(key);
        return this;
    }
    
    has(key: string): boolean {
        return this.params.has(key);
    }
    
    getAll(key: string): string[] {
        return this.params.getAll(key);
    }
    
    toObject(): Record<string, string | string[]> {
        const obj: Record<string, string | string[]> = {};
        for (const [key, value] of this.params) {
            const values = this.params.getAll(key);
            obj[key] = values.length === 1 ? values[0] : values;
        }
        return obj;
    }
    
    toString(): string {
        return this.params.toString();
    }
}

// 使用
const qs = new QueryStringManager('name=Alice&age=25&tags=js&tags=ts');

console.log('Name:', qs.get('name'));
console.log('Age:', qs.getNumber('age'));
console.log('Tags:', qs.getAll('tags'));
console.log('Object:', qs.toObject());
```

## 8. 输出结果说明

查询字符串处理的输出结果：

```text
Name: Alice
Age: 25
Tags: ['js', 'ts']
Object: { name: 'Alice', age: '25', tags: ['js', 'ts'] }
```

**逻辑解析**：
- `get()` 获取单个参数值
- `getAll()` 获取所有同名参数值（数组）
- `getNumber()` 和 `getBoolean()` 进行类型转换
- `toObject()` 转换为对象，处理数组参数

## 9. 使用场景

### 1. HTTP 请求参数解析

解析 HTTP 请求的查询参数：

```ts
// HTTP 请求参数解析示例
import http from 'node:http';
import { URL } from 'node:url';

const server = http.createServer((req, res) => {
    if (!req.url) return;
    
    const url = new URL(req.url, `http://${req.headers.host}`);
    const params = Object.fromEntries(url.searchParams);
    
    // 类型转换
    const page = parseInt(params.page || '1', 10);
    const limit = parseInt(params.limit || '10', 10);
    
    console.log('Page:', page, 'Limit:', limit);
});
```

### 2. API 参数构建

构建 API 请求的查询参数：

```ts
// API 参数构建示例
function buildAPIQuery(params: Record<string, any>): string {
    const qs = new URLSearchParams();
    
    Object.entries(params).forEach(([key, value]) => {
        if (Array.isArray(value)) {
            value.forEach(v => qs.append(key, String(v)));
        } else if (value !== null && value !== undefined) {
            qs.set(key, String(value));
        }
    });
    
    return qs.toString();
}
```

### 3. URL 重定向

构建带查询参数的 URL：

```ts
// URL 重定向示例
function buildRedirectURL(base: string, params: Record<string, string>): string {
    const url = new URL(base);
    Object.entries(params).forEach(([key, value]) => {
        url.searchParams.set(key, value);
    });
    return url.href;
}
```

## 10. 注意事项与常见错误

- **类型转换**：查询参数都是字符串，需要手动转换为数字、布尔值等
- **数组参数**：处理数组参数时使用 `getAll()` 或 `append()`
- **URL 编码**：注意特殊字符的 URL 编码
- **空值处理**：处理空值和 undefined 的情况
- **参数验证**：验证查询参数的有效性

## 11. 常见问题 (FAQ)

**Q: 查询参数都是字符串吗？**
A: 是的，查询参数都是字符串，需要手动转换为其他类型。

**Q: 如何处理数组参数？**
A: 使用 `getAll()` 获取所有同名参数，或使用 `append()` 添加多个同名参数。

**Q: URLSearchParams 和 querystring 有什么区别？**
A: URLSearchParams 是现代的 API，功能更强大；querystring 是旧 API，但更轻量。

## 12. 最佳实践

- **使用 URLSearchParams**：优先使用 URLSearchParams，功能更强大
- **类型转换**：明确处理查询参数的类型转换
- **参数验证**：验证查询参数的有效性
- **URL 编码**：注意 URL 编码，使用 `encodeURIComponent()` 编码参数值
- **错误处理**：处理无效查询字符串的情况

## 13. 对比分析：URLSearchParams vs querystring

| 维度             | URLSearchParams                           | querystring                                |
|:-----------------|:------------------------------------------|:-------------------------------------------|
| **API 设计**     | 面向对象，方法丰富                        | 函数式，简单直接                            |
| **功能**         | 功能完整，支持迭代                        | 功能基础                                    |
| **推荐使用**     | ✅ 推荐（现代 API）                       | 特殊场景使用                                |
| **类型支持**     | 更好的类型支持                            | 类型支持有限                                |

## 14. 练习任务

1. **查询字符串解析实践**：
   - 解析不同类型的查询字符串
   - 处理数组参数
   - 理解参数类型

2. **查询字符串编码实践**：
   - 将对象编码为查询字符串
   - 处理特殊字符
   - 处理数组参数

3. **参数管理实践**：
   - 使用 URLSearchParams 管理参数
   - 实现参数类型转换
   - 实现参数验证

4. **实际应用**：
   - 在实际项目中应用查询字符串处理
   - 实现 API 参数解析
   - 实现 URL 构建功能

完成以上练习后，继续学习下一章：工具函数（util）。

## 总结

查询字符串处理是 Web 开发的基础：

- **解析和编码**：使用 URLSearchParams 或 querystring 处理查询字符串
- **类型转换**：查询参数都是字符串，需要类型转换
- **参数管理**：使用 URLSearchParams 管理查询参数
- **最佳实践**：使用现代 API，注意类型转换和 URL 编码

掌握查询字符串处理有助于构建 Web 应用和 API。

---

**最后更新**：2025-01-XX
