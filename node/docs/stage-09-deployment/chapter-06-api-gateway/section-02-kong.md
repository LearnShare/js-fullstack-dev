# 9.6.2 Kong

## 1. 概述

Kong 是开源的 API 网关，提供了丰富的插件生态系统，支持认证、限流、监控等功能。Kong 基于 Nginx 和 OpenResty，性能优秀。

## 2. 安装与配置

### 2.1 Docker 安装

```bash
# 启动 Kong
docker run -d --name kong \
  -e "KONG_DATABASE=off" \
  -e "KONG_DECLARATIVE_CONFIG=/kong/declarative/kong.yml" \
  -e "KONG_PROXY_ACCESS_LOG=/dev/stdout" \
  -e "KONG_ADMIN_ACCESS_LOG=/dev/stdout" \
  -e "KONG_PROXY_ERROR_LOG=/dev/stderr" \
  -e "KONG_ADMIN_ERROR_LOG=/dev/stderr" \
  -e "KONG_ADMIN_LISTEN=0.0.0.0:8001" \
  -p 8000:8000 \
  -p 8443:8443 \
  -p 8001:8001 \
  -p 8444:8444 \
  kong:latest
```

### 2.2 基本配置

```yaml
# kong.yml
_format_version: "3.0"

services:
  - name: user-service
    url: http://user-service:3000
    routes:
      - name: user-route
        paths:
          - /api/users

  - name: order-service
    url: http://order-service:3000
    routes:
      - name: order-route
        paths:
          - /api/orders
```

## 3. 插件配置

### 3.1 认证插件

```yaml
services:
  - name: user-service
    url: http://user-service:3000
    plugins:
      - name: key-auth
        config:
          key_names:
            - apikey
    routes:
      - name: user-route
        paths:
          - /api/users
```

### 3.2 限流插件

```yaml
services:
  - name: user-service
    url: http://user-service:3000
    plugins:
      - name: rate-limiting
        config:
          minute: 100
          hour: 1000
          policy: local
    routes:
      - name: user-route
        paths:
          - /api/users
```

### 3.3 CORS 插件

```yaml
services:
  - name: user-service
    url: http://user-service:3000
    plugins:
      - name: cors
        config:
          origins:
            - https://example.com
          methods:
            - GET
            - POST
            - PUT
            - DELETE
          headers:
            - Accept
            - Authorization
          credentials: true
```

## 4. 管理 API

### 4.1 使用 Admin API

```bash
# 创建服务
curl -i -X POST http://localhost:8001/services/ \
  -d "name=user-service" \
  -d "url=http://user-service:3000"

# 创建路由
curl -i -X POST http://localhost:8001/services/user-service/routes \
  -d "paths[]=/api/users"

# 启用插件
curl -i -X POST http://localhost:8001/services/user-service/plugins \
  -d "name=rate-limiting" \
  -d "config.minute=100"
```

## 5. 最佳实践

### 5.1 配置管理

- 使用声明式配置
- 版本控制配置
- 分离环境配置
- 定期审查配置

### 5.2 性能优化

- 使用缓存
- 优化插件
- 监控性能
- 调整资源

## 6. 注意事项

- **性能影响**：注意插件的性能开销
- **配置管理**：合理管理配置
- **安全配置**：注意安全配置
- **监控告警**：配置监控告警

## 7. 常见问题

### 7.1 如何配置认证？

使用 key-auth、jwt、oauth2 等插件。

### 7.2 如何实现限流？

使用 rate-limiting 插件配置限流策略。

### 7.3 如何优化性能？

使用缓存、优化插件、调整配置。

## 8. 实践任务

1. **安装配置**：安装和配置 Kong
2. **配置路由**：配置 API 路由
3. **启用插件**：启用认证、限流等插件
4. **性能优化**：优化 Kong 性能
5. **持续优化**：持续优化配置

---

**下一节**：[9.6.3 Traefik](section-03-traefik.md)
