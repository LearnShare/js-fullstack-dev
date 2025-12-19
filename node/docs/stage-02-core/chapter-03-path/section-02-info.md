# 2.3.2 路径信息获取

## 1. 概述

获取路径信息是路径处理的重要功能，包括获取文件名、扩展名、目录名、基础名称等。Node.js 的 `path` 模块提供了多个方法用于提取路径的各个组成部分，这些方法对于文件操作、路径分析等场景非常有用。

## 2. 特性说明

- **路径解析**：将路径分解为各个组成部分（目录、文件名、扩展名等）。
- **信息提取**：提取路径中的特定信息（文件名、扩展名、目录等）。
- **跨平台兼容**：自动处理不同操作系统的路径格式。
- **路径操作**：支持路径的分解和重组。

## 3. 语法与定义

### 路径信息获取方法

```ts
// 获取目录名
path.dirname(path: string): string

// 获取文件名（含扩展名）
path.basename(path: string, ext?: string): string

// 获取扩展名
path.extname(path: string): string

// 解析路径对象
path.parse(path: string): ParsedPath

// 从对象构建路径
path.format(pathObject: ParsedPath): string
```

## 4. 基本用法

### 示例 1：获取路径组成部分

```ts
// 文件: path-info.ts
// 功能: 获取路径信息

import path from 'node:path';

const filePath = '/usr/local/bin/node.exe';

// 获取目录名
const dir = path.dirname(filePath);
console.log('Directory:', dir);
// /usr/local/bin

// 获取文件名（含扩展名）
const basename = path.basename(filePath);
console.log('Basename:', basename);
// node.exe

// 获取文件名（不含扩展名）
const nameWithoutExt = path.basename(filePath, path.extname(filePath));
console.log('Name without ext:', nameWithoutExt);
// node

// 获取扩展名
const ext = path.extname(filePath);
console.log('Extension:', ext);
// .exe
```

### 示例 2：解析路径对象

```ts
// 文件: path-parse.ts
// 功能: 解析路径对象

import path from 'node:path';

const filePath = '/usr/local/bin/node.exe';

// 解析路径
const parsed = path.parse(filePath);
console.log('Parsed path:', parsed);
// {
//   root: '/',
//   dir: '/usr/local/bin',
//   base: 'node.exe',
//   name: 'node',
//   ext: '.exe'
// }

// 从对象构建路径
const reconstructed = path.format(parsed);
console.log('Reconstructed:', reconstructed);
// /usr/local/bin/node.exe
```

### 示例 3：路径信息处理

```ts
// 文件: path-processing.ts
// 功能: 路径信息处理

import path from 'node:path';

function getFileInfo(filePath: string) {
    const dir = path.dirname(filePath);
    const basename = path.basename(filePath);
    const ext = path.extname(filePath);
    const name = path.basename(filePath, ext);
    
    return {
        directory: dir,
        filename: basename,
        name: name,
        extension: ext
    };
}

const info = getFileInfo('./src/utils/helper.ts');
console.log('File info:', info);
```

## 5. 参数说明：路径信息函数参数

### dirname 参数

| 参数名   | 类型     | 说明                                     | 示例                           |
|:---------|:---------|:-----------------------------------------|:-------------------------------|
| **path** | String   | 文件路径。                               | `'/usr/local/bin/node.exe'`    |

### basename 参数

| 参数名   | 类型     | 说明                                     | 示例                           |
|:---------|:---------|:-----------------------------------------|:-------------------------------|
| **path** | String   | 文件路径。                               | `'/usr/local/bin/node.exe'`    |
| **ext**  | String   | 要移除的扩展名（可选）。                 | `'.exe'`                       |

### extname 参数

| 参数名   | 类型     | 说明                                     | 示例                           |
|:---------|:---------|:-----------------------------------------|:-------------------------------|
| **path** | String   | 文件路径。                               | `'/usr/local/bin/node.exe'`    |

## 6. 返回值与状态说明

### dirname 返回值

| 返回类型 | 说明                                     |
|:---------|:-----------------------------------------|
| **string**| 目录路径。                               |

### basename 返回值

| 返回类型 | 说明                                     |
|:---------|:-----------------------------------------|
| **string**| 文件名（含或不含扩展名）。               |

### parse 返回值

| 返回类型   | 说明                                     |
|:-----------|:-----------------------------------------|
| **ParsedPath**| 包含路径各个组成部分的对象。            |

## 7. 代码示例：路径信息应用

以下示例演示了路径信息的常见应用：

```ts
// 文件: path-applications.ts
// 功能: 路径信息应用

import path from 'node:path';

// 1. 文件类型判断
function isTypeScriptFile(filePath: string): boolean {
    return path.extname(filePath) === '.ts';
}

// 2. 文件名处理
function changeExtension(filePath: string, newExt: string): string {
    const parsed = path.parse(filePath);
    return path.format({ ...parsed, ext: newExt, base: undefined });
}

// 3. 路径分类
function categorizePath(filePath: string): { type: string; category: string } {
    const ext = path.extname(filePath);
    const parsed = path.parse(filePath);
    
    if (ext === '.ts' || ext === '.js') {
        return { type: 'source', category: 'code' };
    } else if (ext === '.json') {
        return { type: 'config', category: 'data' };
    } else if (ext === '.md') {
        return { type: 'documentation', category: 'text' };
    }
    
    return { type: 'unknown', category: 'other' };
}
```

## 8. 输出结果说明

路径信息获取的输出结果：

```text
Directory: /usr/local/bin
Basename: node.exe
Name without ext: node
Extension: .exe
```

**逻辑解析**：
- `dirname()` 返回目录路径
- `basename()` 返回文件名
- `extname()` 返回扩展名（包含点号）
- `parse()` 返回包含所有信息的对象

## 9. 使用场景

### 1. 文件类型判断

根据扩展名判断文件类型：

```ts
// 文件类型判断
import path from 'node:path';

function getFileType(filePath: string): string {
    const ext = path.extname(filePath).toLowerCase();
    const typeMap: Record<string, string> = {
        '.ts': 'TypeScript',
        '.js': 'JavaScript',
        '.json': 'JSON',
        '.md': 'Markdown'
    };
    return typeMap[ext] || 'Unknown';
}
```

### 2. 文件名处理

处理文件名（更改扩展名、重命名等）：

```ts
// 文件名处理
import path from 'node:path';

function renameFile(filePath: string, newName: string): string {
    const dir = path.dirname(filePath);
    const ext = path.extname(filePath);
    return path.join(dir, `${newName}${ext}`);
}
```

### 3. 路径分析

分析路径结构：

```ts
// 路径分析
import path from 'node:path';

function analyzePath(filePath: string) {
    const parsed = path.parse(filePath);
    return {
        isAbsolute: path.isAbsolute(filePath),
        depth: parsed.dir.split(path.sep).filter(Boolean).length,
        components: {
            root: parsed.root,
            directories: parsed.dir.split(path.sep).filter(Boolean),
            filename: parsed.base,
            name: parsed.name,
            extension: parsed.ext
        }
    };
}
```

## 10. 注意事项与常见错误

- **扩展名包含点号**：`extname()` 返回的扩展名包含点号（如 `.ts`）
- **basename 参数**：`basename()` 的第二个参数必须是完整的扩展名（含点号）
- **路径格式**：不同操作系统的路径格式不同，`path` 模块会自动处理
- **空路径处理**：处理空路径或无效路径时注意错误处理
- **路径分隔符**：不要假设路径分隔符，使用 `path.sep` 获取

## 11. 常见问题 (FAQ)

**Q: extname 返回的扩展名包含点号吗？**
A: 是的，`extname()` 返回的扩展名包含点号（如 `.ts`、`.js`）。

**Q: 如何获取不带扩展名的文件名？**
A: 使用 `path.basename(filePath, path.extname(filePath))` 或使用 `path.parse()` 获取 `name` 属性。

**Q: parse 和 format 是互逆操作吗？**
A: 是的，`path.format(path.parse(path))` 应该返回原始路径（规范化后）。

## 12. 最佳实践

- **使用 path 模块**：始终使用 `path` 模块获取路径信息
- **扩展名处理**：注意扩展名包含点号，处理时保持一致
- **路径解析**：使用 `path.parse()` 获取完整的路径信息
- **跨平台兼容**：使用 `path` 模块确保跨平台兼容
- **错误处理**：处理无效路径时注意错误处理

## 13. 对比分析：不同信息获取方法

| 方法           | 返回内容                                     | 示例输入                    | 示例输出              |
|:---------------|:---------------------------------------------|:----------------------------|:----------------------|
| **dirname**    | 目录路径                                     | `/usr/local/bin/node.exe`   | `/usr/local/bin`      |
| **basename**   | 文件名（含扩展名）                           | `/usr/local/bin/node.exe`   | `node.exe`            |
| **extname**    | 扩展名（含点号）                             | `/usr/local/bin/node.exe`   | `.exe`                |
| **parse**      | 包含所有信息的对象                           | `/usr/local/bin/node.exe`   | `{ root, dir, base, name, ext }`|

## 14. 练习任务

1. **路径信息获取实践**：
   - 使用各种方法获取路径信息
   - 理解不同方法的返回值
   - 对比不同方法的差异

2. **路径解析实践**：
   - 使用 `path.parse()` 解析路径
   - 使用 `path.format()` 构建路径
   - 理解路径解析和构建的过程

3. **文件类型判断实践**：
   - 根据扩展名判断文件类型
   - 实现文件类型过滤功能
   - 理解扩展名处理的方法

4. **路径处理实践**：
   - 实现文件名处理功能
   - 实现路径分析功能
   - 理解路径处理的应用

5. **实际应用**：
   - 在实际项目中应用路径信息获取
   - 实现文件管理功能
   - 掌握路径信息获取的最佳实践

完成以上练习后，继续学习下一节：跨平台兼容性。

## 总结

路径信息获取是路径处理的重要功能：

- **信息提取**：提取路径的各个组成部分
- **路径解析**：使用 `path.parse()` 获取完整信息
- **文件处理**：根据路径信息进行文件类型判断和处理
- **最佳实践**：使用 `path` 模块，注意扩展名处理

掌握路径信息获取有助于进行文件操作和路径分析。

---

**最后更新**：2025-01-XX
