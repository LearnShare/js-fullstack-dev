# 3.4.2 Turborepo

## 1. 概述

Turborepo 是 Vercel 开发的高性能 Monorepo 构建系统，提供了快速的任务执行、智能缓存和并行构建功能。Turborepo 专注于速度和简单性，是现代 Monorepo 项目的优秀选择。

## 2. 特性说明

- **快速执行**：并行执行任务，提高构建速度。
- **智能缓存**：缓存任务结果，避免重复执行。
- **任务管道**：定义任务之间的依赖关系。
- **远程缓存**：支持远程缓存，团队共享缓存。
- **简单配置**：配置简单，易于使用。

## 3. 安装与配置

### 安装 Turborepo

```bash
# 安装 Turborepo
npm install -D turbo

# 或使用 pnpm
pnpm add -D turbo
```

### 基本配置

```json
// 文件: turbo.json
// 功能: Turborepo 基本配置

{
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**"]
    },
    "dev": {
      "cache": false
    },
    "lint": {
      "outputs": []
    }
  }
}
```

## 4. 基本用法

### 示例 1：基本任务执行

```bash
# 文件: turbo-basic.sh
# 功能: Turborepo 基本使用

# 运行所有包的 build 任务
npx turbo run build

# 运行特定包的任务
npx turbo run build --filter=packages/shared

# 运行多个包的任务
npx turbo run build --filter=packages/*
```

package.json 配置：

```json
{
  "scripts": {
    "build": "turbo run build",
    "dev": "turbo run dev",
    "lint": "turbo run lint"
  }
}
```

### 示例 2：任务管道配置

```json
// 文件: turbo.json
// 功能: Turborepo 任务管道配置

{
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**", ".next/**"]
    },
    "test": {
      "dependsOn": ["build"],
      "outputs": []
    },
    "lint": {
      "outputs": []
    },
    "dev": {
      "cache": false,
      "persistent": true
    }
  }
}
```

### 示例 3：远程缓存配置

```json
// 文件: turbo.json
// 功能: Turborepo 远程缓存配置

{
  "remoteCache": {
    "enabled": true
  },
  "pipeline": {
    "build": {
      "outputs": ["dist/**"]
    }
  }
}
```

## 5. 参数说明：Turborepo 配置选项

### pipeline 配置

| 配置项       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **dependsOn**| Array    | 任务依赖                                 | `["^build"]`                   |
| **outputs**  | Array    | 输出文件模式                             | `["dist/**"]`                  |
| **cache**    | Boolean  | 是否缓存（默认 true）                    | `false`                        |
| **persistent**| Boolean | 是否为持久任务（如 dev）                | `true`                         |

### 命令行参数

| 参数名       | 说明                                     | 示例                           |
|:-------------|:-----------------------------------------|:-------------------------------|
| **--filter** | 过滤包                                   | `--filter=packages/shared`     |
| **--cache-dir**| 缓存目录                               | `--cache-dir=.turbo`           |
| **--force**  | 强制执行，忽略缓存                       | `--force`                      |

## 6. 返回值与状态说明

Turborepo 操作的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **任务执行** | 成功/失败    | 显示任务执行结果和统计                   |

## 7. 代码示例：完整的 Turborepo 配置

以下示例演示了完整的 Turborepo 配置：

```json
// 文件: turbo.json
// 功能: 完整的 Turborepo 配置

{
  "$schema": "https://turbo.build/schema.json",
  "globalDependencies": ["tsconfig.json"],
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**", ".next/**", "build/**"]
    },
    "test": {
      "dependsOn": ["build"],
      "outputs": ["coverage/**"]
    },
    "lint": {
      "outputs": []
    },
    "type-check": {
      "dependsOn": ["^build"],
      "outputs": []
    },
    "dev": {
      "cache": false,
      "persistent": true
    },
    "clean": {
      "cache": false
    }
  }
}
```

## 8. 输出结果说明

Turborepo 执行的输出结果：

```text
• Packages in scope: 4
• Running build in 4 packages
✓ packages/shared:build (cached)
✓ packages/api:build
✓ packages/web:build (cached)
✓ apps/admin:build
• Tasks:    4 successful, 4 total
• Cached:   2/4 (50%)
• Time:     1.2s
```

**逻辑解析**：
- 显示作用域内的包数量
- 显示运行的任务和结果
- 显示缓存命中情况
- 显示任务统计和执行时间

## 9. 使用场景

### 1. 现代 Monorepo 项目

适合现代 Monorepo 项目：

```bash
# 快速构建
turbo run build

# 并行开发
turbo run dev
```

### 2. 大型项目

适合大型项目，提高构建速度：

```json
{
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**"]
    }
  }
}
```

### 3. 团队协作

适合团队协作，共享缓存：

```json
{
  "remoteCache": {
    "enabled": true
  }
}
```

## 10. 注意事项与常见错误

- **任务依赖**：正确配置任务依赖关系
- **输出配置**：正确配置输出文件模式，确保缓存正确
- **缓存失效**：理解缓存失效的条件
- **性能优化**：合理配置并行和缓存提高性能
- **远程缓存**：配置远程缓存需要认证

## 11. 常见问题 (FAQ)

**Q: Turborepo 如何决定是否使用缓存？**
A: 根据输入文件、依赖任务、环境变量等决定，如果都相同则使用缓存。

**Q: 如何清理缓存？**
A: 删除 `.turbo` 目录，或使用 `turbo run clean`。

**Q: 如何配置远程缓存？**
A: 使用 Vercel 或其他支持的服务，配置认证信息。

## 12. 最佳实践

- **任务管道**：合理配置任务依赖关系
- **输出配置**：正确配置输出文件模式
- **缓存优化**：配置远程缓存提高团队效率
- **性能监控**：监控构建性能，持续优化
- **文档说明**：为任务配置提供文档说明

## 13. 对比分析：Turborepo vs Nx vs pnpm Workspaces

| 维度             | Turborepo                              | Nx                                    | pnpm Workspaces                      |
|:-----------------|:---------------------------------------|:--------------------------------------|:-------------------------------------|
| **性能**         | 快（缓存和并行）                        | 快（缓存和并行）                      | 中等（依赖 pnpm）                    |
| **配置复杂度**   | 简单                                    | 复杂                                  | 简单（pnpm 内置）                    |
| **功能**         | 任务执行、缓存                          | 任务执行、缓存、代码生成              | 工作区管理                           |
| **推荐使用**     | ✅ 推荐（现代项目）                     | 大型项目、需要复杂功能                | 简单 Monorepo                        |

## 14. 练习任务

1. **Turborepo 基础实践**：
   - 配置 Turborepo
   - 理解任务管道
   - 运行任务

2. **缓存实践**：
   - 理解缓存机制
   - 配置输出文件
   - 测试缓存效果

3. **实际应用**：
   - 在实际项目中应用 Turborepo
   - 优化任务配置
   - 提升构建性能

完成以上练习后，继续学习下一节：Nx。

## 总结

Turborepo 是高性能的 Monorepo 构建系统：

- **核心优势**：快速执行、智能缓存、简单配置
- **适用场景**：现代 Monorepo 项目、大型项目、团队协作
- **最佳实践**：任务管道、输出配置、缓存优化

掌握 Turborepo 有助于提高 Monorepo 项目的构建效率。

---

**最后更新**：2025-01-XX
