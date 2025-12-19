# 2.3.1 路径拼接与解析

## 1. 概述

路径拼接与解析是路径处理的基础操作。Node.js 的 `path` 模块提供了 `path.join()` 和 `path.resolve()` 等方法，用于安全地拼接和解析路径。这些方法自动处理不同操作系统的路径分隔符差异，确保代码的跨平台兼容性。

## 2. 特性说明

- **跨平台兼容**：自动处理 Windows 和 Unix 系统的路径分隔符差异。
- **路径规范化**：自动处理 `.`、`..` 等路径片段，生成规范化路径。
- **绝对路径解析**：将相对路径解析为绝对路径。
- **路径拼接**：安全地拼接多个路径片段。
- **路径分隔符**：自动使用正确的路径分隔符。

## 3. 语法与定义

### 路径拼接

```ts
// 拼接路径
path.join(...paths: string[]): string

// 解析绝对路径
path.resolve(...paths: string[]): string

// 规范化路径
path.normalize(path: string): string
```

## 4. 基本用法

### 示例 1：路径拼接

```ts
// 文件: path-join.ts
// 功能: 路径拼接示例

import path from 'node:path';

// 拼接路径
const filePath = path.join('src', 'utils', 'helper.ts');
console.log('Joined path:', filePath);
// Windows: src\utils\helper.ts
// Unix: src/utils/helper.ts

// 拼接绝对路径
const absolutePath = path.join('/usr', 'local', 'bin');
console.log('Absolute path:', absolutePath);
// /usr/local/bin

// 处理相对路径片段
const normalizedPath = path.join('src', '..', 'utils', 'helper.ts');
console.log('Normalized path:', normalizedPath);
// utils/helper.ts (.. 被解析)
```

### 示例 2：路径解析

```ts
// 文件: path-resolve.ts
// 功能: 路径解析示例

import path from 'node:path';

// 解析绝对路径
const absolutePath = path.resolve('src', 'index.ts');
console.log('Resolved path:', absolutePath);
// /current/working/directory/src/index.ts

// 从根目录解析
const rootPath = path.resolve('/usr', 'local', 'bin');
console.log('Root path:', rootPath);
// /usr/local/bin

// 处理相对路径
const relativePath = path.resolve('src', '..', 'dist');
console.log('Relative resolved:', relativePath);
// /current/working/directory/dist
```

### 示例 3：路径规范化

```ts
// 文件: path-normalize.ts
// 功能: 路径规范化示例

import path from 'node:path';

// 规范化路径
const normalized1 = path.normalize('/usr/local/../bin');
console.log('Normalized 1:', normalized1);
// /usr/bin

const normalized2 = path.normalize('./src/./utils/../helper.ts');
console.log('Normalized 2:', normalized2);
// src/helper.ts
```

## 5. 参数说明：路径处理函数参数

### join 参数

| 参数名   | 类型     | 说明                                     | 示例                           |
|:---------|:---------|:-----------------------------------------|:-------------------------------|
| **paths**| ...string| 要拼接的路径片段（可变参数）。           | `'src', 'utils', 'helper.ts'`  |

### resolve 参数

| 参数名   | 类型     | 说明                                     | 示例                           |
|:---------|:---------|:-----------------------------------------|:-------------------------------|
| **paths**| ...string| 要解析的路径片段（可变参数）。           | `'src', 'index.ts'`            |

## 6. 返回值与状态说明

### join 返回值

| 返回类型 | 说明                                     |
|:---------|:-----------------------------------------|
| **string**| 拼接后的路径字符串。                     |

### resolve 返回值

| 返回类型 | 说明                                     |
|:---------|:-----------------------------------------|
| **string**| 解析后的绝对路径字符串。                 |

## 7. 代码示例：路径处理实践

以下示例演示了路径处理的常见用法：

```ts
// 文件: path-practice.ts
// 功能: 路径处理实践

import path from 'node:path';

// 1. 构建文件路径
function buildFilePath(dir: string, filename: string): string {
    return path.join(dir, filename);
}

// 2. 构建绝对路径
function buildAbsolutePath(segments: string[]): string {
    return path.resolve(...segments);
}

// 3. 规范化用户输入路径
function normalizeUserPath(userPath: string): string {
    return path.normalize(userPath);
}

// 使用
const filePath = buildFilePath('src', 'utils', 'helper.ts');
const absolutePath = buildAbsolutePath(['src', 'index.ts']);
const normalized = normalizeUserPath('./src/../dist/index.js');
```

## 8. 输出结果说明

路径处理的输出结果：

```text
Joined path: src/utils/helper.ts
Resolved path: /current/working/directory/src/index.ts
Normalized path: dist/index.js
```

**逻辑解析**：
- `join()` 拼接路径，使用正确的路径分隔符
- `resolve()` 解析为绝对路径，从当前工作目录开始
- `normalize()` 规范化路径，处理 `.` 和 `..` 片段

## 9. 使用场景

### 1. 构建文件路径

在文件操作中构建路径：

```ts
// 构建文件路径
import path from 'node:path';
import fsPromises from 'node:fs/promises';

async function readConfig() {
    const configPath = path.join(process.cwd(), 'config', 'app.json');
    return await fsPromises.readFile(configPath, 'utf8');
}
```

### 2. 项目路径管理

管理项目中的路径：

```ts
// 项目路径管理
import path from 'node:path';

const projectRoot = path.resolve(__dirname, '..');
const srcDir = path.join(projectRoot, 'src');
const distDir = path.join(projectRoot, 'dist');
```

### 3. 用户输入路径处理

处理用户输入的路径：

```ts
// 处理用户输入路径
import path from 'node:path';

function processUserPath(userPath: string): string {
    // 规范化路径，防止路径遍历攻击
    const normalized = path.normalize(userPath);
    // 解析为绝对路径
    return path.resolve(normalized);
}
```

## 10. 注意事项与常见错误

- **路径分隔符**：不要手动拼接路径，使用 `path.join()` 确保跨平台兼容
- **绝对路径**：`path.resolve()` 会解析为绝对路径，注意当前工作目录的影响
- **路径遍历**：处理用户输入路径时，注意防止路径遍历攻击（如 `../../../etc/passwd`）
- **路径规范化**：使用 `path.normalize()` 规范化路径，处理 `.` 和 `..` 片段
- **相对路径**：理解相对路径和绝对路径的区别

## 11. 常见问题 (FAQ)

**Q: join 和 resolve 有什么区别？**
A: `join()` 只是拼接路径，可能返回相对路径。`resolve()` 会解析为绝对路径，从当前工作目录开始。

**Q: 什么时候使用 join，什么时候使用 resolve？**
A: 构建相对路径时使用 `join()`，需要绝对路径时使用 `resolve()`。

**Q: normalize 会处理路径分隔符吗？**
A: 会。`normalize()` 会使用正确的路径分隔符，并处理 `.` 和 `..` 片段。

## 12. 最佳实践

- **使用 path 模块**：始终使用 `path` 模块处理路径，不要手动拼接
- **明确路径类型**：明确使用相对路径还是绝对路径
- **路径规范化**：处理用户输入时，规范化路径防止安全问题
- **跨平台考虑**：使用 `path` 模块确保跨平台兼容
- **路径验证**：验证路径的有效性和安全性

## 13. 对比分析：join vs resolve

| 维度             | path.join()                                 | path.resolve()                               |
|:-----------------|:--------------------------------------------|:---------------------------------------------|
| **返回类型**     | 相对或绝对路径                              | 绝对路径                                      |
| **工作方式**     | 拼接路径片段                                | 从当前工作目录解析                            |
| **路径处理**     | 处理路径分隔符                              | 处理路径分隔符和相对路径                      |
| **适用场景**     | 构建相对路径                                | 需要绝对路径的场景                            |

## 14. 练习任务

1. **路径拼接实践**：
   - 使用 `path.join()` 拼接路径
   - 理解路径拼接的行为
   - 对比不同操作系统的输出

2. **路径解析实践**：
   - 使用 `path.resolve()` 解析路径
   - 理解绝对路径的生成
   - 理解当前工作目录的影响

3. **路径规范化实践**：
   - 使用 `path.normalize()` 规范化路径
   - 处理 `.` 和 `..` 片段
   - 理解路径规范化的作用

4. **跨平台实践**：
   - 在不同操作系统上测试路径处理
   - 理解跨平台兼容性
   - 掌握跨平台路径处理的方法

5. **实际应用**：
   - 在实际项目中应用路径处理
   - 构建文件路径管理功能
   - 处理用户输入路径

完成以上练习后，继续学习下一节：路径信息获取。

## 总结

路径拼接与解析是路径处理的基础：

- **路径拼接**：使用 `path.join()` 安全拼接路径
- **路径解析**：使用 `path.resolve()` 解析绝对路径
- **路径规范化**：使用 `path.normalize()` 规范化路径
- **跨平台兼容**：使用 `path` 模块确保跨平台兼容

掌握路径处理有助于编写跨平台兼容的 Node.js 应用。

---

**最后更新**：2025-01-XX
