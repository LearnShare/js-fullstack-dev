# 7.8.2 压力测试与负载测试

## 1. 概述

压力测试和负载测试是性能测试的重要类型，用于测试系统在不同负载下的表现。理解压力测试和负载测试的区别对于正确进行性能测试至关重要。

## 2. 负载测试

### 2.1 定义和目的

**定义**：在正常和预期负载下测试应用性能。

**目的**：
- 验证系统在正常负载下的表现
- 确定性能基准
- 发现性能问题

### 2.2 测试场景

```ts
// 负载测试场景
interface LoadTestScenario {
  name: string;
  duration: number; // 测试持续时间（秒）
  rampUp: number; // 逐步增加用户数
  users: number; // 目标用户数
  requests: Array<{
    method: string;
    url: string;
    weight: number; // 请求权重
  }>;
}

const scenario: LoadTestScenario = {
  name: '正常负载测试',
  duration: 300, // 5 分钟
  rampUp: 60, // 1 分钟内增加到目标用户数
  users: 100, // 100 个并发用户
  requests: [
    { method: 'GET', url: '/api/users', weight: 50 },
    { method: 'POST', url: '/api/users', weight: 30 },
    { method: 'GET', url: '/api/users/:id', weight: 20 }
  ]
};
```

## 3. 压力测试

### 3.1 定义和目的

**定义**：在超过正常负载的情况下测试应用。

**目的**：
- 确定系统极限
- 测试系统恢复能力
- 发现系统崩溃点

### 3.2 测试场景

```ts
// 压力测试场景
const stressScenario: LoadTestScenario = {
  name: '压力测试',
  duration: 600, // 10 分钟
  rampUp: 120, // 2 分钟内逐步增加
  users: 500, // 500 个并发用户（超过正常负载）
  requests: [
    { method: 'GET', url: '/api/users', weight: 50 },
    { method: 'POST', url: '/api/users', weight: 30 },
    { method: 'GET', url: '/api/users/:id', weight: 20 }
  ]
};
```

## 4. 测试实施

### 4.1 测试准备

```ts
interface TestConfig {
  baseURL: string;
  duration: number;
  users: number;
  rampUp: number;
  metrics: {
    responseTime: {
      p95: number;
      p99: number;
    };
    errorRate: number;
    throughput: number;
  };
}

const config: TestConfig = {
  baseURL: 'http://localhost:3000',
  duration: 300,
  users: 100,
  rampUp: 60,
  metrics: {
    responseTime: {
      p95: 500, // P95 响应时间 < 500ms
      p99: 1000 // P99 响应时间 < 1000ms
    },
    errorRate: 0.01, // 错误率 < 1%
    throughput: 1000 // 吞吐量 > 1000 req/s
  }
};
```

### 4.2 测试执行

```ts
async function runLoadTest(config: TestConfig): Promise<void> {
  const startTime = Date.now();
  const results: Array<{ timestamp: number; responseTime: number; status: number }> = [];
  
  // 逐步增加用户
  for (let i = 0; i < config.users; i++) {
    setTimeout(async () => {
      const user = createVirtualUser(config.baseURL);
      await user.run(config.duration);
    }, (config.rampUp / config.users) * i * 1000);
  }
  
  // 收集结果
  // ...
  
  // 验证指标
  validateMetrics(results, config.metrics);
}
```

## 5. 结果分析

### 5.1 性能指标

```ts
interface PerformanceMetrics {
  totalRequests: number;
  successfulRequests: number;
  failedRequests: number;
  averageResponseTime: number;
  p95ResponseTime: number;
  p99ResponseTime: number;
  requestsPerSecond: number;
  errorRate: number;
}

function analyzeResults(results: any[]): PerformanceMetrics {
  const total = results.length;
  const successful = results.filter((r: any) => r.status < 400).length;
  const failed = total - successful;
  
  const responseTimes = results.map((r: any) => r.responseTime).sort((a: number, b: number) => a - b);
  const p95Index = Math.floor(total * 0.95);
  const p99Index = Math.floor(total * 0.99);
  
  return {
    totalRequests: total,
    successfulRequests: successful,
    failedRequests: failed,
    averageResponseTime: responseTimes.reduce((a: number, b: number) => a + b, 0) / total,
    p95ResponseTime: responseTimes[p95Index],
    p99ResponseTime: responseTimes[p99Index],
    requestsPerSecond: total / (results[results.length - 1].timestamp - results[0].timestamp) * 1000,
    errorRate: failed / total
  };
}
```

## 6. 最佳实践

### 6.1 测试设计

- 模拟真实场景
- 逐步增加负载
- 监控关键指标
- 记录测试数据

### 6.2 结果分析

- 分析性能指标
- 识别性能瓶颈
- 对比基准数据
- 提出优化建议

## 7. 注意事项

- **环境准备**：使用接近生产的环境
- **数据准备**：准备足够的测试数据
- **监控指标**：监控关键性能指标
- **结果分析**：深入分析测试结果

## 8. 常见问题

### 8.1 如何确定负载水平？

根据业务需求、历史数据、预期增长确定。

### 8.2 如何处理测试结果？

分析性能指标，识别瓶颈，提出优化建议。

### 8.3 如何优化性能？

根据测试结果，优化代码、配置、架构。

## 9. 实践任务

1. **设计场景**：设计负载和压力测试场景
2. **执行测试**：执行性能测试
3. **收集数据**：收集性能数据
4. **分析结果**：分析测试结果
5. **优化改进**：根据结果优化性能

---

**下一节**：[7.8.3 k6 与 Artillery](section-03-tools.md)
