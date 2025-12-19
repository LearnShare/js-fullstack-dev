# 2.15.2 Intl API 基础

## 概述

Intl API 是 JavaScript 的国际化 API，提供了一组对象和方法来支持多语言和地区特定的格式化。本节介绍 Intl API 的核心概念和基本用法。

## Intl 对象

### 检测支持

```js
// 检测 Intl 对象是否存在
if (typeof Intl !== 'undefined') {
    console.log('Intl API 支持');
} else {
    console.log('Intl API 不支持');
}
```

### 主要属性

```js
// Intl 对象的主要属性
console.log(Intl.DateTimeFormat);   // DateTimeFormat 构造函数
console.log(Intl.NumberFormat);     // NumberFormat 构造函数
console.log(Intl.RelativeTimeFormat); // RelativeTimeFormat 构造函数
console.log(Intl.Collator);          // Collator 构造函数
console.log(Intl.PluralRules);      // PluralRules 构造函数
console.log(Intl.ListFormat);       // ListFormat 构造函数
console.log(Intl.Locale);           // Locale 构造函数
```

## Intl.Locale

### 创建 Locale 对象

```js
// 基本用法
const locale1 = new Intl.Locale('zh-CN');
console.log(locale1.toString());  // "zh-CN"

// 使用选项
const locale2 = new Intl.Locale('zh', {
    script: 'Hans',
    region: 'CN'
});
console.log(locale2.toString());  // "zh-Hans-CN"
```

### Locale 属性

```js
const locale = new Intl.Locale('zh-Hans-CN');

console.log(locale.language);  // "zh"
console.log(locale.script);    // "Hans"
console.log(locale.region);    // "CN"
console.log(locale.baseName);  // "zh-Hans-CN"
```

## 区域设置解析

### 解析区域设置

```js
function parseLocale(localeString) {
    const locale = new Intl.Locale(localeString);
    return {
        language: locale.language,
        script: locale.script || null,
        region: locale.region || null,
        baseName: locale.baseName
    };
}

const parsed = parseLocale('zh-Hans-CN');
console.log(parsed);
// 输出: { language: 'zh', script: 'Hans', region: 'CN', baseName: 'zh-Hans-CN' }
```

### 区域设置匹配

```js
// 获取最佳匹配的区域设置
function getBestLocale(requested, available) {
    for (const locale of available) {
        if (locale.startsWith(requested) || requested.startsWith(locale)) {
            return locale;
        }
    }
    return available[0] || 'en-US';
}

const requested = 'zh-CN';
const available = ['zh-CN', 'zh-TW', 'en-US'];
const best = getBestLocale(requested, available);
console.log(best);  // "zh-CN"
```

## 格式化器创建模式

### 直接创建

```js
// 每次创建新的格式化器
const date1 = new Date();
const formatter1 = new Intl.DateTimeFormat('zh-CN');
console.log(formatter1.format(date1));

const date2 = new Date();
const formatter2 = new Intl.DateTimeFormat('zh-CN');
console.log(formatter2.format(date2));
```

### 复用格式化器

```js
// 创建一次，多次使用（推荐）
const formatter = new Intl.DateTimeFormat('zh-CN');

const dates = [new Date(), new Date(), new Date()];
dates.forEach(date => {
    console.log(formatter.format(date));
});
```

### 工厂函数模式

```js
// 创建格式化器工厂
function createFormatter(type, locale, options) {
    switch (type) {
        case 'date':
            return new Intl.DateTimeFormat(locale, options);
        case 'number':
            return new Intl.NumberFormat(locale, options);
        default:
            throw new Error('Unknown formatter type');
    }
}

const dateFormatter = createFormatter('date', 'zh-CN');
const numberFormatter = createFormatter('number', 'zh-CN');
```

## 选项对象

### 选项结构

```js
// 日期时间选项
const dateOptions = {
    year: 'numeric',      // 'numeric' | '2-digit'
    month: 'long',        // 'numeric' | '2-digit' | 'long' | 'short' | 'narrow'
    day: 'numeric',       // 'numeric' | '2-digit'
    weekday: 'long',      // 'long' | 'short' | 'narrow'
    hour: '2-digit',      // 'numeric' | '2-digit'
    minute: '2-digit',    // 'numeric' | '2-digit'
    second: '2-digit',    // 'numeric' | '2-digit'
    hour12: false,        // true | false
    timeZone: 'Asia/Shanghai'  // 时区
};

// 数字选项
const numberOptions = {
    style: 'currency',    // 'decimal' | 'currency' | 'percent' | 'unit'
    currency: 'CNY',      // 货币代码
    minimumFractionDigits: 2,
    maximumFractionDigits: 2
};
```

## 性能考虑

### 格式化器缓存

```js
// 缓存格式化器对象
const formatterCache = new Map();

function getFormatter(type, locale, options = {}) {
    const key = `${type}-${locale}-${JSON.stringify(options)}`;
    
    if (!formatterCache.has(key)) {
        let formatter;
        switch (type) {
            case 'date':
                formatter = new Intl.DateTimeFormat(locale, options);
                break;
            case 'number':
                formatter = new Intl.NumberFormat(locale, options);
                break;
            default:
                throw new Error('Unknown formatter type');
        }
        formatterCache.set(key, formatter);
    }
    
    return formatterCache.get(key);
}

// 使用缓存的格式化器
const formatter = getFormatter('date', 'zh-CN');
console.log(formatter.format(new Date()));
```

## 注意事项

1. **对象创建开销**：格式化器对象创建有一定开销，建议复用
2. **选项验证**：无效的选项可能导致错误
3. **区域设置支持**：某些区域设置可能不被支持
4. **性能优化**：使用缓存机制提高性能
5. **浏览器兼容性**：检查浏览器支持情况

## 常见问题

### 问题 1：如何检测区域设置是否支持？

```js
function isLocaleSupported(locale) {
    try {
        const formatter = new Intl.DateTimeFormat(locale);
        return true;
    } catch (e) {
        return false;
    }
}

console.log(isLocaleSupported('zh-CN'));  // true
console.log(isLocaleSupported('xx-XX'));  // false
```

### 问题 2：如何获取支持的区域设置列表？

```js
// 注意：浏览器可能不提供完整的支持列表
// 可以通过尝试创建格式化器来检测
function getSupportedLocales(requestedLocales) {
    return requestedLocales.filter(locale => {
        try {
            new Intl.DateTimeFormat(locale);
            return true;
        } catch (e) {
            return false;
        }
    });
}

const locales = getSupportedLocales(['zh-CN', 'en-US', 'xx-XX']);
console.log(locales);  // ["zh-CN", "en-US"]
```

## 最佳实践

1. **复用对象**：创建格式化器对象并复用
2. **缓存机制**：使用缓存存储格式化器对象
3. **错误处理**：处理区域设置不支持的情况
4. **性能优化**：避免频繁创建格式化器对象
5. **选项验证**：验证选项的有效性

## 练习任务

1. 创建一个格式化器缓存类，支持日期和数字格式化器的缓存和复用。

2. 实现一个函数，检测给定的区域设置是否被支持。

3. 编写一个格式化器工厂函数，根据类型和选项创建相应的格式化器。

4. 创建一个区域设置工具类，提供区域设置解析、匹配和验证功能。

5. 实现一个性能优化的格式化函数，使用缓存机制提高性能。
