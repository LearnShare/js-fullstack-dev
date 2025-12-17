# 6.3.1 Next.js 简介

## 概述

Next.js 是 Vercel 开发的 React 全栈框架，提供了服务端渲染、静态生成、API 路由等功能，简化了 React 应用的开发。

## 核心特性

### 1. 服务端渲染（SSR）

Next.js 支持服务端渲染，提升首屏加载速度和 SEO 效果。

```js
// pages/index.js
export async function getServerSideProps() {
    const data = await fetchData();
    return {
        props: { data }
    };
}

export default function Home({ data }) {
    return <div>{data.title}</div>;
}
```

### 2. 静态生成（SSG）

Next.js 支持静态站点生成，可以预渲染页面。

```js
// pages/about.js
export async function getStaticProps() {
    const data = await fetchData();
    return {
        props: { data }
    };
}

export default function About({ data }) {
    return <div>{data.content}</div>;
}
```

### 3. API 路由

Next.js 提供了 API 路由，可以在同一项目中创建后端 API。

```js
// pages/api/users.js
export default function handler(req, res) {
    if (req.method === 'GET') {
        res.status(200).json({ users: [] });
    } else if (req.method === 'POST') {
        res.status(201).json({ message: 'User created' });
    }
}
```

### 4. 文件系统路由

Next.js 使用文件系统作为路由系统。

```
pages/
  index.js          → /
  about.js          → /about
  posts/
    [id].js         → /posts/:id
    index.js        → /posts
```

### 5. 自动代码分割

Next.js 自动进行代码分割，只加载需要的代码。

### 6. 图片优化

Next.js 提供了优化的 Image 组件。

```js
import Image from 'next/image';

<Image
    src="/image.jpg"
    width={500}
    height={300}
    alt="Description"
/>
```

## 应用场景

### 适合使用 Next.js 的场景

1. **需要 SEO**：内容网站、博客、电商网站
2. **服务端渲染**：需要 SSR 的应用
3. **全栈应用**：需要前后端一体的应用
4. **React 生态**：基于 React 的项目

### 不适合使用 Next.js 的场景

1. **纯客户端应用**：不需要 SSR 的应用
2. **简单的静态网站**：可以使用更简单的工具
3. **非 React 项目**：使用 Vue 或其他框架的项目

## 与其他框架对比

| 特性          | Next.js      | Nuxt.js      | Remix        |
|:--------------|:-------------|:-------------|:-------------|
| 基础框架      | React        | Vue          | React        |
| SSR 支持      | 支持         | 支持         | 支持         |
| SSG 支持      | 支持         | 支持         | 支持         |
| API 路由      | 支持         | 支持         | 支持         |
| 学习曲线      | 中等         | 中等         | 较陡         |

## 安装和使用

### 创建项目

```bash
npx create-next-app@latest my-app
cd my-app
npm run dev
```

### 项目结构

```
my-app/
  pages/          # 页面和 API 路由
  public/         # 静态资源
  styles/         # 样式文件
  components/     # 组件
  next.config.js  # Next.js 配置
```

## 注意事项

1. **路由系统**：理解文件系统路由
2. **数据获取**：理解 getServerSideProps 和 getStaticProps
3. **部署**：考虑部署方案（Vercel、自托管等）
4. **性能优化**：利用 Next.js 的性能优化特性

## 最佳实践

1. **路由组织**：合理组织页面结构
2. **数据获取**：根据需求选择 SSR 或 SSG
3. **性能优化**：使用 Image 组件、代码分割等
4. **类型安全**：使用 TypeScript 提升类型安全

## 练习

1. **Next.js 基础**：创建一个 Next.js 项目，实现基本的页面路由。

2. **SSR 实践**：使用 getServerSideProps 实现服务端渲染。

3. **API 路由**：创建 API 路由，实现简单的 CRUD 操作。

4. **静态生成**：使用 getStaticProps 实现静态页面生成。

5. **部署实践**：将 Next.js 项目部署到 Vercel 或其他平台。

完成以上练习后，继续学习下一节，了解 Nuxt.js。

## 总结

Next.js 是强大的 React 全栈框架，提供了 SSR、SSG、API 路由等功能。适合需要 SEO、服务端渲染或全栈应用的场景。Next.js 简化了 React 应用开发，提供了良好的开发体验。

## 相关资源

- [Next.js 官网](https://nextjs.org/)
- [Next.js 文档](https://nextjs.org/docs)
- [Next.js GitHub](https://github.com/vercel/next.js)
