# 2.16.4 ES2023 新特�?

## 概述

ES2023（ES14）是 ECMAScript 2023 标准，于 2023 �?6 月发布。ES2023 主要引入了数组的查找和复制方法，提供了更强大的数组操作能力，特别是不可变数组操作方法�?

## 核心特�?

ES2023 主要包含以下新特性：

1. **数组查找方法**：`Array.prototype.findLast()` �?`Array.prototype.findLastIndex()`
2. **数组复制方法**：`Array.prototype.toReversed()`、`Array.prototype.toSorted()`、`Array.prototype.toSpliced()`、`Array.prototype.with()`
3. **正则表达�?/v 标志**：可编排正则模式（部分引擎支持）

---

## Array.prototype.findLast()

### 概述

`findLast()` 方法返回数组中满足测试函数的最后一个元素的值。如果没有找到，返回 `undefined`�?

### 语法格式

```js
array.findLast(callbackFn, thisArg)
```

### 参数说明

| 参数�?      | 类型     | 说明                           | 是否必需 | 默认�?|
|:-------------|:---------|:-------------------------------|:---------|:-------|
| `callbackFn` | function | 测试函数                       | �?      | -      |
| `thisArg`    | any      | 执行回调时使用的 `this` �?    | �?      | -      |

**回调函数参数**�?

| 参数�?     | 类型   | 说明           |
|:------------|:-------|:---------------|
| `element`   | any    | 当前元素       |
| `index`     | number | 当前索引       |
| `array`     | array  | 原数�?        |

### 返回�?

返回满足条件的最后一个元素，如果没有找到则返�?`undefined`�?

### 基本用法

**示例 1**：查找最后一个偶�?

```js
const numbers = [1, 2, 3, 4, 5, 6];
const lastEven = numbers.findLast(n => n % 2 === 0);
console.log(lastEven); // 6
```

**输出说明**：从数组末尾开始查找，找到最后一个满足条件的元素 `6`�?

**示例 2**：查找最后一个满足条件的对象

```js
const users = [
  { id: 1, active: true },
  { id: 2, active: false },
  { id: 3, active: true },
  { id: 4, active: false }
];

const lastActive = users.findLast(user => user.active);
console.log(lastActive); // { id: 3, active: true }
```

**输出说明**：返回最后一�?`active` �?`true` 的用户对象�?

### �?find() 的对�?

| 方法          | 查找方向 | 返回元素           |
|:--------------|:---------|:-------------------|
| `find()`      | 从前往�?| 第一个满足条件的   |
| `findLast()`  | 从后往�?| 最后一个满足条件的 |

**示例对比**�?

```js
const arr = [1, 2, 3, 4, 5, 4, 3, 2, 1];

console.log(arr.find(n => n > 3));      // 4（第一个）
console.log(arr.findLast(n => n > 3));   // 4（最后一个，但实际是倒数第二�?4�?
```

### 注意事项

1. **稀疏数�?*：对于稀疏数组，未初始化的元素不会被访问
2. **修改原数�?*：如果在回调中修改原数组，行为可能不确定
3. **性能**：需要遍历整个数组（最坏情况）

---

## Array.prototype.findLastIndex()

### 概述

`findLastIndex()` 方法返回数组中满足测试函数的最后一个元素的索引。如果没有找到，返回 `-1`�?

### 语法格式

```js
array.findLastIndex(callbackFn, thisArg)
```

### 参数说明

�?`findLast()` 相同�?

### 返回�?

返回满足条件的最后一个元素的索引，如果没有找到则返回 `-1`�?

### 基本用法

**示例**�?

```js
const numbers = [1, 2, 3, 4, 5, 4, 3, 2, 1];
const lastIndex = numbers.findLastIndex(n => n > 3);
console.log(lastIndex); // 5（最后一个大�?3 的元素的索引�?
```

**输出说明**：返回索�?`5`，对应值为 `4`（最后一个大�?3 的元素）�?

### �?findIndex() 的对�?

| 方法              | 查找方向 | 返回索引           |
|:------------------|:---------|:-------------------|
| `findIndex()`     | 从前往�?| 第一个满足条件的索引 |
| `findLastIndex()` | 从后往�?| 最后一个满足条件的索引 |

---

## 数组复制方法（不可变操作�?

### 概述

ES2023 引入了四个新的数组方法，它们返回新数组而不修改原数组，实现了不可变数组操作�?

- `toReversed()`：返回反转后的新数组
- `toSorted()`：返回排序后的新数组
- `toSpliced()`：返回删�?插入元素后的新数�?
- `with()`：返回替换指定索引元素后的新数组

### Array.prototype.toReversed()

**语法格式**�?
```js
array.toReversed()
```

**返回�?*：返回一个新数组，元素顺序与原数组相反�?

**示例**�?

```js
const arr = [1, 2, 3, 4, 5];
const reversed = arr.toReversed();
console.log(reversed); // [5, 4, 3, 2, 1]
console.log(arr);      // [1, 2, 3, 4, 5]（原数组未改变）
```

**输出说明**�?
- `reversed`：反转后的新数组
- `arr`：原数组保持不变

**�?reverse() 的对�?*�?

| 方法           | 修改原数�?| 返回�?          |
|:---------------|:----------|:----------------|
| `reverse()`    | �?�?    | 原数组（已修改） |
| `toReversed()` | �?�?    | 新数�?         |

### Array.prototype.toSorted()

**语法格式**�?
```js
array.toSorted(compareFn)
```

**参数说明**�?

| 参数�?      | 类型     | 说明           | 是否必需 | 默认�?|
|:-------------|:---------|:---------------|:---------|:-------|
| `compareFn`  | function | 比较函数       | �?      | -      |

**返回�?*：返回一个新数组，元素已排序�?

**示例**�?

```js
const arr = [3, 1, 4, 1, 5];
const sorted = arr.toSorted();
console.log(sorted); // [1, 1, 3, 4, 5]
console.log(arr);    // [3, 1, 4, 1, 5]（原数组未改变）

// 使用比较函数
const sortedDesc = arr.toSorted((a, b) => b - a);
console.log(sortedDesc); // [5, 4, 3, 1, 1]
```

**输出说明**�?
- `toSorted()` 返回排序后的新数�?
- 原数组保持不�?

**�?sort() 的对�?*�?

| 方法          | 修改原数�?| 返回�?          |
|:--------------|:----------|:----------------|
| `sort()`      | �?�?    | 原数组（已修改） |
| `toSorted()`  | �?�?    | 新数�?         |

### Array.prototype.toSpliced()

**语法格式**�?
```js
array.toSpliced(start, deleteCount, ...items)
```

**参数说明**�?

| 参数�?        | 类型   | 说明                           | 是否必需 | 默认�?|
|:---------------|:-------|:-------------------------------|:---------|:-------|
| `start`        | number | 开始位�?                      | �?      | -      |
| `deleteCount`  | number | 要删除的元素数量               | �?      | 0      |
| `...items`     | any    | 要插入的元素（可选，多个�?    | �?      | -      |

**返回�?*：返回一个新数组，包含删除和插入操作后的结果�?

**示例**�?

```js
const arr = [1, 2, 3, 4, 5];

// 删除元素
const deleted = arr.toSpliced(1, 2);
console.log(deleted); // [1, 4, 5]
console.log(arr);     // [1, 2, 3, 4, 5]（原数组未改变）

// 插入元素
const inserted = arr.toSpliced(2, 0, 'a', 'b');
console.log(inserted); // [1, 2, 'a', 'b', 3, 4, 5]

// 替换元素
const replaced = arr.toSpliced(1, 2, 'x', 'y');
console.log(replaced); // [1, 'x', 'y', 4, 5]
```

**输出说明**�?
- `toSpliced()` 可以删除、插入或替换元素
- 返回新数组，原数组不�?

**�?splice() 的对�?*�?

| 方法           | 修改原数�?| 返回�?          |
|:---------------|:----------|:----------------|
| `splice()`     | �?�?    | 被删除元素的数组 |
| `toSpliced()`  | �?�?    | 新数�?         |

### Array.prototype.with()

**语法格式**�?
```js
array.with(index, value)
```

**参数说明**�?

| 参数�?   | 类型   | 说明           | 是否必需 | 默认�?|
|:----------|:-------|:---------------|:---------|:-------|
| `index`   | number | 要替换的索引   | �?      | -      |
| `value`   | any    | 新�?          | �?      | -      |

**返回�?*：返回一个新数组，指定索引的元素已被替换�?

**示例**�?

```js
const arr = [1, 2, 3, 4, 5];
const updated = arr.with(2, 99);
console.log(updated); // [1, 2, 99, 4, 5]
console.log(arr);     // [1, 2, 3, 4, 5]（原数组未改变）

// 使用负索�?
const updatedLast = arr.with(-1, 99);
console.log(updatedLast); // [1, 2, 3, 4, 99]
```

**输出说明**�?
- `with()` 返回替换指定元素后的新数�?
- 支持负索引（从末尾开始）
- 原数组保持不�?

### 不可变操作的优势

1. **函数式编�?*：支持不可变数据操作，符合函数式编程理念
2. **状态管�?*：在 React 等框架中，不可变操作更安�?
3. **调试友好**：不会意外修改原数组，便于调�?

### 注意事项

1. **性能考虑**：创建新数组需要额外的内存和复制操�?
2. **大数�?*：对于大数组，可能影响性能
3. **兼容�?*：需�?Node.js 20.0.0+ 或现代浏览器支持

### 常见错误

**错误 1**：误以为会修改原数组

```js
const arr = [1, 2, 3];
const reversed = arr.toReversed();
// �?错误：以�?arr 被修改了
console.log(arr); // [1, 2, 3]（未改变�?

// �?正确：需要重新赋�?
let arr = [1, 2, 3];
arr = arr.toReversed();
console.log(arr); // [3, 2, 1]
```

---

## 兼容性说�?

### 浏览器支�?

| 特�?             | Chrome | Firefox | Safari | Edge  |
|:------------------|:-------|:--------|:-------|:------|
| `findLast()`      | 97+    | 104+    | 15.4+  | 97+   |
| `findLastIndex()` | 97+    | 104+    | 15.4+  | 97+   |
| `toReversed()`    | 110+   | 115+    | 16+    | 110+  |
| `toSorted()`      | 110+   | 115+    | 16+    | 110+  |
| `toSpliced()`     | 110+   | 115+    | 16+    | 110+  |
| `with()`          | 110+   | 115+    | 16+    | 110+  |

### Node.js 支持

- **`findLast()` / `findLastIndex()`**：Node.js 18.0.0+
- **数组复制方法**：Node.js 20.0.0+

### 转译�?Polyfill

如果需要在旧环境中使用 ES2023 特性：

1. **Babel**：使用相应的插件转译
2. **TypeScript**：在 `tsconfig.json` 中设�?`target: "ES2023"`
3. **Polyfill**：可以使�?`core-js` �?polyfill

---

## 最佳实�?

1. **查找方法**�?
   - 需要从后往前查找时使用 `findLast()` �?`findLastIndex()`
   - 提高代码可读�?

2. **不可变操�?*�?
   - �?React 等框架中优先使用不可变方�?
   - 需要修改原数组时使用传统方法（`reverse()`、`sort()` 等）

3. **性能考虑**�?
   - 大数组频繁操作时，考虑性能影响
   - 根据场景选择可变或不可变方法

---

## 练习

1. **查找方法**�?
   - 使用 `findLast()` 查找数组中最后一个满足条件的元素
   - 使用 `findLastIndex()` 查找最后一个满足条件的元素的索�?

2. **不可变操�?*�?
   - 使用 `toReversed()` 反转数组而不修改原数�?
   - 使用 `toSorted()` 排序数组而不修改原数�?
   - 使用 `with()` 更新数组中的特定元素

3. **综合练习**�?
   - 实现一个不可变的数组操作工具函数库
   - �?React 组件中使用不可变数组方法更新状�?

---

## 总结

ES2023 主要增强了数组操作能力：

- **查找方法**：提供从后往前查找的能力
- **不可变操�?*：提供不修改原数组的数组操作方法
- **函数式编�?*：更好地支持函数式编程范�?

这些特性在现代 JavaScript 开发中，特别是�?React 等框架中非常有用�?

继续学习下一节：ES2024 新特性�?

---

**最后更�?*�?025-12-16
