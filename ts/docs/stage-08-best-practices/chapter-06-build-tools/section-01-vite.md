# 8.6.1 Vite + TypeScript

## 概述

Vite 是一个快速的构建工具，与 TypeScript 集成良好。本节介绍 Vite + TypeScript 的配置。

## 安装

```bash
npm install --save-dev vite typescript
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

### 2. vite.config.ts

```ts
import { defineConfig } from "vite";

export default defineConfig({
    // Vite 配置
});
```

## 使用场景

### 1. 前端项目

前端项目使用 Vite + TypeScript：

```bash
npm run dev
npm run build
```

### 2. 库开发

库开发使用 Vite + TypeScript：

```ts
// vite.config.ts
import { defineConfig } from "vite";

export default defineConfig({
    build: {
        lib: {
            entry: "./src/index.ts",
            formats: ["es", "cjs"]
        }
    }
});
```

## 注意事项

1. **模块解析**：使用 `bundler` 模块解析
2. **类型检查**：Vite 不进行类型检查，需要单独运行
3. **配置正确**：确保 tsconfig.json 配置正确

## 最佳实践

1. **使用 Vite**：前端项目使用 Vite
2. **配置正确**：确保 TypeScript 配置正确
3. **类型检查**：单独运行类型检查

## 练习

1. **Vite 配置**：配置 Vite + TypeScript。

2. **项目使用**：在实际项目中使用 Vite。

3. **实际应用**：在实际项目中应用 Vite 配置。

完成以上练习后，继续学习下一节，了解 Webpack + TypeScript。

## 总结

Vite 是一个快速的构建工具，与 TypeScript 集成良好。配置 tsconfig.json 和 vite.config.ts，使用 `bundler` 模块解析。理解 Vite + TypeScript 的配置是学习构建工具集成的关键。

## 相关资源

- [Vite 文档](https://vitejs.dev/)
- [Vite + TypeScript](https://vitejs.dev/guide/features.html#typescript)
