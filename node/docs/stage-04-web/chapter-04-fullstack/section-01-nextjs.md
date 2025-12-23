# 4.4.1 Next.js 简介

## 1. 概述

Next.js 是一个基于 React 的全栈框架，提供了服务端渲染、静态站点生成、API 路由等功能。Next.js 简化了 React 应用的开发流程，提供了开箱即用的优化和最佳实践。

## 2. 特性说明

- **服务端渲染（SSR）**：支持服务端渲染，提升首屏加载速度
- **静态站点生成（SSG）**：支持静态站点生成，提升性能
- **API 路由**：内置 API 路由，无需单独后端服务
- **自动代码分割**：自动进行代码分割，优化加载性能
- **TypeScript 支持**：原生支持 TypeScript
- **文件系统路由**：基于文件系统的路由

## 3. 安装与初始化

### 3.1 安装

```bash
npx create-next-app@latest my-app --typescript
cd my-app
npm run dev
```

### 3.2 项目结构

```
my-app/
├── app/              # App Router（Next.js 13+）
│   ├── layout.tsx
│   ├── page.tsx
│   └── api/
├── pages/            # Pages Router（传统方式）
│   ├── _app.tsx
│   ├── index.tsx
│   └── api/
├── public/           # 静态资源
├── components/       # React 组件
└── package.json
```

## 4. 页面路由

### 4.1 App Router（Next.js 13+）

```ts
// app/page.tsx
export default function HomePage(): JSX.Element {
  return (
    <div>
      <h1>Home Page</h1>
    </div>
  );
}

// app/about/page.tsx
export default function AboutPage(): JSX.Element {
  return (
    <div>
      <h1>About Page</h1>
    </div>
  );
}

// app/users/[id]/page.tsx
interface PageProps {
  params: {
    id: string;
  };
}

export default function UserPage({ params }: PageProps): JSX.Element {
  return (
    <div>
      <h1>User {params.id}</h1>
    </div>
  );
}
```

### 4.2 Pages Router（传统方式）

```ts
// pages/index.tsx
import type { NextPage } from 'next';

const HomePage: NextPage = (): JSX.Element => {
  return (
    <div>
      <h1>Home Page</h1>
    </div>
  );
};

export default HomePage;

// pages/about.tsx
import type { NextPage } from 'next';

const AboutPage: NextPage = (): JSX.Element => {
  return (
    <div>
      <h1>About Page</h1>
    </div>
  );
};

export default AboutPage;

// pages/users/[id].tsx
import type { NextPage } from 'next';
import { useRouter } from 'next/router';

const UserPage: NextPage = (): JSX.Element => {
  const router = useRouter();
  const { id } = router.query;

  return (
    <div>
      <h1>User {id}</h1>
    </div>
  );
};

export default UserPage;
```

## 5. API 路由

### 5.1 App Router API

```ts
// app/api/users/route.ts
import { NextRequest, NextResponse } from 'next/server';

interface User {
  id: number;
  name: string;
  email: string;
}

const users: User[] = [
  { id: 1, name: 'John', email: 'john@example.com' },
  { id: 2, name: 'Jane', email: 'jane@example.com' }
];

// GET /api/users
export async function GET(request: NextRequest): Promise<NextResponse> {
  return NextResponse.json({ data: users });
}

// POST /api/users
export async function POST(request: NextRequest): Promise<NextResponse> {
  const body = await request.json();
  const newUser: User = {
    id: users.length + 1,
    name: body.name,
    email: body.email
  };
  users.push(newUser);
  return NextResponse.json({ data: newUser }, { status: 201 });
}
```

### 5.2 Pages Router API

```ts
// pages/api/users/index.ts
import type { NextApiRequest, NextApiResponse } from 'next';

interface User {
  id: number;
  name: string;
  email: string;
}

const users: User[] = [
  { id: 1, name: 'John', email: 'john@example.com' },
  { id: 2, name: 'Jane', email: 'jane@example.com' }
];

export default function handler(req: NextApiRequest, res: NextApiResponse): void {
  if (req.method === 'GET') {
    res.status(200).json({ data: users });
  } else if (req.method === 'POST') {
    const { name, email } = req.body;
    const newUser: User = {
      id: users.length + 1,
      name,
      email
    };
    users.push(newUser);
    res.status(201).json({ data: newUser });
  } else {
    res.setHeader('Allow', ['GET', 'POST']);
    res.status(405).end(`Method ${req.method} Not Allowed`);
  }
}
```

## 6. 数据获取

### 6.1 服务端组件（App Router）

```ts
// app/users/page.tsx
async function getUsers(): Promise<User[]> {
  const res = await fetch('https://api.example.com/users');
  return res.json();
}

export default async function UsersPage(): Promise<JSX.Element> {
  const users: User[] = await getUsers();

  return (
    <div>
      <h1>Users</h1>
      <ul>
        {users.map((user: User) => (
          <li key={user.id}>{user.name}</li>
        ))}
      </ul>
    </div>
  );
}
```

### 6.2 getServerSideProps（Pages Router）

```ts
// pages/users.tsx
import type { GetServerSideProps, NextPage } from 'next';

interface UsersPageProps {
  users: User[];
}

const UsersPage: NextPage<UsersPageProps> = ({ users }: UsersPageProps): JSX.Element => {
  return (
    <div>
      <h1>Users</h1>
      <ul>
        {users.map((user: User) => (
          <li key={user.id}>{user.name}</li>
        ))}
      </ul>
    </div>
  );
};

export const getServerSideProps: GetServerSideProps<UsersPageProps> = async () => {
  const res = await fetch('https://api.example.com/users');
  const users: User[] = await res.json();

  return {
    props: {
      users
    }
  };
};

export default UsersPage;
```

### 6.3 getStaticProps（静态生成）

```ts
// pages/posts.tsx
import type { GetStaticProps, NextPage } from 'next';

interface PostsPageProps {
  posts: Post[];
}

const PostsPage: NextPage<PostsPageProps> = ({ posts }: PostsPageProps): JSX.Element => {
  return (
    <div>
      <h1>Posts</h1>
      <ul>
        {posts.map((post: Post) => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul>
    </div>
  );
};

export const getStaticProps: GetStaticProps<PostsPageProps> = async () => {
  const res = await fetch('https://api.example.com/posts');
  const posts: Post[] = await res.json();

  return {
    props: {
      posts
    },
    revalidate: 60 // ISR: 每 60 秒重新生成
  };
};

export default PostsPage;
```

## 7. 中间件

### 7.1 中间件实现

```ts
// middleware.ts
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest): NextResponse {
  const token: string | null = request.cookies.get('token')?.value || null;

  if (!token && request.nextUrl.pathname.startsWith('/dashboard')) {
    return NextResponse.redirect(new URL('/login', request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: '/dashboard/:path*'
};
```

## 8. 最佳实践

### 8.1 代码组织

- 使用 App Router（Next.js 13+）
- 组件放在 `components/` 目录
- 工具函数放在 `lib/` 目录
- 类型定义放在 `types/` 目录

### 8.2 性能优化

- 使用服务端组件减少客户端 JavaScript
- 使用静态生成提升性能
- 使用图片优化组件
- 使用动态导入进行代码分割

### 8.3 SEO 优化

- 使用 Metadata API 设置元数据
- 使用结构化数据
- 使用服务端渲染

## 9. 注意事项

- **App Router vs Pages Router**：新项目推荐使用 App Router
- **服务端组件**：默认是服务端组件，需要客户端交互时使用 'use client'
- **API 路由**：API 路由运行在服务端，不能使用浏览器 API
- **环境变量**：使用 `NEXT_PUBLIC_` 前缀暴露给客户端

## 10. 常见问题

### 10.1 App Router 和 Pages Router 的区别？

App Router 是 Next.js 13+ 的新路由系统，使用服务端组件；Pages Router 是传统路由系统。

### 10.2 如何选择渲染方式？

静态内容用 SSG，动态内容用 SSR，需要实时数据用客户端获取。

### 10.3 如何处理文件上传？

使用 API 路由处理文件上传，或使用第三方服务。

## 11. 实践任务

1. **创建 Next.js 项目**：使用 App Router 创建 Next.js 项目
2. **实现页面路由**：实现动态路由和嵌套路由
3. **实现 API 路由**：实现用户 CRUD API
4. **实现数据获取**：使用服务端组件获取数据
5. **实现中间件**：实现认证和授权中间件

---

**下一节**：[4.4.2 Nuxt.js 简介](section-02-nuxtjs.md)
