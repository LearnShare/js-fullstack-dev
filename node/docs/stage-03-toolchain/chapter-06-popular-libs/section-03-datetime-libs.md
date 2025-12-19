# 3.6.3 日期时间库

## 1. 概述

日期时间处理是开发中的常见需求。虽然 JavaScript 提供了 Date 对象，但使用第三方库可以简化日期时间操作，提供更好的 API 和功能。理解日期时间库的使用对于处理日期时间相关需求非常重要。

## 2. 特性说明

- **简化 API**：提供更简洁的 API，易于使用。
- **时区支持**：支持时区处理。
- **格式化**：强大的格式化功能。
- **解析**：支持多种格式的日期解析。
- **计算**：支持日期计算和比较。

## 3. 主流日期时间库

| 库名         | 特点                                     | 适用场景                       |
|:-------------|:-----------------------------------------|:-------------------------------|
| **date-fns** | 函数式、模块化、Tree-shaking 友好        | 现代项目、推荐使用             |
| **dayjs**    | 轻量级、API 类似 moment.js               | 需要轻量级解决方案             |
| **luxon**    | 功能强大、时区支持完善                   | 需要复杂时区处理               |

## 4. 基本用法

### 示例 1：date-fns

```ts
// 文件: datetime-date-fns.ts
// 功能: date-fns 使用示例

import { format, parse, addDays, differenceInDays } from 'date-fns';

// 格式化
const now = new Date();
const formatted = format(now, 'yyyy-MM-dd HH:mm:ss');
console.log('Formatted:', formatted);

// 解析
const parsed = parse('2024-01-01', 'yyyy-MM-dd', new Date());

// 计算
const tomorrow = addDays(now, 1);
const diff = differenceInDays(tomorrow, now);
console.log('Difference:', diff);
```

### 示例 2：dayjs

```ts
// 文件: datetime-dayjs.ts
// 功能: dayjs 使用示例

import dayjs from 'dayjs';

// 创建和格式化
const now = dayjs();
const formatted = now.format('YYYY-MM-DD HH:mm:ss');
console.log('Formatted:', formatted);

// 计算
const tomorrow = now.add(1, 'day');
const diff = tomorrow.diff(now, 'day');
console.log('Difference:', diff);

// 解析
const parsed = dayjs('2024-01-01', 'YYYY-MM-DD');
```

### 示例 3：luxon

```ts
// 文件: datetime-luxon.ts
// 功能: luxon 使用示例

import { DateTime } from 'luxon';

// 创建和格式化
const now = DateTime.now();
const formatted = now.toFormat('yyyy-MM-dd HH:mm:ss');
console.log('Formatted:', formatted);

// 时区处理
const utc = now.toUTC();
const local = now.toLocal();

// 计算
const tomorrow = now.plus({ days: 1 });
const diff = tomorrow.diff(now, 'days');
console.log('Difference:', diff.days);
```

## 5. 参数说明：日期时间库参数

### date-fns 参数

| 函数名           | 参数                                     | 说明                           |
|:-----------------|:-----------------------------------------|:-------------------------------|
| **format**       | `(date, formatString)`                   | 格式化日期                     |
| **parse**        | `(dateString, formatString, referenceDate)`| 解析日期字符串               |
| **addDays**      | `(date, amount)`                         | 添加天数                       |
| **differenceInDays**| `(dateLeft, dateRight)`                | 计算日期差                     |

## 6. 返回值与状态说明

日期时间库操作的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **格式化**   | String       | 返回格式化后的字符串                     |
| **解析**     | Date/DateTime | 返回日期对象                             |
| **计算**     | Date/Number  | 返回计算后的日期或差值                   |

## 7. 代码示例：完整的日期时间处理

以下示例演示了完整的日期时间处理：

```ts
// 文件: datetime-complete.ts
// 功能: 完整的日期时间处理

import { format, parse, addDays, differenceInDays, startOfDay, endOfDay } from 'date-fns';

class DateTimeHelper {
    formatDate(date: Date, formatString: string = 'yyyy-MM-dd'): string {
        return format(date, formatString);
    }
    
    parseDate(dateString: string, formatString: string = 'yyyy-MM-dd'): Date {
        return parse(dateString, formatString, new Date());
    }
    
    addDaysToDate(date: Date, days: number): Date {
        return addDays(date, days);
    }
    
    getDaysDifference(date1: Date, date2: Date): number {
        return differenceInDays(date2, date1);
    }
    
    getStartOfDay(date: Date): Date {
        return startOfDay(date);
    }
    
    getEndOfDay(date: Date): Date {
        return endOfDay(date);
    }
}

// 使用
const helper = new DateTimeHelper();
const now = new Date();
const formatted = helper.formatDate(now);
const tomorrow = helper.addDaysToDate(now, 1);
const diff = helper.getDaysDifference(now, tomorrow);
```

## 8. 输出结果说明

日期时间处理的输出结果：

```text
Formatted: 2024-01-15 10:30:00
Tomorrow: 2024-01-16 10:30:00
Difference: 1
```

**逻辑解析**：
- 提供简洁的 API
- 支持多种格式化选项
- 支持日期计算

## 9. 使用场景

### 1. 日期格式化

格式化日期显示：

```ts
// 日期格式化示例
import { format } from 'date-fns';

const formatted = format(new Date(), 'yyyy-MM-dd');
```

### 2. 日期计算

进行日期计算：

```ts
// 日期计算示例
import { addDays, differenceInDays } from 'date-fns';

const future = addDays(new Date(), 30);
const diff = differenceInDays(future, new Date());
```

### 3. 时区处理

处理时区：

```ts
// 时区处理示例
import { DateTime } from 'luxon';

const utc = DateTime.now().toUTC();
const local = DateTime.now().toLocal();
```

## 10. 注意事项与常见错误

- **时区问题**：注意时区处理，避免时区错误
- **性能考虑**：某些操作可能有性能开销
- **格式兼容**：注意日期格式的兼容性
- **不可变性**：某些库返回新对象，不修改原对象
- **库选择**：根据需求选择合适的库

## 11. 常见问题 (FAQ)

**Q: date-fns 和 dayjs 如何选择？**
A: date-fns 函数式、模块化；dayjs 轻量级、API 类似 moment.js。

**Q: 如何处理时区？**
A: 使用 luxon 或 date-fns-tz 处理时区。

**Q: 如何格式化日期？**
A: 使用 `format` 函数，指定格式字符串。

## 12. 最佳实践

- **库选择**：根据需求选择合适的库
- **时区处理**：明确时区处理逻辑
- **格式化**：统一日期格式规范
- **性能优化**：注意性能，合理使用
- **类型安全**：使用 TypeScript 提供类型安全

## 13. 对比分析：日期时间库选择

| 维度             | date-fns                              | dayjs                                 | luxon                                |
|:-----------------|:--------------------------------------|:--------------------------------------|:-------------------------------------|
| **体积**         | 中等（按需导入）                      | 小                                    | 大                                    |
| **功能**         | 功能丰富                              | 基础功能                              | 功能强大（时区支持）                  |
| **API 风格**     | 函数式                                | 链式                                  | 链式                                  |
| **推荐使用**     | ✅ 推荐（现代项目）                    | 轻量级需求                            | 复杂时区处理                          |

## 14. 练习任务

1. **日期时间库实践**：
   - 使用不同的日期时间库
   - 理解各库的特点
   - 实现日期时间处理

2. **格式化实践**：
   - 实现日期格式化
   - 理解格式字符串
   - 处理不同格式

3. **实际应用**：
   - 在实际项目中应用日期时间库
   - 实现日期计算功能
   - 处理时区问题

完成以上练习后，继续学习下一节：验证库。

## 总结

日期时间库是处理日期时间的重要工具：

- **核心功能**：格式化、解析、计算、时区处理
- **主流库**：date-fns、dayjs、luxon
- **最佳实践**：库选择、时区处理、格式化规范

掌握日期时间库有助于处理日期时间相关需求。

---

**最后更新**：2025-01-XX
