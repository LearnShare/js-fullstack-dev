# 2.11.3 时区处理

## 概述

时区处理是日期时间编程中的重要概念。JavaScript 的 Date 对象内部存储 UTC 时间，但在显示时会根据本地时区进行转换。本节介绍时区的概念和处理方法。

## 时区概念

### UTC 与本地时间

```js
const date = new Date();

// UTC 时间
console.log(date.toUTCString());
// 输出: "Fri, 19 Dec 2025 02:30:00 GMT"

// 本地时间
console.log(date.toString());
// 输出: "Fri Dec 19 2025 10:30:00 GMT+0800 (中国标准时间)"

// ISO 字符串（UTC）
console.log(date.toISOString());
// 输出: "2025-12-19T02:30:00.000Z"
```

### 时区偏移

```js
const date = new Date();

// 获取时区偏移（分钟）
const offset = date.getTimezoneOffset();
console.log(offset);  // -480（UTC+8，偏移 -480 分钟 = -8 小时）

// 转换为小时
const offsetHours = -offset / 60;
console.log(offsetHours);  // 8（UTC+8）
```

## UTC 方法

### 获取 UTC 时间

```js
const date = new Date(2025, 11, 19, 10, 30, 0);

console.log(date.getUTCFullYear());  // 2025
console.log(date.getUTCMonth());     // 11
console.log(date.getUTCDate());      // 19
console.log(date.getUTCHours());     // 2（UTC 时间，本地是 UTC+8）
console.log(date.getUTCMinutes());   // 30
console.log(date.getUTCSeconds());   // 0
```

### 设置 UTC 时间

```js
const date = new Date();

date.setUTCFullYear(2026);
date.setUTCMonth(0);
date.setUTCDate(1);
date.setUTCHours(0);
date.setUTCMinutes(0);
date.setUTCSeconds(0);
date.setUTCMilliseconds(0);

console.log(date.toISOString());
// 输出: "2026-01-01T00:00:00.000Z"
```

## 时区转换

### UTC 转本地时间

```js
// 创建 UTC 时间
const utcDate = new Date('2025-12-19T10:30:00.000Z');

// 转换为本地时间字符串
console.log(utcDate.toLocaleString('zh-CN'));
// 输出: "2025/12/19 18:30:00"（假设本地是 UTC+8）
```

### 本地时间转 UTC

```js
// 创建本地时间
const localDate = new Date(2025, 11, 19, 10, 30, 0);

// 转换为 UTC 时间字符串
console.log(localDate.toISOString());
// 输出: "2025-12-19T02:30:00.000Z"（假设本地是 UTC+8）
```

### 指定时区转换

```js
// 使用 toLocaleString 指定时区
const date = new Date('2025-12-19T10:30:00.000Z');

// 转换为不同时区
console.log(date.toLocaleString('en-US', { timeZone: 'America/New_York' }));
// 输出: "12/19/2025, 5:30:00 AM"（UTC-5）

console.log(date.toLocaleString('en-US', { timeZone: 'Asia/Tokyo' }));
// 输出: "12/19/2025, 7:30:00 PM"（UTC+9）

console.log(date.toLocaleString('en-US', { timeZone: 'Europe/London' }));
// 输出: "12/19/2025, 10:30:00 AM"（UTC+0）
```

## 时区工具函数

### 获取时区名称

```js
function getTimezoneName() {
    const date = new Date();
    const timeString = date.toString();
    const match = timeString.match(/\(([^)]+)\)/);
    return match ? match[1] : 'Unknown';
}

console.log(getTimezoneName());
// 输出: "中国标准时间"
```

### 时区转换函数

```js
function convertTimezone(date, targetTimezone) {
    return new Date(date.toLocaleString('en-US', { timeZone: targetTimezone }));
}

const date = new Date('2025-12-19T10:30:00.000Z');
const nyTime = convertTimezone(date, 'America/New_York');
console.log(nyTime);
```

### UTC 时间戳转换

```js
// UTC 时间戳转本地时间
function utcTimestampToLocal(timestamp) {
    return new Date(timestamp);
}

// 本地时间转 UTC 时间戳
function localToUtcTimestamp(date) {
    return Date.UTC(
        date.getFullYear(),
        date.getMonth(),
        date.getDate(),
        date.getHours(),
        date.getMinutes(),
        date.getSeconds(),
        date.getMilliseconds()
    );
}

const localDate = new Date(2025, 11, 19, 10, 30, 0);
const utcTimestamp = localToUtcTimestamp(localDate);
console.log(utcTimestamp);
```

## 常见时区

### 时区列表

| 时区标识符          | 说明           | UTC 偏移 |
|:--------------------|:---------------|:---------|
| `UTC`               | 协调世界时     | UTC+0    |
| `Asia/Shanghai`     | 中国标准时间   | UTC+8    |
| `Asia/Tokyo`        | 日本标准时间   | UTC+9    |
| `America/New_York`  | 美国东部时间   | UTC-5    |
| `America/Los_Angeles` | 美国太平洋时间 | UTC-8    |
| `Europe/London`     | 英国时间       | UTC+0    |
| `Europe/Paris`      | 中欧时间       | UTC+1    |

### 使用时区

```js
const date = new Date('2025-12-19T10:30:00.000Z');

// 转换为不同时区
const timezones = [
    'UTC',
    'Asia/Shanghai',
    'Asia/Tokyo',
    'America/New_York',
    'Europe/London'
];

timezones.forEach(tz => {
    const localTime = date.toLocaleString('en-US', { timeZone: tz });
    console.log(`${tz}: ${localTime}`);
});
```

## 夏令时处理

### 检测夏令时

```js
function isDST(date) {
    const jan = new Date(date.getFullYear(), 0, 1);
    const jul = new Date(date.getFullYear(), 6, 1);
    const stdOffset = Math.max(jan.getTimezoneOffset(), jul.getTimezoneOffset());
    return date.getTimezoneOffset() < stdOffset;
}

const date = new Date(2025, 6, 1);  // 7 月（可能处于夏令时）
console.log(isDST(date));
```

## 注意事项

1. **UTC 存储**：Date 对象内部存储 UTC 时间
2. **本地显示**：默认方法返回本地时间
3. **时区标识**：使用 IANA 时区数据库标识符
4. **夏令时**：某些地区有夏令时，需要注意
5. **精度问题**：时区转换可能涉及精度问题

## 常见问题

### 问题 1：如何获取当前时区？

```js
function getCurrentTimezone() {
    const offset = -new Date().getTimezoneOffset() / 60;
    const sign = offset >= 0 ? '+' : '-';
    return `UTC${sign}${Math.abs(offset)}`;
}

console.log(getCurrentTimezone());
// 输出: "UTC+8"
```

### 问题 2：如何在不同时区显示同一时间？

```js
function displayInTimezones(date, timezones) {
    return timezones.map(tz => ({
        timezone: tz,
        time: date.toLocaleString('en-US', { timeZone: tz })
    }));
}

const date = new Date('2025-12-19T10:30:00.000Z');
const times = displayInTimezones(date, ['UTC', 'Asia/Shanghai', 'America/New_York']);
console.log(times);
```

### 问题 3：如何统一使用 UTC 时间？

```js
// 创建 UTC 时间
const utcDate = new Date(Date.UTC(2025, 11, 19, 10, 30, 0));

// 始终使用 UTC 方法
console.log(utcDate.getUTCHours());  // 10
console.log(utcDate.toISOString()); // "2025-12-19T10:30:00.000Z"
```

## 最佳实践

1. **统一时区**：在应用中统一使用 UTC 或指定时区
2. **存储 UTC**：在数据库中存储 UTC 时间
3. **显示转换**：在显示时转换为用户时区
4. **明确标识**：在 API 中明确标识时区信息
5. **使用库**：复杂时区处理考虑使用 date-fns、moment.js 等库

## 练习任务

1. 创建一个函数，获取当前时区的 UTC 偏移量（以小时为单位）。

2. 实现一个函数，将 UTC 时间转换为指定时区的本地时间。

3. 编写一个函数，检测给定日期是否处于夏令时。

4. 创建一个函数，在不同时区显示同一时间点。

5. 实现一个时区转换工具，支持在多个时区之间转换时间。
