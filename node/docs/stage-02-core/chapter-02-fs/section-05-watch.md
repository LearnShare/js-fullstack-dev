# 2.2.5 文件监听（watch）

## 1. 概述

文件监听功能允许程序监控文件或目录的变化，当文件被创建、修改或删除时触发相应的事件。这在开发工具（如热重载）、文件同步、日志监控等场景中非常有用。Node.js 提供了 `fs.watch()` 和 `fs.watchFile()` 两种文件监听方式。

## 2. 特性说明

- **实时监控**：监控文件或目录的实时变化。
- **事件驱动**：通过事件通知文件变化，无需轮询。
- **跨平台支持**：在不同操作系统上提供统一的事件接口。
- **性能优化**：使用操作系统原生 API，性能高效。
- **多种事件**：支持文件创建、修改、删除等多种事件。

## 3. 语法与定义

### fs.watch（推荐）

```ts
// 监听文件或目录（Promise）
fs.watch(filename: string, options?: object): FSWatcher

// 监听文件或目录（回调方式）
fs.watch(filename: string, options?: object, listener?: Function): FSWatcher
```

### fs.watchFile（已废弃）

```ts
// 监听文件变化（已废弃，不推荐使用）
fs.watchFile(filename: string, options?: object, listener?: Function): void
```

## 4. 基本用法

### 示例 1：监听文件变化

```ts
// 文件: watch-file.ts
// 功能: 监听文件变化

import fs from 'node:fs';

// 方式 1：使用事件监听器
const watcher = fs.watch('./data.txt', (eventType, filename) => {
    if (eventType === 'rename') {
        console.log(`File ${filename} was created or deleted`);
    } else if (eventType === 'change') {
        console.log(`File ${filename} was modified`);
    }
});

// 方式 2：使用事件对象
const watcher2 = fs.watch('./data.txt');
watcher2.on('change', (eventType, filename) => {
    console.log(`File ${filename} changed: ${eventType}`);
});

watcher2.on('error', (error) => {
    console.error('Watch error:', error);
});

// 停止监听
// watcher.close();
```

### 示例 2：监听目录变化

```ts
// 文件: watch-dir.ts
// 功能: 监听目录变化

import fs from 'node:fs';

const watcher = fs.watch('./src', { recursive: true }, (eventType, filename) => {
    if (filename) {
        console.log(`File ${filename} in directory: ${eventType}`);
    }
});

watcher.on('error', (error) => {
    console.error('Watch error:', error);
});
```

### 示例 3：使用 Promise 封装

```ts
// 文件: watch-promise.ts
// 功能: 使用 Promise 封装文件监听

import fs from 'node:fs';
import { promisify } from 'node:util';

function watchFile(path: string, callback: (event: string, filename: string) => void) {
    const watcher = fs.watch(path, { recursive: true }, callback);
    
    return {
        close: () => watcher.close(),
        on: (event: string, handler: Function) => watcher.on(event, handler)
    };
}

// 使用
const watcher = watchFile('./src', (eventType, filename) => {
    console.log(`File ${filename}: ${eventType}`);
});
```

## 5. 参数说明：watch 函数参数

### watch 参数

| 参数名       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **filename** | String   | 要监听的文件或目录路径。                 | `'./data.txt'` 或 `'./src'`    |
| **options**  | Object   | 监听选项。                               | `{ recursive: true }`          |
| **recursive**| Boolean  | 是否递归监听子目录（仅目录）。           | `true`                         |
| **encoding** | String   | 文件名编码。                             | `'utf8'`                       |
| **listener** | Function | 变化事件监听器（可选）。                 | `(eventType, filename) => {}` |

## 6. 返回值与状态说明

### watch 返回值

| 返回类型     | 说明                                     |
|:-------------|:-----------------------------------------|
| **FSWatcher**| 文件监听器对象，可以监听事件和关闭监听。 |

### 事件类型

| 事件类型     | 说明                                     |
|:-------------|:-----------------------------------------|
| **'change'** | 文件被修改。                               |
| **'rename'** | 文件被创建、删除或重命名。                 |
| **'error'**  | 监听过程中发生错误。                       |

## 7. 代码示例：文件监听应用

以下示例演示了文件监听的常见应用：

```ts
// 文件: file-watcher.ts
// 功能: 文件监听应用示例

import fs from 'node:fs';
import path from 'node:path';

class FileWatcher {
    private watchers: Map<string, fs.FSWatcher> = new Map();
    
    watch(filePath: string, callback: (event: string, filename: string) => void): void {
        const watcher = fs.watch(filePath, { recursive: true }, (eventType, filename) => {
            if (filename) {
                callback(eventType, filename);
            }
        });
        
        watcher.on('error', (error) => {
            console.error('Watch error:', error);
        });
        
        this.watchers.set(filePath, watcher);
    }
    
    unwatch(filePath: string): void {
        const watcher = this.watchers.get(filePath);
        if (watcher) {
            watcher.close();
            this.watchers.delete(filePath);
        }
    }
    
    closeAll(): void {
        for (const watcher of this.watchers.values()) {
            watcher.close();
        }
        this.watchers.clear();
    }
}

// 使用
const watcher = new FileWatcher();
watcher.watch('./src', (eventType, filename) => {
    console.log(`File ${filename} changed: ${eventType}`);
});
```

## 8. 输出结果说明

文件监听的输出结果：

```text
File index.ts changed: change
File utils.ts changed: change
File new-file.ts changed: rename
```

**逻辑解析**：
- `change` 事件表示文件被修改
- `rename` 事件表示文件被创建、删除或重命名
- 监听器会实时响应文件系统的变化

## 9. 使用场景

### 1. 开发工具热重载

实现开发工具的热重载功能：

```ts
// 热重载功能
import fs from 'node:fs';

function setupHotReload() {
    fs.watch('./src', { recursive: true }, (eventType, filename) => {
        if (eventType === 'change' && filename?.endsWith('.ts')) {
            console.log(`Reloading ${filename}...`);
            // 重新加载模块
        }
    });
}
```

### 2. 文件同步

实现文件同步功能：

```ts
// 文件同步
import fs from 'node:fs';

function syncFiles(sourceDir: string, targetDir: string) {
    fs.watch(sourceDir, { recursive: true }, async (eventType, filename) => {
        if (filename) {
            const sourcePath = path.join(sourceDir, filename);
            const targetPath = path.join(targetDir, filename);
            
            if (eventType === 'change') {
                // 同步文件内容
                await fsPromises.copyFile(sourcePath, targetPath);
            }
        }
    });
}
```

### 3. 日志监控

监控日志文件的变化：

```ts
// 日志监控
import fs from 'node:fs';

function monitorLog(logFile: string) {
    fs.watch(logFile, (eventType) => {
        if (eventType === 'change') {
            // 读取新的日志内容
            const newLines = readNewLogLines(logFile);
            processLogLines(newLines);
        }
    });
}
```

## 10. 注意事项与常见错误

- **事件重复**：某些系统可能触发多次事件，需要去重处理
- **性能影响**：监听大量文件可能影响性能，注意资源管理
- **跨平台差异**：不同操作系统的事件行为可能不同
- **文件删除**：文件删除后监听器可能失效，需要重新创建
- **资源清理**：及时关闭不再需要的监听器，释放资源

## 11. 常见问题 (FAQ)

**Q: watch 和 watchFile 有什么区别？**
A: `watch` 使用操作系统原生 API，性能更好，推荐使用。`watchFile` 使用轮询，已废弃。

**Q: 为什么事件会触发多次？**
A: 某些操作系统和编辑器会触发多次事件，这是正常现象。可以通过防抖处理。

**Q: 如何监听子目录的变化？**
A: 使用 `{ recursive: true }` 选项（仅对目录有效）。

**Q: 监听器什么时候会失效？**
A: 文件被删除或移动时，监听器可能失效。需要重新创建监听器。

## 12. 最佳实践

- **使用 watch**：优先使用 `fs.watch()` 而非 `watchFile()`
- **事件去重**：实现事件去重机制，避免重复处理
- **资源管理**：及时关闭不再需要的监听器
- **错误处理**：监听 `error` 事件，处理监听错误
- **性能优化**：避免监听过多文件，注意性能影响

## 13. 对比分析：watch vs watchFile

| 维度             | fs.watch                                    | fs.watchFile                                 |
|:-----------------|:--------------------------------------------|:---------------------------------------------|
| **实现方式**     | 操作系统原生 API                            | 轮询检查                                     |
| **性能**         | 高效                                        | 较低                                         |
| **事件类型**     | change, rename                              | change, rename                               |
| **推荐使用**     | ✅ 推荐                                     | ❌ 已废弃                                    |
| **跨平台**       | 行为可能不同                                | 行为一致但性能差                             |

## 14. 练习任务

1. **文件监听实践**：
   - 监听单个文件的变化
   - 监听目录的变化
   - 理解不同事件类型的含义

2. **事件处理实践**：
   - 处理 change 和 rename 事件
   - 实现事件去重机制
   - 处理监听错误

3. **实际应用**：
   - 实现简单的热重载功能
   - 实现文件同步功能
   - 实现日志监控功能

4. **性能优化**：
   - 优化文件监听的性能
   - 实现监听器管理
   - 理解性能优化的方法

5. **资源管理**：
   - 实现监听器的创建和销毁
   - 处理监听器失效的情况
   - 理解资源管理的重要性

完成以上练习后，继续学习下一章：路径处理（path）。

## 总结

文件监听是文件系统操作的重要功能：

- **实时监控**：监控文件或目录的实时变化
- **事件驱动**：通过事件通知文件变化
- **最佳实践**：使用 watch，处理事件去重，管理资源
- **应用场景**：热重载、文件同步、日志监控等

掌握文件监听有助于构建响应式的文件管理系统。

---

**最后更新**：2025-01-XX
