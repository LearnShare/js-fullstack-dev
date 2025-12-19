# 2.15.4 数字与货币国际化

## 概述

`Intl.NumberFormat` 用于根据区域设置格式化数字、货币和百分比。`Intl.RelativeTimeFormat` 用于格式化相对时间。本节介绍这些 API 的使用方法。

## Intl.NumberFormat

### 语法

```js
new Intl.NumberFormat([locales[, options]])
```

### 参数详述

| 参数名    | 类型           | 说明                    | 是否必需 | 默认值 |
|:----------|:---------------|:------------------------|:---------|:-------|
| `locales` | string \| Array | 区域设置或区域设置数组   | 否       | 系统默认 |
| `options` | Object         | 格式化选项对象           | 否       | {}     |

### 返回值

返回一个 `NumberFormat` 对象，提供 `format()` 方法用于格式化数字。

## 基本用法

### 数字格式化

```js
const number = 1234567.89;

// 默认格式
const formatter1 = new Intl.NumberFormat('zh-CN');
console.log(formatter1.format(number));
// 输出: "1,234,567.89"

// 英文格式
const formatter2 = new Intl.NumberFormat('en-US');
console.log(formatter2.format(number));
// 输出: "1,234,567.89"

// 德文格式（使用点作为千位分隔符）
const formatter3 = new Intl.NumberFormat('de-DE');
console.log(formatter3.format(number));
// 输出: "1.234.567,89"
```

### 货币格式化

```js
const amount = 1234.56;

// 人民币
const formatter1 = new Intl.NumberFormat('zh-CN', {
    style: 'currency',
    currency: 'CNY'
});
console.log(formatter1.format(amount));
// 输出: "¥1,234.56"

// 美元
const formatter2 = new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD'
});
console.log(formatter2.format(amount));
// 输出: "$1,234.56"

// 欧元
const formatter3 = new Intl.NumberFormat('de-DE', {
    style: 'currency',
    currency: 'EUR'
});
console.log(formatter3.format(amount));
// 输出: "1.234,56 €"
```

### 百分比格式化

```js
const value = 0.1234;

const formatter = new Intl.NumberFormat('zh-CN', {
    style: 'percent',
    minimumFractionDigits: 2,
    maximumFractionDigits: 2
});
console.log(formatter.format(value));
// 输出: "12.34%"
```

## 格式化选项

### 基本选项

```js
const number = 1234567.89;

const options = {
    minimumIntegerDigits: 1,      // 最小整数位数
    minimumFractionDigits: 2,      // 最小小数位数
    maximumFractionDigits: 2,      // 最大小数位数
    useGrouping: true              // 是否使用分组（千位分隔符）
};

const formatter = new Intl.NumberFormat('zh-CN', options);
console.log(formatter.format(number));
// 输出: "1,234,567.89"
```

### 货币选项

```js
const amount = 1234.56;

const options = {
    style: 'currency',
    currency: 'CNY',               // 货币代码（ISO 4217）
    currencyDisplay: 'symbol',      // 'symbol' | 'code' | 'name'
    minimumFractionDigits: 2,
    maximumFractionDigits: 2
};

const formatter = new Intl.NumberFormat('zh-CN', options);
console.log(formatter.format(amount));
// 输出: "¥1,234.56"
```

### 单位选项

```js
const length = 1234.56;

const formatter = new Intl.NumberFormat('zh-CN', {
    style: 'unit',
    unit: 'meter',
    unitDisplay: 'short'
});
console.log(formatter.format(length));
// 输出: "1,234.56 米"
```

## 常用货币代码

| 货币代码 | 货币名称 | 符号 |
|:---------|:---------|:-----|
| `CNY`    | 人民币   | ¥    |
| `USD`    | 美元     | $    |
| `EUR`    | 欧元     | €    |
| `GBP`    | 英镑     | £    |
| `JPY`    | 日元     | ¥    |
| `KRW`    | 韩元     | ₩    |

## formatToParts 方法

### 获取格式化部分

```js
const amount = 1234.56;
const formatter = new Intl.NumberFormat('zh-CN', {
    style: 'currency',
    currency: 'CNY'
});

const parts = formatter.formatToParts(amount);
console.log(parts);
// 输出: [
//   { type: 'currency', value: '¥' },
//   { type: 'integer', value: '1' },
//   { type: 'group', value: ',' },
//   { type: 'integer', value: '234' },
//   { type: 'decimal', value: '.' },
//   { type: 'fraction', value: '56' }
// ]
```

### 自定义格式化

```js
function customCurrencyFormat(amount, locale, currency) {
    const formatter = new Intl.NumberFormat(locale, {
        style: 'currency',
        currency: currency
    });
    
    const parts = formatter.formatToParts(amount);
    return parts.map(part => {
        if (part.type === 'currency') {
            return `[${part.value}]`;
        }
        return part.value;
    }).join('');
}

console.log(customCurrencyFormat(1234.56, 'zh-CN', 'CNY'));
// 输出: "[¥]1,234.56"
```

## Intl.RelativeTimeFormat

### 语法

```js
new Intl.RelativeTimeFormat([locales[, options]])
```

### 基本用法

```js
const rtf = new Intl.RelativeTimeFormat('zh-CN', {
    numeric: 'auto',  // 'always' | 'auto'
    style: 'long'     // 'long' | 'short' | 'narrow'
});

console.log(rtf.format(-1, 'day'));   // "昨天"
console.log(rtf.format(0, 'day'));    // "今天"
console.log(rtf.format(1, 'day'));    // "明天"
console.log(rtf.format(-2, 'day'));   // "2天前"
console.log(rtf.format(2, 'day'));    // "2天后"
```

### 时间单位

```js
const rtf = new Intl.RelativeTimeFormat('zh-CN');

console.log(rtf.format(-1, 'year'));   // "去年"
console.log(rtf.format(1, 'year'));    // "明年"
console.log(rtf.format(-1, 'month'));  // "上个月"
console.log(rtf.format(1, 'month'));   // "下个月"
console.log(rtf.format(-1, 'week'));   // "上周"
console.log(rtf.format(1, 'week'));   // "下周"
console.log(rtf.format(-1, 'day'));   // "昨天"
console.log(rtf.format(1, 'day'));    // "明天"
console.log(rtf.format(-1, 'hour'));   // "1小时前"
console.log(rtf.format(1, 'hour'));   // "1小时后"
console.log(rtf.format(-1, 'minute')); // "1分钟前"
console.log(rtf.format(1, 'minute'));  // "1分钟后"
console.log(rtf.format(-1, 'second')); // "1秒前"
console.log(rtf.format(1, 'second'));  // "1秒后"
```

### 格式化选项

```js
// long 格式
const rtf1 = new Intl.RelativeTimeFormat('zh-CN', { style: 'long' });
console.log(rtf1.format(2, 'day'));  // "2天后"

// short 格式
const rtf2 = new Intl.RelativeTimeFormat('zh-CN', { style: 'short' });
console.log(rtf2.format(2, 'day'));  // "2天后"

// narrow 格式
const rtf3 = new Intl.RelativeTimeFormat('zh-CN', { style: 'narrow' });
console.log(rtf3.format(2, 'day'));  // "2天后"
```

### formatToParts 方法

```js
const rtf = new Intl.RelativeTimeFormat('zh-CN');
const parts = rtf.formatToParts(2, 'day');

console.log(parts);
// 输出: [
//   { type: 'integer', value: '2', unit: 'day' },
//   { type: 'literal', value: '天后' }
// ]
```

## 实用工具函数

### 格式化价格

```js
function formatPrice(amount, currency = 'CNY', locale = 'zh-CN') {
    const formatter = new Intl.NumberFormat(locale, {
        style: 'currency',
        currency: currency,
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    });
    return formatter.format(amount);
}

console.log(formatPrice(1234.56));           // "¥1,234.56"
console.log(formatPrice(1234.56, 'USD'));    // "$1,234.56"
console.log(formatPrice(1234.56, 'EUR', 'de-DE')); // "1.234,56 €"
```

### 格式化相对时间

```js
function formatRelativeTime(date, locale = 'zh-CN') {
    const rtf = new Intl.RelativeTimeFormat(locale, { numeric: 'auto' });
    const now = new Date();
    const diff = date.getTime() - now.getTime();
    
    const seconds = Math.floor(diff / 1000);
    const minutes = Math.floor(seconds / 60);
    const hours = Math.floor(minutes / 60);
    const days = Math.floor(hours / 24);
    const months = Math.floor(days / 30);
    const years = Math.floor(days / 365);
    
    if (Math.abs(years) > 0) {
        return rtf.format(years, 'year');
    } else if (Math.abs(months) > 0) {
        return rtf.format(months, 'month');
    } else if (Math.abs(days) > 0) {
        return rtf.format(days, 'day');
    } else if (Math.abs(hours) > 0) {
        return rtf.format(hours, 'hour');
    } else if (Math.abs(minutes) > 0) {
        return rtf.format(minutes, 'minute');
    } else {
        return rtf.format(seconds, 'second');
    }
}

const date = new Date(Date.now() - 2 * 60 * 60 * 1000);  // 2 小时前
console.log(formatRelativeTime(date));  // "2小时前"
```

## 注意事项

1. **货币代码**：使用 ISO 4217 标准货币代码
2. **小数位数**：注意不同货币的小数位数要求（如日元无小数）
3. **性能考虑**：创建格式化器对象有开销，建议复用
4. **浏览器支持**：某些新特性需要较新的浏览器
5. **区域设置**：使用标准的区域设置标识符

## 常见问题

### 问题 1：如何格式化大数字？

```js
function formatLargeNumber(number, locale = 'zh-CN') {
    const formatter = new Intl.NumberFormat(locale, {
        notation: 'compact',  // 'standard' | 'compact' | 'scientific' | 'engineering'
        compactDisplay: 'short'
    });
    return formatter.format(number);
}

console.log(formatLargeNumber(1234567));  // "123万"
console.log(formatLargeNumber(1234567890));  // "12亿"
```

### 问题 2：如何处理无小数的货币？

```js
function formatCurrency(amount, currency, locale = 'zh-CN') {
    // 日元等货币无小数
    const noDecimalCurrencies = ['JPY', 'KRW'];
    const hasDecimal = !noDecimalCurrencies.includes(currency);
    
    const formatter = new Intl.NumberFormat(locale, {
        style: 'currency',
        currency: currency,
        minimumFractionDigits: hasDecimal ? 2 : 0,
        maximumFractionDigits: hasDecimal ? 2 : 0
    });
    
    return formatter.format(amount);
}

console.log(formatCurrency(1234, 'CNY'));  // "¥1,234.00"
console.log(formatCurrency(1234, 'JPY'));  // "¥1,234"（无小数）
```

## 最佳实践

1. **复用对象**：创建格式化器对象并复用
2. **货币代码**：使用标准的 ISO 4217 货币代码
3. **小数处理**：根据货币类型设置正确的小数位数
4. **性能优化**：使用缓存机制
5. **错误处理**：处理不支持的货币和区域设置

## 练习任务

1. 创建一个货币格式化函数，支持多种货币和区域设置。

2. 实现一个函数，格式化大数字为紧凑格式（如 "123万"、"12亿"）。

3. 编写一个相对时间格式化函数，自动选择合适的时间单位。

4. 创建一个数字格式化工具类，支持数字、货币、百分比等多种格式。

5. 实现一个智能格式化函数，根据数字大小自动选择最佳格式。
