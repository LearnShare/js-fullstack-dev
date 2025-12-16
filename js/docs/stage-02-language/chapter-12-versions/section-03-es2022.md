# 2.12.3 ES2022 新特性

## 概述

ES2022（ES13）是 ECMAScript 2022 标准，于 2022 年 6 月发布。ES2022 引入了类字段、私有字段和方法、顶层 await、Error.cause 等特性，进一步完善了 JavaScript 的面向对象编程能力和错误处理机制。

## 核心特性

ES2022 主要包含以下新特性：

1. **类字段声明**：公共和私有实例字段、静态字段
2. **私有方法和访问器**：私有方法、私有 getter/setter
3. **顶层 await**：在模块顶层使用 await
4. **Error.cause**：错误链式追踪
5. **Array.prototype.at()**：使用负索引访问数组元素
6. **Object.hasOwn()**：更安全的属性检查方法

---

## 类字段声明

### 概述

ES2022 允许在类中直接声明字段，无需在构造函数中初始化。支持公共字段、私有字段和静态字段。

### 公共实例字段

**语法格式**：
```js
class MyClass {
  publicField = value;
}
```

**示例**：

```js
class User {
  name = 'Anonymous';
  age = 0;

  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
}

const user = new User('John', 30);
console.log(user.name); // 'John'
console.log(user.age);  // 30
```

**输出说明**：字段可以在类体中直接声明，也可以在构造函数中重新赋值。

### 私有实例字段

**语法格式**：使用 `#` 前缀声明私有字段

```js
class MyClass {
  #privateField = value;
}
```

**示例**：

```js
class Counter {
  #count = 0; // 私有字段

  increment() {
    this.#count++;
    return this.#count;
  }

  getCount() {
    return this.#count;
  }
}

const counter = new Counter();
console.log(counter.increment()); // 1
console.log(counter.getCount());  // 1
// console.log(counter.#count);   // SyntaxError: 无法访问私有字段
```

**输出说明**：
- 私有字段只能在类内部访问
- 外部访问会抛出 `SyntaxError`

### 静态字段

**语法格式**：
```js
class MyClass {
  static staticField = value;
  static #privateStaticField = value;
}
```

**示例**：

```js
class MathUtils {
  static PI = 3.14159;
  static #secret = 'hidden';

  static getSecret() {
    return this.#secret;
  }
}

console.log(MathUtils.PI);           // 3.14159
console.log(MathUtils.getSecret());  // 'hidden'
// console.log(MathUtils.#secret);   // SyntaxError
```

**输出说明**：
- 静态字段通过类名访问
- 私有静态字段只能在类内部访问

### 字段初始化顺序

字段按照在类中声明的顺序初始化：

```js
class Example {
  a = this.b;  // undefined（b 还未初始化）
  b = 2;
  c = this.b;  // 2（b 已初始化）
}

const ex = new Example();
console.log(ex.a); // undefined
console.log(ex.b); // 2
console.log(ex.c); // 2
```

**输出说明**：字段按声明顺序初始化，访问未初始化的字段返回 `undefined`。

### 注意事项

1. **私有字段不可访问**：私有字段无法通过反射或外部代码访问
2. **必须声明**：私有字段必须在类体中声明，不能在外部动态添加
3. **性能考虑**：私有字段的实现可能比公共字段稍慢，但差异通常可忽略

### 常见错误

**错误 1**：尝试在类外部访问私有字段

```js
class MyClass {
  #private = 'secret';
}

const obj = new MyClass();
// ❌ 错误：SyntaxError
console.log(obj.#private);

// ✅ 正确：通过公共方法访问
class MyClass {
  #private = 'secret';
  getPrivate() {
    return this.#private;
  }
}
```

---

## 私有方法和访问器

### 概述

ES2022 支持私有方法和私有访问器（getter/setter），使用 `#` 前缀声明。

### 私有方法

**语法格式**：
```js
class MyClass {
  #privateMethod() {
    // 方法体
  }
}
```

**示例**：

```js
class BankAccount {
  #balance = 0;

  deposit(amount) {
    this.#validateAmount(amount);
    this.#balance += amount;
  }

  #validateAmount(amount) {
    if (amount <= 0) {
      throw new Error('Amount must be positive');
    }
  }

  getBalance() {
    return this.#balance;
  }
}

const account = new BankAccount();
account.deposit(100);
console.log(account.getBalance()); // 100
// account.#validateAmount(50); // SyntaxError
```

**输出说明**：私有方法只能在类内部调用，外部调用会抛出 `SyntaxError`。

### 私有访问器

**语法格式**：
```js
class MyClass {
  get #privateGetter() {
    return value;
  }

  set #privateSetter(value) {
    // 设置逻辑
  }
}
```

**示例**：

```js
class Temperature {
  #celsius = 0;

  get #fahrenheit() {
    return this.#celsius * 9/5 + 32;
  }

  set #fahrenheit(value) {
    this.#celsius = (value - 32) * 5/9;
  }

  setCelsius(c) {
    this.#celsius = c;
  }

  getCelsius() {
    return this.#celsius;
  }

  setFahrenheit(f) {
    this.#fahrenheit = f;
  }

  getFahrenheit() {
    return this.#fahrenheit;
  }
}

const temp = new Temperature();
temp.setCelsius(25);
console.log(temp.getFahrenheit()); // 77
```

**输出说明**：私有访问器只能在类内部使用，通过公共方法暴露功能。

### 注意事项

1. **命名冲突**：私有方法和字段可以同名，因为它们在不同的命名空间中
2. **继承**：子类无法访问父类的私有方法和字段
3. **调试**：私有成员在调试工具中可能不可见或显示为特殊标识

---

## 顶层 await

### 概述

ES2022 允许在模块的顶层使用 `await`，无需包装在 `async` 函数中。

### 语法格式

```js
// 在模块顶层
const data = await fetch('/api/data').then(r => r.json());
export default data;
```

### 基本用法

**示例 1**：加载配置

```js
// config.js
const config = await fetch('/config.json').then(r => r.json());
export default config;
```

**示例 2**：动态导入

```js
// app.js
const module = await import('./module.js');
module.doSomething();
```

### 与 async 函数的对比

| 特性           | async 函数中的 await        | 顶层 await                  |
|:---------------|:----------------------------|:----------------------------|
| **使用位置**   | 必须在 async 函数内         | 模块顶层                    |
| **模块类型**   | 任何模块                    | 必须是 ESM 模块             |
| **执行时机**   | 函数调用时执行              | 模块加载时执行              |
| **错误处理**   | try-catch 或 .catch()       | 模块加载失败                |

### 注意事项

1. **仅限 ESM**：顶层 await 只能在 ES Modules 中使用，不能在 CommonJS 中使用
2. **模块加载阻塞**：使用顶层 await 的模块会阻塞依赖它的模块加载
3. **错误处理**：顶层 await 的错误会导致模块加载失败

### 常见错误

**错误 1**：在非模块文件中使用

```js
// ❌ 错误：在脚本文件中使用（非模块）
const data = await fetch('/api'); // SyntaxError

// ✅ 正确：在模块中使用
// 文件：module.js
// type: module 或使用 .mjs 扩展名
const data = await fetch('/api');
```

**错误 2**：在 CommonJS 中使用

```js
// ❌ 错误：CommonJS 不支持顶层 await
// const data = await fetch('/api'); // SyntaxError

// ✅ 正确：使用 async 函数
(async () => {
  const data = await fetch('/api');
})();
```

---

## Error.cause

### 概述

ES2022 允许在创建错误时指定原因（cause），实现错误链式追踪。

### 语法格式

```js
new Error(message, { cause })
```

### 参数说明

| 参数名    | 类型   | 说明           | 是否必需 | 默认值 |
|:----------|:-------|:---------------|:---------|:-------|
| `message` | string | 错误消息       | 否       | ''     |
| `cause`   | any    | 错误原因对象   | 否       | -      |

### 基本用法

**示例**：错误链式追踪

```js
try {
  try {
    throw new Error('Database connection failed');
  } catch (dbError) {
    throw new Error('Failed to load user data', { cause: dbError });
  }
} catch (userError) {
  console.log(userError.message);        // 'Failed to load user data'
  console.log(userError.cause);          // Error: Database connection failed
  console.log(userError.cause.message);   // 'Database connection failed'
}
```

**输出说明**：
- `userError.message`：当前错误消息
- `userError.cause`：原始错误对象
- 可以通过 `cause` 属性追溯错误链

### 实际应用场景

**示例**：API 调用错误链

```js
async function fetchUserData(userId) {
  try {
    const response = await fetch(`/api/users/${userId}`);
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`, {
        cause: { status: response.status, url: response.url }
      });
    }
    return await response.json();
  } catch (error) {
    throw new Error('Failed to fetch user data', { cause: error });
  }
}

try {
  await fetchUserData(123);
} catch (error) {
  console.error(error.message);           // 'Failed to fetch user data'
  console.error(error.cause.message);     // 'HTTP 404'
  console.error(error.cause.cause);       // { status: 404, url: '...' }
}
```

**输出说明**：通过 `cause` 属性可以追溯完整的错误链，便于调试和日志记录。

### 注意事项

1. **错误链深度**：可以嵌套多层 `cause`，形成错误链
2. **序列化**：`Error.cause` 在 JSON 序列化时会被包含
3. **兼容性**：需要 Node.js 16.9.0+ 或现代浏览器支持

---

## Array.prototype.at()

### 概述

`at()` 方法接受一个整数值，返回该索引对应的元素，支持负索引（从数组末尾开始计数）。

### 语法格式

```js
array.at(index)
```

### 参数说明

| 参数名    | 类型   | 说明                           | 是否必需 | 默认值 |
|:----------|:-------|:-------------------------------|:---------|:-------|
| `index`   | number | 要返回的元素的索引，支持负数   | 是       | -      |

### 返回值

返回指定索引的元素，如果索引超出范围则返回 `undefined`。

### 基本用法

**示例 1**：正索引（与 `[]` 相同）

```js
const arr = [1, 2, 3, 4, 5];
console.log(arr.at(0));  // 1
console.log(arr.at(2));  // 3
console.log(arr.at(10)); // undefined
```

**输出说明**：正索引的行为与 `arr[index]` 相同。

**示例 2**：负索引（从末尾开始）

```js
const arr = [1, 2, 3, 4, 5];
console.log(arr.at(-1)); // 5（最后一个元素）
console.log(arr.at(-2)); // 4（倒数第二个）
console.log(arr.at(-5)); // 1（第一个元素）
console.log(arr.at(-10)); // undefined
```

**输出说明**：
- `-1` 表示最后一个元素
- `-2` 表示倒数第二个元素
- 超出范围返回 `undefined`

### 与 arr[index] 和 arr[arr.length - 1] 的对比

| 方法                    | 正索引 | 负索引 | 访问最后一个元素        |
|:------------------------|:-------|:-------|:------------------------|
| `arr[index]`            | ✅     | ❌     | `arr[arr.length - 1]`   |
| `arr.at(index)`         | ✅     | ✅     | `arr.at(-1)`            |

**示例对比**：

```js
const arr = [1, 2, 3, 4, 5];

// 访问最后一个元素
console.log(arr[arr.length - 1]); // 5（繁琐）
console.log(arr.at(-1));          // 5（简洁）

// 访问倒数第二个元素
console.log(arr[arr.length - 2]); // 4（繁琐）
console.log(arr.at(-2));          // 4（简洁）
```

### 注意事项

1. **性能**：`at()` 的性能与 `arr[index]` 基本相同
2. **边界检查**：超出范围返回 `undefined`，不会抛出错误
3. **稀疏数组**：对于稀疏数组，`at()` 的行为与 `[]` 相同

### 常见错误

**错误 1**：混淆负索引的起始位置

```js
const arr = [1, 2, 3];
// ❌ 错误理解：-0 不是最后一个元素
console.log(arr.at(-0)); // 1（-0 被转换为 0）

// ✅ 正确：-1 是最后一个元素
console.log(arr.at(-1)); // 3
```

---

## Object.hasOwn()

### 概述

`Object.hasOwn()` 是 `Object.prototype.hasOwnProperty()` 的更安全替代方法，用于检查对象是否拥有指定的自有属性。

### 语法格式

```js
Object.hasOwn(obj, prop)
```

### 参数说明

| 参数名    | 类型   | 说明           | 是否必需 | 默认值 |
|:----------|:-------|:---------------|:---------|:-------|
| `obj`     | object | 要检查的对象   | 是       | -      |
| `prop`    | string | 属性名         | 是       | -      |

### 返回值

返回布尔值：
- `true`：对象拥有指定的自有属性
- `false`：对象不拥有该属性，或属性来自原型链

### 基本用法

**示例**：

```js
const obj = { name: 'John' };

console.log(Object.hasOwn(obj, 'name'));        // true
console.log(Object.hasOwn(obj, 'toString'));     // false（来自原型链）
console.log(Object.hasOwn(obj, 'age'));         // false（不存在）
```

**输出说明**：
- `'name'` 是对象的自有属性，返回 `true`
- `'toString'` 来自 `Object.prototype`，返回 `false`
- `'age'` 不存在，返回 `false`

### 与 hasOwnProperty() 的对比

| 特性              | `hasOwnProperty()`              | `Object.hasOwn()`               |
|:------------------|:--------------------------------|:--------------------------------|
| **调用方式**      | `obj.hasOwnProperty(prop)`     | `Object.hasOwn(obj, prop)`      |
| **null 对象**     | 抛出错误                        | 返回 `false`                    |
| **安全性**        | 可能被覆盖                      | 更安全                           |
| **推荐使用**      | 不推荐                          | 推荐                            |

**示例对比**：

```js
const obj = { name: 'John' };

// hasOwnProperty() 可能被覆盖
const obj2 = { hasOwnProperty: () => false };
console.log(obj2.hasOwnProperty('name')); // false（错误结果）

// Object.hasOwn() 更安全
console.log(Object.hasOwn(obj2, 'name')); // true（正确结果）

// null 对象处理
// obj.hasOwnProperty.call(null, 'prop'); // 可能出错
console.log(Object.hasOwn(null, 'prop')); // false（安全）
```

### 注意事项

1. **仅检查自有属性**：不检查原型链上的属性
2. **null/undefined 安全**：对 `null` 或 `undefined` 返回 `false`，不会抛出错误
3. **性能**：性能与 `hasOwnProperty()` 基本相同

---

## 兼容性说明

### 浏览器支持

| 特性           | Chrome | Firefox | Safari | Edge  |
|:---------------|:-------|:--------|:-------|:------|
| 类字段         | 72+    | 69+     | 14+    | 79+   |
| 私有字段       | 84+    | 90+     | 14.1+  | 84+   |
| 顶层 await     | 89+    | 89+     | 15+    | 89+   |
| Error.cause    | 93+    | 91+     | 15.4+  | 93+   |
| Array.prototype.at() | 92+ | 90+     | 15.4+  | 92+   |
| Object.hasOwn() | 93+   | 92+     | 15.4+  | 93+   |

### Node.js 支持

- **类字段**：Node.js 12.0.0+
- **私有字段**：Node.js 12.0.0+
- **顶层 await**：Node.js 14.8.0+（需要 `--experimental-top-level-await` 或 16.0.0+）
- **Error.cause**：Node.js 16.9.0+
- **Array.prototype.at()**：Node.js 16.6.0+
- **Object.hasOwn()**：Node.js 16.9.0+

### 转译和 Polyfill

如果需要在旧环境中使用 ES2022 特性：

1. **Babel**：使用相应的插件转译类字段和私有字段
2. **TypeScript**：在 `tsconfig.json` 中设置 `target: "ES2022"`
3. **Polyfill**：`Array.prototype.at()` 和 `Object.hasOwn()` 可以使用 `core-js` 的 polyfill

---

## 最佳实践

1. **类字段**：
   - 优先使用类字段声明，代码更简洁
   - 使用私有字段保护内部状态

2. **顶层 await**：
   - 用于模块初始化，如加载配置
   - 注意模块加载阻塞的影响

3. **错误处理**：
   - 使用 `Error.cause` 建立错误链，便于调试
   - 在日志中记录完整的错误链

4. **数组访问**：
   - 使用 `at(-1)` 访问最后一个元素，比 `arr[arr.length - 1]` 更简洁
   - 注意负索引从 `-1` 开始

5. **属性检查**：
   - 优先使用 `Object.hasOwn()` 替代 `hasOwnProperty()`
   - 更安全，不会被覆盖

---

## 练习

1. **类字段和私有字段**：
   - 创建一个 `BankAccount` 类，使用私有字段存储余额，提供公共方法进行存取款
   - 使用静态字段存储银行信息

2. **顶层 await**：
   - 创建一个配置模块，使用顶层 await 从远程加载配置
   - 处理配置加载失败的情况

3. **错误链**：
   - 实现一个函数调用链，使用 `Error.cause` 建立错误链
   - 在错误处理中打印完整的错误链

4. **数组方法**：
   - 使用 `at()` 方法实现获取数组最后一个、倒数第二个元素的工具函数
   - 对比使用 `at()` 和传统方法的代码可读性

5. **属性检查**：
   - 使用 `Object.hasOwn()` 实现一个函数，检查对象是否拥有指定的自有属性
   - 处理 `null` 和 `undefined` 的情况

---

## 总结

ES2022 进一步完善了 JavaScript 的面向对象编程能力：

- **类字段**：提供更简洁的类定义语法
- **私有成员**：保护内部实现，提高封装性
- **顶层 await**：简化模块初始化代码
- **错误链**：提供更好的错误追踪机制
- **数组和对象方法**：提供更便捷的 API

这些特性在现代 JavaScript 开发中广泛使用，建议熟练掌握。

继续学习下一节：ES2023 新特性。

---

**最后更新**：2025-12-16
