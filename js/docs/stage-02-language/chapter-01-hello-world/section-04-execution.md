# 2.1.4 执行方式（浏览器、Node.js、REPL）

## 概述

JavaScript 可以在多种环境中执行。本节介绍在不同环境中执行 JavaScript 代码的方法，包括浏览器、Node.js 和 REPL。

## 浏览器环境

### 方法一：HTML 中嵌入

在 HTML 文件中直接嵌入 JavaScript 代码：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>JavaScript 执行</title>
</head>
<body>
    <script>
        console.log("Hello from HTML!");
    </script>
</body>
</html>
```

### 方法二：外部 JavaScript 文件

创建独立的 JavaScript 文件，在 HTML 中引用：

**script.js**:
```js
console.log("Hello from external file!");
```

**index.html**:
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>JavaScript 执行</title>
</head>
<body>
    <script src="script.js"></script>
</body>
</html>
```

### 方法三：ES Modules

使用 ES Modules 方式加载：

**module.js**:
```js
export function greet() {
    return "Hello from module!";
}
```

**index.html**:
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>JavaScript 执行</title>
</head>
<body>
    <script type="module">
        import { greet } from './module.js';
        console.log(greet());
    </script>
</body>
</html>
```

### 浏览器控制台

直接在浏览器控制台中执行代码：

1. 打开浏览器开发者工具（F12）
2. 切换到 Console 标签
3. 输入代码并回车执行

```js
// 在控制台中直接输入
console.log("Hello from console!");
let x = 10;
x * 2; // 输出 20
```

## Node.js 环境

### 执行文件

使用 `node` 命令执行 JavaScript 文件：

```bash
# 执行单个文件
node app.js

# 执行多个文件
node file1.js file2.js
```

### 示例

**app.js**:
```js
console.log("Hello from Node.js!");
console.log("Node.js version:", process.version);
```

执行：
```bash
node app.js
```

输出：
```
Hello from Node.js!
Node.js version: v20.10.0
```

### 执行字符串

使用 `-e` 选项执行字符串中的代码：

```bash
node -e "console.log('Hello from command line!')"
```

### 执行标准输入

使用管道输入代码：

```bash
echo "console.log('Hello from stdin!')" | node
```

## REPL（交互式解释器）

### Node.js REPL

启动 Node.js REPL：

```bash
node
```

进入 REPL 后，可以直接输入代码：

```js
> console.log("Hello from REPL!")
Hello from REPL!
undefined

> let x = 10
undefined

> x * 2
20

> .exit  // 退出 REPL
```

### REPL 命令

- **`.help`**：显示帮助信息
- **`.exit`** 或 `Ctrl+D`：退出 REPL
- **`.clear`** 或 `Ctrl+L`：清屏
- **`.save <file>`**：保存当前会话到文件
- **`.load <file>`**：加载文件到当前会话

### 浏览器控制台作为 REPL

浏览器控制台也可以作为 REPL 使用：

```js
// 在浏览器控制台中
> let x = 10
undefined

> x * 2
20

> function greet(name) { return `Hello, ${name}!`; }
undefined

> greet("World")
"Hello, World!"
```

## 不同环境的差异

### 全局对象

```js
// 浏览器环境
console.log(typeof window);  // "object"
console.log(typeof document); // "object"

// Node.js 环境
console.log(typeof global);   // "object"
console.log(typeof process);  // "object"
```

### 可用的 API

```js
// 浏览器环境
// 可以使用 DOM API
document.getElementById('myId');

// 可以使用 Fetch API
fetch('/api/data')
    .then(response => response.json())
    .then(data => console.log(data));

// Node.js 环境
// 可以使用文件系统 API
const fs = require('fs');
fs.readFile('file.txt', 'utf8', (err, data) => {
    if (err) throw err;
    console.log(data);
});

// 可以使用 HTTP 模块
const http = require('http');
http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello from Node.js!');
}).listen(3000);
```

### 模块系统

```js
// 浏览器环境（ES Modules）
import { func } from './module.js';

// Node.js 环境（CommonJS）
const { func } = require('./module.js');

// Node.js 环境（ES Modules，需要配置）
import { func } from './module.js';
```

## 执行顺序

### 同步执行

代码按照顺序同步执行：

```js
console.log("1");
console.log("2");
console.log("3");
```

输出：
```
1
2
3
```

### 异步执行

异步代码会在同步代码之后执行：

```js
console.log("1");

setTimeout(() => {
    console.log("2");
}, 0);

console.log("3");
```

输出：
```
1
3
2
```

## 调试执行

### 使用 debugger

在代码中添加 `debugger` 语句：

```js
function calculate(x, y) {
    debugger; // 执行到这里会暂停
    return x + y;
}

calculate(10, 20);
```

在浏览器中打开开发者工具，代码会在 `debugger` 处暂停。

### 使用 console

使用 `console` 方法进行调试：

```js
console.log("普通信息");
console.warn("警告信息");
console.error("错误信息");
console.info("提示信息");
console.debug("调试信息");

// 输出对象
const user = { name: "John", age: 30 };
console.log(user);
console.table(user);

// 计时
console.time("timer");
// 执行一些代码
console.timeEnd("timer");
```

## 最佳实践

### 1. 选择合适的执行环境

- **浏览器**：前端应用、DOM 操作
- **Node.js**：服务器端应用、命令行工具
- **REPL**：快速测试、学习实验

### 2. 使用模块化

```js
// 好的做法：使用模块化
// math.js
export function add(a, b) {
    return a + b;
}

// app.js
import { add } from './math.js';
console.log(add(1, 2));
```

### 3. 错误处理

```js
// 使用 try-catch 处理错误
try {
    riskyOperation();
} catch (error) {
    console.error("Error:", error);
}
```

### 4. 使用严格模式

```js
"use strict";

// 严格模式下的代码
let x = 10;
```

## 总结

了解不同环境下的执行方式，有助于选择合适的开发环境。主要要点：

- 浏览器环境：HTML 嵌入、外部文件、ES Modules
- Node.js 环境：执行文件、命令行、REPL
- REPL：交互式执行、快速测试
- 不同环境有不同的全局对象和 API
- 使用适当的调试工具

完成本章学习后，继续学习下一章：变量与常量。
