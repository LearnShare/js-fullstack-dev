# 2.4.4 现代运算符（??、?.、??=）

## 概述

现代 JavaScript 引入了新的运算符，包括空值合并运算符（??）、可选链运算符（?.）和逻辑赋值运算符（??=、&&=、||=）。这些运算符简化了代码，提高了可读性。

## 空值合并运算符（??）

### 基本用法

```js
// ?? 只在左侧为 null 或 undefined 时返回右侧值
null ?? "default";        // "default"
undefined ?? "default";    // "default"
0 ?? "default";           // 0（不是 null/undefined）
"" ?? "default";          // ""（不是 null/undefined）
false ?? "default";       // false（不是 null/undefined）
```

### 与 || 的区别

```js
// || 会在左侧为假值时返回右侧值
0 || "default";           // "default"
"" || "default";          // "default"
false || "default";       // "default"
null || "default";        // "default"

// ?? 只在 null 或 undefined 时返回右侧值
0 ?? "default";           // 0
"" ?? "default";          // ""
false ?? "default";       // false
null ?? "default";        // "default"
```

### 实际应用

```js
// 设置默认值
const name = userName ?? "Guest";
const port = process.env.PORT ?? 3000;

// 处理 API 响应
const data = response.data ?? [];

// 配置对象
const config = {
    timeout: userConfig.timeout ?? 5000,
    retries: userConfig.retries ?? 3
};
```

## 可选链运算符（?.）

### 基本用法

```js
// ?. 安全地访问嵌套属性
const user = {
    name: "John",
    address: {
        city: "New York"
    }
};

// 安全访问
user?.name;                    // "John"
user?.address?.city;           // "New York"
user?.address?.zipCode;        // undefined（不会报错）

// 如果 user 为 null 或 undefined
const user2 = null;
user2?.name;                   // undefined（不会报错）
```

### 方法调用

```js
// 安全地调用方法
const obj = {
    method: function() {
        return "result";
    }
};

obj?.method?.();               // "result"

// 如果方法不存在
const obj2 = null;
obj2?.method?.();              // undefined（不会报错）
```

### 数组访问

```js
// 安全地访问数组元素
const arr = [1, 2, 3];
arr?.[0];                      // 1
arr?.[10];                     // undefined

// 如果数组为 null 或 undefined
const arr2 = null;
arr2?.[0];                     // undefined（不会报错）
```

### 组合使用

```js
// 组合使用 ?. 和 ??
const city = user?.address?.city ?? "Unknown";
const name = user?.name ?? "Guest";
```

## 逻辑赋值运算符

### 空值合并赋值（??=）

```js
// ??= 只在变量为 null 或 undefined 时赋值
let x = null;
x ??= "default";                // x 现在是 "default"

let y = 0;
y ??= "default";               // y 仍然是 0

// 等价于
let z = null;
z = z ?? "default";            // 与 z ??= "default" 等价
```

### 逻辑与赋值（&&=）

```js
// &&= 只在左侧为真值时赋值
let x = 10;
x &&= 20;                      // x 现在是 20

let y = 0;
y &&= 20;                      // y 仍然是 0

// 等价于
let z = 10;
z = z && 20;                   // 与 z &&= 20 等价
```

### 逻辑或赋值（||=）

```js
// ||= 只在左侧为假值时赋值
let x = null;
x ||= "default";               // x 现在是 "default"

let y = "value";
y ||= "default";              // y 仍然是 "value"

// 等价于
let z = null;
z = z || "default";            // 与 z ||= "default" 等价
```

## 实际应用

### 1. 安全访问嵌套属性

```js
// 使用 ?. 安全访问
const city = user?.address?.city ?? "Unknown";
const email = user?.contact?.email ?? "no-email";

// 避免
const city = user && user.address && user.address.city || "Unknown";
```

### 2. 设置默认值

```js
// 使用 ??= 设置默认值
let config = {};
config.timeout ??= 5000;
config.retries ??= 3;

// 使用 ?? 设置默认值
const timeout = config.timeout ?? 5000;
```

### 3. 条件赋值

```js
// 使用 &&= 进行条件赋值
let value = 10;
value &&= 20;                  // value 现在是 20

// 使用 ||= 设置默认值
let name = null;
name ||= "Guest";              // name 现在是 "Guest"
```

### 4. API 响应处理

```js
// 安全地处理 API 响应
const data = response?.data ?? [];
const user = response?.user ?? null;
const error = response?.error?.message ?? "Unknown error";
```

## 最佳实践

### 1. 使用 ?? 替代 || 设置默认值

```js
// 好的做法：使用 ??
const count = userCount ?? 0;
const name = userName ?? "Guest";

// 避免：使用 ||（可能有意外的行为）
const count2 = userCount || 0; // 如果 userCount 是 0，会变成默认值
```

### 2. 使用 ?. 安全访问

```js
// 好的做法：使用 ?.
const city = user?.address?.city;

// 避免：使用 && 链
const city2 = user && user.address && user.address.city;
```

### 3. 组合使用

```js
// 组合使用 ?. 和 ??
const city = user?.address?.city ?? "Unknown";
const email = user?.contact?.email ?? "no-email";
```

## 浏览器兼容性

### 支持情况

- **??**：ES2020，现代浏览器支持
- **?.**：ES2020，现代浏览器支持
- **??=、&&=、||=**：ES2021，现代浏览器支持

### 使用 Babel 转译

对于旧浏览器，需要使用 Babel 转译这些运算符。

## 练习

1. **空值合并运算符**：使用 `??` 运算符为变量设置默认值，处理可能为 `null` 或 `undefined` 的情况。

2. **可选链运算符**：使用 `?.` 运算符安全地访问嵌套对象属性，避免报错。

3. **组合使用**：组合使用 `?.` 和 `??` 运算符，安全地访问嵌套属性并设置默认值。

4. **逻辑赋值运算符**：使用 `??=`、`&&=`、`||=` 运算符进行条件赋值。

5. **API 响应处理**：使用现代运算符处理 API 响应数据，安全地访问嵌套属性并设置默认值。

完成以上练习后，继续学习下一节，了解运算符优先级。

## 总结

现代运算符简化了代码，提高了可读性。主要要点：

- **??**：空值合并，只在 null/undefined 时返回右侧值
- **?.**：可选链，安全访问嵌套属性
- **??=、&&=、||=**：逻辑赋值运算符
- 使用 ?? 替代 || 设置默认值
- 使用 ?. 安全访问嵌套属性
- 注意浏览器兼容性

继续学习下一节，了解运算符优先级。
