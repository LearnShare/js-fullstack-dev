# 9.1.2 Docker 基础

## 1. 概述

Docker 是最流行的容器化平台，提供了完整的容器生命周期管理功能。本章介绍 Docker 的基本使用和常用命令。

## 2. Docker 安装

### 2.1 安装 Docker

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install docker.io

# macOS
brew install docker

# Windows
# 下载 Docker Desktop
```

### 2.2 验证安装

```bash
docker --version
docker info
```

## 3. 基本命令

### 3.1 镜像操作

```bash
# 拉取镜像
docker pull node:18-alpine

# 列出镜像
docker images

# 删除镜像
docker rmi node:18-alpine

# 构建镜像
docker build -t my-app:latest .

# 查看镜像历史
docker history my-app:latest
```

### 3.2 容器操作

```bash
# 运行容器
docker run -d -p 3000:3000 --name my-app my-app:latest

# 列出容器
docker ps          # 运行中的容器
docker ps -a       # 所有容器

# 停止容器
docker stop my-app

# 启动容器
docker start my-app

# 重启容器
docker restart my-app

# 删除容器
docker rm my-app

# 查看容器日志
docker logs my-app

# 进入容器
docker exec -it my-app sh
```

### 3.3 容器管理

```bash
# 查看容器资源使用
docker stats my-app

# 查看容器详细信息
docker inspect my-app

# 复制文件
docker cp my-app:/app/data.txt ./data.txt
docker cp ./data.txt my-app:/app/data.txt
```

## 4. 数据管理

### 4.1 数据卷（Volume）

```bash
# 创建数据卷
docker volume create my-volume

# 使用数据卷
docker run -v my-volume:/data my-app

# 列出数据卷
docker volume ls

# 删除数据卷
docker volume rm my-volume
```

### 4.2 绑定挂载（Bind Mount）

```bash
# 使用绑定挂载
docker run -v /host/path:/container/path my-app

# 只读挂载
docker run -v /host/path:/container/path:ro my-app
```

## 5. 网络管理

### 5.1 网络操作

```bash
# 创建网络
docker network create my-network

# 列出网络
docker network ls

# 连接容器到网络
docker network connect my-network my-app

# 断开网络
docker network disconnect my-network my-app

# 删除网络
docker network rm my-network
```

### 5.2 网络模式

```bash
# 桥接模式（默认）
docker run --network bridge my-app

# 主机模式
docker run --network host my-app

# 无网络
docker run --network none my-app
```

## 6. 资源限制

### 6.1 CPU 限制

```bash
# 限制 CPU
docker run --cpus="1.5" my-app

# 限制 CPU 份额
docker run --cpu-shares=512 my-app
```

### 6.2 内存限制

```bash
# 限制内存
docker run -m 512m my-app

# 内存和交换空间
docker run -m 512m --memory-swap=1g my-app
```

## 7. 最佳实践

### 7.1 命令使用

- 使用有意义的容器名称
- 使用标签管理镜像版本
- 定期清理未使用的资源
- 使用数据卷持久化数据

### 7.2 资源管理

- 设置合理的资源限制
- 监控容器资源使用
- 及时清理未使用的资源
- 优化镜像大小

## 8. 注意事项

- **资源限制**：设置合理的资源限制
- **数据持久化**：使用数据卷
- **网络配置**：合理配置网络
- **安全配置**：注意容器安全

## 9. 常见问题

### 9.1 如何查看容器日志？

使用 `docker logs` 命令，支持 `-f` 实时查看。

### 9.2 如何进入运行中的容器？

使用 `docker exec -it` 命令。

### 9.3 如何清理未使用的资源？

使用 `docker system prune` 命令。

## 10. 实践任务

1. **安装 Docker**：安装和配置 Docker
2. **基本操作**：练习基本 Docker 命令
3. **数据管理**：使用数据卷和绑定挂载
4. **网络配置**：配置容器网络
5. **资源限制**：设置资源限制

---

**下一节**：[9.1.3 Dockerfile 编写](section-03-dockerfile.md)
