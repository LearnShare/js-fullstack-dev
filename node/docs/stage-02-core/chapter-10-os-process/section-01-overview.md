# 2.10.1 os 和 process 模块概述

## 1. 概述

os 和 process 模块是 Node.js 中用于访问系统信息和进程信息的核心模块。os 模块提供操作系统相关信息（如平台、CPU、内存、网络接口等），process 模块提供当前 Node.js 进程的信息和控制能力（如环境变量、命令行参数、进程退出等）。理解这些模块对于系统监控、性能优化、进程管理等场景非常重要。

## 2. 特性说明

- **操作系统信息**：获取操作系统平台、架构、CPU、内存等信息。
- **进程信息**：访问当前进程的 ID、工作目录、环境变量等。
- **进程控制**：控制进程的退出、信号处理等。
- **系统监控**：监控系统资源使用情况。
- **跨平台支持**：提供跨平台的一致性 API。

## 3. 模块导入方式

### ES Modules 方式

```ts
import os from 'node:os';
import process from 'node:process';
```

### CommonJS 方式

```ts
const os = require('node:os');
const process = require('node:process');
```

## 4. 主要功能概览

| 模块     | 主要功能                                     | 示例                           |
|:---------|:---------------------------------------------|:-------------------------------|
| **os**   | 操作系统信息（平台、CPU、内存、网络等）      | `os.platform()`, `os.cpus()`   |
| **process**| 进程信息和控制（ID、环境变量、退出等）    | `process.pid`, `process.env`   |

## 5. 参数说明：os 和 process 常用 API

| API 名称      | 说明                                     | 示例                           |
|:--------------|:-----------------------------------------|:-------------------------------|
| **os.platform()**| 获取操作系统平台                        | `'win32'`, `'linux'`, `'darwin'`|
| **os.cpus()**| 获取 CPU 信息                            | `[{ model: '...', speed: ... }]`|
| **os.totalmem()**| 获取总内存（字节）                      | `8589934592`                   |
| **process.pid**| 当前进程 ID                              | `12345`                        |
| **process.env**| 环境变量对象                             | `{ NODE_ENV: 'production' }`   |

## 6. 返回值与状态说明

os 和 process 操作的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **os 方法**  | 各种类型     | 根据方法返回不同类型（字符串、对象、数字等）|
| **process 属性**| 各种类型   | 根据属性返回不同类型                     |

## 7. 代码示例：基本使用

以下示例演示了 os 和 process 模块的基本使用：

```ts
// 文件: os-process-basic.ts
// 功能: os 和 process 模块基本使用

import os from 'node:os';
import process from 'node:process';

// 1. 操作系统信息
console.log('Platform:', os.platform());           // win32, linux, darwin
console.log('Architecture:', os.arch());            // x64, arm64
console.log('Hostname:', os.hostname());            // 主机名
console.log('Total Memory:', os.totalmem());        // 总内存（字节）
console.log('Free Memory:', os.freemem());          // 空闲内存（字节）
console.log('CPU Count:', os.cpus().length);        // CPU 核心数

// 2. 进程信息
console.log('Process ID:', process.pid);            // 进程 ID
console.log('Node Version:', process.version);      // Node.js 版本
console.log('Platform:', process.platform);         // 平台
console.log('Working Directory:', process.cwd());    // 工作目录
console.log('Environment:', process.env.NODE_ENV);  // 环境变量
```

## 8. 输出结果说明

os 和 process 模块的输出结果：

```text
Platform: win32
Architecture: x64
Hostname: DESKTOP-ABC123
Total Memory: 8589934592
Free Memory: 4294967296
CPU Count: 8
Process ID: 12345
Node Version: v22.0.0
Platform: win32
Working Directory: C:\works
Environment: development
```

**逻辑解析**：
- os 模块提供系统级信息
- process 模块提供进程级信息
- 这些信息可以用于系统监控和进程管理

## 9. 使用场景

### 1. 系统监控

监控系统资源使用情况：

```ts
// 系统监控示例
import os from 'node:os';

function getSystemInfo() {
    return {
        platform: os.platform(),
        cpuCount: os.cpus().length,
        totalMemory: os.totalmem(),
        freeMemory: os.freemem(),
        memoryUsage: (1 - os.freemem() / os.totalmem()) * 100
    };
}
```

### 2. 环境配置

根据环境变量配置应用：

```ts
// 环境配置示例
import process from 'node:process';

const config = {
    env: process.env.NODE_ENV || 'development',
    port: parseInt(process.env.PORT || '3000', 10),
    database: process.env.DATABASE_URL || 'localhost'
};
```

### 3. 进程管理

管理进程生命周期：

```ts
// 进程管理示例
import process from 'node:process';

// 优雅退出
process.on('SIGTERM', () => {
    console.log('Received SIGTERM, shutting down gracefully');
    process.exit(0);
});
```

## 10. 注意事项与常见错误

- **跨平台差异**：注意不同平台的差异
- **内存单位**：内存值以字节为单位，需要转换
- **环境变量**：环境变量都是字符串，需要类型转换
- **进程退出**：正确使用进程退出，避免资源泄漏
- **信号处理**：理解不同信号的含义

## 11. 常见问题 (FAQ)

**Q: os 和 process 有什么区别？**
A: os 提供操作系统级信息，process 提供进程级信息和控制。

**Q: 如何获取内存使用率？**
A: 使用 `(1 - os.freemem() / os.totalmem()) * 100` 计算。

**Q: 环境变量都是字符串吗？**
A: 是的，环境变量都是字符串，需要手动转换为其他类型。

## 12. 最佳实践

- **系统监控**：使用 os 模块监控系统资源
- **环境配置**：使用 process.env 进行环境配置
- **进程管理**：正确处理进程退出和信号
- **跨平台**：注意跨平台差异，使用跨平台 API
- **性能考虑**：某些操作可能有性能开销

## 13. 对比分析：os vs process

| 维度             | os 模块                                    | process 模块                              |
|:-----------------|:-------------------------------------------|:-------------------------------------------|
| **信息范围**     | 操作系统级信息                             | 进程级信息                                 |
| **控制能力**     | 只读，获取信息                             | 可控制进程行为                             |
| **使用场景**     | 系统监控、资源检查                          | 进程管理、环境配置                          |

## 14. 练习任务

1. **os 模块实践**：
   - 获取操作系统信息
   - 监控系统资源
   - 实现系统信息工具

2. **process 模块实践**：
   - 访问进程信息
   - 处理环境变量
   - 实现进程管理

3. **实际应用**：
   - 在实际项目中应用 os 和 process 模块
   - 实现系统监控功能
   - 实现环境配置管理

完成以上练习后，继续学习下一节：操作系统信息（os）。

## 总结

os 和 process 模块提供了系统信息和进程信息访问能力：

- **os 模块**：获取操作系统相关信息
- **process 模块**：访问和控制进程
- **使用场景**：系统监控、环境配置、进程管理

掌握 os 和 process 模块有助于进行系统监控和进程管理。

---

**最后更新**：2025-01-XX
