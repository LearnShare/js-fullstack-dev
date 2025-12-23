# 7.2.1 单元测试概述

## 1. 概述

单元测试是对代码最小单元（函数、方法、类）的测试，在隔离环境中执行，不依赖外部资源。单元测试是测试金字塔的基础，是保证代码质量的重要手段。

## 2. 核心概念

### 2.1 单元定义

- **函数**：独立的函数
- **方法**：类的方法
- **类**：完整的类
- **模块**：独立的模块

### 2.2 测试特点

- **快速**：执行速度快
- **隔离**：独立执行，不依赖外部
- **可重复**：结果可重复
- **自动化**：可以自动化执行

## 3. 单元测试结构

### 3.1 AAA 模式

```ts
import { describe, it, expect } from 'vitest';

describe('functionName', () => {
  it('should do something', () => {
    // Arrange（准备）：准备测试数据
    const input = 'test';
    
    // Act（执行）：执行被测试代码
    const result = functionName(input);
    
    // Assert（断言）：验证结果
    expect(result).toBe('expected');
  });
});
```

### 3.2 测试组织

```ts
describe('Calculator', () => {
  describe('add', () => {
    it('should add two positive numbers', () => {
      expect(add(1, 2)).toBe(3);
    });
    
    it('should add negative numbers', () => {
      expect(add(-1, -2)).toBe(-3);
    });
  });
  
  describe('subtract', () => {
    it('should subtract two numbers', () => {
      expect(subtract(5, 3)).toBe(2);
    });
  });
});
```

## 4. 测试用例设计

### 4.1 测试场景

- **正常情况**：正常输入和输出
- **边界情况**：边界值测试
- **异常情况**：错误输入和异常处理
- **特殊情况**：空值、null、undefined

### 4.2 示例

```ts
describe('divide', () => {
  it('should divide two numbers', () => {
    expect(divide(10, 2)).toBe(5);
  });
  
  it('should handle division by zero', () => {
    expect(() => divide(10, 0)).toThrow('Division by zero');
  });
  
  it('should handle negative numbers', () => {
    expect(divide(-10, 2)).toBe(-5);
  });
});
```

## 5. 最佳实践

### 5.1 测试编写

- 测试应该简单
- 测试应该独立
- 测试应该快速
- 测试应该可读

### 5.2 测试命名

- 使用描述性名称
- 描述测试场景
- 使用 should/will 开头
- 避免实现细节

## 6. 注意事项

- **测试隔离**：每个测试应该独立
- **测试数据**：使用测试数据而非生产数据
- **Mock 使用**：合理使用 Mock
- **测试维护**：及时维护测试代码

## 7. 常见问题

### 7.1 如何编写好的单元测试？

遵循 AAA 模式，测试应该简单、独立、快速、可读。

### 7.2 如何选择测试框架？

根据项目需求、团队经验、工具特性选择。

### 7.3 如何处理测试依赖？

使用 Mock 和 Stub 隔离依赖。

## 8. 相关资源

- [单元测试](https://en.wikipedia.org/wiki/Unit_testing)
- [测试驱动开发](https://en.wikipedia.org/wiki/Test-driven_development)

---

**下一节**：[7.2.2 Vitest（现代测试框架）](section-02-vitest.md)
