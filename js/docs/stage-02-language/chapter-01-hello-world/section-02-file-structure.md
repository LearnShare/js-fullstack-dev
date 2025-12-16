# 2.1.2 文件结构与编码

## 概述

了解 JavaScript 文件的结构和编码规范，有助于编写规范的代码。本节介绍文件结构、编码规范和组织方式。

## 文件扩展名

### JavaScript 文件

JavaScript 文件通常使用以下扩展名：

- **`.js`**：标准的 JavaScript 文件（最常用）
- **`.mjs`**：ES Modules 文件（Node.js）
- **`.cjs`**：CommonJS 文件（Node.js）

### 示例

```js
// app.js - 标准 JavaScript 文件
console.log("Hello, World!");

// app.mjs - ES Modules 文件
export function greet() {
    return "Hello, World!";
}

// app.cjs - CommonJS 文件
module.exports = {
    greet: function() {
        return "Hello, World!";
    }
};
```

## 文件编码

### UTF-8 编码

JavaScript 文件应该使用 **UTF-8** 编码，这是 Web 标准编码。

**原因**：
- 支持所有 Unicode 字符
- 跨平台兼容性好
- Web 标准推荐

### 检查文件编码

在编辑器中检查文件编码：

- **VS Code**：右下角显示编码，点击可更改
- **WebStorm**：`File` → `File Encoding` → `UTF-8`

### BOM（字节顺序标记）

**不推荐使用 BOM**：

- UTF-8 不需要 BOM
- BOM 可能导致某些工具出现问题
- 现代编辑器默认使用 UTF-8 without BOM

## 文件结构

### 基本结构

一个典型的 JavaScript 文件结构：

```js
// 1. 文件头注释（可选）
/**
 * 文件名：app.js
 * 描述：应用程序主文件
 * 作者：Your Name
 * 日期：2024-01-01
 */

// 2. 导入语句（如果有）
import { helper } from './helper.js';

// 3. 常量定义
const API_URL = 'https://api.example.com';
const MAX_RETRIES = 3;

// 4. 变量定义
let currentUser = null;

// 5. 函数定义
function initialize() {
    // 初始化代码
}

function processData(data) {
    // 处理数据
}

// 6. 类定义（如果有）
class User {
    constructor(name) {
        this.name = name;
    }
}

// 7. 主执行代码
initialize();
```

### 模块化结构

使用 ES Modules 的文件结构：

```js
// utils.js
// 工具函数模块

// 导入依赖
import { format } from './formatter.js';

// 导出函数
export function add(a, b) {
    return a + b;
}

export function subtract(a, b) {
    return a - b;
}

// 默认导出
export default {
    add,
    subtract
};
```

## 代码组织

### 按功能组织

将相关功能组织在一起：

```js
// 用户相关功能
function getUser(id) {
    // ...
}

function updateUser(id, data) {
    // ...
}

// 订单相关功能
function createOrder(data) {
    // ...
}

function getOrder(id) {
    // ...
}
```

### 按类型组织

将相同类型的代码组织在一起：

```js
// 常量
const API_URL = 'https://api.example.com';
const TIMEOUT = 5000;

// 变量
let currentUser = null;
let isLoading = false;

// 函数
function fetchData() {
    // ...
}

function processData(data) {
    // ...
}

// 类
class User {
    // ...
}
```

## 文件命名规范

### 基本规则

- 使用小写字母
- 使用连字符（`-`）分隔单词
- 使用有意义的名称
- 避免使用特殊字符

### 命名示例

```js
// 好的命名
user-profile.js
order-manager.js
api-client.js

// 不好的命名
UserProfile.js      // 使用了大写
order_manager.js    // 使用了下划线
app.js             // 名称不够具体
```

### 特殊文件命名

```js
// 配置文件
config.js
settings.js

// 工具文件
utils.js
helpers.js

// 测试文件
user.test.js
order.spec.js
```

## 目录结构

### 小型项目

```
project/
├── index.html
├── app.js
├── style.css
└── utils.js
```

### 中型项目

```
project/
├── index.html
├── src/
│   ├── main.js
│   ├── components/
│   ├── utils/
│   └── api/
├── styles/
│   └── main.css
└── assets/
    └── images/
```

### 大型项目

```
project/
├── index.html
├── src/
│   ├── main.js
│   ├── components/
│   │   ├── Header/
│   │   ├── Footer/
│   │   └── UserProfile/
│   ├── utils/
│   │   ├── formatters.js
│   │   └── validators.js
│   ├── api/
│   │   ├── users.js
│   │   └── orders.js
│   └── styles/
│       └── main.css
├── tests/
│   ├── unit/
│   └── integration/
└── docs/
    └── README.md
```

## 最佳实践

### 1. 单一职责

每个文件应该只负责一个功能或一个模块。

```js
// 好的做法：单一职责
// user.js - 只处理用户相关功能
export function getUser(id) { }
export function updateUser(id, data) { }

// 不好的做法：混合职责
// utils.js - 混合了多种功能
export function getUser(id) { }
export function formatDate(date) { }
export function validateEmail(email) { }
```

### 2. 清晰的导入导出

使用明确的导入和导出：

```js
// 好的做法：明确的导出
export function add(a, b) {
    return a + b;
}

export const PI = 3.14159;

// 使用明确的导入
import { add, PI } from './math.js';

// 不好的做法：默认导出所有内容
export default {
    add: function(a, b) { return a + b; },
    PI: 3.14159
};
```

### 3. 文件大小控制

保持文件大小合理（建议不超过 300-500 行）：

- 如果文件过大，考虑拆分成多个文件
- 将相关功能组织到同一个文件中
- 使用模块化组织代码

### 4. 注释和文档

为文件添加适当的注释：

```js
/**
 * 用户管理模块
 * 
 * 提供用户相关的功能，包括：
 * - 获取用户信息
 * - 更新用户信息
 * - 删除用户
 * 
 * @module user
 */

/**
 * 获取用户信息
 * @param {string} id - 用户 ID
 * @returns {Promise<Object>} 用户信息
 */
export async function getUser(id) {
    // ...
}
```

## 总结

了解 JavaScript 文件的结构和编码规范，有助于编写规范的代码。主要要点：

- 使用 `.js` 扩展名（或 `.mjs`、`.cjs`）
- 使用 UTF-8 编码
- 按照功能或类型组织代码
- 使用有意义的文件命名
- 保持文件大小合理
- 添加适当的注释

继续学习下一节，了解语句和注释的用法。
