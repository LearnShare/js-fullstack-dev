# 2.7.2 数组基础与操作

## 概述

数组是 JavaScript 中的有序集合，用于存储多个值。数组可以包含任何类型的元素，包括数字、字符串、对象、甚至其他数组。数组是 JavaScript 中最常用的数据结构之一。

数组的主要特点：

- **有序性**：数组中的元素按照插入顺序排列
- **索引访问**：可以通过数字索引（从 0 开始）访问元素
- **可变长度**：可以动态添加或删除元素
- **类型灵活**：可以包含不同类型的元素

## 数组创建

### 数组字面量

**语法**：`[element1, element2, ..., elementN]`

**说明**：使用方括号创建数组，这是最常用的方式。

```js
// 创建包含数字的数组
const numbers = [1, 2, 3, 4, 5];

// 创建空数组
const empty = [];

// 创建包含不同类型元素的数组
const mixed = [1, "hello", true, null, undefined];

// 创建嵌套数组
const nested = [[1, 2], [3, 4], [5, 6]];
```

**输出说明**：数组字面量是最简洁的创建方式，推荐使用。

### Array 构造函数

**语法**：`new Array(element1, element2, ..., elementN)` 或 `new Array(arrayLength)`

**参数说明**：

| 参数名         | 类型   | 说明                           | 是否必需 | 默认值 |
|:---------------|:-------|:-------------------------------|:---------|:-------|
| `...elements`  | any    | 数组元素                       | 否       | -      |
| `arrayLength`  | number | 数组长度（仅一个数字参数时）   | 否       | -      |

**返回值**：新的数组对象

**示例 1**：使用元素创建数组

```js
const arr = new Array(1, 2, 3);
console.log(arr); // [1, 2, 3]
console.log(arr.length); // 3
```

**示例 2**：使用长度创建数组

```js
// 注意：单个数字参数表示长度，不是元素
const empty = new Array(5);
console.log(empty); // [undefined, undefined, undefined, undefined, undefined]
console.log(empty.length); // 5
```

**注意事项**：

- 当只有一个数字参数时，会创建指定长度的空数组（元素为 `undefined`）
- 不推荐使用 `new Array()`，优先使用数组字面量

### Array.of()

**语法**：`Array.of(element1, element2, ..., elementN)`

**参数说明**：

| 参数名        | 类型 | 说明     | 是否必需 | 默认值 |
|:--------------|:-----|:---------|:---------|:-------|
| `...elements` | any  | 数组元素 | 否       | -      |

**返回值**：新的数组对象

**说明**：`Array.of()` 解决了 `new Array()` 单个数字参数的歧义问题。

```js
// Array.of() 总是将参数作为元素
const arr = Array.of(1, 2, 3);
console.log(arr); // [1, 2, 3]

// 单个数字参数也被视为元素
const single = Array.of(5);
console.log(single); // [5]（不是长度为 5 的空数组）

// 对比 new Array()
const arr1 = new Array(5);   // [undefined, undefined, undefined, undefined, undefined]
const arr2 = Array.of(5);    // [5]
```

**输出说明**：`Array.of()` 避免了 `new Array()` 的歧义，推荐使用。

### Array.from()

**语法**：`Array.from(arrayLike[, mapFn[, thisArg]])`

**参数说明**：

| 参数名      | 类型        | 说明                           | 是否必需 | 默认值 |
|:------------|:------------|:-------------------------------|:---------|:-------|
| `arrayLike` | iterable    | 类数组对象或可迭代对象         | 是       | -      |
| `mapFn`     | function    | 映射函数（类似 map）           | 否       | -      |
| `thisArg`   | any         | 映射函数的 this 值             | 否       | -      |

**返回值**：新的数组对象

**示例 1**：从字符串创建数组

```js
const arr = Array.from("hello");
console.log(arr); // ["h", "e", "l", "l", "o"]
```

**示例 2**：从类数组对象创建

```js
// 从 arguments 对象创建
function example() {
  return Array.from(arguments);
}
console.log(example(1, 2, 3)); // [1, 2, 3]
```

**示例 3**：使用映射函数

```js
// 创建数字序列
const numbers = Array.from({ length: 5 }, (_, i) => i + 1);
console.log(numbers); // [1, 2, 3, 4, 5]

// 创建指定范围的数组
const range = Array.from({ length: 10 }, (_, i) => i * 2);
console.log(range); // [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

**输出说明**：`Array.from()` 可以将类数组对象或可迭代对象转换为真正的数组。

## 索引访问

### 基本访问

**语法**：`array[index]`

**参数说明**：

| 参数名   | 类型   | 说明           | 是否必需 | 默认值 |
|:---------|:-------|:---------------|:---------|:-------|
| `index`  | number | 元素索引（从 0 开始） | 是 | -      |

**返回值**：对应索引的元素，如果索引超出范围返回 `undefined`

```js
const arr = [1, 2, 3, 4, 5];

// 访问第一个元素
console.log(arr[0]); // 1

// 访问第三个元素
console.log(arr[2]); // 3

// 访问最后一个元素
console.log(arr[arr.length - 1]); // 5

// 访问不存在的索引
console.log(arr[10]); // undefined
```

**输出说明**：数组索引从 0 开始，访问不存在的索引返回 `undefined`。

### 修改元素

**语法**：`array[index] = value`

**参数说明**：

| 参数名   | 类型   | 说明           | 是否必需 | 默认值 |
|:---------|:-------|:---------------|:---------|:-------|
| `index`  | number | 元素索引       | 是       | -      |
| `value`  | any    | 新值           | 是       | -      |

```js
const arr = [1, 2, 3];

// 修改第一个元素
arr[0] = 10;
console.log(arr); // [10, 2, 3]

// 添加新元素（如果索引超出当前长度）
arr[5] = 6;
console.log(arr); // [10, 2, 3, undefined, undefined, 6]
console.log(arr.length); // 6
```

**输出说明**：可以直接通过索引修改元素，如果索引超出长度会扩展数组。

## 长度属性

### length

**语法**：`array.length`

**说明**：返回或设置数组的长度

**返回值**：数字，表示数组的长度

**示例 1**：获取数组长度

```js
const arr = [1, 2, 3, 4, 5];
console.log(arr.length); // 5
```

**示例 2**：修改 length（截断或扩展）

```js
const arr = [1, 2, 3];

// 扩展数组（添加 undefined 元素）
arr.length = 5;
console.log(arr); // [1, 2, 3, undefined, undefined]

// 截断数组（删除元素）
arr.length = 2;
console.log(arr); // [1, 2]
```

**注意事项**：

- 修改 `length` 会直接改变数组，截断时会删除超出长度的元素
- 扩展时会在末尾添加 `undefined` 元素
- `length` 总是大于等于数组中最大索引 + 1

## 数组方法

### push()

**语法**：`array.push(element1, element2, ..., elementN)`

**参数说明**：

| 参数名        | 类型 | 说明           | 是否必需 | 默认值 |
|:--------------|:-----|:---------------|:---------|:-------|
| `...elements` | any  | 要添加的元素   | 是       | -      |

**返回值**：数字，表示数组的新长度

**说明**：在数组末尾添加一个或多个元素

```js
const arr = [1, 2, 3];

// 添加单个元素
const newLength = arr.push(4);
console.log(arr); // [1, 2, 3, 4]
console.log(newLength); // 4

// 添加多个元素
arr.push(5, 6, 7);
console.log(arr); // [1, 2, 3, 4, 5, 6, 7]
```

**输出说明**：`push()` 会修改原数组，返回新长度。

### pop()

**语法**：`array.pop()`

**参数说明**：无参数

**返回值**：被移除的元素，如果数组为空返回 `undefined`

**说明**：移除并返回数组的最后一个元素

```js
const arr = [1, 2, 3, 4, 5];

// 移除最后一个元素
const last = arr.pop();
console.log(last); // 5
console.log(arr);  // [1, 2, 3, 4]

// 空数组
const empty = [];
const result = empty.pop();
console.log(result); // undefined
```

**输出说明**：`pop()` 会修改原数组，返回被移除的元素。

### unshift()

**语法**：`array.unshift(element1, element2, ..., elementN)`

**参数说明**：

| 参数名        | 类型 | 说明           | 是否必需 | 默认值 |
|:--------------|:-----|:---------------|:---------|:-------|
| `...elements` | any  | 要添加的元素   | 是       | -      |

**返回值**：数字，表示数组的新长度

**说明**：在数组开头添加一个或多个元素

```js
const arr = [1, 2, 3];

// 添加单个元素
const newLength = arr.unshift(0);
console.log(arr); // [0, 1, 2, 3]
console.log(newLength); // 4

// 添加多个元素
arr.unshift(-2, -1);
console.log(arr); // [-2, -1, 0, 1, 2, 3]
```

**输出说明**：`unshift()` 会修改原数组，返回新长度。注意：在开头添加元素需要移动所有现有元素，性能较差。

### shift()

**语法**：`array.shift()`

**参数说明**：无参数

**返回值**：被移除的元素，如果数组为空返回 `undefined`

**说明**：移除并返回数组的第一个元素

```js
const arr = [1, 2, 3, 4, 5];

// 移除第一个元素
const first = arr.shift();
console.log(first); // 1
console.log(arr);   // [2, 3, 4, 5]

// 空数组
const empty = [];
const result = empty.shift();
console.log(result); // undefined
```

**输出说明**：`shift()` 会修改原数组，返回被移除的元素。注意：移除第一个元素需要移动所有剩余元素，性能较差。

### slice()

**语法**：`array.slice([start[, end]])`

**参数说明**：

| 参数名   | 类型   | 说明                                 | 是否必需 | 默认值     |
|:---------|:-------|:-------------------------------------|:---------|:-----------|
| `start`  | number | 起始索引（包含）                     | 否       | 0          |
| `end`    | number | 结束索引（不包含）                    | 否       | `length`   |

**返回值**：新的数组对象，包含从 `start` 到 `end`（不包含）的元素

**说明**：截取数组的一部分，不修改原数组

```js
const arr = [1, 2, 3, 4, 5];

// 从索引 1 到 3（不包含 3）
const part = arr.slice(1, 3);
console.log(part); // [2, 3]
console.log(arr);  // [1, 2, 3, 4, 5]（未改变）

// 从索引 2 到末尾
const rest = arr.slice(2);
console.log(rest); // [3, 4, 5]

// 使用负数索引（从末尾开始计算）
const lastTwo = arr.slice(-2);
console.log(lastTwo); // [4, 5]

// 复制整个数组
const copy = arr.slice();
console.log(copy); // [1, 2, 3, 4, 5]
```

**输出说明**：`slice()` 不修改原数组，返回新数组。负数索引从末尾开始计算。

### splice()

**语法**：`array.splice(start[, deleteCount[, item1[, item2[, ...]]]])`

**参数说明**：

| 参数名        | 类型   | 说明                           | 是否必需 | 默认值           |
|:--------------|:-------|:-------------------------------|:---------|:-----------------|
| `start`       | number | 起始索引                       | 是       | -                |
| `deleteCount` | number | 要删除的元素数量               | 否       | `length - start` |
| `...items`    | any    | 要插入的元素                   | 否       | -                |

**返回值**：包含被删除元素的数组

**说明**：修改数组，删除、替换或插入元素

```js
const arr = [1, 2, 3, 4, 5];

// 删除元素（从索引 1 开始，删除 2 个）
const removed = arr.splice(1, 2);
console.log(removed); // [2, 3]
console.log(arr);     // [1, 4, 5]

// 插入元素（从索引 1 开始，删除 0 个，插入 "a", "b"）
arr.splice(1, 0, "a", "b");
console.log(arr); // [1, "a", "b", 4, 5]

// 替换元素（从索引 1 开始，删除 2 个，插入 "x", "y"）
arr.splice(1, 2, "x", "y");
console.log(arr); // [1, "x", "y", 4, 5]
```

**输出说明**：`splice()` 会修改原数组，返回被删除的元素数组。

### indexOf()

**语法**：`array.indexOf(searchElement[, fromIndex])`

**参数说明**：

| 参数名          | 类型   | 说明                           | 是否必需 | 默认值 |
|:----------------|:-------|:-------------------------------|:---------|:-------|
| `searchElement` | any    | 要查找的元素                   | 是       | -      |
| `fromIndex`     | number | 开始查找的索引                 | 否       | 0      |

**返回值**：数字，第一个匹配元素的索引，未找到返回 -1

**说明**：查找数组中指定元素的第一个索引

```js
const arr = [1, 2, 3, 4, 5, 3];

// 查找元素 3
console.log(arr.indexOf(3));    // 2

// 从索引 3 开始查找
console.log(arr.indexOf(3, 3)); // 5

// 查找不存在的元素
console.log(arr.indexOf(10));   // -1
```

**输出说明**：`indexOf()` 使用严格相等（===）比较，返回第一个匹配的索引。

### includes()

**语法**：`array.includes(searchElement[, fromIndex])`

**参数说明**：

| 参数名          | 类型   | 说明                           | 是否必需 | 默认值 |
|:----------------|:-------|:-------------------------------|:---------|:-------|
| `searchElement` | any    | 要查找的元素                   | 是       | -      |
| `fromIndex`     | number | 开始查找的索引                 | 否       | 0      |

**返回值**：布尔值，找到返回 `true`，否则返回 `false`

**说明**：检查数组是否包含指定元素

```js
const arr = [1, 2, 3, 4, 5];

// 检查是否包含元素
console.log(arr.includes(3));    // true
console.log(arr.includes(10));   // false

// 从指定索引开始查找
console.log(arr.includes(2, 3)); // false（从索引 3 开始，找不到 2）
```

**输出说明**：`includes()` 使用 SameValueZero 算法比较（NaN 被视为相等），返回布尔值。

## 注意事项

### 1. length 截断陷阱

修改 `length` 会直接删除超出长度的元素，且不可恢复：

```js
const arr = [1, 2, 3, 4, 5];
arr.length = 2;
console.log(arr); // [1, 2]
// 元素 3, 4, 5 被永久删除
```

### 2. 稀疏数组

数组可以有"空洞"（sparse array），即某些索引位置没有元素：

```js
const arr = [1, , 3]; // 索引 1 处为空
console.log(arr.length); // 3
console.log(arr[1]);     // undefined
console.log(1 in arr);   // false（索引 1 不存在）
```

### 3. Array.isArray() 的使用

使用 `Array.isArray()` 检查变量是否为数组，而不是 `typeof`：

```js
const arr = [1, 2, 3];

// 正确方式
console.log(Array.isArray(arr)); // true

// 错误方式
console.log(typeof arr); // "object"（不够准确）
```

### 4. 性能考虑

- `push()` 和 `pop()` 在末尾操作，性能较好
- `unshift()` 和 `shift()` 在开头操作，需要移动所有元素，性能较差
- 对于大量数据，优先使用 `push()`/`pop()` 或考虑使用其他数据结构

### 5. 浅拷贝 vs 深拷贝

`slice()` 创建的是浅拷贝：

```js
const arr = [{ id: 1 }, { id: 2 }];
const copy = arr.slice();
copy[0].id = 10;
console.log(arr[0].id); // 10（原数组也被修改）
```

## 常见错误

### 错误 1：混淆 slice() 和 splice()

```js
const arr = [1, 2, 3, 4, 5];

// slice() 不修改原数组
const part1 = arr.slice(1, 3);
console.log(arr); // [1, 2, 3, 4, 5]（未改变）

// splice() 修改原数组
const part2 = arr.splice(1, 3);
console.log(arr); // [1, 5]（已改变）
```

### 错误 2：使用 == 比较数组元素

```js
const arr = [1, 2, 3];

// 错误：使用 ==
console.log(arr.indexOf("2")); // -1（类型不匹配）

// 正确：使用 ===
console.log(arr.indexOf(2)); // 1
```

## 最佳实践

1. **优先使用数组字面量**：`[]` 比 `new Array()` 更简洁
2. **使用 `Array.isArray()` 检查数组**：不要使用 `typeof`
3. **注意 `slice()` 和 `splice()` 的区别**：`slice()` 不修改原数组，`splice()` 修改
4. **性能考虑**：大量数据时优先使用 `push()`/`pop()` 而不是 `unshift()`/`shift()`
5. **使用 `includes()` 检查存在性**：比 `indexOf() !== -1` 更语义化

## 练习

1. **数组创建**：
   - 使用三种方式创建包含 1-5 的数组
   - 使用 `Array.from()` 创建包含 10 个 0 的数组

2. **数组操作**：
   - 创建一个数组，使用 `push()` 添加元素，然后使用 `pop()` 移除
   - 使用 `slice()` 复制数组，并验证是浅拷贝

3. **查找和检查**：
   - 编写函数检查数组是否包含指定元素
   - 编写函数查找数组中所有匹配元素的索引

4. **数组方法组合**：
   - 使用 `push()`、`pop()`、`unshift()`、`shift()` 实现队列和栈

5. **注意事项实践**：
   - 创建稀疏数组，并检查哪些索引存在
   - 使用 `Array.isArray()` 检查不同类型的变量

## 总结

数组是 JavaScript 中最常用的数据结构：

- **创建**：数组字面量、`Array()`、`Array.of()`、`Array.from()`
- **访问**：使用索引 `[index]` 访问和修改元素
- **长度**：`length` 属性可以获取和设置数组长度
- **方法**：`push()`、`pop()`、`unshift()`、`shift()`、`slice()`、`splice()`、`indexOf()`、`includes()`

掌握这些基础操作是学习数组高级方法的前提。

继续学习下一节，了解数组的高级方法（map、filter、reduce）。

---

**最后更新**：2025-12-16
