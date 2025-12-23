# 7.8.3 k6 与 Artillery

## 1. 概述

k6 和 Artillery 是常用的性能测试工具，提供了强大的性能测试功能和丰富的指标报告。本章介绍这两个工具的使用方法。

## 2. k6

### 2.1 安装

```bash
npm install -D k6
```

### 2.2 基本使用

```ts
// load-test.js
import http from 'k6/http';
import { check, sleep } from 'k6';
import { Rate } from 'k6/metrics';

const errorRate = new Rate('errors');

export const options = {
  stages: [
    { duration: '30s', target: 20 }, // 30 秒内增加到 20 个用户
    { duration: '1m', target: 20 },  // 保持 20 个用户 1 分钟
    { duration: '30s', target: 0 },  // 30 秒内减少到 0
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'], // P95 < 500ms
    http_req_failed: ['rate<0.01'],   // 错误率 < 1%
    errors: ['rate<0.1'],
  },
};

export default function (): void {
  const response = http.get('http://localhost:3000/api/users');
  
  const result = check(response, {
    'status is 200': (r: any) => r.status === 200,
    'response time < 500ms': (r: any) => r.timings.duration < 500,
  });
  
  errorRate.add(!result);
  
  sleep(1);
}
```

### 2.3 运行测试

```bash
# 运行测试
k6 run load-test.js

# 使用更多虚拟用户
k6 run --vus 100 --duration 5m load-test.js

# 分布式执行
k6 run --out cloud load-test.js
```

### 2.4 高级特性

```ts
import http from 'k6/http';
import { SharedArray } from 'k6/data';

// 共享测试数据
const users = new SharedArray('users', function () {
  return [
    { id: 1, name: 'John' },
    { id: 2, name: 'Jane' }
  ];
});

export default function (): void {
  const user = users[Math.floor(Math.random() * users.length)];
  const response = http.get(`http://localhost:3000/api/users/${user.id}`);
  check(response, { 'status is 200': (r: any) => r.status === 200 });
}
```

## 3. Artillery

### 3.1 安装

```bash
npm install -D artillery
```

### 3.2 配置文件

```yaml
# artillery.yml
config:
  target: "http://localhost:3000"
  phases:
    - duration: 60
      arrivalRate: 10
      name: "Warm up"
    - duration: 300
      arrivalRate: 50
      name: "Sustained load"
    - duration: 60
      arrivalRate: 100
      name: "Spike test"
  processor: "./processor.js"

scenarios:
  - name: "User flow"
    flow:
      - get:
          url: "/api/users"
      - think: 2
      - post:
          url: "/api/users"
          json:
            name: "{{ $randomString() }}"
            email: "{{ $randomEmail() }}"
      - get:
          url: "/api/users/{{ userId }}"
```

### 3.3 运行测试

```bash
# 运行测试
artillery run artillery.yml

# 生成报告
artillery run --output report.json artillery.yml
artillery report report.json
```

### 3.4 处理器

```ts
// processor.js
module.exports = {
  generateUser: function generateUser(context: any, events: any, done: any): void {
    context.vars.userId = Math.floor(Math.random() * 1000);
    return done();
  }
};
```

## 4. 工具对比

### 4.1 k6 vs Artillery

| 特性 | k6 | Artillery |
|------|----|-----------|
| 语言 | JavaScript | YAML + JavaScript |
| 性能 | 高性能 | 中等性能 |
| 学习曲线 | 中等 | 简单 |
| 报告 | 丰富 | 基础 |
| 分布式 | 支持 | 支持 |

### 4.2 选择建议

- **高性能需求**：使用 k6
- **简单配置**：使用 Artillery
- **JavaScript 偏好**：使用 k6
- **YAML 偏好**：使用 Artillery

## 5. 最佳实践

### 5.1 测试设计

- 模拟真实场景
- 逐步增加负载
- 设置合理阈值
- 监控关键指标

### 5.2 结果分析

- 分析性能指标
- 识别性能瓶颈
- 对比基准数据
- 提出优化建议

## 6. 注意事项

- **环境准备**：使用接近生产的环境
- **数据准备**：准备足够的测试数据
- **监控指标**：监控关键性能指标
- **结果分析**：深入分析测试结果

## 7. 常见问题

### 7.1 如何选择工具？

根据性能需求、团队经验、工具特性选择。

### 7.2 如何优化测试性能？

使用分布式执行、优化测试脚本、减少网络延迟。

### 7.3 如何处理测试结果？

分析性能指标，识别瓶颈，提出优化建议。

## 8. 实践任务

1. **安装工具**：安装 k6 或 Artillery
2. **编写测试**：编写性能测试脚本
3. **执行测试**：执行性能测试
4. **分析结果**：分析测试结果
5. **优化性能**：根据结果优化性能

---

**下一章**：[7.9 代码覆盖率深入](../chapter-09-coverage/readme.md)
