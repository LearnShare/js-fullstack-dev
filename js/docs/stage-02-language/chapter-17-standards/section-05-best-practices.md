# 2.17.5 最佳实践与反模�?
## 概述

最佳实践与反模式介绍了 JavaScript 开发中的最佳实践和常见反模式。了解这些内容有助于编写高质量、可维护�?JavaScript 代码�?
## 核心原则

1. **可读�?*：代码应该易于阅读和理解
2. **可维护�?*：代码应该易于维护和扩展
3. **性能**：代码应该具有良好的性能
4. **安全�?*：代码应该安全可�?
---

## 最佳实�?
### 1. 使用现代 JavaScript 语法

**推荐**：使�?ES2015+ 特�?
```js
// �?推荐：使�?const/let
const name = 'Alice';
let age = 20;

// �?不推荐：使用 var
var name = 'Alice';
var age = 20;
```

**推荐**：使用箭头函�?
```js
// �?推荐
const add = (a, b) => a + b;
const users = items.map(item => item.name);

// �?不推�?const add = function(a, b) {
  return a + b;
};
```

**推荐**：使用解�?
```js
// �?推荐
const { name, age } = user;
const [first, second] = items;

// �?不推�?const name = user.name;
const age = user.age;
```

### 2. 避免全局变量

**推荐**：使用模块化

```js
// �?推荐：使用模�?export const API_URL = 'https://api.example.com';
export function fetchUser(id) {
  // ...
}

// �?不推荐：使用全局变量
window.API_URL = 'https://api.example.com';
window.fetchUser = function(id) {
  // ...
};
```

### 3. 使用严格模式

**推荐**：在文件顶部使用严格模式

```js
// �?推荐
'use strict';

function example() {
  // ...
}
```

**注意**：ES6 模块和类自动启用严格模式�?
### 4. 错误处理

**推荐**：使�?try-catch 处理错误

```js
// �?推荐
async function fetchUser(id) {
  try {
    const response = await fetch(`/api/users/${id}`);
    if (!response.ok) {
      throw new Error('Failed to fetch user');
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching user:', error);
    throw error;
  }
}

// �?不推荐：忽略错误
async function fetchUser(id) {
  const response = await fetch(`/api/users/${id}`);
  return await response.json();
}
```

### 5. 避免魔法数字和字符串

**推荐**：使用常�?
```js
// �?推荐
const MAX_RETRIES = 3;
const DEFAULT_TIMEOUT = 5000;
const STATUS_ACTIVE = 'active';

if (user.status === STATUS_ACTIVE) {
  // ...
}

// �?不推荐：使用魔法数字和字符串
if (user.status === 'active') {
  // ...
}
```

### 6. 使用有意义的变量�?
**推荐**：使用描述性的名称

```js
// �?推荐
const userCount = 10;
const isEmailValid = true;
const maxRetries = 3;

// �?不推�?const uc = 10;
const flag = true;
const mr = 3;
```

### 7. 避免深度嵌套

**推荐**：使用早期返�?
```js
// �?推荐
function processUser(user) {
  if (!user) {
    return null;
  }
  if (!user.isActive) {
    return null;
  }
  return user.name.toUpperCase();
}

// �?不推荐：深度嵌套
function processUser(user) {
  if (user) {
    if (user.isActive) {
      return user.name.toUpperCase();
    }
  }
  return null;
}
```

### 8. 使用数组方法

**推荐**：使用数组方法替代传统循�?
```js
// �?推荐
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(n => n * 2);
const sum = numbers.reduce((acc, n) => acc + n, 0);

// �?不推荐：传统循环
const doubled = [];
for (let i = 0; i < numbers.length; i++) {
  doubled.push(numbers[i] * 2);
}
```

---

## 反模�?
### 1. 使用 var 声明变量

**问题**：`var` 具有函数作用域，容易导致变量提升问题

```js
// �?反模�?for (var i = 0; i < 3; i++) {
  setTimeout(() => {
    console.log(i); // 输出 3, 3, 3
  }, 100);
}

// �?正确做法
for (let i = 0; i < 3; i++) {
  setTimeout(() => {
    console.log(i); // 输出 0, 1, 2
  }, 100);
}
```

### 2. 使用 == 进行比较

**问题**：`==` 会进行类型转换，容易导致意外结果

```js
// �?反模�?if (value == 0) {
  // �?value �?0, '0', false 时都会匹�?}

// �?正确做法
if (value === 0) {
  // 只有�?value 严格等于 0 时才会匹�?}
```

### 3. 修改原型

**问题**：修改内置对象原型会影响所有实�?
```js
// �?反模�?Array.prototype.last = function() {
  return this[this.length - 1];
};

// �?正确做法：使用工具函�?function last(array) {
  return array[array.length - 1];
}
```

### 4. 使用 eval()

**问题**：`eval()` 会执行任意代码，存在安全风险

```js
// �?反模�?const code = 'console.log("Hello")';
eval(code);

// �?正确做法：避免使�?eval()
// 使用其他方式实现需�?```

### 5. 忽略错误

**问题**：忽略错误会导致难以调试的问�?
```js
// �?反模�?try {
  riskyOperation();
} catch (error) {
  // 忽略错误
}

// �?正确做法
try {
  riskyOperation();
} catch (error) {
  console.error('Error:', error);
  // 处理错误或重新抛�?  throw error;
}
```

### 6. 使用 document.write()

**问题**：`document.write()` 会阻塞页面渲�?
```js
// �?反模�?document.write('<script src="app.js"></script>');

// �?正确做法
const script = document.createElement('script');
script.src = 'app.js';
document.head.appendChild(script);
```

### 7. 使用 innerHTML 插入用户内容

**问题**：容易导�?XSS 攻击

```js
// �?反模�?element.innerHTML = userInput; // 危险�?
// �?正确做法
element.textContent = userInput; // 安全
// 或使�?DOMPurify 等库清理 HTML
```

### 8. 使用全局变量

**问题**：全局变量容易导致命名冲突

```js
// �?反模�?function createUser() {
  name = 'Alice'; // 创建全局变量
}

// �?正确做法
function createUser() {
  const name = 'Alice'; // 局部变�?}
```

---

## 性能优化

### 1. 避免不必要的计算

**推荐**：缓存计算结�?
```js
// �?推荐
function expensiveCalculation() {
  if (!expensiveCalculation.cache) {
    expensiveCalculation.cache = computeExpensiveValue();
  }
  return expensiveCalculation.cache;
}

// �?不推荐：每次都重新计�?function expensiveCalculation() {
  return computeExpensiveValue();
}
```

### 2. 使用事件委托

**推荐**：使用事件委托减少事件监听器

```js
// �?推荐
document.addEventListener('click', (event) => {
  if (event.target.matches('.button')) {
    handleClick(event);
  }
});

// �?不推荐：为每个元素添加监听器
document.querySelectorAll('.button').forEach(button => {
  button.addEventListener('click', handleClick);
});
```

### 3. 避免频繁�?DOM 操作

**推荐**：批量更�?DOM

```js
// �?推荐
const fragment = document.createDocumentFragment();
items.forEach(item => {
  const li = document.createElement('li');
  li.textContent = item.name;
  fragment.appendChild(li);
});
list.appendChild(fragment);

// �?不推荐：频繁更新 DOM
items.forEach(item => {
  const li = document.createElement('li');
  li.textContent = item.name;
  list.appendChild(li);
});
```

---

## 安全�?
### 1. 防止 XSS 攻击

**推荐**：使�?`textContent` 或清�?HTML

```js
// �?推荐
element.textContent = userInput;

// 或使�?DOMPurify
import DOMPurify from 'dompurify';
element.innerHTML = DOMPurify.sanitize(userInput);
```

### 2. 防止 CSRF 攻击

**推荐**：使�?CSRF Token

```js
// �?推荐
fetch('/api/users', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-CSRF-Token': getCsrfToken()
  },
  body: JSON.stringify(data)
});
```

### 3. 验证用户输入

**推荐**：始终验证用户输�?
```js
// �?推荐
function validateEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

function createUser(userData) {
  if (!validateEmail(userData.email)) {
    throw new Error('Invalid email');
  }
  // ...
}
```

---

## 注意事项

1. **代码审查**：通过代码审查发现反模�?2. **工具辅助**：使�?ESLint 等工具检查代�?3. **持续学习**：关�?JavaScript 最佳实践的发展
4. **团队协作**：与团队成员分享最佳实�?
---

## 练习

1. **重构代码**�?   - 将使�?`var` 的代码改�?`const`/`let`
   - 将使�?`==` 的比较改�?`===`
   - 使用早期返回减少嵌套

2. **性能优化**�?   - 使用事件委托优化事件处理
   - 批量更新 DOM 减少重排

3. **安全�?*�?   - 验证用户输入
   - 防止 XSS 攻击

---

## 总结

最佳实践与反模式的核心是：

- **可读�?*：代码应该易于阅读和理解
- **可维护�?*：代码应该易于维护和扩展
- **性能**：代码应该具有良好的性能
- **安全�?*：代码应该安全可�?
遵循这些最佳实践，避免反模式，有助于编写高质量、可维护�?JavaScript 代码�?
完成阶段二学习后，继续学习阶段三：异步编程�?
---

**最后更�?*�?025-12-16
