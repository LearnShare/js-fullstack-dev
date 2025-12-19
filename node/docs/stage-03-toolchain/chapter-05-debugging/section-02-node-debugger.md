# 3.5.2 Node.js 调试器

## 1. 概述

Node.js 内置了调试器，可以通过命令行使用。Node.js 调试器支持断点、变量检查、步进执行等基本调试功能。理解 Node.js 调试器的使用对于在服务器环境或命令行环境调试非常重要。

## 2. 特性说明

- **命令行界面**：通过命令行使用，适合服务器环境。
- **基本功能**：支持断点、变量检查、步进执行。
- **Inspector 协议**：支持 Chrome DevTools 协议。
- **远程调试**：支持远程调试。
- **简单易用**：配置简单，易于使用。

## 3. 启动调试

### 基本启动

```bash
# 文件: node-debug.sh
# 功能: Node.js 调试器启动

# 启动调试（Inspector 模式）
node --inspect script.js

# 启动调试（等待调试器连接）
node --inspect-brk script.js

# 启动调试（指定端口）
node --inspect=0.0.0.0:9229 script.js
```

### 调试命令

```bash
# 进入调试模式
node inspect script.js

# 或使用
node --inspect script.js
```

## 4. 基本用法

### 示例 1：基本调试

```ts
// 文件: debug-example.ts
// 功能: 调试示例

function calculateTotal(items: number[]): number {
    let total = 0;
    
    debugger; // 断点
    
    for (const item of items) {
        total += item;
    }
    
    return total;
}

const items = [1, 2, 3, 4, 5];
const total = calculateTotal(items);
console.log('Total:', total);
```

启动调试：

```bash
node --inspect-brk debug-example.ts
```

### 示例 2：调试命令

在调试模式下可以使用以下命令：

```bash
# 调试命令
n> help          # 显示帮助
n> cont, c       # 继续执行
n> next, n       # 下一行
n> step, s       # 进入函数
n> out, o        # 跳出函数
n> repl          # 进入 REPL 模式
n> setBreakpoint # 设置断点
n> list          # 显示代码
```

## 5. 参数说明：Node.js 调试参数

### 启动参数

| 参数名           | 说明                                     | 示例                           |
|:-----------------|:-----------------------------------------|:-------------------------------|
| **--inspect**    | 启动 Inspector，不暂停                   | `node --inspect script.js`     |
| **--inspect-brk**| 启动 Inspector，在第一行暂停             | `node --inspect-brk script.js` |
| **--inspect-port**| 指定端口                               | `node --inspect=9229 script.js`|

## 6. 返回值与状态说明

Node.js 调试器的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **启动调试** | 调试会话     | 显示调试器监听地址                       |
| **断点命中** | 暂停执行     | 代码执行到断点处暂停                     |

## 7. 代码示例：完整调试流程

以下示例演示了完整的调试流程：

```ts
// 文件: debug-complete.ts
// 功能: 完整调试流程

function processUserData(userId: number): any {
    debugger; // 断点 1: 检查 userId
    
    const user = getUserById(userId);
    debugger; // 断点 2: 检查 user
    
    if (!user) {
        throw new Error('User not found');
    }
    
    const processed = {
        id: user.id,
        name: user.name,
        email: user.email
    };
    
    debugger; // 断点 3: 检查 processed
    
    return processed;
}

function getUserById(id: number): any {
    // 模拟获取用户
    return { id, name: 'Alice', email: 'alice@example.com' };
}

// 启动调试
processUserData(1);
```

启动调试：

```bash
node --inspect-brk debug-complete.ts
```

## 8. 输出结果说明

Node.js 调试器的输出结果：

```text
Debugger listening on ws://127.0.0.1:9229/abc123...
For help, see: https://nodejs.org/en/docs/inspector
```

**逻辑解析**：
- 显示调试器监听地址
- 可以使用 Chrome DevTools 连接
- 代码执行到断点处会暂停

## 9. 使用场景

### 1. 服务器环境调试

在服务器环境调试：

```bash
# 启动调试
node --inspect server.js

# 在 Chrome DevTools 中连接
# chrome://inspect
```

### 2. 命令行调试

在命令行环境调试：

```bash
# 进入调试模式
node inspect script.js

# 使用调试命令
n> cont
n> next
n> repl
```

### 3. 远程调试

远程调试：

```bash
# 启动远程调试
node --inspect=0.0.0.0:9229 script.js

# 从远程连接
# chrome://inspect -> Configure -> 添加远程地址
```

## 10. 注意事项与常见错误

- **端口安全**：远程调试时注意端口安全
- **性能影响**：调试模式可能影响性能
- **断点位置**：合理设置断点
- **异步调试**：注意异步代码的调试
- **生产环境**：不要在生产环境启用调试

## 11. 常见问题 (FAQ)

**Q: 如何连接 Chrome DevTools？**
A: 启动 `--inspect` 后，在 Chrome 中访问 `chrome://inspect`，点击 "inspect"。

**Q: 如何设置条件断点？**
A: 在 Chrome DevTools 中设置条件断点，或在代码中使用 `if` 语句。

**Q: 如何调试异步代码？**
A: 使用 `async/await` 或 Promise 的调试功能，注意异步执行流程。

## 12. 最佳实践

- **合理使用**：合理使用调试器，不要过度依赖
- **日志结合**：结合日志调试，提高效率
- **远程调试**：注意远程调试的安全性
- **性能考虑**：注意调试对性能的影响
- **工具选择**：根据环境选择合适的调试方式

## 13. 对比分析：Node.js 调试器 vs Chrome DevTools

| 维度             | Node.js 调试器                          | Chrome DevTools                        |
|:-----------------|:----------------------------------------|:---------------------------------------|
| **界面**         | 命令行                                   | 图形界面                               |
| **功能**         | 基础功能                                 | 功能强大                               |
| **易用性**       | 中等                                     | 高                                     |
| **适用场景**     | 服务器环境、命令行                       | 复杂调试、需要可视化                   |

## 14. 练习任务

1. **Node.js 调试器实践**：
   - 启动调试会话
   - 使用调试命令
   - 设置和检查断点

2. **Chrome DevTools 集成实践**：
   - 连接 Chrome DevTools
   - 使用图形界面调试
   - 理解调试功能

3. **实际应用**：
   - 在实际项目中应用调试器
   - 定位和解决问题
   - 提高调试效率

完成以上练习后，继续学习下一节：Chrome DevTools 集成。

## 总结

Node.js 调试器是基础调试工具：

- **核心功能**：断点、变量检查、步进执行
- **使用场景**：服务器环境、命令行调试、远程调试
- **最佳实践**：合理使用、日志结合、工具选择

掌握 Node.js 调试器有助于在服务器环境调试。

---

**最后更新**：2025-01-XX
