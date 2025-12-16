# 1.0.2 ECMAScript 标准演进

## 概述

ECMAScript 是 JavaScript 的标准化规范，由 ECMA International 组织制定和维护。本节详细介绍 ECMAScript 标准的演进过程、各版本特性以及标准化的重要意义。

## ECMAScript 标准化组织

### ECMA International

ECMA International（欧洲计算机制造商协会）是一个致力于信息和通信系统标准化的国际组织。JavaScript 的标准化工作由 ECMA 的 TC39 技术委员会负责。

### TC39 委员会

TC39（Technical Committee 39）是负责 ECMAScript 标准制定的技术委员会，成员包括：

- 主要浏览器厂商（Google、Mozilla、Microsoft、Apple 等）
- JavaScript 引擎开发者
- 框架和工具开发者
- 学术界代表

### 标准化流程

ECMAScript 新特性的标准化遵循严格的流程：

1. **Stage 0（Strawman）**：提案阶段
2. **Stage 1（Proposal）**：正式提案
3. **Stage 2（Draft）**：草案阶段
4. **Stage 3（Candidate）**：候选阶段
5. **Stage 4（Finished）**：完成阶段，将包含在下一版本中

## ECMAScript 1（1997）

### 标准发布

ECMAScript 1 于 1997 年 6 月发布，这是 JavaScript 的第一个标准化版本。

### 主要内容

- 基本语法和数据类型
- 控制结构
- 函数定义
- 对象和数组
- 正则表达式（基础）

### 意义

ECMAScript 1 确立了 JavaScript 作为标准语言的基础，为后续版本的发展奠定了基础。

## ECMAScript 2（1998）

### 标准发布

ECMAScript 2 于 1998 年 6 月发布，主要是对 ECMAScript 1 的编辑性修正，没有引入新特性。

### 目的

ECMAScript 2 的主要目的是与 ISO/IEC 16262 国际标准保持一致。

## ECMAScript 3（1999）

### 标准发布

ECMAScript 3 于 1999 年 12 月发布，这是 JavaScript 历史上第一个真正稳定和广泛采用的标准版本。

### 主要特性

- **正则表达式**：完整的正则表达式支持
- **异常处理**：try-catch-finally 语句
- **字符串方法**：更多字符串操作方法
- **数值格式化**：`toFixed()`、`toExponential()` 等方法
- **控制流改进**：do-while 循环等

```js
// ECMAScript 3 特性示例
// 正则表达式
var pattern = /test/gi;
var result = pattern.test("This is a test");

// 异常处理
try {
    riskyOperation();
} catch (error) {
    console.log("Error: " + error.message);
} finally {
    cleanup();
}

// 字符串方法
var str = "Hello World";
var upper = str.toUpperCase();
var lower = str.toLowerCase();
```

### 影响

ECMAScript 3 成为了 Web 开发的事实标准，几乎所有浏览器都完全支持这个版本，持续使用了近 10 年。

## ECMAScript 4 的失败（2000-2008）

### 雄心勃勃的计划

ECMAScript 4 试图引入大量新特性，包括：

- 类（Classes）和接口（Interfaces）
- 命名空间（Namespaces）
- 包系统（Packages）
- 类型注解（Type Annotations）
- 可选类型系统
- 模块系统
- 迭代器和生成器
- 结构类型

### 标准化的失败

由于 ECMAScript 4 的改动过于激进，遭到了主要浏览器厂商（特别是 Microsoft）的强烈反对。主要争议点包括：

- 改动过大，可能导致现有代码不兼容
- 类型系统的复杂性
- 实现难度过高

### 结果

2008 年，ECMAScript 4 被正式放弃，TC39 决定采用渐进式的方式推进标准，这为后来 ECMAScript 5 和 ES6 的成功奠定了基础。

### 影响

ECMAScript 4 的失败虽然导致了标准化的停滞，但也让 TC39 学会了采用更务实、渐进的方式来推进标准。

## ECMAScript 5（2009）

### 标准发布

ECMAScript 5 于 2009 年 12 月发布，这是 JavaScript 标准化进程中的重要转折点。

### 主要特性

#### 1. 严格模式（Strict Mode）

```js
"use strict";

// 严格模式下的限制
function strictFunction() {
    "use strict";
    // 未声明的变量会报错
    // x = 1;  // ReferenceError
    
    // 不能删除不可删除的属性
    // delete Object.prototype;  // TypeError
    
    // 函数参数不能重名
    // function duplicate(a, a) {}  // SyntaxError
}
```

#### 2. JSON 支持

```js
// JSON.parse() - 解析 JSON 字符串
var jsonString = '{"name": "John", "age": 30}';
var obj = JSON.parse(jsonString);

// JSON.stringify() - 将对象转换为 JSON 字符串
var obj = { name: "John", age: 30 };
var jsonString = JSON.stringify(obj);
```

#### 3. 数组方法

```js
var numbers = [1, 2, 3, 4, 5];

// forEach - 遍历数组
numbers.forEach(function(value, index, array) {
    console.log(value, index);
});

// map - 映射数组
var doubled = numbers.map(function(value) {
    return value * 2;
});

// filter - 过滤数组
var evens = numbers.filter(function(value) {
    return value % 2 === 0;
});

// reduce - 归约数组
var sum = numbers.reduce(function(acc, value) {
    return acc + value;
}, 0);

// some - 检查是否有元素满足条件
var hasEven = numbers.some(function(value) {
    return value % 2 === 0;
});

// every - 检查是否所有元素都满足条件
var allPositive = numbers.every(function(value) {
    return value > 0;
});
```

#### 4. 对象方法

```js
// Object.keys() - 获取对象的所有键
var obj = { a: 1, b: 2, c: 3 };
var keys = Object.keys(obj);  // ['a', 'b', 'c']

// Object.create() - 创建对象
var proto = { greet: function() { return "Hello"; } };
var obj = Object.create(proto);

// Object.defineProperty() - 定义属性
Object.defineProperty(obj, 'name', {
    value: 'John',
    writable: false,
    enumerable: true,
    configurable: true
});

// Object.getOwnPropertyDescriptor() - 获取属性描述符
var descriptor = Object.getOwnPropertyDescriptor(obj, 'name');
```

#### 5. 函数方法

```js
// Function.prototype.bind() - 绑定 this
var obj = {
    name: "John",
    greet: function() {
        return "Hello, " + this.name;
    }
};

var boundGreet = obj.greet.bind({ name: "Jane" });
console.log(boundGreet());  // "Hello, Jane"
```

#### 6. 字符串方法

```js
// String.prototype.trim() - 去除首尾空白
var str = "  Hello World  ";
var trimmed = str.trim();  // "Hello World"
```

### 影响

ECMAScript 5 为现代 JavaScript 开发奠定了基础，引入了许多现在仍在使用的核心特性，特别是 JSON 支持和数组方法。

## ECMAScript 5.1（2011）

### 标准发布

ECMAScript 5.1 于 2011 年 6 月发布，主要是对 ECMAScript 5 的澄清和修正，没有引入新特性。

### 目的

ECMAScript 5.1 的主要目的是与 ISO/IEC 16262:2011 国际标准保持一致。

## ECMAScript 6 / ES2015（2015）

### 标准发布

ECMAScript 6（也称为 ES2015）于 2015 年 6 月发布，这是 JavaScript 历史上最重要的更新之一。

### 命名变更

从 ES2015 开始，ECMAScript 采用年份命名方式，ES6 也被称为 ES2015。

### 主要特性概览

ECMAScript 6 引入了大量新特性，包括：

- 变量声明（let、const）
- 箭头函数
- 类（Classes）
- 模块系统（ES Modules）
- 解构赋值
- 模板字符串
- Promise
- 生成器（Generators）
- Symbol 类型
- Set 和 Map
- for...of 循环
- 默认参数和剩余参数
- 展开运算符

### 影响

ES6 彻底改变了 JavaScript 的开发方式，引入了现代编程语言的核心特性，为后续版本的发展奠定了基础。

## ECMAScript 2016（ES7）

### 标准发布

ECMAScript 2016 于 2016 年 6 月发布，这是第一个按年份命名的版本。

### 主要特性

- **指数运算符**：`**`
- **Array.prototype.includes()**

```js
// 指数运算符
var result = 2 ** 8;        // 256
var result2 = Math.pow(2, 8);  // 256（等价写法）

// Array.includes()
var arr = [1, 2, 3, 4, 5];
console.log(arr.includes(3));    // true
console.log(arr.includes(6));    // false
console.log(arr.includes(2, 2)); // false（从索引 2 开始搜索）
```

### 标准化流程的改进

ES2016 开始，TC39 采用更快的发布周期，每年 6 月发布新版本，确保新特性能够及时进入标准。

## ECMAScript 2017（ES8）

### 标准发布

ECMAScript 2017 于 2017 年 6 月发布。

### 主要特性

- **async/await**：异步编程语法糖
- **Object.entries()** 和 **Object.values()**
- **字符串填充**：`padStart()`、`padEnd()`
- **Object.getOwnPropertyDescriptors()**
- **共享内存和原子操作**（SharedArrayBuffer、Atomics）

```js
// async/await
async function fetchData() {
    try {
        const response = await fetch('/api/data');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error:', error);
    }
}

// Object.entries() 和 Object.values()
var obj = { a: 1, b: 2, c: 3 };
console.log(Object.entries(obj));  // [['a', 1], ['b', 2], ['c', 3]]
console.log(Object.values(obj));   // [1, 2, 3]

// 字符串填充
var str = "5";
console.log(str.padStart(3, '0'));  // "005"
console.log(str.padEnd(3, '0'));    // "500"
```

## ECMAScript 2018（ES9）

### 标准发布

ECMAScript 2018 于 2018 年 6 月发布。

### 主要特性

- **异步迭代**：`for-await-of`
- **Rest/Spread 属性**：对象解构和展开
- **Promise.prototype.finally()**
- **正则表达式改进**：命名捕获组、后行断言、Unicode 属性转义等

```js
// 异步迭代
async function processItems(items) {
    for await (const item of items) {
        await processItem(item);
    }
}

// Rest/Spread 属性
var { a, ...rest } = { a: 1, b: 2, c: 3 };
var newObj = { ...rest, d: 4 };

// Promise.finally()
promise
    .then(value => console.log(value))
    .catch(error => console.error(error))
    .finally(() => console.log("Done"));

// 正则表达式命名捕获组
var regex = /(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})/;
var match = "2024-12-15".match(regex);
console.log(match.groups.year);   // "2024"
console.log(match.groups.month);  // "12"
```

## ECMAScript 2019（ES10）

### 标准发布

ECMAScript 2019 于 2019 年 6 月发布。

### 主要特性

- **Array.prototype.flat()** 和 **flatMap()**
- **Object.fromEntries()**
- **String.prototype.trimStart()** 和 **trimEnd()**
- **可选 catch 绑定**
- **Symbol.prototype.description**
- **Function.prototype.toString()** 改进

```js
// Array.flat() 和 flatMap()
var nested = [1, [2, 3], [4, [5, 6]]];
var flat = nested.flat(2);  // [1, 2, 3, 4, 5, 6]

var mapped = [1, 2, 3].flatMap(x => [x, x * 2]);  // [1, 2, 2, 4, 3, 6]

// Object.fromEntries()
var entries = [['a', 1], ['b', 2], ['c', 3]];
var obj = Object.fromEntries(entries);  // { a: 1, b: 2, c: 3 }

// 字符串 trim 方法
var str = "  Hello World  ";
console.log(str.trimStart());  // "Hello World  "
console.log(str.trimEnd());    // "  Hello World"

// 可选 catch 绑定
try {
    riskyOperation();
} catch {  // 不需要 error 参数
    console.log("Error occurred");
}
```

## ECMAScript 2020（ES11）

### 标准发布

ECMAScript 2020 于 2020 年 6 月发布。

### 主要特性

- **BigInt**：大整数类型
- **动态 import()**：动态模块导入
- **空值合并运算符**：`??`
- **可选链运算符**：`?.`
- **Promise.allSettled()**
- **globalThis**
- **for-in 顺序保证**

```js
// BigInt
var bigNumber = 9007199254740991n;
var anotherBig = BigInt("9007199254740991");
var sum = bigNumber + anotherBig;

// 动态 import()
async function loadModule() {
    const module = await import('./module.js');
    module.doSomething();
}

// 空值合并运算符
var value = null ?? "default";     // "default"
var value2 = undefined ?? "default";  // "default"
var value3 = 0 ?? "default";      // 0（不是 null/undefined）

// 可选链运算符
var name = user?.profile?.name;
var result = obj?.method?.();
var value = arr?.[0];

// Promise.allSettled()
Promise.allSettled([promise1, promise2, promise3])
    .then(results => {
        results.forEach(result => {
            if (result.status === 'fulfilled') {
                console.log('Success:', result.value);
            } else {
                console.error('Error:', result.reason);
            }
        });
    });

// globalThis
console.log(globalThis === window);  // 浏览器中为 true
console.log(globalThis === global);  // Node.js 中为 true
```

## ECMAScript 2021（ES12）

### 标准发布

ECMAScript 2021 于 2021 年 6 月发布。

### 主要特性

- **String.prototype.replaceAll()**
- **Promise.any()**
- **逻辑赋值运算符**：`&&=`、`||=`、`??=`
- **数字分隔符**：`_`
- **WeakRef** 和 **FinalizationRegistry**

```js
// String.replaceAll()
var str = "hello world world";
var newStr = str.replaceAll("world", "universe");  // "hello universe universe"

// Promise.any()
Promise.any([promise1, promise2, promise3])
    .then(first => console.log("First resolved:", first))
    .catch(errors => console.error("All rejected:", errors));

// 逻辑赋值运算符
var x = 1;
x &&= 2;   // x = x && 2，等价于 if (x) x = 2
x ||= 0;   // x = x || 0，等价于 if (!x) x = 0
x ??= 10;  // x = x ?? 10，等价于 if (x == null) x = 10

// 数字分隔符
var million = 1_000_000;
var binary = 0b1010_0001;
var hex = 0xFF_EC_DE_5E;
```

## ECMAScript 2022（ES13）

### 标准发布

ECMAScript 2022 于 2022 年 6 月发布。

### 主要特性

- **类字段声明**：公共和私有字段
- **私有方法和访问器**
- **静态类字段和方法**
- **Top-level await**
- **Array.prototype.at()**
- **Object.hasOwn()**
- **Error.cause**

```js
// 类字段声明
class Person {
    name = "John";           // 公共字段
    #age = 30;               // 私有字段
    static count = 0;        // 静态字段
    
    #privateMethod() {       // 私有方法
        return this.#age;
    }
    
    get age() {              // 公共访问器
        return this.#age;
    }
    
    static getCount() {      // 静态方法
        return this.count;
    }
}

// Top-level await
const data = await fetch('/api/data').then(r => r.json());

// Array.at()
var arr = [1, 2, 3, 4, 5];
console.log(arr.at(-1));     // 5（最后一个元素）
console.log(arr.at(-2));     // 4

// Object.hasOwn()
var obj = { a: 1 };
console.log(Object.hasOwn(obj, 'a'));  // true
console.log(Object.hasOwn(obj, 'toString'));  // false（继承的属性）
```

## ECMAScript 2023（ES14）

### 标准发布

ECMAScript 2023 于 2023 年 6 月发布。

### 主要特性

- **Array.prototype.findLast()** 和 **findLastIndex()**
- **Hashbang Grammar**：`#!/usr/bin/env node`
- **Symbol 作为 WeakMap 键**

```js
// Array.findLast() 和 findLastIndex()
var arr = [1, 2, 3, 4, 5, 3];
var last = arr.findLast(x => x > 3);        // 5
var lastIndex = arr.findLastIndex(x => x > 3);  // 4

// Hashbang Grammar
#!/usr/bin/env node
console.log("This is a Node.js script");
```

## ECMAScript 2024（ES15）

### 标准发布

ECMAScript 2024 于 2024 年 6 月发布。

### 主要特性

- **Array.prototype.with()**、**toReversed()**、**toSorted()**、**toSpliced()**
- **Promise.withResolvers()**
- **Object.groupBy()** 和 **Map.groupBy()**

```js
// Array 不可变方法
var arr = [1, 2, 3, 4, 5];
var newArr = arr.with(2, 10);      // [1, 2, 10, 4, 5]（不修改原数组）
var reversed = arr.toReversed();    // [5, 4, 3, 2, 1]
var sorted = arr.toSorted();       // [1, 2, 3, 4, 5]

// Promise.withResolvers()
var { promise, resolve, reject } = Promise.withResolvers();
// 可以在外部控制 promise 的解析

// Object.groupBy()
var people = [
    { name: 'John', age: 20 },
    { name: 'Jane', age: 25 },
    { name: 'Bob', age: 20 }
];
var grouped = Object.groupBy(people, person => person.age);
// { 20: [{ name: 'John', age: 20 }, { name: 'Bob', age: 20 }], 25: [{ name: 'Jane', age: 25 }] }
```

## 标准化的重要意义

### 跨平台兼容性

ECMAScript 标准确保了 JavaScript 代码在不同浏览器和运行环境中能够保持一致的行为，这是 Web 开发的基础。

### 向后兼容性

ECMAScript 标准严格遵循向后兼容性原则，确保旧代码在新环境中仍能正常运行。

### 渐进式增强

从 ES2016 开始，ECMAScript 采用每年发布新版本的策略，通过渐进式的方式引入新特性，避免大规模破坏性变更。

### 社区参与

TC39 的开放流程允许社区成员参与标准的制定，确保标准能够反映实际开发需求。

## 未来展望

### 持续演进

ECMAScript 标准将持续演进，每年都会引入新特性和改进。TC39 采用渐进式的方式推进标准，确保向后兼容性。

### 重要趋势

- 类型系统增强（TypeScript 的普及）
- 性能持续优化
- 更好的模块化支持
- 异步编程改进
- WebAssembly 集成
- 模式匹配（Pattern Matching）提案
- 装饰器（Decorators）标准化

## 总结

ECMAScript 标准的演进反映了 JavaScript 从简单脚本语言到现代编程语言的转变。从 ECMAScript 3 的稳定标准，到 ES6 的重大更新，再到每年持续的小版本迭代，ECMAScript 不断演进，适应着现代开发的需求。标准化确保了 JavaScript 的跨平台兼容性和向后兼容性，为 Web 开发提供了坚实的基础。

## 相关资源

- [ECMAScript 官方规范](https://tc39.es/ecma262/)
- [TC39 提案流程](https://tc39.es/process-document/)
- [ECMAScript 兼容性表](https://kangax.github.io/compat-table/es6/)
