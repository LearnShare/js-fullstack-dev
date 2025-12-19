# 3.7.1 CLI 开发

## 1. 概述

CLI（Command Line Interface，命令行界面）开发是 Node.js 的重要应用领域之一。通过 CLI 工具，开发者可以创建命令行程序，提供交互式命令行体验。Node.js 生态中有许多优秀的 CLI 开发框架和工具，帮助开发者快速构建功能强大的命令行工具。

## 2. 特性说明

- **命令行参数解析**：解析命令行参数和选项。
- **交互式输入**：提供交互式命令行输入体验。
- **彩色输出**：支持彩色终端输出，提升用户体验。
- **进度显示**：显示任务进度和状态。
- **命令组织**：支持多命令和子命令的组织。

## 3. 主流工具概览

### Commander.js

最流行的 CLI 框架，功能强大且易用。

**特点**：
- 完整的命令行参数解析
- 支持子命令
- 自动生成帮助信息
- TypeScript 支持

**安装**：
```bash
npm install commander
```

**基本用法**：
```ts
// 文件: cli-commander.ts
// 功能: Commander.js 基本用法

import { Command } from 'commander';

const program = new Command();

program
    .name('my-cli')
    .description('A simple CLI tool')
    .version('1.0.0');

program
    .command('greet <name>')
    .description('Greet someone')
    .option('-t, --title <title>', 'Title to use', 'Mr')
    .action((name, options) => {
        console.log(`Hello, ${options.title} ${name}!`);
    });

program.parse();
```

### Inquirer.js

提供交互式命令行输入体验。

**特点**：
- 多种输入类型（文本、选择、确认等）
- 美观的交互界面
- Promise 支持
- 验证和转换功能

**安装**：
```bash
npm install inquirer
```

**基本用法**：
```ts
// 文件: cli-inquirer.ts
// 功能: Inquirer.js 基本用法

import inquirer from 'inquirer';

async function interactiveCLI() {
    const answers = await inquirer.prompt([
        {
            type: 'input',
            name: 'name',
            message: 'What is your name?',
            validate: (input) => input.length > 0 || 'Name is required'
        },
        {
            type: 'list',
            name: 'language',
            message: 'Choose your favorite language:',
            choices: ['JavaScript', 'TypeScript', 'Python', 'Go']
        },
        {
            type: 'confirm',
            name: 'confirm',
            message: 'Are you sure?'
        }
    ]);
    
    console.log('Answers:', answers);
}

interactiveCLI();
```

### Chalk

提供彩色终端输出。

**特点**：
- 丰富的颜色支持
- 链式调用
- 自动检测终端颜色支持
- TypeScript 支持

**安装**：
```bash
npm install chalk
```

**基本用法**：
```ts
// 文件: cli-chalk.ts
// 功能: Chalk 基本用法

import chalk from 'chalk';

console.log(chalk.blue('Hello') + ' ' + chalk.red('World'));
console.log(chalk.bgGreen.black('Success!'));
console.log(chalk.bold.underline('Important message'));
console.log(chalk.hex('#FF5733')('Custom color'));
```

### Ora

显示加载动画和进度。

**特点**：
- 多种加载动画
- 进度显示
- 成功/失败状态
- 自动清理

**安装**：
```bash
npm install ora
```

**基本用法**：
```ts
// 文件: cli-ora.ts
// 功能: Ora 基本用法

import ora from 'ora';

async function showProgress() {
    const spinner = ora('Loading...').start();
    
    // 模拟异步操作
    await new Promise(resolve => setTimeout(resolve, 2000));
    
    spinner.succeed('Loaded successfully!');
}

showProgress();
```

## 4. 代码示例：完整 CLI 工具

以下示例演示了如何构建一个完整的 CLI 工具：

```ts
// 文件: complete-cli.ts
// 功能: 完整的 CLI 工具示例

import { Command } from 'commander';
import inquirer from 'inquirer';
import chalk from 'chalk';
import ora from 'ora';

const program = new Command();

program
    .name('todo-cli')
    .description('A simple todo list CLI')
    .version('1.0.0');

program
    .command('add')
    .description('Add a new todo')
    .action(async () => {
        const answers = await inquirer.prompt([
            {
                type: 'input',
                name: 'task',
                message: 'Enter task:',
                validate: (input) => input.length > 0 || 'Task cannot be empty'
            }
        ]);
        
        const spinner = ora('Adding task...').start();
        // 模拟保存操作
        await new Promise(resolve => setTimeout(resolve, 1000));
        spinner.succeed(chalk.green(`Task "${answers.task}" added!`));
    });

program
    .command('list')
    .description('List all todos')
    .action(() => {
        console.log(chalk.blue('Todo List:'));
        console.log('  - Task 1');
        console.log('  - Task 2');
    });

program.parse();
```

## 5. 参数说明：CLI 工具常用参数

| 参数类型     | 说明                                     | 示例                           |
|:-------------|:-----------------------------------------|:-------------------------------|
| **位置参数** | 必需的命令参数                            | `greet <name>`                 |
| **选项**     | 可选的命令行选项                          | `-t, --title <title>`          |
| **标志**     | 布尔类型的选项                            | `-v, --verbose`                |
| **子命令**   | 命令的子命令                              | `git add`, `git commit`        |

## 6. 返回值与状态说明

CLI 工具的退出码：

| 退出码 | 说明                                     |
|:-------|:-----------------------------------------|
| **0**  | 成功执行                                 |
| **1**  | 一般错误                                 |
| **2**  | 误用命令（如参数错误）                   |

## 7. 输出结果说明

CLI 工具的输出示例：

```text
$ todo-cli add
? Enter task: Buy groceries
✔ Adding task...
✔ Task "Buy groceries" added!
```

**逻辑解析**：
- 使用 Inquirer 进行交互式输入
- 使用 Ora 显示加载状态
- 使用 Chalk 提供彩色输出

## 8. 使用场景

### 1. 开发工具

创建开发辅助工具：

```ts
// 开发工具示例
program
    .command('init <project-name>')
    .description('Initialize a new project')
    .option('-t, --template <template>', 'Project template')
    .action(async (name, options) => {
        // 初始化项目逻辑
    });
```

### 2. 数据管理工具

创建数据管理工具：

```ts
// 数据管理工具示例
program
    .command('export')
    .description('Export data')
    .option('-f, --format <format>', 'Export format', 'json')
    .action(async (options) => {
        // 导出数据逻辑
    });
```

### 3. 自动化脚本

创建自动化脚本：

```ts
// 自动化脚本示例
program
    .command('deploy')
    .description('Deploy application')
    .option('-e, --env <env>', 'Environment', 'production')
    .action(async (options) => {
        // 部署逻辑
    });
```

## 9. 注意事项与常见错误

- **参数验证**：始终验证用户输入，防止错误
- **错误处理**：提供清晰的错误信息
- **帮助信息**：提供完整的帮助信息
- **退出码**：正确设置退出码，便于脚本调用
- **跨平台兼容**：注意不同操作系统的差异

## 10. 常见问题 (FAQ)

**Q: 如何创建全局 CLI 工具？**
A: 在 `package.json` 中添加 `bin` 字段，然后使用 `npm link` 或发布到 npm。

**Q: 如何测试 CLI 工具？**
A: 使用 `execa` 或 `child_process` 模块执行命令并验证输出。

**Q: 如何支持自动补全？**
A: 使用 `commander` 的自动补全功能，或使用 `tabtab` 等工具。

## 11. 最佳实践

- **使用框架**：使用 Commander.js 等框架，避免手动解析参数
- **交互体验**：使用 Inquirer.js 提供良好的交互体验
- **视觉反馈**：使用 Chalk 和 Ora 提供视觉反馈
- **错误处理**：提供清晰的错误信息和帮助
- **文档完善**：提供完整的命令文档和示例

## 12. 对比分析：主流 CLI 框架

| 框架           | 特点                                     | 适用场景                       |
|:---------------|:-----------------------------------------|:-------------------------------|
| **Commander.js**| 功能强大，使用广泛                        | 复杂 CLI 工具                  |
| **Yargs**      | 灵活的 API，支持插件                     | 需要高度定制的 CLI             |
| **Meow**       | 轻量级，基于 Minimist                    | 简单的 CLI 工具                |
| **Clack**      | 现代设计，TypeScript 优先                 | 新项目，追求现代体验            |

## 13. 练习任务

1. **CLI 工具开发实践**：
   - 使用 Commander.js 创建简单的 CLI 工具
   - 添加交互式输入功能
   - 实现彩色输出和进度显示

2. **参数解析实践**：
   - 实现位置参数和选项参数
   - 添加参数验证
   - 实现子命令功能

3. **用户体验优化**：
   - 使用 Inquirer.js 改善交互体验
   - 使用 Chalk 提供视觉反馈
   - 使用 Ora 显示进度

4. **实际应用**：
   - 创建实际的 CLI 工具（如文件管理、数据处理等）
   - 发布到 npm
   - 编写使用文档

完成以上练习后，继续学习下一节：爬虫开发。

## 总结

CLI 开发是 Node.js 的重要应用领域：

- **主流工具**：Commander.js、Inquirer.js、Chalk、Ora
- **核心功能**：参数解析、交互输入、彩色输出、进度显示
- **最佳实践**：使用框架、提供良好体验、完善文档

掌握 CLI 开发有助于创建强大的命令行工具。

---

**最后更新**：2025-01-XX
