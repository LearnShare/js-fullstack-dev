# 8.6.3 Turbopack + TypeScript

## 概述

Turbopack 是 Next.js 团队开发的快速构建工具，与 TypeScript 集成良好。本节介绍 Turbopack + TypeScript 的配置。

## 安装

```bash
npm install --save-dev turbopack typescript
```

## 配置

### 1. tsconfig.json

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "strict": true
  }
}
```

### 2. 使用 Turbopack

Turbopack 通常与 Next.js 一起使用：

```bash
next dev --turbo
```

## 使用场景

### 1. Next.js 项目

Next.js 项目使用 Turbopack：

```bash
next dev --turbo
next build --turbo
```

### 2. 大型项目

大型项目使用 Turbopack 提高构建速度：

```bash
# 使用 Turbopack
npm run dev --turbo
```

## 注意事项

1. **Next.js**：Turbopack 主要与 Next.js 一起使用
2. **模块解析**：使用 `bundler` 模块解析
3. **配置正确**：确保 TypeScript 配置正确

## 最佳实践

1. **使用 Turbopack**：Next.js 项目使用 Turbopack
2. **配置正确**：确保 TypeScript 配置正确
3. **性能优化**：利用 Turbopack 的性能优势

## 练习

1. **Turbopack 配置**：配置 Turbopack + TypeScript。

2. **项目使用**：在实际项目中使用 Turbopack。

3. **实际应用**：在实际项目中应用 Turbopack 配置。

完成以上练习后，与构建工具集成章节学习完成。阶段八学习完成。

## 总结

Turbopack 是 Next.js 团队开发的快速构建工具，与 TypeScript 集成良好。配置 tsconfig.json，使用 `bundler` 模块解析。理解 Turbopack + TypeScript 的配置是学习构建工具集成的关键。

## 相关资源

- [Turbopack 文档](https://turbo.build/pack)
- [Next.js + Turbopack](https://nextjs.org/docs/app/api-reference/next-config-js/turbopack)
