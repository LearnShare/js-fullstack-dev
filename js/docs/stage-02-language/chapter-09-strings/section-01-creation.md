# 2.9.1 字符串创建与模板字符�?

## 概述

字符串（String）是 JavaScript 的原始类型之一，用于表示文本数据。掌握创建方式、模板字符串、转义、编码（UTF-16）、长度与迭代、特殊字符（emoji、代理对）、以及标签模板等高级特性，有助于正确处理多语言、格式化输出和安全拼接�?

## 字符串的本质与编�?

- JS 字符串基�?UTF-16 编码，每个“代码单元”占 2 字节�?
- `length` 统计的是代码单元数量，不一定等于实际“字符”数（对代理�?emoji 会大�?1）�?
- 常见长度差异�?
```js
const s = '😊';        // 单个 emoji
console.log(s.length); // 2（占两个代码单元�?
```
- 处理 Unicode 补充平面字符时，需使用 `codePointAt` / `fromCodePoint` 或使用展开/迭代器�?

## 字符串创建方�?

### 字符串字面量

```js
const single = 'Hello';
const double = "World";

// 转义
const escaped1 = "He said \"Hello\"";
const escaped2 = 'It\'s a string';
const newline = 'Line1\nLine2';
const tab = 'Column1\tColumn2';
```

### 模板字符串（反引号）

```js
const name = 'John';
const message = `Hello, ${name}!`;
const expr = `1 + 2 = ${1 + 2}`; // 1 + 2 = 3
```

特性：
- 支持嵌入表达�?`${...}`
- 原生支持多行，无需 `\n`
- 保留缩进需注意：反引号中的空格/换行会成为内�?

### String 构造函�?

```js
const objStr = new String('Hello');
console.log(typeof objStr); // "object"（包装对象，不推荐）
```

不推荐使�?`new String()`，它返回对象而非原始值，在比�?类型判断时易混淆�?

### 从数�?编码创建

```js
// 代码点转字符�?
const snowman = String.fromCodePoint(0x2603);
// 代码单元�?6 位）转字符串
const char = String.fromCharCode(0x4F60); // '�?
```

### 强制转换为字符串

```js
String(123);          // "123"
(123).toString();     // "123"
`${123}`;             // "123"
```

注意：`null`/`undefined` 调用 `toString` 会抛错，使用 `String()` 或模板字符串更安全�?

## 模板字符串进�?

### 表达式与内联运算

```js
const a = 10, b = 20;
const result = `Sum: ${a + b}`; // Sum: 30
```

### 多行与格�?

```js
const multiLine = `
Line 1
Line 2
Line 3
`.trim(); // 去掉首尾换行
```

### 标签模板（Tagged Template�?

标签函数可对模板进行自定义解析（防止 XSS、国际化、格式化）�?

```js
function safe(strings, ...values) {
  return strings.reduce((acc, str, i) => {
    const v = values[i] === undefined ? '' : String(values[i]).replace(/</g, '&lt;');
    return acc + str + v;
  }, '');
}

const userInput = '<script>alert(1)</script>';
const output = safe`Hello, ${userInput}!`;
console.log(output); // Hello, &lt;script>alert(1)&lt;/script>!
```

应用：XSS 防护、国际化格式化、样式构造（�?styled-components）�?

## 转义与特殊字�?

常用转义�?
- `\n` 换行
- `\t` 制表
- `\\` 反斜�?
- `\'`、`\"` 引号
- `\uXXXX` 16 位码元；`\u{1F60A}` 码点（ES2015�?

示例�?
```js
const smile = '\u{1F60A}'; // 😊
```

## 字符串长度与迭代

### 代码单元 vs 码点

```js
const s = '😊';
console.log(s.length);           // 2
console.log([...s].length);      // 1（按码点迭代�?
console.log(s.codePointAt(0));   // 128522
```

### 安全截取与遍�?

```js
// 按码点安全截取前 N 个字�?
function take(str, n) {
  return [...str].slice(0, n).join('');
}

take('A😊B', 2); // 'A😊'
```

## 不变性与拷贝

- 字符串是不可变的：`str[0] = 'x'` 无效�?
- 修改需创建新字符串：`str = str + 'x'`�?

## 大小写与本地�?

本地化敏感操作使�?`toLocaleUpperCase`/`toLocaleLowerCase`�?
```js
'istanbul'.toLocaleUpperCase('tr'); // 处理土耳其�?i
```

## 常见陷阱

- 误用 `new String()` 导致类型�?object，`===` 比较�?false�?
- `length` �?emoji/代理对不等于实际字符数�?
- 模板字符串内无意的换�?空格导致格式问题�?
- 拼接用户输入时未做转义，可能引入 XSS（需标签模板或手动转义）�?

## 最佳实�?

1) 使用字面量或模板字符串，避免 `new String()`�? 
2) 处理多语言/emoji 时，用展开运算符或 `codePointAt/fromCodePoint` 处理码点�? 
3) 需要格式化/转义场景使用标签模板封装（安全输出、i18n）�? 
4) 避免在模板字符串里出现不必要缩进/换行，必要时使用 `.trim()`�? 
5) 将与字符串相关的常量集中管理，避免魔法字符串�? 

## 练习

1. 写一个标签模板函�?`escapeHTML`，对插值做 HTML 转义�? 
2. 统计包含 emoji 的字符串真实字符数（按码点），并安全截取�?N 个字符�? 
3. 使用模板字符串生成多�?Markdown 片段，去除多余缩进�? 
4. 演示 `new String()` 与字面量�?`typeof`、`===` 的差异�? 
5. 编写一个安全的 `format` 函数，支持占�?`${}` 与默认值�? 

## 总结

- 字符串基�?UTF-16，长度为代码单元数，处理补充平面字符需注意码点�? 
- 模板字符串支持插值、多行、标签模板，适用于格式化与安全输出�? 
- 字符串不可变，修改需创建新值；避免使用包装对象�? 

继续学习下一节，了解字符串常用方法�?
