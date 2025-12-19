# 3.7.4 数据处理

## 1. 概述

数据处理是 Node.js 的另一个重要应用领域。Node.js 的流式处理和异步特性使其适合处理大量数据。无论是 CSV 解析、JSON 处理、数据转换还是数据分析，Node.js 都有相应的工具和库支持。

## 2. 特性说明

- **流式处理**：支持大文件的流式处理，避免内存溢出。
- **数据转换**：支持各种数据格式的转换。
- **数据验证**：支持数据验证和清洗。
- **批量处理**：支持批量数据处理。
- **性能优化**：支持并发处理和性能优化。

## 3. 主流工具概览

### csv-parse / csv-stringify

CSV 文件解析和生成。

**特点**：
- 流式处理支持
- 灵活的配置选项
- 高性能
- TypeScript 支持

**安装**：
```bash
npm install csv-parse csv-stringify
```

**基本用法**：
```ts
// 文件: data-csv.ts
// 功能: CSV 处理基本用法

import { parse } from 'csv-parse/sync';
import { stringify } from 'csv-stringify/sync';
import fsPromises from 'node:fs/promises';

// 读取 CSV
async function readCSV(filePath: string) {
    const content = await fsPromises.readFile(filePath, 'utf8');
    const records = parse(content, {
        columns: true,
        skip_empty_lines: true
    });
    return records;
}

// 写入 CSV
async function writeCSV(data: any[], filePath: string) {
    const content = stringify(data, {
        header: true
    });
    await fsPromises.writeFile(filePath, content, 'utf8');
}
```

### xlsx

Excel 文件处理。

**特点**：
- 支持读取和写入 Excel
- 支持多种格式
- 流式处理支持
- 跨平台

**安装**：
```bash
npm install xlsx
```

**基本用法**：
```ts
// 文件: data-excel.ts
// 功能: Excel 处理基本用法

import * as XLSX from 'xlsx';
import fsPromises from 'node:fs/promises';

// 读取 Excel
async function readExcel(filePath: string) {
    const buffer = await fsPromises.readFile(filePath);
    const workbook = XLSX.read(buffer, { type: 'buffer' });
    const sheetName = workbook.SheetNames[0];
    const worksheet = workbook.Sheets[sheetName];
    const data = XLSX.utils.sheet_to_json(worksheet);
    return data;
}

// 写入 Excel
async function writeExcel(data: any[], filePath: string) {
    const worksheet = XLSX.utils.json_to_sheet(data);
    const workbook = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(workbook, worksheet, 'Sheet1');
    const buffer = XLSX.write(workbook, { type: 'buffer', bookType: 'xlsx' });
    await fsPromises.writeFile(filePath, buffer);
}
```

### lodash

数据操作工具库。

**特点**：
- 丰富的工具函数
- 函数式编程支持
- 高性能
- 链式调用

**安装**：
```bash
npm install lodash
npm install @types/lodash -D
```

**基本用法**：
```ts
// 文件: data-lodash.ts
// 功能: Lodash 基本用法

import _ from 'lodash';

// 数组操作
const numbers = [1, 2, 3, 4, 5];
const doubled = _.map(numbers, n => n * 2);
const filtered = _.filter(numbers, n => n > 2);
const grouped = _.groupBy([{ age: 20 }, { age: 30 }], 'age');

// 对象操作
const obj = { a: 1, b: 2, c: 3 };
const picked = _.pick(obj, ['a', 'b']);
const omitted = _.omit(obj, ['c']);

// 数据转换
const data = [{ name: 'Alice', age: 25 }, { name: 'Bob', age: 30 }];
const names = _.map(data, 'name');
const ages = _.map(data, 'age');
```

### Papa Parse

强大的 CSV 解析库。

**特点**：
- 流式处理
- 自动类型检测
- 错误处理
- 浏览器和 Node.js 支持

**安装**：
```bash
npm install papaparse
```

**基本用法**：
```ts
// 文件: data-papaparse.ts
// 功能: Papa Parse 基本用法

import Papa from 'papaparse';
import fsPromises from 'node:fs/promises';

async function parseCSV(filePath: string) {
    const content = await fsPromises.readFile(filePath, 'utf8');
    
    return new Promise((resolve, reject) => {
        Papa.parse(content, {
            header: true,
            skipEmptyLines: true,
            complete: (results) => {
                resolve(results.data);
            },
            error: (error) => {
                reject(error);
            }
        });
    });
}
```

## 4. 代码示例：完整数据处理流程

以下示例演示了如何构建一个完整的数据处理流程：

```ts
// 文件: complete-data-processing.ts
// 功能: 完整的数据处理示例

import { parse } from 'csv-parse/sync';
import { stringify } from 'csv-stringify/sync';
import fsPromises from 'node:fs/promises';
import _ from 'lodash';

interface User {
    name: string;
    age: number;
    email: string;
}

async function processData(inputPath: string, outputPath: string) {
    // 1. 读取 CSV
    const content = await fsPromises.readFile(inputPath, 'utf8');
    const records = parse(content, {
        columns: true,
        skip_empty_lines: true
    }) as User[];
    
    // 2. 数据清洗
    const cleaned = records.filter(user => 
        user.name && user.email && user.age > 0
    );
    
    // 3. 数据转换
    const transformed = cleaned.map(user => ({
        ...user,
        age: parseInt(user.age.toString()),
        email: user.email.toLowerCase()
    }));
    
    // 4. 数据分组
    const grouped = _.groupBy(transformed, user => {
        if (user.age < 30) return 'young';
        if (user.age < 50) return 'middle';
        return 'senior';
    });
    
    // 5. 数据统计
    const stats = {
        total: transformed.length,
        byAge: _.mapValues(grouped, group => group.length),
        averageAge: _.meanBy(transformed, 'age')
    };
    
    // 6. 保存结果
    const output = stringify(transformed, { header: true });
    await fsPromises.writeFile(outputPath, output, 'utf8');
    
    // 7. 保存统计
    await fsPromises.writeFile(
        outputPath.replace('.csv', '-stats.json'),
        JSON.stringify(stats, null, 2),
        'utf8'
    );
    
    return stats;
}
```

## 5. 参数说明：数据处理常用参数

| 参数类型     | 说明                                     | 示例                           |
|:-------------|:-----------------------------------------|:-------------------------------|
| **文件路径** | 输入和输出文件路径                        | `'./data.csv'`                 |
| **解析选项** | CSV/Excel 解析配置选项                    | `{ columns: true }`            |
| **转换函数** | 数据转换函数                              | `(item) => transformed`        |
| **过滤条件** | 数据过滤条件                              | `item => item.age > 18`        |

## 6. 返回值与状态说明

数据处理的返回结果：

| 返回类型     | 说明                                     |
|:-------------|:-----------------------------------------|
| **数据数组** | 处理后的数据数组                          |
| **统计信息** | 数据统计信息                              |
| **错误信息** | 处理失败时的错误信息                      |

## 7. 输出结果说明

数据处理的输出示例：

```text
Processed 1000 records
Filtered 50 invalid records
Saved to output.csv
Statistics saved to output-stats.json
```

**逻辑解析**：
- 读取原始数据
- 清洗和转换数据
- 进行数据分析和统计
- 保存处理结果

## 8. 使用场景

### 1. 数据导入导出

处理数据导入导出：

```ts
// 数据导入导出示例
async function importData(filePath: string) {
    const data = await readCSV(filePath);
    await saveToDatabase(data);
}

async function exportData(query: string, filePath: string) {
    const data = await queryDatabase(query);
    await writeCSV(data, filePath);
}
```

### 2. 数据清洗

清洗和验证数据：

```ts
// 数据清洗示例
function cleanData(data: any[]) {
    return data
        .filter(item => item && item.id)
        .map(item => ({
            ...item,
            name: item.name.trim(),
            email: item.email.toLowerCase()
        }));
}
```

### 3. 数据分析

进行数据分析：

```ts
// 数据分析示例
function analyzeData(data: any[]) {
    return {
        count: data.length,
        average: _.meanBy(data, 'value'),
        max: _.maxBy(data, 'value'),
        min: _.minBy(data, 'value'),
        grouped: _.groupBy(data, 'category')
    };
}
```

## 9. 注意事项与常见错误

- **内存管理**：处理大文件时使用流式处理
- **数据验证**：验证数据格式和内容
- **错误处理**：处理文件读取和解析错误
- **性能优化**：使用并发处理提高性能
- **数据安全**：注意敏感数据的处理

## 10. 常见问题 (FAQ)

**Q: 如何处理大文件？**
A: 使用流式处理，避免一次性加载整个文件到内存。

**Q: 如何提高处理速度？**
A: 使用并发处理、优化算法、使用更快的库（如 fast-csv）。

**Q: 如何处理不同编码的文件？**
A: 使用 `iconv-lite` 等库进行编码转换。

## 11. 最佳实践

- **流式处理**：处理大文件时使用流式处理
- **数据验证**：验证数据格式和内容
- **错误处理**：完善的错误处理和日志记录
- **性能优化**：使用并发处理和优化算法
- **代码复用**：封装通用的数据处理函数

## 12. 对比分析：数据处理工具选择

| 工具           | 特点                                     | 适用场景                       |
|:---------------|:-----------------------------------------|:-------------------------------|
| **csv-parse**  | 流式处理，高性能                         | CSV 文件处理                   |
| **xlsx**       | Excel 文件支持                            | Excel 文件处理                 |
| **lodash**     | 丰富的工具函数                           | 数据操作和转换                 |
| **Papa Parse** | 强大的 CSV 解析                          | 复杂 CSV 处理                  |

## 13. 练习任务

1. **CSV 处理实践**：
   - 读取和解析 CSV 文件
   - 清洗和转换数据
   - 保存处理结果

2. **Excel 处理实践**：
   - 读取和写入 Excel 文件
   - 处理多个工作表
   - 实现数据转换

3. **数据分析实践**：
   - 使用 Lodash 进行数据分析
   - 实现数据统计功能
   - 生成数据报告

4. **实际应用**：
   - 创建实际的数据处理工具
   - 实现完整的数据处理流程
   - 优化处理性能

完成以上练习后，继续学习下一阶段：Web 框架与 API 开发。

## 总结

数据处理是 Node.js 的重要应用领域：

- **主流工具**：csv-parse、xlsx、lodash、Papa Parse
- **核心功能**：数据读取、清洗、转换、分析
- **最佳实践**：流式处理、数据验证、错误处理、性能优化

掌握数据处理有助于进行数据分析和数据管理。

---

**最后更新**：2025-01-XX
