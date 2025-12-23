# 函数文档格式标准

## 概述

本文档定义了所有函数、方法、API 的文档格式标准。**所有函数文档必须严格遵守此标准。**

## 必需格式

每个函数文档必须包含以下三个部分，按顺序排列：

### 1. 语法（必需）

**格式**：
```markdown
**语法**：`functionName(param1: type, param2?: type): returnType`
```

**要求**：
- 使用反引号包裹完整函数签名
- 包含所有参数及其类型
- 包含返回值类型
- 可选参数使用 `?` 标注

### 2. 参数（必需）

**格式**：
```markdown
**参数**：
- `param1`：参数说明
- `param2`：可选，参数说明（如果是可选参数，必须标注"可选"）
```

**要求**：
- 每个参数必须单独列出
- 参数名使用反引号包裹
- 必须说明参数的作用和含义
- 可选参数必须标注"可选"或"默认值"
- 复杂参数需要详细说明

### 3. 返回值（必需）

**格式**：
```markdown
**返回值**：返回值的详细说明。
```

**要求**：
- 必须说明返回值的类型
- 必须说明返回值的含义
- 特殊情况必须说明（如返回 `undefined` 表示失败）
- 如果可能返回多种类型，必须说明所有情况

## 完整示例

```markdown
### Array.map() - 映射数组

**语法**：`Array.map<T, U>(callbackfn: (value: T, index: number, array: T[]) => U, thisArg?: any): U[]`

**参数**：
- `callbackfn`：对每个元素执行的函数，接收三个参数：当前元素值、索引、原数组
- `thisArg`：可选，执行回调函数时使用的 `this` 值

**返回值**：返回一个新数组，包含对原数组每个元素执行回调函数的结果。

```ts
const numbers = [1, 2, 3];
const doubled = numbers.map((n: number) => n * 2);
console.log(doubled);  // [2, 4, 6]
```
```

## 多参数函数示例

```markdown
### Array.slice() - 提取数组片段

**语法**：`Array.slice(start?: number, end?: number): T[]`

**参数**：
- `start`：可选，开始提取的位置（包含），默认为 0
- `end`：可选，结束提取的位置（不包含），默认为数组长度

**返回值**：返回一个新数组，包含从 `start` 到 `end`（不包含）的元素。

```ts
const arr = [1, 2, 3, 4, 5];
console.log(arr.slice(1, 3));  // [2, 3]
console.log(arr.slice(2));     // [3, 4, 5]
```
```

## 可能返回多种类型的函数示例

```markdown
### Array.find() - 查找元素

**语法**：`Array.find<T>(predicate: (value: T, index: number, array: T[]) => boolean, thisArg?: any): T | undefined`

**参数**：
- `predicate`：测试函数，返回 `true` 表示找到匹配元素
- `thisArg`：可选，执行回调函数时使用的 `this` 值

**返回值**：找到返回匹配的元素，未找到返回 `undefined`。

```ts
const numbers = [1, 2, 3, 4, 5];
const found = numbers.find((n: number) => n > 3);
if (found !== undefined) {
  console.log(found);  // 4
}
```
```

## 检查清单

在编写或审查函数文档时，必须确认：

- [ ] **语法**：包含完整函数签名，所有参数和返回值类型
- [ ] **参数**：每个参数都有说明，可选参数标注"可选"
- [ ] **返回值**：详细说明返回值类型和含义
- [ ] **格式一致**：所有函数使用相同的格式
- [ ] **内容完整**：没有遗漏任何参数
- [ ] **类型注解**：所有示例代码包含完整的 TypeScript 类型注解

## 常见错误

### ❌ 错误示例 1：缺少参数说明

```markdown
### Array.map() - 映射数组

**语法**：`Array.map<T, U>(callbackfn: (value: T, index: number, array: T[]) => U, thisArg?: any): U[]`

```ts
// 缺少参数和返回值说明
```
```

### ❌ 错误示例 2：参数说明不完整

```markdown
**参数**：
- `callbackfn`：对每个元素执行的函数
// 缺少其他参数的说明
```

### ❌ 错误示例 3：缺少返回值说明

```markdown
**语法**：`Array.map<T, U>(callbackfn: (value: T, index: number, array: T[]) => U, thisArg?: any): U[]`

**参数**：
- `callbackfn`：对每个元素执行的函数

// 缺少返回值说明
```

### ❌ 错误示例 4：缺少类型注解

```ts
// ❌ 错误
const doubled = numbers.map(n => n * 2);

// ✅ 正确
const doubled = numbers.map((n: number) => n * 2);
```

## 适用范围

此标准适用于：

- JavaScript/TypeScript 内置方法
- Node.js API 方法
- 自定义函数
- 类方法
- 任何需要文档化的函数/方法

---

**最后更新**：2025-12-22

**重要提示**：所有函数文档必须包含语法、参数、返回值三个部分，缺一不可。
