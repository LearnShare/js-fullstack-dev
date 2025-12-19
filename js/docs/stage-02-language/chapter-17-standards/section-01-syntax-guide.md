# 2.17.1 JavaScript 语法指南

## 概述

JavaScript 语法指南定义了编�?JavaScript 代码时应遵循的基本语法规则，包括变量声明、语句格式、代码组织等。遵循统一的语法规范有助于提高代码可读性和可维护性�?
## 核心原则

1. **一致�?*：在整个项目中保持一致的代码风格
2. **可读�?*：代码应该易于阅读和理解
3. **简洁�?*：避免不必要的复杂�?4. **现代�?*：优先使用现�?JavaScript 语法（ES2015+�?
---

## 变量声明

### 使用 const �?let

**推荐**：优先使�?`const`，需要重新赋值时使用 `let`

```js
// 推荐
const name = 'Alice';
let age = 20;
age = 21;

// 不推�?var name = 'Alice';
var age = 20;
```

**说明**：`const` �?`let` 具有块级作用域，避免变量提升问题�?
### 变量命名

**推荐**：使用有意义的变量名

```js
// 推荐
const userCount = 10;
const isActive = true;
const userName = 'Alice';

// 不推�?const uc = 10;
const flag = true;
const u = 'Alice';
```

---

## 函数声明

### 函数表达�?vs 函数声明

**推荐**：优先使用箭头函数（简单场景）或函数声明（需要提升）

```js
// 推荐：箭头函数（简单场景）
const add = (a, b) => a + b;

// 推荐：函数声明（需要提升）
function calculateTotal(items) {
  return items.reduce((sum, item) => sum + item.price, 0);
}

// 不推荐：函数表达式（除非必要�?const subtract = function(a, b) {
  return a - b;
};
```

### 函数参数

**推荐**：使用默认参数和解构

```js
// 推荐
function greet(name = 'Guest', { age, city } = {}) {
  console.log(`Hello, ${name}! Age: ${age}, City: ${city}`);
}

// 不推�?function greet(name, options) {
  name = name || 'Guest';
  const age = options && options.age;
  const city = options && options.city;
  console.log(`Hello, ${name}! Age: ${age}, City: ${city}`);
}
```

---

## 对象和数�?
### 对象字面�?
**推荐**：使用简写属性和方法

```js
// 推荐
const name = 'Alice';
const user = {
  name,
  age: 20,
  greet() {
    console.log(`Hello, ${this.name}`);
  }
};

// 不推�?const user = {
  name: name,
  age: 20,
  greet: function() {
    console.log(`Hello, ${this.name}`);
  }
};
```

### 数组方法

**推荐**：使用数组方法替代传统循�?
```js
// 推荐
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(n => n * 2);
const sum = numbers.reduce((acc, n) => acc + n, 0);

// 不推�?const doubled = [];
for (let i = 0; i < numbers.length; i++) {
  doubled.push(numbers[i] * 2);
}
```

---

## 条件语句

### if-else

**推荐**：使用早期返回减少嵌�?
```js
// 推荐
function processUser(user) {
  if (!user) {
    return null;
  }
  if (!user.isActive) {
    return null;
  }
  return user.name.toUpperCase();
}

// 不推�?function processUser(user) {
  if (user) {
    if (user.isActive) {
      return user.name.toUpperCase();
    }
  }
  return null;
}
```

### 三元运算�?
**推荐**：简单条件使用三元运算符

```js
// 推荐
const status = isActive ? 'active' : 'inactive';
const message = count > 0 ? `Found ${count} items` : 'No items found';

// 不推荐：复杂条件
const status = isActive ? (isPremium ? 'premium-active' : 'active') : 'inactive';
```

---

## 循环

### for...of

**推荐**：使�?`for...of` 遍历数组

```js
// 推荐
const items = [1, 2, 3, 4, 5];
for (const item of items) {
  console.log(item);
}

// 不推�?for (let i = 0; i < items.length; i++) {
  console.log(items[i]);
}
```

### for...in

**注意**：`for...in` 用于遍历对象，不推荐用于数组

```js
// 推荐：遍历对�?const user = { name: 'Alice', age: 20 };
for (const key in user) {
  console.log(`${key}: ${user[key]}`);
}

// 不推荐：遍历数组
const items = [1, 2, 3];
for (const index in items) {
  console.log(items[index]);
}
```

---

## 类和模块

### 类声�?
**推荐**：使用类语法

```js
// 推荐
class User {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greet() {
    console.log(`Hello, ${this.name}`);
  }
}

// 不推荐：构造函数模�?function User(name, age) {
  this.name = name;
  this.age = age;
}

User.prototype.greet = function() {
  console.log(`Hello, ${this.name}`);
};
```

### 模块导入导出

**推荐**：使�?ES6 模块语法

```js
// 推荐：命名导�?export const PI = 3.14159;
export function calculateArea(radius) {
  return PI * radius * radius;
}

// 推荐：默认导�?export default class User {
  // ...
}

// 推荐：导�?import User, { PI, calculateArea } from './math.js';
```

---

## 异步代码

### async/await

**推荐**：使�?`async/await` 替代 Promise �?
```js
// 推荐
async function fetchUser(id) {
  try {
    const response = await fetch(`/api/users/${id}`);
    const user = await response.json();
    return user;
  } catch (error) {
    console.error('Error fetching user:', error);
    throw error;
  }
}

// 不推荐：Promise �?function fetchUser(id) {
  return fetch(`/api/users/${id}`)
    .then(response => response.json())
    .then(user => user)
    .catch(error => {
      console.error('Error fetching user:', error);
      throw error;
    });
}
```

---

## 代码组织

### 导入顺序

**推荐**：按以下顺序组织导入

```js
// 1. 外部�?import React from 'react';
import lodash from 'lodash';

// 2. 内部模块
import { User } from './models/User';
import { api } from './utils/api';

// 3. 样式文件
import './styles.css';
```

### 代码分组

**推荐**：按功能分组代码

```js
// 常量
const API_URL = 'https://api.example.com';
const MAX_RETRIES = 3;

// 类型定义（TypeScript�?interface User {
  name: string;
  age: number;
}

// 函数
function fetchUser(id: string): Promise<User> {
  // ...
}

// 导出
export { fetchUser, API_URL };
```

---

## 注意事项

1. **严格模式**：在模块和类中自动启用严格模�?2. **分号**：根据团队规范统一使用或不使用分号
3. **引号**：统一使用单引号或双引号（推荐单引号）
4. **缩进**：使�?2 个空格或 4 个空格（推荐 2 个空格）

---

## 最佳实�?
1. **使用现代语法**：优先使�?ES2015+ 特�?2. **保持一致�?*：在整个项目中保持统一的代码风�?3. **工具辅助**：使�?ESLint、Prettier 等工具自动格式化
4. **代码审查**：通过代码审查确保规范执行

---

## 练习

1. **重构代码**�?   - 将使�?`var` 的代码改�?`const`/`let`
   - 将函数表达式改为箭头函数或函数声�?
2. **代码组织**�?   - 按规范组织导入语�?   - 使用早期返回重构嵌套�?if-else

3. **现代语法**�?   - 使用解构和默认参数简化函�?   - 使用数组方法替代传统循环

---

## 总结

JavaScript 语法指南的核心是�?
- **一致�?*：保持统一的代码风�?- **现代�?*：使用现�?JavaScript 语法
- **可读�?*：编写易于理解的代码

遵循这些规范有助于编写高质量、可维护�?JavaScript 代码�?
继续学习下一节：命名规范�?
---

**最后更�?*�?025-12-16
