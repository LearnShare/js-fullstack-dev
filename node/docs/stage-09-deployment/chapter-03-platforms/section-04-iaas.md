# 9.3.4 IaaS（AWS EC2、DigitalOcean）

## 1. 概述

IaaS（Infrastructure as a Service）提供虚拟化基础设施，开发者需要管理操作系统、中间件和应用。AWS EC2 和 DigitalOcean 是流行的 IaaS 平台。

## 2. AWS EC2

### 2.1 特点

- **完全控制**：完全控制服务器
- **灵活配置**：灵活的资源配置
- **多种实例类型**：多种实例类型选择
- **集成服务**：与 AWS 服务集成

### 2.2 部署流程

```bash
# 1. 创建 EC2 实例
# 2. 配置安全组
# 3. SSH 连接到实例
ssh -i key.pem ubuntu@ec2-instance

# 4. 安装 Node.js
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# 5. 部署应用
git clone https://github.com/user/repo.git
cd repo
npm install
npm run build
npm start
```

### 2.3 使用 PM2

```bash
# 安装 PM2
npm install -g pm2

# 启动应用
pm2 start npm --name "app" -- start

# 保存配置
pm2 save

# 设置开机自启
pm2 startup
```

## 3. DigitalOcean

### 3.1 特点

- **简单易用**：简单的控制面板
- **价格透明**：透明的定价
- **快速部署**：快速创建实例
- **Droplet**：虚拟服务器

### 3.2 部署流程

```bash
# 1. 创建 Droplet
# 2. SSH 连接
ssh root@droplet-ip

# 3. 安装 Node.js
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# 4. 部署应用
git clone https://github.com/user/repo.git
cd repo
npm install
npm run build
pm2 start npm --name "app" -- start
```

## 4. 自动化部署

### 4.1 使用 Ansible

```yaml
# deploy.yml
- hosts: servers
  tasks:
    - name: Install Node.js
      apt:
        name: nodejs
        state: present
    
    - name: Clone repository
      git:
        repo: https://github.com/user/repo.git
        dest: /app
    
    - name: Install dependencies
      npm:
        path: /app
        state: present
    
    - name: Build application
      command: npm run build
      args:
        chdir: /app
    
    - name: Restart application
      systemd:
        name: app
        state: restarted
```

### 4.2 使用 Terraform

```hcl
# main.tf
resource "aws_instance" "app" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"
  
  user_data = <<-EOF
    #!/bin/bash
    apt-get update
    apt-get install -y nodejs npm
    npm install -g pm2
    # 部署应用
  EOF
}
```

## 5. 最佳实践

### 5.1 服务器配置

- 使用非 root 用户
- 配置防火墙
- 启用自动更新
- 配置监控

### 5.2 应用部署

- 使用进程管理
- 配置反向代理
- 启用 HTTPS
- 实现日志管理

## 6. 注意事项

- **安全性**：配置安全设置
- **备份**：定期备份数据
- **监控**：配置监控告警
- **成本**：注意资源成本

## 7. 常见问题

### 7.1 如何选择实例类型？

根据应用需求、性能要求、成本预算选择。

### 7.2 如何实现自动化部署？

使用 Ansible、Terraform、CI/CD 工具。

### 7.3 如何优化服务器性能？

优化应用、使用缓存、配置 CDN。

## 8. 实践任务

1. **创建实例**：创建 IaaS 实例
2. **配置服务器**：配置服务器环境
3. **部署应用**：部署应用到服务器
4. **自动化部署**：实现自动化部署
5. **持续优化**：持续优化服务器配置

---

**下一章**：[9.4 进程管理](../chapter-04-process/readme.md)
