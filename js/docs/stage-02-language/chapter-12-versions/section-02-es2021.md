# 2.12.2 ES2021 新特性

## 概述

ES2021（ES12）是 ECMAScript 2021 标准，于 2021 年 6 月发布。ES2021 引入了逻辑赋值运算符、字符串替换方法、Promise 组合方法等实用特性，进一步提升了 JavaScript 的表达能力和开发效率。

## 核心特性

ES2021 主要包含以下新特性：

1. **逻辑赋值运算符**：`&&=`、`||=`、`??=`
2. **字符串替换方法**：`String.prototype.replaceAll()`
3. **Promise 组合方法**：`Promise.any()` 和 `AggregateError`
4. **弱引用**：`WeakRef` 和 `FinalizationRegistry`
5. **数字分隔符**：下划线分隔符（`1_000_000`）

---

## 逻辑赋值运算符

### 概述

逻辑赋值运算符结合了逻辑运算符和赋值运算符，提供更简洁的赋值语法。ES2021 引入了三种逻辑赋值运算符：

- `&&=`（逻辑与赋值）
- `||=`（逻辑或赋值）
- `??=`（空值合并赋值）

### 语法格式

```js
// 逻辑与赋值
variable &&= value;

// 逻辑或赋值
variable ||= value;

// 空值合并赋值
variable ??= value;
```

### 参数说明

| 参数名      | 类型 | 说明                     | 是否必需 | 默认值 |
|:------------|:-----|:-------------------------|:---------|:-------|
| `variable`  | any  | 要赋值的变量             | 是       | -      |
| `value`     | any  | 要赋值的值               | 是       | -      |

### 返回值

逻辑赋值运算符返回赋值后的变量值。

### 逻辑与赋值（&&=）

**说明**：只有当左侧值为真值（truthy）时，才将右侧值赋给左侧变量。

**等价写法**：
```js
// x &&= y 等价于
x = x && y;
```

**示例**：
```js
let obj = { name: 'John' };

// 只有当 obj.name 存在时才赋值
obj.name &&= 'Jane';
console.log(obj.name); // 'Jane'

// 如果属性不存在，不会赋值
obj.age &&= 30;
console.log(obj.age); // undefined（未定义）
```

**输出说明**：
- 第一行：`obj.name` 存在且为真值，所以赋值为 `'Jane'`
- 第二行：`obj.age` 不存在（undefined），为假值，所以不赋值

### 逻辑或赋值（||=）

**说明**：只有当左侧值为假值（falsy）时，才将右侧值赋给左侧变量。

**等价写法**：
```js
// x ||= y 等价于
x = x || y;
```

**示例**：
```js
let config = {};

// 只有当 config.port 不存在或为假值时才赋值
config.port ||= 3000;
console.log(config.port); // 3000

// 如果已存在，不会覆盖
config.port ||= 8080;
console.log(config.port); // 3000（未改变）
```

**输出说明**：
- 第一行：`config.port` 不存在（undefined），为假值，所以赋值为 `3000`
- 第二行：`config.port` 已存在且为真值，所以不赋值，保持 `3000`

### 空值合并赋值（??=）

**说明**：只有当左侧值为 `null` 或 `undefined` 时，才将右侧值赋给左侧变量。

**等价写法**：
```js
// x ??= y 等价于
x = x ?? y;
```

**示例**：
```js
let user = { name: '', age: 0 };

// 只有当 user.name 为 null 或 undefined 时才赋值
user.name ??= 'Anonymous';
console.log(user.name); // ''（空字符串是假值但不是 null/undefined）

// age 为 0（假值但不是 null/undefined），不赋值
user.age ??= 18;
console.log(user.age); // 0

// 对于 null 或 undefined，会赋值
user.email ??= 'user@example.com';
console.log(user.email); // 'user@example.com'
```

**输出说明**：
- 第一行：`user.name` 是空字符串（假值但不是 null/undefined），所以不赋值
- 第二行：`user.age` 是 0（假值但不是 null/undefined），所以不赋值
- 第三行：`user.email` 不存在（undefined），所以赋值为 `'user@example.com'`

### 三种运算符的区别

| 运算符 | 触发条件           | 示例值（会赋值）        | 示例值（不赋值）    |
|:-------|:-------------------|:-----------------------|:-------------------|
| `&&=`  | 左侧为真值         | `true`、`1`、`'str'`   | `false`、`0`、`''` |
| `||=`  | 左侧为假值         | `false`、`0`、`''`     | `true`、`1`、`'str'` |
| `??=`  | 左侧为 null/undefined | `null`、`undefined`  | `false`、`0`、`''` |

### 注意事项

1. **性能考虑**：逻辑赋值运算符不会重复读取变量，在某些情况下可能比等价写法更高效
2. **可读性**：对于简单的默认值赋值，`??=` 比 `||=` 更精确，避免将假值（如 `0`、`''`）误判为需要赋值的情况
3. **兼容性**：需要 Node.js 15+ 或现代浏览器支持

### 常见错误

**错误 1**：混淆 `||=` 和 `??=`

```js
// ❌ 错误：使用 ||= 会导致 0 被覆盖
let count = 0;
count ||= 10; // count 变成 10（错误）

// ✅ 正确：使用 ??= 保留 0
let count = 0;
count ??= 10; // count 保持 0（正确）
```

**错误 2**：在链式调用中使用

```js
// ❌ 错误：逻辑赋值运算符不能用于链式调用
let obj = {};
obj.name &&= 'John' &&= 'Jane'; // 语法错误

// ✅ 正确：分别赋值
let obj = {};
obj.name &&= 'John';
obj.name &&= 'Jane';
```

---

## String.prototype.replaceAll()

### 概述

`replaceAll()` 方法返回一个新字符串，其中所有匹配的子字符串都被替换为指定的字符串。这是对 `replace()` 方法的补充，提供了更直观的全局替换功能。

### 语法格式

```js
str.replaceAll(searchValue, replaceValue)
```

### 参数说明

| 参数名         | 类型            | 说明                           | 是否必需 | 默认值 |
|:---------------|:----------------|:-------------------------------|:---------|:-------|
| `searchValue`  | string / RegExp | 要替换的子字符串或正则表达式   | 是       | -      |
| `replaceValue` | string / function | 替换为的字符串或替换函数     | 是       | -      |

**注意**：如果 `searchValue` 是正则表达式，必须使用全局标志（`g`），否则会抛出 `TypeError`。

### 返回值

返回一个新字符串，所有匹配的子字符串都被替换。原字符串不会被修改。

### 基本用法

**示例 1**：替换所有匹配的字符串

```js
const text = 'Hello World, Hello JavaScript';
const result = text.replaceAll('Hello', 'Hi');
console.log(result); // 'Hi World, Hi JavaScript'
console.log(text);   // 'Hello World, Hello JavaScript'（原字符串未改变）
```

**输出说明**：
- `result`：所有 `'Hello'` 都被替换为 `'Hi'`
- `text`：原字符串保持不变

**示例 2**：使用正则表达式（必须带 `g` 标志）

```js
const text = 'apple, banana, apple';
const result = text.replaceAll(/apple/g, 'orange');
console.log(result); // 'orange, banana, orange'
```

**输出说明**：正则表达式必须使用全局标志 `g`，否则会抛出错误。

### 与 replace() 的对比

| 特性           | `replace()`                    | `replaceAll()`                 |
|:---------------|:-------------------------------|:-------------------------------|
| **替换范围**   | 只替换第一个匹配               | 替换所有匹配                   |
| **字符串参数** | 只替换第一个                   | 替换所有                       |
| **正则参数**   | 需要 `g` 标志才全局替换        | 必须使用 `g` 标志，否则报错   |
| **返回值**     | 新字符串                       | 新字符串                       |

**示例对比**：

```js
const text = 'apple, banana, apple';

// 使用 replace()：只替换第一个
const result1 = text.replace('apple', 'orange');
console.log(result1); // 'orange, banana, apple'

// 使用 replaceAll()：替换所有
const result2 = text.replaceAll('apple', 'orange');
console.log(result2); // 'orange, banana, orange'

// replace() 需要正则 + g 标志才能全局替换
const result3 = text.replace(/apple/g, 'orange');
console.log(result3); // 'orange, banana, orange'
```

### 使用函数作为替换值

**示例**：使用函数动态替换

```js
const text = 'price: 10, price: 20, price: 30';
const result = text.replaceAll(/price: (\d+)/g, (match, price) => {
  return `price: $${price * 1.1}`; // 增加 10%
});
console.log(result); // 'price: $11, price: $22, price: $33'
```

**输出说明**：函数接收匹配的字符串和捕获组，返回替换后的字符串。

### 注意事项

1. **原字符串不变**：`replaceAll()` 不会修改原字符串，返回新字符串
2. **正则必须带 g**：如果使用正则表达式，必须包含全局标志 `g`，否则会抛出 `TypeError`
3. **大小写敏感**：默认区分大小写，如需忽略大小写，使用正则表达式 `i` 标志

### 常见错误

**错误 1**：正则表达式未使用 `g` 标志

```js
// ❌ 错误：会抛出 TypeError
const text = 'apple, apple';
text.replaceAll(/apple/, 'orange'); // TypeError

// ✅ 正确：使用 g 标志
const text = 'apple, apple';
text.replaceAll(/apple/g, 'orange'); // 'orange, orange'
```

**错误 2**：误以为会修改原字符串

```js
// ❌ 错误：原字符串不会被修改
let text = 'Hello World';
text.replaceAll('Hello', 'Hi');
console.log(text); // 'Hello World'（未改变）

// ✅ 正确：需要重新赋值
let text = 'Hello World';
text = text.replaceAll('Hello', 'Hi');
console.log(text); // 'Hi World'
```

---

## Promise.any() 和 AggregateError

### 概述

`Promise.any()` 返回一个 Promise，只要参数中的任何一个 Promise 成功（fulfilled），就返回该 Promise 的结果。如果所有 Promise 都失败（rejected），则返回一个 `AggregateError`，包含所有失败的原因。

### 语法格式

```js
Promise.any(iterable)
```

### 参数说明

| 参数名      | 类型      | 说明                           | 是否必需 | 默认值 |
|:------------|:----------|:-------------------------------|:---------|:-------|
| `iterable`  | iterable  | 可迭代对象（如数组），包含多个 Promise | 是 | -      |

### 返回值

返回一个 Promise：
- **成功情况**：如果任何一个 Promise 成功，返回该 Promise 的解决值
- **失败情况**：如果所有 Promise 都失败，返回一个 `AggregateError`，包含所有失败原因

### 基本用法

**示例 1**：至少一个 Promise 成功

```js
const promise1 = Promise.reject('Error 1');
const promise2 = Promise.resolve('Success 2');
const promise3 = Promise.reject('Error 3');

Promise.any([promise1, promise2, promise3])
  .then(result => {
    console.log(result); // 'Success 2'
  });
```

**输出说明**：`promise2` 成功，所以 `Promise.any()` 返回 `'Success 2'`。

**示例 2**：所有 Promise 都失败

```js
const promise1 = Promise.reject('Error 1');
const promise2 = Promise.reject('Error 2');
const promise3 = Promise.reject('Error 3');

Promise.any([promise1, promise2, promise3])
  .catch(error => {
    console.log(error instanceof AggregateError); // true
    console.log(error.errors); // ['Error 1', 'Error 2', 'Error 3']
  });
```

**输出说明**：
- `error` 是 `AggregateError` 实例
- `error.errors` 包含所有失败的原因

### AggregateError

`AggregateError` 是一个新的错误类型，用于表示多个错误。

**语法格式**：
```js
new AggregateError(errors, message)
```

**参数说明**：

| 参数名      | 类型   | 说明           | 是否必需 | 默认值 |
|:------------|:-------|:---------------|:---------|:-------|
| `errors`    | array  | 错误数组       | 是       | -      |
| `message`   | string | 错误消息       | 否       | ''     |

**示例**：

```js
const error = new AggregateError(
  ['Error 1', 'Error 2', 'Error 3'],
  'All promises failed'
);

console.log(error.message);     // 'All promises failed'
console.log(error.errors);      // ['Error 1', 'Error 2', 'Error 3']
console.log(error.name);        // 'AggregateError'
```

### 实际应用场景

**示例**：多数据源请求，使用最快的成功响应

```js
// 模拟多个 API 端点
const api1 = fetch('/api/v1/data').then(r => r.json());
const api2 = fetch('/api/v2/data').then(r => r.json());
const api3 = fetch('/api/v3/data').then(r => r.json());

Promise.any([api1, api2, api3])
  .then(data => {
    console.log('Got data from fastest source:', data);
    // 使用最快返回的数据
  })
  .catch(error => {
    console.error('All sources failed:', error.errors);
    // 所有数据源都失败，使用备用方案
  });
```

**输出说明**：使用第一个成功返回的数据源，如果全部失败则处理错误。

### 与 Promise.all() 和 Promise.allSettled() 的对比

| 方法                | 成功条件           | 失败条件           | 返回值                    |
|:--------------------|:-------------------|:-------------------|:--------------------------|
| `Promise.all()`     | 全部成功           | 任何一个失败       | 所有成功值的数组          |
| `Promise.allSettled()` | 等待全部完成   | 不失败（总是成功） | 所有结果的数组            |
| `Promise.any()`      | 任何一个成功       | 全部失败           | 第一个成功的值            |

**示例对比**：

```js
const p1 = Promise.resolve('A');
const p2 = Promise.reject('B');
const p3 = Promise.resolve('C');

// Promise.all：全部成功才成功
Promise.all([p1, p2, p3])
  .catch(err => console.log('all failed:', err)); // 'all failed: B'

// Promise.allSettled：等待全部完成
Promise.allSettled([p1, p2, p3])
  .then(results => console.log(results));
// [{status: 'fulfilled', value: 'A'}, {status: 'rejected', reason: 'B'}, ...]

// Promise.any：任何一个成功就成功
Promise.any([p1, p2, p3])
  .then(result => console.log('any success:', result)); // 'any success: A'
```

### 注意事项

1. **空数组**：如果传入空数组，`Promise.any()` 会立即拒绝，返回 `AggregateError`
2. **非 Promise 值**：数组中的非 Promise 值会被转换为已解决的 Promise
3. **性能考虑**：一旦有 Promise 成功，其他 Promise 的结果会被忽略，但不会取消执行

### 常见错误

**错误 1**：未处理所有失败的情况

```js
// ❌ 错误：可能遗漏所有失败的情况
Promise.any([promise1, promise2])
  .then(result => console.log(result));
// 如果全部失败，未捕获错误

// ✅ 正确：总是处理失败情况
Promise.any([promise1, promise2])
  .then(result => console.log(result))
  .catch(error => {
    if (error instanceof AggregateError) {
      console.error('All failed:', error.errors);
    }
  });
```

---

## WeakRef 和 FinalizationRegistry

### 概述

`WeakRef` 和 `FinalizationRegistry` 提供了对对象弱引用和清理回调的机制，主要用于内存管理和资源清理场景。

### WeakRef

`WeakRef` 允许你创建一个对象的弱引用，不会阻止垃圾回收。

**语法格式**：
```js
new WeakRef(target)
```

**参数说明**：

| 参数名    | 类型   | 说明           | 是否必需 | 默认值 |
|:----------|:-------|:---------------|:---------|:-------|
| `target`  | object | 要创建弱引用的对象 | 是   | -      |

**返回值**：返回一个 `WeakRef` 对象。

**方法**：
- `deref()`：返回被引用的对象，如果对象已被垃圾回收则返回 `undefined`

**示例**：

```js
let obj = { data: 'important' };
const weakRef = new WeakRef(obj);

// 访问对象
console.log(weakRef.deref()); // { data: 'important' }

// 清除强引用
obj = null;

// 垃圾回收后，弱引用失效
// 注意：实际回收时间不确定，这里仅作演示
setTimeout(() => {
  console.log(weakRef.deref()); // undefined（可能已被回收）
}, 1000);
```

**输出说明**：
- 初始时 `weakRef.deref()` 返回原对象
- 清除强引用后，对象可能被垃圾回收，`deref()` 返回 `undefined`

### FinalizationRegistry

`FinalizationRegistry` 允许你在对象被垃圾回收时执行清理回调。

**语法格式**：
```js
new FinalizationRegistry(cleanupCallback)
```

**参数说明**：

| 参数名            | 类型     | 说明                 | 是否必需 | 默认值 |
|:------------------|:---------|:---------------------|:---------|:-------|
| `cleanupCallback` | function | 清理回调函数         | 是       | -      |

**返回值**：返回一个 `FinalizationRegistry` 对象。

**方法**：
- `register(target, heldValue, unregisterToken)`：注册对象，在对象被回收时调用清理回调

**参数说明**：

| 参数名            | 类型   | 说明                           | 是否必需 | 默认值 |
|:------------------|:-------|:-------------------------------|:---------|:-------|
| `target`          | object | 要注册的对象                   | 是       | -      |
| `heldValue`       | any    | 传递给清理回调的值             | 是       | -      |
| `unregisterToken` | any    | 用于取消注册的令牌（可选）     | 否       | -      |

**示例**：

```js
const registry = new FinalizationRegistry((heldValue) => {
  console.log(`Cleaning up: ${heldValue}`);
});

let obj = { data: 'important' };
registry.register(obj, 'resource-1');

// 清除强引用
obj = null;

// 垃圾回收后，清理回调会被调用
// 输出：'Cleaning up: resource-1'
```

**输出说明**：当 `obj` 被垃圾回收时，清理回调会被调用，传入注册时的 `heldValue`。

### 注意事项

1. **使用场景有限**：`WeakRef` 和 `FinalizationRegistry` 主要用于底层库和框架，普通应用开发中很少使用
2. **回收时间不确定**：垃圾回收的时间不确定，不能依赖清理回调的精确执行时间
3. **性能影响**：过度使用可能影响性能
4. **兼容性**：需要 Node.js 14.6+ 或现代浏览器支持

---

## 数字分隔符

### 概述

ES2021 支持在数字字面量中使用下划线（`_`）作为分隔符，提高大数字的可读性。

### 语法格式

```js
const number = 1_000_000;
```

### 示例

```js
// 整数
const million = 1_000_000;
const billion = 1_000_000_000;

// 浮点数
const pi = 3.141_592_653;

// 二进制
const binary = 0b1010_0001;

// 十六进制
const hex = 0xFF_EC_DE_5E;

console.log(million);  // 1000000
console.log(billion);  // 1000000000
console.log(pi);       // 3.141592653
```

**输出说明**：下划线不影响数字的值，仅用于提高可读性。

### 注意事项

1. **位置限制**：下划线不能放在数字开头、结尾、小数点前后、指数符号前后
2. **不影响值**：下划线完全被忽略，不影响数字的实际值
3. **可读性**：主要用于提高大数字的可读性

### 常见错误

**错误示例**：

```js
// ❌ 错误：下划线位置不当
const num1 = _1000;        // 语法错误
const num2 = 1000_;         // 语法错误
const num3 = 10_.5;         // 语法错误
const num4 = 10._5;         // 语法错误
const num5 = 1e_10;         // 语法错误

// ✅ 正确：下划线在合适位置
const num1 = 1_000;         // 正确
const num2 = 10.5_5;        // 正确（但不太常用）
```

---

## 兼容性说明

### 浏览器支持

| 特性                 | Chrome | Firefox | Safari | Edge  |
|:---------------------|:-------|:--------|:-------|:------|
| 逻辑赋值运算符       | 85+    | 79+     | 14+    | 85+   |
| `replaceAll()`       | 85+    | 77+     | 13.1+  | 85+   |
| `Promise.any()`      | 85+    | 79+     | 14+    | 85+   |
| `WeakRef`            | 84+    | 79+     | 14.1+  | 84+   |
| `FinalizationRegistry` | 84+ | 79+     | 14.1+  | 84+   |
| 数字分隔符           | 75+    | 70+     | 13+    | 79+   |

### Node.js 支持

- **逻辑赋值运算符**：Node.js 15.0.0+
- **`replaceAll()`**：Node.js 15.0.0+
- **`Promise.any()`**：Node.js 15.0.0+
- **`WeakRef`**：Node.js 14.6.0+
- **`FinalizationRegistry`**：Node.js 14.6.0+
- **数字分隔符**：Node.js 12.5.0+

### 转译和 Polyfill

如果需要在旧环境中使用 ES2021 特性：

1. **Babel**：使用 `@babel/plugin-proposal-logical-assignment-operators` 等插件
2. **TypeScript**：在 `tsconfig.json` 中设置 `target: "ES2021"`
3. **Polyfill**：`Promise.any()` 可以使用 `core-js` 的 polyfill

---

## 最佳实践

1. **逻辑赋值运算符**：
   - 优先使用 `??=` 设置默认值，避免将假值误判为需要赋值
   - 使用 `&&=` 进行条件赋值，代码更简洁

2. **字符串替换**：
   - 需要全局替换时，优先使用 `replaceAll()`，比 `replace()` + 正则更直观
   - 注意正则表达式必须使用 `g` 标志

3. **Promise 组合**：
   - 需要"最快成功"策略时使用 `Promise.any()`
   - 总是处理 `AggregateError`，避免未捕获的错误

4. **弱引用**：
   - 仅在底层库和框架中使用，普通应用开发避免使用
   - 不要依赖清理回调的精确执行时间

5. **数字分隔符**：
   - 用于提高大数字的可读性
   - 遵循常见的千位分隔习惯

---

## 练习

1. **逻辑赋值运算符**：
   - 使用 `??=` 为配置对象设置默认值，确保 `0`、`''`、`false` 等假值不被覆盖
   - 使用 `&&=` 实现条件属性更新

2. **字符串替换**：
   - 使用 `replaceAll()` 将文本中的所有 `"old"` 替换为 `"new"`
   - 使用 `replaceAll()` 和函数，将文本中的所有数字增加 10%

3. **Promise 组合**：
   - 实现一个函数，从多个数据源请求数据，使用第一个成功返回的结果
   - 处理所有数据源都失败的情况，返回友好的错误信息

4. **数字分隔符**：
   - 使用数字分隔符表示大数字（如 1 亿、10 亿）
   - 在二进制和十六进制数字中使用分隔符提高可读性

5. **综合练习**：
   - 创建一个配置管理器，使用 `??=` 设置默认值，使用 `replaceAll()` 处理配置模板，使用 `Promise.any()` 从多个配置源加载配置

---

## 总结

ES2021 引入了实用的语法糖和 API，提升了开发效率：

- **逻辑赋值运算符**：提供更简洁的赋值语法，`??=` 特别适合设置默认值
- **`replaceAll()`**：提供直观的全局字符串替换
- **`Promise.any()`**：实现"最快成功"策略，适合多数据源场景
- **弱引用机制**：为底层库提供内存管理工具
- **数字分隔符**：提高大数字的可读性

这些特性在现代 JavaScript 开发中广泛使用，建议熟练掌握。

继续学习下一节：ES2022 新特性。

---

**最后更新**：2025-12-16
