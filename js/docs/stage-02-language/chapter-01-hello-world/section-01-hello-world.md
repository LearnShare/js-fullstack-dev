# 2.1.1 Hello World 程序

## 概述

Hello World 是学习任何编程语言的第一个程序。本节介绍如何编写和运行第一个 JavaScript 程序。

## 浏览器中的 Hello World

### 方法一：在 HTML 中嵌入

创建 `index.html` 文件：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Hello World</title>
</head>
<body>
    <script>
        console.log("Hello, World!");
    </script>
</body>
</html>
```

在浏览器中打开 `index.html`，打开开发者工具（F12），在控制台中会看到输出：`Hello, World!`

### 方法二：外部 JavaScript 文件

创建 `hello.js` 文件：

```js
console.log("Hello, World!");
```

创建 `index.html` 文件：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Hello World</title>
</head>
<body>
    <script src="hello.js"></script>
</body>
</html>
```

在浏览器中打开 `index.html`，控制台会输出：`Hello, World!`

### 方法三：使用 ES Modules

创建 `hello.js` 文件：

```js
console.log("Hello, World!");
```

创建 `index.html` 文件：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Hello World</title>
</head>
<body>
    <script type="module" src="hello.js"></script>
</body>
</html>
```

## Node.js 中的 Hello World

### 创建文件

创建 `hello.js` 文件：

```js
console.log("Hello, World!");
```

### 执行程序

在命令行中执行：

```bash
node hello.js
```

输出：
```
Hello, World!
```

## 完整的 Hello World 示例

### 带变量的版本

```js
// 定义变量
const message = "Hello, World!";

// 输出到控制台
console.log(message);
```

### 带函数的版本

```js
// 定义函数
function greet() {
    return "Hello, World!";
}

// 调用函数并输出
console.log(greet());
```

### 带参数的版本

```js
// 定义带参数的函数
function greet(name) {
    return `Hello, ${name}!`;
}

// 调用函数
console.log(greet("World"));
console.log(greet("JavaScript"));
```

输出：
```
Hello, World!
Hello, JavaScript!
```

## 使用 alert（仅浏览器）

在浏览器中，可以使用 `alert()` 显示对话框：

```js
alert("Hello, World!");
```

**注意**：`alert()` 只在浏览器环境中可用，在 Node.js 中不可用。

## 使用 document.write（仅浏览器）

在浏览器中，可以使用 `document.write()` 写入 HTML：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Hello World</title>
</head>
<body>
    <script>
        document.write("<h1>Hello, World!</h1>");
    </script>
</body>
</html>
```

**注意**：`document.write()` 只在浏览器环境中可用，且不推荐在现代开发中使用。

## 验证环境

### 检查浏览器环境

```js
// 检查是否在浏览器环境中
if (typeof window !== 'undefined') {
    console.log("运行在浏览器环境中");
    console.log("浏览器：", navigator.userAgent);
}
```

### 检查 Node.js 环境

```js
// 检查是否在 Node.js 环境中
if (typeof process !== 'undefined' && process.versions && process.versions.node) {
    console.log("运行在 Node.js 环境中");
    console.log("Node.js 版本：", process.versions.node);
}
```

## 常见问题

### 问题 1：控制台没有输出

**可能原因**：
- 没有打开开发者工具
- 代码有语法错误
- 文件路径不正确

**解决方法**：
- 按 F12 打开开发者工具
- 检查控制台是否有错误信息
- 确认文件路径正确

### 问题 2：Node.js 提示找不到文件

**可能原因**：
- 文件路径不正确
- 文件不存在
- 当前目录不正确

**解决方法**：
- 使用绝对路径或相对路径
- 确认文件存在
- 使用 `cd` 命令切换到正确的目录

### 问题 3：中文显示乱码

**可能原因**：
- 文件编码不是 UTF-8
- HTML 没有设置正确的字符集

**解决方法**：
- 将文件保存为 UTF-8 编码
- 在 HTML 的 `<head>` 中添加 `<meta charset="UTF-8">`

## 下一步

完成第一个 JavaScript 程序后，继续学习：

- [文件结构与编码](section-02-file-structure.md)：了解 JavaScript 文件的结构和编码规范
- [语句与注释](section-03-statements-comments.md)：掌握语句规则和注释用法
- [执行方式](section-04-execution.md)：了解不同环境下的执行方式

## 总结

Hello World 是学习编程的第一步。通过本节的学习，你已经能够：

- 在浏览器中运行 JavaScript 代码
- 在 Node.js 中运行 JavaScript 代码
- 使用 `console.log()` 输出信息
- 理解基本的代码结构

继续学习下一节，深入了解 JavaScript 的文件结构和编码规范。
