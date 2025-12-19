# 3.5.4 VS Code 调试配置

## 1. 概述

VS Code 提供了强大的调试功能，可以直接在编辑器中调试 Node.js 应用。VS Code 调试配置简单，功能完整，是日常开发中最常用的调试方式。理解 VS Code 调试配置对于提高开发效率非常重要。

## 2. 特性说明

- **编辑器集成**：直接在编辑器中调试，无需切换工具。
- **配置简单**：通过配置文件即可设置调试。
- **功能完整**：支持断点、变量检查、步进执行等。
- **多配置支持**：支持多个调试配置。
- **条件断点**：支持条件断点和日志断点。

## 3. 配置方式

### 创建调试配置

在 VS Code 中按 `F5` 或点击调试按钮，选择 "Node.js"，会自动创建 `.vscode/launch.json`：

```json
// 文件: .vscode/launch.json
// 功能: VS Code 调试配置

{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "Launch Program",
      "skipFiles": ["<node_internals>/**"],
      "program": "${workspaceFolder}/src/index.ts",
      "outFiles": ["${workspaceFolder}/dist/**/*.js"],
      "runtimeArgs": ["--loader", "tsx/esm"]
    }
  ]
}
```

## 4. 基本用法

### 示例 1：基本调试配置

```json
// 文件: .vscode/launch.json
// 功能: VS Code 基本调试配置

{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "Debug TypeScript",
      "program": "${workspaceFolder}/src/index.ts",
      "runtimeExecutable": "node",
      "runtimeArgs": ["--loader", "tsx/esm"],
      "skipFiles": ["<node_internals>/**"],
      "console": "integratedTerminal"
    }
  ]
}
```

### 示例 2：多配置

```json
// 文件: .vscode/launch.json
// 功能: VS Code 多调试配置

{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug Current File",
      "type": "node",
      "request": "launch",
      "program": "${file}",
      "runtimeArgs": ["--loader", "tsx/esm"]
    },
    {
      "name": "Debug Server",
      "type": "node",
      "request": "launch",
      "program": "${workspaceFolder}/src/server.ts",
      "runtimeArgs": ["--loader", "tsx/esm"],
      "env": {
        "NODE_ENV": "development"
      }
    },
    {
      "name": "Attach to Process",
      "type": "node",
      "request": "attach",
      "port": 9229
    }
  ]
}
```

### 示例 3：条件断点

在 VS Code 中设置条件断点：

1. 设置断点
2. 右键断点，选择 "Edit Breakpoint"
3. 设置条件或日志表达式

## 5. 参数说明：VS Code 调试配置

### 基本配置

| 配置项           | 类型     | 说明                                     | 示例                           |
|:-----------------|:---------|:-----------------------------------------|:-------------------------------|
| **type**         | String   | 调试器类型                               | `"node"`                       |
| **request**      | String   | 请求类型（launch/attach）                | `"launch"`                     |
| **name**         | String   | 配置名称                                 | `"Debug TypeScript"`            |
| **program**      | String   | 程序入口文件                             | `"${workspaceFolder}/src/index.ts"`|
| **runtimeArgs**  | Array    | 运行时参数                               | `["--loader", "tsx/esm"]`      |
| **env**          | Object   | 环境变量                                 | `{ "NODE_ENV": "development" }`|

## 6. 返回值与状态说明

VS Code 调试的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **启动调试** | 调试会话     | 启动调试会话，显示调试面板               |
| **断点命中** | 暂停执行     | 代码执行到断点处暂停，显示变量和调用栈   |

## 7. 代码示例：完整的 VS Code 调试配置

以下示例演示了完整的 VS Code 调试配置：

```json
// 文件: .vscode/launch.json
// 功能: 完整的 VS Code 调试配置

{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug TypeScript",
      "type": "node",
      "request": "launch",
      "program": "${workspaceFolder}/src/index.ts",
      "runtimeExecutable": "node",
      "runtimeArgs": ["--loader", "tsx/esm"],
      "skipFiles": ["<node_internals>/**"],
      "console": "integratedTerminal",
      "internalConsoleOptions": "neverOpen",
      "env": {
        "NODE_ENV": "development"
      },
      "sourceMaps": true,
      "outFiles": ["${workspaceFolder}/dist/**/*.js"]
    },
    {
      "name": "Debug Current File",
      "type": "node",
      "request": "launch",
      "program": "${file}",
      "runtimeArgs": ["--loader", "tsx/esm"],
      "skipFiles": ["<node_internals>/**"]
    },
    {
      "name": "Attach to Process",
      "type": "node",
      "request": "attach",
      "port": 9229,
      "restart": true,
      "localRoot": "${workspaceFolder}",
      "remoteRoot": "${workspaceFolder}"
    }
  ]
}
```

## 8. 输出结果说明

VS Code 调试的输出结果：

在 VS Code 调试面板中可以看到：
- **Variables**：变量值
- **Watch**：监视的表达式
- **Call Stack**：调用栈
- **Breakpoints**：断点列表
- **Debug Console**：调试控制台

## 9. 使用场景

### 1. 日常开发

日常开发中最常用的调试方式：

```json
{
  "name": "Debug Current File",
  "type": "node",
  "request": "launch",
  "program": "${file}",
  "runtimeArgs": ["--loader", "tsx/esm"]
}
```

### 2. 服务器调试

调试服务器应用：

```json
{
  "name": "Debug Server",
  "type": "node",
  "request": "launch",
  "program": "${workspaceFolder}/src/server.ts",
  "env": {
    "NODE_ENV": "development",
    "PORT": "3000"
  }
}
```

### 3. 附加到进程

附加到正在运行的进程：

```json
{
  "name": "Attach to Process",
  "type": "node",
  "request": "attach",
  "port": 9229
}
```

## 10. 注意事项与常见错误

- **TypeScript 支持**：需要配置 TypeScript 支持（使用 tsx 或 ts-node）
- **源映射**：确保启用 source maps
- **环境变量**：正确配置环境变量
- **路径配置**：注意路径配置，使用变量
- **多配置**：合理组织多个调试配置

## 11. 常见问题 (FAQ)

**Q: 如何调试 TypeScript 文件？**
A: 使用 `tsx` 或 `ts-node` 作为加载器，或配置 `outFiles` 指向编译后的文件。

**Q: 如何设置条件断点？**
A: 右键断点，选择 "Edit Breakpoint"，设置条件表达式。

**Q: 如何附加到正在运行的进程？**
A: 使用 `attach` 配置，确保进程已启动 `--inspect`。

## 12. 最佳实践

- **配置管理**：将调试配置提交到版本控制
- **多配置**：为不同场景创建多个配置
- **环境变量**：使用环境变量管理配置
- **源映射**：确保启用 source maps
- **持续优化**：根据项目需求优化配置

## 13. 对比分析：VS Code 调试 vs Chrome DevTools

| 维度             | VS Code 调试                          | Chrome DevTools                        |
|:-----------------|:--------------------------------------|:---------------------------------------|
| **界面**         | 编辑器集成                            | 浏览器界面                             |
| **功能**         | 功能完整（编辑器集成）                | 功能强大（性能、内存分析）              |
| **易用性**       | 高（编辑器用户）                      | 高                                     |
| **适用场景**     | 日常开发、编辑器用户                  | 复杂调试、性能分析                     |

## 14. 练习任务

1. **VS Code 调试实践**：
   - 配置 VS Code 调试
   - 设置断点
   - 使用调试功能

2. **多配置实践**：
   - 创建多个调试配置
   - 理解不同配置的用途
   - 切换不同配置

3. **实际应用**：
   - 在实际项目中应用 VS Code 调试
   - 优化调试配置
   - 提高调试效率

完成以上练习后，继续学习下一章：Node.js 生态流行库概览。

## 总结

VS Code 调试是日常开发中最常用的调试方式：

- **核心功能**：编辑器集成、断点、变量检查、步进执行
- **使用场景**：日常开发、服务器调试、附加到进程
- **最佳实践**：配置管理、多配置、环境变量

掌握 VS Code 调试有助于提高开发效率。

---

**最后更新**：2025-01-XX
