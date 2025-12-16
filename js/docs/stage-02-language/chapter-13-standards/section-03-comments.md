# 2.13.3 注释规范（JSDoc）

## 概述

注释规范定义了 JavaScript 代码中注释的编写规则，包括单行注释、多行注释和 JSDoc 注释。良好的注释能够帮助开发者理解代码的意图和用法。

## 核心原则

1. **必要性**：只注释必要的代码，避免过度注释
2. **准确性**：注释应该准确描述代码的行为
3. **及时性**：代码修改时同步更新注释
4. **清晰性**：使用清晰、简洁的语言

---

## 注释类型

### 单行注释

**推荐**：使用 `//` 进行单行注释

```js
// 计算用户总数
const totalUsers = users.length;

// 验证邮箱格式
if (!isValidEmail(email)) {
  return false;
}
```

### 多行注释

**推荐**：使用 `/* */` 进行多行注释

```js
/*
 * 这是一个复杂的算法
 * 用于计算用户推荐分数
 * 基于多个因素：活跃度、互动次数等
 */
function calculateRecommendationScore(user) {
  // ...
}
```

---

## JSDoc 注释

### 概述

JSDoc 是一种用于 JavaScript 的文档注释标准，能够生成 API 文档并提供 IDE 智能提示。

### 基本语法

**推荐**：使用 JSDoc 注释函数、类和方法

```js
/**
 * 获取用户信息
 * @param {string} id - 用户 ID
 * @returns {Promise<User>} 用户对象
 */
async function getUser(id) {
  // ...
}
```

### 常用标签

#### @param

**说明**：描述函数参数

```js
/**
 * 计算两个数的和
 * @param {number} a - 第一个数
 * @param {number} b - 第二个数
 * @returns {number} 两数之和
 */
function add(a, b) {
  return a + b;
}
```

#### @returns

**说明**：描述函数返回值

```js
/**
 * 验证邮箱格式
 * @param {string} email - 邮箱地址
 * @returns {boolean} 是否为有效邮箱
 */
function isValidEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}
```

#### @throws

**说明**：描述可能抛出的错误

```js
/**
 * 获取用户信息
 * @param {string} id - 用户 ID
 * @returns {Promise<User>} 用户对象
 * @throws {Error} 当用户不存在时抛出错误
 */
async function getUser(id) {
  const user = await db.findUser(id);
  if (!user) {
    throw new Error('User not found');
  }
  return user;
}
```

#### @example

**说明**：提供使用示例

```js
/**
 * 格式化日期
 * @param {Date} date - 日期对象
 * @param {string} format - 格式字符串
 * @returns {string} 格式化后的日期字符串
 * @example
 * formatDate(new Date(), 'YYYY-MM-DD')
 * // => '2025-12-16'
 */
function formatDate(date, format) {
  // ...
}
```

#### @description

**说明**：详细描述（可选，第一行默认作为描述）

```js
/**
 * 这是一个复杂的函数
 * @description 该函数用于处理用户数据，包括验证、转换和存储
 * @param {User} user - 用户对象
 * @returns {Promise<void>}
 */
async function processUser(user) {
  // ...
}
```

---

## 类和方法的注释

### 类注释

**推荐**：使用 JSDoc 注释类

```js
/**
 * 用户类
 * @class
 */
class User {
  /**
   * 创建用户实例
   * @param {string} name - 用户名
   * @param {number} age - 年龄
   */
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  /**
   * 获取用户信息
   * @returns {string} 用户信息字符串
   */
  getInfo() {
    return `${this.name} (${this.age})`;
  }
}
```

### 方法注释

**推荐**：为公共方法添加 JSDoc 注释

```js
class UserService {
  /**
   * 获取用户列表
   * @param {Object} options - 查询选项
   * @param {number} [options.page=1] - 页码
   * @param {number} [options.limit=10] - 每页数量
   * @returns {Promise<User[]>} 用户列表
   */
  async getUsers(options = {}) {
    const { page = 1, limit = 10 } = options;
    // ...
  }
}
```

---

## 类型定义

### 基本类型

**说明**：JSDoc 支持多种类型

```js
/**
 * @param {string} name - 字符串类型
 * @param {number} age - 数字类型
 * @param {boolean} isActive - 布尔类型
 * @param {Object} user - 对象类型
 * @param {Array} items - 数组类型
 * @param {Function} callback - 函数类型
 */
function example(name, age, isActive, user, items, callback) {
  // ...
}
```

### 联合类型

**说明**：使用 `|` 表示联合类型

```js
/**
 * @param {string|number} id - 用户 ID（字符串或数字）
 * @returns {User|null} 用户对象或 null
 */
function getUser(id) {
  // ...
}
```

### 可选参数

**说明**：使用 `[]` 表示可选参数

```js
/**
 * @param {string} name - 用户名
 * @param {number} [age] - 年龄（可选）
 * @param {Object} [options={}] - 选项（可选，默认空对象）
 */
function createUser(name, age, options = {}) {
  // ...
}
```

### 对象类型

**说明**：使用对象字面量定义对象类型

```js
/**
 * @param {Object} user - 用户对象
 * @param {string} user.name - 用户名
 * @param {number} user.age - 年龄
 * @param {boolean} [user.isActive=true] - 是否激活
 */
function updateUser(user) {
  // ...
}
```

### 数组类型

**说明**：使用 `Array<Type>` 或 `Type[]` 定义数组类型

```js
/**
 * @param {Array<string>} names - 名称数组
 * @param {number[]} scores - 分数数组
 * @returns {Promise<User[]>} 用户对象数组
 */
async function createUsers(names, scores) {
  // ...
}
```

---

## 注释最佳实践

### 1. 注释复杂逻辑

**推荐**：为复杂算法和业务逻辑添加注释

```js
// 使用二分查找算法查找目标值
function binarySearch(arr, target) {
  let left = 0;
  let right = arr.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (arr[mid] === target) {
      return mid;
    } else if (arr[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return -1;
}
```

### 2. 注释 TODO 和 FIXME

**推荐**：使用 TODO 和 FIXME 标记待办事项

```js
// TODO: 优化性能，使用缓存
function fetchUser(id) {
  // ...
}

// FIXME: 修复边界情况处理
function calculateTotal(items) {
  // ...
}
```

### 3. 避免过度注释

**不推荐**：为显而易见的代码添加注释

```js
// 不推荐
const name = 'Alice'; // 设置用户名为 Alice
const age = 20; // 设置年龄为 20

// 推荐
const name = 'Alice';
const age = 20;
```

### 4. 保持注释更新

**重要**：代码修改时同步更新注释

```js
// 错误：注释与代码不一致
/**
 * 获取用户列表
 * @returns {Array} 用户数组
 */
function getUsers() {
  return fetch('/api/users').then(res => res.json());
  // 实际返回的是 Promise，不是 Array
}

// 正确
/**
 * 获取用户列表
 * @returns {Promise<User[]>} 用户数组的 Promise
 */
async function getUsers() {
  const res = await fetch('/api/users');
  return res.json();
}
```

---

## 工具支持

### IDE 支持

大多数现代 IDE（VS Code、WebStorm 等）都支持 JSDoc，能够提供：

- 智能提示
- 类型检查
- 文档生成

### 文档生成工具

可以使用以下工具生成 API 文档：

- **JSDoc**：官方文档生成工具
- **TypeDoc**：TypeScript 文档生成工具
- **ESDoc**：ES6+ 文档生成工具

---

## 注意事项

1. **一致性**：在整个项目中保持统一的注释风格
2. **准确性**：确保注释准确描述代码行为
3. **及时性**：代码修改时同步更新注释
4. **简洁性**：避免冗长的注释

---

## 练习

1. **JSDoc 注释**：
   - 为以下函数添加完整的 JSDoc 注释：
     ```js
     function calculateTotal(items, discount = 0) {
       const sum = items.reduce((acc, item) => acc + item.price, 0);
       return sum * (1 - discount);
     }
     ```

2. **类型定义**：
   - 为以下函数添加类型定义：
     ```js
     function processUsers(users, filter, callback) {
       const filtered = users.filter(filter);
       filtered.forEach(callback);
     }
     ```

3. **类注释**：
   - 为以下类添加完整的 JSDoc 注释：
     ```js
     class UserService {
       constructor(apiClient) {
         this.api = apiClient;
       }
       async getUser(id) {
         return this.api.get(`/users/${id}`);
       }
     }
     ```

---

## 总结

注释规范的核心是：

- **必要性**：只注释必要的代码
- **准确性**：注释应该准确描述代码行为
- **清晰性**：使用清晰、简洁的语言

遵循这些规范有助于编写高质量、可维护的 JavaScript 代码。

继续学习下一节：代码风格指南。

---

**最后更新**：2025-12-16
