# 1.1.4 IDE 配置（VSCode、WebStorm）

## 概述

配置 IDE 可以显著提升 TypeScript 开发体验。本节介绍主流 IDE（VSCode、WebStorm）的 TypeScript 配置。

## Visual Studio Code

### 安装 TypeScript 支持

VSCode 内置 TypeScript 支持，无需额外安装。

### 基本配置

#### 用户设置

打开设置：`Ctrl+,`（Windows/Linux）或 `Cmd+,`（macOS）

常用设置（settings.json）：

```json
{
  "typescript.tsdk": "node_modules/typescript/lib",
  "typescript.enablePromptUseWorkspaceTsdk": true,
  "typescript.preferences.importModuleSpecifier": "relative",
  "typescript.updateImportsOnFileMove.enabled": "always",
  "typescript.suggest.autoImports": true,
  "typescript.inlayHints.parameterNames.enabled": "all",
  "typescript.inlayHints.variableTypes.enabled": true,
  "typescript.inlayHints.functionLikeReturnTypes.enabled": true
}
```

#### 工作区设置

创建 `.vscode/settings.json`：

```json
{
  "typescript.tsdk": "./node_modules/typescript/lib",
  "typescript.enablePromptUseWorkspaceTsdk": true
}
```

### 推荐扩展

#### TypeScript 和 JavaScript 语言功能

- **内置扩展**：TypeScript 和 JavaScript 语言功能（内置）
- 提供代码补全、错误检查、重构等功能

#### ESLint

```json
{
  "eslint.validate": [
    "javascript",
    "javascriptreact",
    "typescript",
    "typescriptreact"
  ]
}
```

#### Prettier

```json
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "[typescript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  }
}
```

### 调试配置

创建 `.vscode/launch.json`：

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "Debug TypeScript",
      "program": "${workspaceFolder}/src/index.ts",
      "outFiles": ["${workspaceFolder}/dist/**/*.js"],
      "preLaunchTask": "build",
      "sourceMaps": true
    }
  ]
}
```

创建 `.vscode/tasks.json`：

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "build",
      "type": "shell",
      "command": "tsc",
      "problemMatcher": ["$tsc"]
    }
  ]
}
```

## WebStorm

### 安装 TypeScript 支持

WebStorm 内置 TypeScript 支持，无需额外安装。

### 基本配置

#### 设置 TypeScript 版本

1. 打开设置：`File` → `Settings`（Windows/Linux）或 `WebStorm` → `Preferences`（macOS）
2. 导航到：`Languages & Frameworks` → `TypeScript`
3. 选择 TypeScript 版本：
   - **Bundled**：使用 WebStorm 内置版本
   - **Use TypeScript service from node_modules**：使用项目中的版本（推荐）

#### TypeScript 编译器选项

在 `Languages & Frameworks` → `TypeScript` → `Compiler` 中配置：

- **Recompile on changes**：文件变更时自动重新编译
- **Use tsconfig.json**：使用项目的 tsconfig.json
- **Track changes**：跟踪文件变化

### 代码风格

#### 格式化

1. 打开设置：`Editor` → `Code Style` → `TypeScript`
2. 配置缩进、空格、换行等选项

#### 导入优化

1. 打开设置：`Editor` → `Code Style` → `TypeScript` → `Imports`
2. 配置导入语句的排序和组织

### 代码补全

WebStorm 提供强大的代码补全功能：

- 自动补全
- 参数提示
- 类型信息提示
- 快速文档

### 重构支持

WebStorm 支持多种重构操作：

- 重命名
- 提取函数/变量
- 内联
- 移动
- 安全删除

### 调试配置

1. 创建运行配置：`Run` → `Edit Configurations`
2. 添加 Node.js 配置
3. 配置：
   - **Node interpreter**：Node.js 解释器路径
   - **Working directory**：工作目录
   - **JavaScript file**：编译后的 JavaScript 文件
   - **Application parameters**：应用参数

## 通用配置建议

### TypeScript 版本

**建议**：使用项目中的 TypeScript 版本

- VSCode：设置 `typescript.tsdk` 指向 `node_modules/typescript/lib`
- WebStorm：选择 "Use TypeScript service from node_modules"

**原因**：
- 确保 IDE 使用与项目相同的 TypeScript 版本
- 避免版本不一致导致的问题

### 代码格式化

**建议**：统一使用 Prettier 或编辑器内置格式化

- 配置格式化规则
- 启用保存时自动格式化
- 团队成员使用相同的格式化配置

### 代码检查

**建议**：使用 ESLint 进行代码检查

- 配置 TypeScript ESLint 规则
- 启用自动修复
- 在保存时自动修复

### 导入管理

**建议**：配置导入语句的组织和排序

- 自动排序导入
- 移除未使用的导入
- 使用绝对路径或相对路径（团队统一）

## 常见问题

### 问题 1：类型错误未显示

**解决方案**：
- 检查 TypeScript 版本是否正确
- 重新加载窗口/重启 IDE
- 检查 tsconfig.json 配置

### 问题 2：代码补全不工作

**解决方案**：
- 检查 TypeScript 服务是否运行
- 检查文件是否在 tsconfig.json 的 include 范围内
- 重新启动 TypeScript 服务

### 问题 3：导入路径不正确

**解决方案**：
- 检查 `baseUrl` 和 `paths` 配置
- 配置 IDE 的路径映射
- 使用相对路径作为备选

## 注意事项

1. **版本一致性**：确保 IDE 使用的 TypeScript 版本与项目一致
2. **配置文件**：使用工作区配置文件，确保团队配置一致
3. **扩展管理**：谨慎安装扩展，避免冲突
4. **性能优化**：大型项目可能需要调整 IDE 设置以提升性能

## 最佳实践

1. **使用工作区配置**：在项目中配置 IDE 设置，确保团队一致
2. **版本管理**：使用项目中的 TypeScript 版本
3. **代码格式化**：统一使用 Prettier 格式化代码
4. **代码检查**：使用 ESLint 进行代码检查
5. **调试配置**：配置调试环境，提升开发效率

## 练习

1. **VSCode 配置**：配置 VSCode 的 TypeScript 设置，使用项目中的 TypeScript 版本。

2. **WebStorm 配置**：配置 WebStorm 的 TypeScript 设置，使用项目中的 TypeScript 版本。

3. **代码格式化**：配置 Prettier，启用保存时自动格式化。

4. **代码检查**：配置 ESLint，启用 TypeScript 代码检查。

5. **调试配置**：配置调试环境，能够调试 TypeScript 代码。

完成以上练习后，继续学习下一节，了解 TypeScript 直接执行工具。

## 总结

配置 IDE 可以显著提升 TypeScript 开发体验。VSCode 和 WebStorm 都提供了强大的 TypeScript 支持。建议使用项目中的 TypeScript 版本，配置代码格式化和检查工具，提升开发效率和代码质量。

## 相关资源

- [VSCode TypeScript 文档](https://code.visualstudio.com/docs/languages/typescript)
- [WebStorm TypeScript 文档](https://www.jetbrains.com/help/webstorm/typescript-support.html)
