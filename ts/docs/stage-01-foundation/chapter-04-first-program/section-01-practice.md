# 1.3.1 第一个 TypeScript 程序实践

## 概述

本节通过创建一个简单的 TypeScript 程序，学习 TypeScript 的基本开发流程：编写代码、类型检查、编译和运行。

## 实践步骤

### 步骤 1：创建项目目录

首先创建一个项目目录：

```bash
mkdir my-first-typescript
cd my-first-typescript
```

### 步骤 2：初始化项目

初始化 npm 项目（可选，但推荐）：

```bash
npm init -y
```

### 步骤 3：安装 TypeScript

在项目中安装 TypeScript：

```bash
npm install --save-dev typescript
```

### 步骤 4：创建 TypeScript 文件

创建第一个 TypeScript 文件 `hello.ts`：

```ts
// hello.ts
function greet(name: string): string {
    return `Hello, ${name}!`;
}

const message: string = greet("TypeScript");
console.log(message);
```

### 步骤 5：编译 TypeScript 文件

使用 TypeScript 编译器编译文件：

```bash
npx tsc hello.ts
```

**输出结果说明**：

编译成功后，会在同一目录下生成 `hello.js` 文件：

```js
// hello.js
function greet(name) {
    return `Hello, ${name}!`;
}
const message = greet("TypeScript");
console.log(message);
```

### 步骤 6：运行编译后的代码

运行编译后的 JavaScript 文件：

```bash
node hello.js
```

**输出结果说明**：

```
Hello, TypeScript!
```

## 完整代码示例

### 示例 1：基础类型使用

```ts
// example1.ts
// 定义变量并指定类型
let userName: string = "Alice";
let userAge: number = 25;
let isActive: boolean = true;

// 定义函数并指定参数和返回值类型
function getUserInfo(name: string, age: number): string {
    return `${name} is ${age} years old`;
}

// 调用函数
const info: string = getUserInfo(userName, userAge);
console.log(info);
console.log(`Active: ${isActive}`);
```

**编译命令**：

```bash
npx tsc example1.ts
```

**运行结果**：

```bash
node example1.js
```

**输出结果说明**：

```
Alice is 25 years old
Active: true
```

### 示例 2：数组和对象

```ts
// example2.ts
// 定义数组类型
let numbers: number[] = [1, 2, 3, 4, 5];

// 定义对象类型
interface User {
    name: string;
    age: number;
    email: string;
}

// 创建对象
const user: User = {
    name: "Bob",
    age: 30,
    email: "bob@example.com"
};

// 使用数组方法
const doubled: number[] = numbers.map(n => n * 2);
console.log("Original:", numbers);
console.log("Doubled:", doubled);
console.log("User:", user);
```

**编译和运行**：

```bash
npx tsc example2.ts
node example2.js
```

**输出结果说明**：

```
Original: [ 1, 2, 3, 4, 5 ]
Doubled: [ 2, 4, 6, 8, 10 ]
User: { name: 'Bob', age: 30, email: 'bob@example.com' }
```

### 示例 3：类型错误演示

故意写一些类型错误，观察 TypeScript 的类型检查：

```ts
// example3-error.ts
let count: number = 10;

// 错误：尝试将字符串赋值给数字类型
count = "20";  // TypeScript 会报错

// 错误：函数参数类型不匹配
function add(a: number, b: number): number {
    return a + b;
}

add("10", 20);  // TypeScript 会报错
```

**编译结果**：

```bash
npx tsc example3-error.ts
```

**输出结果说明**：

TypeScript 编译器会显示类型错误：

```
example3-error.ts:5:1 - error TS2322: Type 'string' is not assignable to type 'number'.

5 count = "20";
  ~~~~~

example3-error.ts:12:1 - error TS2345: Argument of type 'string' is not assignable to parameter of type 'number'.

12 add("10", 20);
    ~~~~~

Found 2 errors.
```

## 使用 tsconfig.json

### 创建配置文件

创建 `tsconfig.json` 文件：

```bash
npx tsc --init
```

### 基本配置

编辑 `tsconfig.json`：

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules"]
}
```

### 使用配置文件编译

将 TypeScript 文件放在 `src` 目录下，然后编译：

```bash
npx tsc
```

编译后的文件会输出到 `dist` 目录。

## 注意事项

1. **文件扩展名**：TypeScript 文件使用 `.ts` 扩展名
2. **编译输出**：默认情况下，编译后的 JavaScript 文件与源文件在同一目录
3. **类型检查**：TypeScript 会在编译时进行类型检查，发现类型错误会阻止编译
4. **严格模式**：建议启用严格模式（`"strict": true`）以获得更好的类型安全
5. **输出目录**：使用 `outDir` 选项指定编译输出目录，保持项目结构清晰

## 常见问题

### 问题 1：找不到 tsc 命令

**原因**：TypeScript 未安装或未在 PATH 中

**解决方案**：

```bash
# 使用 npx（推荐）
npx tsc hello.ts

# 或全局安装
npm install -g typescript
tsc hello.ts
```

### 问题 2：编译后找不到输出文件

**原因**：可能配置了 `outDir`，输出到了其他目录

**解决方案**：

检查 `tsconfig.json` 中的 `outDir` 配置，或使用 `--outDir` 选项：

```bash
npx tsc hello.ts --outDir ./dist
```

### 问题 3：类型错误但代码仍能运行

**原因**：TypeScript 默认会编译，即使有类型错误（除非配置了 `noEmitOnError`）

**解决方案**：

在 `tsconfig.json` 中启用 `noEmitOnError`：

```json
{
  "compilerOptions": {
    "noEmitOnError": true
  }
}
```

## 最佳实践

1. **使用配置文件**：使用 `tsconfig.json` 管理编译选项，而不是命令行参数
2. **组织项目结构**：将源文件放在 `src` 目录，编译输出放在 `dist` 目录
3. **启用严格模式**：在 `tsconfig.json` 中启用 `strict: true`
4. **版本控制**：将 `tsconfig.json` 提交到版本控制，但不要提交编译输出
5. **使用类型注解**：为函数参数和返回值添加类型注解，提高代码可读性

## 练习任务

1. **创建第一个程序**：
   - 创建一个 TypeScript 文件，定义一个计算两个数之和的函数
   - 编译并运行该程序
   - 观察编译后的 JavaScript 代码

2. **类型错误实验**：
   - 故意写一些类型错误（如将字符串赋值给数字变量）
   - 尝试编译，观察 TypeScript 的错误提示
   - 修复错误后重新编译

3. **使用接口**：
   - 定义一个 `Person` 接口，包含 `name`、`age`、`email` 属性
   - 创建一个符合该接口的对象
   - 编写一个函数，接收 `Person` 类型的参数并打印信息

4. **数组操作**：
   - 创建一个数字数组
   - 使用数组方法（`map`、`filter`、`reduce`）处理数组
   - 为所有变量和函数添加类型注解

5. **配置项目**：
   - 创建 `tsconfig.json` 文件
   - 配置 `outDir` 和 `rootDir`
   - 启用严格模式
   - 重新组织项目结构并编译

完成以上练习后，继续学习阶段二：结构化类型系统。

## 总结

第一个 TypeScript 程序的创建过程包括：

1. **编写 TypeScript 代码**：使用 `.ts` 扩展名，添加类型注解
2. **编译代码**：使用 `tsc` 命令将 TypeScript 编译为 JavaScript
3. **运行代码**：使用 Node.js 运行编译后的 JavaScript 代码
4. **类型检查**：TypeScript 在编译时进行类型检查，发现类型错误

通过这个实践，你已经掌握了 TypeScript 的基本开发流程。接下来可以深入学习 TypeScript 的类型系统。

---

**最后更新**：2025-01-XX
