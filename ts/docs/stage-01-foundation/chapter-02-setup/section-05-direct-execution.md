# 1.1.5 TypeScript 直接执行工具

## 概述

直接执行工具允许在不编译的情况下直接运行 TypeScript 代码，提升开发效率。本节介绍常用的 TypeScript 直接执行工具。

## ts-node

### 简介

ts-node 是最常用的 TypeScript 直接执行工具，允许直接执行 TypeScript 文件。

### 安装

#### 全局安装

```bash
npm install -g ts-node
```

#### 项目安装（推荐）

```bash
npm install -D ts-node
```

### 基本使用

#### 执行 TypeScript 文件

```bash
ts-node script.ts
```

或使用 npx：

```bash
npx ts-node script.ts
```

#### 示例

创建 `hello.ts`：

```ts
const message: string = "Hello, TypeScript!";
console.log(message);
```

执行：

```bash
ts-node hello.ts
# 输出：Hello, TypeScript!
```

### 配置选项

#### --transpile-only

跳过类型检查，仅进行转译（更快）：

```bash
ts-node --transpile-only script.ts
```

#### --files

加载 tsconfig.json 中指定的文件：

```bash
ts-node --files script.ts
```

#### --compiler-options

指定编译器选项：

```bash
ts-node --compiler-options '{"target":"ES2020"}' script.ts
```

#### --esm

启用 ESM 支持：

```bash
ts-node --esm script.ts
```

### 与 tsconfig.json 集成

ts-node 会自动读取 tsconfig.json 配置。

也可以在 tsconfig.json 中配置 ts-node 选项：

```json
{
  "ts-node": {
    "transpileOnly": true,
    "files": true,
    "compilerOptions": {
      "module": "commonjs"
    }
  },
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs"
  }
}
```

### 性能优化

**建议**：开发时使用 `--transpile-only` 跳过类型检查，提升执行速度。

```bash
ts-node --transpile-only script.ts
```

或在 package.json 中添加脚本：

```json
{
  "scripts": {
    "dev": "ts-node --transpile-only src/index.ts"
  }
}
```

## tsx

### 简介

tsx 是更快的 TypeScript 执行工具，基于 esbuild。

### 安装

```bash
npm install -D tsx
```

### 基本使用

```bash
tsx script.ts
```

或使用 npx：

```bash
npx tsx script.ts
```

### 与 ts-node 对比

| 特性       | ts-node | tsx     |
|:-----------|:--------|:--------|
| 速度       | 中等    | 快      |
| 类型检查   | 支持    | 可选    |
| ESM 支持   | 需配置  | 原生    |
| 性能       | 中等    | 优秀    |

### 使用场景

- 快速执行脚本
- 开发时的临时执行
- 需要更高性能的场景

## ts-node-dev

### 简介

ts-node-dev 是 ts-node 的包装器，提供热重载功能。

### 安装

```bash
npm install -D ts-node-dev
```

### 基本使用

```bash
ts-node-dev --respawn script.ts
```

### 热重载配置

```bash
# 监听文件变化并自动重启
ts-node-dev --respawn script.ts

# 忽略特定文件
ts-node-dev --respawn --ignore "*.test.ts" script.ts

# 使用 transpile-only 提升性能
ts-node-dev --respawn --transpile-only script.ts
```

### 在 package.json 中配置

```json
{
  "scripts": {
    "dev": "ts-node-dev --respawn --transpile-only src/index.ts"
  }
}
```

### 使用场景

- 开发时的服务器应用
- 需要热重载的 Node.js 应用
- API 服务开发

## bun

### 简介

Bun 是一个快速的 JavaScript 运行时，原生支持 TypeScript。

### 安装

访问 [Bun 官网](https://bun.sh/) 安装。

### 基本使用

```bash
bun run script.ts
```

### TypeScript 支持

Bun 原生支持 TypeScript，无需配置：

```bash
# 直接执行 TypeScript 文件
bun run script.ts

# 或简写
bun script.ts
```

### 性能优势

- 执行速度快
- 启动时间短
- 内存占用低

### 使用场景

- Bun 运行时项目
- 需要高性能的场景
- 新项目选择 Bun 运行时

### 注意事项

- Bun 是相对较新的运行时
- 生态系统仍在发展中
- 某些 Node.js 模块可能不兼容

## deno

### 简介

Deno 是一个安全的 JavaScript 和 TypeScript 运行时，原生支持 TypeScript。

### 安装

访问 [Deno 官网](https://deno.land/) 安装。

### 基本使用

```bash
deno run script.ts
```

### TypeScript 支持

Deno 原生支持 TypeScript，无需配置：

```bash
# 直接执行 TypeScript 文件
deno run script.ts

# 允许网络访问
deno run --allow-net script.ts

# 允许文件系统访问
deno run --allow-read script.ts
```

### 与 Node.js 的对比

| 特性         | Node.js      | Deno        |
|:-------------|:-------------|:------------|
| TypeScript   | 需要工具     | 原生支持    |
| 包管理       | npm          | URL 导入    |
| 安全性       | 默认允许     | 默认限制    |
| 标准库       | 需安装       | 内置        |

### 使用场景

- Deno 运行时项目
- 需要安全性的场景
- 使用 URL 导入的项目

## 工具对比

| 工具        | 速度 | 类型检查 | 热重载 | 适用场景           |
|:------------|:-----|:---------|:-------|:-------------------|
| ts-node     | 中等 | 支持     | 需配合 | Node.js 项目       |
| tsx         | 快   | 可选     | 需配合 | 快速执行、脚本     |
| ts-node-dev | 中等 | 支持     | 支持   | 开发时热重载       |
| bun         | 很快 | 支持     | 支持   | Bun 运行时项目     |
| deno        | 快   | 支持     | 支持   | Deno 运行时项目    |

## 选择建议

### Node.js 项目

**推荐**：ts-node 或 tsx

- 开发时：使用 ts-node-dev 获得热重载
- 快速执行：使用 tsx 获得更高性能
- 类型检查：使用 ts-node 进行完整类型检查

### Bun 项目

**推荐**：bun

- 直接使用 bun 执行 TypeScript
- 享受 Bun 的性能优势

### Deno 项目

**推荐**：deno

- 直接使用 deno 执行 TypeScript
- 享受 Deno 的安全性和标准库

## 注意事项

1. **性能考虑**：开发时可以使用 `--transpile-only` 跳过类型检查
2. **生产环境**：生产环境应使用编译后的 JavaScript
3. **工具选择**：根据项目需求和运行环境选择工具
4. **版本兼容**：确保工具版本与 TypeScript 版本兼容

## 最佳实践

1. **开发环境**：使用直接执行工具提升开发效率
2. **类型检查**：定期进行完整类型检查
3. **生产环境**：使用编译后的 JavaScript
4. **工具统一**：团队使用统一的执行工具

## 练习

1. **ts-node 实践**：使用 ts-node 执行 TypeScript 文件。

2. **tsx 实践**：使用 tsx 执行 TypeScript 文件，对比性能。

3. **ts-node-dev 实践**：配置 ts-node-dev 实现热重载。

4. **工具对比**：对比不同工具的执行速度和功能。

5. **项目配置**：在项目中配置直接执行工具的脚本。

完成以上练习后，继续学习下一节，了解编译操作与实践。

## 总结

TypeScript 直接执行工具可以显著提升开发效率。ts-node 是最常用的工具，tsx 提供更高的性能，ts-node-dev 提供热重载功能。Bun 和 Deno 作为现代运行时也原生支持 TypeScript。根据项目需求和运行环境选择合适的工具。

## 相关资源

- [ts-node GitHub](https://github.com/TypeStrong/ts-node)
- [tsx GitHub](https://github.com/esbuild-kit/tsx)
- [ts-node-dev GitHub](https://github.com/wclr/ts-node-dev)
- [Bun 官网](https://bun.sh/)
- [Deno 官网](https://deno.land/)
