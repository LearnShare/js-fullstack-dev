# 2.12.1 JavaScript 版本新特性概述

## 概述

自 ES2015 起，JavaScript 进入年度发布节奏。理解各版本的重要特性有助于编写现代、简洁且可维护的代码，也能指导你在项目中合理选择语法并配置编译目标。本节按时间线列出关键特性，并给出适用场景与示例。

## ES2015（ES6）—— 里程碑版本

- `let` / `const`：块级作用域与不可变绑定
- 解构赋值、展开与剩余：对象/数组拆解、函数参数聚合
- 模板字符串：插值、多行、标签模板
- 箭头函数：简洁写法、词法 this
- `class` / `extends` / `super`：面向对象语法糖
- 模块（ESM）：`import` / `export`
- `Promise`：异步基础
- `Map` / `Set` / `WeakMap` / `WeakSet`
- 迭代器 / 生成器：`for...of`、`yield`
- `Symbol`：唯一标识
- 默认参数、参数展开、尾调用优化（实现依赖引擎）

示例：模板字符串 + 解构
```js
const user = { name: 'Alice', age: 20 };
const { name, age } = user;
console.log(`Hi ${name}, ${age} years old`);
```

## ES2016
- `Array.prototype.includes`
- 指数运算符 `**`

## ES2017
- `async/await`
- `Object.values` / `Object.entries`
- 字符串填充：`padStart` / `padEnd`
- `Trailing commas`（函数参数/调用）

示例：async/await
```js
async function load() {
  try {
    const data = await fetch('/api').then(r => r.json());
    return data;
  } catch {
    return null;
  }
}
```

## ES2018
- 对象展开/剩余：`{ ...obj }`
- `Promise.prototype.finally`
- 弱化转义规则的模板字符串
- 正则改进：`dotAll (s)`、命名捕获组、后行断言、Unicode 属性类 `\p{...}`

## ES2019
- `Array.prototype.flat` / `flatMap`
- `Object.fromEntries`
- `String.prototype.trimStart/trimEnd`
- 可选 catch 绑定：`catch { ... }`

## ES2020
- `BigInt`
- 可选链 `?.`
- 空值合并 `??`
- 动态 import：`import()`
- `Promise.allSettled`
- `globalThis`
- `for-in` 规范化枚举顺序

示例：可选链 + 空值合并
```js
const city = user?.profile?.address?.city ?? 'Unknown';
```

## ES2021
- `String.prototype.replaceAll`
- 逻辑赋值运算符：`&&=`, `||=`, `??=`
- `Promise.any` + `AggregateError`
- `WeakRef` 与 `FinalizationRegistry`

## ES2022
- 类字段与私有字段（公共/私有静态、实例）
- 私有方法/访问器
- `Error` cause：`new Error(message, { cause })`
- 顶层 await（ESM）
- `Array.prototype.at`（负索引访问）

示例：私有字段与顶层 await
```js
class Counter {
  #count = 0;
  inc() { this.#count += 1; return this.#count; }
}

const data = await fetch('/config').then(r => r.json());
```

## ES2023
- `Array.prototype.findLast` / `findLastIndex`
- 复制方法：`toReversed`、`toSorted`、`toSpliced`、`with`（不变式副本）
- 正则 /v 标志（可编排正则模式，提案阶段不同引擎进度可能不一）

## ES2024（已定稿的亮点）
- 迭代器帮助函数：`Iterator.prototype.map/filter/take/drop/...`（提案推进中，浏览器与 Node 支持需关注版本）
- Promise withResolvers（TC39 进展中，需关注环境支持）
- 部分特性仍在落地中，具体可查 MDN/compat 表

## 选型与兼容

- 浏览器/Node 版本直接决定可用特性；低版本需 Babel/SWC 等转译 + Polyfill（core-js）。
- 构建工具 target：`es2018`/`es2020`/`es2022` 取决于最低运行环境。
- 对大数运算选择 BigInt，注意与 Number 不可混算。
- 顶层 await 仅在 ESM 中可用。
- 私有字段不可通过反射访问，调试/序列化需考虑可观测性。

## 最佳实践

1) 在新项目中优先采用现代语法（可选链、空合并、类字段、顶层 await），并通过构建工具兼容旧环境。  
2) 对外部接口和公用库：明确编译目标与兼容矩阵（browserslist/engines）。  
3) 使用 Polyfill 按需注入，避免全量引入；结合 `core-js` 和 `usage` 模式。  
4) 关注 BigInt 与 Number 的混用限制，提供转换或 API 约束。  
5) 在代码审查中鼓励语法更新：replaceAll、findLast、at 等提升可读性。  

## 练习

1. 用可选链/空值合并重构一段嵌套属性读取代码。  
2. 用 `Promise.any` + `AggregateError` 实现“最快成功”策略，并处理全部失败。  
3. 写一个使用私有字段的类，并暴露公共方法读取其状态。  
4. 在 ESM 模块中使用顶层 await 获取远端配置，然后导出配置对象。  
5. 使用 `findLast`/`toSorted` 重构数组处理逻辑，对比旧写法可读性。  

## 总结

- ES2015 奠定现代 JS 基础；后续每年持续迭代补齐语法和标准库能力。  
- 关注环境支持和构建目标，按需转译与 Polyfill。  
- 善用现代特性（可选链、空合并、类字段、顶层 await、findLast、replaceAll 等）可显著提升代码简洁性与安全性。  

完成阶段二学习后，继续学习阶段三：异步编程。
