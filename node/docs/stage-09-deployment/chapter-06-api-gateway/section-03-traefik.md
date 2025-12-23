# 9.6.3 Traefik

## 1. 概述

Traefik 是现代的 HTTP 反向代理和负载均衡器，支持自动服务发现、动态配置、Let's Encrypt 集成等功能。Traefik 特别适合容器化环境。

## 2. 安装与配置

### 2.1 Docker 安装

```yaml
# docker-compose.yml
version: '3.8'

services:
  traefik:
    image: traefik:v2.10
    command:
      - "--api.insecure=true"
      - "--providers.docker=true"
      - "--providers.docker.exposedbydefault=false"
      - "--entrypoints.web.address=:80"
      - "--entrypoints.websecure.address=:443"
    ports:
      - "80:80"
      - "443:443"
      - "8080:8080"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro

  app:
    image: my-app:latest
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.app.rule=Host(`api.example.com`)"
      - "traefik.http.routers.app.entrypoints=web"
      - "traefik.http.services.app.loadbalancer.server.port=3000"
```

### 2.2 配置文件

```yaml
# traefik.yml
api:
  dashboard: true
  insecure: true

entryPoints:
  web:
    address: ":80"
  websecure:
    address: ":443"

providers:
  docker:
    endpoint: "unix:///var/run/docker.sock"
    exposedByDefault: false
  file:
    filename: /etc/traefik/dynamic.yml
    watch: true
```

## 3. 路由配置

### 3.1 基本路由

```yaml
# dynamic.yml
http:
  routers:
    api:
      rule: "Host(`api.example.com`)"
      service: api-service
      entryPoints:
        - websecure
      tls:
        certResolver: letsencrypt

  services:
    api-service:
      loadBalancer:
        servers:
          - url: "http://app:3000"
```

### 3.2 中间件

```yaml
http:
  middlewares:
    auth:
      basicAuth:
        users:
          - "admin:$2y$10$..."
    
    rate-limit:
      rateLimit:
        average: 100
        period: 1m

  routers:
    api:
      rule: "Host(`api.example.com`)"
      service: api-service
      middlewares:
        - auth
        - rate-limit
```

## 4. Let's Encrypt 集成

### 4.1 配置 SSL

```yaml
certificatesResolvers:
  letsencrypt:
    acme:
      email: admin@example.com
      storage: /acme.json
      httpChallenge:
        entryPoint: web
```

## 5. 最佳实践

### 5.1 配置管理

- 使用标签配置
- 分离静态和动态配置
- 版本控制配置
- 定期审查配置

### 5.2 性能优化

- 使用缓存
- 优化路由
- 监控性能
- 调整资源

## 6. 注意事项

- **安全配置**：注意安全配置
- **性能影响**：注意性能开销
- **配置管理**：合理管理配置
- **监控告警**：配置监控告警

## 7. 常见问题

### 7.1 如何配置 SSL？

使用 Let's Encrypt 或自定义证书。

### 7.2 如何实现认证？

使用 basicAuth、forwardAuth 等中间件。

### 7.3 如何优化性能？

使用缓存、优化路由、调整配置。

## 8. 实践任务

1. **安装配置**：安装和配置 Traefik
2. **配置路由**：配置 API 路由
3. **配置中间件**：配置认证、限流等中间件
4. **SSL 配置**：配置 SSL 证书
5. **持续优化**：持续优化配置

---

**下一章**：[9.7 基础设施即代码（IaC）](../chapter-07-iac/readme.md)
