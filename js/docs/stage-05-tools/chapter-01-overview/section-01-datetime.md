# 5.1.1 日期时间处理库

## 概述

日期时间处理是开发中的常见需求。JavaScript 原生的 Date 对象功能有限，因此出现了许多优秀的日期时间处理库。本节介绍常用的日期时间处理库。

## Day.js

### 简介

Day.js 是一个轻量级的日期时间处理库，API 设计简洁，体积小（仅 2KB），是 Moment.js 的现代替代品。

### 安装

```bash
npm install dayjs
```

### 基本使用

```js
import dayjs from 'dayjs';

// 创建当前时间
const now = dayjs();

// 创建指定时间
const date = dayjs('2025-12-17');
const date2 = dayjs(new Date(2025, 11, 17));

// 格式化
console.log(dayjs().format('YYYY-MM-DD HH:mm:ss')); // "2025-12-17 14:30:00"
```

### 常用方法

| 方法                | 说明           | 示例                                  |
|:--------------------|:---------------|:--------------------------------------|
| `format()`          | 格式化日期     | `dayjs().format('YYYY-MM-DD')`        |
| `add()`             | 添加时间       | `dayjs().add(1, 'day')`               |
| `subtract()`        | 减去时间       | `dayjs().subtract(1, 'month')`        |
| `diff()`            | 计算时间差     | `dayjs().diff(other, 'day')`          |
| `isBefore()`        | 是否早于       | `dayjs().isBefore(other)`             |
| `isAfter()`         | 是否晚于       | `dayjs().isAfter(other)`              |
| `isSame()`          | 是否相同       | `dayjs().isSame(other, 'day')`        |

### 插件系统

```js
// 使用插件扩展功能
import dayjs from 'dayjs';
import relativeTime from 'dayjs/plugin/relativeTime';
import utc from 'dayjs/plugin/utc';

dayjs.extend(relativeTime);
dayjs.extend(utc);

// 相对时间
console.log(dayjs().from(dayjs().subtract(1, 'day'))); // "a day ago"
```

## date-fns

### 简介

date-fns 是一个函数式的日期时间处理库，提供了大量实用的函数，支持按需导入，Tree-shaking 友好。

### 安装

```bash
npm install date-fns
```

### 基本使用

```js
import { format, addDays, differenceInDays } from 'date-fns';

// 格式化
console.log(format(new Date(), 'yyyy-MM-dd')); // "2025-12-17"

// 添加天数
const tomorrow = addDays(new Date(), 1);

// 计算时间差
const days = differenceInDays(new Date(2025, 11, 20), new Date());
console.log(days); // 3
```

### 常用函数

| 函数                  | 说明           | 示例                                              |
|:----------------------|:---------------|:--------------------------------------------------|
| `format()`            | 格式化日期     | `format(date, 'yyyy-MM-dd')`                     |
| `addDays()`           | 添加天数       | `addDays(date, 7)`                                |
| `subDays()`           | 减去天数       | `subDays(date, 7)`                                |
| `differenceInDays()`  | 计算天数差     | `differenceInDays(date1, date2)`                  |
| `isBefore()`          | 是否早于       | `isBefore(date1, date2)`                          |
| `isAfter()`           | 是否晚于       | `isAfter(date1, date2)`                           |
| `isSameDay()`         | 是否同一天     | `isSameDay(date1, date2)`                         |

## Moment.js（历史）

### 简介

Moment.js 是一个功能强大的日期时间处理库，但已经进入维护模式，不再推荐用于新项目。

### 为什么不推荐

1. **体积大**：体积较大（约 70KB）
2. **可变对象**：Moment 对象是可变的，容易出错
3. **已进入维护模式**：官方推荐迁移到 Day.js 或 date-fns

### 迁移建议

如果项目中使用 Moment.js，建议迁移到 Day.js 或 date-fns。

## 库对比

| 特性          | Day.js      | date-fns    | Moment.js   |
|:--------------|:------------|:------------|:------------|
| 体积          | 2KB         | 可 Tree-shake | 70KB      |
| API 风格      | 链式调用    | 函数式      | 链式调用    |
| 不可变性      | 支持        | 支持        | 不支持      |
| Tree-shaking  | 部分支持    | 完全支持    | 不支持      |
| 维护状态      | 活跃        | 活跃        | 维护模式    |

## 选择建议

1. **新项目**：推荐使用 Day.js 或 date-fns
2. **需要 Tree-shaking**：推荐 date-fns
3. **需要插件**：推荐 Day.js
4. **旧项目**：逐步迁移到 Day.js 或 date-fns

## 注意事项

1. **时区处理**：注意时区问题，使用相应的插件或函数
2. **格式化字符串**：不同库的格式化字符串可能不同
3. **不可变性**：Day.js 和 date-fns 都是不可变的，每次操作返回新对象
4. **性能考虑**：对于大量日期操作，注意性能影响

## 最佳实践

1. **选择合适库**：根据项目需求选择合适的库
2. **按需导入**：使用 date-fns 时，按需导入函数
3. **时区处理**：使用专门的时区处理插件或函数
4. **格式化统一**：统一使用格式化字符串，避免混乱

## 练习

1. **Day.js 基础**：使用 Day.js 格式化当前时间，并计算未来 7 天的日期。

2. **date-fns 应用**：使用 date-fns 计算两个日期之间的天数差，并判断是否在同一周。

3. **日期比较**：使用选择的库比较多个日期，找出最早和最晚的日期。

4. **相对时间**：使用 Day.js 插件显示相对时间（如 "2 hours ago"）。

5. **时区转换**：使用选择的库处理不同时区的日期时间。

完成以上练习后，继续学习下一节，了解工具函数库。

## 总结

Day.js 和 date-fns 是现代 JavaScript 开发中推荐的日期时间处理库。Day.js 体积小、API 简洁；date-fns 函数式、支持 Tree-shaking。Moment.js 已进入维护模式，不推荐用于新项目。根据项目需求选择合适的库。

## 相关资源

- [Day.js 官网](https://day.js.org/)
- [date-fns 官网](https://date-fns.org/)
- [Moment.js 官网](https://momentjs.com/)
