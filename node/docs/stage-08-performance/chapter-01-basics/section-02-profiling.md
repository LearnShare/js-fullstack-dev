# 8.1.2 性能分析工具

## 1. 概述

性能分析工具用于识别性能瓶颈、分析代码执行时间和资源使用情况。Node.js 提供了多种性能分析工具，帮助开发者优化应用性能。

## 2. Node.js 内置工具

### 2.1 Node.js Profiler

**使用**：
```bash
# 生成性能分析文件
node --prof app.js

# 处理分析文件
node --prof-process isolate-*.log > processed.txt
```

### 2.2 性能钩子（Performance Hooks）

```ts
import { performance, PerformanceObserver } from 'node:perf_hooks';

// 创建性能观察器
const obs = new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    console.log(`${entry.name}: ${entry.duration}ms`);
  }
});

obs.observe({ entryTypes: ['measure', 'function'] });

// 测量代码执行时间
performance.mark('start');
// 执行代码
performance.mark('end');
performance.measure('operation', 'start', 'end');
```

### 2.3 性能计时器

```ts
import { performance } from 'node:perf_hooks';

function measureFunction<T>(fn: () => T, name: string): T {
  const start = performance.now();
  const result = fn();
  const end = performance.now();
  console.log(`${name} took ${(end - start).toFixed(2)}ms`);
  return result;
}

// 使用
const result = measureFunction(() => {
  // 执行代码
  return computeSomething();
}, 'computeSomething');
```

## 3. 第三方工具

### 3.1 clinic.js

**安装**：
```bash
npm install -g clinic
```

**使用**：
```bash
# CPU 分析
clinic doctor -- node app.js

# 内存分析
clinic heapprofiler -- node app.js

# 事件循环分析
clinic bubbleprof -- node app.js
```

### 3.2 0x

**安装**：
```bash
npm install -g 0x
```

**使用**：
```bash
# 生成火焰图
0x app.js
```

### 3.3 autocannon

**安装**：
```bash
npm install -g autocannon
```

**使用**：
```bash
# 压力测试
autocannon -c 100 -d 30 http://localhost:3000
```

## 4. Chrome DevTools

### 4.1 CPU 分析

```bash
# 启动 Node.js 并启用检查器
node --inspect app.js

# 在 Chrome 中打开 chrome://inspect
```

### 4.2 内存分析

```ts
// 生成堆快照
import { writeHeapSnapshot } from 'node:v8';

function takeHeapSnapshot(): string {
  const filename = writeHeapSnapshot();
  console.log(`Heap snapshot written to ${filename}`);
  return filename;
}

// 定期生成快照
setInterval(() => {
  takeHeapSnapshot();
}, 60000); // 每分钟
```

## 5. 性能分析实践

### 5.1 识别热点

```ts
import { performance } from 'node:perf_hooks';

class Profiler {
  private timings: Map<string, number[]> = new Map();
  
  start(name: string): void {
    performance.mark(`${name}-start`);
  }
  
  end(name: string): void {
    performance.mark(`${name}-end`);
    performance.measure(name, `${name}-start`, `${name}-end`);
    
    const measure = performance.getEntriesByName(name, 'measure')[0];
    if (!this.timings.has(name)) {
      this.timings.set(name, []);
    }
    this.timings.get(name)!.push(measure.duration);
  }
  
  getReport(): Record<string, { avg: number; min: number; max: number }> {
    const report: Record<string, { avg: number; min: number; max: number }> = {};
    
    for (const [name, timings] of this.timings.entries()) {
      const sum = timings.reduce((a, b) => a + b, 0);
      report[name] = {
        avg: sum / timings.length,
        min: Math.min(...timings),
        max: Math.max(...timings)
      };
    }
    
    return report;
  }
}

// 使用
const profiler = new Profiler();

profiler.start('database-query');
await db.query('SELECT * FROM users');
profiler.end('database-query');

console.log(profiler.getReport());
```

### 5.2 内存泄漏检测

```ts
import { performance, PerformanceObserver } from 'node:perf_hooks';
import { memoryUsage } from 'node:process';

class MemoryMonitor {
  private baseline: NodeJS.MemoryUsage;
  
  constructor() {
    this.baseline = memoryUsage();
  }
  
  check(): void {
    const current = memoryUsage();
    const heapUsedDiff = current.heapUsed - this.baseline.heapUsed;
    const heapUsedDiffMB = heapUsedDiff / 1024 / 1024;
    
    if (heapUsedDiffMB > 100) {
      console.warn(`Memory increase: ${heapUsedDiffMB.toFixed(2)} MB`);
    }
  }
}

// 使用
const monitor = new MemoryMonitor();
setInterval(() => monitor.check(), 5000);
```

## 6. 最佳实践

### 6.1 分析策略

- 先测量，后优化
- 识别真正的瓶颈
- 使用多种工具
- 持续监控

### 6.2 工具选择

- **CPU 分析**：使用 clinic.js 或 Chrome DevTools
- **内存分析**：使用 heap profiler
- **I/O 分析**：使用性能钩子
- **压力测试**：使用 autocannon 或 k6

## 7. 注意事项

- **性能开销**：分析工具本身有性能开销
- **生产环境**：谨慎在生产环境使用
- **数据解读**：正确解读分析数据
- **持续优化**：基于分析结果持续优化

## 8. 常见问题

### 8.1 如何选择分析工具？

根据分析目标、环境、工具特性选择。

### 8.2 如何解读火焰图？

查看最宽的部分，这些是性能瓶颈。

### 8.3 如何处理内存泄漏？

使用堆快照对比，查找未释放的对象。

## 9. 实践任务

1. **使用工具**：使用性能分析工具分析应用
2. **识别瓶颈**：识别性能瓶颈
3. **优化代码**：基于分析结果优化代码
4. **验证效果**：验证优化效果
5. **持续监控**：建立持续监控机制

---

**下一章**：[8.2 代码优化](../chapter-02-code/readme.md)
