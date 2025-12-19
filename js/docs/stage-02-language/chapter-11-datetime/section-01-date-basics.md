# 2.11.1 Date 对象基础

## 概述

Date 对象是 JavaScript 中用于表示日期和时间的对象。它基于 UTC（协调世界时）1970 年 1 月 1 日 00:00:00 开始的毫秒数。

## 特性

- **时间戳基础**：基于 Unix 时间戳（毫秒级）
- **时区支持**：支持本地时区和 UTC 时区
- **多种创建方式**：支持多种构造函数形式
- **丰富的方法**：提供获取、设置日期时间的方法
- **自动处理**：自动处理月份溢出、闰年等

## 创建 Date 对象

### 当前时间

```js
// 创建表示当前日期和时间的 Date 对象
const now = new Date();
console.log(now);
// 输出: 2025-12-19T10:30:00.000Z（示例，实际为当前时间）
```

### 时间戳创建

```js
// 使用时间戳（毫秒）创建
const date1 = new Date(1702987800000);
console.log(date1);
// 输出: 2025-12-19T10:30:00.000Z

// 使用时间戳（秒，需要乘以 1000）
const timestamp = 1702987800;
const date2 = new Date(timestamp * 1000);
console.log(date2);
```

### 字符串创建

```js
// ISO 8601 格式
const date1 = new Date('2025-12-19T10:30:00.000Z');
console.log(date1);

// 其他格式（可能因浏览器而异）
const date2 = new Date('December 19, 2025 10:30:00');
const date3 = new Date('2025/12/19 10:30:00');
```

### 年月日创建

```js
// new Date(year, monthIndex, day, hours, minutes, seconds, milliseconds)
// 注意：monthIndex 从 0 开始（0 = 一月，11 = 十二月）

const date1 = new Date(2025, 11, 19);  // 2025年12月19日
const date2 = new Date(2025, 11, 19, 10, 30, 0);  // 2025年12月19日 10:30:00
const date3 = new Date(2025, 11, 19, 10, 30, 0, 500);  // 包含毫秒
```

**注意**：月份从 0 开始，所以 11 表示 12 月。

## 获取日期时间信息

### 获取年份

```js
const date = new Date(2025, 11, 19);
console.log(date.getFullYear());  // 2025（四位数年份）
console.log(date.getYear());      // 125（已废弃，返回年份 - 1900）
```

### 获取月份

```js
const date = new Date(2025, 11, 19);
console.log(date.getMonth());     // 11（0-11，11 表示 12 月）
console.log(date.getMonth() + 1); // 12（实际月份）
```

### 获取日期

```js
const date = new Date(2025, 11, 19);
console.log(date.getDate());      // 19（月份中的日期，1-31）
console.log(date.getDay());       // 5（星期几，0-6，0 表示星期日）
```

### 获取时间

```js
const date = new Date(2025, 11, 19, 10, 30, 45, 500);
console.log(date.getHours());     // 10（0-23）
console.log(date.getMinutes());   // 30（0-59）
console.log(date.getSeconds());   // 45（0-59）
console.log(date.getMilliseconds()); // 500（0-999）
```

### UTC 方法

```js
const date = new Date(2025, 11, 19, 10, 30, 0);

// 本地时间
console.log(date.getHours());        // 10（本地时区）
console.log(date.getMinutes());      // 30（本地时区）

// UTC 时间
console.log(date.getUTCHours());     // 2（UTC 时区，假设本地是 UTC+8）
console.log(date.getUTCMinutes());   // 30（UTC 时区）
```

## 设置日期时间

### 设置年份

```js
const date = new Date();
date.setFullYear(2026);
console.log(date.getFullYear());  // 2026
```

### 设置月份

```js
const date = new Date();
date.setMonth(0);  // 设置为 1 月（0-11）
console.log(date.getMonth());     // 0
```

### 设置日期

```js
const date = new Date();
date.setDate(25);
console.log(date.getDate());  // 25
```

### 设置时间

```js
const date = new Date();
date.setHours(15);
date.setMinutes(45);
date.setSeconds(30);
date.setMilliseconds(500);

console.log(date.getHours());     // 15
console.log(date.getMinutes());  // 45
console.log(date.getSeconds());  // 30
console.log(date.getMilliseconds()); // 500
```

### 链式设置

```js
const date = new Date();
date.setFullYear(2026)
    .setMonth(0)
    .setDate(1)
    .setHours(0)
    .setMinutes(0)
    .setSeconds(0)
    .setMilliseconds(0);

console.log(date);
// 输出: 2026-01-01T00:00:00.000Z
```

## 时间戳

### 获取时间戳

```js
const date = new Date();

// 方法 1：getTime()
console.log(date.getTime());  // 1702987800000（毫秒）

// 方法 2：valueOf()
console.log(date.valueOf());  // 1702987800000（毫秒）

// 方法 3：Number 转换
console.log(Number(date));    // 1702987800000（毫秒）

// 方法 4：一元加号
console.log(+date);           // 1702987800000（毫秒）

// 方法 5：Date.now()（当前时间戳）
console.log(Date.now());      // 1702987800000（毫秒）
```

### 设置时间戳

```js
const date = new Date();
date.setTime(1702987800000);
console.log(date);
```

## 日期比较

### 比较操作符

```js
const date1 = new Date(2025, 11, 19);
const date2 = new Date(2025, 11, 20);

console.log(date1 < date2);   // true
console.log(date1 > date2);   // false
console.log(date1 === date2); // false（比较的是对象引用）

// 比较时间戳
console.log(date1.getTime() === date2.getTime()); // false
```

### 比较方法

```js
const date1 = new Date(2025, 11, 19);
const date2 = new Date(2025, 11, 19);

// 使用时间戳比较
function isEqual(date1, date2) {
    return date1.getTime() === date2.getTime();
}

console.log(isEqual(date1, date2)); // true
```

## 日期运算

### 日期加减

```js
const date = new Date(2025, 11, 19);

// 加一天
date.setDate(date.getDate() + 1);
console.log(date.getDate());  // 20

// 加一个月
date.setMonth(date.getMonth() + 1);
console.log(date.getMonth()); // 0（1 月，因为 12 月 + 1 = 13，自动转为 1 月）

// 加一年
date.setFullYear(date.getFullYear() + 1);
console.log(date.getFullYear()); // 2026
```

### 日期差值

```js
const date1 = new Date(2025, 11, 19);
const date2 = new Date(2025, 11, 25);

// 计算差值（毫秒）
const diff = date2.getTime() - date1.getTime();
console.log(diff);  // 518400000（6 天的毫秒数）

// 转换为天数
const days = diff / (1000 * 60 * 60 * 24);
console.log(days);  // 6
```

## 常用方法

### Date.now()

```js
// 获取当前时间戳（毫秒）
const timestamp = Date.now();
console.log(timestamp);  // 1702987800000
```

### Date.parse()

```js
// 解析日期字符串，返回时间戳
const timestamp = Date.parse('2025-12-19T10:30:00.000Z');
console.log(timestamp);  // 1702987800000

// 无效日期返回 NaN
const invalid = Date.parse('invalid date');
console.log(invalid);    // NaN
```

### Date.UTC()

```js
// 返回 UTC 时间戳
// Date.UTC(year, monthIndex, day, hours, minutes, seconds, milliseconds)
const timestamp = Date.UTC(2025, 11, 19, 10, 30, 0);
console.log(timestamp);  // 1702987800000

// 创建 UTC 日期
const date = new Date(Date.UTC(2025, 11, 19, 10, 30, 0));
console.log(date);
```

## 注意事项

1. **月份索引**：月份从 0 开始（0 = 一月，11 = 十二月）
2. **时区问题**：Date 对象内部存储 UTC 时间，显示时转换为本地时区
3. **年份问题**：使用 `getFullYear()` 而不是已废弃的 `getYear()`
4. **自动处理**：Date 对象会自动处理月份溢出、闰年等情况
5. **性能考虑**：频繁创建 Date 对象可能影响性能

## 常见问题

### 问题 1：为什么月份从 0 开始？

这是 JavaScript 的历史遗留问题，为了与 C 语言的 `struct tm` 保持一致。

### 问题 2：如何获取实际月份？

```js
const date = new Date();
const month = date.getMonth() + 1;  // 加 1 得到实际月份
console.log(month);  // 12（12 月）
```

### 问题 3：如何比较两个日期是否相等？

```js
function isEqual(date1, date2) {
    return date1.getTime() === date2.getTime();
}

const date1 = new Date(2025, 11, 19);
const date2 = new Date(2025, 11, 19);
console.log(isEqual(date1, date2)); // true
```

### 问题 4：如何获取当前时间戳？

```js
// 方法 1：Date.now()
const timestamp1 = Date.now();

// 方法 2：new Date().getTime()
const timestamp2 = new Date().getTime();

// 方法 3：+new Date()
const timestamp3 = +new Date();
```

## 最佳实践

1. **使用 getFullYear()**：不要使用已废弃的 `getYear()`
2. **注意月份索引**：记住月份从 0 开始
3. **使用时间戳比较**：比较日期时使用时间戳而不是对象引用
4. **统一时区**：在应用中统一使用 UTC 或本地时区
5. **性能优化**：避免频繁创建 Date 对象

## 练习任务

1. 创建一个 Date 对象表示 2025 年 12 月 25 日，并获取其年份、月份和日期。

2. 编写一个函数，计算两个日期之间的天数差。

3. 创建一个函数，判断给定的年份是否为闰年。

4. 编写一个函数，获取当前日期是星期几（中文名称）。

5. 实现一个函数，将日期对象转换为 "YYYY-MM-DD" 格式的字符串。
