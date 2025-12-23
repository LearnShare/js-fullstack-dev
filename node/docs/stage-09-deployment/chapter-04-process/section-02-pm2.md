# 9.4.2 PM2

## 1. 概述

PM2 是 Node.js 应用的进程管理器，提供了进程管理、负载均衡、监控、日志管理等功能。PM2 是 Node.js 生产环境中最常用的进程管理器。

## 2. 安装与基本使用

### 2.1 安装

```bash
npm install -g pm2
```

### 2.2 基本命令

```bash
# 启动应用
pm2 start app.js

# 启动并指定名称
pm2 start app.js --name my-app

# 列出所有进程
pm2 list

# 查看进程信息
pm2 show my-app

# 停止进程
pm2 stop my-app

# 重启进程
pm2 restart my-app

# 删除进程
pm2 delete my-app

# 查看日志
pm2 logs my-app

# 监控
pm2 monit
```

## 3. 配置文件

### 3.1 ecosystem.config.js

```ts
// ecosystem.config.js
module.exports = {
  apps: [{
    name: 'my-app',
    script: './dist/index.js',
    instances: 4,
    exec_mode: 'cluster',
    env: {
      NODE_ENV: 'development',
      PORT: 3000
    },
    env_production: {
      NODE_ENV: 'production',
      PORT: 3000
    },
    error_file: './logs/err.log',
    out_file: './logs/out.log',
    log_date_format: 'YYYY-MM-DD HH:mm:ss Z',
    merge_logs: true,
    max_memory_restart: '1G',
    min_uptime: '10s',
    max_restarts: 10,
    watch: false,
    ignore_watch: ['node_modules', 'logs']
  }]
};
```

### 3.2 使用配置

```bash
# 启动所有应用
pm2 start ecosystem.config.js

# 启动特定环境
pm2 start ecosystem.config.js --env production

# 重新加载配置
pm2 reload ecosystem.config.js
```

## 4. 集群模式

### 4.1 配置集群

```ts
module.exports = {
  apps: [{
    name: 'my-app',
    script: './dist/index.js',
    instances: 'max',  // 使用所有 CPU 核心
    exec_mode: 'cluster',
    env: {
      NODE_ENV: 'production'
    }
  }]
};
```

### 4.2 负载均衡

PM2 集群模式自动实现负载均衡，将请求分发到不同的进程实例。

## 5. 监控和日志

### 5.1 监控

```bash
# 实时监控
pm2 monit

# 查看详细信息
pm2 describe my-app

# 查看资源使用
pm2 show my-app
```

### 5.2 日志管理

```bash
# 查看日志
pm2 logs my-app

# 清空日志
pm2 flush

# 日志轮转
pm2 install pm2-logrotate
pm2 set pm2-logrotate:max_size 10M
pm2 set pm2-logrotate:retain 7
```

## 6. 开机自启

### 6.1 生成启动脚本

```bash
# 生成启动脚本
pm2 startup

# 保存当前进程列表
pm2 save
```

### 6.2 移除开机自启

```bash
pm2 unstartup
```

## 7. 最佳实践

### 7.1 配置管理

- 使用配置文件
- 分离环境配置
- 设置资源限制
- 配置日志管理

### 7.2 监控告警

- 监控进程状态
- 监控资源使用
- 设置告警规则
- 定期审查日志

## 8. 注意事项

- **资源限制**：设置合理的资源限制
- **日志管理**：管理应用日志
- **监控告警**：配置监控告警
- **安全配置**：注意安全配置

## 9. 常见问题

### 9.1 如何配置集群模式？

使用 `exec_mode: 'cluster'` 和 `instances` 配置。

### 9.2 如何处理进程崩溃？

使用 `max_restarts`、`min_uptime` 配置自动重启。

### 9.3 如何优化性能？

使用集群模式、优化资源限制、监控性能。

## 10. 实践任务

1. **安装配置**：安装和配置 PM2
2. **启动应用**：使用 PM2 启动应用
3. **集群模式**：配置集群模式
4. **监控日志**：配置监控和日志
5. **持续优化**：持续优化 PM2 配置

---

**下一节**：[9.4.3 systemd](section-03-systemd.md)
