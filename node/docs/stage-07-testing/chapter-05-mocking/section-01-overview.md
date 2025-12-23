# 7.5.1 Mock 与 Stub 概述

## 1. 概述

Mock 和 Stub 是测试中的重要技术，用于隔离被测试代码的依赖，使测试更加独立和可控。理解 Mock 和 Stub 的区别对于正确使用它们至关重要。

## 2. 核心概念

### 2.1 Mock

**定义**：Mock 是模拟对象，用于验证交互。

**特点**：
- 验证方法调用
- 记录调用信息
- 验证调用参数
- 验证调用次数

**示例**：
```ts
const mockFn = vi.fn();
mockFn('arg1', 'arg2');
expect(mockFn).toHaveBeenCalledWith('arg1', 'arg2');
expect(mockFn).toHaveBeenCalledTimes(1);
```

### 2.2 Stub

**定义**：Stub 是桩对象，用于替换依赖。

**特点**：
- 替换真实实现
- 返回预设值
- 不验证交互
- 简化测试

**示例**：
```ts
const stubFn = vi.fn().mockReturnValue(42);
const result = stubFn();
expect(result).toBe(42);
```

## 3. Mock vs Stub

### 3.1 区别

| 特性 | Mock | Stub |
|------|------|------|
| 目的 | 验证交互 | 替换依赖 |
| 验证 | 验证调用 | 不验证调用 |
| 返回值 | 可设置 | 必须设置 |
| 使用场景 | 验证行为 | 隔离依赖 |

### 3.2 选择建议

- **验证交互**：使用 Mock
- **隔离依赖**：使用 Stub
- **两者结合**：根据需求结合使用

## 4. 使用场景

### 4.1 Mock 使用场景

- 验证函数调用
- 验证调用参数
- 验证调用次数
- 验证调用顺序

### 4.2 Stub 使用场景

- 替换外部依赖
- 模拟网络请求
- 模拟数据库操作
- 模拟文件系统

## 5. 最佳实践

### 5.1 Mock 使用

- 只 Mock 外部依赖
- 避免过度 Mock
- 使用真实实现
- 验证关键交互

### 5.2 Stub 使用

- 替换慢速操作
- 替换不稳定依赖
- 简化测试数据
- 隔离测试环境

## 6. 注意事项

- **适度使用**：避免过度使用 Mock
- **真实实现**：优先使用真实实现
- **测试质量**：Mock 不应降低测试质量
- **维护成本**：考虑 Mock 的维护成本

## 7. 常见问题

### 7.1 何时使用 Mock？

需要验证交互时使用 Mock。

### 7.2 何时使用 Stub？

需要隔离依赖时使用 Stub。

### 7.3 如何避免过度 Mock？

只 Mock 外部依赖，优先使用真实实现。

## 8. 相关资源

- [Mock 对象](https://en.wikipedia.org/wiki/Mock_object)
- [测试替身](https://martinfowler.com/bliki/TestDouble.html)

---

**下一节**：[7.5.2 Mock 基础](section-02-basics.md)
