# 3.2.4 Webpack（传统构建工具）

## 1. 概述

Webpack 是一个功能强大的模块打包器，可以将项目中的各种资源（JavaScript、CSS、图片等）打包成适合浏览器使用的格式。虽然现在有 Vite、Turbopack 等更快的工具，但 Webpack 仍然是最广泛使用的构建工具，特别是在需要高度定制的复杂项目中。

## 2. 特性说明

- **模块打包**：将多个模块打包成单个或多个文件。
- **代码分割**：支持代码分割，按需加载。
- **加载器系统**：通过加载器处理不同类型的文件。
- **插件系统**：丰富的插件生态系统。
- **高度可配置**：支持高度定制和配置。

## 3. 安装与配置

### 安装 Webpack

```bash
# 安装 Webpack
npm install -D webpack webpack-cli

# 安装常用加载器
npm install -D ts-loader css-loader style-loader
```

### 基本配置

```ts
// 文件: webpack.config.ts
// 功能: Webpack 基本配置

import path from 'node:path';
import { Configuration } from 'webpack';

const config: Configuration = {
    entry: './src/index.ts',
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'bundle.js'
    },
    module: {
        rules: [
            {
                test: /\.ts$/,
                use: 'ts-loader',
                exclude: /node_modules/
            }
        ]
    },
    resolve: {
        extensions: ['.ts', '.js']
    }
};

export default config;
```

## 4. 基本用法

### 示例 1：基本构建

```bash
# 文件: webpack-build.sh
# 功能: Webpack 基本构建

# 开发模式构建
npx webpack --mode development

# 生产模式构建
npx webpack --mode production
```

package.json 配置：

```json
{
  "scripts": {
    "build": "webpack --mode production",
    "dev": "webpack --mode development --watch"
  }
}
```

### 示例 2：TypeScript 项目配置

```ts
// 文件: webpack.config.ts
// 功能: TypeScript 项目配置

import path from 'node:path';
import { Configuration } from 'webpack';

const config: Configuration = {
    entry: './src/index.ts',
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'bundle.js',
        clean: true
    },
    module: {
        rules: [
            {
                test: /\.ts$/,
                use: 'ts-loader',
                exclude: /node_modules/
            },
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader']
            }
        ]
    },
    resolve: {
        extensions: ['.ts', '.js'],
        alias: {
            '@': path.resolve(__dirname, 'src')
        }
    },
    devtool: 'source-map'
};

export default config;
```

### 示例 3：开发服务器

```bash
# 安装 webpack-dev-server
npm install -D webpack-dev-server

# 启动开发服务器
npx webpack serve
```

```ts
// webpack.config.ts
const config: Configuration = {
    // ... 其他配置
    devServer: {
        port: 3000,
        open: true,
        hot: true
    }
};
```

## 5. 参数说明：Webpack 配置选项

### 基本配置

| 配置项       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **entry**    | String/Object | 入口文件                             | `'./src/index.ts'`             |
| **output.path**| String | 输出目录                             | `path.resolve(__dirname, 'dist')`|
| **output.filename**| String | 输出文件名                       | `'bundle.js'`                  |
| **mode**     | String   | 模式（development/production）           | `'production'`                 |

### 模块配置

| 配置项       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **module.rules**| Array | 加载器规则                             | `[{ test: /\.ts$/, use: 'ts-loader' }]`|
| **resolve.extensions**| Array | 文件扩展名解析                     | `['.ts', '.js']`               |
| **resolve.alias**| Object | 路径别名                             | `{ '@': './src' }`             |

## 6. 返回值与状态说明

Webpack 操作的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **构建**     | 成功/失败    | 构建成功或失败，显示构建信息             |
| **开发服务器**| 服务器实例  | 启动开发服务器，提供 HMR 功能            |

## 7. 代码示例：完整的 Webpack 配置

以下示例演示了完整的 Webpack 配置：

```ts
// 文件: webpack.config.ts
// 功能: 完整的 Webpack 配置

import path from 'node:path';
import { Configuration } from 'webpack';

const config: Configuration = {
    // 入口文件
    entry: './src/index.ts',
    
    // 输出配置
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'bundle.js',
        clean: true,
        publicPath: '/'
    },
    
    // 模式
    mode: 'production',
    
    // 模块规则
    module: {
        rules: [
            // TypeScript
            {
                test: /\.ts$/,
                use: 'ts-loader',
                exclude: /node_modules/
            },
            // CSS
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader']
            },
            // 图片
            {
                test: /\.(png|jpg|jpeg|gif|svg)$/,
                type: 'asset/resource'
            }
        ]
    },
    
    // 解析配置
    resolve: {
        extensions: ['.ts', '.js', '.json'],
        alias: {
            '@': path.resolve(__dirname, 'src'),
            '@utils': path.resolve(__dirname, 'src/utils')
        }
    },
    
    // 开发工具
    devtool: 'source-map',
    
    // 开发服务器
    devServer: {
        port: 3000,
        open: true,
        hot: true,
        historyApiFallback: true
    },
    
    // 优化配置
    optimization: {
        splitChunks: {
            chunks: 'all'
        }
    }
};

export default config;
```

## 8. 输出结果说明

Webpack 构建的输出结果：

```text
asset bundle.js  245 KiB  [emitted]  [minified]  (name: main)
asset index.html  220 bytes  [emitted]
runtime modules  891 bytes  4 modules
cacheable modules  1.23 MiB  50 modules
webpack 5.89.0 compiled successfully in 2.5s
```

**逻辑解析**：
- 显示输出文件大小
- 显示模块数量
- 显示 Webpack 版本
- 显示构建时间

## 9. 使用场景

### 1. 复杂项目

适合需要高度定制的复杂项目：

```ts
// 复杂项目的 Webpack 配置
const config: Configuration = {
    // 多入口
    entry: {
        main: './src/index.ts',
        admin: './src/admin.ts'
    },
    // 代码分割
    optimization: {
        splitChunks: {
            chunks: 'all'
        }
    }
};
```

### 2. 传统项目

适合需要向后兼容的传统项目：

```ts
// 传统项目的 Webpack 配置
const config: Configuration = {
    target: 'es5',
    output: {
        filename: 'bundle.js'
    }
};
```

### 3. 需要特定插件

适合需要使用特定 Webpack 插件的项目：

```ts
// 使用特定插件
import HtmlWebpackPlugin from 'html-webpack-plugin';

const config: Configuration = {
    plugins: [
        new HtmlWebpackPlugin({
            template: './src/index.html'
        })
    ]
};
```

## 10. 注意事项与常见错误

- **配置复杂度**：Webpack 配置较为复杂，需要理解概念
- **构建速度**：Webpack 构建速度较慢，特别是大型项目
- **插件兼容**：注意插件版本兼容性
- **学习曲线**：Webpack 学习曲线较陡
- **性能优化**：需要配置优化选项提升性能

## 11. 常见问题 (FAQ)

**Q: Webpack 和 Vite 如何选择？**
A: Webpack 适合复杂项目、需要高度定制；Vite 适合现代项目、追求速度。

**Q: 如何优化 Webpack 构建速度？**
A: 使用缓存、并行构建、代码分割、减少插件等。

**Q: Webpack 5 和 Webpack 4 有什么区别？**
A: Webpack 5 改进了缓存、模块联邦、Tree Shaking 等。

## 12. 最佳实践

- **代码分割**：合理配置代码分割，提高加载性能
- **缓存配置**：配置缓存提升构建速度
- **优化配置**：配置优化选项减少包大小
- **插件管理**：合理使用插件，避免过度配置
- **性能监控**：监控构建性能，持续优化

## 13. 对比分析：Webpack vs Vite vs Turbopack

| 维度             | Webpack                                | Vite                                    | Turbopack                              |
|:-----------------|:---------------------------------------|:----------------------------------------|:---------------------------------------|
| **构建速度**     | 中等                                   | 快                                      | 极快                                   |
| **配置复杂度**   | 复杂                                   | 简单                                    | 简单（Next.js 集成）                   |
| **生态支持**     | 非常丰富                               | 良好                                    | Next.js 生态                            |
| **适用场景**     | 复杂项目、需要高度定制                 | 现代前端项目、全栈项目                  | Next.js 项目                            |
| **学习曲线**     | 陡峭                                   | 平缓                                    | 平缓（Next.js 集成）                   |

## 14. 练习任务

1. **Webpack 基础实践**：
   - 配置 Webpack 项目
   - 理解加载器和插件
   - 配置开发服务器

2. **高级配置实践**：
   - 配置代码分割
   - 配置优化选项
   - 配置多入口

3. **实际应用**：
   - 在实际项目中应用 Webpack
   - 优化构建配置
   - 提升构建性能

完成以上练习后，继续学习下一章：代码质量工具。

## 总结

Webpack 是功能强大的构建工具：

- **核心功能**：模块打包、代码分割、加载器系统、插件系统
- **适用场景**：复杂项目、需要高度定制、传统项目
- **最佳实践**：代码分割、缓存配置、优化配置

掌握 Webpack 有助于处理复杂的构建需求。

---

**最后更新**：2025-01-XX
