# 9.7.2 Terraform

## 1. 概述

Terraform 是 HashiCorp 开发的基础设施即代码工具，使用声明式配置语言（HCL）定义基础设施，支持多云平台和丰富的 Provider。

## 2. 安装与配置

### 2.1 安装

```bash
# 下载 Terraform
wget https://releases.hashicorp.com/terraform/1.5.0/terraform_1.5.0_linux_amd64.zip
unzip terraform_1.5.0_linux_amd64.zip
sudo mv terraform /usr/local/bin/
```

### 2.2 基本配置

```hcl
# main.tf
terraform {
  required_version = ">= 1.0"
  
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}
```

## 3. 资源定义

### 3.1 EC2 实例

```hcl
resource "aws_instance" "app" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"
  
  tags = {
    Name = "my-app"
    Environment = "production"
  }
  
  user_data = <<-EOF
    #!/bin/bash
    apt-get update
    apt-get install -y nodejs npm
    npm install -g pm2
    # 部署应用
  EOF
}
```

### 3.2 安全组

```hcl
resource "aws_security_group" "app" {
  name        = "app-sg"
  description = "Security group for app"
  
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

## 4. 模块化

### 4.1 模块定义

```hcl
# modules/app/main.tf
variable "instance_type" {
  type = string
}

variable "environment" {
  type = string
}

resource "aws_instance" "app" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = var.instance_type
  
  tags = {
    Environment = var.environment
  }
}

output "instance_id" {
  value = aws_instance.app.id
}
```

### 4.2 模块使用

```hcl
# main.tf
module "app" {
  source = "./modules/app"
  
  instance_type = "t3.micro"
  environment   = "production"
}
```

## 5. 状态管理

### 5.1 远程状态

```hcl
terraform {
  backend "s3" {
    bucket = "my-terraform-state"
    key    = "production/terraform.tfstate"
    region = "us-east-1"
  }
}
```

## 6. 最佳实践

### 6.1 配置管理

- 使用模块化设计
- 分离环境配置
- 使用变量和输出
- 版本控制配置

### 6.2 状态管理

- 使用远程状态
- 状态锁定
- 定期备份
- 状态隔离

## 7. 注意事项

- **状态管理**：合理管理状态
- **安全性**：保护敏感信息
- **成本控制**：注意资源成本
- **变更管理**：谨慎处理变更

## 8. 常见问题

### 8.1 如何处理状态冲突？

使用状态锁定、远程状态、团队协作流程。

### 8.2 如何管理多环境？

使用工作空间、模块化、环境变量。

### 8.3 如何优化 Terraform 性能？

使用并行执行、优化配置、使用缓存。

## 9. 实践任务

1. **安装配置**：安装和配置 Terraform
2. **定义资源**：定义基础设施资源
3. **模块化设计**：实现模块化设计
4. **状态管理**：配置状态管理
5. **持续优化**：持续优化配置

---

**下一节**：[9.7.3 Pulumi](section-03-pulumi.md)
