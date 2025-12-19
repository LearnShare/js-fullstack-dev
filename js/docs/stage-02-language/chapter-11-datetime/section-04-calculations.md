# 2.11.4 日期计算与比较

## 概述

日期计算包括日期的加减运算、日期比较、差值计算等操作。本节介绍常用的日期计算方法。

## 日期加减

### 加减天数

```js
function addDays(date, days) {
    const result = new Date(date);
    result.setDate(result.getDate() + days);
    return result;
}

function subtractDays(date, days) {
    return addDays(date, -days);
}

const date = new Date(2025, 11, 19);
const nextWeek = addDays(date, 7);
const lastWeek = subtractDays(date, 7);

console.log(nextWeek);  // 2025-12-26
console.log(lastWeek);  // 2025-12-12
```

### 加减月份

```js
function addMonths(date, months) {
    const result = new Date(date);
    result.setMonth(result.getMonth() + months);
    return result;
}

function subtractMonths(date, months) {
    return addMonths(date, -months);
}

const date = new Date(2025, 11, 19);
const nextMonth = addMonths(date, 1);
const lastMonth = subtractMonths(date, 1);

console.log(nextMonth);  // 2026-01-19
console.log(lastMonth);  // 2025-11-19
```

### 加减年份

```js
function addYears(date, years) {
    const result = new Date(date);
    result.setFullYear(result.getFullYear() + years);
    return result;
}

function subtractYears(date, years) {
    return addYears(date, -years);
}

const date = new Date(2025, 11, 19);
const nextYear = addYears(date, 1);
const lastYear = subtractYears(date, 1);

console.log(nextYear);  // 2026-12-19
console.log(lastYear);  // 2024-12-19
```

### 加减小时、分钟、秒

```js
function addHours(date, hours) {
    const result = new Date(date);
    result.setHours(result.getHours() + hours);
    return result;
}

function addMinutes(date, minutes) {
    const result = new Date(date);
    result.setMinutes(result.getMinutes() + minutes);
    return result;
}

function addSeconds(date, seconds) {
    const result = new Date(date);
    result.setSeconds(result.getSeconds() + seconds);
    return result;
}

const date = new Date(2025, 11, 19, 10, 30, 0);
const nextHour = addHours(date, 1);
const next30Minutes = addMinutes(date, 30);
const next30Seconds = addSeconds(date, 30);

console.log(nextHour);        // 11:30:00
console.log(next30Minutes);   // 11:00:00
console.log(next30Seconds);   // 10:30:30
```

## 日期差值计算

### 计算天数差

```js
function daysDifference(date1, date2) {
    const diff = Math.abs(date2.getTime() - date1.getTime());
    return Math.floor(diff / (1000 * 60 * 60 * 24));
}

const date1 = new Date(2025, 11, 19);
const date2 = new Date(2025, 11, 25);
const diff = daysDifference(date1, date2);
console.log(diff);  // 6
```

### 计算小时差

```js
function hoursDifference(date1, date2) {
    const diff = Math.abs(date2.getTime() - date1.getTime());
    return Math.floor(diff / (1000 * 60 * 60));
}

const date1 = new Date(2025, 11, 19, 10, 0, 0);
const date2 = new Date(2025, 11, 19, 16, 30, 0);
const diff = hoursDifference(date1, date2);
console.log(diff);  // 6
```

### 计算分钟差

```js
function minutesDifference(date1, date2) {
    const diff = Math.abs(date2.getTime() - date1.getTime());
    return Math.floor(diff / (1000 * 60));
}

const date1 = new Date(2025, 11, 19, 10, 0, 0);
const date2 = new Date(2025, 11, 19, 10, 45, 0);
const diff = minutesDifference(date1, date2);
console.log(diff);  // 45
```

### 计算完整时间差

```js
function timeDifference(date1, date2) {
    const diff = Math.abs(date2.getTime() - date1.getTime());
    
    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((diff % (1000 * 60)) / 1000);
    
    return { days, hours, minutes, seconds };
}

const date1 = new Date(2025, 11, 19, 10, 0, 0);
const date2 = new Date(2025, 11, 20, 14, 30, 45);
const diff = timeDifference(date1, date2);
console.log(diff);
// 输出: { days: 1, hours: 4, minutes: 30, seconds: 45 }
```

## 日期比较

### 基本比较

```js
function compareDates(date1, date2) {
    const time1 = date1.getTime();
    const time2 = date2.getTime();
    
    if (time1 < time2) return -1;
    if (time1 > time2) return 1;
    return 0;
}

const date1 = new Date(2025, 11, 19);
const date2 = new Date(2025, 11, 20);
console.log(compareDates(date1, date2));  // -1（date1 早于 date2）
```

### 比较函数

```js
function isBefore(date1, date2) {
    return date1.getTime() < date2.getTime();
}

function isAfter(date1, date2) {
    return date1.getTime() > date2.getTime();
}

function isEqual(date1, date2) {
    return date1.getTime() === date2.getTime();
}

function isSameDay(date1, date2) {
    return date1.getFullYear() === date2.getFullYear() &&
           date1.getMonth() === date2.getMonth() &&
           date1.getDate() === date2.getDate();
}

const date1 = new Date(2025, 11, 19, 10, 0, 0);
const date2 = new Date(2025, 11, 19, 14, 0, 0);

console.log(isBefore(date1, date2));   // true
console.log(isAfter(date1, date2));   // false
console.log(isEqual(date1, date2));   // false
console.log(isSameDay(date1, date2));  // true
```

### 范围检查

```js
function isInRange(date, startDate, endDate) {
    const time = date.getTime();
    const start = startDate.getTime();
    const end = endDate.getTime();
    return time >= start && time <= end;
}

const date = new Date(2025, 11, 19);
const start = new Date(2025, 11, 1);
const end = new Date(2025, 11, 31);

console.log(isInRange(date, start, end));  // true
```

## 日期工具函数

### 获取月份第一天和最后一天

```js
function getFirstDayOfMonth(date) {
    return new Date(date.getFullYear(), date.getMonth(), 1);
}

function getLastDayOfMonth(date) {
    return new Date(date.getFullYear(), date.getMonth() + 1, 0);
}

const date = new Date(2025, 11, 19);
console.log(getFirstDayOfMonth(date));  // 2025-12-01
console.log(getLastDayOfMonth(date));   // 2025-12-31
```

### 获取周的开始和结束

```js
function getStartOfWeek(date, firstDayOfWeek = 0) {
    const day = date.getDay();
    const diff = date.getDate() - day + (day === 0 ? -6 : firstDayOfWeek);
    return new Date(date.setDate(diff));
}

function getEndOfWeek(date, firstDayOfWeek = 0) {
    const start = getStartOfWeek(date, firstDayOfWeek);
    return addDays(start, 6);
}

const date = new Date(2025, 11, 19);
console.log(getStartOfWeek(date));  // 2025-12-15（星期日）
console.log(getEndOfWeek(date));    // 2025-12-21（星期六）
```

### 计算年龄

```js
function calculateAge(birthDate) {
    const today = new Date();
    let age = today.getFullYear() - birthDate.getFullYear();
    const monthDiff = today.getMonth() - birthDate.getMonth();
    
    if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }
    
    return age;
}

const birthDate = new Date(1990, 5, 15);
const age = calculateAge(birthDate);
console.log(age);  // 35（示例）
```

## 注意事项

1. **月份溢出**：Date 对象会自动处理月份溢出（如 12 月 + 1 = 1 月）
2. **闰年处理**：Date 对象自动处理闰年
3. **时区问题**：计算时注意时区影响
4. **性能考虑**：频繁计算可能影响性能
5. **精度问题**：毫秒级精度可能在某些场景下不够

## 常见问题

### 问题 1：如何计算两个日期之间的工作日？

```js
function workingDaysBetween(startDate, endDate) {
    let count = 0;
    const current = new Date(startDate);
    
    while (current <= endDate) {
        const day = current.getDay();
        if (day !== 0 && day !== 6) {  // 排除周末
            count++;
        }
        current.setDate(current.getDate() + 1);
    }
    
    return count;
}

const start = new Date(2025, 11, 16);  // 星期一
const end = new Date(2025, 11, 20);    // 星期五
console.log(workingDaysBetween(start, end));  // 5
```

### 问题 2：如何获取两个日期之间的所有日期？

```js
function getDatesBetween(startDate, endDate) {
    const dates = [];
    const current = new Date(startDate);
    
    while (current <= endDate) {
        dates.push(new Date(current));
        current.setDate(current.getDate() + 1);
    }
    
    return dates;
}

const start = new Date(2025, 11, 19);
const end = new Date(2025, 11, 23);
const dates = getDatesBetween(start, end);
console.log(dates.length);  // 5
```

## 最佳实践

1. **使用时间戳**：比较和计算时使用时间戳更高效
2. **处理边界**：注意月份、年份的边界情况
3. **统一时区**：计算时统一使用 UTC 或本地时区
4. **性能优化**：对频繁使用的计算结果进行缓存
5. **使用库**：复杂计算考虑使用 date-fns、dayjs 等库

## 练习任务

1. 创建一个函数，计算两个日期之间的天数差，考虑正负值。

2. 实现一个函数，判断给定日期是否在指定日期范围内。

3. 编写一个函数，获取指定日期所在月份的第一天和最后一天。

4. 创建一个函数，计算两个日期之间的工作日数量（排除周末）。

5. 实现一个函数，获取两个日期之间的所有日期数组。
