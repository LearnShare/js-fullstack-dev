# 6.3.2 Nuxt.js 简介

## 概述

Nuxt.js 是基于 Vue.js 的全栈框架，提供了服务端渲染、静态生成、模块化架构等功能，简化了 Vue 应用的开发。

## 核心特性

### 1. 服务端渲染（SSR）

Nuxt.js 支持服务端渲染，提升首屏加载速度和 SEO 效果。

```js
// pages/index.vue
export default {
    async asyncData({ $http }) {
        const data = await $http.$get('/api/data');
        return { data };
    }
}
```

### 2. 静态生成（SSG）

Nuxt.js 支持静态站点生成，可以预渲染页面。

```bash
# 生成静态站点
npm run generate
```

### 3. 自动路由

Nuxt.js 基于文件系统自动生成路由。

```
pages/
  index.vue        → /
  about.vue        → /about
  users/
    _id.vue        → /users/:id
    index.vue      → /users
```

### 4. 模块化架构

Nuxt.js 提供了模块系统，可以轻松扩展功能。

```js
// nuxt.config.js
export default {
    modules: [
        '@nuxtjs/axios',
        '@nuxtjs/auth'
    ]
}
```

### 5. Vuex 集成

Nuxt.js 内置 Vuex 状态管理支持。

```js
// store/index.js
export const state = () => ({
    counter: 0
})

export const mutations = {
    increment(state) {
        state.counter++
    }
}
```

### 6. 中间件支持

Nuxt.js 支持中间件，可以在路由前后执行代码。

```js
// middleware/auth.js
export default function ({ store, redirect }) {
    if (!store.state.auth) {
        return redirect('/login')
    }
}
```

## 应用场景

### 适合使用 Nuxt.js 的场景

1. **需要 SEO**：内容网站、博客、电商网站
2. **Vue 生态**：基于 Vue 的项目
3. **服务端渲染**：需要 SSR 的应用
4. **全栈应用**：需要前后端一体的应用

### 不适合使用 Nuxt.js 的场景

1. **纯客户端应用**：不需要 SSR 的应用
2. **React 项目**：使用 React 的项目应该使用 Next.js
3. **简单的静态网站**：可以使用更简单的工具

## 与其他框架对比

| 特性          | Nuxt.js      | Next.js      | Remix        |
|:--------------|:-------------|:-------------|:-------------|
| 基础框架      | Vue          | React        | React        |
| SSR 支持      | 支持         | 支持         | 支持         |
| SSG 支持      | 支持         | 支持         | 支持         |
| 模块系统      | 支持         | 不支持       | 不支持       |
| 学习曲线      | 中等         | 中等         | 较陡         |

## 安装和使用

### 创建项目

```bash
npx create-nuxt-app my-app
cd my-app
npm run dev
```

### 项目结构

```
my-app/
  pages/          # 页面（自动路由）
  components/     # 组件
  layouts/        # 布局
  middleware/     # 中间件
  plugins/        # 插件
  store/          # Vuex store
  static/         # 静态资源
  nuxt.config.js  # Nuxt 配置
```

## 注意事项

1. **路由系统**：理解文件系统路由
2. **数据获取**：理解 asyncData 和 fetch
3. **模块系统**：合理使用模块扩展功能
4. **部署**：考虑部署方案

## 最佳实践

1. **路由组织**：合理组织页面结构
2. **数据获取**：根据需求选择 SSR 或 SSG
3. **组件复用**：使用 components 目录组织组件
4. **状态管理**：合理使用 Vuex

## 练习

1. **Nuxt.js 基础**：创建一个 Nuxt.js 项目，实现基本的页面路由。

2. **SSR 实践**：使用 asyncData 实现服务端渲染。

3. **模块使用**：使用 Nuxt 模块扩展功能。

4. **状态管理**：使用 Vuex 管理应用状态。

5. **部署实践**：将 Nuxt.js 项目部署到生产环境。

完成以上练习后，继续学习下一节，了解 Remix。

## 总结

Nuxt.js 是强大的 Vue 全栈框架，提供了 SSR、SSG、模块化架构等功能。适合需要 SEO、服务端渲染或全栈应用的 Vue 项目。Nuxt.js 简化了 Vue 应用开发，提供了良好的开发体验。

## 相关资源

- [Nuxt.js 官网](https://nuxt.com/)
- [Nuxt.js 文档](https://nuxt.com/docs)
- [Nuxt.js GitHub](https://github.com/nuxt/nuxt)
