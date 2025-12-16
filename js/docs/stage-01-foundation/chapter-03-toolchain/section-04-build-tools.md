# 1.2.4 构建工具（Vite、Webpack、Turbopack）

## 概述

构建工具用于编译、打包和优化代码。本节介绍主流构建工具的配置和使用，包括 Vite、Webpack 和 Turbopack。

## Vite

### Vite 简介

Vite 是新一代的前端构建工具，由 Vue.js 作者开发，专注于提供极快的开发体验。

### 主要特点

- **极快的开发服务器启动**：基于 ES Modules
- **快速的热更新（HMR）**：只更新修改的模块
- **优化的生产构建**：使用 Rollup 打包
- **开箱即用**：支持 TypeScript、JSX、CSS 预处理器等

### 安装

```bash
# 使用 npm
npm create vite@latest my-project

# 使用 pnpm
pnpm create vite my-project

# 使用 yarn
yarn create vite my-project
```

### 基本配置

创建 `vite.config.js`：

```js
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    open: true
  },
  build: {
    outDir: 'dist',
    sourcemap: true
  }
});
```

### 使用示例

```bash
# 开发模式
npm run dev

# 生产构建
npm run build

# 预览生产构建
npm run preview
```

## Webpack

### Webpack 简介

Webpack 是一个模块打包器，将各种资源打包成静态资源。

### 主要特点

- **代码分割**：按需加载
- **模块热替换（HMR）**：开发时热更新
- **插件系统**：丰富的插件生态
- **广泛的社区支持**：成熟的生态系统

### 安装

```bash
# 安装 webpack 和 webpack-cli
npm install --save-dev webpack webpack-cli
```

### 基本配置

创建 `webpack.config.js`：

```js
const path = require('path');

module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist')
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader'
        }
      }
    ]
  },
  plugins: [],
  devServer: {
    contentBase: './dist',
    hot: true
  }
};
```

### 使用示例

```bash
# 开发模式
npm run dev

# 生产构建
npm run build
```

## Turbopack

### Turbopack 简介

Turbopack 是 Next.js 团队开发的下一代构建工具，使用 Rust 编写。

### 主要特点

- **极快的构建速度**：使用 Rust 编写
- **增量编译**：只编译修改的部分
- **与 Webpack 兼容**：可以逐步迁移
- **专为大型项目优化**：适合大型应用

### 使用

Turbopack 目前主要用于 Next.js 项目：

```bash
# 使用 Turbopack 运行 Next.js
next dev --turbo
```

## 构建工具对比

### 性能对比

| 特性                 | Vite   | Webpack | Turbopack |
|:---------------------|:-------|:--------|:----------|
| **开发服务器启动**   | 极快   | 中等    | 极快      |
| **HMR 速度**         | 极快   | 快      | 极快      |
| **生产构建**         | 快     | 快      | 极快      |
| **大型项目**         | 良好   | 优秀    | 优秀      |

### 功能对比

| 特性                 | Vite       | Webpack    | Turbopack  |
|:---------------------|:-----------|:-----------|:-----------|
| **配置复杂度**       | 简单       | 复杂       | 中等       |
| **插件生态**         | 丰富       | 非常丰富   | 有限       |
| **TypeScript 支持**  | 开箱即用   | 需要配置   | 开箱即用   |
| **代码分割**         | 支持       | 支持       | 支持       |

### 选择建议

#### 选择 Vite

- 新项目
- 需要快速开发体验
- 中小型项目
- Vue/React 项目

#### 选择 Webpack

- 大型项目
- 需要复杂配置
- 需要丰富的插件
- 已有 Webpack 项目

#### 选择 Turbopack

- Next.js 项目
- 大型项目
- 需要极快构建速度
- 实验性项目

## 生产构建优化

### 代码分割

**说明**：代码分割可以将代码拆分为多个小块，按需加载，减少初始加载时间。

**Vite 配置**：

```js
// vite.config.js
export default defineConfig({
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
          utils: ['./src/utils']
        }
      }
    }
  }
});
```

**Webpack 配置**：

```js
// webpack.config.js
module.exports = {
  optimization: {
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          chunks: 'all'
        }
      }
    }
  }
};
```

### Tree Shaking

**说明**：Tree Shaking 可以移除未使用的代码，减少打包体积。

**Vite**：自动启用 Tree Shaking

**Webpack**：在生产模式下自动启用

```js
// 只导入需要的函数
import { debounce } from 'lodash-es'; // 只打包 debounce

// 避免导入整个库
import _ from 'lodash'; // 会打包整个库
```

### 缓存策略

**说明**：使用文件哈希命名，实现长期缓存。

**Vite 配置**：

```js
export default defineConfig({
  build: {
    rollupOptions: {
      output: {
        entryFileNames: 'assets/[name].[hash].js',
        chunkFileNames: 'assets/[name].[hash].js',
        assetFileNames: 'assets/[name].[hash].[ext]'
      }
    }
  }
});
```

**Webpack 配置**：

```js
module.exports = {
  output: {
    filename: '[name].[contenthash].js',
    chunkFilename: '[name].[contenthash].chunk.js'
  }
};
```

### CSS 处理

**说明**：提取 CSS 到独立文件，压缩 CSS。

**Vite**：自动提取和压缩 CSS

**Webpack 配置**：

```js
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  plugins: [
    new MiniCssExtractPlugin({
      filename: '[name].[contenthash].css'
    })
  ],
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [MiniCssExtractPlugin.loader, 'css-loader']
      }
    ]
  }
};
```

### 图片处理

**说明**：压缩图片，使用现代格式（WebP）。

**Vite 配置**：

```js
import { defineConfig } from 'vite';
import { imagetools } from 'vite-imagetools';

export default defineConfig({
  plugins: [imagetools()]
});
```

**Webpack 配置**：

```js
const ImageMinimizerPlugin = require('image-minimizer-webpack-plugin');

module.exports = {
  optimization: {
    minimizer: [
      new ImageMinimizerPlugin({
        minimizer: {
          implementation: ImageMinimizerPlugin.imageminMinify,
          options: {
            plugins: ['imagemin-webp']
          }
        }
      })
    ]
  }
};
```

## 故障排查

### 常见错误

#### 1. 模块未找到

**错误信息**：`Cannot find module 'xxx'`

**原因**：
- 依赖未安装
- 路径错误
- 模块名称拼写错误

**解决方案**：

```bash
# 检查依赖是否安装
npm list xxx

# 重新安装依赖
npm install

# 检查路径是否正确
import xxx from './path/to/xxx';
```

#### 2. 构建失败

**错误信息**：`Build failed with errors`

**原因**：
- 语法错误
- 类型错误（TypeScript）
- 配置错误

**解决方案**：

```bash
# 检查语法错误
npm run lint

# 检查类型错误
npm run type-check

# 查看详细错误信息
npm run build -- --verbose
```

#### 3. HMR 不工作

**错误信息**：热更新不生效

**原因**：
- 配置错误
- 浏览器缓存
- 网络问题

**解决方案**：

```js
// Vite 配置
export default defineConfig({
  server: {
    hmr: {
      overlay: true
    }
  }
});

// 清除浏览器缓存
// 检查网络连接
```

#### 4. 生产构建体积过大

**原因**：
- 未启用 Tree Shaking
- 导入了整个库
- 未压缩代码

**解决方案**：

```js
// 只导入需要的函数
import { debounce } from 'lodash-es';

// 启用压缩
export default defineConfig({
  build: {
    minify: 'terser',
    terserOptions: {
      compress: {
        drop_console: true
      }
    }
  }
});
```

#### 5. 路径别名不工作

**错误信息**：`Cannot resolve '@/utils'`

**原因**：路径别名未配置

**解决方案**：

```js
// Vite 配置
import { resolve } from 'path';

export default defineConfig({
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src')
    }
  }
});

// Webpack 配置
module.exports = {
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src')
    }
  }
};
```

### 调试技巧

#### 1. 查看构建信息

```bash
# Vite
npm run build -- --debug

# Webpack
npm run build -- --stats verbose
```

#### 2. 分析打包体积

```bash
# 安装分析工具
npm install --save-dev vite-bundle-visualizer

# 生成分析报告
npm run build -- --analyze
```

#### 3. 检查配置

```js
// 打印配置
console.log(JSON.stringify(config, null, 2));
```

## 迁移指南

### 从 Webpack 迁移到 Vite

**步骤**：

1. **安装 Vite**：

```bash
npm install --save-dev vite
```

2. **创建配置文件**：

```js
// vite.config.js
import { defineConfig } from 'vite';

export default defineConfig({
  // 迁移配置
});
```

3. **更新脚本**：

```json
{
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  }
}
```

4. **迁移插件**：查找 Vite 对应的插件

5. **测试**：逐步测试功能

### 从 Vite 迁移到 Turbopack

**说明**：Turbopack 主要用于 Next.js 项目

```bash
# Next.js 中使用 Turbopack
next dev --turbo
```

## 注意事项

### 1. 开发与生产环境差异

- 开发环境：快速启动、HMR
- 生产环境：优化、压缩、代码分割

### 2. 浏览器兼容性

- 配置 Babel 转译
- 使用 Polyfill
- 检查目标浏览器

### 3. 性能优化

- 代码分割
- 懒加载
- 缓存策略
- 压缩资源

### 4. 安全性

- 避免暴露敏感信息
- 使用环境变量
- 检查依赖漏洞

## 最佳实践

1. **选择合适的工具**：根据项目需求选择
2. **优化构建配置**：启用代码分割、Tree Shaking
3. **监控构建性能**：使用分析工具
4. **保持依赖更新**：定期更新构建工具
5. **文档化配置**：记录配置原因和变更

## 练习

1. **基础配置**：
   - 使用 Vite 创建一个新项目
   - 配置开发服务器端口和代理
   - 配置生产构建输出目录

2. **代码分割**：
   - 配置手动代码分割
   - 实现路由级别的代码分割
   - 分析打包体积

3. **优化实践**：
   - 启用 Tree Shaking
   - 配置缓存策略
   - 压缩 CSS 和图片

4. **故障排查**：
   - 模拟常见错误并解决
   - 使用调试工具分析构建
   - 优化构建性能

5. **迁移实践**：
   - 从 Webpack 迁移到 Vite（如果有现有项目）
   - 配置路径别名
   - 迁移插件配置

## 总结

构建工具是现代前端开发的核心工具：

- **Vite**：快速开发体验，适合新项目
- **Webpack**：成熟稳定，适合大型项目
- **Turbopack**：极快构建，适合 Next.js 项目

掌握构建工具的配置和优化是前端开发的重要技能。

继续学习下一节，了解代码质量工具。

---

## 相关资源

- [Vite 官方文档](https://vitejs.dev/)
- [Webpack 官方文档](https://webpack.js.org/)
- [Turbopack 官方文档](https://turbo.build/pack)

---

**最后更新**：2025-12-16
