# 3.3.4 TypeScript 类型检查

## 1. 概述

TypeScript 提供了强大的类型系统，可以在编译时检查类型错误。除了编译时的类型检查，还可以在开发时和 CI/CD 中进行类型检查，不生成文件。理解 TypeScript 类型检查的配置对于保证类型安全至关重要。

## 2. 特性说明

- **类型检查**：检查类型错误，提供类型安全。
- **编译时检查**：在编译时发现类型错误。
- **开发时检查**：在开发时进行类型检查，不生成文件。
- **严格模式**：支持严格类型检查模式。
- **增量检查**：支持增量类型检查，提高性能。

## 3. 安装与配置

### TypeScript 已安装

TypeScript 通常已经作为项目依赖安装：

```bash
# 检查 TypeScript 版本
npx tsc --version
```

### 类型检查配置

```json
// 文件: tsconfig.json
// 功能: TypeScript 类型检查配置

{
  "compilerOptions": {
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true
  }
}
```

## 4. 基本用法

### 示例 1：类型检查（不生成文件）

```bash
# 文件: type-check.sh
# 功能: TypeScript 类型检查

# 类型检查（不生成文件）
npx tsc --noEmit

# 类型检查（严格模式）
npx tsc --noEmit --strict
```

package.json 配置：

```json
{
  "scripts": {
    "type-check": "tsc --noEmit",
    "type-check:watch": "tsc --noEmit --watch"
  }
}
```

### 示例 2：严格类型检查配置

```json
// 文件: tsconfig.json
// 功能: 严格类型检查配置

{
  "compilerOptions": {
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true
  }
}
```

### 示例 3：增量类型检查

```json
// 文件: tsconfig.json
// 功能: 增量类型检查配置

{
  "compilerOptions": {
    "incremental": true,
    "tsBuildInfoFile": ".tsbuildinfo"
  }
}
```

## 5. 参数说明：TypeScript 类型检查选项

### 类型检查选项

| 选项                 | 类型     | 说明                                     | 示例                           |
|:---------------------|:---------|:-----------------------------------------|:-------------------------------|
| **--noEmit**         | Flag     | 只检查类型，不生成文件                   | `tsc --noEmit`                 |
| **--strict**         | Flag     | 启用所有严格类型检查选项                 | `tsc --strict`                |
| **--noUnusedLocals** | Boolean  | 检查未使用的局部变量                     | `true`                         |
| **--noUnusedParameters**| Boolean | 检查未使用的参数                     | `true`                         |
| **--noImplicitReturns**| Boolean | 检查函数隐式返回                     | `true`                         |

## 6. 返回值与状态说明

TypeScript 类型检查的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **类型检查** | 成功/错误    | 显示类型错误和警告                       |

## 7. 代码示例：完整的类型检查配置

以下示例演示了完整的类型检查配置：

```json
// 文件: tsconfig.json
// 功能: 完整的类型检查配置

{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "lib": ["ES2022"],
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    
    // 类型检查选项
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    
    // 增量检查
    "incremental": true,
    "tsBuildInfoFile": ".tsbuildinfo"
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

## 8. 输出结果说明

TypeScript 类型检查的输出结果：

```text
src/index.ts:5:10 - error TS6133: 'unusedVar' is declared but its value is never read.

src/utils/helper.ts:8:5 - error TS7030: Not all code paths return a value.

✖ Found 2 errors.
```

**逻辑解析**：
- 显示文件路径和行号
- 显示错误代码和描述
- 显示错误统计

## 9. 使用场景

### 1. 开发时检查

在开发时进行类型检查：

```bash
# 类型检查（watch 模式）
npm run type-check:watch
```

### 2. 提交前检查

在提交代码前检查类型：

```bash
# 使用 pre-commit 钩子
npx husky add .husky/pre-commit "npm run type-check"
```

### 3. CI/CD 集成

在 CI/CD 中检查类型：

```yaml
# .github/workflows/ci.yml
- name: Type Check
  run: npm run type-check
```

## 10. 注意事项与常见错误

- **严格模式**：启用严格模式可能发现很多错误，需要逐步修复
- **性能考虑**：大型项目类型检查可能较慢，使用增量检查
- **配置一致性**：确保开发和生产使用相同的配置
- **类型定义**：确保所有依赖都有类型定义
- **持续更新**：定期更新 TypeScript

## 11. 常见问题 (FAQ)

**Q: --noEmit 和正常编译有什么区别？**
A: `--noEmit` 只检查类型，不生成文件；正常编译会生成 JavaScript 文件。

**Q: 如何启用严格类型检查？**
A: 在 `tsconfig.json` 中设置 `"strict": true`，或使用 `--strict` 标志。

**Q: 类型检查很慢怎么办？**
A: 使用增量检查（`"incremental": true`），或使用 `tsc --incremental`。

## 12. 最佳实践

- **严格模式**：启用严格类型检查，提高类型安全
- **增量检查**：使用增量检查提高性能
- **自动化**：集成到开发流程中，自动化检查
- **持续改进**：逐步修复类型错误，提高类型覆盖率
- **文档说明**：为类型定义提供文档说明

## 13. 对比分析：类型检查方式

| 方式             | 说明                                     | 适用场景                       |
|:-------------|:-----------------------------------------|:-------------------------------|
| **编译时检查** | 编译时自动检查类型                       | 正常编译流程                   |
| **开发时检查** | 使用 `--noEmit` 只检查类型              | 开发时快速检查                 |
| **编辑器检查** | 编辑器实时显示类型错误                   | 开发时实时反馈                 |
| **CI/CD 检查** | 在 CI/CD 中检查类型                      | 保证代码质量                   |

## 14. 练习任务

1. **类型检查实践**：
   - 配置 TypeScript 类型检查
   - 理解类型检查选项
   - 运行类型检查

2. **严格模式实践**：
   - 启用严格类型检查
   - 修复类型错误
   - 提高类型覆盖率

3. **实际应用**：
   - 在实际项目中应用类型检查
   - 配置自动化检查
   - 提升类型安全

完成以上练习后，继续学习下一章：Monorepo 管理。

## 总结

TypeScript 类型检查是保证类型安全的重要工具：

- **核心功能**：类型检查、严格模式、增量检查
- **使用场景**：开发时检查、提交前检查、CI/CD 集成
- **最佳实践**：严格模式、增量检查、自动化

掌握 TypeScript 类型检查有助于提高类型安全。

---

**最后更新**：2025-01-XX
