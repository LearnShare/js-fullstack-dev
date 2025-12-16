# 1.2.3 包管理器（npm、pnpm、yarn）

## 概述

包管理器用于管理项目的依赖关系。本节介绍主流包管理器的安装、使用和对比，包括 npm、pnpm 和 yarn。

## npm

### npm 简介

npm（Node Package Manager）是 Node.js 的默认包管理器，也是世界上最大的软件注册表。

### 基本命令

#### 初始化项目

```bash
# 初始化 package.json
npm init

# 使用默认值快速初始化
npm init -y
```

#### 安装包

```bash
# 安装到 dependencies
npm install package-name
# 或简写
npm i package-name

# 安装到 devDependencies
npm install --save-dev package-name
# 或简写
npm i -D package-name

# 全局安装
npm install -g package-name
# 或简写
npm i -g package-name

# 安装特定版本
npm install package-name@1.2.3

# 安装最新版本
npm install package-name@latest
```

#### 卸载包

```bash
# 卸载包
npm uninstall package-name
# 或简写
npm un package-name

# 卸载全局包
npm uninstall -g package-name
```

#### 更新包

```bash
# 更新所有包
npm update

# 更新特定包
npm update package-name

# 检查过时的包
npm outdated
```

#### 查看包信息

```bash
# 查看已安装的包
npm list

# 查看全局包
npm list -g

# 查看包信息
npm info package-name

# 查看包版本
npm view package-name version
```

### package.json

package.json 是 Node.js 项目的配置文件。

#### 主要字段

```json
{
  "name": "my-project",
  "version": "1.0.0",
  "description": "项目描述",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "test": "jest",
    "dev": "node --watch index.js"
  },
  "dependencies": {
    "express": "^4.18.2"
  },
  "devDependencies": {
    "jest": "^29.5.0"
  },
  "engines": {
    "node": ">=18.0.0",
    "npm": ">=9.0.0"
  }
}
```

#### scripts 字段

scripts 字段定义了可执行的脚本命令。

```json
{
  "scripts": {
    "start": "node index.js",
    "dev": "node --watch index.js",
    "test": "jest",
    "build": "webpack --mode production",
    "lint": "eslint ."
  }
}
```

运行脚本：

```bash
npm run start
npm run dev
npm run test
```

### 版本管理

#### 语义化版本

npm 使用语义化版本（Semantic Versioning）：

- **主版本号**：不兼容的 API 修改
- **次版本号**：向下兼容的功能性新增
- **修订号**：向下兼容的问题修正

#### 版本范围

```json
{
  "dependencies": {
    "package": "^1.2.3",  // 兼容版本：>=1.2.3 <2.0.0
    "package": "~1.2.3",  // 近似版本：>=1.2.3 <1.3.0
    "package": "1.2.3",    // 精确版本
    "package": "*",        // 任意版本
    "package": ">=1.2.3"  // 大于等于
  }
}
```

### npm 配置

#### 查看配置

```bash
# 查看所有配置
npm config list

# 查看特定配置
npm config get registry
```

#### 设置配置

```bash
# 设置注册表
npm config set registry https://registry.npmjs.org/

# 设置全局安装目录
npm config set prefix ~/.npm-global
```

## pnpm

### pnpm 简介

pnpm 是一个快速、节省磁盘空间的包管理器，使用硬链接和符号链接来管理依赖。

### 安装

```bash
# 使用 npm 安装
npm install -g pnpm

# 使用独立安装脚本
curl -fsSL https://get.pnpm.io/install.sh | sh -
```

### 基本命令

#### 初始化项目

```bash
# 初始化 package.json
pnpm init
```

#### 安装包

```bash
# 安装到 dependencies
pnpm add package-name

# 安装到 devDependencies
pnpm add -D package-name

# 全局安装
pnpm add -g package-name

# 安装所有依赖
pnpm install
# 或简写
pnpm i
```

#### 卸载包

```bash
# 卸载包
pnpm remove package-name
# 或简写
pnpm rm package-name
```

#### 更新包

```bash
# 更新所有包
pnpm update

# 更新特定包
pnpm update package-name
```

### pnpm 的优势

#### 1. 节省磁盘空间

pnpm 使用硬链接和符号链接，避免重复存储相同的包。

#### 2. 更快的安装速度

pnpm 的安装速度通常比 npm 和 yarn 更快。

#### 3. 严格的依赖管理

pnpm 使用符号链接，确保只能访问 package.json 中声明的依赖。

#### 4. Monorepo 支持

pnpm 对 monorepo 有很好的支持。

### pnpm 工作空间

创建 `pnpm-workspace.yaml`：

```yaml
packages:
  - 'packages/*'
  - 'apps/*'
```

## yarn

### yarn 简介

yarn 是 Facebook 开发的包管理器，提供了更好的性能和可靠性。

### 安装

```bash
# 使用 npm 安装
npm install -g yarn

# 使用独立安装脚本
curl -o- -L https://yarnpkg.com/install.sh | bash -
```

### 基本命令

#### 初始化项目

```bash
# 初始化 package.json
yarn init
```

#### 安装包

```bash
# 安装到 dependencies
yarn add package-name

# 安装到 devDependencies
yarn add -D package-name

# 全局安装
yarn global add package-name

# 安装所有依赖
yarn install
# 或简写
yarn
```

#### 卸载包

```bash
# 卸载包
yarn remove package-name
```

#### 更新包

```bash
# 更新所有包
yarn upgrade

# 更新特定包
yarn upgrade package-name
```

### yarn 的优势

#### 1. 并行安装

yarn 并行安装包，提高安装速度。

#### 2. 离线缓存

yarn 使用离线缓存，即使网络断开也能安装包。

#### 3. 锁定文件

yarn 使用 `yarn.lock` 锁定依赖版本，确保一致性。

#### 4. Workspaces

yarn 支持 workspaces，便于管理 monorepo。

### yarn workspaces

在 `package.json` 中配置：

```json
{
  "private": true,
  "workspaces": [
    "packages/*",
    "apps/*"
  ]
}
```

## 包管理器对比

### 性能对比

| 特性 | npm | pnpm | yarn |
|------|-----|------|------|
| **安装速度** | 中等 | 快 | 快 |
| **磁盘占用** | 高 | 低 | 中等 |
| **并行安装** | 否 | 是 | 是 |
| **离线缓存** | 是 | 是 | 是 |

### 功能对比

| 特性 | npm | pnpm | yarn |
|------|-----|------|------|
| **Monorepo 支持** | 基础 | 优秀 | 优秀 |
| **Workspaces** | 是 | 是 | 是 |
| **锁定文件** | package-lock.json | pnpm-lock.yaml | yarn.lock |
| **全局安装** | 是 | 是 | 是 |

### 选择建议

#### 选择 npm

- Node.js 默认包管理器
- 简单项目
- 团队已有 npm 经验

#### 选择 pnpm

- 需要节省磁盘空间
- 需要更快的安装速度
- Monorepo 项目
- 需要严格的依赖管理

#### 选择 yarn

- 需要更好的性能
- 需要 Workspaces
- 团队已有 yarn 经验

## 最佳实践

### 1. 使用锁定文件

始终提交锁定文件到版本控制：

- `package-lock.json`（npm）
- `pnpm-lock.yaml`（pnpm）
- `yarn.lock`（yarn）

### 2. 版本管理

使用语义化版本，合理使用版本范围：

```json
{
  "dependencies": {
    "package": "^1.2.3"  // 推荐：允许补丁和次版本更新
  }
}
```

### 3. 依赖分类

区分 dependencies 和 devDependencies：

```json
{
  "dependencies": {
    "express": "^4.18.2"  // 生产依赖
  },
  "devDependencies": {
    "jest": "^29.5.0"     // 开发依赖
  }
}
```

### 4. 定期更新

定期检查和更新依赖：

```bash
# npm
npm outdated
npm update

# pnpm
pnpm outdated
pnpm update

# yarn
yarn outdated
yarn upgrade
```

### 5. 安全审计

定期进行安全审计：

```bash
# npm
npm audit
npm audit fix

# pnpm
pnpm audit
pnpm audit --fix

# yarn
yarn audit
yarn audit --fix
```

## 练习

1. **项目初始化**：使用 npm/pnpm/yarn 初始化一个新项目，创建 `package.json`。

2. **依赖安装**：安装开发依赖和生产依赖，理解 `dependencies` 和 `devDependencies` 的区别。

3. **版本管理**：使用语义化版本管理依赖，理解 `^`、`~` 等版本范围符号。

4. **锁定文件**：理解锁定文件的作用，提交锁定文件到版本控制。

5. **安全审计**：运行安全审计命令，检查依赖中的安全漏洞。

完成以上练习后，继续学习下一节，了解构建工具。

## 总结

包管理器是现代 JavaScript 开发的基础工具。npm、pnpm 和 yarn 都是优秀的包管理器，选择哪个取决于项目需求和团队经验。理解包管理器的基本操作和最佳实践，有助于高效管理项目依赖。

## 相关资源

- [npm 官方文档](https://docs.npmjs.com/)
- [pnpm 官方文档](https://pnpm.io/)
- [yarn 官方文档](https://yarnpkg.com/)
- [语义化版本规范](https://semver.org/)
