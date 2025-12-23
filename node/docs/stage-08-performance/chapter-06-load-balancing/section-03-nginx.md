# 8.6.3 Nginx 负载均衡

## 1. 概述

Nginx 是广泛使用的 Web 服务器和反向代理，提供了强大的负载均衡功能。本章介绍如何使用 Nginx 配置负载均衡。

## 2. 基本配置

### 2.1 upstream 配置

```nginx
http {
    upstream backend {
        server backend1.example.com;
        server backend2.example.com;
        server backend3.example.com;
    }
    
    server {
        listen 80;
        
        location / {
            proxy_pass http://backend;
        }
    }
}
```

### 2.2 负载均衡方法

```nginx
# 轮询（默认）
upstream backend {
    server backend1.example.com;
    server backend2.example.com;
}

# 加权轮询
upstream backend {
    server backend1.example.com weight=3;
    server backend2.example.com weight=1;
}

# IP 哈希
upstream backend {
    ip_hash;
    server backend1.example.com;
    server backend2.example.com;
}

# 最少连接
upstream backend {
    least_conn;
    server backend1.example.com;
    server backend2.example.com;
}
```

## 3. 健康检查

### 3.1 被动健康检查

```nginx
upstream backend {
    server backend1.example.com max_fails=3 fail_timeout=30s;
    server backend2.example.com max_fails=3 fail_timeout=30s;
}
```

### 3.2 主动健康检查（需要模块）

```nginx
upstream backend {
    server backend1.example.com;
    server backend2.example.com;
}

# 需要 nginx_upstream_check_module
check interval=3000 rise=2 fall=3 timeout=1000 type=http;
check_http_send "GET /health HTTP/1.0\r\n\r\n";
check_http_expect_alive http_2xx http_3xx;
```

## 4. 高级配置

### 4.1 会话保持

```nginx
upstream backend {
    ip_hash;  # 使用 IP 哈希保持会话
    server backend1.example.com;
    server backend2.example.com;
}
```

### 4.2 代理设置

```nginx
location / {
    proxy_pass http://backend;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    
    proxy_connect_timeout 60s;
    proxy_send_timeout 60s;
    proxy_read_timeout 60s;
}
```

## 5. 最佳实践

### 5.1 配置优化

- 使用合适的负载均衡方法
- 配置健康检查
- 设置合理的超时时间
- 监控负载情况

### 5.2 性能优化

- 使用 keepalive 连接
- 启用 gzip 压缩
- 配置缓存
- 优化缓冲区大小

## 6. 注意事项

- **健康检查**：配置健康检查
- **超时设置**：设置合理的超时时间
- **会话保持**：处理有状态服务
- **监控告警**：监控负载均衡状态

## 7. 常见问题

### 7.1 如何处理服务器故障？

使用健康检查、自动移除故障服务器。

### 7.2 如何实现会话保持？

使用 IP 哈希、粘性会话、共享会话存储。

### 7.3 如何优化性能？

使用 keepalive、优化缓冲区、启用压缩。

## 8. 实践任务

1. **配置负载均衡**：配置 Nginx 负载均衡
2. **健康检查**：实现健康检查
3. **性能优化**：优化负载均衡性能
4. **监控告警**：监控负载均衡状态
5. **持续优化**：持续优化配置

---

**下一节**：[8.6.4 HAProxy](section-04-haproxy.md)
