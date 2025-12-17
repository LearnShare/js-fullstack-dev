# 6.4.2 静态站点生成器

## 概述

静态站点生成器（SSG）是 JAMstack 架构的核心组件，用于在构建时生成静态 HTML。本节介绍常用的静态站点生成器及其特点。

## 常用静态站点生成器

### Next.js（SSG 模式）

Next.js 在 SSG 模式下可以作为静态站点生成器使用。

```js
// pages/posts/[id].js
export async function getStaticPaths() {
    const posts = await getPosts();
    return {
        paths: posts.map(post => ({ params: { id: post.id } })),
        fallback: false
    };
}

export async function getStaticProps({ params }) {
    const post = await getPost(params.id);
    return {
        props: { post }
    };
}

export default function Post({ post }) {
    return <article>{post.content}</article>;
}
```

### Nuxt.js（SSG 模式）

Nuxt.js 支持静态站点生成。

```bash
# 生成静态站点
npm run generate
```

```js
// nuxt.config.js
export default {
    target: 'static',
    generate: {
        routes: ['/posts/1', '/posts/2']
    }
}
```

### Gatsby

Gatsby 是一个基于 React 的静态站点生成器。

```js
// gatsby-node.js
exports.createPages = async ({ graphql, actions }) => {
    const { createPage } = actions;
    const result = await graphql(`
        query {
            allPosts {
                nodes {
                    id
                    slug
                }
            }
        }
    `);
    
    result.data.allPosts.nodes.forEach(node => {
        createPage({
            path: `/posts/${node.slug}`,
            component: require.resolve('./src/templates/post.js'),
            context: { id: node.id }
        });
    });
};
```

### Hugo

Hugo 是一个用 Go 编写的静态站点生成器，速度非常快。

```yaml
# config.yaml
baseURL: "https://example.com"
languageCode: "zh-cn"
title: "My Site"
```

### Jekyll

Jekyll 是一个基于 Ruby 的静态站点生成器，GitHub Pages 原生支持。

```markdown
---
layout: post
title: "My Post"
---

# My Post Content
```

### 11ty（Eleventy）

11ty 是一个简单的静态站点生成器，不依赖框架。

```js
// .eleventy.js
module.exports = function(eleventyConfig) {
    return {
        dir: {
            input: "src",
            output: "dist"
        }
    };
};
```

## 静态站点生成器对比

| 特性          | Next.js | Nuxt.js | Gatsby | Hugo   | Jekyll |
|:--------------|:--------|:--------|:-------|:-------|:-------|
| 基础框架      | React   | Vue     | React  | 无     | 无     |
| 构建速度      | 中等    | 中等    | 较慢   | 快     | 中等   |
| 学习曲线      | 中等    | 中等    | 较陡   | 平缓   | 平缓   |
| 插件生态      | 丰富    | 丰富    | 非常丰富 | 中等 | 丰富   |
| 数据源        | 灵活    | 灵活    | GraphQL | 灵活 | 灵活   |

## 选择建议

### 根据技术栈选择

- **React 项目**：Next.js、Gatsby
- **Vue 项目**：Nuxt.js
- **无框架偏好**：Hugo、11ty、Jekyll

### 根据需求选择

- **需要 React/Vue**：Next.js、Nuxt.js、Gatsby
- **需要快速构建**：Hugo
- **简单项目**：11ty、Jekyll
- **内容优先**：Hugo、Jekyll

## 使用流程

### 1. 安装和初始化

```bash
# Next.js
npx create-next-app@latest my-site

# Nuxt.js
npx create-nuxt-app my-site

# Gatsby
npx gatsby new my-site

# Hugo
hugo new site my-site
```

### 2. 配置生成器

根据生成器的文档配置生成选项。

### 3. 编写内容

使用 Markdown、MDX 或其他格式编写内容。

### 4. 构建静态站点

```bash
# Next.js
npm run build

# Nuxt.js
npm run generate

# Gatsby
npm run build

# Hugo
hugo
```

### 5. 部署

将生成的静态文件部署到 CDN。

## 注意事项

1. **构建时间**：大型站点构建时间可能较长
2. **动态内容**：需要动态内容时使用客户端 JavaScript 和 API
3. **增量构建**：某些生成器支持增量构建
4. **数据源**：合理选择和管理数据源

## 最佳实践

1. **选择合适的生成器**：根据项目需求选择
2. **优化构建**：使用增量构建和缓存
3. **内容管理**：使用 Headless CMS 管理内容
4. **性能优化**：优化静态资源加载

## 练习

1. **Next.js SSG**：使用 Next.js 创建静态站点，实现页面生成。

2. **Nuxt.js SSG**：使用 Nuxt.js 创建静态站点。

3. **Hugo 实践**：使用 Hugo 创建简单的静态站点。

4. **数据源集成**：集成外部数据源（如 API、CMS）到静态站点。

5. **构建优化**：优化静态站点的构建速度和输出大小。

完成以上练习后，继续学习下一节，了解 Headless CMS。

## 总结

静态站点生成器是 JAMstack 架构的核心组件，用于在构建时生成静态 HTML。Next.js、Nuxt.js、Gatsby、Hugo、Jekyll 等是常用的静态站点生成器。根据项目需求和技术栈选择合适的生成器，可以快速构建高性能的静态站点。

## 相关资源

- [Next.js SSG](https://nextjs.org/docs/basic-features/pages#static-generation)
- [Nuxt.js SSG](https://nuxt.com/docs/getting-started/deployment#static-hosting)
- [Gatsby 官网](https://www.gatsbyjs.com/)
- [Hugo 官网](https://gohugo.io/)
