# 7.5.3 Sinon.js

## 1. 概述

Sinon.js 是一个强大的 JavaScript Mock 库，提供了 Spy、Stub、Mock 等功能。Sinon.js 可以与任何测试框架配合使用，是 Node.js 测试中常用的 Mock 工具。

## 2. 特性说明

- **Spy**：监视函数调用
- **Stub**：替换函数实现
- **Mock**：组合 Spy 和 Stub
- **Fake Timers**：模拟时间

## 3. 安装与使用

### 3.1 安装

```bash
npm install -D sinon
npm install -D @types/sinon
```

### 3.2 基本使用

```ts
import sinon from 'sinon';
import { describe, it, expect } from 'vitest';

describe('Sinon', () => {
  it('should create a spy', (): void => {
    const spy = sinon.spy();
    spy('arg1', 'arg2');
    
    expect(spy.called).toBe(true);
    expect(spy.calledWith('arg1', 'arg2')).toBe(true);
    expect(spy.callCount).toBe(1);
  });
});
```

## 4. Spy

### 4.1 函数 Spy

```ts
import sinon from 'sinon';

function originalFunction(a: number, b: number): number {
  return a + b;
}

describe('Spy', () => {
  it('should spy on function', (): void => {
    const spy = sinon.spy(originalFunction);
    const result = spy(1, 2);
    
    expect(result).toBe(3);
    expect(spy.called).toBe(true);
    expect(spy.calledWith(1, 2)).toBe(true);
  });
  
  it('should spy on method', (): void => {
    const obj = {
      method: function (value: string): string {
        return value.toUpperCase();
      }
    };
    
    const spy = sinon.spy(obj, 'method');
    const result = obj.method('test');
    
    expect(result).toBe('TEST');
    expect(spy.called).toBe(true);
  });
});
```

## 5. Stub

### 5.1 函数 Stub

```ts
import sinon from 'sinon';

describe('Stub', () => {
  it('should stub function', (): void => {
    const stub = sinon.stub().returns(42);
    expect(stub()).toBe(42);
  });
  
  it('should stub with different returns', (): void => {
    const stub = sinon.stub()
      .onFirstCall().returns(1)
      .onSecondCall().returns(2)
      .returns(3);
    
    expect(stub()).toBe(1);
    expect(stub()).toBe(2);
    expect(stub()).toBe(3);
  });
  
  it('should stub async function', async (): Promise<void> => {
    const stub = sinon.stub().resolves({ id: 1, name: 'John' });
    const result = await stub();
    
    expect(result).toEqual({ id: 1, name: 'John' });
  });
  
  it('should stub with implementation', (): void => {
    const stub = sinon.stub().callsFake((a: number, b: number): number => {
      return a * b;
    });
    
    expect(stub(3, 4)).toBe(12);
  });
});
```

### 5.2 对象方法 Stub

```ts
import sinon from 'sinon';

class UserService {
  async getUser(id: number): Promise<any> {
    // 真实实现
    return { id, name: 'User' };
  }
}

describe('Object Stub', () => {
  it('should stub object method', async (): Promise<void> => {
    const service = new UserService();
    const stub = sinon.stub(service, 'getUser').resolves({ id: 1, name: 'John' });
    
    const user = await service.getUser(1);
    expect(user).toEqual({ id: 1, name: 'John' });
    expect(stub.calledWith(1)).toBe(true);
  });
});
```

## 6. Mock

### 6.1 Mock 对象

```ts
import sinon from 'sinon';

describe('Mock', () => {
  it('should create mock', (): void => {
    const obj = {
      method1: (): void => {},
      method2: (): void => {}
    };
    
    const mock = sinon.mock(obj);
    mock.expects('method1').once().withArgs('arg1');
    mock.expects('method2').never();
    
    obj.method1('arg1');
    
    mock.verify();
  });
});
```

## 7. Fake Timers

### 7.1 时间 Mock

```ts
import sinon from 'sinon';

describe('Fake Timers', () => {
  let clock: sinon.SinonFakeTimers;
  
  beforeEach((): void => {
    clock = sinon.useFakeTimers();
  });
  
  afterEach((): void => {
    clock.restore();
  });
  
  it('should advance time', (): void => {
    const callback = sinon.spy();
    setTimeout(callback, 1000);
    
    clock.tick(1000);
    expect(callback.called).toBe(true);
  });
  
  it('should mock date', (): void => {
    const mockDate = new Date('2024-01-01');
    clock.setSystemTime(mockDate);
    
    const now = new Date();
    expect(now.getTime()).toBe(mockDate.getTime());
  });
});
```

## 8. 最佳实践

### 8.1 使用建议

- 使用 Spy 监视调用
- 使用 Stub 替换实现
- 使用 Mock 验证交互
- 及时清理 Mock

### 8.2 清理机制

```ts
import sinon from 'sinon';

describe('Cleanup', () => {
  afterEach((): void => {
    sinon.restore(); // 恢复所有 Mock
  });
});
```

## 9. 注意事项

- **及时清理**：使用后及时清理 Mock
- **适度使用**：避免过度使用 Mock
- **真实实现**：优先使用真实实现
- **测试维护**：及时维护 Mock 代码

## 10. 常见问题

### 10.1 如何选择 Spy、Stub、Mock？

Spy 用于监视，Stub 用于替换，Mock 用于验证。

### 10.2 如何处理异步函数？

使用 `resolves` 或 `rejects` 方法。

### 10.3 如何清理 Mock？

使用 `sinon.restore()` 或 `stub.restore()`。

## 11. 实践任务

1. **Spy 使用**：使用 Spy 监视函数
2. **Stub 使用**：使用 Stub 替换实现
3. **Mock 使用**：使用 Mock 验证交互
4. **时间 Mock**：使用 Fake Timers
5. **最佳实践**：遵循 Sinon.js 最佳实践

---

**下一节**：[7.5.4 MSW（Mock Service Worker）](section-04-msw.md)
