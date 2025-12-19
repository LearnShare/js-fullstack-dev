# 2.16.1 ES2020 新特性

## 概述

ES2020（ES11）是 ECMAScript 2020 标准，引入了多项重要特性，包括 BigInt、可选链、空值合并、动态 import 等。这些特性显著提升了 JavaScript 的表达能力和开发体验。

## 特性列表

ES2020 引入的主要特性：

| 特性              | 说明                           | 状态   |
|:------------------|:-------------------------------|:-------|
| BigInt            | 大整数类型                      | 已定稿 |
| 可选链（?.）      | 安全访问嵌套属性                | 已定稿 |
| 空值合并（??）    | 空值合并运算符                  | 已定稿 |
| 动态 import       | 动态导入模块                    | 已定稿 |
| Promise.allSettled | 等待所有 Promise 完成          | 已定稿 |
| globalThis        | 全局 this 引用                  | 已定稿 |
| for-in 规范化     | 规范化的枚举顺序                | 已定稿 |

## BigInt

### 概述

BigInt 是一种新的原始类型，用于表示大于 `Number.MAX_SAFE_INTEGER`（2^53 - 1）的整数。

### 语法

```js
// 方法 1：在数字后加 n
const bigInt1 = 9007199254740993n;

// 方法 2：使用 BigInt() 构造函数
const bigInt2 = BigInt(9007199254740993);
```

### 基本用法

```js
// 创建 BigInt
const a = 9007199254740993n;
const b = BigInt('9007199254740993');

// 运算
const sum = a + b;
const product = a * b;
const quotient = a / b;

console.log(sum);        // 18014398509481986n
console.log(product);    // 81129638414606681695789005144065n
```

### 注意事项

- BigInt 不能与 Number 直接运算
- BigInt 不能使用 `Math` 对象的方法
- BigInt 在 JSON 序列化时需要特殊处理

## 可选链（Optional Chaining）

### 概述

可选链运算符 `?.` 允许安全地访问嵌套的对象属性，即使中间属性为 `null` 或 `undefined` 也不会抛出错误。

### 语法

```js
obj?.prop
obj?.[expr]
func?.(args)
```

### 基本用法

```js
const user = {
    name: "John",
    address: {
        city: "Beijing"
    }
};

// 安全访问嵌套属性
console.log(user?.address?.city);        // "Beijing"
console.log(user?.profile?.email);       // undefined（不会报错）

// 安全调用方法
const result = user?.getName?.();         // undefined（如果方法不存在）

// 安全访问数组
const firstItem = arr?.[0];              // undefined（如果数组不存在）
```

### 与空值合并结合

```js
const city = user?.address?.city ?? 'Unknown';
console.log(city);  // "Beijing" 或 "Unknown"
```

## 空值合并（Nullish Coalescing）

### 概述

空值合并运算符 `??` 提供了一种简洁的方式来处理 `null` 或 `undefined` 的默认值。

### 语法

```js
leftExpr ?? rightExpr
```

### 基本用法

```js
// 与 || 的区别
const value1 = 0 || 'default';      // "default"（0 被视为 falsy）
const value2 = 0 ?? 'default';     // 0（只有 null/undefined 才使用默认值）

const value3 = '' || 'default';     // "default"
const value4 = '' ?? 'default';     // ""

const value5 = null ?? 'default';    // "default"
const value6 = undefined ?? 'default'; // "default"
```

### 实际应用

```js
// 配置默认值
const config = {
    timeout: userConfig.timeout ?? 5000,
    retries: userConfig.retries ?? 3
};

// 函数参数默认值
function greet(name) {
    const displayName = name ?? 'Guest';
    return `Hello, ${displayName}!`;
}
```

## 动态 import

### 概述

动态 `import()` 允许在运行时按需加载模块，返回一个 Promise。

### 语法

```js
import(moduleSpecifier)
```

### 基本用法

```js
// 动态导入模块
async function loadModule() {
    const module = await import('./utils.js');
    module.doSomething();
}

// 条件导入
if (condition) {
    const { func1, func2 } = await import('./module1.js');
} else {
    const { func3 } = await import('./module2.js');
}

// 错误处理
try {
    const module = await import('./module.js');
} catch (error) {
    console.error('模块加载失败:', error);
}
```

### 使用场景

- 代码分割和懒加载
- 条件加载模块
- 按需加载大型库

## Promise.allSettled

### 概述

`Promise.allSettled()` 等待所有 Promise 完成（无论成功或失败），返回一个包含所有结果的数组。

### 语法

```js
Promise.allSettled(iterable)
```

### 基本用法

```js
const promises = [
    Promise.resolve(1),
    Promise.reject('Error'),
    Promise.resolve(3)
];

Promise.allSettled(promises).then(results => {
    results.forEach((result, index) => {
        if (result.status === 'fulfilled') {
            console.log(`Promise ${index}:`, result.value);
        } else {
            console.log(`Promise ${index}:`, result.reason);
        }
    });
});

// 输出:
// Promise 0: 1
// Promise 1: Error
// Promise 2: 3
```

### 与 Promise.all 的区别

| 特性           | Promise.all        | Promise.allSettled |
|:---------------|:-------------------|:--------------------|
| 失败处理       | 立即拒绝           | 等待所有完成        |
| 返回值         | 值数组             | 结果对象数组        |
| 使用场景       | 需要所有成功       | 需要所有结果        |

## globalThis

### 概述

`globalThis` 提供了一个标准的方式来访问全局对象，无论在什么环境中都能正常工作。

### 语法

```js
globalThis
```

### 基本用法

```js
// 在不同环境中访问全局对象
// 浏览器: window
// Node.js: global
// Web Worker: self

// 使用 globalThis（统一方式）
globalThis.console.log('Hello');

// 设置全局变量
globalThis.myGlobalVar = 'value';
```

### 兼容性处理

```js
// 旧代码的兼容方式
const getGlobal = function() {
    if (typeof globalThis !== 'undefined') return globalThis;
    if (typeof window !== 'undefined') return window;
    if (typeof global !== 'undefined') return global;
    if (typeof self !== 'undefined') return self;
    throw new Error('无法找到全局对象');
};
```

## for-in 规范化

### 概述

ES2020 规范了 `for...in` 循环的枚举顺序，使其在不同引擎中保持一致。

### 枚举顺序规则

1. 非负整数键（按数字顺序）
2. 字符串键（按插入顺序）
3. Symbol 键（按插入顺序）

### 示例

```js
const obj = {
    2: 'two',
    'b': 'b',
    1: 'one',
    'a': 'a'
};

for (const key in obj) {
    console.log(key);
}
// 输出顺序: 1, 2, 'b', 'a'（规范化后的顺序）
```

## 注意事项

1. **BigInt 限制**：不能与 Number 直接运算，需要转换
2. **可选链性能**：可选链有轻微性能开销，但通常可忽略
3. **空值合并优先级**：`??` 的优先级低于 `&&` 和 `||`
4. **动态 import**：返回 Promise，需要使用 `await` 或 `.then()`
5. **浏览器支持**：需要较新的浏览器版本

## 常见问题

### 问题 1：BigInt 如何与 Number 运算？

```js
const bigInt = 9007199254740993n;
const number = 100;

// 需要转换
const result1 = Number(bigInt) + number;
const result2 = bigInt + BigInt(number);
```

### 问题 2：可选链可以用于哪些场景？

```js
// 对象属性
obj?.prop

// 数组元素
arr?.[0]

// 方法调用
func?.()

// 链式调用
obj?.prop?.method?.()
```

### 问题 3：空值合并与逻辑或的区别？

```js
// || 对所有 falsy 值生效
0 || 'default'      // "default"
'' || 'default'    // "default"
false || 'default' // "default"

// ?? 只对 null/undefined 生效
0 ?? 'default'      // 0
'' ?? 'default'    // ""
false ?? 'default' // false
```

## 最佳实践

1. **使用可选链**：访问嵌套属性时使用可选链避免错误
2. **使用空值合并**：设置默认值时使用 `??` 而不是 `||`
3. **动态导入**：大型模块使用动态导入实现代码分割
4. **Promise.allSettled**：需要所有结果时使用 `allSettled` 而不是 `all`
5. **globalThis**：跨环境代码使用 `globalThis` 访问全局对象

## 练习任务

1. 使用可选链和空值合并重构一段嵌套属性访问代码，提高安全性。

2. 实现一个函数，使用动态 `import()` 按需加载工具模块。

3. 使用 `Promise.allSettled()` 处理多个异步操作，并收集所有结果（包括失败的）。

4. 创建一个 BigInt 计算函数，处理大数字运算。

5. 使用 `globalThis` 创建一个跨环境的全局配置对象。
