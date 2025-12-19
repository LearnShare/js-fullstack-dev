# 阶段二：核心模块与基础 API（核心能力）

## 1. 概述

阶段二旨在掌握 Node.js 的核心模块与基础 API，这些是构建全栈应用的基础能力。重点涵盖模块系统、文件系统、HTTP 模块、事件系统、加密安全、Buffer 与 Stream、URL 处理、工具函数、操作系统信息、子进程与集群等核心内容。通过本阶段的学习，开发者应能够熟练使用 Node.js 内置模块进行后端开发。

## 2. 章节目录

| 章节编号 | 章节名称                                                       | 核心逻辑与技术点                                 |
|:---------|:---------------------------------------------------------------|:-------------------------------------------------|
| **2.1**  | [模块系统](chapter-01-modules/readme.md)                       | CommonJS 与 ESM 模块系统、模块解析与加载机制。  |
| **2.2**  | [文件系统（fs）](chapter-02-fs/readme.md)                      | 文件读写、目录操作、文件监听、Promise 版本 API。|
| **2.3**  | [路径处理（path）](chapter-03-path/readme.md)                 | 路径拼接与解析、跨平台兼容性处理。              |
| **2.4**  | [HTTP 模块](chapter-04-http/readme.md)                         | HTTP 服务器与客户端、请求与响应处理。            |
| **2.5**  | [事件系统（events）](chapter-05-events/readme.md)              | EventEmitter 基础、事件监听与触发、自定义事件。  |
| **2.6**  | [加密与安全（crypto）](chapter-06-crypto/readme.md)           | 哈希算法、加密解密、数字签名。                    |
| **2.7**  | [Buffer 与 Stream](chapter-07-buffer-stream/readme.md)        | Buffer 基础、Stream 类型、管道与背压处理。       |
| **2.8**  | [URL 与查询字符串处理](chapter-08-url-querystring/readme.md)  | URL 解析与构建、查询字符串处理。                  |
| **2.9**  | [工具函数（util）](chapter-09-util/readme.md)                 | promisify、类型检查、调试工具。                   |
| **2.10** | [操作系统与进程信息](chapter-10-os-process/readme.md)          | os 模块、process 模块、环境变量与配置。           |
| **2.11** | [子进程与集群](chapter-11-child-cluster/readme.md)             | child_process 模块、cluster 模块基础。            |

## 3. 学习目标

- **掌握模块系统**：理解 CommonJS 与 ESM 的区别和使用场景。
- **文件操作能力**：熟练使用 fs 模块进行文件读写和目录操作。
- **HTTP 开发**：能够使用原生 HTTP 模块创建服务器和客户端。
- **事件驱动编程**：掌握 EventEmitter 的使用和自定义事件。
- **安全基础**：了解加密、哈希、数字签名等安全机制。
- **流式处理**：理解 Buffer 和 Stream 的使用场景和处理方式。

## 4. 前置知识要求

学习本阶段前，需要掌握：

- **阶段一内容**：Node.js 运行时架构、TypeScript 项目初始化
- **JavaScript 基础**：异步编程、Promise、async/await
- **TypeScript 基础**：类型系统、接口、类型注解

## 5. 学习建议

1. **实践为主**：每个模块都要编写代码示例并运行验证。
2. **理解原理**：理解模块系统、事件循环等底层机制。
3. **对比学习**：对比 CommonJS 与 ESM、同步与异步 API 的区别。
4. **安全意识**：在学习加密模块时，理解安全最佳实践。

## 6. 预计学习时间

- **总学习时间**：约 4-6 周
- **每日学习时间**：2-3 小时
- **预计完成时间**：1-2 个月

---

**版本说明**：2025.12 版 | 适用 Node.js 22+
