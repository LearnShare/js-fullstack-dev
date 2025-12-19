# 2.17.4 代码风格指南（Airbnb、Google、Standard�?
## 概述

代码风格指南定义�?JavaScript 代码的格式和风格规范。主流的代码风格指南包括 Airbnb、Google �?Standard。了解这些指南有助于选择适合项目的代码风格�?
## 核心原则

1. **一致�?*：在整个项目中保持统一的代码风�?2. **可读�?*：代码应该易于阅读和理解
3. **工具支持**：使用工具自动检查和格式化代�?4. **团队协作**：与团队成员统一代码风格

---

## Airbnb JavaScript 风格指南

### 概述

Airbnb JavaScript 风格指南是最流行�?JavaScript 代码风格指南之一，强调现�?JavaScript 语法和最佳实践�?
### 核心规则

#### 变量声明

**规则**：优先使�?`const`，需要重新赋值时使用 `let`

```js
// �?推荐
const name = 'Alice';
let age = 20;
age = 21;

// �?不推�?var name = 'Alice';
```

#### 对象和数�?
**规则**：使用对象和数组的解�?
```js
// �?推荐
const { name, age } = user;
const [first, second] = items;

// �?不推�?const name = user.name;
const age = user.age;
```

#### 箭头函数

**规则**：优先使用箭头函�?
```js
// �?推荐
const add = (a, b) => a + b;
const users = items.map(item => item.name);

// �?不推�?const add = function(a, b) {
  return a + b;
};
```

#### 类和构造函�?
**规则**：优先使用类语法

```js
// �?推荐
class User {
  constructor(name) {
    this.name = name;
  }
}

// �?不推�?function User(name) {
  this.name = name;
}
```

### 配置 ESLint

**安装**�?
```bash
npm install --save-dev eslint-config-airbnb-base
```

**配置**（`.eslintrc.js`）：

```js
module.exports = {
  extends: 'airbnb-base',
  rules: {
    // 自定义规�?  }
};
```

---

## Google JavaScript 风格指南

### 概述

Google JavaScript 风格指南�?Google 内部使用�?JavaScript 代码风格规范，强调可读性和可维护性�?
### 核心规则

#### 命名规范

**规则**：使用描述性的名称

```js
// �?推荐
const userCount = 10;
const isEmailValid = true;

// �?不推�?const uc = 10;
const flag = true;
```

#### 函数声明

**规则**：优先使用函数声�?
```js
// �?推荐
function calculateTotal(items) {
  return items.reduce((sum, item) => sum + item.price, 0);
}

// �?不推�?const calculateTotal = function(items) {
  return items.reduce((sum, item) => sum + item.price, 0);
};
```

#### 注释

**规则**：使�?JSDoc 注释

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

**安装**�?
```bash
npm install --save-dev eslint-config-google
```

**配置**（`.eslintrc.js`）：

```js
module.exports = {
  extends: 'google',
  rules: {
    // 自定义规�?  }
};
```

---

## Standard JavaScript 风格指南

### 概述

Standard JavaScript 风格指南是一�?零配�?的代码风格指南，强调简洁性和一致性�?
### 核心规则

#### 不使用分�?
**规则**：不使用分号（除非必要）

```js
// �?推荐
const name = 'Alice'
const age = 20

// �?不推�?const name = 'Alice';
const age = 20;
```

#### 使用 2 个空格缩�?
**规则**：使�?2 个空格缩�?
```js
// �?推荐
function greet(name) {
  console.log(`Hello, ${name}`)
}

// �?不推�?function greet(name) {
    console.log(`Hello, ${name}`)
}
```

#### 使用单引�?
**规则**：使用单引号（除非字符串包含单引号）

```js
// �?推荐
const name = 'Alice'
const message = "It's a beautiful day"

// �?不推�?const name = "Alice"
```

### 配置 ESLint

**安装**�?
```bash
npm install --save-dev eslint-config-standard
```

**配置**（`.eslintrc.js`）：

```js
module.exports = {
  extends: 'standard',
  rules: {
    // 自定义规�?  }
};
```

---

## 风格指南对比

### 主要差异

| 特�?             | Airbnb        | Google        | Standard     |
|:------------------|:--------------|:--------------|:-------------|
| **分号**          | 使用          | 使用          | 不使�?      |
| **引号**          | 单引�?       | 单引�?       | 单引�?      |
| **缩进**          | 2 个空�?     | 2 个空�?     | 2 个空�?    |
| **函数声明**      | 箭头函数优先  | 函数声明优先  | 函数声明优先 |
| **变量声明**      | const/let     | const/let     | const/let    |
| **对象属�?*      | 简写属�?     | 简写属�?     | 简写属�?    |
| **数组方法**      | 优先使用      | 优先使用      | 优先使用     |

### 选择建议

1. **Airbnb**�?   - 适合现代 JavaScript 项目
   - 强调 ES6+ 特�?   - 规则较为严格

2. **Google**�?   - 适合大型项目
   - 强调可读性和可维护�?   - 规则较为宽松

3. **Standard**�?   - 适合快速启动项�?   - 零配置，开箱即�?   - 规则较为简�?
---

## 工具支持

### ESLint

**说明**：使�?ESLint 自动检查代码风�?
**安装**�?
```bash
npm install --save-dev eslint
```

**配置**（`.eslintrc.js`）：

```js
module.exports = {
  extends: 'airbnb-base',
  rules: {
    // 自定义规�?  }
};
```

### Prettier

**说明**：使�?Prettier 自动格式化代�?
**安装**�?
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

**说明**：使�?EditorConfig 统一编辑器配�?
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

## 最佳实�?
### 1. 选择适合的风格指�?
**建议**：根据项目需求选择风格指南

- 新项目：推荐 Airbnb �?Standard
- 大型项目：推�?Google
- 快速原型：推荐 Standard

### 2. 使用工具自动检�?
**建议**：配�?ESLint �?Prettier

```json
{
  "scripts": {
    "lint": "eslint .",
    "format": "prettier --write ."
  }
}
```

### 3. 团队协作

**建议**：在项目文档中明确代码风格规�?
```markdown
# 代码风格

本项目使�?Airbnb JavaScript 风格指南�?
运行 `npm run lint` 检查代码风格�?运行 `npm run format` 格式化代码�?```

### 4. 持续改进

**建议**：根据项目需求调整代码风�?
```js
// .eslintrc.js
module.exports = {
  extends: 'airbnb-base',
  rules: {
    // 根据项目需求调整规�?    'no-console': 'warn',
    'max-len': ['error', { code: 120 }]
  }
};
```

---

## 注意事项

1. **一致�?*：在整个项目中保持统一的代码风�?2. **工具支持**：使用工具自动检查和格式化代�?3. **团队协作**：与团队成员统一代码风格
4. **文档说明**：在项目文档中明确代码风格规�?
---

## 练习

1. **配置 ESLint**�?   - 安装并配�?Airbnb 风格指南
   - 运行 `npm run lint` 检查代码风�?
2. **配置 Prettier**�?   - 安装并配�?Prettier
   - 运行 `npm run format` 格式化代�?
3. **代码重构**�?   - 根据选择的风格指南重构现有代�?   - 确保代码符合风格规范

---

## 总结

代码风格指南的核心是�?
- **一致�?*：在整个项目中保持统一的代码风�?- **可读�?*：代码应该易于阅读和理解
- **工具支持**：使用工具自动检查和格式化代�?
遵循这些规范有助于编写高质量、可维护�?JavaScript 代码�?
继续学习下一节：最佳实践与反模式�?
---

**最后更�?*�?025-12-16
