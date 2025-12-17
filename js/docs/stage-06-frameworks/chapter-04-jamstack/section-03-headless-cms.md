# 6.4.3 Headless CMS

## 概述

Headless CMS（无头内容管理系统）是一种将内容管理和内容展示分离的 CMS 架构。在 JAMstack 架构中，Headless CMS 提供内容数据，前端通过 API 获取内容。

## Headless CMS 的概念

### 传统 CMS vs Headless CMS

#### 传统 CMS

```
内容管理 + 内容展示 = 耦合系统
```

**特点**：
- 内容管理和展示耦合
- 前端展示方式受限
- 难以跨平台使用

#### Headless CMS

```
内容管理 ← API → 内容展示（前端）
```

**特点**：
- 内容管理和展示分离
- 前端展示方式灵活
- 可以跨平台使用

## 常见 Headless CMS

### Contentful

Contentful 是一个流行的 Headless CMS，提供 REST 和 GraphQL API。

```js
// 使用 Contentful API
import { createClient } from 'contentful';

const client = createClient({
    space: 'your-space-id',
    accessToken: 'your-access-token'
});

const entries = await client.getEntries({
    content_type: 'post'
});
```

### Strapi

Strapi 是一个开源 Headless CMS，可以自托管。

```js
// 使用 Strapi API
const response = await fetch('http://localhost:1337/api/posts');
const data = await response.json();
```

### Sanity

Sanity 是一个实时协作的 Headless CMS。

```js
// 使用 Sanity
import sanityClient from '@sanity/client';

const client = sanityClient({
    projectId: 'your-project-id',
    dataset: 'production',
    useCdn: true
});

const posts = await client.fetch('*[_type == "post"]');
```

### Ghost

Ghost 是一个专注于发布的内容平台，也提供 Headless API。

```js
// 使用 Ghost API
const response = await fetch('https://your-site.com/ghost/api/content/posts/', {
    headers: {
        'Authorization': `Ghost ${apiKey}`
    }
});
const data = await response.json();
```

## Headless CMS 的特点

### 优势

1. **灵活性**：前端可以使用任何技术栈
2. **可扩展性**：可以轻松扩展到多个平台
3. **性能**：内容通过 API 获取，可以缓存
4. **解耦**：内容管理和展示分离

### 劣势

1. **学习成本**：需要了解 API 使用
2. **成本**：某些 SaaS CMS 需要付费
3. **复杂性**：增加了系统复杂性

## 选择建议

### 根据需求选择

- **需要实时协作**：Sanity
- **需要自托管**：Strapi、Ghost
- **需要简单易用**：Contentful
- **需要开源**：Strapi、Ghost

### 根据团队选择

- **技术团队强**：Strapi（可定制）
- **非技术团队**：Contentful（易用）
- **内容优先**：Ghost

## 集成到 JAMstack

### 在静态生成时获取内容

```js
// Next.js 示例
export async function getStaticProps() {
    const posts = await fetch('https://api.cms.com/posts')
        .then(res => res.json());
    
    return {
        props: { posts }
    };
}
```

### 在运行时获取内容

```js
// 客户端获取
useEffect(() => {
    fetch('https://api.cms.com/posts')
        .then(res => res.json())
        .then(data => setPosts(data));
}, []);
```

## 注意事项

1. **API 限制**：注意 API 的速率限制
2. **数据缓存**：合理缓存 API 数据
3. **内容更新**：考虑内容更新的策略
4. **成本控制**：注意 SaaS CMS 的成本

## 最佳实践

1. **API 设计**：设计良好的 API 接口
2. **数据缓存**：合理缓存 API 数据
3. **错误处理**：实现完善的错误处理
4. **内容更新**：使用 webhook 触发重新构建

## 练习

1. **Contentful 集成**：使用 Contentful 作为内容源，集成到静态站点。

2. **Strapi 实践**：部署 Strapi，创建内容模型，集成到前端。

3. **Sanity 使用**：使用 Sanity 创建内容，通过 API 获取内容。

4. **内容更新流程**：实现内容更新后自动触发重新构建的流程。

5. **多平台使用**：使用同一个 Headless CMS 为多个平台提供内容。

完成以上练习后，继续学习下一节，了解 CDN 与边缘计算。

## 总结

Headless CMS 是 JAMstack 架构的重要组成部分，提供内容数据。Contentful、Strapi、Sanity、Ghost 等是常用的 Headless CMS。选择适合的 Headless CMS，可以通过 API 灵活获取内容，实现内容管理和展示的解耦。

## 相关资源

- [Contentful 官网](https://www.contentful.com/)
- [Strapi 官网](https://strapi.io/)
- [Sanity 官网](https://www.sanity.io/)
- [Ghost 官网](https://ghost.org/)
