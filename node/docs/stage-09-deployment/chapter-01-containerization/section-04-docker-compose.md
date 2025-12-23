# 9.1.4 Docker Compose

## 1. 概述

Docker Compose 是用于定义和运行多容器 Docker 应用的工具，通过 YAML 文件配置应用服务，可以简化多容器应用的管理。

## 2. 基本使用

### 2.1 docker-compose.yml

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - DATABASE_URL=postgresql://user:password@db:5432/mydb
    depends_on:
      - db
      - redis

  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=mydb
    volumes:
      - postgres-data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis-data:/data

volumes:
  postgres-data:
  redis-data:
```

### 2.2 基本命令

```bash
# 启动服务
docker-compose up

# 后台启动
docker-compose up -d

# 停止服务
docker-compose down

# 查看日志
docker-compose logs

# 查看服务状态
docker-compose ps

# 重启服务
docker-compose restart

# 构建镜像
docker-compose build
```

## 3. 服务配置

### 3.1 环境变量

```yaml
services:
  app:
    environment:
      - NODE_ENV=production
      - DATABASE_URL=postgresql://db:5432/mydb
    env_file:
      - .env
      - .env.production
```

### 3.2 数据卷

```yaml
services:
  app:
    volumes:
      - ./app:/app
      - app-data:/data
    volumes:
      app-data:
```

### 3.3 网络配置

```yaml
services:
  app:
    networks:
      - frontend
      - backend

networks:
  frontend:
  backend:
```

## 4. 健康检查

### 4.1 健康检查配置

```yaml
services:
  app:
    healthcheck:
      test: ["CMD", "node", "healthcheck.js"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
```

## 5. 依赖管理

### 5.1 depends_on

```yaml
services:
  app:
    depends_on:
      - db
      - redis
    # 等待服务健康
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
```

### 5.2 启动顺序

```yaml
services:
  app:
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
```

## 6. 最佳实践

### 6.1 配置管理

- 使用环境变量
- 分离开发和生产配置
- 使用 .env 文件
- 合理使用数据卷

### 6.2 服务设计

- 单一职责
- 合理依赖关系
- 健康检查
- 资源限制

## 7. 注意事项

- **配置管理**：合理管理配置
- **数据持久化**：使用数据卷
- **网络配置**：合理配置网络
- **资源限制**：设置资源限制

## 8. 常见问题

### 8.1 如何处理服务依赖？

使用 `depends_on` 和健康检查。

### 8.2 如何管理环境变量？

使用 `.env` 文件和 `env_file`。

### 8.3 如何优化 Compose 配置？

分离配置、使用扩展、合理使用缓存。

## 9. 实践任务

1. **编写 Compose**：编写 docker-compose.yml
2. **服务配置**：配置多个服务
3. **依赖管理**：管理服务依赖
4. **数据管理**：使用数据卷
5. **持续优化**：持续优化配置

---

**下一章**：[9.2 CI/CD](../chapter-02-cicd/readme.md)
