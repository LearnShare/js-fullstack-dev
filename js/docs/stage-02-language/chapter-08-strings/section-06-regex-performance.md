# 2.8.6 正则表达式性能优化

## 概述

本节介绍正则表达式的性能优化技巧，包括避免回溯灾难、优化匹配策略、使用合适的标志位、预编译正则表达式等性能优化方法。

## 回溯问题

### 什么是回溯

回溯是正则表达式引擎在匹配失败时，回到之前的状态尝试其他可能的匹配路径：

```js
// 简单的回溯示例
const re = /ab*c/;
const str = 'abc';
// 匹配过程：
// 1. 匹配 'a' ✓
// 2. 尝试匹配 'b*'（贪婪），匹配 'b' ✓
// 3. 尝试匹配 'c'，但当前是 'c'，匹配成功 ✓
```

### 灾难性回溯

当正则表达式中包含嵌套的量词或可选分支时，可能导致指数级的回溯：

```js
// 灾难性回溯示例
const badRe = /^(a+)+$/;
const str = 'aaaaaaaaaaaaaaaaaaaaa!'; // 21个 a 加一个 !
// 这个正则会导致大量回溯，性能极差
```

### 避免嵌套量词

```js
// 错误：嵌套量词
const badRe = /^(a+)+$/;

// 正确：简化量词
const goodRe = /^a+$/;
```

### 使用原子组

```js
// 使用原子组减少回溯
const re = /(?>a+)b/;
// 原子组一旦匹配就不会回溯
```

## 量词优化

### 贪婪 vs 惰性

```js
// 贪婪量词（默认）
const greedyRe = /<.*>/;
const str = '<div>Hello</div><span>World</span>';
console.log(str.match(greedyRe)[0]); // "<div>Hello</div><span>World</span>"

// 惰性量词（添加 ?）
const lazyRe = /<.*?>/;
console.log(str.match(lazyRe)[0]); // "<div>"
```

### 使用具体的量词范围

```js
// 错误：无限量词可能导致大量回溯
const badRe = /\d+-\d+/;

// 正确：使用具体范围
const goodRe = /\d{1,10}-\d{1,10}/;
```

## 字符类优化

### 使用具体字符类

```js
// 错误：使用 . 匹配所有字符
const badRe = /a.b/;

// 正确：使用具体的字符类
const goodRe = /a[\w\s]b/;
```

### 字符类顺序

```js
// 优化：将最可能匹配的字符放在前面
const re = /[aeiou]/; // 如果知道元音字母更常见
```

## 锚点优化

### 使用开始锚点

```js
// 错误：没有锚点，需要在整个字符串中搜索
const badRe = /\d{4}-\d{2}-\d{2}/;

// 正确：使用开始锚点，只从开头匹配
const goodRe = /^\d{4}-\d{2}-\d{2}/;
```

### 使用单词边界

```js
// 使用单词边界提高匹配精度
const re = /\bword\b/;
// 只匹配完整的单词，不会匹配 "sword" 中的 "word"
```

## 预编译正则表达式

### 全局变量存储

```js
// 错误：每次都创建新的正则表达式
function validateEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

// 正确：预编译正则表达式
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
function validateEmail(email) {
    return EMAIL_RE.test(email);
}
```

### 在循环中复用

```js
// 错误：在循环中创建正则
const emails = ['user1@example.com', 'user2@example.com', 'user3@example.com'];
emails.forEach(email => {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    console.log(re.test(email));
});

// 正确：在循环外创建
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
emails.forEach(email => {
    console.log(EMAIL_RE.test(email));
});
```

## 标志位选择

### g 标志的使用

```js
// 只匹配一次时，不要使用 g 标志
const re1 = /\d+/; // 更高效
const re2 = /\d+/g; // 如果需要多次匹配，使用 g

// 多次匹配
const str = '123 456 789';
const matches1 = str.match(/\d+/); // ["123"]
const matches2 = str.match(/\d+/g); // ["123", "456", "789"]
```

### u 标志的必要性

```js
// 处理 Unicode 时使用 u 标志
const unicodeRe = /\p{Letter}/u; // 正确
const asciiRe = /[a-zA-Z]/; // 如果只需要 ASCII 字符，不需要 u
```

## 避免不必要的捕获

### 使用非捕获组

```js
// 错误：不必要的捕获
const badRe = /(\w+)\s+(\w+)/;
// 如果只需要匹配，不需要捕获

// 正确：使用非捕获组
const goodRe = /(?:\w+)\s+(?:\w+)/;
```

### 只捕获需要的部分

```js
// 只捕获需要的部分
const re = /(?<year>\d{4})-(?:\d{2})-(?:\d{2})/;
// 只捕获年份，不捕获月份和日期
```

## 使用合适的 API

### test vs match

```js
// 只需要检查是否存在，使用 test（更快）
const re = /\d+/;
if (re.test(str)) {
    // 存在数字
}

// 需要获取匹配结果，使用 match
const match = str.match(re);
```

### exec vs match

```js
// 全局匹配时，exec 可以控制 lastIndex
const re = /\d+/g;
let match;
while ((match = re.exec(str)) !== null) {
    console.log(match[0]);
}

// 非全局匹配时，match 更简单
const match2 = str.match(/\d+/);
```

## 性能测试

### 基准测试

```js
// 性能测试示例
function benchmark(re, str, iterations = 10000) {
    const start = performance.now();
    for (let i = 0; i < iterations; i++) {
        re.test(str);
    }
    const end = performance.now();
    return end - start;
}

const re1 = /^[a-z]+$/;
const re2 = /^[a-z]*$/;
const str = 'hello';

console.log('re1:', benchmark(re1, str), 'ms');
console.log('re2:', benchmark(re2, str), 'ms');
```

## 实际优化案例

### 案例 1：邮箱验证优化

```js
// 优化前：复杂的正则
const badEmailRe = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

// 优化后：简化的正则（如果业务允许）
const goodEmailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
// 预编译
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
```

### 案例 2：URL 提取优化

```js
// 优化前：复杂的命名捕获组
const badUrlRe = /^(?<protocol>https?):\/\/(?<domain>[\w.-]+)(?<path>\/[^\s]*)?/;

// 优化后：根据需要简化
const goodUrlRe = /https?:\/\/[\w.-]+(?:\/[^\s]*)?/;
// 如果需要各部分，可以后续解析
```

## 注意事项

1. **过早优化**：不要过早优化，先确保功能正确
2. **可读性优先**：性能优化不应牺牲代码可读性
3. **实际测试**：在真实数据上测试性能，不要假设
4. **权衡考虑**：在性能和可维护性之间找到平衡
5. **浏览器差异**：不同浏览器的正则引擎可能有性能差异

## 常见错误

### 错误 1：忽略回溯问题

```js
// 错误：可能导致灾难性回溯
const badRe = /^(a+)+$/;

// 正确：简化或限制
const goodRe = /^a+$/;
// 或
const goodRe2 = /^(a{1,100})+$/;
```

### 错误 2：在循环中创建正则

```js
// 错误：每次循环都创建新正则
for (let i = 0; i < 1000; i++) {
    const re = /\d+/;
    re.test(str);
}

// 正确：在循环外创建
const re = /\d+/;
for (let i = 0; i < 1000; i++) {
    re.test(str);
}
```

### 错误 3：过度复杂的正则

```js
// 错误：过于复杂，难以维护和优化
const badRe = /^(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$/;

// 正确：考虑拆分为多个简单验证
function isValidIP(ip) {
    const parts = ip.split('.');
    if (parts.length !== 4) return false;
    return parts.every(part => {
        const num = parseInt(part, 10);
        return num >= 0 && num <= 255;
    });
}
```

## 最佳实践

1. **预编译正则**：对于频繁使用的正则，预编译并复用
2. **避免回溯灾难**：避免嵌套量词，使用具体范围
3. **使用锚点**：使用 `^` 和 `$` 限制匹配范围
4. **选择合适 API**：根据需求选择 test、match、exec
5. **简化正则**：复杂验证可以考虑拆分为多个简单验证
6. **性能测试**：在真实场景中测试性能，不要假设

## 练习

1. **性能对比**：编写两个正则表达式验证邮箱，一个复杂一个简单，使用性能测试对比两者的差异。

2. **优化回溯**：识别并优化一个存在回溯问题的正则表达式。

3. **预编译实践**：编写一个函数，使用预编译的正则表达式验证多个邮箱地址。

4. **API 选择**：对比 test、match、exec 在不同场景下的性能差异。

5. **综合优化**：优化一个复杂的正则表达式，考虑性能、可读性和可维护性。

完成以上练习后，继续学习下一章：Set 与 Map。

## 总结

正则表达式性能优化包括避免回溯灾难、使用合适的量词、预编译正则表达式、选择正确的 API 等。在实际开发中，应该平衡性能、可读性和可维护性，根据实际需求进行优化。

## 相关资源

- [MDN：正则表达式性能](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions#performance)
- [正则表达式回溯灾难](https://www.regular-expressions.info/catastrophic.html)
- [JavaScript 正则表达式性能优化](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions#advanced_searching_with_flags)
