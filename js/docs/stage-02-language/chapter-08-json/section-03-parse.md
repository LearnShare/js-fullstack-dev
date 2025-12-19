# 2.8.3 JSON.parse

## 概述

`JSON.parse()` 方法将 JSON 字符串解析为 JavaScript 值。这是反序列化 JSON 数据的标准方法，常用于处理 API 响应、读取配置文件等场景。

## 语法

```js
JSON.parse(text[, reviver])
```

## 参数详述

| 参数名    | 类型     | 说明                                    | 是否必需 | 默认值 |
|:----------|:---------|:----------------------------------------|:---------|:-------|
| `text`    | string   | 要解析的 JSON 字符串                     | 是       | -      |
| `reviver` | Function | 用于转换解析结果的函数                   | 否       | -      |

## 返回值

返回解析后的 JavaScript 值（对象、数组、字符串、数字、布尔值或 `null`）。

## 基本用法

### 解析对象

```js
const json = '{"name":"John","age":30,"city":"Beijing"}';
const obj = JSON.parse(json);

console.log(obj);
// 输出: { name: 'John', age: 30, city: 'Beijing' }

console.log(obj.name);  // "John"
console.log(obj.age);   // 30
```

### 解析数组

```js
const json = '[1,2,3,"hello",true]';
const arr = JSON.parse(json);

console.log(arr);
// 输出: [1, 2, 3, 'hello', true]

console.log(arr[0]);  // 1
console.log(arr[3]); // "hello"
```

### 解析基本类型

```js
console.log(JSON.parse('"hello"'));  // "hello"
console.log(JSON.parse('42'));       // 42
console.log(JSON.parse('true'));     // true
console.log(JSON.parse('null'));     // null
```

## reviver 参数

`reviver` 函数可以在解析过程中转换值。函数接收两个参数：键名和值。

### 转换日期字符串

```js
const json = '{"name":"John","createdAt":"2025-12-19T10:30:00.000Z"}';

const obj = JSON.parse(json, function(key, value) {
    // 将 ISO 日期字符串转换为 Date 对象
    if (key === 'createdAt' && typeof value === 'string') {
        return new Date(value);
    }
    return value;
});

console.log(obj.createdAt instanceof Date);  // true
console.log(obj.createdAt.toLocaleDateString());  // "2025/12/19"
```

### 转换数字格式

```js
const json = '{"price":"99.99","quantity":"10"}';

const obj = JSON.parse(json, function(key, value) {
    // 将字符串数字转换为数字类型
    if ((key === 'price' || key === 'quantity') && typeof value === 'string') {
        return parseFloat(value);
    }
    return value;
});

console.log(typeof obj.price);     // "number"
console.log(typeof obj.quantity);  // "number"
```

### 过滤或转换特定值

```js
const json = '{"name":"John","age":30,"status":"active"}';

const obj = JSON.parse(json, function(key, value) {
    // 将 status 转换为布尔值
    if (key === 'status') {
        return value === 'active';
    }
    return value;
});

console.log(obj.status);  // true（布尔值）
```

## 错误处理

### 语法错误

```js
try {
    const obj = JSON.parse('{name: "John"}');  // 键名缺少引号
} catch (e) {
    console.error('解析错误:', e.message);
    // 输出: 解析错误: Expected property name or '}' in JSON at position 1
}
```

### 常见错误类型

| 错误类型           | 原因                           | 示例                          |
|:------------------|:-------------------------------|:------------------------------|
| SyntaxError        | JSON 格式不正确                 | `{name: "John"}`（键名无引号）|
| SyntaxError        | 尾随逗号                       | `{"name": "John",}`           |
| SyntaxError        | 单引号字符串                   | `{'name': 'John'}`            |
| SyntaxError        | 注释                           | `{"name": "John" // comment}` |

### 安全解析函数

```js
function safeParse(jsonString, defaultValue = null) {
    try {
        return JSON.parse(jsonString);
    } catch (e) {
        console.error('JSON 解析失败:', e.message);
        return defaultValue;
    }
}

const obj1 = safeParse('{"name":"John"}');
console.log(obj1);  // { name: 'John' }

const obj2 = safeParse('invalid json', {});
console.log(obj2);  // {}（返回默认值）
```

## 解析嵌套结构

### 复杂对象

```js
const json = `{
    "user": {
        "id": 1,
        "name": "John",
        "address": {
            "city": "Beijing",
            "country": "China"
        }
    },
    "posts": [
        {"id": 1, "title": "Post 1"},
        {"id": 2, "title": "Post 2"}
    ]
}`;

const data = JSON.parse(json);

console.log(data.user.name);              // "John"
console.log(data.user.address.city);      // "Beijing"
console.log(data.posts[0].title);        // "Post 1"
```

### 数组中的对象

```js
const json = '[{"id":1,"name":"John"},{"id":2,"name":"Jane"}]';
const users = JSON.parse(json);

users.forEach(user => {
    console.log(`${user.id}: ${user.name}`);
});
// 输出:
// 1: John
// 2: Jane
```

## 性能考虑

### 大 JSON 字符串

对于大 JSON 字符串，解析可能较慢：

```js
// 如果 JSON 很大，考虑使用流式解析或分批处理
function parseLargeJSON(jsonString) {
    try {
        return JSON.parse(jsonString);
    } catch (e) {
        // 处理错误
        throw new Error('无法解析大 JSON 文件');
    }
}
```

### 缓存解析结果

```js
const parseCache = new Map();

function cachedParse(jsonString) {
    if (parseCache.has(jsonString)) {
        return parseCache.get(jsonString);
    }
    
    const result = JSON.parse(jsonString);
    parseCache.set(jsonString, result);
    return result;
}
```

## 与 JSON.stringify 配合使用

### 深拷贝对象

```js
const original = {
    name: "John",
    age: 30,
    address: {
        city: "Beijing"
    }
};

// 使用 JSON 序列化和反序列化实现深拷贝
const copy = JSON.parse(JSON.stringify(original));

copy.address.city = "Shanghai";

console.log(original.address.city);  // "Beijing"（未改变）
console.log(copy.address.city);      // "Shanghai"
```

**注意**：这种方法有局限性：
- 不能处理函数、`undefined`、Symbol
- 不能处理循环引用
- Date 对象会变成字符串

## 注意事项

1. **格式严格**：JSON 字符串必须严格符合 JSON 规范
2. **安全性**：解析不可信的 JSON 数据时要注意安全性（可能包含恶意代码）
3. **性能**：大 JSON 字符串解析可能较慢
4. **类型转换**：数字可能丢失精度
5. **Date 对象**：日期字符串不会自动转换为 Date 对象

## 常见问题

### 问题 1：如何解析包含 Date 的 JSON？

使用 `reviver` 函数：

```js
const json = '{"date":"2025-12-19T10:30:00.000Z"}';

const obj = JSON.parse(json, function(key, value) {
    if (key === 'date' && typeof value === 'string') {
        return new Date(value);
    }
    return value;
});
```

### 问题 2：如何处理解析错误？

使用 try-catch：

```js
try {
    const obj = JSON.parse(jsonString);
} catch (e) {
    if (e instanceof SyntaxError) {
        console.error('JSON 格式错误:', e.message);
    } else {
        console.error('其他错误:', e);
    }
}
```

### 问题 3：可以解析包含函数的 JSON 吗？

不可以。JSON 不支持函数。如果需要，可以在解析后手动添加：

```js
const json = '{"name":"John"}';
const obj = JSON.parse(json);

// 解析后添加函数
obj.greet = function() {
    return `Hello, ${this.name}!`;
};
```

## 最佳实践

1. **错误处理**：始终使用 try-catch 处理解析错误
2. **验证输入**：解析前验证 JSON 字符串格式
3. **使用 reviver**：利用 `reviver` 进行类型转换
4. **性能优化**：对于大 JSON，考虑流式解析
5. **安全性**：不要解析不可信的 JSON 数据

## 练习任务

1. 解析一个包含用户信息的 JSON 字符串，并使用 `reviver` 将日期字符串转换为 Date 对象。

2. 创建一个安全解析函数，解析失败时返回默认值而不是抛出错误。

3. 解析一个包含嵌套对象的 JSON 字符串，并访问深层属性。

4. 实现一个函数，解析 JSON 字符串并自动将字符串数字转换为数字类型。

5. 使用 `JSON.parse()` 和 `JSON.stringify()` 实现对象的深拷贝功能。
