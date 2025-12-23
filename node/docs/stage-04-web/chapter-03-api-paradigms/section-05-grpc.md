# 4.3.5 gRPC

## 1. 概述

gRPC 是一个高性能、开源的远程过程调用（RPC）框架，基于 Protocol Buffers。gRPC 支持多种编程语言，适用于微服务架构和高性能场景。

## 2. 特性说明

- **高性能**：基于 HTTP/2，支持多路复用
- **类型安全**：使用 Protocol Buffers 定义接口
- **跨语言**：支持多种编程语言
- **流式传输**：支持单向流、双向流
- **代码生成**：自动生成客户端和服务器代码

## 3. 安装与初始化

### 3.1 安装

```bash
npm install @grpc/grpc-js @grpc/proto-loader
npm install -D grpc-tools @types/google-protobuf
```

### 3.2 定义 Protocol Buffers

```protobuf
// user.proto
syntax = "proto3";

package user;

service UserService {
  rpc GetUser (GetUserRequest) returns (User);
  rpc CreateUser (CreateUserRequest) returns (User);
  rpc UpdateUser (UpdateUserRequest) returns (User);
  rpc DeleteUser (DeleteUserRequest) returns (DeleteUserResponse);
  rpc ListUsers (ListUsersRequest) returns (ListUsersResponse);
}

message User {
  int32 id = 1;
  string name = 2;
  string email = 3;
}

message GetUserRequest {
  int32 id = 1;
}

message CreateUserRequest {
  string name = 1;
  string email = 2;
}

message UpdateUserRequest {
  int32 id = 1;
  string name = 2;
  string email = 3;
}

message DeleteUserRequest {
  int32 id = 1;
}

message DeleteUserResponse {
  bool success = 1;
}

message ListUsersRequest {
  int32 page = 1;
  int32 limit = 2;
}

message ListUsersResponse {
  repeated User users = 1;
  int32 total = 2;
}
```

## 4. 服务器实现

### 4.1 基本服务器

```ts
import * as grpc from '@grpc/grpc-js';
import * as protoLoader from '@grpc/proto-loader';
import { join } from 'node:path';

// 加载 proto 文件
const PROTO_PATH: string = join(__dirname, '../proto/user.proto');
const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true
});

const userProto = grpc.loadPackageDefinition(packageDefinition) as any;

interface User {
  id: number;
  name: string;
  email: string;
}

const users: User[] = [
  { id: 1, name: 'John', email: 'john@example.com' },
  { id: 2, name: 'Jane', email: 'jane@example.com' }
];

// 实现服务方法
function getUser(call: grpc.ServerUnaryCall<any, any>, callback: grpc.sendUnaryData<any>): void {
  const id: number = call.request.id;
  const user: User | undefined = users.find((u: User) => u.id === id);
  
  if (!user) {
    callback({
      code: grpc.status.NOT_FOUND,
      message: 'User not found'
    });
    return;
  }
  
  callback(null, user);
}

function createUser(call: grpc.ServerUnaryCall<any, any>, callback: grpc.sendUnaryData<any>): void {
  const { name, email } = call.request;
  const newUser: User = {
    id: users.length + 1,
    name,
    email
  };
  users.push(newUser);
  callback(null, newUser);
}

function updateUser(call: grpc.ServerUnaryCall<any, any>, callback: grpc.sendUnaryData<any>): void {
  const { id, name, email } = call.request;
  const userIndex: number = users.findIndex((u: User) => u.id === id);
  
  if (userIndex === -1) {
    callback({
      code: grpc.status.NOT_FOUND,
      message: 'User not found'
    });
    return;
  }
  
  users[userIndex] = { id, name, email };
  callback(null, users[userIndex]);
}

function deleteUser(call: grpc.ServerUnaryCall<any, any>, callback: grpc.sendUnaryData<any>): void {
  const id: number = call.request.id;
  const userIndex: number = users.findIndex((u: User) => u.id === id);
  
  if (userIndex === -1) {
    callback({
      code: grpc.status.NOT_FOUND,
      message: 'User not found'
    });
    return;
  }
  
  users.splice(userIndex, 1);
  callback(null, { success: true });
}

function listUsers(call: grpc.ServerUnaryCall<any, any>, callback: grpc.sendUnaryData<any>): void {
  const { page, limit } = call.request;
  const start: number = (page - 1) * limit;
  const end: number = start + limit;
  const paginatedUsers: User[] = users.slice(start, end);
  
  callback(null, {
    users: paginatedUsers,
    total: users.length
  });
}

// 创建服务器
const server = new grpc.Server();

server.addService(userProto.user.UserService.service, {
  getUser,
  createUser,
  updateUser,
  deleteUser,
  listUsers
});

// 启动服务器
server.bindAsync('0.0.0.0:50051', grpc.ServerCredentials.createInsecure(), (err: Error | null, port: number): void => {
  if (err) {
    console.error('Failed to start server:', err);
    return;
  }
  server.start();
  console.log(`gRPC server running on port ${port}`);
});
```

## 5. 客户端实现

### 5.1 基本客户端

```ts
import * as grpc from '@grpc/grpc-js';
import * as protoLoader from '@grpc/proto-loader';
import { join } from 'node:path';

const PROTO_PATH: string = join(__dirname, '../proto/user.proto');
const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true
});

const userProto = grpc.loadPackageDefinition(packageDefinition) as any;

// 创建客户端
const client = new userProto.user.UserService('localhost:50051', grpc.credentials.createInsecure());

// 调用服务方法
client.getUser({ id: 1 }, (error: grpc.ServiceError | null, response: any): void => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  console.log('User:', response);
});

// Promise 包装
function getUser(id: number): Promise<any> {
  return new Promise((resolve, reject): void => {
    client.getUser({ id }, (error: grpc.ServiceError | null, response: any): void => {
      if (error) {
        reject(error);
        return;
      }
      resolve(response);
    });
  });
}

// 使用
async function main(): Promise<void> {
  try {
    const user = await getUser(1);
    console.log('User:', user);
  } catch (error) {
    console.error('Error:', error);
  }
}

main();
```

## 6. 流式传输

### 6.1 服务器流

```protobuf
// proto 定义
service UserService {
  rpc ListUsersStream (ListUsersRequest) returns (stream User);
}
```

```ts
function listUsersStream(call: grpc.ServerWritableStream<any, any>): void {
  const { page, limit } = call.request;
  const start: number = (page - 1) * limit;
  const end: number = start + limit;
  const paginatedUsers: User[] = users.slice(start, end);
  
  paginatedUsers.forEach((user: User): void => {
    call.write(user);
  });
  
  call.end();
}
```

### 6.2 客户端流

```protobuf
// proto 定义
service UserService {
  rpc CreateUsersStream (stream CreateUserRequest) returns (CreateUsersResponse);
}
```

```ts
function createUsersStream(call: grpc.ServerReadableStream<any, any>, callback: grpc.sendUnaryData<any>): void {
  const createdUsers: User[] = [];
  
  call.on('data', (request: any): void => {
    const newUser: User = {
      id: users.length + 1,
      name: request.name,
      email: request.email
    };
    users.push(newUser);
    createdUsers.push(newUser);
  });
  
  call.on('end', (): void => {
    callback(null, { users: createdUsers });
  });
}
```

### 6.3 双向流

```protobuf
// proto 定义
service UserService {
  rpc Chat (stream ChatMessage) returns (stream ChatMessage);
}
```

```ts
function chat(call: grpc.ServerDuplexStream<any, any>): void {
  call.on('data', (message: any): void => {
    console.log('Received:', message);
    call.write({ message: `Echo: ${message.message}` });
  });
  
  call.on('end', (): void => {
    call.end();
  });
}
```

## 7. 错误处理

### 7.1 错误码

```ts
import * as grpc from '@grpc/grpc-js';

// 使用标准错误码
callback({
  code: grpc.status.NOT_FOUND,
  message: 'User not found'
});

// 自定义错误
callback({
  code: grpc.status.INVALID_ARGUMENT,
  message: 'Invalid user data',
  details: 'Name and email are required'
});
```

### 7.2 错误处理

```ts
client.getUser({ id: 1 }, (error: grpc.ServiceError | null, response: any): void => {
  if (error) {
    switch (error.code) {
      case grpc.status.NOT_FOUND:
        console.error('User not found');
        break;
      case grpc.status.INVALID_ARGUMENT:
        console.error('Invalid argument:', error.message);
        break;
      default:
        console.error('Error:', error);
    }
    return;
  }
  console.log('User:', response);
});
```

## 8. 中间件

### 8.1 认证中间件

```ts
import * as grpc from '@grpc/grpc-js';

function authenticate(call: grpc.ServerUnaryCall<any, any>, callback: grpc.sendUnaryData<any>, next: () => void): void {
  const metadata = call.metadata;
  const token = metadata.get('authorization')[0] as string;
  
  if (!token || !isValidToken(token)) {
    callback({
      code: grpc.status.UNAUTHENTICATED,
      message: 'Unauthorized'
    });
    return;
  }
  
  next();
}
```

## 9. 最佳实践

### 9.1 服务定义

- 使用有意义的服务和方法名称
- 定义清晰的请求和响应消息
- 使用合适的字段编号

### 9.2 错误处理

- 使用标准 gRPC 错误码
- 提供清晰的错误消息
- 实现统一的错误处理

### 9.3 性能优化

- 使用流式传输处理大量数据
- 实现连接池
- 使用压缩

## 10. 注意事项

- **Protocol Buffers**：需要维护 .proto 文件
- **代码生成**：需要生成客户端和服务器代码
- **HTTP/2**：需要支持 HTTP/2 的环境
- **类型安全**：使用 TypeScript 类型定义

## 11. 常见问题

### 11.1 gRPC 和 RESTful 的区别？

gRPC 使用 HTTP/2 和 Protocol Buffers，性能更高；RESTful 使用 HTTP/1.1 和 JSON，更通用。

### 11.2 如何在浏览器中使用 gRPC？

使用 gRPC-Web，通过代理将 gRPC 转换为 HTTP/1.1。

### 11.3 如何处理文件上传？

使用流式传输或通过 RESTful API 处理文件上传。

## 12. 实践任务

1. **实现基本 gRPC 服务**：实现用户 CRUD 的 gRPC 服务
2. **实现流式传输**：实现服务器流和客户端流
3. **实现错误处理**：实现统一的错误处理机制
4. **实现认证**：实现 gRPC 认证和授权
5. **客户端集成**：实现 gRPC 客户端并调用服务

---

**下一章**：[4.4 全栈框架概览](../chapter-04-fullstack/readme.md)
