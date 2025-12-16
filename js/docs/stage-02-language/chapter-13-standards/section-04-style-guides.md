# 2.13.4 代码风格指南（Airbnb、Google、Standard）

## 概述

代码风格指南定义了 JavaScript 代码的格式和风格规范。主流的代码风格指南包括 Airbnb、Google 和 Standard。了解这些指南有助于选择适合项目的代码风格。

## 核心原则

1. **一致性**：在整个项目中保持统一的代码风格
2. **可读性**：代码应该易于阅读和理解
3. **工具支持**：使用工具自动检查和格式化代码
4. **团队协作**：与团队成员统一代码风格

---

## Airbnb JavaScript 风格指南

### 概述

Airbnb JavaScript 风格指南是最流行的 JavaScript 代码风格指南之一，强调现代 JavaScript 语法和最佳实践。

### 核心规则

#### 变量声明

**规则**：优先使用 `const`，需要重新赋值时使用 `let`

```js
// ✅ 推荐
const name = 'Alice';
let age = 20;
age = 21;

// ❌ 不推荐
var name = 'Alice';
```

#### 对象和数组

**规则**：使用对象和数组的解构

```js
// ✅ 推荐
const { name, age } = user;
const [first, second] = items;

// ❌ 不推荐
const name = user.name;
const age = user.age;
```

#### 箭头函数

**规则**：优先使用箭头函数

```js
// ✅ 推荐
const add = (a, b) => a + b;
const users = items.map(item => item.name);

// ❌ 不推荐
const add = function(a, b) {
  return a + b;
};
```

#### 类和构造函数

**规则**：优先使用类语法

```js
// ✅ 推荐
class User {
  constructor(name) {
    this.name = name;
  }
}

// ❌ 不推荐
function User(name) {
  this.name = name;
}
```

### 配置 ESLint

**安装**：

```bash
npm install --save-dev eslint-config-airbnb-base
```

**配置**（`.eslintrc.js`）：

```js
module.exports = {
  extends: 'airbnb-base',
  rules: {
    // 自定义规则
  }
};
```

---

## Google JavaScript 风格指南

### 概述

Google JavaScript 风格指南是 Google 内部使用的 JavaScript 代码风格规范，强调可读性和可维护性。

### 核心规则

#### 命名规范

**规则**：使用描述性的名称

```js
// ✅ 推荐
const userCount = 10;
const isEmailValid = true;

// ❌ 不推荐
const uc = 10;
const flag = true;
```

#### 函数声明

**规则**：优先使用函数声明

```js
// ✅ 推荐
function calculateTotal(items) {
  return items.reduce((sum, item) => sum + item.price, 0);
}

// ❌ 不推荐
const calculateTotal = function(items) {
  return items.reduce((sum, item) => sum + item.price, 0);
};
```

#### 注释

**规则**：使用 JSDoc 注释

```js
/**
 * 计算总价
 * @param {Array<Item>} items - 商品列表
 * @returns {number} 总价
 */
function calculateTotal(items) {
  return items.reduce((sum, item) => sum + item.price, 0);
}
```

### 配置 ESLint

**安装**：

```bash
npm install --save-dev eslint-config-google
```

**配置**（`.eslintrc.js`）：

```js
module.exports = {
  extends: 'google',
  rules: {
    // 自定义规则
  }
};
```

---

## Standard JavaScript 风格指南

### 概述

Standard JavaScript 风格指南是一个"零配置"的代码风格指南，强调简洁性和一致性。

### 核心规则

#### 不使用分号

**规则**：不使用分号（除非必要）

```js
// ✅ 推荐
const name = 'Alice'
const age = 20

// ❌ 不推荐
const name = 'Alice';
const age = 20;
```

#### 使用 2 个空格缩进

**规则**：使用 2 个空格缩进

```js
// ✅ 推荐
function greet(name) {
  console.log(`Hello, ${name}`)
}

// ❌ 不推荐
function greet(name) {
    console.log(`Hello, ${name}`)
}
```

#### 使用单引号

**规则**：使用单引号（除非字符串包含单引号）

```js
// ✅ 推荐
const name = 'Alice'
const message = "It's a beautiful day"

// ❌ 不推荐
const name = "Alice"
```

### 配置 ESLint

**安装**：

```bash
npm install --save-dev eslint-config-standard
```

**配置**（`.eslintrc.js`）：

```js
module.exports = {
  extends: 'standard',
  rules: {
    // 自定义规则
  }
};
```

---

## 风格指南对比

### 主要差异

| 特性              | Airbnb        | Google        | Standard     |
|:------------------|:--------------|:--------------|:-------------|
| **分号**          | 使用          | 使用          | 不使用       |
| **引号**          | 单引号        | 单引号        | 单引号       |
| **缩进**          | 2 个空格      | 2 个空格      | 2 个空格     |
| **函数声明**      | 箭头函数优先  | 函数声明优先  | 函数声明优先 |
| **变量声明**      | const/let     | const/let     | const/let    |
| **对象属性**      | 简写属性      | 简写属性      | 简写属性     |
| **数组方法**      | 优先使用      | 优先使用      | 优先使用     |

### 选择建议

1. **Airbnb**：
   - 适合现代 JavaScript 项目
   - 强调 ES6+ 特性
   - 规则较为严格

2. **Google**：
   - 适合大型项目
   - 强调可读性和可维护性
   - 规则较为宽松

3. **Standard**：
   - 适合快速启动项目
   - 零配置，开箱即用
   - 规则较为简洁

---

## 工具支持

### ESLint

**说明**：使用 ESLint 自动检查代码风格

**安装**：

```bash
npm install --save-dev eslint
```

**配置**（`.eslintrc.js`）：

```js
module.exports = {
  extends: 'airbnb-base',
  rules: {
    // 自定义规则
  }
};
```

### Prettier

**说明**：使用 Prettier 自动格式化代码

**安装**：

```bash
npm install --save-dev prettier
```

**配置**（`.prettierrc`）：

```json
{
  "semi": true,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "es5"
}
```

### EditorConfig

**说明**：使用 EditorConfig 统一编辑器配置

**配置**（`.editorconfig`）：

```ini
root = true

[*]
charset = utf-8
end_of_line = lf
indent_style = space
indent_size = 2
insert_final_newline = true
trim_trailing_whitespace = true
```

---

## 最佳实践

### 1. 选择适合的风格指南

**建议**：根据项目需求选择风格指南

- 新项目：推荐 Airbnb 或 Standard
- 大型项目：推荐 Google
- 快速原型：推荐 Standard

### 2. 使用工具自动检查

**建议**：配置 ESLint 和 Prettier

```json
{
  "scripts": {
    "lint": "eslint .",
    "format": "prettier --write ."
  }
}
```

### 3. 团队协作

**建议**：在项目文档中明确代码风格规范

```markdown
# 代码风格

本项目使用 Airbnb JavaScript 风格指南。

运行 `npm run lint` 检查代码风格。
运行 `npm run format` 格式化代码。
```

### 4. 持续改进

**建议**：根据项目需求调整代码风格

```js
// .eslintrc.js
module.exports = {
  extends: 'airbnb-base',
  rules: {
    // 根据项目需求调整规则
    'no-console': 'warn',
    'max-len': ['error', { code: 120 }]
  }
};
```

---

## 注意事项

1. **一致性**：在整个项目中保持统一的代码风格
2. **工具支持**：使用工具自动检查和格式化代码
3. **团队协作**：与团队成员统一代码风格
4. **文档说明**：在项目文档中明确代码风格规范

---

## 练习

1. **配置 ESLint**：
   - 安装并配置 Airbnb 风格指南
   - 运行 `npm run lint` 检查代码风格

2. **配置 Prettier**：
   - 安装并配置 Prettier
   - 运行 `npm run format` 格式化代码

3. **代码重构**：
   - 根据选择的风格指南重构现有代码
   - 确保代码符合风格规范

---

## 总结

代码风格指南的核心是：

- **一致性**：在整个项目中保持统一的代码风格
- **可读性**：代码应该易于阅读和理解
- **工具支持**：使用工具自动检查和格式化代码

遵循这些规范有助于编写高质量、可维护的 JavaScript 代码。

继续学习下一节：最佳实践与反模式。

---

**最后更新**：2025-12-16
