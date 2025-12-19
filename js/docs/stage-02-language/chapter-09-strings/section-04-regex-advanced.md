# 2.9.4 正则表达式高级用�?
## 概述

本节介绍正则表达式的高级特性，包括命名捕获组、后向断言、Unicode 属性转义、正则表达式与字符串方法的组合使用等高级技巧�?
## 命名捕获�?
### 基本语法

ES2018 引入了命名捕获组，可以给捕获组命名，使代码更易读�?
**语法格式**：`(?<name>pattern)`

```js
// 普通捕获组
const re1 = /(\d{4})-(\d{2})-(\d{2})/;
const match1 = '2025-12-17'.match(re1);
console.log(match1[1]); // "2025"（不易读�?
// 命名捕获�?const re2 = /(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})/;
const match2 = '2025-12-17'.match(re2);
console.log(match2.groups.year);  // "2025"
console.log(match2.groups.month); // "12"
console.log(match2.groups.day);   // "17"
```

### �?replace 中使�?
```js
const re = /(?<firstName>\w+) (?<lastName>\w+)/;
const str = 'John Doe';
const result = str.replace(re, '$<lastName>, $<firstName>');
console.log(result); // "Doe, John"
```

### �?exec 中使�?
```js
const re = /(?<protocol>https?):\/\/(?<domain>[\w.-]+)/g;
const str = 'Visit https://example.com and http://test.org';
let match;

while ((match = re.exec(str)) !== null) {
    console.log(match.groups.protocol); // "https", "http"
    console.log(match.groups.domain);   // "example.com", "test.org"
}
```

## 后向断言（Lookbehind Assertions�?
### 后向肯定断言

**语法格式**：`(?<=pattern)`

匹配后面跟着指定模式的位置：

```js
// 匹配价格，但只返回数字部�?const re = /(?<=\$)\d+\.\d{2}/;
const match = '$99.99'.match(re);
console.log(match[0]); // "99.99"
```

### 后向否定断言

**语法格式**：`(?<!pattern)`

匹配后面不跟着指定模式的位置：

```js
// 匹配不是美元符号开头的价格
const re = /(?<!\$)\d+\.\d{2}/;
const str = 'Price: $99.99 or 88.88';
const match = str.match(re);
console.log(match[0]); // "88.88"
```

### 前向断言回顾

```js
// 前向肯定断言 (?=pattern)
const re1 = /\d+(?=px)/;
console.log('100px'.match(re1)[0]); // "100"

// 前向否定断言 (?!pattern)
const re2 = /\d+(?!px)/;
console.log('100em'.match(re2)[0]); // "100"
```

## Unicode 属性转�?
### 基本概念

使用 `\p{...}` 匹配 Unicode 属性，需�?`u` 标志�?
```js
// 匹配所有字母（包括中文、日文等�?const re = /\p{Letter}+/gu;
const str = 'Hello 世界 こんにち�?;
console.log(str.match(re)); // ["Hello", "世界", "こんにち�?]
```

### 常用 Unicode 属�?
```js
// 字母
/\p{Letter}/u

// 数字
/\p{Number}/u

// 标点符号
/\p{Punctuation}/u

// 符号
/\p{Symbol}/u

// 空白字符
/\p{Whitespace}/u

// Emoji
/\p{Emoji}/u

// 脚本（Script�?/\p{Script=Latin}/u  // 拉丁字母
/\p{Script=Han}/u    // 汉字
/\p{Script=Hiragana}/u  // 平假�?```

### 实际应用

```js
// 提取所�?emoji
const re = /\p{Emoji}/gu;
const str = 'I love JavaScript! 🎉🚀';
console.log(str.match(re)); // ["🎉", "🚀"]

// 匹配中文
const chineseRe = /\p{Script=Han}+/gu;
const str2 = 'Hello 世界 こんにち�?;
console.log(str2.match(chineseRe)); // ["世界"]
```

## 非捕获组与原子组

### 非捕获组

**语法格式**：`(?:pattern)`

匹配但不捕获，用于分组但不保存结果：

```js
// 捕获�?const re1 = /(\d{4})-(?:jan|feb|mar)/i;
const match1 = '2025-JAN'.match(re1);
console.log(match1[1]); // "2025"
console.log(match1[2]); // undefined（月份未捕获�?
// 与捕获组对比
const re2 = /(\d{4})-(jan|feb|mar)/i;
const match2 = '2025-JAN'.match(re2);
console.log(match2[1]); // "2025"
console.log(match2[2]); // "JAN"
```

### 原子组（Atomic Groups�?
**语法格式**：`(?>pattern)`

原子组匹配后不会回溯，可以提高性能�?
```js
// 普通分组（可能回溯�?const re1 = /(a+)b/;
console.log(re1.test('aaaaac')); // false（会回溯�?
// 原子组（不回溯）
const re2 = /(?>a+)b/;
console.log(re2.test('aaaaac')); // false（更快，因为不回溯）
```

## 条件表达�?
### 基本语法

**语法格式**：`(?(condition)true-pattern|false-pattern)`

根据条件选择不同的模式：

```js
// 如果前面是数字，匹配字母；否则匹配数�?const re = /(\d)?(?(1)[a-z]+|\d+)/;
console.log(re.test('123abc')); // true
console.log(re.test('abc123')); // true
```

## 反向引用

### 基本用法

使用 `\n` 引用前面捕获组的内容�?
```js
// 匹配重复的单�?const re = /\b(\w+)\s+\1\b/;
console.log(re.test('the the')); // true
console.log(re.test('the cat')); // false

// 匹配 HTML 标签
const tagRe = /<(\w+)>.*?<\/\1>/;
console.log(tagRe.test('<div>content</div>')); // true
console.log(tagRe.test('<div>content</span>')); // false
```

### 命名反向引用

**语法格式**：`\k<name>`

```js
// 使用命名捕获组的反向引用
const re = /(?<word>\w+)\s+\k<word>/;
console.log(re.test('hello hello')); // true
```

## 粘性匹配（Sticky Matching�?
### y 标志

**语法格式**：`/pattern/y`

�?`lastIndex` 位置开始匹配，必须连续�?
```js
const re = /\d+/y;
re.lastIndex = 5;
console.log(re.test('123 456')); // false（位�?是空格）

re.lastIndex = 4;
console.log(re.test('123 456')); // true（位�?�?�?```

### �?g 标志的区�?
```js
// g 标志：全局搜索，可以跳过不匹配的字�?const reG = /\d+/g;
const str = 'a1b2c3';
console.log(str.match(reG)); // ["1", "2", "3"]

// y 标志：必须从 lastIndex 开始连续匹�?const reY = /\d+/y;
reY.lastIndex = 1;
console.log(reY.exec(str)); // ["1"]
reY.lastIndex = 2;
console.log(reY.exec(str)); // null（位�?�?b'，不匹配�?```

## dotAll 模式

### s 标志

**语法格式**：`/pattern/s`

允许 `.` 匹配换行符：

```js
// 默认�? 不匹配换行符
const re1 = /a.b/;
console.log(re1.test('a\nb')); // false

// s 标志�? 匹配换行�?const re2 = /a.b/s;
console.log(re2.test('a\nb')); // true
```

## 正则表达式与字符串方法组�?
### 链式处理

```js
// 提取并清理数�?const text = 'Prices: $99.99, $199.99, $299.99';
const prices = text
    .match(/\$\d+\.\d{2}/g)           // 提取价格
    .map(price => price.replace('$', '')) // 移除 $ 符号
    .map(Number);                      // 转换为数�?console.log(prices); // [99.99, 199.99, 299.99]
```

### 复杂替换

```js
// 使用函数进行复杂替换
const text = 'Hello World';
const result = text.replace(/(\w+)\s+(\w+)/, (match, p1, p2) => {
    return `${p2}, ${p1}`;
});
console.log(result); // "World, Hello"
```

## 注意事项

1. **命名捕获组兼容�?*：ES2018+，较旧的浏览器可能不支持
2. **后向断言兼容�?*：ES2018+，需要较新的 JavaScript 引擎
3. **Unicode 属性转�?*：必须使�?`u` 标志，ES2018+
4. **性能考虑**：复杂正则可能影响性能，需要优�?5. **可读�?*：命名捕获组可以提高代码可读�?
## 常见错误

### 错误 1：忘�?u 标志

```js
// 错误：Unicode 属性转义需�?u 标志
const re1 = /\p{Letter}/;
console.log(re1.test('a')); // SyntaxError

// 正确
const re2 = /\p{Letter}/u;
console.log(re2.test('a')); // true
```

### 错误 2：后向断言中的量词限制

```js
// 错误：后向断言中不能使用无限量�?const re1 = /(?<=a*)/; // SyntaxError

// 正确：使用固定长度或有限量词
const re2 = /(?<=a{0,3})/; // 可以
```

### 错误 3：命名捕获组访问错误

```js
const re = /(?<name>\w+)/;
const match = 'John'.match(re);

// 错误：使用数组索引访问命名组
console.log(match.groups); // { name: 'John' }

// 正确：使�?groups 属�?console.log(match.groups.name); // "John"
```

## 最佳实�?
1. **使用命名捕获�?*：提高代码可读性，特别是复杂正�?2. **合理使用断言**：避免复杂的断言嵌套，保持可读�?3. **Unicode 属性转�?*：处理多语言文本时使用，记住�?`u` 标志
4. **性能优化**：对于性能敏感的场景，使用原子组减少回�?5. **注释说明**：复杂正则添加注释，说明各部分的作用

## 练习

1. **命名捕获组练�?*：编写正则表达式提取邮箱地址，使用命名捕获组分别提取用户名和域名�?
2. **后向断言练习**：编写正则表达式匹配价格（如 "$99.99"），但只返回数字部分，使用后向断言�?
3. **Unicode 属性练�?*：编写正则表达式统计文本�?emoji 的数量�?
4. **反向引用练习**：编写正则表达式检测字符串中是否有重复的单词（�?"the the"）�?
5. **综合练习**：编写正则表达式验证并提�?URL，使用命名捕获组分别提取协议、域名和路径�?
完成以上练习后，继续学习下一节，了解常见正则模式�?
## 总结

正则表达式的高级特性包括命名捕获组、后向断言、Unicode 属性转义等，这些特性可以让我们编写更强大、更易读的正则表达式。掌握这些高级特性，能够处理更复杂的文本匹配和提取需求�?
## 相关资源

- [MDN：正则表达式](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions)
- [MDN：命名捕获组](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions/Groups_and_Backreferences#named_capturing_groups)
