# 9.4.3 systemd

## 1. 概述

systemd 是 Linux 系统的初始化系统和服务管理器，可以管理系统服务、实现开机自启、管理资源、处理日志。systemd 是生产环境中管理 Node.js 应用的常用方式。

## 2. 服务文件

### 2.1 创建服务文件

```ini
# /etc/systemd/system/my-app.service
[Unit]
Description=My Node.js Application
After=network.target

[Service]
Type=simple
User=nodejs
WorkingDirectory=/app
Environment=NODE_ENV=production
Environment=PORT=3000
ExecStart=/usr/bin/node /app/dist/index.js
Restart=always
RestartSec=10
StandardOutput=journal
StandardError=journal
SyslogIdentifier=my-app

# 资源限制
LimitNOFILE=65536
MemoryLimit=1G
CPUQuota=200%

[Install]
WantedBy=multi-user.target
```

### 2.2 服务管理

```bash
# 重新加载 systemd
sudo systemctl daemon-reload

# 启动服务
sudo systemctl start my-app

# 停止服务
sudo systemctl stop my-app

# 重启服务
sudo systemctl restart my-app

# 查看状态
sudo systemctl status my-app

# 启用开机自启
sudo systemctl enable my-app

# 禁用开机自启
sudo systemctl disable my-app

# 查看日志
sudo journalctl -u my-app -f
```

## 3. 环境变量

### 3.1 环境文件

```bash
# /etc/my-app/env
NODE_ENV=production
DATABASE_URL=postgresql://...
REDIS_URL=redis://...
```

### 3.2 服务配置

```ini
[Service]
EnvironmentFile=/etc/my-app/env
ExecStart=/usr/bin/node /app/dist/index.js
```

## 4. 资源限制

### 4.1 内存限制

```ini
[Service]
MemoryLimit=1G
MemoryHigh=800M
```

### 4.2 CPU 限制

```ini
[Service]
CPUQuota=200%
CPUAccounting=true
```

## 5. 日志管理

### 5.1 Journal 日志

```bash
# 查看日志
sudo journalctl -u my-app

# 实时查看
sudo journalctl -u my-app -f

# 查看最近日志
sudo journalctl -u my-app -n 100

# 按时间查看
sudo journalctl -u my-app --since "2024-01-01" --until "2024-01-02"
```

### 5.2 日志轮转

```ini
# /etc/systemd/journald.conf
[Journal]
SystemMaxUse=1G
SystemKeepFree=2G
MaxRetentionSec=1month
```

## 6. 最佳实践

### 6.1 服务配置

- 使用非 root 用户
- 设置资源限制
- 配置自动重启
- 实现健康检查

### 6.2 日志管理

- 使用 journal 日志
- 配置日志轮转
- 监控日志大小
- 定期清理日志

## 7. 注意事项

- **用户权限**：使用非 root 用户
- **资源限制**：设置合理的资源限制
- **日志管理**：管理日志大小
- **安全配置**：注意安全配置

## 8. 常见问题

### 8.1 如何配置自动重启？

使用 `Restart=always` 和 `RestartSec`。

### 8.2 如何查看服务日志？

使用 `journalctl -u service-name`。

### 8.3 如何设置资源限制？

使用 `MemoryLimit`、`CPUQuota` 等配置。

## 9. 实践任务

1. **创建服务**：创建 systemd 服务文件
2. **配置服务**：配置服务参数
3. **管理服务**：管理服务生命周期
4. **监控日志**：监控服务日志
5. **持续优化**：持续优化服务配置

---

**下一章**：[9.5 监控与告警](../chapter-05-monitoring/readme.md)
