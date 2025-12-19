# 2.9.5 常见正则模式

## 概述

本节介绍实际开发中常用的正则表达式模式，包括邮箱验证、URL 提取、日期匹配、手机号验证等常见场景的正则表达式�?
## 邮箱验证

### 基础邮箱格式

```js
// 简单邮箱验证（基础格式�?const emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
console.log(emailRe.test('user@example.com')); // true
console.log(emailRe.test('invalid.email')); // false
```

### 严格的邮箱验�?
```js
// 较严格的邮箱验证
const strictEmailRe = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
console.log(strictEmailRe.test('user.name+tag@example.co.uk')); // true
console.log(strictEmailRe.test('user@example')); // false
```

### RFC 5322 标准邮箱

```js
// 更符�?RFC 5322 的邮箱验证（简化版�?const rfcEmailRe = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;
```

## URL 匹配与提�?
### 基础 URL 匹配

```js
// 简�?URL 匹配
const urlRe = /^https?:\/\/[\w.-]+/;
console.log(urlRe.test('https://example.com')); // true
console.log(urlRe.test('http://test.org/path')); // true
```

### 完整 URL 提取（命名捕获组�?
```js
// 提取 URL 的各个部�?const urlRe = /^(?<protocol>https?):\/\/(?<domain>[\w.-]+)(?<path>\/[^\s]*)?(?<query>\?[^\s]*)?(?<hash>#.*)?$/;
const match = 'https://example.com/path/to/page?param=value#section'.match(urlRe);
console.log(match.groups.protocol); // "https"
console.log(match.groups.domain);   // "example.com"
console.log(match.groups.path);     // "/path/to/page"
console.log(match.groups.query);    // "?param=value"
console.log(match.groups.hash);     // "#section"
```

### 从文本中提取所�?URL

```js
// 从文本中提取所�?URL
const text = 'Visit https://example.com and http://test.org for more info';
const urlRe = /https?:\/\/[\w.-]+(?:\/[\w.-]*)*(?:\?[\w=&-]*)?(?:#[\w.-]*)?/g;
const urls = text.match(urlRe);
console.log(urls); // ["https://example.com", "http://test.org"]
```

## 日期匹配

### 基础日期格式

```js
// YYYY-MM-DD 格式
const dateRe = /^\d{4}-\d{2}-\d{2}$/;
console.log(dateRe.test('2025-12-17')); // true
console.log(dateRe.test('2025-1-1')); // false
```

### 带验证的日期匹配

```js
// 验证日期有效性（简单版本）
const dateRe = /^(?<year>\d{4})-(?<month>0[1-9]|1[0-2])-(?<day>0[1-9]|[12]\d|3[01])$/;
const match = '2025-12-17'.match(dateRe);
if (match) {
    console.log(`�? ${match.groups.year}, �? ${match.groups.month}, �? ${match.groups.day}`);
}
```

### 多种日期格式

```js
// 匹配多种日期格式
const dateRe = /^\d{4}[-\/]\d{2}[-\/]\d{2}$/;
console.log(dateRe.test('2025-12-17')); // true
console.log(dateRe.test('2025/12/17')); // true
```

## 手机号验�?
### 中国手机�?
```js
// 中国手机号（11位，1开头，第二位为3-9�?const phoneRe = /^1[3-9]\d{9}$/;
console.log(phoneRe.test('13812345678')); // true
console.log(phoneRe.test('12812345678')); // false
```

### 带区号的手机�?
```js
// 带区号的手机号（可选）
const phoneWithAreaRe = /^(?:\+86)?[-\s]?1[3-9]\d{9}$/;
console.log(phoneWithAreaRe.test('+86-13812345678')); // true
console.log(phoneWithAreaRe.test('138 1234 5678')); // true
```

### 国际手机号（简化）

```js
// 国际手机号（简化版本）
const internationalPhoneRe = /^\+(?:[1-9]\d{0,3})[-\s]?\d{6,14}$/;
console.log(internationalPhoneRe.test('+1-555-123-4567')); // true
console.log(internationalPhoneRe.test('+86 138 1234 5678')); // true
```

## 身份证号验证

### 中国身份证号

```js
// 18位身份证号（简单验证）
const idCardRe = /^[1-9]\d{5}(?:18|19|20)\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])\d{3}[\dXx]$/;
console.log(idCardRe.test('110101199001011234')); // true
console.log(idCardRe.test('11010119900101123X')); // true
```

### 带格式的身份证号

```js
// 带分隔符的身份证�?const idCardFormattedRe = /^[1-9]\d{5}(?:\d{2}){2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])\d{3}[\dXx]$/;
```

## IP 地址匹配

### IPv4 地址

```js
// IPv4 地址�?.0.0.0 �?255.255.255.255�?const ipv4Re = /^(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$/;
console.log(ipv4Re.test('192.168.1.1')); // true
console.log(ipv4Re.test('256.1.1.1')); // false
```

### IPv6 地址（简化）

```js
// IPv6 地址（简化版本）
const ipv6Re = /^(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$/;
console.log(ipv6Re.test('2001:0db8:85a3:0000:0000:8a2e:0370:7334')); // true
```

## 密码强度验证

### 基础密码要求

```js
// 至少8位，包含字母和数�?const passwordRe = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
console.log(passwordRe.test('password123')); // true
console.log(passwordRe.test('12345678')); // false（缺少字母）
```

### 强密码要�?
```js
// 至少8位，包含大小写字母、数字和特殊字符
const strongPasswordRe = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
console.log(strongPasswordRe.test('Password123!')); // true
console.log(strongPasswordRe.test('password123')); // false
```

## 中文匹配

### 基础中文匹配

```js
// 匹配中文字符
const chineseRe = /[\u4e00-\u9fa5]/;
console.log(chineseRe.test('你好')); // true
console.log(chineseRe.test('hello')); // false
```

### Unicode 属性方式（推荐�?
```js
// 使用 Unicode 属性（需�?u 标志�?const chineseReUnicode = /\p{Script=Han}/u;
console.log(chineseReUnicode.test('你好世界')); // true
```

## 数字格式�?
### 千分位分�?
```js
// 添加千分位分隔符
const number = '1234567.89';
const formatted = number.replace(/\B(?=(\d{3})+(?!\d))/g, ',');
console.log(formatted); // "1,234,567.89"
```

### 提取数字

```js
// 从文本中提取所有数�?const text = 'Price: $99.99, Tax: $9.99';
const numbers = text.match(/\d+\.?\d*/g);
console.log(numbers); // ["99.99", "9.99"]
```

## HTML 标签处理

### 匹配 HTML 标签

```js
// 匹配 HTML 标签
const tagRe = /<(\w+)[^>]*>.*?<\/\1>/g;
const html = '<div>Content</div><span>Text</span>';
console.log(html.match(tagRe)); // ["<div>Content</div>", "<span>Text</span>"]
```

### 移除 HTML 标签

```js
// 移除所�?HTML 标签
const html = '<div>Hello <strong>World</strong></div>';
const text = html.replace(/<[^>]+>/g, '');
console.log(text); // "Hello World"
```

## 文件路径处理

### 提取文件�?
```js
// 从路径中提取文件�?const pathRe = /[^\/\\]+$/;
const path = '/path/to/file.txt';
console.log(path.match(pathRe)[0]); // "file.txt"
```

### 提取文件扩展�?
```js
// 提取文件扩展�?const extRe = /\.([^.]+)$/;
const filename = 'document.pdf';
const match = filename.match(extRe);
console.log(match[1]); // "pdf"
```

## 颜色值匹�?
### 十六进制颜色

```js
// 十六进制颜色值（#RGB �?#RRGGBB�?const hexColorRe = /^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/;
console.log(hexColorRe.test('#FF0000')); // true
console.log(hexColorRe.test('#F00')); // true
console.log(hexColorRe.test('#GG0000')); // false
```

### RGB 颜色�?
```js
// RGB/RGBA 颜色�?const rgbColorRe = /^rgba?\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*(?:,\s*[\d.]+\s*)?\)$/;
console.log(rgbColorRe.test('rgb(255, 0, 0)')); // true
console.log(rgbColorRe.test('rgba(255, 0, 0, 0.5)')); // true
```

## 时间格式匹配

### 24小时制时�?
```js
// HH:MM �?HH:MM:SS 格式
const timeRe = /^([01]\d|2[0-3]):([0-5]\d)(?::([0-5]\d))?$/;
console.log(timeRe.test('23:59:59')); // true
console.log(timeRe.test('09:30')); // true
console.log(timeRe.test('25:00')); // false
```

## 注意事项

1. **验证 vs 匹配**：正则表达式只能验证格式，不能验证逻辑正确性（如日期是否真实存在）
2. **安全�?*：不要仅依赖客户端正则验证，服务端也要验�?3. **性能**：复杂正则可能影响性能，需要测试和优化
4. **可维护�?*：复杂的正则表达式应该添加注释说�?5. **国际�?*：考虑不同地区的格式差�?
## 常见错误

### 错误 1：过度简�?
```js
// 错误：过于简单，可能匹配无效邮箱
const badEmailRe = /.+@.+/;
console.log(badEmailRe.test('a@b')); // true（无效）

// 正确：更严格的验�?const goodEmailRe = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
```

### 错误 2：忘记边界符

```js
// 错误：可能匹配部分字符串
const badRe = /\d{4}-\d{2}-\d{2}/;
console.log(badRe.test('Date: 2025-12-17 in log')); // true（应该只匹配完整日期�?
// 正确：使用边界符
const goodRe = /^\d{4}-\d{2}-\d{2}$/;
```

### 错误 3：转义问�?
```js
// 错误：在字符串中需要转�?const badRe = new RegExp('^d+$'); // 错误：\d 被转�?
// 正确：双重转义或使用字面�?const goodRe1 = new RegExp('^\\d+$');
const goodRe2 = /^\d+$/;
```

## 最佳实�?
1. **使用命名捕获�?*：提高代码可读�?2. **添加注释**：复杂正则添加注释说�?3. **测试覆盖**：编写测试用例验证各种情�?4. **性能考虑**：对于频繁使用的正则，考虑预编�?5. **组合使用**：复杂验证可以拆分为多个简单正�?
## 练习

1. **邮箱验证**：编写正则表达式验证邮箱，要求：
   - 用户名部分允许字母、数字、点、下划线、连字符
   - 域名部分至少包含一个点
   - 顶级域名至少2个字�?
2. **URL 提取**：编写正则表达式从文本中提取所�?URL，并使用命名捕获组分别提取协议、域名和路径�?
3. **日期验证**：编写正则表达式验证日期格式 YYYY-MM-DD，并验证月份和日期的有效性范围�?
4. **手机号格式化**：编写代码将手机号格式化�?138-1234-5678 的格式�?
5. **密码强度检�?*：编写函数检测密码强度，要求�?   - 至少8�?   - 包含大小写字�?   - 包含数字
   - 包含特殊字符

完成以上练习后，继续学习下一节，了解正则表达式性能优化�?
## 总结

常见正则模式包括邮箱、URL、日期、手机号、身份证号等验证，掌握这些常用模式可以快速解决实际开发中的文本处理需求。编写正则表达式时要注意验证的严格性和性能，添加适当的注释提高可维护性�?
## 相关资源

- [MDN：正则表达式](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions)
- [正则表达式测试工具](https://regex101.com/)
- [常用正则表达式收集](https://github.com/ziishaned/learn-regex)
