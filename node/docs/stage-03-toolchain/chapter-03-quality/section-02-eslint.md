# 3.3.2 ESLint 配置

## 1. 概述

ESLint 是一个可插拔的 JavaScript 和 TypeScript 代码检查工具，用于发现代码中的错误、潜在问题和代码风格问题。理解 ESLint 的配置和使用对于保证代码质量至关重要。

## 2. 特性说明

- **错误检测**：检测代码中的错误和潜在问题。
- **代码风格**：检查代码风格，保持一致性。
- **可配置**：高度可配置，支持自定义规则。
- **插件系统**：丰富的插件生态系统。
- **自动修复**：支持自动修复部分问题。

## 3. 安装与配置

### 安装 ESLint

```bash
# 安装 ESLint
npm install -D eslint

# 安装 TypeScript 支持
npm install -D @typescript-eslint/parser @typescript-eslint/eslint-plugin

# 安装 Prettier 集成
npm install -D eslint-config-prettier eslint-plugin-prettier
```

### 初始化配置

```bash
# 初始化 ESLint 配置
npx eslint --init
```

## 4. 基本用法

### 示例 1：基本配置

```js
// 文件: .eslintrc.js
// 功能: ESLint 基本配置

module.exports = {
    env: {
        node: true,
        es2022: true
    },
    extends: [
        'eslint:recommended'
    ],
    parserOptions: {
        ecmaVersion: 'latest',
        sourceType: 'module'
    },
    rules: {
        'no-console': 'warn',
        'no-unused-vars': 'error'
    }
};
```

### 示例 2：TypeScript 配置

```js
// 文件: .eslintrc.js
// 功能: ESLint TypeScript 配置

module.exports = {
    env: {
        node: true,
        es2022: true
    },
    extends: [
        'eslint:recommended',
        'plugin:@typescript-eslint/recommended'
    ],
    parser: '@typescript-eslint/parser',
    plugins: ['@typescript-eslint'],
    parserOptions: {
        ecmaVersion: 'latest',
        sourceType: 'module',
        project: './tsconfig.json'
    },
    rules: {
        '@typescript-eslint/no-unused-vars': 'error',
        '@typescript-eslint/explicit-function-return-type': 'warn'
    }
};
```

### 示例 3：与 Prettier 集成

```js
// 文件: .eslintrc.js
// 功能: ESLint 与 Prettier 集成

module.exports = {
    extends: [
        'eslint:recommended',
        'plugin:@typescript-eslint/recommended',
        'prettier'  // 必须放在最后
    ],
    plugins: ['prettier'],
    rules: {
        'prettier/prettier': 'error'
    }
};
```

## 5. 参数说明：ESLint 配置选项

### 基本配置

| 配置项       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **env**      | Object   | 环境配置                                 | `{ node: true, es2022: true }` |
| **extends**  | Array    | 继承的配置                               | `['eslint:recommended']`       |
| **parser**   | String   | 解析器                                   | `'@typescript-eslint/parser'`  |
| **plugins**  | Array    | 插件列表                                 | `['@typescript-eslint']`       |
| **rules**    | Object   | 规则配置                                 | `{ 'no-console': 'warn' }`     |

### 规则级别

| 级别     | 说明                                     |
|:---------|:-----------------------------------------|
| **"off"**| 关闭规则                                 |
| **"warn"**| 警告级别                                |
| **"error"**| 错误级别                               |

## 6. 返回值与状态说明

ESLint 操作的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **检查**     | 成功/错误    | 显示检查结果，列出错误和警告             |
| **自动修复** | 成功/失败    | 自动修复部分问题，显示修复的文件         |

## 7. 代码示例：完整的 ESLint 配置

以下示例演示了完整的 ESLint 配置：

```js
// 文件: .eslintrc.js
// 功能: 完整的 ESLint 配置

module.exports = {
    env: {
        node: true,
        es2022: true
    },
    extends: [
        'eslint:recommended',
        'plugin:@typescript-eslint/recommended',
        'plugin:@typescript-eslint/recommended-requiring-type-checking',
        'prettier'
    ],
    parser: '@typescript-eslint/parser',
    plugins: ['@typescript-eslint', 'prettier'],
    parserOptions: {
        ecmaVersion: 'latest',
        sourceType: 'module',
        project: './tsconfig.json'
    },
    rules: {
        // TypeScript 规则
        '@typescript-eslint/no-unused-vars': 'error',
        '@typescript-eslint/explicit-function-return-type': 'warn',
        '@typescript-eslint/no-explicit-any': 'warn',
        
        // 通用规则
        'no-console': 'warn',
        'no-debugger': 'error',
        'prefer-const': 'error',
        
        // Prettier 集成
        'prettier/prettier': 'error'
    },
    ignorePatterns: ['dist/', 'node_modules/', '*.config.js']
};
```

## 8. 输出结果说明

ESLint 检查的输出结果：

```text
✖ ESLint found 3 problems (2 errors, 1 warning)

src/index.ts
  5:10  error  'unusedVar' is assigned a value but never used  @typescript-eslint/no-unused-vars
  8:5   error  Missing return type annotation                   @typescript-eslint/explicit-function-return-type
  12:3  warning  Unexpected console statement                   no-console
```

**逻辑解析**：
- 显示检查结果统计
- 显示文件路径和行号
- 显示错误描述和规则名称
- 显示错误类型（error/warning）

## 9. 使用场景

### 1. 开发时检查

在开发时实时检查代码：

```bash
# 检查代码
npm run lint

# 自动修复
npm run lint:fix
```

### 2. 编辑器集成

在编辑器中集成 ESLint：

```json
// .vscode/settings.json
{
  "eslint.validate": [
    "javascript",
    "typescript"
  ],
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
  }
}
```

### 3. CI/CD 集成

在 CI/CD 中集成 ESLint：

```yaml
# .github/workflows/ci.yml
- name: Lint
  run: npm run lint
```

## 10. 注意事项与常见错误

- **配置冲突**：与 Prettier 的配置可能冲突，需要使用 `eslint-config-prettier`
- **性能考虑**：大型项目检查可能较慢，需要配置忽略文件
- **规则选择**：根据项目需求选择合适的规则，不要过度严格
- **类型检查**：TypeScript 项目需要配置类型检查规则
- **持续更新**：定期更新 ESLint 和插件

## 11. 常见问题 (FAQ)

**Q: ESLint 和 Prettier 如何配合使用？**
A: 使用 `eslint-config-prettier` 禁用冲突规则，使用 `eslint-plugin-prettier` 集成 Prettier。

**Q: 如何忽略某些文件？**
A: 使用 `.eslintignore` 文件或 `ignorePatterns` 配置。

**Q: 如何自定义规则？**
A: 在 `rules` 中配置规则，或创建自定义插件。

## 12. 最佳实践

- **使用预设**：使用推荐的预设配置
- **渐进式采用**：逐步引入规则，不要一次性启用所有规则
- **团队协作**：配置文件应该提交到版本控制
- **自动修复**：配置自动修复，提高效率
- **持续改进**：根据项目需求调整规则

## 13. 对比分析：ESLint 配置方式

| 配置方式     | 说明                                     | 适用场景                       |
|:-------------|:-----------------------------------------|:-------------------------------|
| **.eslintrc.js**| JavaScript 配置文件                  | 需要动态配置                   |
| **.eslintrc.json**| JSON 配置文件                      | 简单配置                       |
| **eslint.config.js**| 扁平配置（ESLint 9+）            | 现代项目，ESLint 9+            |
| **package.json**| 在 package.json 中配置            | 简单项目                       |

## 14. 练习任务

1. **ESLint 基础实践**：
   - 配置 ESLint
   - 理解规则和配置
   - 运行代码检查

2. **TypeScript 集成实践**：
   - 配置 TypeScript 支持
   - 配置类型检查规则
   - 解决常见问题

3. **Prettier 集成实践**：
   - 集成 Prettier
   - 解决配置冲突
   - 配置自动修复

4. **实际应用**：
   - 在实际项目中应用 ESLint
   - 配置团队规则
   - 集成到开发流程

完成以上练习后，继续学习下一节：Prettier 配置。

## 总结

ESLint 是代码质量检查的重要工具：

- **核心功能**：错误检测、代码风格检查、自动修复
- **使用场景**：开发时检查、编辑器集成、CI/CD 集成
- **最佳实践**：使用预设、渐进式采用、团队协作

掌握 ESLint 有助于保证代码质量。

---

**最后更新**：2025-01-XX
