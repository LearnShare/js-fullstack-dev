# 1.1.1 TypeScript 安装

## 概述

安装 TypeScript 是使用 TypeScript 的第一步。本节介绍如何安装 TypeScript 编译器，包括全局安装和项目安装两种方式。

## 安装方式

### 全局安装

全局安装后，可以在任何地方使用 `tsc` 命令。

#### 使用 npm

```bash
npm install -g typescript
```

#### 使用 yarn

```bash
yarn global add typescript
```

#### 使用 pnpm

```bash
pnpm add -g typescript
```

#### 验证安装

```bash
tsc --version
# 或
tsc -v
```

**输出示例**：
```
Version 5.6.2
```

### 项目安装

项目安装将 TypeScript 作为开发依赖安装在项目中，推荐使用这种方式。

#### 使用 npm

```bash
npm install -D typescript
```

#### 使用 yarn

```bash
yarn add -D typescript
```

#### 使用 pnpm

```bash
pnpm add -D typescript
```

#### 使用 npx 执行

项目安装后，可以使用 npx 执行：

```bash
npx tsc --version
```

#### 在 package.json 中添加脚本

```json
{
  "scripts": {
    "build": "tsc",
    "type-check": "tsc --noEmit"
  }
}
```

然后运行：

```bash
npm run build
npm run type-check
```

## 安装特定版本

### 安装最新版本

```bash
npm install -D typescript@latest
```

### 安装特定版本

```bash
npm install -D typescript@5.6.0
```

### 安装 Beta 或 RC 版本

```bash
npm install -D typescript@beta
npm install -D typescript@rc
```

## 升级 TypeScript

### 升级全局安装

```bash
npm update -g typescript
```

### 升级项目安装

```bash
npm update typescript
```

或手动更新 package.json 中的版本号，然后运行：

```bash
npm install
```

## 卸载 TypeScript

### 卸载全局安装

```bash
npm uninstall -g typescript
```

### 卸载项目安装

```bash
npm uninstall typescript
```

## 安装建议

### 推荐方式：项目安装

**优势**：
- 项目可以锁定 TypeScript 版本
- 团队成员使用相同的 TypeScript 版本
- 不同项目可以使用不同版本
- 避免全局污染

**使用方式**：
- 使用 `npx tsc` 执行
- 或在 package.json 中添加脚本

### 全局安装的使用场景

**适用场景**：
- 快速测试和学习
- 临时使用 TypeScript
- 全局工具脚本

**注意事项**：
- 全局安装可能与项目版本冲突
- 团队协作时可能版本不一致

## 验证安装

### 检查版本

```bash
tsc --version
```

### 检查帮助信息

```bash
tsc --help
```

### 创建测试文件

创建 `test.ts` 文件：

```ts
const message: string = "Hello, TypeScript!";
console.log(message);
```

编译测试：

```bash
tsc test.ts
```

如果安装成功，会生成 `test.js` 文件。

## 常见问题

### 问题 1：命令未找到

**错误信息**：
```
'tsc' 不是内部或外部命令，也不是可运行的程序
```

**解决方案**：
1. 检查是否已安装：`npm list -g typescript`
2. 检查 PATH 环境变量
3. 使用项目安装 + npx：`npx tsc`

### 问题 2：版本不匹配

**问题**：全局版本与项目版本不一致

**解决方案**：
- 使用项目安装，避免全局版本冲突
- 或在项目中指定 TypeScript 版本

### 问题 3：权限问题

**错误信息**：
```
EACCES: permission denied
```

**解决方案**：
- 使用项目安装，避免权限问题
- 或使用 sudo（不推荐）

## 注意事项

1. **版本管理**：建议使用项目安装，锁定版本
2. **Node.js 版本**：确保 Node.js 版本兼容（建议 Node.js 14+）
3. **包管理器**：根据项目使用的包管理器选择安装方式
4. **团队协作**：团队成员使用相同的 TypeScript 版本

## 最佳实践

1. **项目安装**：优先使用项目安装
2. **版本锁定**：在 package.json 中锁定 TypeScript 版本
3. **CI/CD 一致**：确保 CI/CD 环境使用相同的版本
4. **定期更新**：定期更新到最新稳定版本

## 练习

1. **安装 TypeScript**：在项目中安装 TypeScript 作为开发依赖。

2. **验证安装**：使用 `tsc --version` 验证安装是否成功。

3. **创建测试**：创建第一个 TypeScript 文件，编译并运行。

4. **版本管理**：在 package.json 中查看和锁定 TypeScript 版本。

5. **脚本配置**：在 package.json 中添加编译和类型检查脚本。

完成以上练习后，继续学习下一节，了解 tsconfig.json 配置。

## 总结

TypeScript 可以通过全局安装或项目安装。推荐使用项目安装，可以锁定版本并确保团队使用相同的 TypeScript 版本。安装后可以通过 `tsc --version` 验证安装是否成功。

## 相关资源

- [TypeScript 官网](https://www.typescriptlang.org/)
- [npm TypeScript 包](https://www.npmjs.com/package/typescript)
