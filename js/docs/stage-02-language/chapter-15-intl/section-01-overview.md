# 2.15.1 国际化概述

## 概述

国际化（Internationalization，简称 i18n）是指设计和开发应用程序时，使其能够适应不同语言、地区和文化习惯的过程。JavaScript 提供了 Intl API 来支持国际化功能。

## 特性

- **多语言支持**：支持多种语言的日期、数字、货币格式化
- **区域设置**：基于区域设置自动选择格式
- **标准 API**：基于 ECMAScript 国际化规范
- **浏览器支持**：现代浏览器广泛支持
- **性能优化**：内置性能优化机制

## 国际化 vs 本地化

| 特性     | 国际化（i18n）                    | 本地化（l10n）                    |
|:---------|:----------------------------------|:----------------------------------|
| 定义     | 使应用适应不同语言和地区           | 为特定地区定制应用                 |
| 范围     | 架构和设计层面                    | 内容和翻译层面                    |
| 示例     | 支持多语言日期格式                | 将文本翻译为中文                  |
| 关系     | 国际化为本地化提供基础             | 本地化在国际化基础上进行           |

## 区域设置（Locale）

### 区域设置格式

区域设置标识符格式：`language[-script][-region]`

- `language`：语言代码（ISO 639-1），如 `zh`、`en`
- `script`：脚本代码（可选），如 `Hans`、`Hant`
- `region`：地区代码（ISO 3166-1），如 `CN`、`US`

### 常见区域设置

| 区域设置    | 说明           | 示例                          |
|:------------|:---------------|:------------------------------|
| `zh-CN`     | 简体中文（中国）| 日期：2025/12/19              |
| `zh-TW`     | 繁体中文（台湾）| 日期：2025/12/19              |
| `en-US`     | 英语（美国）    | 日期：12/19/2025              |
| `en-GB`     | 英语（英国）    | 日期：19/12/2025              |
| `ja-JP`     | 日语（日本）    | 日期：2025/12/19              |
| `fr-FR`     | 法语（法国）    | 日期：19/12/2025              |
| `de-DE`     | 德语（德国）    | 日期：19.12.2025              |

### 区域设置示例

```js
// 基本语言代码
console.log('zh');   // 中文
console.log('en');   // 英语
console.log('ja');   // 日语

// 语言 + 地区
console.log('zh-CN');  // 简体中文（中国）
console.log('zh-TW');  // 繁体中文（台湾）
console.log('en-US');  // 英语（美国）
console.log('en-GB');  // 英语（英国）

// 语言 + 脚本 + 地区
console.log('zh-Hans-CN');  // 简体中文（中国）
console.log('zh-Hant-TW');  // 繁体中文（台湾）
```

## Intl API 概述

### 主要对象

| 对象                      | 用途                     |
|:--------------------------|:-------------------------|
| `Intl.DateTimeFormat`     | 日期时间格式化            |
| `Intl.NumberFormat`       | 数字格式化                |
| `Intl.RelativeTimeFormat` | 相对时间格式化            |
| `Intl.Collator`           | 字符串比较和排序          |
| `Intl.PluralRules`        | 复数规则                  |
| `Intl.ListFormat`         | 列表格式化                |
| `Intl.Locale`             | 区域设置对象              |

### 基本用法

```js
// 日期时间格式化
const date = new Date();
const formatter = new Intl.DateTimeFormat('zh-CN');
console.log(formatter.format(date));
// 输出: "2025/12/19"

// 数字格式化
const number = 1234567.89;
const numFormatter = new Intl.NumberFormat('zh-CN');
console.log(numFormatter.format(number));
// 输出: "1,234,567.89"
```

## 国际化的优势

### 1. 用户体验

```js
// 根据用户区域设置自动格式化
const userLocale = navigator.language || 'zh-CN';
const date = new Date();
const formatter = new Intl.DateTimeFormat(userLocale);
console.log(formatter.format(date));
// 中文用户：2025/12/19
// 英文用户：12/19/2025
```

### 2. 数据准确性

```js
// 正确的货币格式化
const price = 1234.56;
const formatter = new Intl.NumberFormat('zh-CN', {
    style: 'currency',
    currency: 'CNY'
});
console.log(formatter.format(price));
// 输出: "¥1,234.56"
```

### 3. 文化适应

```js
// 不同地区的数字格式
const number = 1234567.89;

console.log(new Intl.NumberFormat('en-US').format(number));
// 输出: "1,234,567.89"

console.log(new Intl.NumberFormat('de-DE').format(number));
// 输出: "1.234.567,89"（使用点作为千位分隔符，逗号作为小数分隔符）
```

## 浏览器支持

### 检测支持

```js
function isIntlSupported() {
    return typeof Intl !== 'undefined' &&
           typeof Intl.DateTimeFormat !== 'undefined' &&
           typeof Intl.NumberFormat !== 'undefined';
}

console.log(isIntlSupported());
// 现代浏览器：true
```

### 兼容性处理

```js
function safeIntlFormat(date, locale) {
    if (typeof Intl !== 'undefined' && Intl.DateTimeFormat) {
        const formatter = new Intl.DateTimeFormat(locale);
        return formatter.format(date);
    }
    // 降级处理
    return date.toLocaleDateString();
}
```

## 注意事项

1. **浏览器支持**：Intl API 需要现代浏览器支持
2. **性能考虑**：创建格式化器对象有性能开销，考虑复用
3. **区域设置**：使用标准的区域设置标识符
4. **数据格式**：不同地区的日期、数字格式可能不同
5. **时区处理**：日期时间格式化时注意时区问题

## 常见问题

### 问题 1：如何获取用户区域设置？

```js
// 方法 1：navigator.language
const locale1 = navigator.language;
console.log(locale1);  // "zh-CN"

// 方法 2：navigator.languages（首选语言列表）
const locales = navigator.languages;
console.log(locales);  // ["zh-CN", "zh", "en-US", "en"]

// 方法 3：从 URL 或配置获取
const locale3 = new URLSearchParams(window.location.search).get('locale') || 'zh-CN';
```

### 问题 2：如何处理不支持的区域设置？

```js
function getSupportedLocale(requestedLocale, fallback = 'en-US') {
    try {
        const formatter = new Intl.DateTimeFormat(requestedLocale);
        return requestedLocale;
    } catch (e) {
        return fallback;
    }
}

const locale = getSupportedLocale('xx-XX', 'zh-CN');
console.log(locale);  // "zh-CN"（如果 xx-XX 不支持）
```

### 问题 3：Intl API 的性能如何？

Intl API 的格式化器创建有一定开销，建议：

```js
// 创建格式化器对象并复用
const dateFormatter = new Intl.DateTimeFormat('zh-CN');
const numberFormatter = new Intl.NumberFormat('zh-CN');

// 多次使用同一个格式化器
const dates = [new Date(), new Date(), new Date()];
dates.forEach(date => {
    console.log(dateFormatter.format(date));
});
```

## 最佳实践

1. **检测支持**：使用前检测浏览器是否支持 Intl API
2. **复用对象**：创建格式化器对象并复用，避免频繁创建
3. **降级处理**：为不支持的环境提供降级方案
4. **区域设置**：使用标准的区域设置标识符
5. **性能优化**：缓存格式化器对象

## 练习任务

1. 创建一个函数，检测浏览器是否支持 Intl API，并提供降级方案。

2. 编写一个函数，获取用户的区域设置，并验证其有效性。

3. 实现一个国际化工具类，封装常用的格式化功能。

4. 创建一个函数，根据区域设置自动选择日期格式。

5. 编写一个函数，处理不支持的区域设置，自动回退到默认区域设置。
