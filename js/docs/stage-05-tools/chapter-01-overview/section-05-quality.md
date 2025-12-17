# 5.1.5 代码质量工具

## 概述

代码质量工具帮助保持代码风格一致、发现潜在问题。本节介绍常用的代码质量工具，包括 ESLint、Prettier 等。

## ESLint

### 简介

ESLint 是一个 JavaScript 代码检查工具，用于发现代码中的问题和强制执行代码风格。

### 安装

```bash
npm install --save-dev eslint
```

### 基本使用

```bash
# 初始化配置
npx eslint --init

# 检查文件
npx eslint file.js

# 自动修复
npx eslint file.js --fix
```

### 配置文件

```js
// .eslintrc.js
module.exports = {
    env: {
        browser: true,
        es2021: true,
    },
    extends: [
        'eslint:recommended',
    ],
    parserOptions: {
        ecmaVersion: 'latest',
        sourceType: 'module',
    },
    rules: {
        'no-console': 'warn',
        'no-unused-vars': 'error',
    },
};
```

### 常用规则

| 规则                | 说明                     | 级别   |
|:--------------------|:-------------------------|:-------|
| `no-console`        | 禁止使用 console         | warn   |
| `no-unused-vars`    | 禁止未使用的变量         | error  |
| `no-undef`          | 禁止未声明的变量         | error  |
| `eqeqeq`            | 要求使用 === 和 !==      | error  |
| `semi`              | 要求或禁止分号           | error  |
| `quotes`            | 要求使用单引号或双引号   | warn   |

### 插件和扩展

```bash
# 安装插件
npm install --save-dev eslint-plugin-react
npm install --save-dev @typescript-eslint/eslint-plugin
```

```js
// .eslintrc.js
module.exports = {
    plugins: ['react'],
    extends: [
        'eslint:recommended',
        'plugin:react/recommended',
    ],
};
```

## Prettier

### 简介

Prettier 是一个代码格式化工具，自动格式化代码，保持代码风格一致。

### 安装

```bash
npm install --save-dev prettier
```

### 基本使用

```bash
# 格式化文件
npx prettier --write file.js

# 检查格式
npx prettier --check file.js
```

### 配置文件

```json
// .prettierrc
{
    "semi": true,
    "singleQuote": true,
    "tabWidth": 2,
    "trailingComma": "es5",
    "printWidth": 80
}
```

### 常用配置

| 配置项          | 说明                   | 默认值   |
|:----------------|:-----------------------|:---------|
| `semi`          | 是否使用分号           | true     |
| `singleQuote`   | 是否使用单引号         | false    |
| `tabWidth`      | 缩进空格数             | 2        |
| `trailingComma` | 是否使用尾随逗号       | "none"   |
| `printWidth`    | 每行最大字符数         | 80       |

### 与 ESLint 集成

```bash
npm install --save-dev eslint-config-prettier
```

```js
// .eslintrc.js
module.exports = {
    extends: [
        'eslint:recommended',
        'prettier', // 必须放在最后
    ],
};
```

## TypeScript

### 简介

TypeScript 是 JavaScript 的超集，添加了类型系统，可以在编译时发现错误。

### 安装

```bash
npm install --save-dev typescript
```

### 配置文件

```json
// tsconfig.json
{
    "compilerOptions": {
        "target": "ES2020",
        "module": "ESNext",
        "strict": true,
        "esModuleInterop": true,
        "skipLibCheck": true,
        "forceConsistentCasingInFileNames": true
    }
}
```

### 基本使用

```bash
# 编译 TypeScript
npx tsc

# 检查类型
npx tsc --noEmit
```

## Husky

### 简介

Husky 是一个 Git hooks 工具，可以在提交代码前运行检查。

### 安装

```bash
npm install --save-dev husky
npx husky install
```

### 配置

```bash
# 添加 pre-commit hook
npx husky add .husky/pre-commit "npm test"
npx husky add .husky/pre-commit "npm run lint"
```

## lint-staged

### 简介

lint-staged 可以只对暂存的文件运行 lint 和格式化。

### 安装

```bash
npm install --save-dev lint-staged
```

### 配置

```json
// package.json
{
    "lint-staged": {
        "*.js": ["eslint --fix", "prettier --write"],
        "*.{json,md}": ["prettier --write"]
    }
}
```

## 工具对比

| 工具        | 作用           | 特点                     |
|:------------|:---------------|:-------------------------|
| ESLint      | 代码检查       | 可配置规则，发现代码问题 |
| Prettier    | 代码格式化     | 自动格式化，风格一致     |
| TypeScript  | 类型检查       | 编译时类型检查           |
| Husky       | Git hooks      | 提交前检查               |
| lint-staged | 暂存文件检查   | 只检查修改的文件         |

## 选择建议

1. **代码检查**：使用 ESLint
2. **代码格式化**：使用 Prettier
3. **类型安全**：使用 TypeScript
4. **提交前检查**：使用 Husky + lint-staged

## 注意事项

1. **规则配置**：根据团队需求配置规则
2. **工具冲突**：注意 ESLint 和 Prettier 的冲突
3. **性能考虑**：大型项目注意检查性能
4. **持续维护**：定期更新规则和配置

## 最佳实践

1. **统一配置**：团队使用统一的配置
2. **自动修复**：配置自动修复和格式化
3. **提交前检查**：使用 Git hooks 提交前检查
4. **CI/CD 集成**：在 CI/CD 中运行检查

## 练习

1. **ESLint 配置**：配置 ESLint，设置适合的规则。

2. **Prettier 配置**：配置 Prettier，设置代码格式化规则。

3. **工具集成**：将 ESLint 和 Prettier 集成，避免冲突。

4. **Git hooks**：使用 Husky 和 lint-staged 配置提交前检查。

5. **TypeScript 实践**：在项目中使用 TypeScript，体验类型检查。

完成以上练习后，继续学习下一节，了解历史技术与库。

## 总结

ESLint、Prettier、TypeScript 等工具可以帮助保持代码质量。ESLint 用于代码检查，Prettier 用于代码格式化，TypeScript 提供类型安全。使用 Husky 和 lint-staged 可以在提交前自动检查代码，确保代码质量。

## 相关资源

- [ESLint 官网](https://eslint.org/)
- [Prettier 官网](https://prettier.io/)
- [TypeScript 官网](https://www.typescriptlang.org/)
- [Husky 官网](https://typicode.github.io/husky/)
