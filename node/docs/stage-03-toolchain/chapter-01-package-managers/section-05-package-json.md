# 3.1.5 package.json 详解

## 1. 概述

package.json 是 Node.js 项目的核心配置文件，定义了项目的元数据、依赖、脚本、配置等信息。理解 package.json 的配置对于管理 Node.js 项目至关重要。本章详细介绍 package.json 的各个字段和配置选项。

## 2. 特性说明

- **项目元数据**：定义项目名称、版本、描述等信息。
- **依赖管理**：定义项目依赖和开发依赖。
- **脚本管理**：定义项目脚本命令。
- **配置选项**：定义项目配置（如模块类型、入口文件等）。
- **发布信息**：定义包的发布相关信息。

## 3. package.json 结构

### 基本结构

```json
{
  "name": "my-project",
  "version": "1.0.0",
  "description": "项目描述",
  "main": "index.js",
  "type": "module",
  "scripts": {
    "start": "node index.js"
  },
  "dependencies": {},
  "devDependencies": {},
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

## 4. 基本字段说明

### 示例 1：基本配置

```json
// 文件: package.json
// 功能: package.json 基本配置

{
  "name": "my-app",
  "version": "1.0.0",
  "description": "My Node.js application",
  "main": "dist/index.js",
  "type": "module",
  "scripts": {
    "dev": "tsx watch src/index.ts",
    "build": "tsc",
    "start": "node dist/index.js",
    "test": "jest",
    "lint": "eslint src",
    "format": "prettier --write src"
  },
  "keywords": ["nodejs", "typescript"],
  "author": "Your Name",
  "license": "MIT"
}
```

### 示例 2：依赖配置

```json
// 文件: package.json
// 功能: 依赖配置

{
  "dependencies": {
    "express": "^4.18.0",
    "cors": "^2.8.5",
    "dotenv": "^16.3.0"
  },
  "devDependencies": {
    "typescript": "^5.3.0",
    "@types/node": "^20.10.0",
    "@types/express": "^4.17.21",
    "tsx": "^4.7.0",
    "eslint": "^8.55.0",
    "prettier": "^3.1.0"
  },
  "peerDependencies": {
    "react": "^18.0.0"
  },
  "optionalDependencies": {
    "fsevents": "^2.3.2"
  }
}
```

### 示例 3：脚本配置

```json
// 文件: package.json
// 功能: 脚本配置

{
  "scripts": {
    "prebuild": "rimraf dist",
    "build": "tsc",
    "postbuild": "node scripts/copy-assets.js",
    "prestart": "npm run build",
    "start": "node dist/index.js",
    "dev": "tsx watch src/index.ts",
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage",
    "lint": "eslint src",
    "lint:fix": "eslint src --fix",
    "format": "prettier --write src",
    "format:check": "prettier --check src"
  }
}
```

## 5. 参数说明：package.json 字段

### 基本字段

| 字段名       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **name**     | String   | 包名称（必须）                           | `"my-app"`                     |
| **version**  | String   | 版本号（必须，语义化版本）               | `"1.0.0"`                      |
| **description**| String | 项目描述                                 | `"My Node.js app"`             |
| **main**     | String   | 入口文件                                 | `"dist/index.js"`              |
| **type**     | String   | 模块类型（"module" 或 "commonjs"）       | `"module"`                     |

### 依赖字段

| 字段名       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **dependencies**| Object | 生产依赖                                 | `{ "express": "^4.18.0" }`    |
| **devDependencies**| Object | 开发依赖                             | `{ "typescript": "^5.3.0" }`   |
| **peerDependencies**| Object | 对等依赖                           | `{ "react": "^18.0.0" }`       |
| **optionalDependencies**| Object | 可选依赖                         | `{ "fsevents": "^2.3.2" }`     |

## 6. 返回值与状态说明

package.json 的配置影响：

| 配置项       | 影响                                     |
|:-------------|:-----------------------------------------|
| **name**     | 包的唯一标识                             |
| **version**  | 包的版本号                               |
| **main**     | 包的入口文件                             |
| **type**     | 模块系统类型（ESM 或 CommonJS）          |
| **scripts**  | 可执行的脚本命令                         |

## 7. 代码示例：完整的 package.json

以下示例演示了完整的 package.json 配置：

```json
// 文件: package.json
// 功能: 完整的 package.json 配置

{
  "name": "my-app",
  "version": "1.0.0",
  "description": "A Node.js application built with TypeScript",
  "main": "dist/index.js",
  "type": "module",
  "exports": {
    ".": {
      "import": "./dist/index.js",
      "require": "./dist/index.cjs"
    }
  },
  "files": [
    "dist",
    "README.md"
  ],
  "scripts": {
    "dev": "tsx watch src/index.ts",
    "build": "tsc",
    "start": "node dist/index.js",
    "test": "jest",
    "lint": "eslint src",
    "format": "prettier --write src"
  },
  "keywords": [
    "nodejs",
    "typescript",
    "express"
  ],
  "author": "Your Name <your.email@example.com>",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/username/my-app.git"
  },
  "bugs": {
    "url": "https://github.com/username/my-app/issues"
  },
  "homepage": "https://github.com/username/my-app#readme",
  "engines": {
    "node": ">=18.0.0",
    "npm": ">=9.0.0"
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
    "tsx": "^4.7.0",
    "eslint": "^8.55.0",
    "prettier": "^3.1.0",
    "jest": "^29.7.0"
  }
}
```

## 8. 输出结果说明

package.json 配置的影响：

- **name 和 version**：用于包的唯一标识
- **main 和 exports**：定义包的入口点
- **type**：决定模块系统类型
- **scripts**：定义可执行的命令
- **dependencies**：定义运行时依赖

## 9. 使用场景

### 1. 项目配置

配置项目基本信息：

```json
{
  "name": "my-project",
  "version": "1.0.0",
  "description": "项目描述",
  "author": "Your Name",
  "license": "MIT"
}
```

### 2. 依赖管理

管理项目依赖：

```json
{
  "dependencies": {
    "express": "^4.18.0"
  },
  "devDependencies": {
    "typescript": "^5.3.0"
  }
}
```

### 3. 脚本管理

管理项目脚本：

```json
{
  "scripts": {
    "build": "tsc",
    "start": "node dist/index.js"
  }
}
```

## 10. 注意事项与常见错误

- **name 规范**：包名称必须符合 npm 命名规范
- **version 格式**：版本号必须符合语义化版本规范
- **type 字段**：设置 "module" 后，所有 .js 文件都是 ESM
- **exports 字段**：现代包的入口点配置，优先于 main
- **engines 字段**：指定 Node.js 和 npm 版本要求

## 11. 常见问题 (FAQ)

**Q: name 字段有什么要求？**
A: 必须是小写字母、数字、连字符或下划线，不能以点或下划线开头。

**Q: type: "module" 和 type: "commonjs" 有什么区别？**
A: "module" 使用 ES Modules，"commonjs" 使用 CommonJS。不设置时默认为 CommonJS。

**Q: exports 字段和 main 字段有什么区别？**
A: exports 是现代标准，支持条件导出；main 是传统字段。exports 优先于 main。

## 12. 最佳实践

- **语义化版本**：使用语义化版本规范
- **明确依赖**：明确区分 dependencies 和 devDependencies
- **脚本组织**：合理组织脚本，使用 pre/post 钩子
- **engines 字段**：指定 Node.js 和 npm 版本要求
- **exports 字段**：使用 exports 字段定义包的入口点

## 13. 对比分析：不同配置方式

| 配置方式     | 说明                                     | 适用场景                       |
|:-------------|:-----------------------------------------|:-------------------------------|
| **main**     | 传统入口点                               | 简单包，向后兼容               |
| **exports**  | 现代入口点，支持条件导出                 | 现代包，需要条件导出           |
| **type: "module"**| 使用 ES Modules                      | 现代项目，使用 ESM             |
| **type: "commonjs"**| 使用 CommonJS（默认）            | 传统项目，向后兼容             |

## 14. 练习任务

1. **package.json 实践**：
   - 创建和配置 package.json
   - 理解各个字段的作用
   - 配置项目元数据

2. **依赖管理实践**：
   - 配置 dependencies 和 devDependencies
   - 理解版本范围（^、~、*）
   - 配置 peerDependencies

3. **脚本管理实践**：
   - 配置项目脚本
   - 使用 pre/post 钩子
   - 组织不同环境的脚本

4. **实际应用**：
   - 在实际项目中配置 package.json
   - 管理项目依赖和脚本
   - 发布包到 npm

完成以上练习后，继续学习下一章：构建工具。

## 总结

package.json 是 Node.js 项目的核心配置文件：

- **核心功能**：项目元数据、依赖管理、脚本管理
- **重要字段**：name、version、main、type、scripts、dependencies
- **最佳实践**：语义化版本、明确依赖、脚本组织

掌握 package.json 有助于高效管理 Node.js 项目。

---

**最后更新**：2025-01-XX
