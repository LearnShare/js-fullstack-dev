# 2.8.4 JSON 最佳实践

## 概述

本节总结 JSON 处理的最佳实践，包括性能优化、错误处理、安全性考虑和常见问题的解决方案。

## 性能优化

### 1. 只序列化需要的属性

```js
const largeObj = {
    id: 1,
    name: "John",
    // ... 大量其他属性
    metadata: {
        // ... 大量元数据
    }
};

// 只序列化需要的属性
const json = JSON.stringify(largeObj, ['id', 'name']);
```

### 2. 使用流式解析大 JSON

对于非常大的 JSON 文件，考虑使用流式解析：

```js
// 使用第三方库如 JSONStream 进行流式解析
// 示例：使用 Node.js 流
import { createReadStream } from 'node:fs';
import { parse } from 'jsonstream';

const stream = createReadStream('large.json')
    .pipe(parse('*'));
```

### 3. 缓存序列化结果

```js
const cache = new WeakMap();

function getCachedStringify(obj) {
    if (cache.has(obj)) {
        return cache.get(obj);
    }
    
    const json = JSON.stringify(obj);
    cache.set(obj, json);
    return json;
}
```

## 错误处理

### 统一的错误处理函数

```js
function safeStringify(obj, defaultValue = '{}') {
    try {
        return JSON.stringify(obj);
    } catch (e) {
        console.error('序列化失败:', e.message);
        return defaultValue;
    }
}

function safeParse(jsonString, defaultValue = null) {
    try {
        return JSON.parse(jsonString);
    } catch (e) {
        console.error('解析失败:', e.message);
        return defaultValue;
    }
}
```

### 验证 JSON 格式

```js
function isValidJSON(str) {
    try {
        JSON.parse(str);
        return true;
    } catch (e) {
        return false;
    }
}

function validateAndParse(jsonString) {
    if (!isValidJSON(jsonString)) {
        throw new Error('无效的 JSON 格式');
    }
    return JSON.parse(jsonString);
}
```

## 安全性考虑

### 1. 不要解析不可信的数据

```js
// 危险：解析用户输入
const userInput = getUserInput();
const data = JSON.parse(userInput);  // 可能包含恶意代码

// 安全：验证和清理
function safeParseUserInput(input) {
    // 验证输入长度
    if (input.length > 10000) {
        throw new Error('输入过长');
    }
    
    // 验证基本格式
    if (!input.trim().startsWith('{') && !input.trim().startsWith('[')) {
        throw new Error('无效的 JSON 格式');
    }
    
    try {
        return JSON.parse(input);
    } catch (e) {
        throw new Error('JSON 解析失败');
    }
}
```

### 2. 限制解析深度

```js
function parseWithDepthLimit(jsonString, maxDepth = 10) {
    let depth = 0;
    
    return JSON.parse(jsonString, function(key, value) {
        if (typeof value === 'object' && value !== null) {
            depth++;
            if (depth > maxDepth) {
                throw new Error('JSON 嵌套过深');
            }
        }
        return value;
    });
}
```

## 数据转换模式

### 1. 自定义序列化

```js
class User {
    constructor(name, password) {
        this.name = name;
        this.password = password;
    }
    
    toJSON() {
        return {
            name: this.name
            // password 被排除
        };
    }
}

const user = new User('John', 'secret');
console.log(JSON.stringify(user));
// 输出: {"name":"John"}
```

### 2. 处理循环引用

```js
function stringifyWithCircular(obj) {
    const seen = new WeakSet();
    
    return JSON.stringify(obj, function(key, value) {
        if (typeof value === 'object' && value !== null) {
            if (seen.has(value)) {
                return '[Circular]';
            }
            seen.add(value);
        }
        return value;
    });
}
```

### 3. 处理特殊类型

```js
function stringifyWithSpecialTypes(obj) {
    return JSON.stringify(obj, function(key, value) {
        // 处理 Date
        if (value instanceof Date) {
            return {
                __type: 'Date',
                __value: value.toISOString()
            };
        }
        
        // 处理 RegExp
        if (value instanceof RegExp) {
            return {
                __type: 'RegExp',
                __value: value.toString()
            };
        }
        
        return value;
    });
}

function parseWithSpecialTypes(jsonString) {
    return JSON.parse(jsonString, function(key, value) {
        if (value && value.__type === 'Date') {
            return new Date(value.__value);
        }
        if (value && value.__type === 'RegExp') {
            const match = value.__value.match(/\/(.*)\/([gimuy]*)/);
            return new RegExp(match[1], match[2]);
        }
        return value;
    });
}
```

## 格式化与可读性

### 开发环境格式化

```js
// 开发环境：格式化输出
const isDevelopment = process.env.NODE_ENV === 'development';

function stringify(obj) {
    return JSON.stringify(
        obj,
        null,
        isDevelopment ? 2 : 0
    );
}
```

### 自定义格式化

```js
function prettyStringify(obj, indent = 2) {
    return JSON.stringify(obj, null, indent)
        .replace(/\n/g, '\n')
        .replace(/^/gm, '  ');  // 额外缩进
}
```

## 常见问题解决方案

### 问题 1：处理 undefined

```js
// 方案 1：转换为 null
function stringifyWithUndefined(obj) {
    return JSON.stringify(obj, function(key, value) {
        return value === undefined ? null : value;
    });
}

// 方案 2：使用特殊标记
function stringifyWithUndefinedMarker(obj) {
    return JSON.stringify(obj, function(key, value) {
        return value === undefined ? '__UNDEFINED__' : value;
    });
}
```

### 问题 2：处理大数字精度

```js
// JSON 中的大数字可能丢失精度
const bigNumber = 9007199254740993;  // 超过 Number.MAX_SAFE_INTEGER

// 解决方案：使用字符串
const obj = {
    id: bigNumber.toString()
};

const json = JSON.stringify(obj);
const parsed = JSON.parse(json, function(key, value) {
    if (key === 'id' && typeof value === 'string') {
        return BigInt(value);
    }
    return value;
});
```

### 问题 3：处理特殊字符

```js
// JSON 自动转义特殊字符
const obj = {
    text: 'Line 1\nLine 2\tTab "Quote"'
};

const json = JSON.stringify(obj);
console.log(json);
// 输出: {"text":"Line 1\nLine 2\tTab \"Quote\""}

// 解析时自动还原
const parsed = JSON.parse(json);
console.log(parsed.text);
// 输出: Line 1
//       Line 2	Tab "Quote"
```

## 最佳实践总结

1. **性能优化**
   - 只序列化需要的属性
   - 缓存序列化结果
   - 对大 JSON 使用流式解析

2. **错误处理**
   - 始终使用 try-catch
   - 提供默认值
   - 验证输入格式

3. **安全性**
   - 不要解析不可信数据
   - 限制解析深度和大小
   - 验证和清理输入

4. **数据转换**
   - 使用 `toJSON()` 自定义序列化
   - 使用 `reviver` 自定义反序列化
   - 处理特殊类型和循环引用

5. **可读性**
   - 开发环境使用格式化
   - 生产环境去除格式化以节省空间

## 练习任务

1. 实现一个安全的 JSON 解析函数，包含输入验证、错误处理和默认值。

2. 创建一个处理循环引用的 JSON 序列化函数。

3. 实现一个 JSON 工具类，包含序列化、反序列化、验证和格式化功能。

4. 创建一个函数，将包含 Date 和 RegExp 的对象序列化为 JSON，并能正确还原。

5. 实现一个性能优化的 JSON 序列化函数，支持属性过滤和结果缓存。
