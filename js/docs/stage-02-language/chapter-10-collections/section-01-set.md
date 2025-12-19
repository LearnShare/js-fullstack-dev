# 2.10.1 Set 数据结构

## 概述

Set �?ES6 引入的数据结构，用于存储唯一值的集合。Set 对象允许你存储任何类型的唯一值，无论是原始值还是对象引用。Set 中的值只会出现一次，�?Set 中的值是唯一的�?

Set 数据结构的主要特点：
- **唯一�?*：Set 中的每个值都是唯一的，重复的值会被自动忽�?
- **值比�?*：使�?SameValueZero 算法进行值比较（类似于严格相�?===，但 NaN 被视为相等）
- **插入顺序**：Set 按照插入顺序保存元素
- **可迭�?*：Set 是可迭代对象，可以使�?for...of 循环遍历

## Set 的特�?

### 唯一性保�?

Set 保证集合中的每个值都是唯一的。当尝试添加重复的值时，Set 会忽略该操作，不会抛出错误�?

```js
const set = new Set([1, 2, 2, 3, 3, 4]);
console.log(set); // Set(4) { 1, 2, 3, 4 }
// 注意：重复的�?2 �?3 被自动去除了
```

### 值比较机�?

Set 使用 SameValueZero 算法进行值比较：

```js
// 原始类型按值比�?
const set1 = new Set([1, 2, 3]);
set1.add(1); // 重复值，被忽�?
console.log(set1.size); // 3

// NaN 的特殊处�?
const set2 = new Set([NaN]);
set2.add(NaN); // NaN 被视为相等，被忽�?
console.log(set2.size); // 1

// 对象按引用比�?
const obj1 = { id: 1 };
const obj2 = { id: 1 };
const set3 = new Set([obj1]);
set3.add(obj2); // 不同的对象引用，可以添加
console.log(set3.size); // 2

set3.add(obj1); // 相同的对象引用，被忽�?
console.log(set3.size); // 2
```

### 与数组的对比

| 特�?          | Set                    | Array                  |
| :------------- | :--------------------- | :--------------------- |
| **唯一�?*     | 自动保证唯一           | 不保证唯一             |
| **索引访问**   | 不支�?                | 支持                   |
| **长度属�?*   | `size`                 | `length`               |
| **遍历方式**   | for...of、forEach      | for、for...of、forEach |
| **查找性能**   | O(1) 平均              | O(n) 最�?             |
| **插入顺序**   | 保持插入顺序           | 保持插入顺序           |
| **去重功能**   | 内置                   | 需要手动实�?          |

## 创建 Set

### 使用构造函数创建空 Set

**语法**：`new Set()`

```js
// 创建�?Set
const emptySet = new Set();
console.log(emptySet.size); // 0
console.log(emptySet);      // Set(0) {}
```

### 使用可迭代对象创�?Set

**语法**：`new Set(iterable)`

**参数**�?
- `iterable`（可选）：可迭代对象（如数组、字符串、另一�?Set 等）

**返回�?*：新�?Set 对象

```js
// 从数组创�?
const setFromArray = new Set([1, 2, 3, 4, 5]);
console.log(setFromArray); // Set(5) { 1, 2, 3, 4, 5 }

// 从字符串创建（每个字符作为独立元素）
const setFromString = new Set("hello");
console.log(setFromString); // Set(4) { 'h', 'e', 'l', 'o' }
// 注意：重复的 'l' 被去除了

// 从另一�?Set 创建
const originalSet = new Set([1, 2, 3]);
const copiedSet = new Set(originalSet);
console.log(copiedSet); // Set(3) { 1, 2, 3 }
```

### 动态创建和添加元素

```js
// 先创建空 Set，再逐个添加
const set = new Set();

set.add(1);
set.add(2);
set.add(3);
set.add(2); // 重复值，被忽�?

console.log(set); // Set(3) { 1, 2, 3 }
```

## Set 的方法和属�?

### size 属�?

**说明**：返�?Set 对象中元素的数量

**语法**：`set.size`

**返回�?*：数字，表示 Set 中元素的数量

```js
const set = new Set([1, 2, 3, 4, 5]);
console.log(set.size); // 5

// size 是只读属�?
// set.size = 10; // 无效，不会改�?size
```

### add() 方法

**语法格式**：`set.add(value)`

**参数说明**�?

| 参数�?  | 类型 | 说明                           | 是否必需 | 默认�?|
|:---------|:-----|:-------------------------------|:---------|:-------|
| `value`  | any  | 要添加到 Set 的值，可以是任何类�?| �?      | -      |

**返回�?*：Set 对象本身（支持链式调用）

```js
const set = new Set();

// 添加原始类型
set.add(1);
set.add("hello");
set.add(true);
set.add(null);
set.add(undefined);

// 添加对象
const obj = { id: 1 };
set.add(obj);

// 链式调用
set.add(10).add(20).add(30);

console.log(set.size); // 9
```

### has() 方法

**语法格式**：`set.has(value)`

**参数说明**�?

| 参数�?  | 类型 | 说明       | 是否必需 | 默认�?|
|:---------|:-----|:-----------|:---------|:-------|
| `value`  | any  | 要查找的�?| �?      | -      |

**返回�?*：布尔值，如果 Set 中包含该值返�?`true`，否则返�?`false`

```js
const set = new Set([1, 2, 3, "hello"]);

console.log(set.has(1));        // true
console.log(set.has(2));        // true
console.log(set.has(4));        // false
console.log(set.has("hello"));  // true
console.log(set.has("world"));  // false

// 对象引用比较
const obj1 = { id: 1 };
const obj2 = { id: 1 };
set.add(obj1);

console.log(set.has(obj1));     // true（相同的引用�?
console.log(set.has(obj2));     // false（不同的引用，即使内容相同）
```

### delete() 方法

**语法格式**：`set.delete(value)`

**参数说明**�?

| 参数�?  | 类型 | 说明       | 是否必需 | 默认�?|
|:---------|:-----|:-----------|:---------|:-------|
| `value`  | any  | 要删除的�?| �?      | -      |

**返回�?*：布尔值，如果删除成功返回 `true`，如果值不存在返回 `false`

```js
const set = new Set([1, 2, 3, 4, 5]);

console.log(set.delete(3)); // true（删除成功）
console.log(set);           // Set(4) { 1, 2, 4, 5 }

console.log(set.delete(10)); // false（值不存在�?
console.log(set.size);       // 4（未改变�?
```

### clear() 方法

**语法格式**：`set.clear()`

**参数说明**：无参数

**返回�?*：`undefined`

```js
const set = new Set([1, 2, 3, 4, 5]);

console.log(set.size); // 5

set.clear();

console.log(set.size); // 0
console.log(set);      // Set(0) {}
```

## Set 的遍�?

### for...of 循环

```js
const set = new Set([1, 2, 3, 4, 5]);

// 遍历�?
for (const value of set) {
    console.log(value);
}
// 输出�?
// 1
// 2
// 3
// 4
// 5
```

### forEach() 方法

**语法格式**：`set.forEach(callbackFn[, thisArg])`

**参数说明**�?

| 参数�?       | 类型     | 说明                           | 是否必需 | 默认�?|
|:--------------|:---------|:-------------------------------|:---------|:-------|
| `callbackFn`  | Function | 为每个元素执行的函数，接收三个参数：<br>- `value`：当前元素的�?br>- `valueAgain`：当前元素的值（Set 中没有键，所以值重复）<br>- `set`：正在遍历的 Set 对象 | �?      | -      |
| `thisArg`     | any      | 执行 `callbackFn` 时使用的 `this` �?| �?      | -      |

**返回�?*：`undefined`

```js
const set = new Set([1, 2, 3, 4, 5]);

// 基本用法
set.forEach((value) => {
    console.log(value);
});

// 使用所有参�?
set.forEach((value, valueAgain, set) => {
    console.log(`Value: ${value}, Set size: ${set.size}`);
});

// 使用 thisArg
const obj = {
    multiplier: 2,
    process(value) {
        console.log(value * this.multiplier);
    }
};

set.forEach(obj.process, obj);
```

### values() 方法

**说明**：返回一个新的迭代器对象，包�?Set 对象中的所有�?

**语法**：`set.values()`

**返回�?*：新�?Set 迭代器对�?

```js
const set = new Set([1, 2, 3]);

const valuesIterator = set.values();

console.log(valuesIterator.next().value); // 1
console.log(valuesIterator.next().value); // 2
console.log(valuesIterator.next().value); // 3
console.log(valuesIterator.next().done);  // true

// 使用 for...of 遍历迭代�?
for (const value of set.values()) {
    console.log(value);
}
```

### keys() 方法

**说明**：返回一个新的迭代器对象，包�?Set 对象中的所有值（�?`values()` 相同，因�?Set 没有键）

**语法**：`set.keys()`

**返回�?*：新�?Set 迭代器对�?

```js
const set = new Set([1, 2, 3]);

// keys() �?values() 返回相同的内�?
const keysIterator = set.keys();

for (const key of keysIterator) {
    console.log(key); // 1, 2, 3
}
```

### entries() 方法

**说明**：返回一个新的迭代器对象，包�?`[value, value]` 形式的数组（为了�?Map �?API 保持一致）

**语法**：`set.entries()`

**返回�?*：新�?Set 迭代器对�?

```js
const set = new Set([1, 2, 3]);

const entriesIterator = set.entries();

console.log(entriesIterator.next().value); // [1, 1]
console.log(entriesIterator.next().value); // [2, 2]
console.log(entriesIterator.next().value); // [3, 3]

// 使用 for...of 遍历
for (const [value, valueAgain] of set.entries()) {
    console.log(value, valueAgain); // 值重复，都是相同的�?
}
```

## Set 与数组的转换

### 从数组创�?Set（去重）

```js
// 数组去重
const arr = [1, 2, 2, 3, 3, 4, 4, 5];
const uniqueSet = new Set(arr);
console.log(uniqueSet); // Set(5) { 1, 2, 3, 4, 5 }

// 转换为数�?
const uniqueArray = [...uniqueSet];
console.log(uniqueArray); // [1, 2, 3, 4, 5]

// 一行代码完成去�?
const unique = [...new Set(arr)];
console.log(unique); // [1, 2, 3, 4, 5]
```

### �?Set 转换为数�?

```js
const set = new Set([1, 2, 3, 4, 5]);

// 使用展开运算�?
const arr1 = [...set];
console.log(arr1); // [1, 2, 3, 4, 5]

// 使用 Array.from()
const arr2 = Array.from(set);
console.log(arr2); // [1, 2, 3, 4, 5]

// 使用 Array.from() 并转换�?
const arr3 = Array.from(set, x => x * 2);
console.log(arr3); // [2, 4, 6, 8, 10]
```

## Set 的实际应用场�?

### 1. 数组去重

```js
// 基本去重
function removeDuplicates(arr) {
    return [...new Set(arr)];
}

const numbers = [1, 2, 2, 3, 3, 4, 4, 5];
const unique = removeDuplicates(numbers);
console.log(unique); // [1, 2, 3, 4, 5]

// 对象数组去重（需要自定义比较函数�?
function removeDuplicateObjects(arr, keyFn) {
    const seen = new Set();
    return arr.filter(item => {
        const key = keyFn(item);
        if (seen.has(key)) {
            return false;
        }
        seen.add(key);
        return true;
    });
}

const users = [
    { id: 1, name: "John" },
    { id: 2, name: "Jane" },
    { id: 1, name: "John" }, // 重复
    { id: 3, name: "Bob" }
];

const uniqueUsers = removeDuplicateObjects(users, user => user.id);
console.log(uniqueUsers);
// [{ id: 1, name: "John" }, { id: 2, name: "Jane" }, { id: 3, name: "Bob" }]
```

### 2. 集合运算

```js
// 并集
function union(setA, setB) {
    return new Set([...setA, ...setB]);
}

// 交集
function intersection(setA, setB) {
    return new Set([...setA].filter(x => setB.has(x)));
}

// 差集（A - B�?
function difference(setA, setB) {
    return new Set([...setA].filter(x => !setB.has(x)));
}

// 对称差集（A �?B 的并集减去交集）
function symmetricDifference(setA, setB) {
    return difference(union(setA, setB), intersection(setA, setB));
}

// 使用示例
const setA = new Set([1, 2, 3, 4]);
const setB = new Set([3, 4, 5, 6]);

console.log(union(setA, setB));              // Set(6) { 1, 2, 3, 4, 5, 6 }
console.log(intersection(setA, setB));      // Set(2) { 3, 4 }
console.log(difference(setA, setB));         // Set(2) { 1, 2 }
console.log(symmetricDifference(setA, setB)); // Set(4) { 1, 2, 5, 6 }
```

### 3. 快速查�?

```js
// 使用 Set 进行快速成员检�?
function createLookupSet(items) {
    return new Set(items);
}

const allowedUsers = createLookupSet([1, 2, 3, 4, 5]);

function isUserAllowed(userId) {
    return allowedUsers.has(userId);
}

console.log(isUserAllowed(3)); // true
console.log(isUserAllowed(10)); // false

// 性能对比：Set vs Array
const largeArray = Array.from({ length: 1000000 }, (_, i) => i);
const largeSet = new Set(largeArray);

// Set 查找：O(1) 平均
console.time("Set lookup");
largeSet.has(999999);
console.timeEnd("Set lookup");

// Array 查找：O(n) 最�?
console.time("Array lookup");
largeArray.includes(999999);
console.timeEnd("Array lookup");
```

### 4. 标记已处理的项目

```js
// 跟踪已处理的项目
const processedItems = new Set();

function processItem(item) {
    if (processedItems.has(item.id)) {
        console.log(`Item ${item.id} already processed`);
        return;
    }
    
    // 处理项目
    console.log(`Processing item ${item.id}`);
    processedItems.add(item.id);
}

const items = [
    { id: 1, name: "Item 1" },
    { id: 2, name: "Item 2" },
    { id: 1, name: "Item 1" }, // 重复
    { id: 3, name: "Item 3" }
];

items.forEach(processItem);
// 输出�?
// Processing item 1
// Processing item 2
// Item 1 already processed
// Processing item 3
```

### 5. 字符串字符去�?

```js
// 获取字符串中的唯一字符
function getUniqueCharacters(str) {
    return [...new Set(str)].join("");
}

const text = "hello world";
const uniqueChars = getUniqueCharacters(text);
console.log(uniqueChars); // "helo wrd"

// 检查字符串是否包含重复字符
function hasDuplicateCharacters(str) {
    return new Set(str).size !== str.length;
}

console.log(hasDuplicateCharacters("hello")); // true（有重复�?'l'�?
console.log(hasDuplicateCharacters("world"));  // false（无重复字符�?
```

## 完整示例

```js
// 完整�?Set 使用示例
class SetExamples {
    static demonstrate() {
        console.log("=== 创建 Set ===");
        const set1 = new Set([1, 2, 3, 4, 5]);
        const set2 = new Set();
        set2.add("apple");
        set2.add("banana");
        set2.add("apple"); // 重复值，被忽�?
        
        console.log("Set 1:", set1);
        console.log("Set 2:", set2);
        console.log("Set 2 size:", set2.size);
        
        console.log("\n=== 检查成�?===");
        console.log("set1.has(3):", set1.has(3));     // true
        console.log("set1.has(10):", set1.has(10));     // false
        console.log("set2.has('apple'):", set2.has("apple")); // true
        
        console.log("\n=== 遍历 Set ===");
        console.log("使用 for...of:");
        for (const value of set1) {
            console.log(value);
        }
        
        console.log("\n使用 forEach:");
        set1.forEach((value) => {
            console.log(value);
        });
        
        console.log("\n=== 集合运算 ===");
        const setA = new Set([1, 2, 3, 4]);
        const setB = new Set([3, 4, 5, 6]);
        
        // 并集
        const union = new Set([...setA, ...setB]);
        console.log("并集:", [...union]);
        
        // 交集
        const intersection = new Set([...setA].filter(x => setB.has(x)));
        console.log("交集:", [...intersection]);
        
        // 差集
        const difference = new Set([...setA].filter(x => !setB.has(x)));
        console.log("差集 (A - B):", [...difference]);
        
        console.log("\n=== 数组去重 ===");
        const arr = [1, 2, 2, 3, 3, 4, 4, 5];
        const unique = [...new Set(arr)];
        console.log("原数�?", arr);
        console.log("去重�?", unique);
        
        console.log("\n=== 删除元素 ===");
        const set3 = new Set([1, 2, 3, 4, 5]);
        console.log("删除�?", [...set3]);
        set3.delete(3);
        console.log("删除 3 �?", [...set3]);
        set3.clear();
        console.log("清空�?", [...set3]);
    }
}

SetExamples.demonstrate();
```

## 注意事项

### 1. 对象引用的唯一�?

Set 使用引用比较对象，内容相同的不同对象被视为不同的值：

```js
const obj1 = { id: 1, name: "John" };
const obj2 = { id: 1, name: "John" };
const set = new Set([obj1]);

console.log(set.has(obj1)); // true
console.log(set.has(obj2)); // false（不同的对象引用�?

set.add(obj2);
console.log(set.size); // 2（两个不同的对象�?
```

### 2. NaN 的特殊处�?

NaN �?Set 中被视为相等�?

```js
const set = new Set([NaN]);
console.log(set.has(NaN)); // true

set.add(NaN);
console.log(set.size); // 1（NaN 被视为相等）
```

### 3. +0 �?-0 的处�?

+0 �?-0 �?Set 中被视为相等�?

```js
const set = new Set([+0]);
set.add(-0);
console.log(set.size); // 1�?0 �?-0 被视为相等）
```

### 4. 性能考虑

- **查找性能**：Set �?`has()` 方法平均时间复杂度为 O(1)，比数组�?`includes()` 方法（O(n)）快得多
- **插入性能**：Set �?`add()` 方法平均时间复杂度为 O(1)
- **内存使用**：Set 使用哈希表实现，内存使用略高于数�?

### 5. 不能直接访问元素

Set 不支持索引访问，不能使用 `set[0]` 这样的语法：

```js
const set = new Set([1, 2, 3]);
// console.log(set[0]); // undefined（不支持索引访问�?

// 需要转换为数组或使用迭代器
const arr = [...set];
console.log(arr[0]); // 1
```

## 常见问题

### 问题 1：如何获�?Set 中的第一个元素？

```js
const set = new Set([1, 2, 3, 4, 5]);

// 方法 1：使用迭代器
const first = set.values().next().value;
console.log(first); // 1

// 方法 2：转换为数组
const first2 = [...set][0];
console.log(first2); // 1
```

### 问题 2：如何检�?Set 是否为空�?

```js
const set = new Set();

// 方法 1：使�?size 属�?
if (set.size === 0) {
    console.log("Set is empty");
}

// 方法 2：转换为布尔�?
if (!set.size) {
    console.log("Set is empty");
}
```

### 问题 3：如何合并多�?Set�?

```js
const set1 = new Set([1, 2, 3]);
const set2 = new Set([4, 5, 6]);
const set3 = new Set([7, 8, 9]);

// 方法 1：使用展开运算�?
const merged = new Set([...set1, ...set2, ...set3]);
console.log([...merged]); // [1, 2, 3, 4, 5, 6, 7, 8, 9]

// 方法 2：逐个添加
const merged2 = new Set(set1);
set2.forEach(value => merged2.add(value));
set3.forEach(value => merged2.add(value));
```

### 问题 4：如何对 Set 进行排序�?

```js
const set = new Set([3, 1, 4, 1, 5, 9, 2, 6]);

// Set 本身不排序，需要转换为数组后排�?
const sorted = [...set].sort((a, b) => a - b);
console.log(sorted); // [1, 2, 3, 4, 5, 6, 9]

// 降序
const sortedDesc = [...set].sort((a, b) => b - a);
console.log(sortedDesc); // [9, 6, 5, 4, 3, 2, 1]
```

## 最佳实�?

### 1. 使用 Set 进行快速查�?

```js
// 好的做法：使�?Set 进行快速查�?
const allowedIds = new Set([1, 2, 3, 4, 5]);
if (allowedIds.has(userId)) {
    // 处理允许的用�?
}

// 避免：使用数组进行查�?
const allowedIdsArray = [1, 2, 3, 4, 5];
if (allowedIdsArray.includes(userId)) {
    // 性能较差，特别是对于大数�?
}
```

### 2. 使用 Set 进行数组去重

```js
// 好的做法：使�?Set 去重
const unique = [...new Set(array)];

// 避免：手动去�?
const unique2 = [];
for (let item of array) {
    if (!unique2.includes(item)) {
        unique2.push(item);
    }
}
```

### 3. 使用 Set 跟踪状�?

```js
// 好的做法：使�?Set 跟踪已处理的项目
const processed = new Set();

function processItem(item) {
    if (processed.has(item.id)) {
        return; // 已处�?
    }
    // 处理项目
    processed.add(item.id);
}
```

### 4. 集合运算使用 Set

```js
// 好的做法：使�?Set 进行集合运算
function getCommonElements(arr1, arr2) {
    const set1 = new Set(arr1);
    const set2 = new Set(arr2);
    return [...set1].filter(x => set2.has(x));
}

// 避免：使用数组进行集合运算（性能较差�?
function getCommonElementsSlow(arr1, arr2) {
    return arr1.filter(x => arr2.includes(x));
}
```

## 练习

1. **实现数组去重函数**：编写一个函数，接受一个数组作为参数，返回去重后的新数组�?

2. **实现集合运算函数**：编写函数实现并集、交集、差集和对称差集运算�?

3. **实现快速查找函�?*：使�?Set 实现一个函数，检查一个值是否在一组值中存在�?

4. **实现字符统计函数**：编写一个函数，统计字符串中每个唯一字符出现的次数�?

5. **实现权限检查系�?*：使�?Set 实现一个权限检查系统，能够快速检查用户是否具有特定权限�?

6. **实现标签系统**：使�?Set 实现一个标签系统，能够为文章添加标签，并支持标签的查询和去重�?

完成以上练习后，继续学习下一节，了解 Map 数据结构�?
