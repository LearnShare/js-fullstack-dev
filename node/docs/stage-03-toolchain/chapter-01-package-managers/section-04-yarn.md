# 3.1.4 yarn（经典包管理器）

## 1. 概述

yarn 是 Facebook 开发的包管理器，提供了快速、可靠、安全的依赖管理。yarn 在 npm 的基础上改进了性能和可靠性，引入了锁定文件机制。虽然现在有 pnpm 等更现代的选择，但 yarn 仍然是许多项目的可靠选择。

## 2. 特性说明

- **快速安装**：并行安装，缓存机制。
- **锁定文件**：yarn.lock 确保依赖一致性。
- **离线模式**：支持离线安装。
- **工作区支持**：支持 Monorepo 工作区。
- **插件系统**：支持插件扩展功能。

## 3. 安装与配置

### 安装 yarn

```bash
# 使用 npm 安装
npm install -g yarn

# 使用独立安装脚本
corepack enable
corepack prepare yarn@stable --activate

# 使用 Homebrew (macOS)
brew install yarn
```

### 验证安装

```bash
yarn --version
```

## 4. 基本用法

### 示例 1：项目初始化

```bash
# 文件: yarn-init.sh
# 功能: 初始化 yarn 项目

# 初始化项目
yarn init

# 或使用 npm 的 package.json
npm init -y
```

### 示例 2：安装依赖

```bash
# 文件: yarn-install.sh
# 功能: 安装依赖

# 安装生产依赖
yarn add express

# 安装开发依赖
yarn add -D typescript @types/node

# 安装全局包
yarn global add typescript

# 安装所有依赖
yarn install
```

### 示例 3：管理脚本

运行脚本的方式与 npm 相同：

```bash
yarn run build
yarn run dev
yarn start  # 可以省略 run
```

## 5. 参数说明：yarn 命令参数

| 命令           | 说明                                     | 示例                           |
|:---------------|:-----------------------------------------|:-------------------------------|
| **add**        | 添加依赖                                 | `yarn add express`             |
| **remove**     | 删除依赖                                 | `yarn remove express`          |
| **upgrade**    | 更新依赖                                 | `yarn upgrade`                 |
| **install**    | 安装所有依赖                             | `yarn install`                 |
| **run**        | 运行脚本                                 | `yarn run build`               |
| **list**       | 列出依赖                                 | `yarn list`                    |

## 6. yarn 的特性

### 1. 锁定文件

yarn.lock 确保依赖版本一致性：

```yaml
# yarn.lock 示例
express@^4.18.0:
  version "4.18.2"
  resolved "https://registry.npmjs.org/express/-/express-4.18.2.tgz"
  integrity sha512-5/PsL6iGPdfQ/lKM1UuielYgv3BUoJfz1aUwU9vHZ+J7gyvwdQXFEBIEIaxeGf0GIcreATNyBExtalisDbuMqQ==
  dependencies:
    accepts "~1.3.8"
    array-flatten "1.1.1"
    ...
```

### 2. 工作区支持

支持 Monorepo 工作区：

```json
{
  "workspaces": [
    "packages/*"
  ]
}
```

### 3. 插件系统

支持插件扩展功能：

```bash
yarn plugin import <plugin-name>
```

## 7. 代码示例：yarn 工作流

以下示例演示了 yarn 的完整工作流：

```bash
# 文件: yarn-workflow.sh
# 功能: yarn 完整工作流

# 1. 初始化项目
yarn init

# 2. 安装生产依赖
yarn add express cors dotenv

# 3. 安装开发依赖
yarn add -D typescript @types/node @types/express tsx

# 4. 配置 package.json
cat > package.json << 'EOF'
{
  "name": "my-app",
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "tsx watch src/index.ts",
    "build": "tsc",
    "start": "node dist/index.js"
  }
}
EOF

# 5. 运行开发服务器
yarn run dev

# 6. 构建项目
yarn run build
```

## 8. 输出结果说明

yarn 命令的输出结果：

```text
yarn add v1.22.19
info No lockfile found.
[1/4] Resolving packages...
[2/4] Fetching packages...
[3/4] Linking dependencies...
[4/4] Building fresh packages...
success Saved lockfile.
✨  Done in 5.23s.
```

**逻辑解析**：
- 显示 yarn 版本
- 显示安装步骤
- 显示完成时间

## 9. 使用场景

### 1. 企业项目

适合需要稳定性的企业项目：

```bash
# 企业项目使用 yarn
yarn install  # 稳定可靠
```

### 2. Monorepo

支持 Monorepo 工作区：

```bash
# Monorepo 项目
yarn workspaces info
yarn workspace package-a add express
```

### 3. 离线安装

支持离线模式：

```bash
# 离线安装
yarn install --offline
```

## 10. 注意事项与常见错误

- **锁定文件**：yarn.lock 应该提交到版本控制
- **版本兼容**：注意 yarn 1.x 和 yarn 2+ 的差异
- **迁移**：从 npm 迁移到 yarn 需要删除 node_modules 和 package-lock.json
- **性能**：yarn 1.x 性能与 npm 相当，yarn 2+ 有改进

## 11. 常见问题 (FAQ)

**Q: yarn 1.x 和 yarn 2+ 有什么区别？**
A: yarn 2+ 引入了 PnP（Plug'n'Play）模式，不再使用 node_modules，但兼容性可能有问题。

**Q: 如何从 npm 迁移到 yarn？**
A: 删除 node_modules 和 package-lock.json，然后运行 `yarn install`。

**Q: yarn 和 npm 可以混用吗？**
A: 不建议混用，应该统一使用一个包管理器。

## 12. 最佳实践

- **使用锁定文件**：提交 yarn.lock 到版本控制
- **统一使用**：项目统一使用 yarn，不要混用其他包管理器
- **工作区**：在 Monorepo 项目中使用 yarn workspaces
- **版本选择**：根据项目需求选择 yarn 1.x 或 yarn 2+

## 13. 对比分析：yarn vs npm vs pnpm

| 维度             | yarn                                    | npm                                    | pnpm                                    |
|:-----------------|:----------------------------------------|:---------------------------------------|:----------------------------------------|
| **安装速度**     | 中等（yarn 1.x）或快（yarn 2+）         | 中等                                   | 快                                      |
| **磁盘空间**     | 每个项目独立                            | 每个项目独立                            | 节省（全局存储）                        |
| **锁定文件**     | yarn.lock                               | package-lock.json                      | pnpm-lock.yaml                          |
| **Monorepo**     | 良好支持                                | 基础支持                                | 优秀支持                                |
| **稳定性**       | 高                                      | 高                                      | 高                                      |

## 14. 练习任务

1. **yarn 基础实践**：
   - 安装和配置 yarn
   - 使用 yarn 初始化项目
   - 理解 yarn.lock 的作用

2. **依赖管理实践**：
   - 使用 yarn 管理依赖
   - 理解工作区功能
   - 使用离线模式

3. **Monorepo 实践**：
   - 使用 yarn workspaces 创建 Monorepo
   - 管理 Monorepo 依赖
   - 运行 Monorepo 脚本

4. **实际应用**：
   - 在实际项目中应用 yarn
   - 从 npm 迁移到 yarn
   - 配置 yarn 工作区

完成以上练习后，继续学习下一节：package.json 详解。

## 总结

yarn 是经典的包管理器选择：

- **核心特性**：快速安装、锁定文件、工作区支持
- **适用场景**：企业项目、Monorepo、需要稳定性的场景
- **最佳实践**：使用锁定文件、统一使用、工作区支持

掌握 yarn 有助于管理 Node.js 项目依赖。

---

**最后更新**：2025-01-XX
