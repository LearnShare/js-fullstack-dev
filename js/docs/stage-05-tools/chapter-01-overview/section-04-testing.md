# 5.1.4 测试框架

## 概述

测试是保证代码质量的重要手段。本节介绍常用的 JavaScript 测试框架，包括 Jest、Vitest 等。

## Jest

### 简介

Jest 是 Facebook 开发的 JavaScript 测试框架，功能完善，开箱即用，是 React 项目的默认测试框架。

### 安装

```bash
npm install --save-dev jest
```

### 基本使用

```js
// sum.js
function sum(a, b) {
    return a + b;
}
module.exports = sum;

// sum.test.js
const sum = require('./sum');

test('adds 1 + 2 to equal 3', () => {
    expect(sum(1, 2)).toBe(3);
});
```

### 运行测试

```bash
npm test
```

### 常用断言

```js
// 相等性
expect(value).toBe(3);
expect(value).toEqual({ a: 1 });

// 真值
expect(value).toBeTruthy();
expect(value).toBeFalsy();

// 数字
expect(value).toBeGreaterThan(3);
expect(value).toBeLessThan(5);

// 字符串
expect(str).toMatch(/pattern/);
expect(str).toContain('substring');

// 数组
expect(array).toContain(item);
expect(array).toHaveLength(3);

// 对象
expect(obj).toHaveProperty('key');
expect(obj).toMatchObject({ a: 1 });
```

### 异步测试

```js
// Promise
test('async test', () => {
    return fetchData().then(data => {
        expect(data).toBe('data');
    });
});

// async/await
test('async test', async () => {
    const data = await fetchData();
    expect(data).toBe('data');
});
```

### Mock

```js
// Mock 函数
const mockFn = jest.fn();
mockFn('arg');
expect(mockFn).toHaveBeenCalledWith('arg');

// Mock 模块
jest.mock('./module');
```

## Vitest

### 简介

Vitest 是基于 Vite 的测试框架，快速、兼容 Jest API，适合现代 JavaScript 项目。

### 安装

```bash
npm install --save-dev vitest
```

### 基本使用

```js
// sum.test.js
import { describe, it, expect } from 'vitest';
import { sum } from './sum';

describe('sum', () => {
    it('adds 1 + 2 to equal 3', () => {
        expect(sum(1, 2)).toBe(3);
    });
});
```

### 配置

```js
// vitest.config.js
import { defineConfig } from 'vitest/config';

export default defineConfig({
    test: {
        globals: true,
        environment: 'node',
    },
});
```

### 优势

1. **速度快**：基于 Vite，速度快
2. **兼容 Jest**：API 兼容 Jest
3. **TypeScript 支持**：原生支持 TypeScript
4. **ESM 支持**：原生支持 ESM

## 其他测试框架

### Mocha

```js
const assert = require('assert');

describe('Array', function() {
    describe('#indexOf()', function() {
        it('should return -1 when the value is not present', function() {
            assert.equal([1, 2, 3].indexOf(4), -1);
        });
    });
});
```

### Jasmine

```js
describe('sum', function() {
    it('adds 1 + 2 to equal 3', function() {
        expect(sum(1, 2)).toBe(3);
    });
});
```

## 测试类型

### 单元测试

```js
// 测试单个函数
test('sum function', () => {
    expect(sum(1, 2)).toBe(3);
});
```

### 集成测试

```js
// 测试多个模块协作
test('user registration flow', async () => {
    const user = await registerUser({ name: 'John' });
    expect(user).toHaveProperty('id');
});
```

### 端到端测试

使用 Playwright 或 Cypress 进行端到端测试。

## 框架对比

| 特性          | Jest        | Vitest     | Mocha      |
|:--------------|:------------|:-----------|:-----------|
| 速度          | 中等        | 快         | 中等       |
| 配置          | 开箱即用    | 需要配置   | 需要配置   |
| TypeScript    | 需要配置    | 原生支持   | 需要配置   |
| ESM 支持      | 需要配置    | 原生支持   | 需要配置   |
| 生态          | 完善        | 增长中     | 完善       |

## 选择建议

1. **React 项目**：推荐 Jest
2. **Vite 项目**：推荐 Vitest
3. **需要快速测试**：推荐 Vitest
4. **传统项目**：可以使用 Jest 或 Mocha

## 注意事项

1. **测试覆盖率**：关注测试覆盖率，但不盲目追求
2. **测试质量**：测试质量比数量更重要
3. **维护测试**：及时维护和更新测试
4. **CI/CD 集成**：集成到 CI/CD 流程

## 最佳实践

1. **编写测试**：为关键功能编写测试
2. **测试命名**：使用清晰的测试名称
3. **测试隔离**：每个测试应该独立
4. **Mock 使用**：合理使用 Mock，避免过度依赖

## 练习

1. **Jest 基础**：使用 Jest 编写函数测试，包含多种断言。

2. **异步测试**：使用 Jest 编写异步函数测试。

3. **Mock 使用**：使用 Jest Mock 测试依赖外部模块的函数。

4. **Vitest 实践**：使用 Vitest 编写测试，体验快速测试。

5. **测试覆盖率**：配置测试覆盖率报告，分析测试覆盖率。

完成以上练习后，继续学习下一节，了解代码质量工具。

## 总结

Jest 和 Vitest 是常用的 JavaScript 测试框架。Jest 功能完善、生态成熟；Vitest 速度快、原生支持 TypeScript 和 ESM。根据项目需求选择合适的测试框架，编写高质量的测试用例。

## 相关资源

- [Jest 官网](https://jestjs.io/)
- [Vitest 官网](https://vitest.dev/)
- [Mocha 官网](https://mochajs.org/)
