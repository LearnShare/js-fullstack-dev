# 8.6.2 Webpack + TypeScript

## 概述

Webpack 是一个流行的构建工具，与 TypeScript 集成良好。本节介绍 Webpack + TypeScript 的配置。

## 安装

```bash
npm install --save-dev webpack webpack-cli typescript ts-loader
```

## 配置

### 1. tsconfig.json

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "moduleResolution": "node",
    "strict": true
  }
}
```

### 2. webpack.config.js

```js
module.exports = {
    entry: "./src/index.ts",
    module: {
        rules: [
            {
                test: /\.ts$/,
                use: "ts-loader",
                exclude: /node_modules/
            }
        ]
    },
    resolve: {
        extensions: [".ts", ".js"]
    }
};
```

## 使用场景

### 1. 大型项目

大型项目使用 Webpack + TypeScript：

```js
// webpack.config.js
module.exports = {
    // 复杂配置
};
```

### 2. 传统项目

传统项目使用 Webpack + TypeScript：

```js
// webpack.config.js
module.exports = {
    // 传统配置
};
```

## 注意事项

1. **ts-loader**：使用 ts-loader 处理 TypeScript
2. **模块解析**：使用 `node` 模块解析
3. **配置正确**：确保 webpack 配置正确

## 最佳实践

1. **使用 Webpack**：大型项目使用 Webpack
2. **配置正确**：确保 TypeScript 配置正确
3. **性能优化**：优化 Webpack 性能

## 练习

1. **Webpack 配置**：配置 Webpack + TypeScript。

2. **项目使用**：在实际项目中使用 Webpack。

3. **实际应用**：在实际项目中应用 Webpack 配置。

完成以上练习后，继续学习下一节，了解 Turbopack + TypeScript。

## 总结

Webpack 是一个流行的构建工具，与 TypeScript 集成良好。配置 tsconfig.json 和 webpack.config.js，使用 ts-loader 处理 TypeScript。理解 Webpack + TypeScript 的配置是学习构建工具集成的关键。

## 相关资源

- [Webpack 文档](https://webpack.js.org/)
- [ts-loader](https://github.com/TypeStrong/ts-loader)
