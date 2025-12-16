# 1.0.1 JavaScript 起源与发展历程

## 概述

JavaScript 是一种高级的、解释型的编程语言，主要用于 Web 开发。本节介绍 JavaScript 的起源、发展历程和重要里程碑。

## JavaScript 的诞生（1995）

### Brendan Eich 的创造

1995 年，Brendan Eich 在 Netscape 公司（网景公司）工作期间，仅用 10 天时间创建了 JavaScript。当时 Netscape 需要一种脚本语言来增强网页的交互能力。

### 命名历史

JavaScript 最初被命名为 "Mocha"，后来改名为 "LiveScript"，最终在 1995 年 12 月发布时命名为 "JavaScript"。这个命名是为了借助当时流行的 Java 语言的名气，但两者在语言设计上几乎没有关系。

### 第一个版本

1995 年 12 月，Netscape Navigator 2.0 发布了 JavaScript 1.0，这是 JavaScript 的第一个公开版本。JavaScript 1.0 包含：

- 基本的变量和数据类型
- 函数定义和调用
- 简单的 DOM 操作
- 事件处理

```js
// 早期 JavaScript 示例（1995）
function greet(name) {
    alert("Hello, " + name + "!");
}

greet("World");
```

## JavaScript 1.1 - 1.3（1996-1998）

### JavaScript 1.1（1996）

1996 年发布的 JavaScript 1.1 随 Netscape Navigator 3.0 一起发布，主要改进包括：

- 数组对象（Array）
- 字符串对象（String）
- 日期对象（Date）
- 数学对象（Math）
- 正则表达式支持

### JavaScript 1.2（1997）

1997 年发布的 JavaScript 1.2 引入了：

- switch 语句
- 正则表达式字面量
- 数组字面量语法
- 函数字面量

```js
// JavaScript 1.2 新特性
var arr = [1, 2, 3];  // 数组字面量
var regex = /test/;   // 正则表达式字面量

function process(item) {
    switch(item) {
        case 1:
            return "one";
        case 2:
            return "two";
        default:
            return "other";
    }
}
```

### JavaScript 1.3（1998）

1998 年发布的 JavaScript 1.3 主要改进：

- 异常处理（try-catch）
- 数值格式化
- 改进的正则表达式

## ECMAScript 标准化（1997）

### ECMA-262 标准

1997 年，JavaScript 被提交给欧洲计算机制造商协会（ECMA）进行标准化，形成了 ECMA-262 标准。这个标准化的版本被称为 ECMAScript。

### 标准化的重要性

标准化确保了 JavaScript 在不同浏览器和环境中能够保持一致的行为，为 JavaScript 的广泛采用奠定了基础。

## JavaScript 1.4 - 1.5（1999-2000）

### JavaScript 1.4（1999）

1999 年发布的 JavaScript 1.4 引入了：

- 异常处理（try-catch-finally）
- 改进的数组方法
- 新的字符串方法

### JavaScript 1.5（2000）

2000 年发布的 JavaScript 1.5 是 JavaScript 发展史上的重要版本，引入了：

- 异常处理（完整的 try-catch-finally）
- 正则表达式改进
- 新的数组方法（map、filter、reduce 等）
- 函数表达式
- 对象字面量增强

```js
// JavaScript 1.5 新特性
try {
    var result = riskyOperation();
} catch (error) {
    console.log("Error: " + error.message);
} finally {
    cleanup();
}

// 数组方法
var numbers = [1, 2, 3, 4, 5];
var doubled = numbers.map(function(n) {
    return n * 2;
});
```

## ECMAScript 3（1999）- 稳定标准

### 重要里程碑

ECMAScript 3 于 1999 年 12 月发布，这是 JavaScript 历史上第一个真正稳定的标准版本，被广泛采用并持续使用了近 10 年。

### 主要特性

- 正则表达式
- 异常处理
- 更好的字符串处理
- 数值格式化
- 控制流改进

### 影响

ECMAScript 3 成为了 Web 开发的事实标准，几乎所有浏览器都支持这个版本。

## ECMAScript 4 的失败（2000-2008）

### 雄心勃勃的计划

ECMAScript 4 试图引入大量新特性，包括：

- 类（Classes）
- 模块系统
- 类型注解
- 命名空间
- 包系统

### 标准化的失败

由于 ECMAScript 4 的改动过于激进，遭到了主要浏览器厂商的反对，最终在 2008 年被放弃。

### 影响

ECMAScript 4 的失败导致了 JavaScript 标准化的停滞，但也为后来 ECMAScript 5 和 ES6 的渐进式改进奠定了基础。

## ECMAScript 5（2009）- 现代 JavaScript 的起点

### 重要里程碑

ECMAScript 5 于 2009 年 12 月发布，这是 JavaScript 标准化进程中的重要转折点。

### 主要特性

- **严格模式**（"use strict"）
- **JSON 支持**：`JSON.parse()`、`JSON.stringify()`
- **数组方法**：`forEach`、`map`、`filter`、`reduce`、`some`、`every`
- **对象方法**：`Object.keys()`、`Object.create()`、`Object.defineProperty()`
- **函数方法**：`Function.prototype.bind()`
- **字符串方法**：`String.prototype.trim()`

```js
// ECMAScript 5 新特性
"use strict";  // 严格模式

// JSON 支持
var data = JSON.parse('{"name": "John", "age": 30}');
var json = JSON.stringify(data);

// 数组方法
var numbers = [1, 2, 3, 4, 5];
numbers.forEach(function(n) {
    console.log(n);
});

var doubled = numbers.map(function(n) {
    return n * 2;
});

// 对象方法
var obj = Object.create(null);
Object.defineProperty(obj, 'name', {
    value: 'John',
    writable: false,
    enumerable: true,
    configurable: true
});
```

### 影响

ECMAScript 5 为现代 JavaScript 开发奠定了基础，引入了许多现在仍在使用的核心特性。

## ECMAScript 5.1（2011）

### 小版本更新

ECMAScript 5.1 于 2011 年 6 月发布，主要是对 ECMAScript 5 的澄清和修正，没有引入新特性。

## ECMAScript 6 / ES2015（2015）- 重大更新

### 重要里程碑

ECMAScript 6（也称为 ES2015）于 2015 年 6 月发布，这是 JavaScript 历史上最重要的更新之一，引入了大量新特性。

### 主要特性

#### 1. 变量声明

- `let` 和 `const` 关键字
- 块级作用域
- 暂时性死区（TDZ）

```js
// ES6 变量声明
let x = 1;
const y = 2;

{
    let x = 3;  // 块级作用域
    console.log(x);  // 3
}
console.log(x);  // 1
```

#### 2. 箭头函数

```js
// ES6 箭头函数
const add = (a, b) => a + b;
const square = x => x * x;
const greet = () => console.log("Hello");
```

#### 3. 类（Classes）

```js
// ES6 类
class Person {
    constructor(name) {
        this.name = name;
    }
    
    greet() {
        return `Hello, ${this.name}`;
    }
}

class Student extends Person {
    constructor(name, grade) {
        super(name);
        this.grade = grade;
    }
}
```

#### 4. 模块系统

```js
// ES6 模块
// math.js
export function add(a, b) {
    return a + b;
}

export const PI = 3.14159;

// main.js
import { add, PI } from './math.js';
```

#### 5. 解构赋值

```js
// ES6 解构赋值
const [a, b, c] = [1, 2, 3];
const { name, age } = { name: 'John', age: 30 };

function greet({ name, age }) {
    return `Hello, ${name}, age ${age}`;
}
```

#### 6. 模板字符串

```js
// ES6 模板字符串
const name = "John";
const message = `Hello, ${name}!`;
const multiLine = `
    Line 1
    Line 2
`;
```

#### 7. Promise

```js
// ES6 Promise
const promise = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve("Success!");
    }, 1000);
});

promise.then(value => {
    console.log(value);
});
```

#### 8. 其他重要特性

- 默认参数
- 剩余参数（rest parameters）
- 展开运算符（spread operator）
- Symbol 类型
- Set 和 Map
- for...of 循环
- 生成器（Generators）

### 影响

ES6 彻底改变了 JavaScript 的开发方式，引入了现代编程语言的核心特性，为后续版本的发展奠定了基础。

## ECMAScript 2016（ES7）

### 发布时间

ECMAScript 2016 于 2016 年 6 月发布，这是第一个按年份命名的 ECMAScript 版本。

### 主要特性

- **指数运算符**：`**`
- **Array.prototype.includes()**

```js
// ES2016 新特性
const result = 2 ** 8;  // 256

const arr = [1, 2, 3];
console.log(arr.includes(2));  // true
```

## ECMAScript 2017（ES8）

### 发布时间

ECMAScript 2017 于 2017 年 6 月发布。

### 主要特性

- **async/await**：异步编程语法糖
- **Object.entries()** 和 **Object.values()**
- **字符串填充**：`padStart()`、`padEnd()`
- **Object.getOwnPropertyDescriptors()**

```js
// ES2017 async/await
async function fetchData() {
    try {
        const response = await fetch('/api/data');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error(error);
    }
}

// Object.entries() 和 Object.values()
const obj = { a: 1, b: 2, c: 3 };
console.log(Object.entries(obj));  // [['a', 1], ['b', 2], ['c', 3]]
console.log(Object.values(obj));   // [1, 2, 3]
```

## ECMAScript 2018（ES9）

### 发布时间

ECMAScript 2018 于 2018 年 6 月发布。

### 主要特性

- **异步迭代**：`for-await-of`
- **Rest/Spread 属性**：对象解构和展开
- **Promise.prototype.finally()**
- **正则表达式改进**：命名捕获组、后行断言等

```js
// ES2018 新特性
// 异步迭代
async function processItems(items) {
    for await (const item of items) {
        await processItem(item);
    }
}

// Rest/Spread 属性
const { a, ...rest } = { a: 1, b: 2, c: 3 };
const newObj = { ...rest, d: 4 };

// Promise.finally()
promise
    .then(value => console.log(value))
    .catch(error => console.error(error))
    .finally(() => console.log("Done"));
```

## ECMAScript 2019（ES10）

### 发布时间

ECMAScript 2019 于 2019 年 6 月发布。

### 主要特性

- **Array.prototype.flat()** 和 **flatMap()**
- **Object.fromEntries()**
- **String.prototype.trimStart()** 和 **trimEnd()**
- **可选 catch 绑定**
- **Symbol.prototype.description**

```js
// ES2019 新特性
// Array.flat()
const nested = [1, [2, 3], [4, [5, 6]]];
const flat = nested.flat(2);  // [1, 2, 3, 4, 5, 6]

// Object.fromEntries()
const entries = [['a', 1], ['b', 2]];
const obj = Object.fromEntries(entries);  // { a: 1, b: 2 }

// 可选 catch 绑定
try {
    riskyOperation();
} catch {  // 不需要 error 参数
    console.log("Error occurred");
}
```

## ECMAScript 2020（ES11）

### 发布时间

ECMAScript 2020 于 2020 年 6 月发布。

### 主要特性

- **BigInt**：大整数类型
- **动态 import()**：动态模块导入
- **空值合并运算符**：`??`
- **可选链运算符**：`?.`
- **Promise.allSettled()**
- **globalThis**

```js
// ES2020 新特性
// BigInt
const bigNumber = 9007199254740991n;
const anotherBig = BigInt("9007199254740991");

// 空值合并运算符
const value = null ?? "default";  // "default"
const value2 = 0 ?? "default";    // 0

// 可选链运算符
const name = user?.profile?.name;
const result = obj?.method?.();

// Promise.allSettled()
Promise.allSettled([promise1, promise2])
    .then(results => {
        results.forEach(result => {
            if (result.status === 'fulfilled') {
                console.log(result.value);
            } else {
                console.error(result.reason);
            }
        });
    });
```

## ECMAScript 2021（ES12）

### 发布时间

ECMAScript 2021 于 2021 年 6 月发布。

### 主要特性

- **String.prototype.replaceAll()**
- **Promise.any()**
- **逻辑赋值运算符**：`&&=`、`||=`、`??=`
- **数字分隔符**：`_`
- **WeakRef** 和 **FinalizationRegistry**

```js
// ES2021 新特性
// String.replaceAll()
const str = "hello world world";
const newStr = str.replaceAll("world", "universe");

// Promise.any()
Promise.any([promise1, promise2, promise3])
    .then(first => console.log(first))
    .catch(errors => console.error(errors));

// 逻辑赋值运算符
let x = 1;
x &&= 2;  // x = x && 2
x ||= 0;  // x = x || 0
x ??= 10; // x = x ?? 10

// 数字分隔符
const million = 1_000_000;
const binary = 0b1010_0001;
```

## ECMAScript 2022（ES13）

### 发布时间

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
// ES2022 新特性
// 类字段声明
class Person {
    name = "John";           // 公共字段
    #age = 30;               // 私有字段
    static count = 0;        // 静态字段
    
    #privateMethod() {       // 私有方法
        return this.#age;
    }
    
    static getCount() {      // 静态方法
        return this.count;
    }
}

// Top-level await
const data = await fetch('/api/data').then(r => r.json());

// Array.at()
const arr = [1, 2, 3, 4, 5];
console.log(arr.at(-1));  // 5（最后一个元素）

// Object.hasOwn()
const obj = { a: 1 };
console.log(Object.hasOwn(obj, 'a'));  // true
```

## ECMAScript 2023（ES14）

### 发布时间

ECMAScript 2023 于 2023 年 6 月发布。

### 主要特性

- **Array.prototype.findLast()** 和 **findLastIndex()**
- **Hashbang Grammar**：`#!/usr/bin/env node`
- **Symbol 作为 WeakMap 键**

```js
// ES2023 新特性
// Array.findLast()
const arr = [1, 2, 3, 4, 5, 3];
const last = arr.findLast(x => x > 3);  // 5
const lastIndex = arr.findLastIndex(x => x > 3);  // 4
```

## ECMAScript 2024（ES15）

### 发布时间

ECMAScript 2024 于 2024 年 6 月发布。

### 主要特性

- **Array.prototype.with()**、**toReversed()**、**toSorted()**、**toSpliced()**
- **Promise.withResolvers()**
- **Object.groupBy()** 和 **Map.groupBy()**

```js
// ES2024 新特性
// Array 不可变方法
const arr = [1, 2, 3, 4, 5];
const newArr = arr.with(2, 10);      // [1, 2, 10, 4, 5]
const reversed = arr.toReversed();   // [5, 4, 3, 2, 1]
const sorted = arr.toSorted();       // [1, 2, 3, 4, 5]

// Promise.withResolvers()
const { promise, resolve, reject } = Promise.withResolvers();

// Object.groupBy()
const people = [
    { name: 'John', age: 20 },
    { name: 'Jane', age: 25 },
    { name: 'Bob', age: 20 }
];
const grouped = Object.groupBy(people, person => person.age);
```

## JavaScript 运行时的演进

### V8 引擎（2008）

2008 年，Google 发布了 V8 JavaScript 引擎，这是一个高性能的 JavaScript 引擎，显著提升了 JavaScript 的执行速度。

### Node.js（2009）

2009 年，Ryan Dahl 创建了 Node.js，将 JavaScript 带到了服务器端，开启了全栈 JavaScript 开发的时代。

### 现代运行时

- **Deno**（2018）：由 Node.js 创始人创建的新运行时
- **Bun**（2022）：高性能的 JavaScript 运行时

## JavaScript 的未来

### 持续演进

JavaScript 标准每年都会发布新版本，持续引入新特性和改进。ECMAScript 委员会采用渐进式的方式推进标准，确保向后兼容性。

### 重要趋势

- 类型系统增强（TypeScript 的普及）
- 性能持续优化
- 更好的模块化支持
- 异步编程改进
- WebAssembly 集成

## 练习

1. **版本特性识别**：识别代码中使用的 ECMAScript 版本特性，判断需要的最低版本支持。

2. **历史特性演示**：编写代码演示不同 ECMAScript 版本的重要特性（ES5、ES6、ES2020 等）。

3. **兼容性检查**：使用工具检查代码的浏览器兼容性，了解不同版本特性的支持情况。

4. **版本演进理解**：总结 JavaScript 从 ES5 到 ES2024 的主要演进路径和重要特性。

5. **现代特性应用**：使用 ES2020+ 的新特性（可选链、空值合并、top-level await 等）编写代码。

完成以上练习后，继续学习下一节，了解 ECMAScript 的演进。

## 总结

JavaScript 从 1995 年诞生至今，经历了近 30 年的发展，从一个简单的脚本语言发展成为现代 Web 开发的核心技术。从 ECMAScript 3 的稳定标准，到 ES6 的重大更新，再到每年持续的小版本迭代，JavaScript 不断演进，适应着现代开发的需求。

## 相关资源

- [ECMAScript 官方规范](https://tc39.es/ecma262/)
- [MDN JavaScript 文档](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript)
- [JavaScript 历史时间线](https://en.wikipedia.org/wiki/JavaScript#History)
