# 3.2.2 Vite（现代构建工具）

## 1. 概述

Vite 是一个现代的前端构建工具，由 Vue.js 作者尤雨溪开发。Vite 基于原生 ES Modules，提供了极快的开发服务器启动速度和热模块替换（HMR）。理解 Vite 的使用对于现代 Node.js 和前端开发非常重要。

## 2. 特性说明

- **极速启动**：基于原生 ES Modules，无需打包即可启动开发服务器。
- **快速 HMR**：精确的 HMR，只更新修改的模块。
- **生产优化**：使用 Rollup 进行生产构建，代码分割和优化。
- **TypeScript 支持**：开箱即用的 TypeScript 支持。
- **插件生态**：丰富的插件生态系统。

## 3. 安装与配置

### 安装 Vite

```bash
# 创建 Vite 项目
npm create vite@latest my-app -- --template vanilla-ts

# 或手动安装
npm install -D vite
```

### 基本配置

```ts
// 文件: vite.config.ts
// 功能: Vite 基本配置

import { defineConfig } from 'vite';

export default defineConfig({
    root: './src',
    build: {
        outDir: '../dist',
        emptyOutDir: true
    },
    server: {
        port: 3000,
        open: true
    }
});
```

## 4. 基本用法

### 示例 1：开发服务器

```bash
# 文件: vite-dev.sh
# 功能: 启动 Vite 开发服务器

# 启动开发服务器
npm run dev

# 或直接使用
npx vite
```

package.json 配置：

```json
{
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  }
}
```

### 示例 2：生产构建

```bash
# 文件: vite-build.sh
# 功能: Vite 生产构建

# 构建生产版本
npm run build

# 预览生产构建
npm run preview
```

### 示例 3：TypeScript 项目配置

```ts
// 文件: vite.config.ts
// 功能: TypeScript 项目配置

import { defineConfig } from 'vite';
import { resolve } from 'node:path';

export default defineConfig({
    resolve: {
        alias: {
            '@': resolve(__dirname, './src')
        }
    },
    build: {
        target: 'node18',
        lib: {
            entry: resolve(__dirname, 'src/index.ts'),
            name: 'MyLib',
            fileName: 'my-lib',
            formats: ['es', 'cjs']
        }
    }
});
```

## 5. 参数说明：Vite 配置选项

### 基本配置

| 配置项       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **root**     | String   | 项目根目录                               | `'./src'`                      |
| **base**     | String   | 公共基础路径                             | `'/my-app/'`                   |
| **build.outDir**| String | 构建输出目录                           | `'dist'`                        |
| **server.port**| Number | 开发服务器端口                         | `3000`                          |
| **server.open**| Boolean | 启动时自动打开浏览器                  | `true`                          |

### 构建配置

| 配置项       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **build.target**| String | 构建目标（ES 版本）                   | `'node18'`, `'es2020'`         |
| **build.minify**| String | 压缩工具                               | `'esbuild'`, `'terser'`        |
| **build.sourcemap**| Boolean | 生成 source map                    | `true`                          |

## 6. 返回值与状态说明

Vite 操作的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **开发服务器**| 服务器实例  | 启动开发服务器，提供 HMR 功能            |
| **构建**     | 成功/失败    | 构建成功或失败，显示构建信息             |

## 7. 代码示例：完整的 Vite 配置

以下示例演示了完整的 Vite 配置：

```ts
// 文件: vite.config.ts
// 功能: 完整的 Vite 配置

import { defineConfig } from 'vite';
import { resolve } from 'node:path';

export default defineConfig({
    // 项目根目录
    root: './src',
    
    // 公共基础路径
    base: '/',
    
    // 开发服务器配置
    server: {
        port: 3000,
        open: true,
        cors: true,
        proxy: {
            '/api': {
                target: 'http://localhost:8080',
                changeOrigin: true,
                rewrite: (path: string): string => path.replace(/^\/api/, '')
            }
        }
    },
    
    // 构建配置
    build: {
        outDir: '../dist',
        emptyOutDir: true,
        target: 'node18',
        sourcemap: true,
        minify: 'esbuild',
        rollupOptions: {
            input: {
                main: resolve(__dirname, 'src/index.ts')
            },
            output: {
                format: 'es',
                entryFileNames: '[name].js',
                chunkFileNames: '[name]-[hash].js'
            }
        }
    },
    
    // 路径别名
    resolve: {
        alias: {
            '@': resolve(__dirname, './src'),
            '@utils': resolve(__dirname, './src/utils')
        }
    },
    
    // 环境变量
    envPrefix: 'VITE_'
});
```

## 8. 输出结果说明

Vite 构建的输出结果：

```text
vite v5.0.0 building for production...
✓ 50 modules transformed.
dist/index.js  10.5 kB
dist/index.css  2.3 kB
built in 1.2s
```

**逻辑解析**：
- 显示 Vite 版本
- 显示构建模式
- 显示转换的模块数量
- 显示输出文件大小
- 显示构建时间

## 9. 使用场景

### 1. 前端项目

构建前端项目：

```bash
# 创建前端项目
npm create vite@latest my-frontend -- --template react-ts

# 开发
npm run dev

# 构建
npm run build
```

### 2. 全栈项目

构建全栈项目：

```ts
// vite.config.ts
export default defineConfig({
    build: {
        target: 'node18',
        lib: {
            entry: 'src/index.ts',
            formats: ['es', 'cjs']
        }
    }
});
```

### 3. 库开发

构建库：

```ts
// vite.config.ts
export default defineConfig({
    build: {
        lib: {
            entry: 'src/index.ts',
            name: 'MyLib',
            fileName: 'my-lib',
            formats: ['es', 'cjs', 'umd']
        }
    }
});
```

## 10. 注意事项与常见错误

- **ES Modules**：Vite 基于 ES Modules，确保代码使用 ESM
- **路径别名**：配置路径别名需要在 tsconfig.json 中也配置
- **环境变量**：环境变量需要以 `VITE_` 开头才能在客户端访问
- **插件兼容**：注意插件的兼容性
- **生产构建**：生产构建使用 Rollup，配置方式可能不同

## 11. 常见问题 (FAQ)

**Q: Vite 和 Webpack 有什么区别？**
A: Vite 基于 ES Modules，开发时无需打包，速度快；Webpack 需要打包，但功能更强大。

**Q: 如何在 Vite 中使用环境变量？**
A: 环境变量需要以 `VITE_` 开头，通过 `import.meta.env.VITE_XXX` 访问。

**Q: Vite 支持 CommonJS 吗？**
A: 开发时支持，但生产构建时建议使用 ES Modules。

## 12. 最佳实践

- **使用 TypeScript**：使用 TypeScript 配置文件
- **路径别名**：配置路径别名提高开发效率
- **环境变量**：使用环境变量管理配置
- **代码分割**：合理配置代码分割
- **生产优化**：启用压缩、优化等生产特性

## 13. 对比分析：Vite vs Webpack

| 维度             | Vite                                    | Webpack                                |
|:-----------------|:----------------------------------------|:---------------------------------------|
| **开发速度**     | 极快（无需打包）                        | 中等（需要打包）                       |
| **HMR 速度**     | 快（精确更新）                          | 中等（全量更新）                       |
| **配置复杂度**   | 简单                                    | 复杂                                   |
| **生态支持**     | 良好                                    | 非常丰富                               |
| **适用场景**     | 现代前端项目、全栈项目                  | 复杂项目、需要高度定制                 |

## 14. 练习任务

1. **Vite 基础实践**：
   - 创建 Vite 项目
   - 配置开发服务器
   - 理解 HMR 机制

2. **构建配置实践**：
   - 配置生产构建
   - 配置路径别名
   - 配置环境变量

3. **实际应用**：
   - 在实际项目中应用 Vite
   - 优化构建配置
   - 提升开发体验

完成以上练习后，继续学习下一节：Turbopack（Next.js 构建工具）。

## 总结

Vite 是现代快速构建工具：

- **核心优势**：极速启动、快速 HMR、生产优化
- **适用场景**：现代前端项目、全栈项目、库开发
- **最佳实践**：使用 TypeScript、配置路径别名、环境变量管理

掌握 Vite 有助于提高开发效率和构建性能。

---

**最后更新**：2025-01-XX
