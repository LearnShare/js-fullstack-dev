# 8.6.4 HAProxy

## 1. 概述

HAProxy 是高性能的负载均衡器和反向代理，提供了丰富的负载均衡算法和健康检查功能。本章介绍如何使用 HAProxy 配置负载均衡。

## 2. 基本配置

### 2.1 全局配置

```haproxy
global
    log /dev/log local0
    maxconn 4096
    user haproxy
    group haproxy
    daemon

defaults
    log global
    mode http
    option httplog
    option dontlognull
    timeout connect 5000ms
    timeout client 50000ms
    timeout server 50000ms
```

### 2.2 前端和后端配置

```haproxy
frontend http-in
    bind *:80
    default_backend servers

backend servers
    balance roundrobin
    server server1 192.168.1.10:8080 check
    server server2 192.168.1.11:8080 check
    server server3 192.168.1.12:8080 check
```

## 3. 负载均衡算法

### 3.1 算法配置

```haproxy
backend servers
    # 轮询
    balance roundrobin
    
    # 最少连接
    # balance leastconn
    
    # 源 IP 哈希
    # balance source
    
    # URI 哈希
    # balance uri
    
    server server1 192.168.1.10:8080 check
    server server2 192.168.1.11:8080 check
```

### 3.2 加权配置

```haproxy
backend servers
    balance roundrobin
    server server1 192.168.1.10:8080 weight 3 check
    server server2 192.168.1.11:8080 weight 1 check
```

## 4. 健康检查

### 4.1 HTTP 健康检查

```haproxy
backend servers
    option httpchk GET /health
    http-check expect status 200
    server server1 192.168.1.10:8080 check
    server server2 192.168.1.11:8080 check
```

### 4.2 TCP 健康检查

```haproxy
backend servers
    option tcplog
    server server1 192.168.1.10:8080 check
    server server2 192.168.1.11:8080 check
```

## 5. 统计页面

### 5.1 启用统计

```haproxy
frontend stats
    bind *:8404
    stats enable
    stats uri /stats
    stats refresh 30s
    stats admin if TRUE
```

## 6. 最佳实践

### 6.1 配置优化

- 选择合适的负载均衡算法
- 配置健康检查
- 设置合理的超时时间
- 启用统计页面

### 6.2 性能优化

- 优化 maxconn
- 使用 keepalive
- 配置合理的超时
- 监控性能指标

## 7. 注意事项

- **健康检查**：配置健康检查
- **超时设置**：设置合理的超时时间
- **会话保持**：处理有状态服务
- **监控告警**：监控负载均衡状态

## 8. 常见问题

### 8.1 如何选择 HAProxy vs Nginx？

根据需求、性能、功能选择。

### 8.2 如何处理服务器故障？

使用健康检查、自动移除故障服务器。

### 8.3 如何优化性能？

优化配置、使用 keepalive、监控性能。

## 9. 实践任务

1. **配置负载均衡**：配置 HAProxy 负载均衡
2. **健康检查**：实现健康检查
3. **性能优化**：优化负载均衡性能
4. **监控告警**：监控负载均衡状态
5. **持续优化**：持续优化配置

---

**下一章**：[8.7 CDN 深入](../chapter-07-cdn/readme.md)
