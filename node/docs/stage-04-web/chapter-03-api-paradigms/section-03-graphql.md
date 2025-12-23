# 4.3.3 GraphQL API

## 1. 概述

GraphQL 是一种用于 API 的查询语言和运行时系统。GraphQL 允许客户端精确指定需要的数据，减少过度获取和请求次数，提供更好的开发体验。

## 2. 特性说明

- **单一端点**：所有查询通过单一端点进行
- **客户端定义查询**：客户端定义需要的数据结构
- **类型系统**：强类型系统，提供类型安全
- **减少过度获取**：只获取需要的数据
- **实时订阅**：支持实时数据订阅

## 3. 安装与初始化

### 3.1 安装

```bash
npm install graphql @graphql-tools/schema
npm install @apollo/server graphql-tag
```

### 3.2 基本使用

```ts
import { ApolloServer } from '@apollo/server';
import { startStandaloneServer } from '@apollo/server/standalone';
import { gql } from 'graphql-tag';

// 类型定义
const typeDefs = gql`
  type User {
    id: ID!
    name: String!
    email: String!
  }

  type Query {
    users: [User!]!
    user(id: ID!): User
  }

  type Mutation {
    createUser(name: String!, email: String!): User!
  }
`;

// 解析器
interface User {
  id: string;
  name: string;
  email: string;
}

const users: User[] = [
  { id: '1', name: 'John', email: 'john@example.com' },
  { id: '2', name: 'Jane', email: 'jane@example.com' }
];

const resolvers = {
  Query: {
    users: (): User[] => users,
    user: (_: unknown, { id }: { id: string }): User | undefined => {
      return users.find((u: User) => u.id === id);
    }
  },
  Mutation: {
    createUser: (_: unknown, { name, email }: { name: string; email: string }): User => {
      const newUser: User = {
        id: String(users.length + 1),
        name,
        email
      };
      users.push(newUser);
      return newUser;
    }
  }
};

// 创建服务器
const server = new ApolloServer({
  typeDefs,
  resolvers
});

// 启动服务器
const { url } = await startStandaloneServer(server, {
  listen: { port: 4000 }
});

console.log(`GraphQL server ready at ${url}`);
```

## 4. 类型定义

### 4.1 基本类型

```ts
const typeDefs = gql`
  type User {
    id: ID!
    name: String!
    email: String!
    age: Int
    active: Boolean!
    createdAt: String!
  }

  type Query {
    user(id: ID!): User
  }
`;
```

### 4.2 关系类型

```ts
const typeDefs = gql`
  type User {
    id: ID!
    name: String!
    posts: [Post!]!
  }

  type Post {
    id: ID!
    title: String!
    content: String!
    author: User!
  }

  type Query {
    user(id: ID!): User
    post(id: ID!): Post
  }
`;
```

### 4.3 输入类型

```ts
const typeDefs = gql`
  input CreateUserInput {
    name: String!
    email: String!
    age: Int
  }

  type Mutation {
    createUser(input: CreateUserInput!): User!
  }
`;
```

## 5. 解析器实现

### 5.1 查询解析器

```ts
const resolvers = {
  Query: {
    users: (): User[] => {
      return users;
    },
    user: (_: unknown, { id }: { id: string }): User | undefined => {
      return users.find((u: User) => u.id === id);
    }
  }
};
```

### 5.2 变更解析器

```ts
const resolvers = {
  Mutation: {
    createUser: (_: unknown, { input }: { input: { name: string; email: string } }): User => {
      const newUser: User = {
        id: String(users.length + 1),
        name: input.name,
        email: input.email
      };
      users.push(newUser);
      return newUser;
    },
    updateUser: (_: unknown, { id, input }: { id: string; input: Partial<User> }): User | null => {
      const userIndex: number = users.findIndex((u: User) => u.id === id);
      if (userIndex === -1) return null;
      
      users[userIndex] = { ...users[userIndex], ...input };
      return users[userIndex];
    },
    deleteUser: (_: unknown, { id }: { id: string }): boolean => {
      const userIndex: number = users.findIndex((u: User) => u.id === id);
      if (userIndex === -1) return false;
      
      users.splice(userIndex, 1);
      return true;
    }
  }
};
```

### 5.3 字段解析器

```ts
const resolvers = {
  User: {
    posts: (parent: User): Post[] => {
      return posts.filter((p: Post) => p.authorId === parent.id);
    }
  },
  Post: {
    author: (parent: Post): User | undefined => {
      return users.find((u: User) => u.id === parent.authorId);
    }
  }
};
```

## 6. 查询示例

### 6.1 基本查询

```graphql
query {
  users {
    id
    name
    email
  }
}
```

### 6.2 带参数查询

```graphql
query {
  user(id: "1") {
    id
    name
    email
  }
}
```

### 6.3 嵌套查询

```graphql
query {
  user(id: "1") {
    id
    name
    posts {
      id
      title
      content
    }
  }
}
```

### 6.4 变更操作

```graphql
mutation {
  createUser(input: {
    name: "Alice"
    email: "alice@example.com"
  }) {
    id
    name
    email
  }
}
```

## 7. 与 Express 集成

### 7.1 Express 集成

```ts
import express, { Express } from 'express';
import { ApolloServer } from '@apollo/server';
import { expressMiddleware } from '@apollo/server/express4';
import { json } from 'body-parser';

const app: Express = express();

const server = new ApolloServer({
  typeDefs,
  resolvers
});

await server.start();

app.use('/graphql', json(), expressMiddleware(server));

app.listen(4000, (): void => {
  console.log('GraphQL server ready at http://localhost:4000/graphql');
});
```

## 8. 数据加载器（DataLoader）

### 8.1 安装

```bash
npm install dataloader
```

### 8.2 使用 DataLoader

```ts
import DataLoader from 'dataloader';

// 创建用户加载器
const userLoader = new DataLoader<string, User>(async (ids: readonly string[]): Promise<User[]> => {
  const users: User[] = await fetchUsersByIds(ids as string[]);
  return ids.map((id: string) => users.find((u: User) => u.id === id) || new Error('User not found'));
});

// 在解析器中使用
const resolvers = {
  Post: {
    author: async (parent: Post): Promise<User> => {
      return await userLoader.load(parent.authorId);
    }
  }
};
```

## 9. 订阅（Subscriptions）

### 9.1 安装

```bash
npm install graphql-ws ws
```

### 9.2 实现订阅

```ts
import { useServer } from 'graphql-ws/lib/use/ws';
import { WebSocketServer } from 'ws';

const typeDefs = gql`
  type Subscription {
    userCreated: User!
  }
`;

const resolvers = {
  Subscription: {
    userCreated: {
      subscribe: () => pubsub.asyncIterator(['USER_CREATED'])
    }
  }
};

// WebSocket 服务器
const wsServer = new WebSocketServer({
  server: httpServer,
  path: '/graphql'
});

useServer({ schema }, wsServer);
```

## 10. 最佳实践

### 10.1 类型定义

- 使用描述性类型名称
- 使用非空类型（!）明确要求
- 使用输入类型组织参数

### 10.2 解析器

- 保持解析器简单
- 使用 DataLoader 避免 N+1 问题
- 处理错误情况

### 10.3 性能优化

- 使用 DataLoader 批量加载
- 实现查询复杂度限制
- 使用查询缓存

## 11. 注意事项

- **N+1 问题**：使用 DataLoader 避免 N+1 查询问题
- **查询复杂度**：限制查询复杂度，防止恶意查询
- **错误处理**：实现统一的错误处理机制
- **安全性**：实现认证和授权机制

## 12. 常见问题

### 12.1 GraphQL 和 RESTful 的区别？

GraphQL 使用单一端点，客户端定义查询；RESTful 使用多个端点，服务器定义响应。

### 12.2 如何处理文件上传？

使用 `graphql-upload` 或通过 RESTful API 处理文件上传。

### 12.3 如何实现分页？

使用 `first`、`after`、`last`、`before` 参数实现游标分页。

## 13. 实践任务

1. **实现基本 GraphQL API**：实现用户和文章的 GraphQL API
2. **实现 DataLoader**：使用 DataLoader 优化查询性能
3. **实现订阅**：实现实时数据订阅功能
4. **实现认证**：实现 GraphQL 认证和授权
5. **实现查询复杂度限制**：实现查询复杂度限制机制

---

**下一节**：[4.3.4 tRPC](section-04-trpc.md)
