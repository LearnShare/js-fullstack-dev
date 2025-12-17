# 1.1.2 tsconfig.json 详解

## 概述

`tsconfig.json` 是 TypeScript 项目的配置文件，用于指定编译选项、文件包含和排除规则等。本节详细介绍 `tsconfig.json` 的结构和配置项。

## 创建 tsconfig.json

### 自动生成

使用 `tsc --init` 命令自动生成 `tsconfig.json`：

```bash
tsc --init
```

这会创建一个包含所有配置选项和注释的 `tsconfig.json` 文件。

### 手动创建

手动创建 `tsconfig.json` 文件：

```json
{
  "compilerOptions": {},
  "include": ["src/**/*"],
  "exclude": ["node_modules"]
}
```

## 配置文件结构

### 基本结构

```json
{
  "compilerOptions": {
    // 编译器选项
  },
  "include": [
    // 包含的文件
  ],
  "exclude": [
    // 排除的文件
  ],
  "files": [
    // 明确指定的文件
  ],
  "extends": "./base.json",
  "references": [
    // 项目引用
  ]
}
```

### compilerOptions

`compilerOptions` 是核心配置选项，包含编译器的各种设置。

### include

指定要包含的文件或目录，使用 glob 模式：

```json
{
  "include": [
    "src/**/*",
    "tests/**/*"
  ]
}
```

### exclude

指定要排除的文件或目录：

```json
{
  "exclude": [
    "node_modules",
    "dist",
    "**/*.test.ts"
  ]
}
```

### files

明确指定要编译的文件列表（不推荐，使用 include 更灵活）：

```json
{
  "files": [
    "src/index.ts",
    "src/app.ts"
  ]
}
```

### extends

继承其他配置文件：

```json
{
  "extends": "./tsconfig.base.json",
  "compilerOptions": {
    "outDir": "./dist"
  }
}
```

### references

项目引用（用于多项目结构）：

```json
{
  "references": [
    { "path": "./core" },
    { "path": "./utils" }
  ]
}
```

## 常用配置示例

### 基础配置

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "lib": ["ES2020"],
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

### Node.js 项目配置

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "lib": ["ES2020"],
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist", "**/*.test.ts"]
}
```

### 浏览器项目配置

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx"
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

## 配置继承

### 基础配置（tsconfig.base.json）

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  }
}
```

### 扩展配置（tsconfig.json）

```json
{
  "extends": "./tsconfig.base.json",
  "compilerOptions": {
    "outDir": "./dist",
    "rootDir": "./src"
  },
  "include": ["src/**/*"]
}
```

## 多项目配置

### 项目结构

```
project/
  tsconfig.json
  core/
    tsconfig.json
  utils/
    tsconfig.json
  app/
    tsconfig.json
```

### 根配置（tsconfig.json）

```json
{
  "files": [],
  "references": [
    { "path": "./core" },
    { "path": "./utils" },
    { "path": "./app" }
  ]
}
```

### 子项目配置（core/tsconfig.json）

```json
{
  "compilerOptions": {
    "composite": true,
    "outDir": "./dist"
  },
  "include": ["src/**/*"]
}
```

## 配置文件优先级

1. 命令行选项（最高优先级）
2. tsconfig.json 中的配置
3. 继承的配置文件
4. 默认值（最低优先级）

## 注意事项

1. **文件路径**：使用相对路径或绝对路径
2. **glob 模式**：使用标准的 glob 模式匹配文件
3. **配置合并**：extends 会合并配置，子配置会覆盖父配置
4. **项目引用**：使用 composite 模式需要启用 `composite: true`

## 最佳实践

1. **使用 extends**：创建基础配置，其他配置继承
2. **明确 include/exclude**：明确指定包含和排除的文件
3. **项目引用**：大型项目使用项目引用管理
4. **配置分离**：不同环境使用不同的配置文件

## 练习

1. **创建配置**：使用 `tsc --init` 创建 tsconfig.json。

2. **配置实践**：根据项目类型（Node.js 或浏览器）配置 tsconfig.json。

3. **配置继承**：创建基础配置，并使用 extends 继承。

4. **多项目配置**：尝试配置多项目结构。

5. **配置验证**：使用 `tsc --showConfig` 查看最终配置。

完成以上练习后，继续学习下一节，了解编译器选项。

## 总结

`tsconfig.json` 是 TypeScript 项目的核心配置文件。通过合理配置 `tsconfig.json`，可以控制编译行为、指定文件包含规则、管理多项目结构等。理解 `tsconfig.json` 的结构和配置项是使用 TypeScript 的基础。

## 相关资源

- [TypeScript tsconfig.json 文档](https://www.typescriptlang.org/tsconfig)
