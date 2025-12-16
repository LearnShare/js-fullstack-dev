# 1.3.4 模块打包与 Tree Shaking

## 概述

模块打包是将多个模块及其依赖打包成可部署的产物（bundle）的过程，目标是提升加载性能、兼容性和可维护性。Tree Shaking 是利用静态分析删除未使用代码的优化技术。本节从原理、工具、配置、性能优化到常见问题，帮助你在实际项目中正确选择和使用打包方案。

## 为什么需要打包

- **浏览器兼容性**：将 ESNext/TypeScript 转译为主流浏览器可执行的代码。
- **依赖管理**：解决模块依赖关系和加载顺序，打平为若干 bundle。
- **性能优化**：压缩、拆分、缓存、懒加载，减少首屏体积与请求次数。
- **资源统一处理**：JS、CSS、图片、字体、SVG、WASM 等统一处理和指纹化。
- **安全与合规**：内联/移除调试信息，控制可见代码面，满足合规要求。

## 常见打包工具对比

| 工具       | 主要特点                                | 适用场景                     |
| :--------- | :-------------------------------------- | :--------------------------- |
| Webpack    | 功能最全、生态成熟、插件/Loader 丰富    | 复杂前端应用、微前端         |
| Vite       | 开发极快（依赖 esbuild），生产用 Rollup | 现代前端、快速开发体验       |
| Rollup     | ESM 优先，产物精简，库打包友好          | JS/TS 库、组件库             |
| esbuild    | Go 实现，极速打包，API 简洁             | 工具链底座、预构建、快速原型 |
| Parcel     | 零配置开箱即用                          | 小中型项目、入门场景         |
| Turbopack  | Rust 实现，强调冷/热启动速度            | 需实验特性时可尝试           |

选择建议：
- **应用**：优先 Vite（快、简单）；对复杂/老项目可用 Webpack。
- **库/组件库**：优先 Rollup；若需多产物格式 (CJS/ESM/UMD) 亦可用 tsup/esbuild + Rollup。
- **极致构建速度**：esbuild；但对产物精细化（如高级 Tree Shaking、Chunk 拆分）仍常结合 Rollup/Webpack。

## 基本概念

- **Entry（入口）**：打包起点文件；多入口对应多 bundle。
- **Output（产物）**：打包后的文件名、路径、格式（ESM/CJS/IIFE/UMD）。
- **Loader/Plugin**：Loader 处理文件类型（如 ts/less/png），Plugin 介入生命周期（压缩、注入变量、产物分析）。
- **Chunk**：打包过程生成的内部代码块，最终输出为 bundle。
- **Code Splitting**：按需拆分代码，减少首屏体积；常见为动态导入、路由分包、依赖分离。
- **Source Map**：映射打包后代码到源码，便于调试。
- **Hash/Content Hash**：基于内容生成指纹，配合缓存。

## Tree Shaking 原理与前置条件

Tree Shaking 利用静态分析删除未引用的导出，减少最终体积。
- **前置条件**：使用 ES Modules（静态导入导出），构建工具支持 DCE（Dead Code Elimination）。
- **流程**：静态依赖图 → 标记未使用导出 → 删除 → 压缩器（二次 DCE）。
- **限制**：动态 `require`/`import()` 难以完全静态分析；副作用文件需声明 sideEffects。

### 副作用 (sideEffects) 声明

在 `package.json` 中使用 `sideEffects` 帮助 Tree Shaking：
- `"sideEffects": false` 表示默认无副作用，未使用的导出可被安全移除。
- 如有全局样式/Polyfill 需保留，可列出白名单：`"sideEffects": ["./src/styles.css", "./src/polyfill.js"]`。

### 常见 Tree Shaking 失效原因

- 使用 CommonJS（非静态）或动态 `require`。
- 在导入路径上使用通配/动态字符串。
- 未正确声明 sideEffects，导致全部保留。
- 构建目标未启用生产模式（未压缩/未做 DCE）。

## 代码分割 (Code Splitting)

### 动态导入

```js
// 基于路由的懒加载
async function loadPage(page) {
    const module = await import(`./pages/${page}.js`);
    return module.render();
}
```

### 常见拆分策略
- **路由分包**：按页面或路由拆分。
- **依赖分包**：将大体积第三方依赖（如 React/Vue）单独抽出生成 vendor。
- **组件级懒加载**：交互时再加载（如弹窗、编辑器）。
- **并行加载**：将独立模块拆分，提升并发下载。

### Chunk 命名与缓存
- 使用 `[name].[contenthash].js` 保障缓存；入口/动态 Chunk 命名清晰（如 `about.[hash].js`）。
- 调整 `splitChunks`（Webpack）或 `build.rollupOptions.output.manualChunks`（Vite/Rollup）优化拆分。

## 产物类型与格式

- **格式**：ESM、CJS、IIFE、UMD。浏览器优先 ESM；Node 可按需求产出 CJS/ESM 双格式。
- **目标 (target)**：设定转译目标（如 `es2018`），平衡兼容与体积。
- **Polyfill 与降级**：结合 Babel/Swc 及 `core-js` 按需注入，避免全量引入。

## Source Map 策略

- 开发：`inline-source-map`（便于调试，体积大，禁用于生产）。
- 生产：`hidden-source-map` 或 `nosources-source-map`，兼顾调试与安全；若需错误上报，上传 map 到监控平台（Sentry）。

## 资源与资产处理

- **CSS/预处理器**：PostCSS、Sass/Less、CSS Modules、Tailwind；提取为独立 CSS 文件（如 `mini-css-extract-plugin`）。
- **图片/字体**：小文件内联（Base64），大文件使用文件指纹；可开启图片压缩（imagemin、svgo）。
- **WASM/Worker**：确保构建器支持对应的 loader/plugin，或使用 `new URL('./worker.js', import.meta.url)`。

## 性能优化清单

1. **Tree Shaking**：开启生产模式 + sideEffects 声明。
2. **Code Splitting**：路由/依赖拆分，避免大单包。
3. **按需加载**：动态导入组件、第三方库（如图表、编辑器）。
4. **缓存**：使用 contenthash，分离运行时代码（runtimeChunk），长缓存。
5. **压缩与 Minify**：Terser/Esbuild/Swc 压缩；移除 console/debug。
6. **预构建/预编译**：Vite 依赖预构建，Webpack DLL（旧方案）。
7. **预加载策略**：合理使用 `preload`/`prefetch`，避免过度。
8. **Bundle 分析**：使用 `webpack-bundle-analyzer` / `rollup-plugin-visualizer` 观察体积与重复依赖。

## 常见配置示例

### Vite 生产构建（简化示例）

```js
// vite.config.js
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [vue()],
  build: {
    target: 'es2018',
    sourcemap: false,
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['vue', 'vue-router', 'pinia']
        },
        chunkFileNames: 'assets/[name]-[hash].js',
        entryFileNames: 'assets/[name]-[hash].js'
      }
    }
  }
});
```

### Webpack 代码分割（简化示例）

```js
// webpack.config.js
module.exports = {
  mode: 'production',
  entry: {
    main: './src/index.js'
  },
  output: {
    filename: '[name].[contenthash].js',
    chunkFilename: '[name].[contenthash].js',
    clean: true
  },
  optimization: {
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendor',
          chunks: 'all'
        }
      }
    },
    runtimeChunk: 'single'
  },
  devtool: 'hidden-source-map'
};
```

## 故障排查与常见问题

- **Tree Shaking 无效**：检查是否使用 ES Modules；确认 sideEffects 声明；避免动态 require。
- **Chunk 过多/过碎**：调整拆分策略，合并过小依赖；合理设置最小体积阈值。
- **首屏体积过大**：路由懒加载、拆分大依赖、开启 gzip/br 压缩（部署时配置 Nginx/CDN）。
- **Source Map 泄露**：生产环境禁用 inline map，使用 hidden/nosources，并限制 map 访问。
- **兼容性问题**：检查 target/浏览器列表；确认 Polyfill 策略；避免引入未转译的三方包。

## 最佳实践清单

- 生产模式构建，开启压缩与 Tree Shaking。
- 为包声明 sideEffects，减少无效代码保留。
- 使用动态导入实现懒加载，结合合理的 Chunk 命名。
- 产物使用 contenthash，拆分 runtime 与 vendor，提升缓存命中。
- 依赖体积分析，定期清理重复或大体积依赖。
- 上传 Source Map 到监控平台而非直接暴露到公网。
- 结合 lint/format/test/CI，确保构建与质量流程一致。

## 练习

1. 使用 Vite 或 Webpack 将一个多路由应用拆分为路由级别的 Chunk，并验证懒加载效果。
2. 为一个包含未使用导出的示例项目开启 Tree Shaking，观察打包前后体积差异。
3. 使用 bundle 分析工具定位最大依赖，尝试替换或拆分以减小体积。
4. 为生产环境配置 contenthash 与 runtimeChunk，观察缓存命中率的提升。
5. 为项目添加 Source Map 上报到错误监控平台（如 Sentry），并确保产物不暴露 map 到公网。

## 总结

模块打包与 Tree Shaking 是现代前端性能和工程化的核心环节。理解工具差异、配置要点与常见陷阱，并结合代码分割、缓存、压缩、Source Map、安全策略等综合手段，才能产出体积可控、性能优良、可维护的前端产物。
