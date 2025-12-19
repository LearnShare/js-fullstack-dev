# 2.11.2 日期格式化与解析

## 概述

日期格式化是将 Date 对象转换为可读字符串的过程，日期解析是将字符串转换为 Date 对象的过程。本节介绍常用的格式化方法和解析技巧。

## 格式化方法

### toString()

```js
const date = new Date(2025, 11, 19, 10, 30, 0);
console.log(date.toString());
// 输出: "Fri Dec 19 2025 10:30:00 GMT+0800 (中国标准时间)"
```

### toISOString()

```js
const date = new Date(2025, 11, 19, 10, 30, 0);
console.log(date.toISOString());
// 输出: "2025-12-19T02:30:00.000Z"（UTC 时间）
```

### toLocaleString()

```js
const date = new Date(2025, 11, 19, 10, 30, 0);

// 默认格式
console.log(date.toLocaleString());
// 输出: "2025/12/19 10:30:00"（根据系统区域设置）

// 指定区域
console.log(date.toLocaleString('zh-CN'));
// 输出: "2025/12/19 10:30:00"

console.log(date.toLocaleString('en-US'));
// 输出: "12/19/2025, 10:30:00 AM"

// 指定选项
console.log(date.toLocaleString('zh-CN', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit'
}));
// 输出: "2025/12/19 10:30"
```

### toLocaleDateString()

```js
const date = new Date(2025, 11, 19);

console.log(date.toLocaleDateString('zh-CN'));
// 输出: "2025/12/19"

console.log(date.toLocaleDateString('en-US'));
// 输出: "12/19/2025"
```

### toLocaleTimeString()

```js
const date = new Date(2025, 11, 19, 10, 30, 0);

console.log(date.toLocaleTimeString('zh-CN'));
// 输出: "10:30:00"

console.log(date.toLocaleTimeString('en-US'));
// 输出: "10:30:00 AM"
```

## 自定义格式化

### 手动格式化

```js
function formatDate(date, format = 'YYYY-MM-DD') {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    const hours = String(date.getHours()).padStart(2, '0');
    const minutes = String(date.getMinutes()).padStart(2, '0');
    const seconds = String(date.getSeconds()).padStart(2, '0');

    return format
        .replace('YYYY', year)
        .replace('MM', month)
        .replace('DD', day)
        .replace('HH', hours)
        .replace('mm', minutes)
        .replace('ss', seconds);
}

const date = new Date(2025, 11, 19, 10, 30, 45);
console.log(formatDate(date, 'YYYY-MM-DD'));        // "2025-12-19"
console.log(formatDate(date, 'YYYY-MM-DD HH:mm:ss')); // "2025-12-19 10:30:45"
```

### 更完整的格式化函数

```js
function formatDate(date, format) {
    const map = {
        'YYYY': date.getFullYear(),
        'MM': String(date.getMonth() + 1).padStart(2, '0'),
        'DD': String(date.getDate()).padStart(2, '0'),
        'HH': String(date.getHours()).padStart(2, '0'),
        'mm': String(date.getMinutes()).padStart(2, '0'),
        'ss': String(date.getSeconds()).padStart(2, '0'),
        'M': date.getMonth() + 1,
        'D': date.getDate(),
        'H': date.getHours(),
        'm': date.getMinutes(),
        's': date.getSeconds()
    };

    return format.replace(/YYYY|MM|DD|HH|mm|ss|M|D|H|m|s/g, (match) => {
        return map[match] || match;
    });
}

const date = new Date(2025, 11, 19, 10, 30, 45);
console.log(formatDate(date, 'YYYY年MM月DD日 HH:mm:ss'));
// 输出: "2025年12月19日 10:30:45"
```

## 日期解析

### Date.parse()

```js
// ISO 8601 格式
const timestamp1 = Date.parse('2025-12-19T10:30:00.000Z');
console.log(timestamp1);  // 1702987800000

// 其他格式（可能因浏览器而异）
const timestamp2 = Date.parse('December 19, 2025');
const timestamp3 = Date.parse('2025/12/19');

// 无效日期返回 NaN
const invalid = Date.parse('invalid date');
console.log(invalid);  // NaN
```

### new Date() 构造函数

```js
// 字符串解析
const date1 = new Date('2025-12-19T10:30:00.000Z');
const date2 = new Date('2025-12-19');
const date3 = new Date('December 19, 2025');

// 注意：不同浏览器可能支持不同的格式
```

### 自定义解析函数

```js
function parseDate(dateString, format = 'YYYY-MM-DD') {
    // 简单的解析实现
    if (format === 'YYYY-MM-DD') {
        const parts = dateString.split('-');
        if (parts.length === 3) {
            const year = parseInt(parts[0], 10);
            const month = parseInt(parts[1], 10) - 1;  // 月份从 0 开始
            const day = parseInt(parts[2], 10);
            return new Date(year, month, day);
        }
    }
    // 默认使用 Date 构造函数
    return new Date(dateString);
}

const date = parseDate('2025-12-19', 'YYYY-MM-DD');
console.log(date);
```

## 常用格式

### ISO 8601 格式

```js
const date = new Date();
console.log(date.toISOString());
// 输出: "2025-12-19T10:30:00.000Z"
```

### 中文格式

```js
const date = new Date(2025, 11, 19);

function formatChinese(date) {
    const year = date.getFullYear();
    const month = date.getMonth() + 1;
    const day = date.getDate();
    return `${year}年${month}月${day}日`;
}

console.log(formatChinese(date));
// 输出: "2025年12月19日"
```

### 相对时间

```js
function formatRelative(date) {
    const now = new Date();
    const diff = now.getTime() - date.getTime();
    const seconds = Math.floor(diff / 1000);
    const minutes = Math.floor(seconds / 60);
    const hours = Math.floor(minutes / 60);
    const days = Math.floor(hours / 24);

    if (days > 0) {
        return `${days}天前`;
    } else if (hours > 0) {
        return `${hours}小时前`;
    } else if (minutes > 0) {
        return `${minutes}分钟前`;
    } else {
        return '刚刚';
    }
}

const date = new Date(Date.now() - 2 * 60 * 60 * 1000);  // 2 小时前
console.log(formatRelative(date));
// 输出: "2小时前"
```

## 格式化选项

### toLocaleString 选项

```js
const date = new Date(2025, 11, 19, 10, 30, 0);

const options = {
    year: 'numeric',      // 'numeric' | '2-digit'
    month: 'long',        // 'numeric' | '2-digit' | 'long' | 'short' | 'narrow'
    day: 'numeric',       // 'numeric' | '2-digit'
    weekday: 'long',      // 'long' | 'short' | 'narrow'
    hour: '2-digit',      // 'numeric' | '2-digit'
    minute: '2-digit',    // 'numeric' | '2-digit'
    second: '2-digit',    // 'numeric' | '2-digit'
    hour12: false         // true | false
};

console.log(date.toLocaleString('zh-CN', options));
// 输出: "2025年12月19日 星期五 10:30:00"
```

### 常用选项组合

```js
const date = new Date(2025, 11, 19, 10, 30, 0);

// 日期格式
console.log(date.toLocaleDateString('zh-CN', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
}));
// 输出: "2025年12月19日"

// 时间格式
console.log(date.toLocaleTimeString('zh-CN', {
    hour: '2-digit',
    minute: '2-digit',
    hour12: false
}));
// 输出: "10:30"
```

## 注意事项

1. **时区问题**：`toISOString()` 返回 UTC 时间，其他方法返回本地时间
2. **格式兼容性**：不同浏览器对日期字符串格式的支持可能不同
3. **性能考虑**：频繁格式化可能影响性能，考虑缓存结果
4. **区域设置**：`toLocaleString()` 的结果取决于系统区域设置
5. **解析错误**：无效的日期字符串会返回 `Invalid Date`

## 常见问题

### 问题 1：如何格式化日期为 "YYYY-MM-DD"？

```js
function formatYYYYMMDD(date) {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
}

const date = new Date();
console.log(formatYYYYMMDD(date));
// 输出: "2025-12-19"
```

### 问题 2：如何解析 "YYYY-MM-DD" 格式的字符串？

```js
function parseYYYYMMDD(dateString) {
    const parts = dateString.split('-');
    const year = parseInt(parts[0], 10);
    const month = parseInt(parts[1], 10) - 1;
    const day = parseInt(parts[2], 10);
    return new Date(year, month, day);
}

const date = parseYYYYMMDD('2025-12-19');
console.log(date);
```

### 问题 3：如何判断日期字符串是否有效？

```js
function isValidDate(dateString) {
    const date = new Date(dateString);
    return date instanceof Date && !isNaN(date.getTime());
}

console.log(isValidDate('2025-12-19'));  // true
console.log(isValidDate('invalid'));     // false
```

## 最佳实践

1. **使用 ISO 格式**：在数据传输中使用 ISO 8601 格式
2. **统一格式化函数**：创建统一的格式化函数库
3. **处理时区**：明确使用 UTC 还是本地时间
4. **验证输入**：解析前验证日期字符串格式
5. **性能优化**：对频繁使用的格式化结果进行缓存

## 练习任务

1. 创建一个函数，将 Date 对象格式化为 "YYYY年MM月DD日 HH:mm:ss" 格式。

2. 实现一个函数，解析 "YYYY-MM-DD HH:mm:ss" 格式的字符串为 Date 对象。

3. 编写一个函数，计算并格式化相对时间（如 "2小时前"、"3天前"）。

4. 创建一个函数，将日期格式化为中文格式，包括星期几（如 "2025年12月19日 星期五"）。

5. 实现一个通用的日期格式化函数，支持多种格式模板（如 'YYYY-MM-DD'、'MM/DD/YYYY' 等）。
