# 3.2 Promise

## 目标

- 理解 Promise 的概念和用途
- 掌握 Promise 的创建和使用
- 理解 Promise 的状态转换
- 掌握 Promise 链式调用和错误处理
- 了解 Promise 组合方法的使用

## 章节内容

本章分为五个独立小节，每节提供详细的概念解释和完整示例：

1. **[Promise 概述](section-01-overview.md)**：Promise 的概念、解决的问题和基本用法

2. **[Promise 基础](section-02-basics.md)**：Promise 的创建、状态和基本方法

3. **[Promise 链式调用](section-03-chaining.md)**：Promise 链的构建和执行流程

4. **[Promise 组合方法](section-04-composition.md)**：Promise.all、Promise.race、Promise.allSettled 等方法

5. **[Promise 错误处理](section-05-error-handling.md)**：Promise 的错误处理机制和最佳实践

## 核心概念

- **Promise**：表示一个异步操作的最终完成或失败
- **状态**：pending（等待）、fulfilled（成功）、rejected（失败）
- **链式调用**：通过 then 方法串联多个异步操作
- **错误处理**：使用 catch 方法处理错误
- **组合方法**：Promise.all、Promise.race 等组合多个 Promise

## 学习建议

1. **理解概念**：深入理解 Promise 的三种状态和状态转换
2. **多实践**：通过大量练习掌握 Promise 的使用
3. **理解链式调用**：掌握 Promise 链的执行流程
4. **错误处理**：学会正确处理 Promise 的错误

## 完成本章后

- 能够创建和使用 Promise
- 理解 Promise 的状态转换
- 能够构建 Promise 链处理复杂的异步场景
- 掌握 Promise 的错误处理和组合方法

## 相关章节

- **3.1 事件循环机制**：Promise 是微任务，需要理解事件循环
- **3.3 async/await**：async/await 基于 Promise，是 Promise 的语法糖
