# 1.1.3 Node.js 环境

## 概述

Node.js 是基于 V8 引擎的服务器端 JavaScript 运行环境，使 JavaScript 能够在服务器端运行。本节详细介绍 Node.js 的安装、配置和基本使用。

## Node.js 简介

### 什么是 Node.js

Node.js 是一个基于 Chrome V8 引擎的 JavaScript 运行时，使 JavaScript 能够在服务器端运行。

**主要特点**：
- 基于 V8 引擎
- 事件驱动、非阻塞 I/O
- 单线程事件循环
- 丰富的核心模块
- 庞大的包生态系统（npm）

### Node.js 的诞生

Node.js 由 Ryan Dahl 于 2009 年创建，目的是让 JavaScript 能够在服务器端运行。

### Node.js 的应用场景

- **Web 服务器**：构建 HTTP 服务器
- **API 服务**：RESTful API、GraphQL API
- **命令行工具**：开发工具、脚本
- **实时应用**：WebSocket 服务器、聊天应用
- **微服务**：构建微服务架构
- **全栈开发**：前后端统一使用 JavaScript

## Node.js 安装

### Windows 安装

#### 方法一：官方安装包

1. 访问 [Node.js 官网](https://nodejs.org/)
2. 下载 LTS（长期支持）版本
3. 运行安装程序
4. 按照向导完成安装

#### 方法二：使用包管理器

**使用 Chocolatey**：
```powershell
choco install nodejs-lts
```

**使用 Scoop**：
```powershell
scoop install nodejs-lts
```

#### 方法三：使用版本管理器（推荐）

**使用 nvm-windows**：
```powershell
# 安装 nvm-windows
# 下载：https://github.com/coreybutler/nvm-windows/releases

# 安装 Node.js
nvm install 20.10.0
nvm use 20.10.0

# 查看已安装版本
nvm list

# 切换版本
nvm use 18.18.0
```

### macOS 安装

#### 方法一：官方安装包

1. 访问 [Node.js 官网](https://nodejs.org/)
2. 下载 macOS 安装包
3. 运行安装程序

#### 方法二：使用 Homebrew

```bash
# 安装 Homebrew（如果未安装）
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 安装 Node.js
brew install node

# 安装特定版本
brew install node@20
```

#### 方法三：使用版本管理器

**使用 nvm**：
```bash
# 安装 nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

# 重新加载 shell 配置
source ~/.bashrc  # 或 ~/.zshrc

# 安装 Node.js
nvm install 20.10.0
nvm use 20.10.0

# 设置默认版本
nvm alias default 20.10.0

# 查看已安装版本
nvm list

# 切换版本
nvm use 18.18.0
```

**使用 fnm（Fast Node Manager）**：
```bash
# 安装 fnm
curl -fsSL https://fnm.vercel.app/install | bash

# 安装 Node.js
fnm install 20.10.0
fnm use 20.10.0

# 设置默认版本
fnm default 20.10.0
```

### Linux 安装

#### 方法一：使用包管理器

**Ubuntu/Debian**：
```bash
# 使用 NodeSource 仓库
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# 或使用默认仓库
sudo apt update
sudo apt install nodejs npm
```

**CentOS/RHEL**：
```bash
# 使用 NodeSource 仓库
curl -fsSL https://rpm.nodesource.com/setup_20.x | sudo bash -
sudo yum install -y nodejs
```

#### 方法二：使用版本管理器

**使用 nvm**：
```bash
# 安装 nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

# 重新加载 shell 配置
source ~/.bashrc

# 安装 Node.js
nvm install 20.10.0
nvm use 20.10.0
```

## 验证安装

### 检查版本

```bash
# 检查 Node.js 版本
node --version
# 或
node -v

# 检查 npm 版本
npm --version
# 或
npm -v

# 查看详细信息
node -p "process.versions"
```

### 运行第一个程序

创建 `hello.js` 文件：

```js
// hello.js
console.log("Hello, Node.js!");
```

运行程序：

```bash
node hello.js
```

输出：
```
Hello, Node.js!
```

## Node.js 核心模块

### fs 模块（文件系统）

fs 模块提供了文件系统操作功能。

```js
// 引入 fs 模块
const fs = require('fs');

// 同步读取文件
const data = fs.readFileSync('file.txt', 'utf8');
console.log(data);

// 异步读取文件
fs.readFile('file.txt', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data);
});

// 使用 Promise（Node.js 14+）
const fs = require('fs').promises;

async function readFile() {
    try {
        const data = await fs.readFile('file.txt', 'utf8');
        console.log(data);
    } catch (error) {
        console.error(error);
    }
}
```

### path 模块（路径处理）

path 模块提供了路径处理功能。

```js
const path = require('path');

// 路径拼接
const fullPath = path.join('/users', 'john', 'documents', 'file.txt');
// Windows: \users\john\documents\file.txt
// Unix: /users/john/documents/file.txt

// 路径解析
const parsed = path.parse('/users/john/file.txt');
// {
//   root: '/',
//   dir: '/users/john',
//   base: 'file.txt',
//   ext: '.txt',
//   name: 'file'
// }

// 获取文件名
const filename = path.basename('/users/john/file.txt');  // 'file.txt'

// 获取目录名
const dirname = path.dirname('/users/john/file.txt');    // '/users/john'

// 获取扩展名
const ext = path.extname('/users/john/file.txt');       // '.txt'

// 解析为绝对路径
const absolute = path.resolve('file.txt');
```

### http 模块（HTTP 服务器）

http 模块提供了创建 HTTP 服务器的功能。

```js
const http = require('http');

// 创建服务器
const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello, Node.js!');
});

// 监听端口
server.listen(3000, () => {
    console.log('Server running at http://localhost:3000/');
});
```

### events 模块（事件系统）

events 模块提供了事件处理功能。

```js
const EventEmitter = require('events');

// 创建事件发射器
const emitter = new EventEmitter();

// 监听事件
emitter.on('event', (data) => {
    console.log('Event received:', data);
});

// 触发事件
emitter.emit('event', { message: 'Hello' });

// 只监听一次
emitter.once('event', () => {
    console.log('This will only fire once');
});

// 移除监听器
emitter.removeListener('event', handler);

// 移除所有监听器
emitter.removeAllListeners('event');
```

### crypto 模块（加密）

crypto 模块提供了加密功能。

```js
const crypto = require('crypto');

// 创建哈希
const hash = crypto.createHash('sha256');
hash.update('Hello, World!');
const digest = hash.digest('hex');
console.log(digest);

// 生成随机字节
const randomBytes = crypto.randomBytes(16);
console.log(randomBytes.toString('hex'));
```

## npm 包管理器

### npm 简介

npm（Node Package Manager）是 Node.js 的默认包管理器，也是世界上最大的软件注册表。

### 基本命令

#### 初始化项目

```bash
# 初始化 package.json
npm init

# 使用默认值快速初始化
npm init -y
```

生成的 `package.json` 示例：

```json
{
  "name": "my-project",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

#### 安装包

```bash
# 安装到 dependencies
npm install package-name

# 安装到 devDependencies
npm install --save-dev package-name

# 全局安装
npm install -g package-name

# 安装特定版本
npm install package-name@1.2.3

# 安装最新版本
npm install package-name@latest
```

#### 卸载包

```bash
# 卸载包
npm uninstall package-name

# 卸载全局包
npm uninstall -g package-name
```

#### 更新包

```bash
# 更新所有包
npm update

# 更新特定包
npm update package-name

# 检查过时的包
npm outdated
```

#### 查看包信息

```bash
# 查看已安装的包
npm list

# 查看全局包
npm list -g

# 查看包信息
npm info package-name

# 查看包版本
npm view package-name version
```

### package.json

package.json 是 Node.js 项目的配置文件。

#### 主要字段

```json
{
  "name": "my-project",
  "version": "1.0.0",
  "description": "项目描述",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "test": "jest",
    "dev": "node --watch index.js"
  },
  "dependencies": {
    "express": "^4.18.2"
  },
  "devDependencies": {
    "jest": "^29.5.0"
  },
  "engines": {
    "node": ">=18.0.0",
    "npm": ">=9.0.0"
  }
}
```

#### scripts 字段

scripts 字段定义了可执行的脚本命令。

```json
{
  "scripts": {
    "start": "node index.js",
    "dev": "node --watch index.js",
    "test": "jest",
    "build": "webpack --mode production",
    "lint": "eslint ."
  }
}
```

运行脚本：

```bash
npm run start
npm run dev
npm run test
```

## Node.js 与浏览器的差异

### 全局对象

```js
// 浏览器
console.log(window);      // 全局对象
console.log(document);    // DOM 文档

// Node.js
console.log(global);       // 全局对象
console.log(process);     // 进程对象
// 没有 document
```

### 模块系统

```js
// 浏览器：ES Modules
import { func } from './module.js';

// Node.js：CommonJS（传统）
const { func } = require('./module');

// Node.js：ES Modules（现代，需要配置）
import { func } from './module.js';
```

### 文件系统访问

```js
// 浏览器：无法直接访问文件系统
// 需要通过 File API 或用户选择

// Node.js：可以直接访问文件系统
const fs = require('fs');
const data = fs.readFileSync('file.txt', 'utf8');
```

### 网络请求

```js
// 浏览器：Fetch API、XMLHttpRequest
fetch('/api/data')
    .then(response => response.json())
    .then(data => console.log(data));

// Node.js：http/https 模块、fetch（Node.js 18+）
const https = require('https');
// 或使用 fetch（Node.js 18+）
fetch('https://api.example.com/data')
    .then(response => response.json())
    .then(data => console.log(data));
```

## Node.js 版本管理

### 使用 nvm

nvm（Node Version Manager）是 Node.js 的版本管理工具。

```bash
# 安装 Node.js 版本
nvm install 20.10.0
nvm install 18.18.0
nvm install 16.20.0

# 使用特定版本
nvm use 20.10.0

# 设置默认版本
nvm alias default 20.10.0

# 查看已安装版本
nvm list

# 查看可用版本
nvm list-remote

# 卸载版本
nvm uninstall 16.20.0
```

### 使用 fnm

fnm（Fast Node Manager）是另一个 Node.js 版本管理工具。

```bash
# 安装 Node.js 版本
fnm install 20.10.0
fnm install 18.18.0

# 使用特定版本
fnm use 20.10.0

# 设置默认版本
fnm default 20.10.0

# 查看已安装版本
fnm list
```

## 常见问题

### 权限问题

在 Linux/macOS 上，全局安装可能需要 sudo：

```bash
# 不推荐：使用 sudo
sudo npm install -g package-name

# 推荐：配置 npm 全局目录
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
export PATH=~/.npm-global/bin:$PATH
```

### 版本兼容性

检查 Node.js 版本要求：

```bash
# 查看当前版本
node --version

# 查看项目要求的版本
cat package.json | grep engines
```

### 缓存问题

清理 npm 缓存：

```bash
# 清理缓存
npm cache clean --force

# 查看缓存位置
npm config get cache
```

## 总结

Node.js 使 JavaScript 能够在服务器端运行，提供了丰富的核心模块和庞大的包生态系统。掌握 Node.js 的安装、配置和基本使用，是进行服务器端 JavaScript 开发的基础。

## 相关资源

- [Node.js 官方文档](https://nodejs.org/)
- [npm 官方文档](https://docs.npmjs.com/)
- [Node.js API 文档](https://nodejs.org/api/)
