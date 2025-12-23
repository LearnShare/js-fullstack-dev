# 9.7.3 Pulumi

## 1. 概述

Pulumi 是使用通用编程语言定义基础设施的工具，支持 TypeScript、Python、Go 等语言，提供类型安全和丰富的库。

## 2. 安装与配置

### 2.1 安装

```bash
# 安装 Pulumi CLI
curl -fsSL https://get.pulumi.com | sh

# 验证安装
pulumi version
```

### 2.2 初始化项目

```bash
# 创建新项目
pulumi new typescript

# 选择模板和配置
```

## 3. TypeScript 实现

### 3.1 基本资源

```ts
// index.ts
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

// 创建 VPC
const vpc = new aws.ec2.Vpc("my-vpc", {
  cidrBlock: "10.0.0.0/16",
  tags: {
    Name: "my-vpc"
  }
});

// 创建子网
const subnet = new aws.ec2.Subnet("my-subnet", {
  vpcId: vpc.id,
  cidrBlock: "10.0.1.0/24",
  availabilityZone: "us-east-1a",
  tags: {
    Name: "my-subnet"
  }
});

// 创建 EC2 实例
const instance = new aws.ec2.Instance("my-app", {
  ami: "ami-0c55b159cbfafe1f0",
  instanceType: "t3.micro",
  subnetId: subnet.id,
  tags: {
    Name: "my-app"
  },
  userData: `#!/bin/bash
    apt-get update
    apt-get install -y nodejs npm
    npm install -g pm2
  `
});

export const instanceId = instance.id;
export const publicIp = instance.publicIp;
```

## 4. 组件和模块

### 4.1 组件定义

```ts
// components/app.ts
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

interface AppComponentArgs {
  instanceType: string;
  environment: string;
}

export class AppComponent extends pulumi.ComponentResource {
  public readonly instanceId: pulumi.Output<string>;
  
  constructor(name: string, args: AppComponentArgs, opts?: pulumi.ComponentResourceOptions) {
    super("custom:App", name, args, opts);
    
    const instance = new aws.ec2.Instance(`${name}-instance`, {
      ami: "ami-0c55b159cbfafe1f0",
      instanceType: args.instanceType,
      tags: {
        Environment: args.environment
      }
    }, { parent: this });
    
    this.instanceId = instance.id;
    
    this.registerOutputs({
      instanceId: this.instanceId
    });
  }
}
```

### 4.2 组件使用

```ts
// index.ts
import { AppComponent } from "./components/app";

const app = new AppComponent("my-app", {
  instanceType: "t3.micro",
  environment: "production"
});

export const instanceId = app.instanceId;
```

## 5. 配置管理

### 5.1 配置

```bash
# 设置配置
pulumi config set aws:region us-east-1
pulumi config set instanceType t3.micro

# 查看配置
pulumi config
```

### 5.2 使用配置

```ts
import * as pulumi from "@pulumi/pulumi";

const config = new pulumi.Config();
const instanceType = config.get("instanceType") || "t3.micro";
const region = config.require("aws:region");
```

## 6. 最佳实践

### 6.1 代码组织

- 使用组件和模块
- 分离环境配置
- 类型安全
- 代码复用

### 6.2 状态管理

- 使用 Pulumi Cloud
- 状态锁定
- 定期备份
- 状态隔离

## 7. 注意事项

- **类型安全**：利用类型系统
- **状态管理**：合理管理状态
- **成本控制**：注意资源成本
- **变更管理**：谨慎处理变更

## 8. 常见问题

### 8.1 如何选择语言？

根据团队技能、项目需求、生态支持选择。

### 8.2 如何处理状态管理？

使用 Pulumi Cloud、自托管后端、状态锁定。

### 8.3 如何优化性能？

使用并行执行、优化代码、使用缓存。

## 9. 实践任务

1. **安装配置**：安装和配置 Pulumi
2. **定义资源**：使用 TypeScript 定义资源
3. **组件设计**：实现组件化设计
4. **状态管理**：配置状态管理
5. **持续优化**：持续优化代码

---

**下一章**：[9.8 部署策略](../chapter-08-deployment-strategies/readme.md)
