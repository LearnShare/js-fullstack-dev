# 2.10.2 操作系统信息（os）

## 1. 概述

os 模块提供了访问操作系统相关信息的能力，包括平台信息、CPU 信息、内存信息、网络接口等。这些信息对于系统监控、性能优化、跨平台开发等场景非常有用。理解 os 模块的使用有助于编写更健壮的跨平台应用。

## 2. 特性说明

- **平台信息**：获取操作系统平台、架构、版本等信息。
- **CPU 信息**：获取 CPU 核心数、型号、频率等信息。
- **内存信息**：获取总内存、空闲内存、内存使用率等。
- **网络接口**：获取网络接口信息。
- **跨平台支持**：提供跨平台的一致性 API。

## 3. 语法与定义

### os 模块常用方法

```ts
// 平台信息
os.platform(): string
os.arch(): string
os.type(): string
os.release(): string
os.hostname(): string

// CPU 信息
os.cpus(): Array<CPUInfo>
os.loadavg(): number[]

// 内存信息
os.totalmem(): number
os.freemem(): number

// 网络接口
os.networkInterfaces(): object
```

## 4. 基本用法

### 示例 1：平台信息

```ts
// 文件: os-platform.ts
// 功能: 获取平台信息

import os from 'node:os';

console.log('Platform:', os.platform());     // win32, linux, darwin
console.log('Architecture:', os.arch());     // x64, arm64, ia32
console.log('Type:', os.type());             // Windows_NT, Linux, Darwin
console.log('Release:', os.release());       // 操作系统版本
console.log('Hostname:', os.hostname());     // 主机名
```

### 示例 2：CPU 信息

```ts
// 文件: os-cpu.ts
// 功能: 获取 CPU 信息

import os from 'node:os';

const cpus = os.cpus();
console.log('CPU Count:', cpus.length);
console.log('CPU Info:', cpus[0]);
// { model: 'Intel Core i7', speed: 2400, times: { ... } }

const loadavg = os.loadavg();
console.log('Load Average:', loadavg);
// [1.5, 1.2, 1.0] (1分钟、5分钟、15分钟的平均负载)
```

### 示例 3：内存信息

```ts
// 文件: os-memory.ts
// 功能: 获取内存信息

import os from 'node:os';

const totalMem = os.totalmem();
const freeMem = os.freemem();
const usedMem = totalMem - freeMem;
const memUsage = (usedMem / totalMem) * 100;

console.log('Total Memory:', (totalMem / 1024 / 1024 / 1024).toFixed(2), 'GB');
console.log('Free Memory:', (freeMem / 1024 / 1024 / 1024).toFixed(2), 'GB');
console.log('Used Memory:', (usedMem / 1024 / 1024 / 1024).toFixed(2), 'GB');
console.log('Memory Usage:', memUsage.toFixed(2), '%');
```

## 5. 参数说明：os 模块方法

| 方法名           | 返回类型     | 说明                                     | 示例                           |
|:-----------------|:-------------|:-----------------------------------------|:-------------------------------|
| **platform()**   | String       | 操作系统平台                             | `'win32'`, `'linux'`, `'darwin'`|
| **arch()**       | String       | CPU 架构                                 | `'x64'`, `'arm64'`             |
| **cpus()**       | Array        | CPU 信息数组                             | `[{ model: '...', speed: ... }]`|
| **totalmem()**   | Number       | 总内存（字节）                           | `8589934592`                   |
| **freemem()**    | Number       | 空闲内存（字节）                         | `4294967296`                   |
| **networkInterfaces()**| Object | 网络接口信息                            | `{ eth0: [...], wifi0: [...] }`|

## 6. 返回值与状态说明

os 模块操作的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **平台信息** | String       | 返回平台相关的字符串                     |
| **CPU 信息** | Array/Object | 返回 CPU 信息数组或对象                  |
| **内存信息** | Number       | 返回内存大小（字节）                     |
| **网络信息** | Object       | 返回网络接口信息对象                     |

## 7. 代码示例：系统监控工具

以下示例演示了如何构建系统监控工具：

```ts
// 文件: os-monitor.ts
// 功能: 系统监控工具

import os from 'node:os';

class SystemMonitor {
    getSystemInfo() {
        return {
            platform: os.platform(),
            architecture: os.arch(),
            hostname: os.hostname(),
            cpuCount: os.cpus().length,
            cpuModel: os.cpus()[0]?.model || 'Unknown',
            totalMemory: this.formatBytes(os.totalmem()),
            freeMemory: this.formatBytes(os.freemem()),
            usedMemory: this.formatBytes(os.totalmem() - os.freemem()),
            memoryUsage: ((1 - os.freemem() / os.totalmem()) * 100).toFixed(2) + '%',
            loadAverage: os.loadavg()
        };
    }
    
    formatBytes(bytes: number): string {
        const gb = bytes / 1024 / 1024 / 1024;
        if (gb >= 1) {
            return gb.toFixed(2) + ' GB';
        }
        const mb = bytes / 1024 / 1024;
        return mb.toFixed(2) + ' MB';
    }
    
    getNetworkInterfaces() {
        return os.networkInterfaces();
    }
}

// 使用
const monitor = new SystemMonitor();
console.log('System Info:', monitor.getSystemInfo());
console.log('Network Interfaces:', monitor.getNetworkInterfaces());
```

## 8. 输出结果说明

系统监控的输出结果：

```text
System Info: {
  platform: 'win32',
  architecture: 'x64',
  hostname: 'DESKTOP-ABC123',
  cpuCount: 8,
  cpuModel: 'Intel Core i7-9700K',
  totalMemory: '16.00 GB',
  freeMemory: '8.00 GB',
  usedMemory: '8.00 GB',
  memoryUsage: '50.00%',
  loadAverage: [1.5, 1.2, 1.0]
}
```

**逻辑解析**：
- 获取系统的基本信息
- 格式化内存单位为 GB/MB
- 计算内存使用率
- 提供网络接口信息

## 9. 使用场景

### 1. 系统监控

监控系统资源使用情况：

```ts
// 系统监控示例
import os from 'node:os';

function monitorSystem() {
    setInterval(() => {
        const memUsage = (1 - os.freemem() / os.totalmem()) * 100;
        console.log(`Memory Usage: ${memUsage.toFixed(2)}%`);
    }, 5000);
}
```

### 2. 跨平台开发

根据平台执行不同逻辑：

```ts
// 跨平台开发示例
import os from 'node:os';

function getConfigPath() {
    const platform = os.platform();
    if (platform === 'win32') {
        return 'C:\\ProgramData\\app\\config.json';
    } else {
        return '/etc/app/config.json';
    }
}
```

### 3. 性能优化

根据系统资源调整应用行为：

```ts
// 性能优化示例
import os from 'node:os';

function getWorkerCount() {
    const cpuCount = os.cpus().length;
    // 根据 CPU 核心数设置工作进程数
    return Math.max(1, cpuCount - 1);
}
```

## 10. 注意事项与常见错误

- **内存单位**：内存值以字节为单位，需要转换为 GB/MB
- **跨平台差异**：注意不同平台的差异
- **性能开销**：某些操作可能有性能开销
- **网络接口**：网络接口信息可能因平台而异
- **负载平均值**：Windows 不支持 loadavg，返回 [0, 0, 0]

## 11. 常见问题 (FAQ)

**Q: 如何获取内存使用率？**
A: 使用 `(1 - os.freemem() / os.totalmem()) * 100` 计算。

**Q: loadavg 在 Windows 上可用吗？**
A: Windows 不支持 loadavg，返回 [0, 0, 0]。

**Q: 如何判断操作系统类型？**
A: 使用 `os.platform()` 或 `os.type()` 判断。

## 12. 最佳实践

- **系统监控**：使用 os 模块监控系统资源
- **跨平台**：注意跨平台差异，使用跨平台 API
- **内存格式化**：将字节转换为可读格式（GB/MB）
- **性能考虑**：注意某些操作的性能开销
- **错误处理**：处理平台不支持的功能

## 13. 对比分析：不同平台差异

| 功能             | Windows                                    | Linux/macOS                                |
|:-----------------|:-------------------------------------------|:-------------------------------------------|
| **platform**     | `'win32'`                                  | `'linux'` 或 `'darwin'`                    |
| **loadavg**      | 返回 [0, 0, 0]                             | 返回实际负载平均值                          |
| **网络接口**     | 接口名称可能不同                            | 接口名称可能不同                            |

## 14. 练习任务

1. **平台信息实践**：
   - 获取不同平台的信息
   - 实现跨平台逻辑
   - 理解平台差异

2. **系统监控实践**：
   - 实现系统监控工具
   - 监控内存和 CPU 使用
   - 格式化输出系统信息

3. **实际应用**：
   - 在实际项目中应用 os 模块
   - 实现系统监控功能
   - 实现跨平台配置

完成以上练习后，继续学习下一节：进程信息与控制（process）。

## 总结

os 模块提供了操作系统信息访问能力：

- **核心功能**：平台信息、CPU 信息、内存信息、网络接口
- **使用场景**：系统监控、跨平台开发、性能优化
- **最佳实践**：注意跨平台差异，格式化内存单位

掌握 os 模块有助于进行系统监控和跨平台开发。

---

**最后更新**：2025-01-XX
