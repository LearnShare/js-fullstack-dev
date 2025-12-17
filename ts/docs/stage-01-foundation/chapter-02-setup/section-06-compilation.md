# 1.1.6 编译操作与实践

## 概述

编译是 TypeScript 开发的核心操作。本节介绍 TypeScript 编译器的使用，包括 tsc 命令、编译模式、监视模式、编译输出配置等。

## tsc 命令基础

### 基本语法

```bash
tsc [options] [file...]
```

### 单文件编译

编译单个 TypeScript 文件：

```bash
tsc script.ts
```

这会生成 `script.js` 文件。

### 项目编译

使用 tsconfig.json 编译整个项目：

```bash
tsc
```

### 指定配置文件

使用 `-p` 或 `--project` 指定配置文件：

```bash
tsc -p tsconfig.json
tsc --project tsconfig.json
```

### 编译特定文件

编译多个文件：

```bash
tsc file1.ts file2.ts file3.ts
```

### 查看帮助

```bash
tsc --help
tsc -h
```

### 查看配置

查看最终使用的配置：

```bash
tsc --showConfig
```

## 编译模式

### 单文件编译模式

直接指定文件编译，不使用 tsconfig.json：

```bash
tsc script.ts
```

**特点**：
- 不读取 tsconfig.json
- 使用默认编译选项
- 适合快速测试

### 项目编译模式

使用 tsconfig.json 编译整个项目：

```bash
tsc
```

**特点**：
- 读取 tsconfig.json 配置
- 编译 include 中的所有文件
- 遵循 exclude 规则

### 增量编译

启用增量编译，只编译变更的文件：

```json
{
  "compilerOptions": {
    "incremental": true
  }
}
```

或使用命令行：

```bash
tsc --incremental
```

**优势**：
- 编译速度更快
- 减少不必要的编译

### 复合编译

启用项目引用，支持多项目结构：

```json
{
  "compilerOptions": {
    "composite": true
  }
}
```

### 项目引用

使用项目引用管理多项目结构：

```json
{
  "references": [
    { "path": "./core" },
    { "path": "./utils" }
  ]
}
```

编译时：

```bash
tsc --build
```

## 监视模式

### 基本使用

启用监视模式，文件变更时自动重新编译：

```bash
tsc --watch
tsc -w
```

### 监视模式配置

在 tsconfig.json 中配置：

```json
{
  "watchOptions": {
    "watchFile": "useFsEvents",
    "watchDirectory": "useFsEvents",
    "fallbackPolling": "dynamicPriority",
    "synchronousWatchDirectory": true,
    "excludeDirectories": ["**/node_modules", "**/dist"]
  }
}
```

### 性能考虑

监视模式会持续运行，注意：

- 监控文件数量影响性能
- 使用 exclude 排除不需要的文件
- 大型项目可能需要调整 watchOptions

### 与直接执行工具的对比

| 方式         | 编译输出 | 类型检查 | 性能 | 适用场景     |
|:-------------|:---------|:---------|:-----|:-------------|
| tsc --watch  | 是       | 是       | 中等 | 需要编译输出 |
| ts-node-dev  | 否       | 可选     | 中等 | 开发时执行   |

## 编译输出配置

### 输出目录

使用 `--outDir` 指定输出目录：

```bash
tsc --outDir ./dist
```

或在 tsconfig.json 中：

```json
{
  "compilerOptions": {
    "outDir": "./dist"
  }
}
```

### 输出文件

使用 `--outFile` 将所有文件合并为一个文件（仅 AMD 或 System 模块）：

```bash
tsc --outFile bundle.js
```

### 目标版本

使用 `--target` 指定编译目标：

```bash
tsc --target ES2020
```

### 模块系统

使用 `--module` 指定模块系统：

```bash
tsc --module commonjs
tsc --module ES2020
```

### Source Map

生成 source map 文件：

```bash
tsc --sourceMap
```

或在 tsconfig.json 中：

```json
{
  "compilerOptions": {
    "sourceMap": true
  }
}
```

### 声明文件

生成声明文件（.d.ts）：

```bash
tsc --declaration
```

或在 tsconfig.json 中：

```json
{
  "compilerOptions": {
    "declaration": true
  }
}
```

## 编译错误处理

### 错误类型

#### 类型错误

类型不匹配导致的错误：

```ts
let value: string = 123; // 错误：类型 'number' 不能赋值给类型 'string'
```

#### 语法错误

语法不正确导致的错误：

```ts
function fn( { // 错误：缺少右括号
  return 1;
}
```

### 错误修复策略

1. **理解错误信息**：仔细阅读错误信息，理解问题所在
2. **检查类型**：确认类型定义是否正确
3. **查看文档**：查阅相关 API 文档
4. **使用类型断言**：必要时使用类型断言（谨慎使用）

### 忽略特定错误

#### @ts-ignore

忽略下一行的类型错误：

```ts
// @ts-ignore
let value: string = 123;
```

#### @ts-expect-error

期望下一行有错误（如果没有错误会提示）：

```ts
// @ts-expect-error
let value: string = 123;
```

#### @ts-nocheck

忽略整个文件的类型检查：

```ts
// @ts-nocheck
let value: string = 123;
```

### 仅编译不检查

使用 `--transpileOnly`（ts-node）：

```bash
ts-node --transpile-only script.ts
```

**注意**：这会跳过类型检查，仅进行转译。

## 编译性能优化

### 增量编译

启用增量编译：

```json
{
  "compilerOptions": {
    "incremental": true
  }
}
```

### 项目引用

使用项目引用管理大型项目：

```json
{
  "compilerOptions": {
    "composite": true
  },
  "references": [
    { "path": "./core" },
    { "path": "./utils" }
  ]
}
```

### 跳过类型检查（开发时）

开发时可以使用 `--transpileOnly` 跳过类型检查：

```bash
ts-node --transpileOnly script.ts
```

### 并行编译

使用构建工具（如 esbuild、swc）进行并行编译。

## 编译工作流

### 开发环境

**推荐**：使用直接执行工具（ts-node、tsx）

```json
{
  "scripts": {
    "dev": "ts-node-dev --respawn --transpile-only src/index.ts"
  }
}
```

### 构建环境

**推荐**：使用 tsc 进行完整编译

```json
{
  "scripts": {
    "build": "tsc",
    "build:watch": "tsc --watch"
  }
}
```

### 类型检查

单独进行类型检查（不生成文件）：

```bash
tsc --noEmit
```

```json
{
  "scripts": {
    "type-check": "tsc --noEmit"
  }
}
```

## 常见问题

### 问题 1：编译速度慢

**解决方案**：
- 启用增量编译
- 使用项目引用
- 排除不需要的文件
- 使用更快的工具（tsx、esbuild）

### 问题 2：输出文件不正确

**解决方案**：
- 检查 outDir 配置
- 检查 include/exclude 配置
- 检查 rootDir 配置

### 问题 3：类型错误过多

**解决方案**：
- 逐步修复错误
- 使用 `@ts-ignore` 临时忽略（谨慎）
- 检查 tsconfig.json 配置

## 注意事项

1. **生产环境**：生产环境应使用编译后的 JavaScript
2. **类型检查**：定期进行完整的类型检查
3. **性能优化**：大型项目注意编译性能
4. **错误处理**：及时修复编译错误，避免累积

## 最佳实践

1. **开发环境**：使用直接执行工具，提升开发效率
2. **构建环境**：使用 tsc 进行完整编译和类型检查
3. **增量编译**：启用增量编译提升性能
4. **错误处理**：及时修复编译错误，避免使用过多 @ts-ignore

## 练习

1. **基本编译**：使用 tsc 编译 TypeScript 文件。

2. **项目编译**：配置 tsconfig.json，编译整个项目。

3. **监视模式**：使用 `tsc --watch` 启用监视模式。

4. **输出配置**：配置输出目录、source map、声明文件等。

5. **性能优化**：启用增量编译，体验性能提升。

完成以上练习后，继续学习下一章，了解基础类型系统。

## 总结

TypeScript 编译是开发的核心操作。理解 tsc 命令的使用、编译模式、监视模式和输出配置是使用 TypeScript 的基础。开发时可以使用直接执行工具提升效率，构建时使用 tsc 进行完整编译和类型检查。

## 相关资源

- [TypeScript 编译器选项](https://www.typescriptlang.org/tsconfig#compilerOptions)
- [TypeScript 编译选项](https://www.typescriptlang.org/docs/handbook/compiler-options.html)
