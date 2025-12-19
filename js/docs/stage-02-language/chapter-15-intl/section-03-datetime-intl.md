# 2.15.3 日期时间国际化

## 概述

`Intl.DateTimeFormat` 用于根据区域设置格式化日期和时间。它能够自动适应不同地区的日期时间格式，提供统一的国际化支持。

## 语法

```js
new Intl.DateTimeFormat([locales[, options]])
```

## 参数详述

| 参数名    | 类型           | 说明                    | 是否必需 | 默认值 |
|:----------|:---------------|:------------------------|:---------|:-------|
| `locales` | string \| Array | 区域设置或区域设置数组   | 否       | 系统默认 |
| `options` | Object         | 格式化选项对象           | 否       | {}     |

## 返回值

返回一个 `DateTimeFormat` 对象，提供 `format()` 方法用于格式化日期。

## 基本用法

### 默认格式化

```js
const date = new Date(2025, 11, 19, 10, 30, 0);

// 使用系统默认区域设置
const formatter1 = new Intl.DateTimeFormat();
console.log(formatter1.format(date));
// 输出: "2025/12/19 10:30:00"（根据系统设置）

// 指定区域设置
const formatter2 = new Intl.DateTimeFormat('zh-CN');
console.log(formatter2.format(date));
// 输出: "2025/12/19 10:30:00"

const formatter3 = new Intl.DateTimeFormat('en-US');
console.log(formatter3.format(date));
// 输出: "12/19/2025, 10:30:00 AM"
```

### 格式化方法

```js
const date = new Date(2025, 11, 19, 10, 30, 0);
const formatter = new Intl.DateTimeFormat('zh-CN');

// format() 方法
console.log(formatter.format(date));
// 输出: "2025/12/19 10:30:00"

// formatToParts() 方法（返回格式化部分数组）
const parts = formatter.formatToParts(date);
console.log(parts);
// 输出: [
//   { type: 'year', value: '2025' },
//   { type: 'literal', value: '/' },
//   { type: 'month', value: '12' },
//   ...
// ]

// formatRange() 方法（格式化日期范围）
const date1 = new Date(2025, 11, 19);
const date2 = new Date(2025, 11, 25);
console.log(formatter.formatRange(date1, date2));
// 输出: "2025/12/19 - 2025/12/25"
```

## 格式化选项

### 日期选项

```js
const date = new Date(2025, 11, 19);

const options = {
    year: 'numeric',    // 'numeric' | '2-digit'
    month: 'long',      // 'numeric' | '2-digit' | 'long' | 'short' | 'narrow'
    day: 'numeric'      // 'numeric' | '2-digit'
};

const formatter = new Intl.DateTimeFormat('zh-CN', options);
console.log(formatter.format(date));
// 输出: "2025年12月19日"
```

### 时间选项

```js
const date = new Date(2025, 11, 19, 10, 30, 45);

const options = {
    hour: '2-digit',      // 'numeric' | '2-digit'
    minute: '2-digit',    // 'numeric' | '2-digit'
    second: '2-digit',    // 'numeric' | '2-digit'
    hour12: false         // true | false（12 小时制或 24 小时制）
};

const formatter = new Intl.DateTimeFormat('zh-CN', options);
console.log(formatter.format(date));
// 输出: "10:30:45"
```

### 星期选项

```js
const date = new Date(2025, 11, 19);

const options = {
    weekday: 'long',      // 'long' | 'short' | 'narrow'
    year: 'numeric',
    month: 'long',
    day: 'numeric'
};

const formatter = new Intl.DateTimeFormat('zh-CN', options);
console.log(formatter.format(date));
// 输出: "2025年12月19日 星期五"
```

### 时区选项

```js
const date = new Date('2025-12-19T10:30:00.000Z');

const options = {
    timeZone: 'Asia/Shanghai',
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit'
};

const formatter = new Intl.DateTimeFormat('zh-CN', options);
console.log(formatter.format(date));
// 输出: "2025/12/19 18:30"（UTC+8）
```

## 常用格式组合

### 短日期格式

```js
const date = new Date(2025, 11, 19);

const formatter = new Intl.DateTimeFormat('zh-CN', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit'
});

console.log(formatter.format(date));
// 输出: "2025/12/19"
```

### 长日期格式

```js
const date = new Date(2025, 11, 19);

const formatter = new Intl.DateTimeFormat('zh-CN', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    weekday: 'long'
});

console.log(formatter.format(date));
// 输出: "2025年12月19日 星期五"
```

### 日期时间格式

```js
const date = new Date(2025, 11, 19, 10, 30, 0);

const formatter = new Intl.DateTimeFormat('zh-CN', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    hour12: false
});

console.log(formatter.format(date));
// 输出: "2025/12/19 10:30"
```

## 不同地区的格式

### 中文格式

```js
const date = new Date(2025, 11, 19, 10, 30, 0);

const formatter = new Intl.DateTimeFormat('zh-CN', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
});

console.log(formatter.format(date));
// 输出: "2025年12月19日 10:30"
```

### 英文格式

```js
const date = new Date(2025, 11, 19, 10, 30, 0);

const formatter = new Intl.DateTimeFormat('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    hour12: true
});

console.log(formatter.format(date));
// 输出: "December 19, 2025, 10:30 AM"
```

### 日文格式

```js
const date = new Date(2025, 11, 19, 10, 30, 0);

const formatter = new Intl.DateTimeFormat('ja-JP', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
});

console.log(formatter.format(date));
// 输出: "2025年12月19日 10:30"
```

## formatToParts 方法

### 获取格式化部分

```js
const date = new Date(2025, 11, 19);
const formatter = new Intl.DateTimeFormat('zh-CN', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
});

const parts = formatter.formatToParts(date);
console.log(parts);
// 输出: [
//   { type: 'year', value: '2025' },
//   { type: 'literal', value: '年' },
//   { type: 'month', value: '12' },
//   { type: 'literal', value: '月' },
//   { type: 'day', value: '19' },
//   { type: 'literal', value: '日' }
// ]
```

### 自定义格式化

```js
function customFormat(date, locale, options) {
    const formatter = new Intl.DateTimeFormat(locale, options);
    const parts = formatter.formatToParts(date);
    
    return parts.map(part => {
        switch (part.type) {
            case 'year':
                return `[${part.value}]`;
            case 'month':
                return part.value.toUpperCase();
            default:
                return part.value;
        }
    }).join('');
}

const date = new Date(2025, 11, 19);
console.log(customFormat(date, 'zh-CN', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
}));
// 输出: "[2025]12月19日"
```

## formatRange 方法

### 格式化日期范围

```js
const date1 = new Date(2025, 11, 19);
const date2 = new Date(2025, 11, 25);

const formatter = new Intl.DateTimeFormat('zh-CN', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
});

console.log(formatter.formatRange(date1, date2));
// 输出: "2025年12月19日 - 2025年12月25日"
```

### 智能范围格式化

```js
const date1 = new Date(2025, 11, 19);
const date2 = new Date(2025, 11, 19, 14, 0, 0);

const formatter = new Intl.DateTimeFormat('zh-CN', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
});

console.log(formatter.formatRange(date1, date2));
// 输出: "2025年12月19日 00:00 - 14:00"（自动省略重复部分）
```

## 注意事项

1. **性能考虑**：创建格式化器对象有开销，建议复用
2. **时区处理**：使用 `timeZone` 选项指定时区
3. **选项组合**：某些选项组合可能不被支持
4. **浏览器兼容性**：某些新特性需要较新的浏览器
5. **区域设置**：使用标准的区域设置标识符

## 常见问题

### 问题 1：如何格式化相对时间？

使用 `Intl.RelativeTimeFormat`（见下一节）或手动计算：

```js
function formatRelative(date, locale = 'zh-CN') {
    const now = new Date();
    const diff = date.getTime() - now.getTime();
    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    
    if (days === 0) {
        return '今天';
    } else if (days === 1) {
        return '明天';
    } else if (days === -1) {
        return '昨天';
    } else {
        const formatter = new Intl.DateTimeFormat(locale, {
            month: 'long',
            day: 'numeric'
        });
        return formatter.format(date);
    }
}
```

### 问题 2：如何获取月份名称？

```js
function getMonthName(monthIndex, locale = 'zh-CN') {
    const date = new Date(2025, monthIndex, 1);
    const formatter = new Intl.DateTimeFormat(locale, { month: 'long' });
    return formatter.format(date);
}

console.log(getMonthName(11, 'zh-CN'));  // "12月"
console.log(getMonthName(11, 'en-US')); // "December"
```

## 最佳实践

1. **复用对象**：创建格式化器对象并复用
2. **选项优化**：根据需求选择合适的选项
3. **时区处理**：明确指定时区或使用 UTC
4. **性能优化**：使用缓存机制
5. **错误处理**：处理不支持的选项和区域设置

## 练习任务

1. 创建一个日期格式化函数，支持多种预定义格式（短日期、长日期、日期时间）。

2. 实现一个函数，根据区域设置自动选择最佳的日期格式。

3. 编写一个函数，使用 `formatToParts()` 方法自定义日期格式。

4. 创建一个日期范围格式化函数，智能处理相同和不同的日期部分。

5. 实现一个多语言日期格式化工具类，支持缓存和性能优化。
