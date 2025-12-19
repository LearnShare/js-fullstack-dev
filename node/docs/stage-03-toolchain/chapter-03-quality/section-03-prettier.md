# 3.3.3 Prettier 配置

## 1. 概述

Prettier 是一个代码格式化工具，用于自动格式化代码，保持代码风格一致。Prettier 支持多种语言，包括 JavaScript、TypeScript、JSON、CSS 等。理解 Prettier 的使用对于保持代码风格一致非常重要。

## 2. 特性说明

- **自动格式化**：自动格式化代码，无需手动调整。
- **多语言支持**：支持 JavaScript、TypeScript、JSON、CSS、Markdown 等。
- **配置简单**：配置简单，开箱即用。
- **团队协作**：保证团队代码风格一致。
- **编辑器集成**：可以集成到编辑器中，保存时自动格式化。

## 3. 安装与配置

### 安装 Prettier

```bash
# 安装 Prettier
npm install -D prettier
```

### 基本配置

```json
// 文件: .prettierrc.json
// 功能: Prettier 基本配置

{
  "semi": true,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "es5",
  "printWidth": 80
}
```

## 4. 基本用法

### 示例 1：格式化文件

```bash
# 文件: prettier-format.sh
# 功能: Prettier 格式化

# 格式化所有文件
npx prettier --write "src/**/*.{ts,js,json}"

# 检查格式（不修改）
npx prettier --check "src/**/*.{ts,js,json}"
```

package.json 配置：

```json
{
  "scripts": {
    "format": "prettier --write \"src/**/*.{ts,js,json}\"",
    "format:check": "prettier --check \"src/**/*.{ts,js,json}\""
  }
}
```

### 示例 2：完整配置

```json
// 文件: .prettierrc.json
// 功能: Prettier 完整配置

{
  "semi": true,
  "singleQuote": true,
  "tabWidth": 2,
  "useTabs": false,
  "trailingComma": "es5",
  "printWidth": 80,
  "arrowParens": "always",
  "endOfLine": "lf",
  "bracketSpacing": true,
  "bracketSameLine": false
}
```

### 示例 3：忽略文件

```text
// 文件: .prettierignore
// 功能: Prettier 忽略文件

node_modules/
dist/
build/
*.min.js
package-lock.json
```

## 5. 参数说明：Prettier 配置选项

### 基本配置

| 配置项           | 类型     | 说明                                     | 示例                           |
|:-----------------|:---------|:-----------------------------------------|:-------------------------------|
| **semi**         | Boolean  | 是否使用分号                             | `true`                         |
| **singleQuote**  | Boolean  | 是否使用单引号                           | `true`                         |
| **tabWidth**     | Number   | 缩进宽度（空格数）                       | `2`                            |
| **useTabs**      | Boolean  | 是否使用 Tab                             | `false`                        |
| **trailingComma**| String   | 尾随逗号（"none"、"es5"、"all"）         | `"es5"`                         |
| **printWidth**   | Number   | 每行最大字符数                           | `80`                            |

## 6. 返回值与状态说明

Prettier 操作的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **格式化**   | 成功/失败    | 格式化代码，显示修改的文件               |
| **检查**     | 成功/失败    | 检查格式，显示不符合格式的文件           |

## 7. 代码示例：Prettier 工作流

以下示例演示了 Prettier 的完整工作流：

```bash
# 文件: prettier-workflow.sh
# 功能: Prettier 完整工作流

# 1. 格式化所有文件
npm run format

# 2. 检查格式（CI/CD）
npm run format:check

# 3. 格式化特定文件
npx prettier --write src/index.ts

# 4. 格式化并检查
npx prettier --write --check "src/**/*.{ts,js}"
```

## 8. 输出结果说明

Prettier 格式化的输出结果：

```text
src/index.ts
src/utils/helper.ts
✨ 2 files formatted
```

**逻辑解析**：
- 显示格式化的文件列表
- 显示格式化结果统计

## 9. 使用场景

### 1. 开发时格式化

在开发时自动格式化：

```json
// .vscode/settings.json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode"
}
```

### 2. 提交前格式化

在提交代码前格式化：

```bash
# 使用 pre-commit 钩子
npx husky add .husky/pre-commit "npm run format"
```

### 3. CI/CD 集成

在 CI/CD 中检查格式：

```yaml
# .github/workflows/ci.yml
- name: Check Format
  run: npm run format:check
```

## 10. 注意事项与常见错误

- **配置冲突**：与 ESLint 的配置可能冲突，需要使用 `eslint-config-prettier`
- **文件忽略**：使用 `.prettierignore` 忽略不需要格式化的文件
- **团队协作**：配置文件应该提交到版本控制
- **性能考虑**：大型项目格式化可能较慢
- **持续更新**：定期更新 Prettier

## 11. 常见问题 (FAQ)

**Q: Prettier 和 ESLint 有什么区别？**
A: Prettier 只格式化代码，ESLint 检查代码质量和风格。两者可以配合使用。

**Q: 如何忽略某些文件？**
A: 使用 `.prettierignore` 文件，类似 `.gitignore`。

**Q: 如何配置编辑器自动格式化？**
A: 在编辑器设置中启用 `formatOnSave`，并设置 Prettier 为默认格式化器。

## 12. 最佳实践

- **统一配置**：团队使用统一的配置文件
- **自动格式化**：配置保存时自动格式化
- **CI/CD 检查**：在 CI/CD 中检查格式
- **文档说明**：为配置选项提供文档说明
- **持续改进**：根据项目需求调整配置

## 13. 对比分析：Prettier vs 其他格式化工具

| 维度             | Prettier                                | ESLint (格式化)                        |
|:-----------------|:----------------------------------------|:---------------------------------------|
| **功能**         | 专门格式化                              | 检查 + 格式化                          |
| **配置**         | 简单                                    | 复杂                                   |
| **性能**         | 快                                      | 中等                                   |
| **推荐使用**     | ✅ 推荐（专门格式化）                   | 检查使用 ESLint，格式化使用 Prettier   |

## 14. 练习任务

1. **Prettier 基础实践**：
   - 配置 Prettier
   - 格式化代码
   - 理解配置选项

2. **编辑器集成实践**：
   - 配置编辑器自动格式化
   - 配置保存时格式化
   - 测试格式化功能

3. **实际应用**：
   - 在实际项目中应用 Prettier
   - 配置团队规则
   - 集成到开发流程

完成以上练习后，继续学习下一节：TypeScript 类型检查。

## 总结

Prettier 是代码格式化的重要工具：

- **核心功能**：自动格式化、多语言支持、团队协作
- **使用场景**：开发时格式化、提交前格式化、CI/CD 检查
- **最佳实践**：统一配置、自动格式化、CI/CD 检查

掌握 Prettier 有助于保持代码风格一致。

---

**最后更新**：2025-01-XX
