# 7.5.2 Mock 基础

## 1. 概述

Mock 基础包括 Mock 函数、Mock 模块、Mock 对象等基本概念和使用方法。掌握 Mock 基础是使用高级 Mock 工具的前提。

## 2. Mock 函数

### 2.1 Vitest Mock

```ts
import { describe, it, expect, vi } from 'vitest';

describe('Mock Functions', () => {
  it('should create a mock function', (): void => {
    const mockFn = vi.fn();
    mockFn('arg1', 'arg2');
    
    expect(mockFn).toHaveBeenCalled();
    expect(mockFn).toHaveBeenCalledWith('arg1', 'arg2');
    expect(mockFn).toHaveBeenCalledTimes(1);
  });
  
  it('should return a value', (): void => {
    const mockFn = vi.fn().mockReturnValue(42);
    expect(mockFn()).toBe(42);
  });
  
  it('should return different values', (): void => {
    const mockFn = vi.fn()
      .mockReturnValueOnce(1)
      .mockReturnValueOnce(2)
      .mockReturnValue(3);
    
    expect(mockFn()).toBe(1);
    expect(mockFn()).toBe(2);
    expect(mockFn()).toBe(3);
    expect(mockFn()).toBe(3);
  });
  
  it('should throw an error', (): void => {
    const mockFn = vi.fn().mockImplementation(() => {
      throw new Error('Mock error');
    });
    
    expect(() => mockFn()).toThrow('Mock error');
  });
});
```

### 2.2 Jest Mock

```ts
import { jest } from '@jest/globals';

describe('Mock Functions', () => {
  it('should create a mock function', (): void => {
    const mockFn = jest.fn();
    mockFn('arg1', 'arg2');
    
    expect(mockFn).toHaveBeenCalled();
    expect(mockFn).toHaveBeenCalledWith('arg1', 'arg2');
    expect(mockFn).toHaveBeenCalledTimes(1);
  });
  
  it('should return a value', (): void => {
    const mockFn = jest.fn().mockReturnValue(42);
    expect(mockFn()).toBe(42);
  });
});
```

## 3. Mock 模块

### 3.1 Vitest Mock 模块

```ts
import { describe, it, expect, vi } from 'vitest';

// Mock 整个模块
vi.mock('./api', () => ({
  fetchUser: vi.fn().mockResolvedValue({ id: 1, name: 'John' }),
  createUser: vi.fn().mockResolvedValue({ id: 2, name: 'Jane' })
}));

import { fetchUser, createUser } from './api';

describe('User Service', () => {
  it('should fetch user', async (): Promise<void> => {
    const user = await fetchUser(1);
    expect(user).toEqual({ id: 1, name: 'John' });
    expect(fetchUser).toHaveBeenCalledWith(1);
  });
});
```

### 3.2 部分 Mock

```ts
import { vi } from 'vitest';
import * as api from './api';

// 部分 Mock
vi.spyOn(api, 'fetchUser').mockResolvedValue({ id: 1, name: 'John' });

// 其他函数保持原样
const result = await api.createUser({ name: 'Jane' }); // 真实实现
```

## 4. Mock 对象

### 4.1 对象 Mock

```ts
import { describe, it, expect, vi } from 'vitest';

const mockUser = {
  id: 1,
  name: 'John',
  email: 'john@example.com',
  getName: vi.fn().mockReturnValue('John'),
  getEmail: vi.fn().mockReturnValue('john@example.com')
};

describe('Mock Object', () => {
  it('should use mock object', (): void => {
    expect(mockUser.getName()).toBe('John');
    expect(mockUser.getName).toHaveBeenCalled();
  });
});
```

### 4.2 类 Mock

```ts
import { describe, it, expect, vi } from 'vitest';

class UserService {
  async getUser(id: number): Promise<any> {
    // 真实实现
  }
}

// Mock 类方法
const mockGetUser = vi.fn().mockResolvedValue({ id: 1, name: 'John' });
UserService.prototype.getUser = mockGetUser;

describe('UserService', () => {
  it('should get user', async (): Promise<void> => {
    const service = new UserService();
    const user = await service.getUser(1);
    expect(user).toEqual({ id: 1, name: 'John' });
  });
});
```

## 5. 时间 Mock

### 5.1 日期 Mock

```ts
import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';

describe('Date Mock', () => {
  beforeEach((): void => {
    vi.useFakeTimers();
  });
  
  afterEach((): void => {
    vi.useRealTimers();
  });
  
  it('should mock date', (): void => {
    const mockDate = new Date('2024-01-01');
    vi.setSystemTime(mockDate);
    
    const now = new Date();
    expect(now.getTime()).toBe(mockDate.getTime());
  });
  
  it('should advance time', (): void => {
    const callback = vi.fn();
    setTimeout(callback, 1000);
    
    vi.advanceTimersByTime(1000);
    expect(callback).toHaveBeenCalled();
  });
});
```

## 6. 最佳实践

### 6.1 Mock 使用

- 只 Mock 外部依赖
- 保持 Mock 简单
- 验证关键交互
- 及时清理 Mock

### 6.2 测试组织

- 使用 beforeEach/afterEach
- 隔离 Mock 状态
- 使用描述性名称
- 组织 Mock 代码

## 7. 注意事项

- **适度使用**：避免过度使用 Mock
- **真实实现**：优先使用真实实现
- **Mock 清理**：及时清理 Mock 状态
- **测试维护**：及时维护 Mock 代码

## 8. 常见问题

### 8.1 如何选择 Mock 方式？

根据依赖类型、测试需求、工具特性选择。

### 8.2 如何处理异步 Mock？

使用 `mockResolvedValue` 或 `mockRejectedValue`。

### 8.3 如何清理 Mock？

使用 `vi.restoreAllMocks()` 或 `jest.clearAllMocks()`。

## 9. 实践任务

1. **Mock 函数**：创建和使用 Mock 函数
2. **Mock 模块**：Mock 模块和部分 Mock
3. **Mock 对象**：Mock 对象和类
4. **时间 Mock**：Mock 时间和定时器
5. **最佳实践**：遵循 Mock 最佳实践

---

**下一节**：[7.5.3 Sinon.js](section-03-sinon.md)
