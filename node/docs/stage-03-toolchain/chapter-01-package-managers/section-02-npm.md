# 3.1.2 npm 基础

## 1. 概述

npm（Node Package Manager）是 Node.js 自带的包管理器，也是 Node.js 生态系统中最广泛使用的包管理器。npm 提供了安装、更新、删除包的功能，以及管理项目脚本、配置项目信息等能力。理解 npm 的使用是 Node.js 开发的基础。

## 2. 特性说明

- **包安装**：从 npm 仓库安装包。
- **版本管理**：管理包的版本和版本范围。
- **脚本管理**：通过 package.json 管理项目脚本。
- **配置管理**：通过 .npmrc 配置文件管理 npm 行为。
- **仓库管理**：支持使用不同的包仓库源。

## 3. 语法与定义

### npm 基本命令

```bash
# 初始化项目
npm init [--yes]

# 安装包
npm install [package-name] [--save|--save-dev|--global]

# 删除包
npm uninstall [package-name]

# 更新包
npm update [package-name]

# 运行脚本
npm run [script-name]

# 查看包信息
npm list [--depth=n]

# 安全审计
npm audit [--fix]
```

## 4. 基本用法

### 示例 1：项目初始化

```bash
# 文件: npm-init.sh
# 功能: 初始化 npm 项目

# 交互式初始化
npm init

# 非交互式初始化（使用默认值）
npm init -y
```

生成的 package.json：

```json
{
  "name": "my-project",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

### 示例 2：安装依赖

```bash
# 文件: npm-install.sh
# 功能: 安装依赖

# 安装生产依赖
npm install express

# 安装开发依赖
npm install -D typescript @types/node

# 安装全局包
npm install -g typescript

# 安装所有依赖（根据 package.json）
npm install
```

### 示例 3：管理脚本

package.json 中的脚本配置：

```json
{
  "scripts": {
    "build": "tsc",
    "start": "node dist/index.js",
    "dev": "tsx watch src/index.ts",
    "test": "jest",
    "lint": "eslint src",
    "format": "prettier --write src"
  }
}
```

运行脚本：

```bash
npm run build
npm run start
npm run dev
```

## 5. 参数说明：npm 命令参数

### install 命令参数

| 参数名       | 说明                                     | 示例                           |
|:-------------|:-----------------------------------------|:-------------------------------|
| **--save**   | 保存到 dependencies（默认）               | `npm install express --save`   |
| **--save-dev**| 保存到 devDependencies（-D 简写）        | `npm install -D typescript`    |
| **--global** | 全局安装（-g 简写）                      | `npm install -g typescript`   |
| **--no-save**| 不保存到 package.json                    | `npm install --no-save`        |

### 其他常用参数

| 参数名       | 说明                                     | 示例                           |
|:-------------|:-----------------------------------------|:-------------------------------|
| **--yes**    | 非交互式，使用默认值（-y 简写）          | `npm init -y`                  |
| **--depth**  | 限制依赖树深度                           | `npm list --depth=0`           |
| **--fix**    | 自动修复问题                             | `npm audit --fix`              |

## 6. 返回值与状态说明

npm 命令的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **安装**     | 成功/失败    | 显示安装的包信息和依赖树                 |
| **删除**     | 成功/失败    | 显示删除的包信息                         |
| **更新**     | 成功/失败    | 显示更新的包信息                         |
| **运行脚本** | 脚本输出     | 显示脚本的执行结果                       |

## 7. 代码示例：完整的 npm 工作流

以下示例演示了完整的 npm 工作流：

```bash
# 文件: npm-workflow.sh
# 功能: 完整的 npm 工作流

# 1. 初始化项目
npm init -y

# 2. 安装生产依赖
npm install express cors dotenv

# 3. 安装开发依赖
npm install -D typescript @types/node @types/express tsx

# 4. 配置 package.json
cat > package.json << 'EOF'
{
  "name": "my-app",
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "tsx watch src/index.ts",
    "build": "tsc",
    "start": "node dist/index.js",
    "lint": "eslint src",
    "test": "jest"
  },
  "dependencies": {
    "express": "^4.18.0",
    "cors": "^2.8.5",
    "dotenv": "^16.3.0"
  },
  "devDependencies": {
    "typescript": "^5.3.0",
    "@types/node": "^20.10.0",
    "@types/express": "^4.17.21",
    "tsx": "^4.7.0"
  }
}
EOF

# 5. 运行开发服务器
npm run dev

# 6. 构建项目
npm run build

# 7. 运行生产版本
npm start
```

## 8. 输出结果说明

npm 命令的输出结果：

```text
added 50 packages, and audited 51 packages in 5s

found 0 vulnerabilities
```

**逻辑解析**：
- 显示安装的包数量
- 显示审计结果
- 显示安装时间
- 显示安全漏洞信息

## 9. 使用场景

### 1. 项目初始化

初始化新项目：

```bash
# 创建新项目
mkdir my-project
cd my-project
npm init -y

# 安装依赖
npm install express
npm install -D typescript
```

### 2. 依赖管理

管理项目依赖：

```bash
# 安装特定版本
npm install express@4.18.0

# 安装最新版本
npm install express@latest

# 更新所有依赖
npm update

# 删除依赖
npm uninstall express
```

### 3. 脚本管理

管理项目脚本：

```json
{
  "scripts": {
    "prebuild": "rimraf dist",
    "build": "tsc",
    "postbuild": "node scripts/copy-assets.js"
  }
}
```

## 10. 注意事项与常见错误

- **锁定文件**：package-lock.json 应该提交到版本控制
- **版本范围**：理解语义化版本和版本范围（^、~、*）
- **全局安装**：谨慎使用全局安装，优先使用项目本地安装
- **安全审计**：定期运行 `npm audit` 检查安全漏洞
- **磁盘空间**：node_modules 可能占用大量磁盘空间

## 11. 常见问题 (FAQ)

**Q: package-lock.json 需要提交吗？**
A: 是的，应该提交到版本控制，确保团队使用相同的依赖版本。

**Q: ^ 和 ~ 有什么区别？**
A: `^` 允许更新次要版本和补丁版本，`~` 只允许更新补丁版本。

**Q: 如何清理 node_modules？**
A: 删除 node_modules 和 package-lock.json，然后运行 `npm install`。

## 12. 最佳实践

- **使用锁定文件**：提交 package-lock.json 到版本控制
- **版本管理**：使用语义化版本，明确版本范围
- **安全审计**：定期运行 `npm audit` 检查安全漏洞
- **脚本管理**：使用 npm scripts 管理项目任务
- **配置管理**：使用 .npmrc 配置文件管理 npm 行为

## 13. 对比分析：npm vs 其他包管理器

| 维度             | npm                                    | pnpm                                    | yarn                                    |
|:-----------------|:---------------------------------------|:----------------------------------------|:----------------------------------------|
| **安装速度**     | 中等                                   | 快                                      | 中等                                    |
| **磁盘空间**     | 每个项目独立 node_modules              | 全局存储，节省空间                      | 每个项目独立 node_modules               |
| **依赖隔离**     | 扁平化结构                              | 严格隔离                                | 扁平化结构                              |
| **使用广泛度**   | 最广泛                                  | 增长中                                  | 广泛                                    |
| **默认支持**     | Node.js 自带                           | 需要安装                                | 需要安装                                |

## 14. 练习任务

1. **npm 基础实践**：
   - 初始化 npm 项目
   - 安装和删除依赖
   - 理解 package.json 结构

2. **依赖管理实践**：
   - 管理生产依赖和开发依赖
   - 理解版本范围和锁定文件
   - 运行安全审计

3. **脚本管理实践**：
   - 配置项目脚本
   - 使用 pre/post 钩子
   - 运行不同环境的脚本

4. **实际应用**：
   - 在实际项目中应用 npm
   - 管理项目依赖
   - 配置构建和部署脚本

完成以上练习后，继续学习下一节：pnpm（现代包管理器）。

## 总结

npm 是 Node.js 开发的基础工具：

- **核心功能**：包安装、版本管理、脚本管理
- **使用场景**：项目初始化、依赖管理、脚本执行
- **最佳实践**：使用锁定文件、版本管理、安全审计

掌握 npm 有助于高效管理 Node.js 项目。

---

**最后更新**：2025-01-XX
