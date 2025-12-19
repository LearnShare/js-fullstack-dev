# 2.9.2 字符串方�?

## 概述

本节系统梳理字符串常用方法，涵盖查找、替换、截取、分割、填充、大小写、比较、匹配、重复、补全、对齐，以及处理 Unicode 补充字符的安全用法。重点关注：方法语法、参数、返回值、示例与输出、常见陷阱和最佳实践�?

## 查找与匹�?

### indexOf()

**语法格式**：`str.indexOf(searchValue[, fromIndex])`

**参数说明**�?

| 参数�?        | 类型   | 说明                           | 是否必需 | 默认�?|
|:---------------|:-------|:-------------------------------|:---------|:-------|
| `searchValue`  | string | 要查找的子字符串               | �?      | -      |
| `fromIndex`    | number | 开始查找的索引位置             | �?      | 0      |

**返回�?*：数字，第一个匹配的索引，未找到返回 -1

```js
const str = 'Hello, World!';
console.log(str.indexOf('World'));      // 7
console.log(str.lastIndexOf('o'));      // 8
console.log(str.indexOf('xyz'));        // -1
console.log(str.indexOf('o', 5));       // 8（从索引 5 开始找�?
```

**输出说明**：`indexOf()` 从前往后查找，`lastIndexOf()` 从后往前查找�?

### lastIndexOf()

**语法格式**：`str.lastIndexOf(searchValue[, fromIndex])`

**参数说明**：与 `indexOf()` 相同

**返回�?*：数字，最后一个匹配的索引，未找到返回 -1

### includes()

**语法格式**：`str.includes(searchString[, position])`

**参数说明**�?

| 参数�?        | 类型   | 说明                           | 是否必需 | 默认�?|
|:---------------|:-------|:-------------------------------|:---------|:-------|
| `searchString` | string | 要查找的子字符串               | �?      | -      |
| `position`     | number | 开始查找的索引位置             | �?      | 0      |

**返回�?*：布尔值，找到返回 `true`，否则返�?`false`

```js
const s = 'Hello, World!';
console.log(s.includes('World'));       // true
console.log(s.includes('xyz'));         // false
```

### startsWith()

**语法格式**：`str.startsWith(searchString[, position])`

**参数说明**�?

| 参数�?        | 类型   | 说明                           | 是否必需 | 默认�?|
|:---------------|:-------|:-------------------------------|:---------|:-------|
| `searchString` | string | 要查找的前缀字符�?            | �?      | -      |
| `position`     | number | 开始查找的索引位置             | �?      | 0      |

**返回�?*：布尔值，以指定字符串开头返�?`true`，否则返�?`false`

```js
const s = 'Hello, World!';
console.log(s.startsWith('Hello'));     // true
console.log(s.startsWith('World', 7));  // true（从索引 7 判断前缀�?
```

### endsWith()

**语法格式**：`str.endsWith(searchString[, length])`

**参数说明**�?

| 参数�?        | 类型   | 说明                           | 是否必需 | 默认�?|
|:---------------|:-------|:-------------------------------|:---------|:-------|
| `searchString` | string | 要查找的后缀字符�?            | �?      | -      |
| `length`       | number | 作为字符串长度的位置           | �?      | `str.length` |

**返回�?*：布尔值，以指定字符串结尾返回 `true`，否则返�?`false`

```js
const s = 'Hello, World!';
console.log(s.endsWith('!'));           // true
console.log(s.endsWith('World', 12));   // true（检查前 12 个字符）
```

### search()

**语法格式**：`str.search(regexp)`

**参数说明**�?

| 参数�?  | 类型   | 说明           | 是否必需 | 默认�?|
|:---------|:-------|:---------------|:---------|:-------|
| `regexp` | RegExp | 正则表达�?    | �?      | -      |

**返回�?*：数字，第一个匹配的索引，未匹配返回 -1

```js
'abc123'.search(/\d+/); // 3
```

## 替换

### replace()

**语法格式**：`str.replace(searchValue, replacer)`

**参数说明**�?

| 参数�?       | 类型           | 说明                           | 是否必需 | 默认�?|
|:--------------|:---------------|:-------------------------------|:---------|:-------|
| `searchValue` | string\|RegExp | 要替换的字符串或正则表达�?    | �?      | -      |
| `replacer`    | string\|function | 替换字符串或替换函数         | �?      | -      |

**返回�?*：字符串，替换后的新字符串（不修改原字符串）

**说明**：只替换第一个匹配项（除非使用全局正则�?

```js
const str = 'Hello, World!';
console.log(str.replace('World', 'JS'));          // Hello, JS!

// 使用正则全局替换
const input = 'item-1, item-2';
const out = input.replace(/item-(\d+)/g, (_, n) => `#${Number(n) + 10}`);
console.log(out); // #11, #12
```

**输出说明**：`replace()` 返回新字符串，不修改原字符串�?

### replaceAll()

**语法格式**：`str.replaceAll(searchValue, replacer)`

**参数说明**�?

| 参数�?       | 类型           | 说明                           | 是否必需 | 默认�?|
|:--------------|:---------------|:-------------------------------|:---------|:-------|
| `searchValue` | string\|RegExp | 要替换的字符串或正则表达�?    | �?      | -      |
| `replacer`    | string\|function | 替换字符串或替换函数         | �?      | -      |

**返回�?*：字符串，替换后的新字符串（不修改原字符串）

**说明**：替换所有匹配项

```js
const str = 'Hello, World!';
console.log(str.replaceAll('l', 'L'));            // HeLLo, WorLd!
```

**注意事项**：`replaceAll()` 需�?ES2021+ 支持，旧环境使用 `/.../g` + `replace()`�?

## 截取与分�?

### slice()

**语法格式**：`str.slice([start[, end]])`

**参数说明**�?

| 参数�?  | 类型   | 说明                           | 是否必需 | 默认�?    |
|:---------|:-------|:-------------------------------|:---------|:-----------|
| `start`  | number | 起始索引（包含）               | �?      | 0          |
| `end`    | number | 结束索引（不包含�?            | �?      | `length`   |

**返回�?*：字符串，截取后的新字符串（不修改原字符串）

**说明**：支持负数索引，从末尾开始计�?

```js
const str = 'Hello, World!';
console.log(str.slice(0, 5));      // Hello
console.log(str.slice(-6));        // World!
console.log(str.slice(7, 12));     // World
```

**输出说明**：`slice()` 返回新字符串，支持负数索引�?

### substring()

**语法格式**：`str.substring(indexStart[, indexEnd])`

**参数说明**�?

| 参数�?       | 类型   | 说明                           | 是否必需 | 默认�?    |
|:--------------|:-------|:-------------------------------|:---------|:-----------|
| `indexStart`  | number | 起始索引（包含）               | �?      | -          |
| `indexEnd`    | number | 结束索引（不包含�?            | �?      | `length`   |

**返回�?*：字符串，截取后的新字符串（不修改原字符串）

**说明**：不支持负数，会自动交换 start �?end

```js
const str = 'Hello, World!';
console.log(str.substring(0, 5));  // Hello
console.log(str.substring(5, 0));  // Hello（参数会被交换）
```

**注意事项**：`substring()` 不支持负数索引，参数会自动交换，容易产生困惑。建议优先使�?`slice()`�?

### substr()（已废弃�?

**说明**：`substr()` 方法已废弃，不应使用。使�?`slice()` 替代�?

### split()

**语法格式**：`str.split([separator[, limit]])`

**参数说明**�?

| 参数�?      | 类型           | 说明                           | 是否必需 | 默认�?|
|:-------------|:---------------|:-------------------------------|:---------|:-------|
| `separator`  | string\|RegExp | 分隔�?                        | �?      | -      |
| `limit`      | number         | 限制返回数组的最大长�?        | �?      | -      |

**返回�?*：数组，分割后的字符串数�?

```js
const csv = 'apple,banana,orange';
console.log(csv.split(','));      // ["apple","banana","orange"]
console.log(csv.split(',', 2));   // ["apple","banana"]

// 处理多空格可用正�?
'a  b   c'.split(/\s+/); // ["a","b","c"]
```

**输出说明**：`split()` 返回字符串数组，`limit` 限制返回元素数量�?

## 大小写与本地�?

### toUpperCase / toLowerCase
```js
'Hello'.toUpperCase(); // HELLO
'Hello'.toLowerCase(); // hello
```

### toLocaleUpperCase / toLocaleLowerCase
处理语言特定规则（如土耳其�?i）�?
```js
'istanbul'.toLocaleUpperCase('tr'); // İSTANBUL
```

## 去除空白与填�?

### trim / trimStart / trimEnd
```js
const str = '  Hello  ';
console.log(str.trim());      // "Hello"
console.log(str.trimStart()); // "Hello  "
console.log(str.trimEnd());   // "  Hello"
```

### padStart()

**语法格式**：`str.padStart(targetLength[, padString])`

**参数说明**�?

| 参数�?        | 类型   | 说明                           | 是否必需 | 默认�?|
|:---------------|:-------|:-------------------------------|:---------|:-------|
| `targetLength` | number | 目标长度                       | �?      | -      |
| `padString`    | string | 填充字符�?                    | �?      | ' '    |

**返回�?*：字符串，在开头填充后的新字符�?

**说明**：如果字符串长度小于目标长度，在开头填�?

```js
'5'.padStart(3, '0'); // "005"
'12'.padStart(4, '0'); // "0012"
```

**输出说明**：常用于日期/时间补零、对齐输出�?

### padEnd()

**语法格式**：`str.padEnd(targetLength[, padString])`

**参数说明**：与 `padStart()` 相同

**返回�?*：字符串，在结尾填充后的新字符串

**说明**：如果字符串长度小于目标长度，在结尾填充

```js
'5'.padEnd(3, '0');   // "500"
'12'.padEnd(4, '0');  // "1200"
```

## 重复

### repeat()

**语法格式**：`str.repeat(count)`

**参数说明**�?

| 参数�?  | 类型   | 说明                           | 是否必需 | 默认�?|
|:---------|:-------|:-------------------------------|:---------|:-------|
| `count`  | number | 重复次数（必�?>= 0�?         | �?      | -      |

**返回�?*：字符串，重复指定次数后的新字符�?

```js
'ab'.repeat(3); // "ababab"
'-'.repeat(10);  // "----------"
```

**输出说明**：可用于生成分隔线、占位符�?

## 比较与排�?

### localeCompare

语法：`str.localeCompare(compareString, [locales], [options])`  
适用于本地化排序/比较�?

```js
['ä', 'a', 'z'].sort((a, b) => a.localeCompare(b, 'de')); // ["a","ä","z"]
```

## 访问字符与码�?

### charAt / charCodeAt / codePointAt
```js
const s = '😊';
console.log(s.charAt(0));        // �?(半个字符)
console.log(s.codePointAt(0));   // 128522
```

### 安全迭代（按码点�?
```js
const arr = [...'A😊B']; // ["A","😊","B"]
```
避免 surrogate pair 被拆分�?

## 匹配与提取（简要）

`match` / `matchAll` 与正则相关，本节只列出简单用法，详细见正则章节�?

```js
'a1b2'.match(/\d/g);           // ["1","2"]
[... 'a1b2'.matchAll(/\d/g)];  // 迭代所有匹配（含索引）
```

## 替代/扩展�?

- `String.prototype.replaceAll` 在老环境需 polyfill�?
- 复杂大小�?折叠可用 `Intl.Collator`，多语言格式化可�?`Intl` 系列 API�?

## 常见陷阱

- `substr` 已废弃，避免使用�? 
- `substring` 会交换参数且不支持负数，易产生困惑；优先 `slice`�? 
- 处理 emoji/补充平面字符时，`length`/`charAt`/`slice` 可能拆半字符；用展开或码�?API�? 
- `replace` 默认只替换首个匹配；需要全局请用正则 / `replaceAll`�? 
- `split('')` 会按代码单元拆分，emoji 会被拆成两个字符；用 `[...str]` 更安全�? 

## 最佳实�?

1) 截取/遍历包含 emoji 的字符串时，使用展开（`[...str]`）或 `codePointAt`/`fromCodePoint`�? 
2) 替换多个匹配时优�?`replaceAll` 或带 `/g` 的正则�? 
3) 规范化大小写时，需考虑本地化：�?`toLocaleUpperCase`/`toLocaleLowerCase`�? 
4) 优先 `slice` 处理区间；避�?`substr`，谨慎使�?`substring`�? 
5) 需排序/比较的场景使�?`localeCompare` �?`Intl.Collator`，避免简�?ASCII 比较导致多语言错误�? 

## 练习

1. 写一�?`safeSlice(str, start, end)`，按码点截取，支持负数�? 
2. 使用 `replaceAll` 或正则，将字符串中的 HTML 标签去除，保留文本�? 
3. �?`localeCompare` 对包含重音符的单词进行德语排序�? 
4. 统计字符串中出现次数最多的字符，考虑 emoji 计数�? 
5. �?CSV 行用 `split` 转为数组，并去除多余空格�? 

## 总结

- 查找：`includes`/`indexOf`；替换：`replace`/`replaceAll`；截取：`slice`；分割：`split`�? 
- 大小写、本地化：`toLocaleUpperCase/LowerCase`；比较：`localeCompare`�? 
- 处理 Unicode 时，用码点级操作或展开迭代，避免拆分代理对�? 
- 选择合适方法并注意陷阱，可提升文本处理的正确性与健壮性�? 

继续学习下一节，了解正则表达式的基础与模式匹配�?
