# 3.1.3 pnpm（现代包管理器）

## 1. 概述

pnpm（performant npm）是一个快速、节省磁盘空间的包管理器。pnpm 使用内容寻址存储和硬链接，实现了严格的依赖隔离，避免了依赖提升问题。理解 pnpm 的使用对于大型项目和 Monorepo 开发非常重要。

## 2. 特性说明

- **高性能**：安装速度快，磁盘空间效率高。
- **严格隔离**：每个包只能访问 package.json 中声明的依赖。
- **全局存储**：使用全局存储和硬链接，节省磁盘空间。
- **Monorepo 支持**：优秀的 Monorepo 支持。
- **兼容性**：与 npm 和 yarn 兼容。

## 3. 安装与配置

### 安装 pnpm

```bash
# 使用 npm 安装
npm install -g pnpm

# 使用独立安装脚本
curl -fsSL https://get.pnpm.io/install.sh | sh -

# 使用 Homebrew (macOS)
brew install pnpm
```

### 验证安装

```bash
pnpm --version
```

## 4. 基本用法

### 示例 1：项目初始化

```bash
# 文件: pnpm-init.sh
# 功能: 初始化 pnpm 项目

# 初始化项目
pnpm init

# 或使用 npm 的 package.json
npm init -y
```

### 示例 2：安装依赖

```bash
# 文件: pnpm-install.sh
# 功能: 安装依赖

# 安装生产依赖
pnpm add express

# 安装开发依赖
pnpm add -D typescript @types/node

# 安装全局包
pnpm add -g typescript

# 安装所有依赖
pnpm install
```

### 示例 3：管理脚本

运行脚本的方式与 npm 相同：

```bash
pnpm run build
pnpm run dev
pnpm start  # 可以省略 run
```

## 5. 参数说明：pnpm 命令参数

| 命令           | 说明                                     | 示例                           |
|:---------------|:-----------------------------------------|:-------------------------------|
| **add**        | 添加依赖（类似 npm install）              | `pnpm add express`             |
| **remove**     | 删除依赖                                 | `pnpm remove express`          |
| **update**     | 更新依赖                                 | `pnpm update`                  |
| **install**    | 安装所有依赖                             | `pnpm install`                 |
| **run**        | 运行脚本                                 | `pnpm run build`               |
| **list**       | 列出依赖                                 | `pnpm list`                    |

## 6. pnpm 的优势

### 1. 磁盘空间效率

pnpm 使用全局存储和硬链接，多个项目共享相同的包，节省磁盘空间：

```
~/.pnpm-store/  (全局存储)
  └── express@4.18.0/
      └── node_modules/

project1/node_modules/express -> ~/.pnpm-store/express@4.18.0/
project2/node_modules/express -> ~/.pnpm-store/express@4.18.0/
```

### 2. 严格依赖隔离

pnpm 使用符号链接实现严格的依赖隔离，避免依赖提升问题：

```
node_modules/
  ├── express/          # 直接依赖
  └── .pnpm/
      ├── express@4.18.0/
      │   └── node_modules/
      │       ├── express/
      │       └── body-parser/  # express 的依赖
      └── body-parser@1.20.0/
```

### 3. 性能优势

- **安装速度快**：并行安装，缓存机制
- **磁盘空间少**：全局存储，硬链接
- **Monorepo 支持**：优秀的 Monorepo 支持

## 7. 代码示例：pnpm 工作流

以下示例演示了 pnpm 的完整工作流：

```bash
# 文件: pnpm-workflow.sh
# 功能: pnpm 完整工作流

# 1. 初始化项目
pnpm init

# 2. 安装生产依赖
pnpm add express cors dotenv

# 3. 安装开发依赖
pnpm add -D typescript @types/node @types/express tsx

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
pnpm run dev

# 6. 构建项目
pnpm run build
```

## 8. 输出结果说明

pnpm 命令的输出结果：

```text
Packages: +50
++++++++++++++++++++++++++++++++++++++++++++++++++
Progress: resolved 50, reused 45, downloaded 5, added 50
```

**逻辑解析**：
- 显示安装的包数量
- 显示缓存复用情况
- 显示下载和添加的包数量

## 9. 使用场景

### 1. 大型项目

适合大型项目，节省磁盘空间：

```bash
# 大型项目使用 pnpm
pnpm install  # 快速安装，节省空间
```

### 2. Monorepo

优秀的 Monorepo 支持：

```bash
# Monorepo 项目
pnpm -r add express  # 为所有包添加依赖
pnpm -r run build    # 运行所有包的构建脚本
```

### 3. 多项目开发

多个项目共享全局存储：

```bash
# 项目 A
cd project-a
pnpm install

# 项目 B（共享存储）
cd project-b
pnpm install  # 从全局存储链接，不重复下载
```

## 10. 注意事项与常见错误

- **全局存储**：pnpm 使用全局存储，注意存储位置和清理
- **符号链接**：某些工具可能不支持符号链接
- **兼容性**：虽然兼容 npm，但某些边缘情况可能不同
- **迁移**：从 npm/yarn 迁移到 pnpm 需要删除 node_modules 和锁定文件

## 11. 常见问题 (FAQ)

**Q: pnpm 和 npm 可以混用吗？**
A: 不建议混用，应该统一使用一个包管理器。

**Q: 如何从 npm 迁移到 pnpm？**
A: 删除 node_modules 和 package-lock.json，然后运行 `pnpm install`。

**Q: pnpm 的全局存储在哪里？**
A: 默认在 `~/.pnpm-store`，可以通过 `pnpm store path` 查看。

## 12. 最佳实践

- **统一使用**：项目统一使用 pnpm，不要混用其他包管理器
- **清理存储**：定期清理全局存储，释放磁盘空间
- **Monorepo**：在 Monorepo 项目中优先使用 pnpm
- **CI/CD**：在 CI/CD 中配置 pnpm 缓存

## 13. 对比分析：pnpm vs npm

| 维度             | pnpm                                    | npm                                    |
|:-----------------|:----------------------------------------|:---------------------------------------|
| **安装速度**     | 快                                      | 中等                                   |
| **磁盘空间**     | 节省（全局存储）                        | 每个项目独立                            |
| **依赖隔离**     | 严格隔离                                | 扁平化结构                              |
| **Monorepo**     | 优秀支持                                | 基础支持                                |
| **兼容性**       | 兼容 npm                                | 原生支持                                |

## 14. 练习任务

1. **pnpm 基础实践**：
   - 安装和配置 pnpm
   - 使用 pnpm 初始化项目
   - 理解 pnpm 的存储机制

2. **依赖管理实践**：
   - 使用 pnpm 管理依赖
   - 理解严格依赖隔离
   - 查看全局存储

3. **Monorepo 实践**：
   - 使用 pnpm 创建 Monorepo
   - 管理 Monorepo 依赖
   - 运行 Monorepo 脚本

4. **实际应用**：
   - 在实际项目中应用 pnpm
   - 从 npm 迁移到 pnpm
   - 优化项目依赖管理

完成以上练习后，继续学习下一节：yarn（经典包管理器）。

## 总结

pnpm 是现代高性能包管理器：

- **核心优势**：高性能、磁盘空间效率、严格依赖隔离
- **适用场景**：大型项目、Monorepo、多项目开发
- **最佳实践**：统一使用、清理存储、Monorepo 支持

掌握 pnpm 有助于提高开发效率和节省资源。

---

**最后更新**：2025-01-XX
