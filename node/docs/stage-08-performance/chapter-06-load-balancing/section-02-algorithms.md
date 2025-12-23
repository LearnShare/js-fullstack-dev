# 8.6.2 负载均衡算法

## 1. 概述

负载均衡算法决定了如何将请求分发到后端服务器，不同的算法适用于不同的场景。理解各种算法对于选择合适的负载均衡策略至关重要。

## 2. 轮询（Round Robin）

### 2.1 工作原理

按顺序依次将请求分发到每个服务器。

### 2.2 实现

```ts
class RoundRobinBalancer {
  private servers: string[];
  private currentIndex: number = 0;
  
  constructor(servers: string[]) {
    this.servers = servers;
  }
  
  getNextServer(): string {
    const server = this.servers[this.currentIndex];
    this.currentIndex = (this.currentIndex + 1) % this.servers.length;
    return server;
  }
}
```

### 2.3 优缺点

**优点**：简单、公平分配

**缺点**：不考虑服务器负载

## 3. 加权轮询（Weighted Round Robin）

### 3.1 工作原理

根据服务器权重分配请求。

### 3.2 实现

```ts
interface Server {
  url: string;
  weight: number;
}

class WeightedRoundRobinBalancer {
  private servers: Server[];
  private currentIndex: number = 0;
  private currentWeight: number = 0;
  
  constructor(servers: Server[]) {
    this.servers = servers;
  }
  
  getNextServer(): string {
    while (true) {
      this.currentIndex = (this.currentIndex + 1) % this.servers.length;
      
      if (this.currentIndex === 0) {
        this.currentWeight -= this.getGCD();
        if (this.currentWeight <= 0) {
          this.currentWeight = this.getMaxWeight();
        }
      }
      
      if (this.servers[this.currentIndex].weight >= this.currentWeight) {
        return this.servers[this.currentIndex].url;
      }
    }
  }
  
  private getMaxWeight(): number {
    return Math.max(...this.servers.map(s => s.weight));
  }
  
  private getGCD(): number {
    // 计算最大公约数
    return 1;
  }
}
```

## 4. 最少连接（Least Connections）

### 4.1 工作原理

将请求分发到当前连接数最少的服务器。

### 4.2 实现

```ts
class LeastConnectionsBalancer {
  private servers: Map<string, number> = new Map();
  
  constructor(serverUrls: string[]) {
    for (const url of serverUrls) {
      this.servers.set(url, 0);
    }
  }
  
  getNextServer(): string {
    let minConnections = Infinity;
    let selectedServer = '';
    
    for (const [url, connections] of this.servers.entries()) {
      if (connections < minConnections) {
        minConnections = connections;
        selectedServer = url;
      }
    }
    
    this.servers.set(selectedServer, minConnections + 1);
    return selectedServer;
  }
  
  releaseConnection(server: string): void {
    const connections = this.servers.get(server) || 0;
    this.servers.set(server, Math.max(0, connections - 1));
  }
}
```

## 5. IP 哈希（IP Hash）

### 5.1 工作原理

根据客户端 IP 计算哈希值，将同一 IP 的请求分发到同一服务器。

### 5.2 实现

```ts
import { createHash } from 'node:crypto';

class IPHashBalancer {
  private servers: string[];
  
  constructor(servers: string[]) {
    this.servers = servers;
  }
  
  getServer(ip: string): string {
    const hash = createHash('md5').update(ip).digest('hex');
    const index = parseInt(hash.substring(0, 8), 16) % this.servers.length;
    return this.servers[index];
  }
}
```

## 6. 算法选择

### 6.1 选择建议

- **轮询**：服务器性能相近
- **加权轮询**：服务器性能不同
- **最少连接**：连接持续时间不同
- **IP 哈希**：需要会话保持

## 7. 最佳实践

### 7.1 算法设计

- 根据场景选择算法
- 考虑服务器性能
- 实现健康检查
- 监控负载分布

## 8. 注意事项

- **会话保持**：使用 IP 哈希或粘性会话
- **健康检查**：排除不健康服务器
- **动态调整**：根据负载动态调整

## 9. 常见问题

### 9.1 如何选择算法？

根据服务器性能、请求特性、会话需求选择。

### 9.2 如何处理服务器故障？

使用健康检查、自动移除故障服务器。

### 9.3 如何优化负载分布？

使用加权算法、动态调整权重、监控负载。

## 10. 实践任务

1. **实现算法**：实现负载均衡算法
2. **性能测试**：测试不同算法性能
3. **健康检查**：实现健康检查
4. **动态调整**：实现动态调整
5. **持续优化**：持续优化负载均衡

---

**下一节**：[8.6.3 Nginx 负载均衡](section-03-nginx.md)
