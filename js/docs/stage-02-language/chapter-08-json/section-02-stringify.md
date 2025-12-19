# 2.8.2 JSON.stringify

## 概述

`JSON.stringify()` 方法将 JavaScript 值转换为 JSON 字符串。这是序列化 JavaScript 对象的标准方法，常用于数据存储、网络传输和日志记录。

## 语法

```js
JSON.stringify(value[, replacer[, space]])
```

## 参数详述

| 参数名    | 类型                    | 说明                                 | 是否必需 | 默认值 |
|:----------|:------------------------|:-------------------------------------|:---------|:-------|
| `value`   | any                     | 要转换为 JSON 字符串的值              | 是       | -      |
| `replacer`| Function \| Array \| null | 用于转换结果的函数或数组              | 否       | null   |
| `space`   | Number \| String        | 用于缩进的空格数或字符串              | 否       | 0      |

## 返回值

返回表示给定值的 JSON 字符串。

## 基本用法

### 转换对象

```js
const obj = {
    name: "John",
    age: 30,
    city: "Beijing"
};

const json = JSON.stringify(obj);
console.log(json);
// 输出: {"name":"John","age":30,"city":"Beijing"}
```

### 转换数组

```js
const arr = [1, 2, 3, "hello", true];
const json = JSON.stringify(arr);
console.log(json);
// 输出: [1,2,3,"hello",true]
```

### 转换基本类型

```js
console.log(JSON.stringify("hello"));     // "hello"
console.log(JSON.stringify(42));            // 42
console.log(JSON.stringify(true));         // true
console.log(JSON.stringify(null));         // null
console.log(JSON.stringify(undefined));    // undefined（注意：会被忽略）
```

## 格式化输出

### 使用 space 参数

```js
const obj = {
    name: "John",
    age: 30,
    address: {
        city: "Beijing",
        country: "China"
    }
};

// 不格式化
console.log(JSON.stringify(obj));
// 输出: {"name":"John","age":30,"address":{"city":"Beijing","country":"China"}}

// 使用 2 个空格缩进
console.log(JSON.stringify(obj, null, 2));
// 输出:
// {
//   "name": "John",
//   "age": 30,
//   "address": {
//     "city": "Beijing",
//     "country": "China"
//   }
// }

// 使用制表符缩进
console.log(JSON.stringify(obj, null, '\t'));
// 输出:
// {
// 	"name": "John",
// 	"age": 30,
// 	"address": {
// 		"city": "Beijing",
// 		"country": "China"
// 	}
// }
```

### space 参数限制

- 数字：最大值为 10，超过 10 会被截断为 10
- 字符串：最多使用前 10 个字符

```js
const obj = { name: "John" };

console.log(JSON.stringify(obj, null, 20));  // 实际使用 10 个空格
console.log(JSON.stringify(obj, null, "---")); // 使用 "---" 作为缩进
```

## replacer 参数

### 使用数组过滤属性

```js
const obj = {
    name: "John",
    age: 30,
    email: "john@example.com",
    password: "secret"
};

// 只包含 name 和 age
const json = JSON.stringify(obj, ['name', 'age']);
console.log(json);
// 输出: {"name":"John","age":30}
```

### 使用函数转换值

```js
const obj = {
    name: "John",
    age: 30,
    password: "secret",
    date: new Date()
};

const json = JSON.stringify(obj, function(key, value) {
    // 过滤掉 password
    if (key === 'password') {
        return undefined;
    }
    
    // 将 Date 对象转换为字符串
    if (value instanceof Date) {
        return value.toISOString();
    }
    
    return value;
});

console.log(json);
// 输出: {"name":"John","age":30,"date":"2025-12-19T10:30:00.000Z"}
```

### replacer 函数的返回值

- 返回 `undefined`：该属性会被忽略
- 返回其他值：使用返回值替换原值

```js
const obj = {
    name: "John",
    age: 30,
    score: 95
};

const json = JSON.stringify(obj, function(key, value) {
    if (key === 'score') {
        return value >= 90 ? '优秀' : '良好';
    }
    return value;
});

console.log(json);
// 输出: {"name":"John","age":30,"score":"优秀"}
```

## 不支持的数据类型

### undefined

```js
const obj = {
    name: "John",
    age: undefined
};

console.log(JSON.stringify(obj));
// 输出: {"name":"John"}（age 被忽略）
```

### 函数

```js
const obj = {
    name: "John",
    greet: function() {
        return "Hello";
    }
};

console.log(JSON.stringify(obj));
// 输出: {"name":"John"}（greet 被忽略）
```

### Symbol

```js
const obj = {
    name: "John",
    id: Symbol('id')
};

console.log(JSON.stringify(obj));
// 输出: {"name":"John"}（id 被忽略）
```

### Date 对象

```js
const obj = {
    name: "John",
    date: new Date()
};

console.log(JSON.stringify(obj));
// 输出: {"name":"John","date":"2025-12-19T10:30:00.000Z"}
// Date 对象会被转换为 ISO 8601 格式的字符串
```

## toJSON 方法

对象可以实现 `toJSON()` 方法来自定义序列化行为：

```js
const user = {
    name: "John",
    age: 30,
    password: "secret",
    toJSON() {
        return {
            name: this.name,
            age: this.age
            // password 被排除
        };
    }
};

console.log(JSON.stringify(user));
// 输出: {"name":"John","age":30}
```

## 循环引用处理

### 问题

```js
const obj = {};
obj.self = obj;

// 会抛出错误
try {
    JSON.stringify(obj);
} catch (e) {
    console.error(e.message);
    // 输出: Converting circular structure to JSON
}
```

### 解决方案

```js
function stringifyCircular(obj) {
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

const obj = {};
obj.self = obj;

console.log(stringifyCircular(obj));
// 输出: {"self":"[Circular]"}
```

## 性能考虑

### 大对象处理

```js
// 对于大对象，考虑只序列化需要的属性
const largeObj = {
    // ... 大量数据
};

// 只序列化需要的部分
const json = JSON.stringify(largeObj, ['id', 'name', 'status']);
```

### 避免重复序列化

```js
// 缓存序列化结果
let cachedJson = null;
let cachedObj = null;

function getJsonString(obj) {
    if (obj === cachedObj && cachedJson) {
        return cachedJson;
    }
    cachedObj = obj;
    cachedJson = JSON.stringify(obj);
    return cachedJson;
}
```

## 注意事项

1. **不可序列化的值**：`undefined`、函数、Symbol 会被忽略
2. **Date 对象**：自动转换为 ISO 8601 字符串
3. **循环引用**：会导致错误，需要特殊处理
4. **性能**：大对象序列化可能较慢
5. **精度**：数字精度可能丢失（JavaScript 数字精度限制）

## 常见问题

### 问题 1：如何保留 undefined？

`JSON.stringify()` 无法直接保留 `undefined`。可以使用 `replacer` 函数：

```js
const obj = { name: "John", age: undefined };

const json = JSON.stringify(obj, function(key, value) {
    return value === undefined ? null : value;
});

console.log(json);
// 输出: {"name":"John","age":null}
```

### 问题 2：如何自定义 Date 格式？

实现 `toJSON()` 方法或使用 `replacer`：

```js
const obj = {
    date: new Date()
};

// 方法 1：使用 toJSON
Date.prototype.toJSON = function() {
    return this.toLocaleDateString('zh-CN');
};

// 方法 2：使用 replacer
const json = JSON.stringify(obj, function(key, value) {
    if (value instanceof Date) {
        return value.toLocaleDateString('zh-CN');
    }
    return value;
});
```

### 问题 3：如何序列化包含函数的对象？

函数无法直接序列化，需要转换为字符串或其他格式：

```js
const obj = {
    name: "John",
    greet: function() { return "Hello"; }
};

const json = JSON.stringify(obj, function(key, value) {
    if (typeof value === 'function') {
        return value.toString();
    }
    return value;
});
```

## 最佳实践

1. **使用格式化**：开发时使用 `space` 参数提高可读性
2. **过滤敏感数据**：使用 `replacer` 过滤密码等敏感信息
3. **处理循环引用**：实现自定义序列化逻辑
4. **性能优化**：只序列化需要的属性
5. **错误处理**：使用 try-catch 处理序列化错误

## 练习任务

1. 创建一个包含用户信息的对象，使用 `JSON.stringify()` 序列化，并格式化输出。

2. 实现一个函数，序列化对象时自动过滤掉值为 `undefined` 的属性。

3. 创建一个包含 Date 对象的对象，序列化时将 Date 转换为自定义格式（如 "2025-12-19"）。

4. 实现一个函数，安全地序列化可能包含循环引用的对象。

5. 创建一个包含函数和 Symbol 的对象，使用 `replacer` 函数将它们转换为可序列化的格式。
