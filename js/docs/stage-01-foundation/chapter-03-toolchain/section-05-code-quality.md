# 1.2.5 代码质量工具（ESLint、Prettier、TypeScript、Husky）

## 概述

代码质量工具确保风格一致、提前暴露潜在错误、降低评审成本，是团队协作和持续交付的基础。本节覆盖 ESLint（规则/风格/最佳实践）、Prettier（格式化）、TypeScript（类型检查）、Husky + lint-staged（提交前校验），以及 CI 集成、排错与最佳实践清单。

## 为什么要用
- 统一风格，减少无谓争论。
- 在编码期暴露问题（未定义变量、未使用变量、潜在类型错误）。
- 提升可维护性和可读性。
- 与 CI/CD/提交钩子协同，防止问题进入主干。

## ESLint

### 安装与初始化
```bash
npm install --save-dev eslint
npx eslint --init
```

### 基础配置示例
```js
// .eslintrc.js
module.exports = {
  env: { browser: true, es2022: true, node: true },
  extends: ['eslint:recommended'],
  parserOptions: { ecmaVersion: 2022, sourceType: 'module' },
  rules: {
    'no-unused-vars': ['warn', { argsIgnorePattern: '^_' }],
    'no-undef': 'error',
    'eqeqeq': ['error', 'always'],
    'curly': ['error', 'all'],
    'prefer-const': 'warn'
  }
};
```

### 运行
```bash
npx eslint src --fix
```

## Prettier（格式化）

### 安装与配置
```bash
npm install --save-dev prettier
```
`.prettierrc` 示例：
```json
{
  "singleQuote": true,
  "semi": true,
  "trailingComma": "es5",
  "printWidth": 100
}
```
忽略：`.prettierignore`（如 `dist/`, `coverage/`, `*.min.js`）。

### 运行
```bash
npx prettier --write "src/**/*.{js,ts,jsx,tsx,json,md}"
```

## ESLint + Prettier 协同

安装：
```bash
npm install --save-dev eslint-config-prettier eslint-plugin-prettier
```

配置（关闭冲突规则，并把格式化问题当作 lint）：
```js
module.exports = {
  extends: [
    'eslint:recommended',
    'plugin:prettier/recommended'
  ]
};
```

## TypeScript 类型检查

### 安装
```bash
npm install --save-dev typescript @types/node
```

### `tsconfig.json` 示例
```json
{
  "compilerOptions": {
    "target": "es2020",
    "module": "esnext",
    "moduleResolution": "node",
    "strict": true,
    "jsx": "react-jsx",
    "allowJs": true,
    "esModuleInterop": true,
    "skipLibCheck": true
  },
  "include": ["src"]
}
```

### 配合 ESLint（TS 项目）
```bash
npm install --save-dev @typescript-eslint/parser @typescript-eslint/eslint-plugin
```
```js
module.exports = {
  parser: '@typescript-eslint/parser',
  plugins: ['@typescript-eslint'],
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:prettier/recommended'
  ]
};
```

## 提交前校验：Husky + lint-staged

### 安装与钩子
```bash
npm install --save-dev husky lint-staged
npx husky install
npx husky add .husky/pre-commit "npx lint-staged"
```

`package.json` 中添加：
```json
{
  "lint-staged": {
    "*.{js,ts,jsx,tsx}": ["eslint --fix", "prettier --write"],
    "*.{json,md}": ["prettier --write"]
  }
}
```

## CI 集成（GitHub Actions 示例）
```yaml
name: lint
on: [push, pull_request]
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 20 }
      - run: npm ci
      - run: npm run lint && npm run format -- --check
```

## 常见问题与排查
- **格式化与 ESLint 冲突**：缺少 `eslint-config-prettier`；或 extends 顺序错误（需放末尾）。  
- **未被格式化**：glob 未匹配、文件被 `.prettierignore` 忽略。  
- **类型检查未生效**：未用 TS parser；`include` 未覆盖；`allowJs/checkJs` 配置不当。  
- **CI 与本地不一致**：Node/依赖未锁定，缺少 `npm ci`，或未提交锁文件。  
- **提交前过慢**：lint-staged 仅处理变更文件；必要时缩小规则或使用缓存。  

## 最佳实践清单
1) ESLint 负责语法/最佳实践，Prettier 负责格式化，使用 `plugin:prettier/recommended` 消除冲突。  
2) 在 TS 项目开启 `strict`，在 JS 项目可用 `checkJs` + JSDoc 增强类型。  
3) 提交前钩子（Husky + lint-staged）前移质量门槛，CI 再兜底。  
4) 锁定 Node 与依赖版本，使用 `npm ci`/`pnpm install --frozen-lockfile` 保持可重复构建。  
5) 为团队提供统一的编辑器设置（格式化、保存自动修复），减少环境差异。  
6) 对生成物/第三方代码使用 ignore，避免无意义检查。  

## 练习
1. 为示例项目配置 ESLint + Prettier + TS，运行 `npm run lint`、`npm run format -- --check`。  
2. 配置 Husky + lint-staged，在提交前自动修复并阻止未通过的提交。  
3. 在 CI 中添加 lint 工作流，确保与本地规则一致。  
4. 开启 `strict` 后修复暴露的潜在问题，体会类型系统收益。  
5. 设计团队级规则清单（必选/可选/忽略），写入仓库配置与 README。  

## 小结

- ESLint：语法与最佳实践；Prettier：格式化；TypeScript：类型防线。  
- `eslint-config-prettier` 解决格式冲突，`plugin:prettier/recommended` 将格式问题视为 lint。  
- Husky + lint-staged 在提交前自动把关，CI 兜底。  
- 统一配置、锁定依赖与版本，减少“环境不一致”带来的返工。  
