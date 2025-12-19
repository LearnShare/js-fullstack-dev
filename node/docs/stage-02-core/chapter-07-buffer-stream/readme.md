# 2.7 Buffer 与 Stream

## 章节概述

Buffer 和 Stream 是 Node.js 处理二进制数据和流式数据的核心机制。Buffer 用于处理二进制数据，Stream 用于处理数据流。理解 Buffer 和 Stream 对于处理文件、网络通信、大文件操作等场景至关重要。

## 学习目标

完成本章学习后，你将能够：

- 理解 Buffer 的基本概念和使用
- 掌握 Stream 的类型和使用
- 理解管道（pipe）和背压（backpressure）处理
- 在实际项目中应用 Buffer 和 Stream

## 前置知识

学习本章前，需要掌握：

- Node.js 核心模块基础
- 文件系统基础
- 异步编程基础

## 章节结构

本章包含以下小节：

1. **Buffer 与 Stream 概述**：Buffer 和 Stream 的基本概念
2. **Buffer 基础**：Buffer 的创建、操作和使用
3. **Stream 基础**：Stream 的类型和基本使用
4. **可读流、可写流、双工流**：不同类型的 Stream
5. **管道（pipe）与背压（backpressure）**：Stream 的高级用法

## 学习建议

1. **理解概念**：重点理解 Buffer 和 Stream 的基本概念
2. **实践为主**：通过代码示例理解 Buffer 和 Stream 的使用
3. **性能考虑**：理解 Stream 对性能的影响
4. **实际应用**：在实际项目中应用 Buffer 和 Stream

## 预计学习时间

- **总学习时间**：约 4-5 小时
- **每日学习时间**：1-2 小时
- **预计完成时间**：2-3 天

## 相关章节

- **2.2 文件系统（fs）**：文件操作使用 Stream
- **2.4 HTTP 模块**：HTTP 请求和响应使用 Stream

完成本章学习后，继续学习下一章：URL 与查询字符串处理。
