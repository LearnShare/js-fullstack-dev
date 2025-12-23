# 9.1.3 Dockerfile 编写

## 1. 概述

Dockerfile 是用于构建 Docker 镜像的文本文件，包含构建镜像的指令。编写高效的 Dockerfile 对于优化镜像大小、构建速度和安全性至关重要。

## 2. Dockerfile 指令

### 2.1 FROM

**作用**：指定基础镜像。

```dockerfile
FROM node:18-alpine
```

### 2.2 WORKDIR

**作用**：设置工作目录。

```dockerfile
WORKDIR /app
```

### 2.3 COPY/ADD

**作用**：复制文件到镜像。

```dockerfile
# COPY：推荐使用
COPY package*.json ./
COPY . .

# ADD：支持 URL 和解压（不推荐）
ADD https://example.com/file.tar.gz /app
```

### 2.4 RUN

**作用**：执行命令。

```dockerfile
RUN npm ci --only=production
RUN apk add --no-cache curl
```

### 2.5 EXPOSE

**作用**：声明端口。

```dockerfile
EXPOSE 3000
```

### 2.6 CMD/ENTRYPOINT

**作用**：设置启动命令。

```dockerfile
# CMD：可被覆盖
CMD ["node", "index.js"]

# ENTRYPOINT：不可被覆盖
ENTRYPOINT ["node"]
```

## 3. Node.js Dockerfile 示例

### 3.1 基础示例

```dockerfile
FROM node:18-alpine

WORKDIR /app

# 复制依赖文件
COPY package*.json ./

# 安装依赖
RUN npm ci --only=production

# 复制应用代码
COPY . .

# 暴露端口
EXPOSE 3000

# 启动应用
CMD ["node", "index.js"]
```

### 3.2 多阶段构建

```dockerfile
# 构建阶段
FROM node:18-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

# 生产阶段
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm ci --only=production

COPY --from=builder /app/dist ./dist

EXPOSE 3000

CMD ["node", "dist/index.js"]
```

## 4. 优化技巧

### 4.1 使用 .dockerignore

```dockerignore
# .dockerignore
node_modules
npm-debug.log
.git
.env
*.md
.DS_Store
```

### 4.2 层缓存优化

```dockerfile
# 不优化：依赖变化时重新复制所有文件
COPY . .
RUN npm install

# 优化：先复制依赖文件，利用缓存
COPY package*.json ./
RUN npm install
COPY . .
```

### 4.3 使用 Alpine 镜像

```dockerfile
# 使用 Alpine 减小镜像大小
FROM node:18-alpine

# 安装必要的系统依赖
RUN apk add --no-cache \
    python3 \
    make \
    g++
```

## 5. 安全最佳实践

### 5.1 非 root 用户

```dockerfile
FROM node:18-alpine

# 创建非 root 用户
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001

WORKDIR /app

# 更改文件所有者
COPY --chown=nodejs:nodejs . .

# 切换到非 root 用户
USER nodejs

EXPOSE 3000

CMD ["node", "index.js"]
```

### 5.2 最小权限

```dockerfile
# 只安装生产依赖
RUN npm ci --only=production

# 删除不必要的文件
RUN rm -rf /tmp/* /var/tmp/*
```

## 6. 健康检查

### 6.1 HEALTHCHECK

```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD node healthcheck.js || exit 1
```

### 6.2 健康检查脚本

```ts
// healthcheck.js
import http from 'node:http';

const options = {
  host: 'localhost',
  port: 3000,
  path: '/health',
  timeout: 2000
};

const request = http.request(options, (res) => {
  if (res.statusCode === 200) {
    process.exit(0);
  } else {
    process.exit(1);
  }
});

request.on('error', () => {
  process.exit(1);
});

request.end();
```

## 7. 最佳实践

### 7.1 Dockerfile 设计

- 使用多阶段构建
- 最小化镜像层数
- 合理使用缓存
- 使用 .dockerignore

### 7.2 安全考虑

- 使用非 root 用户
- 最小权限原则
- 定期更新基础镜像
- 扫描镜像漏洞

## 8. 注意事项

- **镜像大小**：优化镜像大小
- **构建速度**：优化构建速度
- **安全性**：注意容器安全
- **可维护性**：保持 Dockerfile 可读

## 9. 常见问题

### 9.1 如何减小镜像大小？

使用多阶段构建、Alpine 镜像、删除不必要的文件。

### 9.2 如何优化构建速度？

利用层缓存、使用 .dockerignore、并行构建。

### 9.3 如何保证安全性？

使用非 root 用户、最小权限、定期更新镜像。

## 10. 实践任务

1. **编写 Dockerfile**：编写 Node.js 应用的 Dockerfile
2. **多阶段构建**：使用多阶段构建优化镜像
3. **安全加固**：实现安全最佳实践
4. **健康检查**：添加健康检查
5. **持续优化**：持续优化 Dockerfile

---

**下一节**：[9.1.4 Docker Compose](section-04-docker-compose.md)
