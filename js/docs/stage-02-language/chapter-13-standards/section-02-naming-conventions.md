# 2.13.2 命名规范（变量、函数、类）

## 概述

命名规范定义了 JavaScript 代码中变量、函数、类等标识符的命名规则。良好的命名规范能够提高代码可读性，降低维护成本。

## 核心原则

1. **描述性**：名称应该清晰描述其用途
2. **一致性**：在整个项目中保持一致的命名风格
3. **简洁性**：避免过长的名称，但不要过度缩写
4. **可读性**：使用易于理解的单词和短语

---

## 变量命名

### 基本规则

**推荐**：使用驼峰命名法（camelCase）

```js
// 推荐
const userName = 'Alice';
const userCount = 10;
const isActive = true;
const maxRetries = 3;

// 不推荐
const user_name = 'Alice';
const UserCount = 10;
const IS_ACTIVE = true;
```

### 布尔值命名

**推荐**：使用 `is`、`has`、`can`、`should` 等前缀

```js
// 推荐
const isActive = true;
const hasPermission = false;
const canEdit = true;
const shouldValidate = false;

// 不推荐
const active = true;
const permission = false;
```

### 常量命名

**推荐**：使用全大写字母，单词间用下划线分隔

```js
// 推荐
const MAX_RETRIES = 3;
const API_BASE_URL = 'https://api.example.com';
const DEFAULT_TIMEOUT = 5000;

// 不推荐
const maxRetries = 3;
const apiBaseUrl = 'https://api.example.com';
```

### 私有变量

**推荐**：使用下划线前缀表示私有变量（约定）

```js
// 推荐
class User {
  constructor(name) {
    this.name = name;
    this._internalId = generateId();
  }
}

// 不推荐：没有明确标识私有变量
class User {
  constructor(name) {
    this.name = name;
    this.internalId = generateId();
  }
}
```

---

## 函数命名

### 基本规则

**推荐**：使用驼峰命名法，动词开头

```js
// 推荐
function getUserById(id) {
  // ...
}

function calculateTotal(items) {
  // ...
}

function validateEmail(email) {
  // ...
}

// 不推荐
function get_user_by_id(id) {
  // ...
}

function UserById(id) {
  // ...
}
```

### 常见动词前缀

| 前缀      | 含义           | 示例                    |
|:----------|:---------------|:------------------------|
| `get`     | 获取           | `getUser()`             |
| `set`     | 设置           | `setName()`             |
| `is`      | 判断           | `isValid()`             |
| `has`     | 检查存在       | `hasPermission()`       |
| `can`     | 检查能力       | `canEdit()`             |
| `should`  | 是否应该       | `shouldValidate()`      |
| `create`  | 创建           | `createUser()`          |
| `update`  | 更新           | `updateUser()`          |
| `delete`  | 删除           | `deleteUser()`          |
| `find`    | 查找           | `findUser()`            |
| `calculate` | 计算        | `calculateTotal()`      |
| `validate` | 验证          | `validateEmail()`       |
| `handle`  | 处理           | `handleClick()`         |
| `render`  | 渲染           | `renderUser()`          |

### 事件处理函数

**推荐**：使用 `handle` 前缀

```js
// 推荐
function handleClick(event) {
  // ...
}

function handleSubmit(event) {
  // ...
}

// 不推荐
function onClick(event) {
  // ...
}

function submit(event) {
  // ...
}
```

### 异步函数

**推荐**：使用 `async` 或 `fetch` 等明确表示异步

```js
// 推荐
async function fetchUser(id) {
  // ...
}

async function loadData() {
  // ...
}

// 不推荐
function getUser(id) {
  return fetch(`/api/users/${id}`);
}
```

---

## 类命名

### 基本规则

**推荐**：使用帕斯卡命名法（PascalCase）

```js
// 推荐
class User {
  // ...
}

class UserService {
  // ...
}

class HttpRequest {
  // ...
}

// 不推荐
class user {
  // ...
}

class user_service {
  // ...
}
```

### 接口和类型（TypeScript）

**推荐**：使用帕斯卡命名法，接口使用 `I` 前缀（可选）

```typescript
// 推荐：接口
interface User {
  name: string;
  age: number;
}

// 推荐：类型别名
type UserId = string;
type UserList = User[];

// 可选：使用 I 前缀
interface IUser {
  name: string;
  age: number;
}
```

---

## 文件命名

### 基本规则

**推荐**：使用小写字母和连字符（kebab-case）

```js
// 推荐
user-service.js
user-model.js
api-client.js

// 不推荐
UserService.js
user_model.js
apiClient.js
```

### 组件文件（React）

**推荐**：使用帕斯卡命名法

```js
// 推荐
UserProfile.jsx
UserList.jsx
NavigationBar.jsx

// 不推荐
user-profile.jsx
user_list.jsx
```

---

## 命名约定对比

### 不同场景的命名风格

| 场景           | 命名风格      | 示例                |
|:---------------|:--------------|:--------------------|
| 变量、函数     | camelCase     | `userName`, `getUser()` |
| 类、接口       | PascalCase    | `User`, `UserService` |
| 常量           | UPPER_SNAKE_CASE | `MAX_RETRIES`, `API_URL` |
| 文件           | kebab-case    | `user-service.js`   |
| 组件文件       | PascalCase    | `UserProfile.jsx`    |
| 私有变量       | _camelCase    | `_internalId`       |

---

## 命名最佳实践

### 1. 使用有意义的名称

```js
// 推荐
const userCount = 10;
const isEmailValid = true;

// 不推荐
const uc = 10;
const flag = true;
```

### 2. 避免缩写（除非是常见缩写）

```js
// 推荐
const userCount = 10;
const httpRequest = new HttpRequest();

// 不推荐
const usrCnt = 10;
const httpReq = new HttpRequest();
```

### 3. 使用复数表示数组或集合

```js
// 推荐
const users = [];
const items = [];

// 不推荐
const user = [];
const item = [];
```

### 4. 避免使用保留字

```js
// 不推荐
const class = 'active';
const function = 'handler';

// 推荐
const className = 'active';
const handler = 'handler';
```

---

## 注意事项

1. **一致性**：在整个项目中保持统一的命名风格
2. **团队规范**：遵循团队的命名约定
3. **工具辅助**：使用 ESLint 规则检查命名规范
4. **文档说明**：在项目文档中明确命名规范

---

## 练习

1. **变量命名**：
   - 将以下变量改为符合规范的名称：
     - `usr_nm` → `userName`
     - `cnt` → `count`
     - `flag` → `isActive`

2. **函数命名**：
   - 为以下函数选择合适的前缀：
     - `user(id)` → `getUser(id)` 或 `findUser(id)`
     - `check(email)` → `validateEmail(email)`
     - `click(event)` → `handleClick(event)`

3. **类命名**：
   - 将以下类名改为符合规范的名称：
     - `user` → `User`
     - `user_service` → `UserService`
     - `httpRequest` → `HttpRequest`

---

## 总结

命名规范的核心是：

- **描述性**：名称应该清晰描述其用途
- **一致性**：在整个项目中保持统一的命名风格
- **可读性**：使用易于理解的单词和短语

遵循这些规范有助于编写高质量、可维护的 JavaScript 代码。

继续学习下一节：注释规范。

---

**最后更新**：2025-12-16
