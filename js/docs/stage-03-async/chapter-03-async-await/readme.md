# 3.3 async/await

## 目标

- 理解 async/await 的概念和用途
- 掌握 async 函数的使用
- 理解 await 表达式的工作原理
- 掌握 async/await 的错误处理
- 了解并行执行和性能优化

## 章节内容

本章分为四个独立小节，每节提供详细的概念解释和完整示例：

1. **[async/await 概述](section-01-overview.md)**：async/await 的概念、优势和基本用法

2. **[async 函数](section-02-async-functions.md)**：async 函数的定义、返回值和特性

3. **[await 表达式](section-03-await.md)**：await 的使用、等待机制和注意事项

4. **[错误处理与并行执行](section-04-error-parallel.md)**：async/await 的错误处理和并行执行优化

## 核心概念

- **async 函数**：返回 Promise 的函数
- **await 表达式**：等待 Promise 完成并返回结果
- **语法糖**：async/await 是 Promise 的语法糖，使异步代码更像同步代码
- **错误处理**：使用 try/catch 处理异步错误
- **并行执行**：使用 Promise.all 实现并行执行

## 学习建议

1. **理解概念**：async/await 是基于 Promise 的语法糖
2. **多实践**：通过大量练习掌握 async/await 的使用
3. **错误处理**：学会使用 try/catch 处理异步错误
4. **性能优化**：理解并行执行和串行执行的区别

## 完成本章后

- 能够使用 async/await 编写异步代码
- 理解 async 函数和 await 表达式的工作原理
- 能够正确处理异步错误
- 掌握并行执行和性能优化

## 相关章节

- **3.2 Promise**：async/await 基于 Promise，需要理解 Promise
- **3.1 事件循环机制**：理解事件循环有助于理解 async/await 的执行
