# 1.2.2 代码编辑器与 IDE 配置

## 概述

代码编辑器是开发的基础工具。本节介绍主流代码编辑器的安装、配置和使用，包括 VS Code、WebStorm 等。

## VS Code

### VS Code 简介

Visual Studio Code（VS Code）是 Microsoft 开发的免费、开源的代码编辑器，支持多种编程语言。

### 安装

#### Windows

1. 访问 [VS Code 官网](https://code.visualstudio.com/)
2. 下载 Windows 安装包
3. 运行安装程序
4. 按照向导完成安装

#### macOS

1. 访问 VS Code 官网
2. 下载 macOS 安装包
3. 将 VS Code 拖拽到 Applications 文件夹

或使用 Homebrew：

```bash
brew install --cask visual-studio-code
```

#### Linux

**Ubuntu/Debian**：
```bash
# 使用 snap
sudo snap install --classic code

# 或下载 .deb 包安装
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt update
sudo apt install code
```

### 基本配置

#### 用户设置

打开设置：`Ctrl+,`（Windows/Linux）或 `Cmd+,`（macOS）

常用设置：

```json
{
  "editor.fontSize": 14,
  "editor.tabSize": 2,
  "editor.insertSpaces": true,
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
  },
  "files.autoSave": "afterDelay",
  "files.autoSaveDelay": 1000,
  "files.exclude": {
    "**/.git": true,
    "**/.DS_Store": true,
    "**/node_modules": true
  }
}
```

#### 工作区设置

创建 `.vscode/settings.json`：

```json
{
  "editor.tabSize": 2,
  "editor.formatOnSave": true,
  "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[typescript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  }
}
```

### 推荐扩展

#### JavaScript/TypeScript 开发

- **ESLint**：代码检查
- **Prettier**：代码格式化
- **TypeScript Vue Plugin**：Vue TypeScript 支持
- **JavaScript (ES6) code snippets**：代码片段

#### 通用工具

- **GitLens**：Git 增强
- **Path Intellisense**：路径自动补全
- **Auto Rename Tag**：自动重命名标签
- **Bracket Pair Colorizer**：括号配对着色
- **indent-rainbow**：缩进彩虹

#### 主题和图标

- **One Dark Pro**：主题
- **Material Icon Theme**：图标主题

### 调试配置

#### 浏览器调试

创建 `.vscode/launch.json`：

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "chrome",
      "request": "launch",
      "name": "Launch Chrome",
      "url": "http://localhost:3000",
      "webRoot": "${workspaceFolder}"
    }
  ]
}
```

#### Node.js 调试

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "Launch Node.js",
      "program": "${workspaceFolder}/index.js",
      "console": "integratedTerminal"
    }
  ]
}
```

## WebStorm

### WebStorm 简介

WebStorm 是 JetBrains 开发的 JavaScript IDE，提供完整的开发功能。

### 安装

1. 访问 [WebStorm 官网](https://www.jetbrains.com/webstorm/)
2. 下载安装包
3. 运行安装程序
4. 激活许可证（试用或购买）

### 基本配置

#### 编辑器设置

1. 打开设置：`File` → `Settings`（Windows/Linux）或 `WebStorm` → `Preferences`（macOS）
2. 配置编辑器：
   - 字体大小
   - 代码风格
   - 自动保存
   - 代码格式化

#### 代码风格

1. 打开 `Settings` → `Editor` → `Code Style`
2. 选择 JavaScript 或 TypeScript
3. 配置缩进、换行等规则

### 功能特性

#### 智能代码补全

WebStorm 提供强大的代码补全功能：

- 上下文感知补全
- 导入建议
- 参数提示

#### 重构工具

- 重命名
- 提取方法
- 提取变量
- 移动文件

#### 调试支持

- 断点调试
- 变量检查
- 调用栈查看
- 条件断点

## 编辑器配置文件

### .editorconfig

`.editorconfig` 是跨编辑器的配置文件：

```ini
# EditorConfig 配置文件
root = true

[*]
charset = utf-8
end_of_line = lf
indent_style = space
indent_size = 2
insert_final_newline = true
trim_trailing_whitespace = true

[*.md]
trim_trailing_whitespace = false
```

### .vscode/extensions.json

推荐扩展列表：

```json
{
  "recommendations": [
    "dbaeumer.vscode-eslint",
    "esbenp.prettier-vscode",
    "ms-vscode.vscode-typescript-next"
  ]
}
```

### .vscode/settings.json

工作区设置：

```json
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
  },
  "files.exclude": {
    "**/.git": true,
    "**/node_modules": true,
    "**/dist": true
  }
}
```

## 键盘快捷键

### VS Code 常用快捷键

#### 编辑

- `Ctrl/Cmd + D`：选择下一个相同文本
- `Alt + Up/Down`：移动行
- `Shift + Alt + Up/Down`：复制行
- `Ctrl/Cmd + /`：切换注释
- `Ctrl/Cmd + Shift + K`：删除行

#### 导航

- `Ctrl/Cmd + P`：快速打开文件
- `Ctrl/Cmd + Shift + P`：命令面板
- `Ctrl/Cmd + B`：切换侧边栏
- `Ctrl/Cmd + J`：切换面板

#### 搜索

- `Ctrl/Cmd + F`：查找
- `Ctrl/Cmd + H`：替换
- `Ctrl/Cmd + Shift + F`：全局搜索

### WebStorm 常用快捷键

#### 编辑

- `Ctrl/Cmd + D`：复制行
- `Ctrl/Cmd + Y`：删除行
- `Ctrl/Cmd + /`：切换注释
- `Alt + Enter`：快速修复

#### 导航

- `Ctrl/Cmd + N`：查找类
- `Ctrl/Cmd + Shift + N`：查找文件
- `Ctrl/Cmd + E`：最近文件
- `Alt + F1`：定位文件

## 调试配置

### VS Code 调试

#### 浏览器调试

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "chrome",
      "request": "launch",
      "name": "Launch Chrome",
      "url": "http://localhost:3000",
      "webRoot": "${workspaceFolder}/src",
      "sourceMaps": true
    }
  ]
}
```

#### Node.js 调试

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "Launch Node.js",
      "program": "${workspaceFolder}/index.js",
      "console": "integratedTerminal",
      "skipFiles": ["<node_internals>/**"]
    }
  ]
}
```

### WebStorm 调试

1. 设置断点
2. 右键点击文件 → `Debug 'filename'`
3. 使用调试工具栏控制执行

## 练习

1. **编辑器配置**：创建 `.editorconfig` 文件，统一编辑器配置。

2. **VS Code 设置**：配置 VS Code 的工作区设置，包括格式化、代码检查等。

3. **扩展安装**：安装常用的 VS Code 扩展（ESLint、Prettier、TypeScript 等）。

4. **调试配置**：创建 VS Code 的调试配置文件，配置浏览器和 Node.js 调试。

5. **快捷键练习**：练习常用的编辑器快捷键，提高编辑效率。

完成以上练习后，继续学习下一节，了解包管理器。

## 总结

代码编辑器是开发的基础工具。VS Code 和 WebStorm 都是优秀的编辑器，选择哪个取决于个人偏好和项目需求。正确配置编辑器能够显著提高开发效率。

## 相关资源

- [VS Code 官方文档](https://code.visualstudio.com/docs)
- [WebStorm 官方文档](https://www.jetbrains.com/help/webstorm/)
- [VS Code 扩展市场](https://marketplace.visualstudio.com/)
- [EditorConfig 官网](https://editorconfig.org/)
