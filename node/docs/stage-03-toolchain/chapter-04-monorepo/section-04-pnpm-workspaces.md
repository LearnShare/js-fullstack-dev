# 3.4.4 pnpm Workspaces

## 1. 概述

pnpm Workspaces 是 pnpm 内置的 Monorepo 支持功能，提供了简单的工作区管理能力。pnpm Workspaces 配置简单，适合简单的 Monorepo 项目，特别是已经使用 pnpm 的项目。

## 2. 特性说明

- **简单配置**：配置简单，只需一个配置文件。
- **依赖管理**：统一管理依赖，避免重复安装。
- **工作区链接**：工作区之间可以相互引用。
- **pnpm 集成**：与 pnpm 深度集成，使用 pnpm 命令即可。
- **性能优势**：利用 pnpm 的性能优势。

## 3. 安装与配置

### 配置 pnpm Workspaces

```yaml
# 文件: pnpm-workspace.yaml
# 功能: pnpm Workspaces 配置

packages:
  - 'packages/*'
  - 'apps/*'
```

### 根 package.json

```json
// 文件: package.json (根目录)
// 功能: Monorepo 根配置

{
  "name": "my-monorepo",
  "private": true,
  "scripts": {
    "build": "pnpm -r run build",
    "dev": "pnpm -r run dev",
    "lint": "pnpm -r run lint"
  }
}
```

## 4. 基本用法

### 示例 1：安装依赖

```bash
# 文件: pnpm-workspace.sh
# 功能: pnpm Workspaces 基本使用

# 在根目录安装依赖（所有工作区）
pnpm install

# 在特定工作区安装依赖
pnpm --filter packages/shared add express

# 为所有工作区添加依赖
pnpm -r add typescript
```

### 示例 2：运行脚本

```bash
# 文件: pnpm-scripts.sh
# 功能: pnpm Workspaces 运行脚本

# 运行所有工作区的 build 脚本
pnpm -r run build

# 运行特定工作区的脚本
pnpm --filter packages/shared run build

# 运行多个工作区的脚本
pnpm --filter packages/* run build
```

### 示例 3：工作区依赖

```json
// 文件: packages/app/package.json
// 功能: 工作区依赖配置

{
  "name": "@my-monorepo/app",
  "dependencies": {
    "@my-monorepo/shared": "workspace:*",
    "@my-monorepo/utils": "workspace:*"
  }
}
```

## 5. 参数说明：pnpm Workspaces 命令

### pnpm 命令参数

| 参数名       | 说明                                     | 示例                           |
|:-------------|:-----------------------------------------|:-------------------------------|
| **-r**       | 递归运行（所有工作区）                   | `pnpm -r run build`            |
| **--filter** | 过滤工作区                               | `pnpm --filter shared add express`|
| **-w**       | 在根目录运行                             | `pnpm -w add typescript`       |

## 6. 返回值与状态说明

pnpm Workspaces 操作的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **安装**     | 成功/失败    | 显示安装的包信息                         |
| **运行脚本** | 脚本输出     | 显示脚本的执行结果                       |

## 7. 代码示例：完整的 pnpm Workspaces 配置

以下示例演示了完整的 pnpm Workspaces 配置：

```yaml
# 文件: pnpm-workspace.yaml
# 功能: 完整的 pnpm Workspaces 配置

packages:
  - 'packages/*'
  - 'apps/*'
  - 'tools/*'
```

```json
// 文件: package.json (根目录)
// 功能: Monorepo 根配置

{
  "name": "my-monorepo",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "build": "pnpm -r --parallel run build",
    "dev": "pnpm -r --parallel run dev",
    "lint": "pnpm -r run lint",
    "test": "pnpm -r run test",
    "clean": "pnpm -r run clean"
  },
  "devDependencies": {
    "typescript": "^5.3.0",
    "@types/node": "^20.10.0"
  }
}
```

```json
// 文件: packages/shared/package.json
// 功能: 工作区包配置

{
  "name": "@my-monorepo/shared",
  "version": "1.0.0",
  "main": "dist/index.js",
  "types": "dist/index.d.ts",
  "scripts": {
    "build": "tsc",
    "dev": "tsx watch src/index.ts"
  },
  "dependencies": {}
}
```

## 8. 输出结果说明

pnpm Workspaces 执行的输出结果：

```text
Scope: 4 packages
packages/shared build$ tsc
packages/api build$ tsc
apps/web build$ vite build
apps/admin build$ vite build

packages/shared build: Done
packages/api build: Done
apps/web build: Done
apps/admin build: Done
```

**逻辑解析**：
- 显示作用域内的包数量
- 显示每个包的脚本执行
- 显示执行结果

## 9. 使用场景

### 1. 简单 Monorepo

适合简单的 Monorepo 项目：

```yaml
# pnpm-workspace.yaml
packages:
  - 'packages/*'
```

### 2. 使用 pnpm 的项目

适合已经使用 pnpm 的项目：

```bash
# 直接使用 pnpm 命令
pnpm -r run build
```

### 3. 小型团队项目

适合小型团队项目：

```bash
# 简单的工作区管理
pnpm --filter shared add express
```

## 10. 注意事项与常见错误

- **工作区命名**：工作区包名应该使用作用域命名（如 `@my-monorepo/shared`）
- **依赖版本**：工作区依赖使用 `workspace:*` 版本
- **脚本执行**：使用 `-r` 递归运行，`--parallel` 并行执行
- **性能考虑**：大型项目可能需要配合 Turborepo 等工具
- **配置简单**：功能相对简单，复杂需求可能需要其他工具

## 11. 常见问题 (FAQ)

**Q: pnpm Workspaces 和 Turborepo 可以一起使用吗？**
A: 可以，pnpm Workspaces 管理依赖，Turborepo 管理任务执行。

**Q: 如何在工作区之间共享代码？**
A: 使用 `workspace:*` 版本引用其他工作区包。

**Q: 如何运行特定工作区的脚本？**
A: 使用 `--filter` 参数，如 `pnpm --filter shared run build`。

## 12. 最佳实践

- **工作区命名**：使用作用域命名，避免冲突
- **依赖管理**：统一管理依赖，使用锁定文件
- **脚本组织**：合理组织脚本，使用递归执行
- **性能优化**：大型项目配合 Turborepo 等工具
- **文档说明**：为工作区结构提供文档说明

## 13. 对比分析：pnpm Workspaces vs Turborepo vs Nx

| 维度             | pnpm Workspaces                      | Turborepo                              | Nx                                    |
|:-----------------|:-------------------------------------|:---------------------------------------|:--------------------------------------|
| **功能**         | 工作区管理                           | 任务执行、缓存                         | 任务执行、缓存、代码生成               |
| **配置复杂度**   | 简单（pnpm 内置）                    | 简单                                   | 复杂                                  |
| **性能**         | 中等（依赖 pnpm）                    | 快（缓存和并行）                       | 快（缓存和并行）                      |
| **适用场景**     | 简单 Monorepo、使用 pnpm             | 现代项目、追求速度                     | 大型项目、需要复杂功能                 |
| **推荐使用**     | 简单 Monorepo                        | ✅ 推荐（现代项目）                     | 大型项目                              |

## 14. 练习任务

1. **pnpm Workspaces 实践**：
   - 配置 pnpm Workspaces
   - 理解工作区结构
   - 管理工作区依赖

2. **脚本执行实践**：
   - 运行工作区脚本
   - 理解过滤和递归
   - 配置并行执行

3. **实际应用**：
   - 在实际项目中应用 pnpm Workspaces
   - 优化工作区结构
   - 提升开发效率

完成以上练习后，继续学习下一章：调试工具。

## 总结

pnpm Workspaces 是简单的 Monorepo 解决方案：

- **核心功能**：工作区管理、依赖管理、脚本执行
- **适用场景**：简单 Monorepo、使用 pnpm、小型团队
- **最佳实践**：工作区命名、依赖管理、脚本组织

掌握 pnpm Workspaces 有助于管理简单的 Monorepo 项目。

---

**最后更新**：2025-01-XX
