# 3.4.3 Nx

## 1. 概述

Nx 是一个功能强大的 Monorepo 工具，提供了任务执行、缓存、代码生成、依赖图分析等功能。Nx 适合大型项目和需要复杂工作流的场景，提供了丰富的插件和工具。

## 2. 特性说明

- **任务执行**：并行执行任务，支持任务依赖。
- **智能缓存**：缓存任务结果，支持远程缓存。
- **代码生成**：支持代码生成和脚手架。
- **依赖图**：可视化依赖关系，分析影响范围。
- **插件生态**：丰富的插件生态系统。

## 3. 安装与配置

### 安装 Nx

```bash
# 创建 Nx 工作区
npx create-nx-workspace@latest my-workspace

# 或在现有项目中安装
npm install -D nx
```

### 基本配置

```json
// 文件: nx.json
// 功能: Nx 基本配置

{
  "tasksRunnerOptions": {
    "default": {
      "runner": "nx/tasks-runners/default",
      "options": {
        "cacheableOperations": ["build", "test", "lint"]
      }
    }
  }
}
```

## 4. 基本用法

### 示例 1：基本任务执行

```bash
# 文件: nx-basic.sh
# 功能: Nx 基本使用

# 运行所有项目的 build 任务
npx nx run-many --target=build --all

# 运行特定项目的任务
npx nx build my-app

# 运行受影响的任务
npx nx affected --target=build
```

### 示例 2：代码生成

```bash
# 文件: nx-generate.sh
# 功能: Nx 代码生成

# 生成应用
npx nx generate @nx/node:application my-api

# 生成库
npx nx generate @nx/node:library my-lib

# 生成组件
npx nx generate @nx/react:component my-component
```

### 示例 3：依赖图分析

```bash
# 文件: nx-graph.sh
# 功能: Nx 依赖图分析

# 查看依赖图
npx nx graph

# 查看特定项目的依赖
npx nx graph --focus=my-app
```

## 5. 参数说明：Nx 配置选项

### nx.json 配置

| 配置项       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **tasksRunnerOptions**| Object | 任务运行器配置                       | `{ default: {...} }`           |
| **cacheableOperations**| Array | 可缓存的操作列表                   | `["build", "test"]`            |

### 命令行参数

| 参数名       | 说明                                     | 示例                           |
|:-------------|:-----------------------------------------|:-------------------------------|
| **--target** | 目标任务                                 | `--target=build`               |
| **--all**    | 所有项目                                 | `--all`                        |
| **--affected**| 受影响的项目                            | `--affected`                   |

## 6. 返回值与状态说明

Nx 操作的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **任务执行** | 成功/失败    | 显示任务执行结果和统计                   |
| **代码生成** | 成功/失败    | 显示生成的文件和配置                     |

## 7. 代码示例：完整的 Nx 配置

以下示例演示了完整的 Nx 配置：

```json
// 文件: nx.json
// 功能: 完整的 Nx 配置

{
  "$schema": "./node_modules/nx/schemas/nx-schema.json",
  "tasksRunnerOptions": {
    "default": {
      "runner": "nx/tasks-runners/default",
      "options": {
        "cacheableOperations": ["build", "test", "lint"],
        "parallel": 3
      }
    }
  },
  "targetDefaults": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["{projectRoot}/dist"]
    },
    "test": {
      "dependsOn": ["build"],
      "outputs": ["{projectRoot}/coverage"]
    }
  },
  "namedInputs": {
    "default": ["{projectRoot}/**/*", "sharedGlobals"],
    "production": [
      "default",
      "!{projectRoot}/**/*.spec.ts",
      "!{projectRoot}/**/*.test.ts"
    ]
  }
}
```

## 8. 输出结果说明

Nx 执行的输出结果：

```text
> nx run-many --target=build --all

Running target build for 4 project(s):

  my-app:build
  my-lib:build
  shared:build
  utils:build

  ✓  my-app:build (cached)
  ✓  my-lib:build
  ✓  shared:build (cached)
  ✓  utils:build

————————————————————————————————————————————————————————————————————
  ✓  Ran target build for 4 projects (2 cached, 2 new)
```

**逻辑解析**：
- 显示运行的目标和项目
- 显示任务执行结果
- 显示缓存情况
- 显示执行统计

## 9. 使用场景

### 1. 大型 Monorepo 项目

适合大型 Monorepo 项目：

```bash
# 运行受影响的任务
nx affected --target=build

# 并行执行任务
nx run-many --target=test --all --parallel=5
```

### 2. 需要代码生成的项目

适合需要代码生成的项目：

```bash
# 生成应用和库
nx generate @nx/node:application api
nx generate @nx/node:library shared
```

### 3. 需要依赖分析的项目

适合需要依赖分析的项目：

```bash
# 查看依赖图
nx graph

# 分析影响范围
nx affected:graph
```

## 10. 注意事项与常见错误

- **配置复杂度**：Nx 配置较为复杂，需要理解概念
- **学习曲线**：Nx 学习曲线较陡
- **插件依赖**：需要安装相应的插件
- **性能考虑**：大型项目需要优化配置
- **迁移成本**：从其他工具迁移到 Nx 需要成本

## 11. 常见问题 (FAQ)

**Q: Nx 和 Turborepo 如何选择？**
A: Nx 功能更强大，适合大型项目；Turborepo 更简单，适合现代项目。

**Q: 如何配置 Nx 缓存？**
A: 在 `nx.json` 中配置 `cacheableOperations`，或使用远程缓存。

**Q: Nx 支持哪些框架？**
A: Nx 支持 React、Vue、Angular、Node.js 等多种框架。

## 12. 最佳实践

- **任务配置**：合理配置任务依赖和输出
- **缓存优化**：配置缓存提高性能
- **代码生成**：使用代码生成提高效率
- **依赖分析**：使用依赖图分析影响范围
- **持续优化**：持续优化配置和性能

## 13. 对比分析：Nx vs Turborepo

| 维度             | Nx                                    | Turborepo                              |
|:-----------------|:--------------------------------------|:---------------------------------------|
| **功能**         | 功能强大（任务、缓存、代码生成）      | 专注任务执行和缓存                     |
| **配置复杂度**   | 复杂                                  | 简单                                   |
| **学习曲线**     | 陡峭                                  | 平缓                                   |
| **适用场景**     | 大型项目、需要复杂功能                | 现代项目、追求简单                     |
| **推荐使用**     | 大型项目、需要代码生成                | ✅ 推荐（现代项目）                     |

## 14. 练习任务

1. **Nx 基础实践**：
   - 创建 Nx 工作区
   - 理解任务执行
   - 配置缓存

2. **代码生成实践**：
   - 使用代码生成功能
   - 生成应用和库
   - 理解生成的结构

3. **实际应用**：
   - 在实际项目中应用 Nx
   - 优化任务配置
   - 提升构建效率

完成以上练习后，继续学习下一节：pnpm Workspaces。

## 总结

Nx 是功能强大的 Monorepo 工具：

- **核心功能**：任务执行、缓存、代码生成、依赖分析
- **适用场景**：大型项目、需要复杂功能、需要代码生成
- **最佳实践**：任务配置、缓存优化、代码生成

掌握 Nx 有助于管理大型 Monorepo 项目。

---

**最后更新**：2025-01-XX
