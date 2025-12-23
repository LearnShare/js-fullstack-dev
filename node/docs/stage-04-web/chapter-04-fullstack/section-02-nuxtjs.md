# 4.4.2 Nuxt.js 简介

## 1. 概述

Nuxt.js 是一个基于 Vue.js 的全栈框架，提供了服务端渲染、静态站点生成、自动代码分割等功能。Nuxt.js 简化了 Vue.js 应用的开发流程，提供了开箱即用的优化和最佳实践。

## 2. 特性说明

- **服务端渲染（SSR）**：支持服务端渲染，提升首屏加载速度
- **静态站点生成（SSG）**：支持静态站点生成，提升性能
- **自动代码分割**：自动进行代码分割，优化加载性能
- **文件系统路由**：基于文件系统的路由
- **TypeScript 支持**：原生支持 TypeScript
- **模块系统**：丰富的模块生态系统

## 3. 安装与初始化

### 3.1 安装

```bash
npx nuxi@latest init my-app
cd my-app
npm install
npm run dev
```

### 3.2 项目结构

```
my-app/
├── app.vue           # 根组件
├── pages/            # 页面路由
│   ├── index.vue
│   └── about.vue
├── components/       # 组件
├── server/          # 服务端代码
│   └── api/
├── public/           # 静态资源
└── nuxt.config.ts    # 配置文件
```

## 4. 页面路由

### 4.1 基本路由

```vue
<!-- pages/index.vue -->
<template>
  <div>
    <h1>Home Page</h1>
  </div>
</template>

<script setup lang="ts">
// 页面逻辑
</script>
```

```vue
<!-- pages/about.vue -->
<template>
  <div>
    <h1>About Page</h1>
  </div>
</template>

<script setup lang="ts">
// 页面逻辑
</script>
```

### 4.2 动态路由

```vue
<!-- pages/users/[id].vue -->
<template>
  <div>
    <h1>User {{ $route.params.id }}</h1>
  </div>
</template>

<script setup lang="ts">
const route = useRoute();
const userId = computed(() => route.params.id as string);
</script>
```

### 4.3 嵌套路由

```
pages/
├── users/
│   ├── index.vue
│   └── [id].vue
```

## 5. API 路由

### 5.1 服务端 API

```ts
// server/api/users/index.get.ts
interface User {
  id: number;
  name: string;
  email: string;
}

const users: User[] = [
  { id: 1, name: 'John', email: 'john@example.com' },
  { id: 2, name: 'Jane', email: 'jane@example.com' }
];

export default defineEventHandler((event): { data: User[] } => {
  return { data: users };
});
```

```ts
// server/api/users/index.post.ts
export default defineEventHandler(async (event): Promise<{ data: User }> => {
  const body = await readBody(event);
  const newUser: User = {
    id: users.length + 1,
    name: body.name,
    email: body.email
  };
  users.push(newUser);
  setResponseStatus(event, 201);
  return { data: newUser };
});
```

### 5.2 动态 API 路由

```ts
// server/api/users/[id].get.ts
export default defineEventHandler((event): { data: User | null } => {
  const id = parseInt(getRouterParam(event, 'id') || '0');
  const user = users.find((u: User) => u.id === id);
  
  if (!user) {
    setResponseStatus(event, 404);
    return { data: null };
  }
  
  return { data: user };
});
```

## 6. 数据获取

### 6.1 useFetch

```vue
<!-- pages/users.vue -->
<template>
  <div>
    <h1>Users</h1>
    <ul>
      <li v-for="user in users" :key="user.id">
        {{ user.name }}
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
interface User {
  id: number;
  name: string;
  email: string;
}

const { data: users } = await useFetch<User[]>('/api/users');
</script>
```

### 6.2 useAsyncData

```vue
<script setup lang="ts">
const { data: users, error } = await useAsyncData('users', async () => {
  const response = await $fetch<User[]>('/api/users');
  return response;
});
</script>
```

### 6.3 $fetch

```vue
<script setup lang="ts">
const users = ref<User[]>([]);

onMounted(async () => {
  users.value = await $fetch<User[]>('/api/users');
});
</script>
```

## 7. 组合式函数（Composables）

### 7.1 创建组合式函数

```ts
// composables/useUsers.ts
export const useUsers = () => {
  const users = ref<User[]>([]);
  const loading = ref<boolean>(false);
  const error = ref<Error | null>(null);

  const fetchUsers = async (): Promise<void> => {
    loading.value = true;
    try {
      users.value = await $fetch<User[]>('/api/users');
    } catch (err) {
      error.value = err as Error;
    } finally {
      loading.value = false;
    }
  };

  return {
    users,
    loading,
    error,
    fetchUsers
  };
};
```

### 7.2 使用组合式函数

```vue
<script setup lang="ts">
const { users, loading, error, fetchUsers } = useUsers();

onMounted(() => {
  fetchUsers();
});
</script>
```

## 8. 中间件

### 8.1 路由中间件

```ts
// middleware/auth.ts
export default defineNuxtRouteMiddleware((to, from) => {
  const token = useCookie('token');
  
  if (!token.value && to.path.startsWith('/dashboard')) {
    return navigateTo('/login');
  }
});
```

### 8.2 使用中间件

```vue
<!-- pages/dashboard.vue -->
<script setup lang="ts">
definePageMeta({
  middleware: 'auth'
});
</script>
```

## 9. 插件

### 9.1 创建插件

```ts
// plugins/api.client.ts
export default defineNuxtPlugin(() => {
  return {
    provide: {
      api: {
        getUsers: async (): Promise<User[]> => {
          return await $fetch('/api/users');
        }
      }
    }
  };
});
```

### 9.2 使用插件

```vue
<script setup lang="ts">
const { $api } = useNuxtApp();
const users = await $api.getUsers();
</script>
```

## 10. 最佳实践

### 10.1 代码组织

- 使用组合式函数复用逻辑
- 使用 TypeScript 提供类型安全
- 使用服务端 API 处理数据操作

### 10.2 性能优化

- 使用服务端渲染提升首屏加载
- 使用静态生成提升性能
- 使用自动代码分割优化加载

### 10.3 SEO 优化

- 使用 `useHead` 设置元数据
- 使用服务端渲染
- 使用结构化数据

## 11. 注意事项

- **服务端 vs 客户端**：区分服务端和客户端代码
- **API 路由**：API 路由运行在服务端
- **环境变量**：使用 `useRuntimeConfig` 访问配置
- **类型安全**：使用 TypeScript 提供类型安全

## 12. 常见问题

### 12.1 Nuxt.js 和 Vue.js 的区别？

Nuxt.js 是基于 Vue.js 的全栈框架，提供了 SSR、路由、状态管理等功能。

### 12.2 如何选择渲染方式？

静态内容用 SSG，动态内容用 SSR，需要实时数据用客户端获取。

### 12.3 如何处理文件上传？

使用服务端 API 处理文件上传，或使用第三方服务。

## 13. 实践任务

1. **创建 Nuxt.js 项目**：创建 Nuxt.js 项目并配置 TypeScript
2. **实现页面路由**：实现动态路由和嵌套路由
3. **实现 API 路由**：实现用户 CRUD API
4. **实现数据获取**：使用 useFetch 获取数据
5. **实现组合式函数**：创建可复用的组合式函数

---

**下一节**：[4.4.3 Remix 简介](section-03-remix.md)
