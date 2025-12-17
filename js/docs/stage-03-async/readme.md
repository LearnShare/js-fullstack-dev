# 阶段三：异步编程（核心能力）

## 目标

本阶段旨在帮助学习者深入理解 JavaScript 的异步编程机制，掌握事件循环、Promise、async/await、生成器等核心概念，能够编写高质量的异步代码，处理复杂的异步场景。

## 前置知识要求

完成阶段二的学习，掌握：

- JavaScript 基础语法（变量、函数、对象、数组等）
- 函数的高级用法（闭包、高阶函数）
- 作用域和作用域链
- 控制结构（循环、条件语句）

## 学习时间估算

- **总学习时间**：约 50-70 小时
- **每日学习时间**：2-3 小时
- **预计完成时间**：4-6 周

## 核心内容

本阶段涵盖 JavaScript 异步编程的四大核心主题：

1. **事件循环机制**：理解 JavaScript 单线程执行模型和事件循环的工作原理
2. **Promise**：掌握 Promise 的创建、链式调用和错误处理
3. **async/await**：使用现代异步语法简化异步代码
4. **生成器与迭代器**：理解生成器函数和迭代器协议

## 学习建议

1. **理解原理**：异步编程是 JavaScript 的核心特性，需要深入理解事件循环机制
2. **多实践**：通过大量练习掌握 Promise 和 async/await 的使用
3. **循序渐进**：先理解事件循环，再学习 Promise，最后掌握 async/await
4. **项目练习**：完成每章后的练习任务，在实际项目中应用异步编程

## 章节内容

本阶段包含 4 个主要章节，每个章节都包含多个小节，提供详细的概念解释、语法说明、参数列表和完整示例：

### 3.1 事件循环机制

理解 JavaScript 的单线程模型和事件循环机制，掌握调用栈、任务队列、宏任务和微任务的概念。

- [3.1.1 事件循环机制概述](chapter-01-event-loop/section-01-overview.md)
- [3.1.2 调用栈与任务队列](chapter-01-event-loop/section-02-call-stack.md)
- [3.1.3 宏任务与微任务](chapter-01-event-loop/section-03-macro-micro.md)
- [3.1.4 浏览器与 Node.js 的事件循环差异](chapter-01-event-loop/section-04-differences.md)

### 3.2 Promise

掌握 Promise 的创建、状态转换、链式调用和错误处理，理解 Promise 组合方法的使用。

- [3.2.1 Promise 概述](chapter-02-promise/section-01-overview.md)
- [3.2.2 Promise 基础](chapter-02-promise/section-02-basics.md)
- [3.2.3 Promise 链式调用](chapter-02-promise/section-03-chaining.md)
- [3.2.4 Promise 组合方法（all、race、allSettled）](chapter-02-promise/section-04-composition.md)
- [3.2.5 Promise 错误处理](chapter-02-promise/section-05-error-handling.md)

### 3.3 async/await

使用 async/await 语法简化异步代码，掌握错误处理和并行执行的方法。

- [3.3.1 async/await 概述](chapter-03-async-await/section-01-overview.md)
- [3.3.2 async 函数](chapter-03-async-await/section-02-async-functions.md)
- [3.3.3 await 表达式](chapter-03-async-await/section-03-await.md)
- [3.3.4 错误处理与并行执行](chapter-03-async-await/section-04-error-parallel.md)

### 3.4 生成器与迭代器

理解迭代器协议、生成器函数的创建和使用，掌握异步生成器的应用。

- [3.4.1 生成器与迭代器概述](chapter-04-generators/section-01-overview.md)
- [3.4.2 迭代器协议](chapter-04-generators/section-02-iterators.md)
- [3.4.3 生成器函数](chapter-04-generators/section-03-generators.md)
- [3.4.4 异步生成器](chapter-04-generators/section-04-async-generators.md)

## 完成本阶段后

- 能够深入理解 JavaScript 的事件循环机制
- 熟练使用 Promise 处理异步操作
- 能够使用 async/await 编写清晰的异步代码
- 理解生成器和迭代器的工作原理
- 能够处理复杂的异步场景和错误处理

## 相关章节

- **阶段二：JavaScript 基础语法**：异步编程需要扎实的语言基础
- **阶段四：浏览器环境与 DOM**：异步编程在前端开发中的应用
