# 3.7.3 自动化脚本

## 1. 概述

自动化脚本是 Node.js 的另一个重要应用领域。通过自动化脚本，可以自动化执行重复性任务，提高工作效率。Node.js 的异步特性和丰富的生态系统使其成为构建自动化脚本的理想选择。

## 2. 特性说明

- **任务自动化**：自动化执行重复性任务。
- **文件操作**：自动化文件处理和管理。
- **系统集成**：与操作系统和外部工具集成。
- **定时执行**：支持定时和计划任务。
- **错误处理**：完善的错误处理和日志记录。

## 3. 主流工具概览

### node-cron

定时任务调度工具。

**特点**：
- Cron 表达式支持
- 灵活的调度选项
- 时区支持
- 任务管理

**安装**：
```bash
npm install node-cron
```

**基本用法**：
```ts
// 文件: automation-cron.ts
// 功能: node-cron 基本用法

import cron from 'node-cron';

// 每分钟执行
cron.schedule('* * * * *', () => {
    console.log('Running every minute');
});

// 每天凌晨执行
cron.schedule('0 0 * * *', () => {
    console.log('Running daily at midnight');
});

// 每周一执行
cron.schedule('0 0 * * 1', () => {
    console.log('Running every Monday');
});
```

### glob

文件匹配工具。

**特点**：
- 支持 glob 模式
- 递归匹配
- 异步和同步 API
- 跨平台支持

**安装**：
```bash
npm install glob
```

**基本用法**：
```ts
// 文件: automation-glob.ts
// 功能: glob 基本用法

import { glob } from 'glob';

async function findFiles() {
    // 查找所有 TypeScript 文件
    const tsFiles = await glob('**/*.ts');
    console.log('TypeScript files:', tsFiles);
    
    // 查找特定目录下的文件
    const srcFiles = await glob('src/**/*.{ts,js}');
    console.log('Source files:', srcFiles);
}
```

### chokidar

文件系统监听工具。

**特点**：
- 跨平台文件监听
- 高性能
- 支持递归监听
- 事件驱动

**安装**：
```bash
npm install chokidar
```

**基本用法**：
```ts
// 文件: automation-chokidar.ts
// 功能: chokidar 基本用法

import chokidar from 'chokidar';

const watcher = chokidar.watch('./src', {
    ignored: /node_modules/,
    persistent: true
});

watcher
    .on('add', path => console.log(`File ${path} has been added`))
    .on('change', path => console.log(`File ${path} has been changed`))
    .on('unlink', path => console.log(`File ${path} has been removed`));
```

### execa

更好的子进程执行工具。

**特点**：
- Promise 支持
- 更好的错误处理
- 跨平台支持
- 流式输出

**安装**：
```bash
npm install execa
```

**基本用法**：
```ts
// 文件: automation-execa.ts
// 功能: execa 基本用法

import { execa } from 'execa';

async function runCommand() {
    try {
        const { stdout } = await execa('git', ['status']);
        console.log(stdout);
    } catch (error) {
        console.error('Command failed:', error);
    }
}

// 执行多个命令
async function runMultipleCommands() {
    await execa('npm', ['install']);
    await execa('npm', ['run', 'build']);
    await execa('npm', ['test']);
}
```

## 4. 代码示例：完整自动化脚本

以下示例演示了如何构建一个完整的自动化脚本：

```ts
// 文件: complete-automation.ts
// 功能: 完整的自动化脚本示例

import cron from 'node-cron';
import { glob } from 'glob';
import { execa } from 'execa';
import fsPromises from 'node:fs/promises';

// 1. 文件备份任务
async function backupFiles() {
    const files = await glob('src/**/*.ts');
    const backupDir = './backup';
    
    await fsPromises.mkdir(backupDir, { recursive: true });
    
    for (const file of files) {
        const backupPath = file.replace('src', backupDir);
        await fsPromises.copyFile(file, backupPath);
    }
    
    console.log(`Backed up ${files.length} files`);
}

// 2. 定时执行任务
cron.schedule('0 2 * * *', async () => {
    console.log('Running backup at 2 AM');
    await backupFiles();
});

// 3. 文件变更处理
import chokidar from 'chokidar';

const watcher = chokidar.watch('./src', {
    ignored: /node_modules/,
    persistent: true
});

watcher.on('change', async (path) => {
    console.log(`File changed: ${path}`);
    // 执行相关处理
    await execa('npm', ['run', 'lint', path]);
});
```

## 5. 参数说明：自动化脚本常用参数

| 参数类型     | 说明                                     | 示例                           |
|:-------------|:-----------------------------------------|:-------------------------------|
| **Cron 表达式**| 定时任务的时间表达式                    | `'0 0 * * *'`                  |
| **Glob 模式**| 文件匹配模式                             | `'**/*.ts'`                    |
| **命令参数** | 要执行的命令和参数                       | `['git', ['status']]`          |
| **监听选项** | 文件监听的配置选项                       | `{ ignored: /node_modules/ }` |

## 6. 返回值与状态说明

自动化脚本的执行结果：

| 返回类型     | 说明                                     |
|:-------------|:-----------------------------------------|
| **成功**     | 任务执行成功，返回结果数据               |
| **失败**     | 任务执行失败，返回错误信息               |
| **进行中**   | 任务正在执行，返回进度信息               |

## 7. 输出结果说明

自动化脚本的输出示例：

```text
Running backup at 2 AM
Backed up 25 files
File changed: src/index.ts
Running linter...
```

**逻辑解析**：
- 定时任务在指定时间执行
- 文件监听实时响应文件变化
- 执行相应的处理逻辑

## 8. 使用场景

### 1. 文件备份

自动化文件备份：

```ts
// 文件备份示例
cron.schedule('0 0 * * *', async () => {
    await backupFiles();
});
```

### 2. 代码检查

自动化代码检查：

```ts
// 代码检查示例
watcher.on('change', async (path) => {
    await execa('npm', ['run', 'lint', path]);
    await execa('npm', ['run', 'test']);
});
```

### 3. 数据同步

自动化数据同步：

```ts
// 数据同步示例
cron.schedule('*/5 * * * *', async () => {
    await syncData();
});
```

## 9. 注意事项与常见错误

- **错误处理**：完善的错误处理和日志记录
- **资源管理**：及时释放资源，避免内存泄漏
- **并发控制**：控制并发任务数量
- **时区处理**：注意定时任务的时区设置
- **权限问题**：确保有执行相关操作的权限

## 10. 常见问题 (FAQ)

**Q: 如何确保定时任务可靠执行？**
A: 使用进程管理器（如 PM2）管理定时任务，确保任务持续运行。

**Q: 如何处理长时间运行的任务？**
A: 使用队列系统（如 Bull）管理长时间运行的任务，支持任务重试和监控。

**Q: 如何监控自动化脚本的执行？**
A: 添加日志记录、错误追踪和性能监控。

## 11. 最佳实践

- **错误处理**：完善的错误处理和重试机制
- **日志记录**：记录任务执行日志，便于排查问题
- **资源管理**：及时释放资源，避免资源泄漏
- **任务隔离**：将任务隔离，避免相互影响
- **监控告警**：添加监控和告警机制

## 12. 对比分析：自动化工具选择

| 工具           | 特点                                     | 适用场景                       |
|:---------------|:-----------------------------------------|:-------------------------------|
| **node-cron**  | 简单易用，Cron 表达式                    | 定时任务调度                   |
| **node-schedule**| 更灵活的调度选项                        | 复杂调度需求                   |
| **chokidar**   | 高性能文件监听                           | 文件变更监控                   |
| **execa**      | 更好的子进程执行                         | 执行系统命令                   |

## 13. 练习任务

1. **定时任务实践**：
   - 使用 node-cron 创建定时任务
   - 实现文件备份功能
   - 实现数据同步功能

2. **文件处理实践**：
   - 使用 glob 查找文件
   - 批量处理文件
   - 实现文件转换功能

3. **文件监听实践**：
   - 使用 chokidar 监听文件变化
   - 实现自动构建功能
   - 实现自动测试功能

4. **实际应用**：
   - 创建实际的自动化脚本
   - 实现完整的自动化流程
   - 添加监控和日志功能

完成以上练习后，继续学习下一节：数据处理。

## 总结

自动化脚本是 Node.js 的重要应用领域：

- **主流工具**：node-cron、glob、chokidar、execa
- **核心功能**：定时任务、文件处理、系统集成
- **最佳实践**：错误处理、日志记录、资源管理、监控告警

掌握自动化脚本有助于提高工作效率。

---

**最后更新**：2025-01-XX
