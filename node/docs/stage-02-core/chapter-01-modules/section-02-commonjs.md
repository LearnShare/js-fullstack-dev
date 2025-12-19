# 2.1.2 CommonJS 模块

## 1. 概述

CommonJS 是 Node.js 最早采用的模块系统，使用 `require()` 和 `module.exports` 进行模块的导入和导出。虽然 ES Modules 是未来的标准，但理解 CommonJS 对于维护传统项目和理解 Node.js 的模块系统仍然很重要。

## 2. 特性说明

- **动态加载**：模块在运行时动态加载，支持条件导入。
- **同步加载**：模块加载是同步的，适合服务器端环境。
- **缓存机制**：已加载的模块会被缓存，避免重复加载。
- **向后兼容**：Node.js 的默认模块系统，兼容性最好。
- **灵活导出**：支持多种导出方式（对象、函数、类等）。

## 3. 语法与定义

### 模块导出

CommonJS 使用 `module.exports` 或 `exports` 导出模块：

```ts
// 方式 1：直接导出对象
module.exports = {
    add: (a: number, b: number) => a + b,
    subtract: (a: number, b: number) => a - b
};

// 方式 2：逐个导出属性
exports.add = (a: number, b: number) => a + b;
exports.subtract = (a: number, b: number) => a - b;

// 方式 3：导出单个值
module.exports = function calculate(a: number, b: number) {
    return a + b;
};
```

### 模块导入

CommonJS 使用 `require()` 导入模块：

```ts
// 导入整个模块
const math = require('./math.cjs');

// 解构导入
const { add, subtract } = require('./math.cjs');

// 导入核心模块
const fs = require('node:fs');
const path = require('node:path');
```

## 4. 基本用法

### 示例 1：导出和导入函数

```ts
// 文件: utils.cjs
// 功能: 工具函数模块

function formatDate(date: Date): string {
    return date.toISOString();
}

function formatCurrency(amount: number): string {
    return `$${amount.toFixed(2)}`;
}

module.exports = {
    formatDate,
    formatCurrency
};
```

```ts
// 文件: main.cjs
// 功能: 使用工具函数

const { formatDate, formatCurrency } = require('./utils.cjs');

const date = new Date();
console.log(formatDate(date));
console.log(formatCurrency(100.5));
```

### 示例 2：导出类

```ts
// 文件: user.cjs
// 功能: 用户类模块

class User {
    constructor(public name: string, public age: number) {}

    greet(): string {
        return `Hello, I'm ${this.name}, ${this.age} years old.`;
    }
}

module.exports = User;
```

```ts
// 文件: main.cjs
// 功能: 使用用户类

const User = require('./user.cjs');

const user = new User('Alice', 25);
console.log(user.greet());
```

## 5. 参数说明：require() 函数

`require()` 函数接受一个模块标识符（字符串）：

| 参数类型     | 示例                           | 说明                                     |
|:-------------|:-------------------------------|:-----------------------------------------|
| **核心模块** | `'node:fs'`                    | Node.js 内置模块，使用 `node:` 前缀。     |
| **相对路径** | `'./utils.cjs'`                | 相对于当前文件的路径。                   |
| **绝对路径** | `'/path/to/module.cjs'`        | 绝对路径（不推荐）。                     |
| **包名**     | `'express'`                    | 从 `node_modules` 查找。                 |

## 6. 返回值与状态说明

`require()` 返回模块的导出对象：

| 返回类型     | 说明                                     | 示例                           |
|:-------------|:-----------------------------------------|:-------------------------------|
| **Object**   | 模块导出的对象                           | `{ add, subtract }`            |
| **Function** | 模块导出的函数                           | `function calculate() {}`      |
| **Class**    | 模块导出的类                             | `class User {}`                |
| **Primitive**| 模块导出的原始值（不常见）               | `42`                           |

## 7. 代码示例：模块缓存机制

CommonJS 模块会被缓存，多次 `require()` 同一模块只会执行一次：

```ts
// 文件: counter.cjs
// 功能: 演示模块缓存

let count = 0;

function increment(): number {
    return ++count;
}

console.log('Module loaded'); // 只会执行一次

module.exports = { increment };
```

```ts
// 文件: main.cjs
// 功能: 多次导入同一模块

const counter1 = require('./counter.cjs');
const counter2 = require('./counter.cjs');

console.log(counter1.increment()); // 1
console.log(counter2.increment()); // 2（共享同一个 count）
```

## 8. 输出结果说明

```text
Module loaded
1
2
```

**逻辑解析**：
- 第一次 `require()` 时，模块代码执行，`count` 初始化为 0
- 第二次 `require()` 时，返回缓存的模块，不会重新执行代码
- `counter1` 和 `counter2` 引用同一个模块实例，共享 `count` 变量

## 9. 使用场景

### 1. 传统 Node.js 项目

在传统 Node.js 项目中使用 CommonJS：

```ts
// 传统 Express 应用
const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('Hello World');
});

app.listen(3000);
```

### 2. 向后兼容

维护需要向后兼容的代码库：

```ts
// 兼容旧版本的代码
if (typeof module !== 'undefined' && module.exports) {
    module.exports = MyLibrary;
}
```

### 3. 条件导入

利用动态加载实现条件导入：

```ts
// 根据环境条件导入不同模块
const config = process.env.NODE_ENV === 'production'
    ? require('./config.prod.cjs')
    : require('./config.dev.cjs');
```

## 10. 注意事项与常见错误

- **文件扩展名**：CommonJS 文件通常使用 `.cjs` 扩展名（在 ESM 项目中）
- **exports vs module.exports**：`exports` 是 `module.exports` 的引用，不能直接赋值
- **循环依赖**：CommonJS 支持循环依赖，但可能导致部分导出为 `undefined`
- **同步加载**：`require()` 是同步的，会阻塞执行，不适合浏览器环境
- **缓存机制**：模块会被缓存，修改模块文件后需要重启应用才能生效

## 11. 常见问题 (FAQ)

**Q: `exports` 和 `module.exports` 有什么区别？**
A: `exports` 是 `module.exports` 的引用。直接给 `exports` 赋值不会生效，应该使用 `module.exports` 或给 `exports` 的属性赋值。

**Q: CommonJS 模块可以导入 ESM 模块吗？**
A: 不能直接导入。需要使用动态 `import()` 或 `createRequire()` 函数。

**Q: 如何判断模块是否已加载？**
A: 使用 `require.cache` 对象检查模块缓存：

```ts
if (require.cache[require.resolve('./module.cjs')]) {
    console.log('Module already loaded');
}
```

## 12. 最佳实践

- **明确导出**：使用 `module.exports` 明确导出，避免混用 `exports`
- **类型定义**：为 CommonJS 模块添加 TypeScript 类型定义
- **避免循环依赖**：设计模块结构时避免循环依赖
- **使用 node: 前缀**：导入核心模块时使用 `node:` 前缀
- **文件扩展名**：在 ESM 项目中，CommonJS 文件使用 `.cjs` 扩展名

## 13. 对比分析：CommonJS vs ES Modules

| 维度             | CommonJS                                    | ES Modules                                  |
|:-----------------|:--------------------------------------------|:--------------------------------------------|
| **语法**         | `require()` / `module.exports`              | `import` / `export`                         |
| **加载时机**     | 运行时动态加载                              | 编译时静态分析                              |
| **同步/异步**    | 同步                                        | 异步                                        |
| **Tree Shaking** | 不支持                                      | 支持                                        |
| **Top-level await** | 不支持                                  | 支持                                        |
| **浏览器支持**    | 需要构建工具                                | 现代浏览器原生支持                          |

## 14. 练习任务

1. **模块导出实践**：
   - 创建工具函数模块，使用 `module.exports` 导出
   - 尝试不同的导出方式（对象、函数、类）
   - 理解导出方式的区别

2. **模块导入实践**：
   - 创建主文件，使用 `require()` 导入模块
   - 尝试不同的导入方式（整体导入、解构导入）
   - 理解导入方式的区别

3. **模块缓存实验**：
   - 创建带状态的模块（如计数器）
   - 多次 `require()` 同一模块
   - 观察模块缓存的行为

4. **循环依赖实验**：
   - 创建两个相互依赖的模块
   - 观察循环依赖的行为
   - 理解如何避免循环依赖

5. **实际应用**：
   - 在实际项目中使用 CommonJS 组织代码
   - 理解 CommonJS 的适用场景
   - 掌握 CommonJS 的最佳实践

完成以上练习后，继续学习下一节：ES Modules (ESM)。

## 总结

CommonJS 是 Node.js 的传统模块系统：

- **语法**：使用 `require()` 和 `module.exports`
- **特点**：动态加载、同步执行、模块缓存
- **适用场景**：传统项目、向后兼容
- **最佳实践**：明确导出、避免循环依赖、使用类型定义

理解 CommonJS 有助于维护传统项目和理解 Node.js 的模块系统。

---

**最后更新**：2025-01-XX
