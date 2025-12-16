# 2.11.1 错误类型

## 概述

JavaScript 通过内置错误类型对不同异常场景进行分类。熟悉各错误的触发条件、典型栈信息、修复方式，有助于快速定位问题并编写鲁棒的错误处理逻辑。本节梳理常见内置错误、触发示例、排查要点和最佳实践。

## 常见内置错误

### Error（通用错误）
基础错误类型，其他错误继承自它。
```js
throw new Error('Something went wrong');
```
- 触发：手动抛出，或自定义错误继承。
- 场景：业务校验失败、兜底异常。

### TypeError（类型错误）
在对不适当类型的值执行操作时触发。
```js
const obj = null;
obj.property; // TypeError: Cannot read properties of null

const fn = 123;
fn(); // TypeError: fn is not a function
```
- 场景：调用非函数、解构 null/undefined、访问不存在的方法等。

### ReferenceError（引用错误）
访问未声明的变量或作用域外变量。
```js
console.log(notDefined); // ReferenceError: notDefined is not defined
```
- 场景：变量名拼写错误、暂时性死区（let/const）、作用域链外访问。

### SyntaxError（语法错误）
代码解析阶段失败。
```js
// const x = ; // SyntaxError: Unexpected token
JSON.parse('{ bad json }'); // SyntaxError: Unexpected token b
```
- 场景：漏括号/逗号、非法 JSON、严格模式语法违规。

### RangeError（范围错误）
值超出有效范围。
```js
new Array(-1);        // RangeError: Invalid array length
Number.prototype.toFixed(101); // RangeError
```
- 场景：数组长度为负或过大，数字方法参数越界。

### URIError（URI 编码解码错误）
`decodeURI/decodeURIComponent` 传入无效编码。
```js
decodeURIComponent('%E0%A4%A'); // URIError: URI malformed
```

### EvalError（已废弃）
历史遗留，现代环境很少使用。

### AggregateError（聚合错误，ES2021）
表示多个错误集合，常用于 `Promise.any`。
```js
const err = new AggregateError([
  new Error('fail1'),
  new Error('fail2')
], 'All failed');
console.log(err.errors.length); // 2
```

## 错误对象的属性

- `name`：错误名称（TypeError/ReferenceError...）
- `message`：错误信息
- `stack`：调用栈（实现相关）
- 自定义字段：可在自定义错误中添加 `code`、`status` 等。

示例：
```js
try {
  throw new TypeError('Invalid type');
} catch (err) {
  console.log(err.name);    // TypeError
  console.log(err.message); // Invalid type
  console.log(err.stack);   // 调用栈
}
```

## 触发与排查示例

### TypeError 常见触发
- 调用非函数：`foo()` 但 foo 不是函数
- 访问空值属性：`null.prop` / `undefined.prop`
- 数组/字符串方法入参类型不符
- `this` 丢失导致方法未定义

排查建议：检查数据类型、提前做空值守卫、确认 this 绑定。

### ReferenceError 常见触发
- 变量未声明 / 拼写错误
- 暂时性死区：在 `let/const` 声明前访问

排查建议：启用 linter，检查作用域，避免在声明前使用。

### SyntaxError 常见触发
- JSON 解析不合规
- 模板/对象字面量缺逗号、括号
- 模块导入路径错误（可能表现为语法错误）

排查建议：使用格式化/ESLint；对 JSON 使用可信解析。

### RangeError 常见触发
- `new Array(-1)`、`new Array(1e9)`（过大）
- 数字格式化方法参数超界

排查建议：校验参数范围；避免滥用稀疏数组。

### URIError 常见触发
- 解码非法 URI 片段

排查建议：确保输入已正确编码；对用户输入加 try/catch。

### AggregateError 场景
- `Promise.any([])` 空数组
- `Promise.any` 中全部拒绝

排查建议：对 errors 逐条处理，或为空数组做前置判定。

## 自定义错误与语义化

为业务场景定义更语义化的错误类型，便于捕获和分类。

```js
class ValidationError extends Error {
  constructor(field, message) {
    super(`Invalid ${field}: ${message}`);
    this.name = 'ValidationError';
    this.field = field;
    this.code = 'VALIDATION_ERROR';
  }
}

throw new ValidationError('email', 'required');
```

## 浏览器 vs Node 栈信息差异

- 栈格式随引擎不同而异（V8/SpiderMonkey 等）。
- Source Map 可将压缩/打包后代码栈还原到源码。
- 生产环境避免暴露完整栈到前端用户，建议上报到监控平台。

## 错误分类与处理建议

- **可预期业务错误**：输入校验失败、权限不足 → 返回业务码；不应上报为致命错误。
- **可恢复错误**：网络重试、缓存降级。
- **编程错误**：空指针、类型错误、语法错误 → 开发期修复，生产期兜底上报+降级。

## 最佳实践

1) 使用语义化自定义错误，附加 `code`/`field`/`status`。  
2) 对外暴露友好提示，对内保留详细 message/stack。  
3) 在关键边界做参数校验，减少 TypeError/RangeError。  
4) 对 JSON/动态构造代码做 try/catch，避免 SyntaxError 崩溃。  
5) 结合监控（Sentry/自建）收集错误，配合 Source Map。  
6) 在异步链路中补齐 `.catch` / try...catch，避免未处理拒绝。  

## 练习

1. 手动构造并抛出 TypeError / ReferenceError / RangeError，观察栈信息。  
2. 写一个 JSON 解析函数，捕获 SyntaxError 并返回安全结果。  
3. 实现一个 ValidationError，并在表单校验中使用。  
4. 用 `Promise.any` 构造 AggregateError，遍历 `errors` 输出。  
5. 在浏览器和 Node 分别触发同类错误，比较 stack 格式差异。  

## 小结

- 内置错误类型对应不同异常来源：类型、引用、语法、范围、URI、聚合。  
- 正确识别错误类型能加速定位与分类处理。  
- 通过自定义错误、参数校验、监控上报与 Source Map，构建可靠的错误处理体系。  

继续学习下一节，了解异常捕获与 try...catch...finally。
