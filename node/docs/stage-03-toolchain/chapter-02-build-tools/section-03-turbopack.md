# 3.2.3 Turbopack（Next.js 构建工具）

## 1. 概述

Turbopack 是 Next.js 团队开发的下一代构建工具，使用 Rust 编写，提供了极快的构建速度。Turbopack 专为 Next.js 设计，但也可以独立使用。理解 Turbopack 的特点对于使用 Next.js 开发非常重要。

## 2. 特性说明

- **极速构建**：使用 Rust 编写，构建速度极快。
- **增量编译**：只编译修改的文件，提高开发效率。
- **Next.js 集成**：与 Next.js 深度集成，开箱即用。
- **Webpack 兼容**：兼容大部分 Webpack 配置和插件。
- **现代特性**：支持最新的 JavaScript 和 TypeScript 特性。

## 3. 安装与使用

### Next.js 中使用 Turbopack

```bash
# 创建 Next.js 项目（使用 Turbopack）
npx create-next-app@latest my-app --turbo

# 或在现有项目中启用
npm run dev --turbo
```

### 独立使用 Turbopack

```bash
# 安装 Turbopack
npm install -D turbo

# 使用 Turbopack
turbo build
```

## 4. 基本用法

### 示例 1：Next.js 项目

```bash
# 文件: nextjs-turbopack.sh
# 功能: Next.js 项目使用 Turbopack

# 创建 Next.js 项目（使用 Turbopack）
npx create-next-app@latest my-app --turbo

# 开发（使用 Turbopack）
npm run dev

# 构建（使用 Turbopack）
npm run build
```

### 示例 2：配置 Next.js

```ts
// 文件: next.config.ts
// 功能: Next.js 配置（Turbopack）

import type { NextConfig } from 'next';

const nextConfig: NextConfig = {
    // Turbopack 相关配置
    experimental: {
        turbo: {
            rules: {
                '*.svg': {
                    loaders: ['@svgr/webpack'],
                    as: '*.js'
                }
            }
        }
    }
};

export default nextConfig;
```

## 5. 参数说明：Turbopack 配置

### Next.js 配置

| 配置项       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **experimental.turbo**| Object | Turbopack 配置                           | `{ rules: {...} }`             |
| **experimental.turbo.rules**| Object | 文件处理规则                         | `{ '*.svg': {...} }`           |

## 6. Turbopack 的优势

### 1. 构建速度

Turbopack 的构建速度比 Webpack 快很多：

- **开发启动**：比 Webpack 快 10-100 倍
- **HMR**：比 Webpack 快 5-10 倍
- **生产构建**：比 Webpack 快 2-5 倍

### 2. 增量编译

只编译修改的文件，提高开发效率：

```
修改文件: src/components/Button.tsx
↓
Turbopack 只编译 Button.tsx 及其依赖
↓
快速更新，无需重新编译整个项目
```

### 3. Next.js 集成

与 Next.js 深度集成，开箱即用：

- 自动配置路由
- 自动代码分割
- 自动优化图片
- 自动处理 CSS

## 7. 代码示例：Turbopack 配置

以下示例演示了 Turbopack 的配置：

```ts
// 文件: next.config.ts
// 功能: Turbopack 完整配置

import type { NextConfig } from 'next';

const nextConfig: NextConfig = {
    // Turbopack 配置
    experimental: {
        turbo: {
            // 文件处理规则
            rules: {
                // SVG 处理
                '*.svg': {
                    loaders: ['@svgr/webpack'],
                    as: '*.js'
                },
                // 自定义文件处理
                '*.custom': {
                    loaders: ['./custom-loader'],
                    as: '*.js'
                }
            },
            // 解析别名
            resolveAlias: {
                '@': './src',
                '@components': './src/components'
            },
            // 环境变量
            env: {
                CUSTOM_VAR: 'value'
            }
        }
    }
};

export default nextConfig;
```

## 8. 输出结果说明

Turbopack 构建的输出结果：

```text
▲ Next.js 15.0.0
- Local:        http://localhost:3000
- Environments: .env.local

✓ Ready in 200ms
```

**逻辑解析**：
- 显示 Next.js 版本
- 显示本地服务器地址
- 显示环境文件
- 显示启动时间（极快）

## 9. 使用场景

### 1. Next.js 项目

Next.js 项目的首选构建工具：

```bash
# 创建 Next.js 项目（使用 Turbopack）
npx create-next-app@latest my-app --turbo

# 开发
npm run dev

# 构建
npm run build
```

### 2. 大型项目

适合大型项目，构建速度快：

```bash
# 大型项目使用 Turbopack
npm run dev  # 快速启动
```

### 3. 需要快速迭代的项目

适合需要快速迭代的项目：

```bash
# 快速 HMR
npm run dev  # 修改文件后立即看到效果
```

## 10. 注意事项与常见错误

- **Next.js 专用**：Turbopack 主要针对 Next.js，独立使用功能有限
- **插件兼容**：部分 Webpack 插件可能不兼容
- **配置方式**：配置方式与 Webpack 不同
- **版本要求**：需要 Next.js 13+ 才能使用
- **实验性功能**：Turbopack 仍在开发中，某些功能可能不稳定

## 11. 常见问题 (FAQ)

**Q: Turbopack 可以独立使用吗？**
A: 可以，但功能有限，主要针对 Next.js 优化。

**Q: Turbopack 和 Webpack 有什么区别？**
A: Turbopack 使用 Rust 编写，速度更快；Webpack 功能更丰富，生态更完善。

**Q: 如何从 Webpack 迁移到 Turbopack？**
A: 在 Next.js 项目中，使用 `--turbo` 标志即可，大部分配置会自动迁移。

## 12. 最佳实践

- **Next.js 项目**：Next.js 项目优先使用 Turbopack
- **配置优化**：根据项目需求配置 Turbopack 规则
- **性能监控**：监控构建性能，优化配置
- **保持更新**：Turbopack 仍在开发中，保持更新

## 13. 对比分析：Turbopack vs Webpack vs Vite

| 维度             | Turbopack                              | Webpack                                | Vite                                    |
|:-----------------|:---------------------------------------|:---------------------------------------|:----------------------------------------|
| **构建速度**     | 极快（Rust 编写）                      | 中等                                   | 快（基于 ESM）                           |
| **适用场景**     | Next.js 项目                           | 通用项目                               | 现代前端项目                             |
| **配置复杂度**   | 简单（Next.js 集成）                   | 复杂                                   | 简单                                    |
| **生态支持**     | Next.js 生态                           | 非常丰富                               | 良好                                    |

## 14. 练习任务

1. **Turbopack 实践**：
   - 创建 Next.js 项目（使用 Turbopack）
   - 理解 Turbopack 的构建速度
   - 配置 Turbopack 规则

2. **性能对比实践**：
   - 对比 Turbopack 和 Webpack 的构建速度
   - 理解增量编译的优势
   - 优化构建配置

3. **实际应用**：
   - 在实际 Next.js 项目中应用 Turbopack
   - 优化构建性能
   - 提升开发体验

完成以上练习后，继续学习下一节：Webpack（传统构建工具）。

## 总结

Turbopack 是 Next.js 的极速构建工具：

- **核心优势**：极速构建、增量编译、Next.js 集成
- **适用场景**：Next.js 项目、大型项目、需要快速迭代的项目
- **最佳实践**：Next.js 项目优先使用、配置优化、保持更新

掌握 Turbopack 有助于提高 Next.js 项目的开发效率。

---

**最后更新**：2025-01-XX
