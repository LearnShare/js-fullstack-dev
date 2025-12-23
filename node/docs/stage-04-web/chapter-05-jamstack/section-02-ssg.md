# 4.5.2 静态站点生成器

## 1. 概述

静态站点生成器（SSG）是 JAMstack 架构的核心工具，用于在构建时生成静态 HTML 文件。静态站点生成器将源代码转换为静态文件，通过 CDN 分发，提供高性能的 Web 应用。

## 2. 特性说明

- **预渲染**：在构建时生成静态 HTML
- **模板系统**：使用模板生成页面
- **数据源集成**：支持多种数据源
- **构建优化**：自动优化静态资源
- **开发体验**：提供开发服务器和热重载

## 3. 主流静态站点生成器

### 3.1 Next.js

**特点**：
- 基于 React
- 支持 SSG 和 SSR
- 文件系统路由
- API 路由支持

**适用场景**：
- React 项目
- 需要 SSR 和 SSG 混合
- 全栈应用

**基本使用**：

```tsx
// pages/posts/[slug].tsx
import { GetStaticProps, GetStaticPaths } from 'next';

interface Post {
  slug: string;
  title: string;
  content: string;
}

export const getStaticPaths: GetStaticPaths = async () => {
  const posts = await fetchPosts();
  const paths = posts.map((post: Post) => ({
    params: { slug: post.slug }
  }));

  return {
    paths,
    fallback: false
  };
};

export const getStaticProps: GetStaticProps = async ({ params }) => {
  const post = await fetchPost(params!.slug as string);
  return {
    props: { post }
  };
};

export default function PostPage({ post }: { post: Post }): JSX.Element {
  return (
    <div>
      <h1>{post.title}</h1>
      <div>{post.content}</div>
    </div>
  );
}
```

### 3.2 Nuxt.js

**特点**：
- 基于 Vue
- 支持 SSG 和 SSR
- 文件系统路由
- 自动代码分割

**适用场景**：
- Vue 项目
- 需要 SSR 和 SSG 混合
- 全栈应用

**基本使用**：

```vue
<!-- pages/posts/[slug].vue -->
<template>
  <div>
    <h1>{{ post.title }}</h1>
    <div>{{ post.content }}</div>
  </div>
</template>

<script setup lang="ts">
interface Post {
  slug: string;
  title: string;
  content: string;
}

const route = useRoute();
const { data: post } = await useFetch<Post>(`/api/posts/${route.params.slug}`);
</script>
```

### 3.3 Gatsby

**特点**：
- 基于 React
- GraphQL 数据层
- 插件生态系统
- 性能优化

**适用场景**：
- React 项目
- 内容驱动网站
- 需要 GraphQL

**基本使用**：

```tsx
// src/pages/posts/{MarkdownRemark.frontmatter__slug}.tsx
import { graphql } from 'gatsby';

export const query = graphql`
  query($slug: String!) {
    markdownRemark(frontmatter: { slug: { eq: $slug } }) {
      frontmatter {
        title
      }
      html
    }
  }
`;

export default function PostPage({ data }: { data: any }): JSX.Element {
  const post = data.markdownRemark;
  return (
    <div>
      <h1>{post.frontmatter.title}</h1>
      <div dangerouslySetInnerHTML={{ __html: post.html }} />
    </div>
  );
}
```

### 3.4 Astro

**特点**：
- 多框架支持
- Islands 架构
- 零 JavaScript 默认
- 内容优先

**适用场景**：
- 内容驱动网站
- 需要多框架支持
- 性能优先

**基本使用**：

```tsx
// src/pages/posts/[slug].astro
---
import Layout from '../../layouts/Layout.astro';
const { slug } = Astro.params;
const post = await fetchPost(slug!);
---

<Layout title={post.title}>
  <article>
    <h1>{post.title}</h1>
    <div set:html={post.content} />
  </article>
</Layout>
```

## 4. 数据源集成

### 4.1 Markdown 文件

```ts
// 读取 Markdown 文件
import { readFileSync } from 'node:fs';
import { join } from 'node:path';
import matter from 'gray-matter';

function getPost(slug: string): { data: any; content: string } {
  const filePath = join(process.cwd(), 'content', `${slug}.md`);
  const fileContents = readFileSync(filePath, 'utf8');
  const { data, content } = matter(fileContents);
  return { data, content };
}
```

### 4.2 API 数据

```ts
// 从 API 获取数据
async function fetchPosts(): Promise<Post[]> {
  const response = await fetch('https://api.example.com/posts');
  return response.json();
}
```

### 4.3 数据库

```ts
// 从数据库获取数据
import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

async function getPosts(): Promise<Post[]> {
  return await prisma.post.findMany();
}
```

## 5. 构建配置

### 5.1 Next.js 配置

```ts
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export', // 静态导出
  images: {
    unoptimized: true // 静态导出时禁用图片优化
  }
};

module.exports = nextConfig;
```

### 5.2 Nuxt.js 配置

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  ssr: false, // 禁用 SSR，使用 SSG
  nitro: {
    prerender: {
      routes: ['/posts/1', '/posts/2']
    }
  }
});
```

## 6. 增量静态生成（ISR）

### 6.1 Next.js ISR

```tsx
export const getStaticProps: GetStaticProps = async () => {
  const posts = await fetchPosts();
  return {
    props: { posts },
    revalidate: 60 // 每 60 秒重新生成
  };
};
```

### 6.2 按需重新验证

```ts
// pages/api/revalidate.ts
import type { NextApiRequest, NextApiResponse } from 'next';

export default async function handler(req: NextApiRequest, res: NextApiResponse): Promise<void> {
  const { secret, slug } = req.query;

  if (secret !== process.env.REVALIDATE_SECRET) {
    return res.status(401).json({ message: 'Invalid token' });
  }

  try {
    await res.revalidate(`/posts/${slug}`);
    return res.json({ revalidated: true });
  } catch (err) {
    return res.status(500).send('Error revalidating');
  }
}
```

## 7. 最佳实践

### 7.1 构建优化

- 使用增量构建
- 优化静态资源
- 使用代码分割

### 7.2 性能优化

- 优化图片
- 使用预加载
- 减少 JavaScript 大小

### 7.3 SEO 优化

- 使用元数据
- 结构化数据
- 语义化 HTML

## 8. 注意事项

- **构建时间**：大型站点构建时间可能较长
- **动态内容**：需要实时数据时使用 API
- **路由生成**：注意动态路由的生成
- **资源优化**：优化静态资源大小

## 9. 常见问题

### 9.1 如何处理动态路由？

使用 `getStaticPaths` 或类似功能生成所有可能的路径。

### 9.2 如何更新静态内容？

使用 ISR 或重新构建部署。

### 9.3 静态站点生成器适合所有项目吗？

适合内容驱动和不需要实时数据的项目。

## 10. 实践任务

1. **创建静态站点**：使用 Next.js 或 Nuxt.js 创建静态站点
2. **集成数据源**：集成 Markdown 或 API 数据源
3. **实现 ISR**：实现增量静态生成
4. **优化性能**：优化静态资源性能
5. **部署到 CDN**：部署静态站点到 CDN

---

**下一节**：[4.5.3 Headless CMS](section-03-headless-cms.md)
