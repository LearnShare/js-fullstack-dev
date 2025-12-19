# 2.8.1 JSON 概述

## 概述

JSON（JavaScript Object Notation）是一种轻量级的数据交换格式，基于 JavaScript 对象字面量语法，但独立于编程语言。JSON 易于人类阅读和编写，也易于机器解析和生成。

## 特性

- **轻量级**：相比 XML 等格式，JSON 更加简洁
- **文本格式**：基于文本，易于传输和存储
- **语言无关**：虽然源自 JavaScript，但被多种编程语言支持
- **结构化数据**：支持对象、数组等复杂数据结构
- **广泛支持**：现代编程语言和工具都支持 JSON

## JSON 语法规则

### 基本数据类型

JSON 支持以下数据类型：

| 类型     | 说明                     | 示例              |
|:---------|:-------------------------|:------------------|
| 字符串   | 必须使用双引号           | `"hello"`         |
| 数字     | 整数或浮点数             | `42`、`3.14`      |
| 布尔值   | `true` 或 `false`        | `true`            |
| `null`   | 空值                     | `null`            |
| 对象     | 键值对集合，使用 `{}`    | `{"key": "value"}`|
| 数组     | 有序值列表，使用 `[]`    | `[1, 2, 3]`       |

### 对象语法

```json
{
    "name": "John",
    "age": 30,
    "isActive": true,
    "address": {
        "city": "Beijing",
        "country": "China"
    }
}
```

### 数组语法

```json
[
    "apple",
    "banana",
    "orange"
]
```

### 混合结构

```json
{
    "users": [
        {
            "id": 1,
            "name": "John",
            "email": "john@example.com"
        },
        {
            "id": 2,
            "name": "Jane",
            "email": "jane@example.com"
        }
    ],
    "total": 2
}
```

## JSON 与 JavaScript 对象的区别

| 特性           | JSON                    | JavaScript 对象        |
|:---------------|:------------------------|:-----------------------|
| 键名           | 必须使用双引号           | 可以使用单引号或不加引号 |
| 字符串值       | 必须使用双引号           | 可以使用单引号或双引号   |
| 注释           | 不支持                   | 支持                   |
| 函数           | 不支持                   | 支持                   |
| `undefined`    | 不支持                   | 支持                   |
| 日期对象       | 不支持（需转换为字符串）  | 支持                   |
| 尾随逗号       | 不支持                   | 支持（ES2017+）        |

### 示例对比

**JavaScript 对象**：

```js
const obj = {
    name: "John",           // 键名可以不加引号
    age: 30,
    greet: function() {     // 可以包含函数
        return "Hello";
    },
    date: new Date(),       // 可以包含 Date 对象
    undefined: undefined    // 可以包含 undefined
};
```

**JSON 格式**：

```json
{
    "name": "John",         // 键名必须使用双引号
    "age": 30
    // 不能包含函数、Date 对象、undefined
}
```

## JSON 的用途

### 1. 数据交换

前后端数据交换的标准格式：

```js
// 前端发送数据
const data = {
    username: "john",
    password: "secret"
};

fetch('/api/login', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
});
```

### 2. 配置文件

许多工具使用 JSON 作为配置文件格式：

```json
{
    "name": "my-project",
    "version": "1.0.0",
    "scripts": {
        "start": "node index.js",
        "test": "jest"
    },
    "dependencies": {
        "express": "^4.18.0"
    }
}
```

### 3. 数据存储

在 localStorage 中存储数据：

```js
const user = {
    name: "John",
    preferences: {
        theme: "dark",
        language: "zh-CN"
    }
};

// 存储
localStorage.setItem('user', JSON.stringify(user));

// 读取
const stored = JSON.parse(localStorage.getItem('user'));
```

### 4. API 响应

RESTful API 通常返回 JSON 格式：

```js
// API 响应示例
{
    "status": "success",
    "data": {
        "users": [
            {"id": 1, "name": "John"},
            {"id": 2, "name": "Jane"}
        ]
    },
    "message": "Users retrieved successfully"
}
```

## JSON 验证

### 在线验证工具

可以使用在线工具验证 JSON 格式：

- JSONLint：https://jsonlint.com/
- JSON Formatter：https://jsonformatter.org/

### 手动验证

```js
function isValidJSON(str) {
    try {
        JSON.parse(str);
        return true;
    } catch (e) {
        return false;
    }
}

console.log(isValidJSON('{"name": "John"}'));  // true
console.log(isValidJSON('{name: "John"}'));    // false（键名缺少引号）
console.log(isValidJSON('{"name": "John"'));   // false（缺少闭合括号）
```

## 常见错误

### 错误 1：键名未使用双引号

```json
// 错误
{
    name: "John"
}

// 正确
{
    "name": "John"
}
```

### 错误 2：字符串值使用单引号

```json
// 错误
{
    "name": 'John'
}

// 正确
{
    "name": "John"
}
```

### 错误 3：尾随逗号

```json
// 错误
{
    "name": "John",
    "age": 30,
}

// 正确
{
    "name": "John",
    "age": 30
}
```

### 错误 4：包含注释

```json
// 错误
{
    "name": "John"  // 这是注释
}

// 正确（JSON 不支持注释）
{
    "name": "John"
}
```

## 注意事项

1. **严格语法**：JSON 语法非常严格，任何格式错误都会导致解析失败
2. **字符编码**：JSON 必须使用 UTF-8 编码
3. **性能考虑**：大 JSON 文件的解析可能影响性能
4. **安全性**：解析不可信的 JSON 数据时要注意安全性

## 常见问题

### 问题 1：JSON 支持哪些数据类型？

JSON 支持字符串、数字、布尔值、`null`、对象和数组。不支持函数、`undefined`、Date 对象等 JavaScript 特有类型。

### 问题 2：JSON 可以包含注释吗？

不可以。JSON 规范不支持注释。如果需要注释，可以在数据外部添加说明文档。

### 问题 3：JSON 键名必须使用双引号吗？

是的。JSON 规范要求键名必须使用双引号，不能使用单引号或不加引号。

### 问题 4：如何表示日期？

JSON 不支持 Date 对象，通常将日期转换为 ISO 8601 格式的字符串：

```json
{
    "createdAt": "2025-12-19T10:30:00.000Z"
}
```

## 最佳实践

1. **使用工具验证**：在开发过程中使用 JSON 验证工具检查格式
2. **统一编码**：确保 JSON 文件使用 UTF-8 编码
3. **格式化输出**：使用 `JSON.stringify()` 的第三个参数进行格式化
4. **错误处理**：解析 JSON 时始终使用 try-catch 处理错误
5. **性能优化**：对于大 JSON 文件，考虑使用流式解析

## 练习任务

1. 编写一个包含用户信息的 JSON 对象，包括姓名、年龄、邮箱和地址（嵌套对象）。

2. 编写一个包含商品列表的 JSON 数组，每个商品包含 id、名称、价格和库存。

3. 创建一个函数，验证字符串是否为有效的 JSON 格式。

4. 编写一个 JSON 对象，表示一个博客文章，包括标题、作者、发布日期、标签数组和内容。

5. 创建一个包含错误信息的 JSON 对象，用于 API 错误响应，包括错误代码、错误消息和详细信息。
