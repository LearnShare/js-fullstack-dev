# 4.5.3 Headless CMS

## 1. 概述

Headless CMS（无头内容管理系统）是一种内容管理系统，将内容存储和内容展示分离。Headless CMS 通过 API 提供内容，前端应用通过 API 获取内容，实现内容与展示的完全解耦。

## 2. 特性说明

- **API 驱动**：通过 REST 或 GraphQL API 提供内容
- **内容与展示分离**：内容存储和展示完全分离
- **多平台支持**：内容可以用于多个平台
- **类型安全**：支持类型定义和验证
- **实时更新**：支持实时内容更新

## 3. 主流 Headless CMS

### 3.1 Contentful

**特点**：
- 云端服务
- REST 和 GraphQL API
- 丰富的字段类型
- 多语言支持

**基本使用**：

```ts
import { createClient } from 'contentful';

const client = createClient({
  space: process.env.CONTENTFUL_SPACE_ID!,
  accessToken: process.env.CONTENTFUL_ACCESS_TOKEN!
});

interface Post {
  fields: {
    title: string;
    content: string;
    slug: string;
  };
}

async function getPosts(): Promise<Post[]> {
  const response = await client.getEntries({
    content_type: 'post'
  });
  return response.items as Post[];
}

async function getPost(slug: string): Promise<Post | null> {
  const response = await client.getEntries({
    content_type: 'post',
    'fields.slug': slug
  });
  return response.items[0] as Post || null;
}
```

### 3.2 Strapi

**特点**：
- 开源自托管
- REST 和 GraphQL API
- 可定制性强
- 插件系统

**基本使用**：

```ts
// 安装 Strapi SDK
// npm install @strapi/strapi

async function getPosts(): Promise<Post[]> {
  const response = await fetch(`${process.env.STRAPI_URL}/api/posts`);
  const data = await response.json();
  return data.data;
}

async function getPost(id: number): Promise<Post | null> {
  const response = await fetch(`${process.env.STRAPI_URL}/api/posts/${id}`);
  const data = await response.json();
  return data.data || null;
}
```

### 3.3 Sanity

**特点**：
- 实时协作
- GraphQL API
- 结构化内容
- 版本控制

**基本使用**：

```ts
import { createClient } from '@sanity/client';

const client = createClient({
  projectId: process.env.SANITY_PROJECT_ID!,
  dataset: 'production',
  useCdn: true,
  apiVersion: '2023-01-01'
});

interface Post {
  _id: string;
  title: string;
  content: string;
  slug: { current: string };
}

async function getPosts(): Promise<Post[]> {
  return await client.fetch<Post[]>(`
    *[_type == "post"] {
      _id,
      title,
      content,
      slug
    }
  `);
}

async function getPost(slug: string): Promise<Post | null> {
  const posts = await client.fetch<Post[]>(`
    *[_type == "post" && slug.current == $slug][0] {
      _id,
      title,
      content,
      slug
    }
  `, { slug });
  return posts || null;
}
```

### 3.4 Ghost

**特点**：
- 专业发布平台
- REST API
- 会员系统
- 邮件订阅

**基本使用**：

```ts
import GhostContentAPI from '@tryghost/content-api';

const api = new GhostContentAPI({
  url: process.env.GHOST_URL!,
  key: process.env.GHOST_CONTENT_API_KEY!,
  version: 'v5.0'
});

interface Post {
  id: string;
  title: string;
  html: string;
  slug: string;
}

async function getPosts(): Promise<Post[]> {
  return await api.posts.browse({
    limit: 10,
    include: ['tags', 'authors']
  });
}

async function getPost(slug: string): Promise<Post | null> {
  try {
    return await api.posts.read({ slug });
  } catch (error) {
    return null;
  }
}
```

## 4. 与静态站点生成器集成

### 4.1 Next.js 集成

```tsx
// lib/contentful.ts
import { createClient } from 'contentful';

export const contentfulClient = createClient({
  space: process.env.CONTENTFUL_SPACE_ID!,
  accessToken: process.env.CONTENTFUL_ACCESS_TOKEN!
});

// pages/posts/[slug].tsx
import { GetStaticProps, GetStaticPaths } from 'next';
import { contentfulClient } from '../../lib/contentful';

export const getStaticPaths: GetStaticPaths = async () => {
  const posts = await contentfulClient.getEntries({ content_type: 'post' });
  const paths = posts.items.map((post: any) => ({
    params: { slug: post.fields.slug }
  }));

  return { paths, fallback: false };
};

export const getStaticProps: GetStaticProps = async ({ params }) => {
  const posts = await contentfulClient.getEntries({
    content_type: 'post',
    'fields.slug': params!.slug
  });
  const post = posts.items[0];

  return {
    props: { post: post.fields }
  };
};
```

### 4.2 Nuxt.js 集成

```vue
<!-- pages/posts/[slug].vue -->
<template>
  <div>
    <h1>{{ post.title }}</h1>
    <div v-html="post.content"></div>
  </div>
</template>

<script setup lang="ts">
import { createClient } from 'contentful';

const route = useRoute();
const config = useRuntimeConfig();

const client = createClient({
  space: config.public.contentfulSpaceId,
  accessToken: config.public.contentfulAccessToken
});

const { data: post } = await useAsyncData(`post-${route.params.slug}`, async () => {
  const response = await client.getEntries({
    content_type: 'post',
    'fields.slug': route.params.slug
  });
  return response.items[0]?.fields || null;
});
</script>
```

## 5. 内容预览

### 5.1 Contentful 预览

```ts
const previewClient = createClient({
  space: process.env.CONTENTFUL_SPACE_ID!,
  accessToken: process.env.CONTENTFUL_PREVIEW_ACCESS_TOKEN!,
  host: 'preview.contentful.com'
});

async function getPostPreview(slug: string): Promise<Post | null> {
  const response = await previewClient.getEntries({
    content_type: 'post',
    'fields.slug': slug
  });
  return response.items[0]?.fields || null;
}
```

### 5.2 Sanity 预览

```ts
import { createClient } from '@sanity/client';

const previewClient = createClient({
  projectId: process.env.SANITY_PROJECT_ID!,
  dataset: 'production',
  useCdn: false,
  token: process.env.SANITY_PREVIEW_TOKEN
});

async function getPostPreview(slug: string): Promise<Post | null> {
  return await previewClient.fetch(`
    *[_type == "post" && slug.current == $slug][0]
  `, { slug });
}
```

## 6. Webhook 集成

### 6.1 重新验证 Webhook

```ts
// pages/api/revalidate.ts
import type { NextApiRequest, NextApiResponse } from 'next';

export default async function handler(req: NextApiRequest, res: NextApiResponse): Promise<void> {
  const { secret, slug } = req.body;

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

### 6.2 Contentful Webhook

```ts
// 在 Contentful 中配置 Webhook
// URL: https://your-domain.com/api/revalidate
// 事件: Entry publish, Entry unpublish
```

## 7. 最佳实践

### 7.1 内容建模

- 使用清晰的内容模型
- 定义字段类型
- 使用引用关系

### 7.2 API 使用

- 使用缓存减少 API 调用
- 实现错误处理
- 使用类型定义

### 7.3 性能优化

- 使用 CDN 缓存
- 实现增量更新
- 优化图片加载

## 8. 注意事项

- **API 限制**：注意 API 调用限制
- **内容预览**：实现内容预览功能
- **类型安全**：使用 TypeScript 类型定义
- **错误处理**：实现完善的错误处理

## 9. 常见问题

### 9.1 如何选择 Headless CMS？

根据项目需求、预算和技术栈选择。云端服务用 Contentful，自托管用 Strapi。

### 9.2 如何处理内容更新？

使用 Webhook 触发重新构建，或使用 ISR 增量更新。

### 9.3 Headless CMS 和传统 CMS 的区别？

Headless CMS 只提供内容 API，不提供展示层；传统 CMS 提供完整的内容管理和展示。

## 10. 实践任务

1. **集成 Headless CMS**：在 Next.js 或 Nuxt.js 中集成 Contentful 或 Strapi
2. **实现内容获取**：实现内容获取和展示功能
3. **实现内容预览**：实现内容预览功能
4. **实现 Webhook**：实现内容更新 Webhook
5. **优化性能**：优化内容加载性能

---

**下一节**：[4.5.4 CDN 与边缘计算](section-04-cdn-edge.md)
