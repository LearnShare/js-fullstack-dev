# 7.1.3 垃圾回收机制

## 概述

垃圾回收（Garbage Collection，GC）是 JavaScript 引擎自动管理内存的机制。本节介绍 V8 引擎的垃圾回收算法、优化建议和最佳实践。

## 垃圾回收基础

### 什么是垃圾回收

垃圾回收是自动内存管理机制，自动识别和释放不再使用的内存。

### 标记-清除算法

V8 引擎使用标记-清除（Mark-and-Sweep）算法：

1. **标记阶段**：从根对象开始，标记所有可达对象
2. **清除阶段**：清除未标记的对象

```js
// 示例
let obj1 = { name: 'obj1' };
let obj2 = { name: 'obj2' };
obj1.ref = obj2;
obj2.ref = obj1;

obj1 = null;
obj2 = null;
// 虽然 obj1 和 obj2 相互引用，但标记-清除算法可以处理循环引用
```

## V8 引擎的垃圾回收

### 分代垃圾回收

V8 将堆内存分为两个区域：

1. **新生代（New Space）**：新创建的对象
2. **老生代（Old Space）**：存活时间较长的对象

### 新生代垃圾回收

使用 **Scavenge 算法**（复制算法）：

```js
// 新生代分为两个半空间：From 和 To
// 1. 新对象分配在 From 空间
// 2. From 空间满时，将存活对象复制到 To 空间
// 3. 清空 From 空间，交换 From 和 To
```

特点：
- 速度快，适合频繁回收
- 空间利用率低（只有一半空间可用）

### 老生代垃圾回收

使用 **标记-清除-整理算法**：

1. **标记**：标记所有存活对象
2. **清除**：清除未标记对象
3. **整理**：整理内存碎片

特点：
- 回收时间长，但频率低
- 空间利用率高

### 增量标记

为了减少垃圾回收的停顿时间，V8 使用增量标记：

```js
// 将标记过程分成多个小步骤
// 在 JavaScript 执行间隙进行标记
// 减少单次停顿时间
```

## 优化建议

### 1. 减少对象创建

```js
// 错误：频繁创建对象
function processData(arr) {
    return arr.map(item => ({
        value: item * 2,
        timestamp: Date.now()
    })); // 每次迭代都创建新对象
}

// 正确：复用对象或使用原始值
function processDataOptimized(arr) {
    const result = [];
    for (let i = 0; i < arr.length; i++) {
        result.push(arr[i] * 2); // 只使用原始值
    }
    return result;
}
```

### 2. 避免在循环中创建函数

```js
// 错误：在循环中创建函数
function badExample(arr) {
    const callbacks = [];
    for (let i = 0; i < arr.length; i++) {
        callbacks.push(function() {
            console.log(arr[i]); // 每个函数都创建闭包
        });
    }
    return callbacks;
}

// 正确：在循环外创建函数
function goodExample(arr) {
    const callbacks = [];
    const logItem = (item) => () => console.log(item);
    for (let i = 0; i < arr.length; i++) {
        callbacks.push(logItem(arr[i]));
    }
    return callbacks;
}
```

### 3. 使用对象池

```js
// 对象池：复用对象，减少垃圾回收
class Vector2DPool {
    constructor() {
        this.pool = [];
    }
    
    acquire(x = 0, y = 0) {
        const vec = this.pool.pop() || { x: 0, y: 0 };
        vec.x = x;
        vec.y = y;
        return vec;
    }
    
    release(vec) {
        this.pool.push(vec);
    }
}

const pool = new Vector2DPool();
const vec = pool.acquire(10, 20);
// 使用 vec
pool.release(vec);
```

### 4. 避免内存泄漏

```js
// 及时释放引用
let largeData = new Array(1000000).fill(0);
// 使用完毕后
largeData = null; // 帮助垃圾回收
```

### 5. 使用 WeakMap/WeakSet

```js
// WeakMap 的键是弱引用，不会阻止垃圾回收
const cache = new WeakMap();

function getCachedData(obj) {
    if (!cache.has(obj)) {
        cache.set(obj, expensiveOperation(obj));
    }
    return cache.get(obj);
}
// 当 obj 被回收时，cache 中的条目也会被自动移除
```

## 性能监控

### 监控垃圾回收

```js
// 使用 Performance API
if ('memory' in performance) {
    const memory = performance.memory;
    console.log('Used:', (memory.usedJSHeapSize / 1048576).toFixed(2), 'MB');
    console.log('Total:', (memory.totalJSHeapSize / 1048576).toFixed(2), 'MB');
}
```

### Chrome DevTools

1. 打开 Performance 面板
2. 勾选 Memory 选项
3. 录制性能
4. 查看内存使用和垃圾回收事件

## 注意事项

1. **不要手动触发 GC**：让引擎自动管理
2. **理解分代回收**：新对象和老对象有不同的回收策略
3. **减少对象创建**：复用对象，使用对象池
4. **避免内存泄漏**：及时释放引用
5. **监控内存使用**：使用工具监控内存和 GC

## 常见错误

### 错误 1：频繁创建临时对象

```js
// 错误：在循环中频繁创建对象
function processItems(items) {
    const results = [];
    for (let i = 0; i < items.length; i++) {
        results.push({
            id: items[i].id,
            value: items[i].value * 2
        }); // 每次迭代都创建新对象
    }
    return results;
}

// 正确：如果可能，复用对象结构
function processItemsOptimized(items) {
    const results = [];
    const temp = {}; // 复用临时对象
    for (let i = 0; i < items.length; i++) {
        temp.id = items[i].id;
        temp.value = items[i].value * 2;
        results.push({ ...temp }); // 浅拷贝
    }
    return results;
}
```

### 错误 2：持有不必要的引用

```js
// 错误：持有大量不需要的引用
const cache = new Map();
function processData(data) {
    // 缓存所有数据，即使不再需要
    cache.set(data.id, data);
    return process(data);
}

// 正确：使用 WeakMap 或及时清理
const cache = new WeakMap();
function processDataOptimized(data) {
    cache.set(data, process(data));
    return cache.get(data);
}
```

## 最佳实践

1. **减少对象创建**：复用对象，使用对象池
2. **避免内存泄漏**：及时释放引用，清理监听器
3. **使用弱引用**：在适当场景使用 WeakMap/WeakSet
4. **监控内存**：使用工具监控内存使用和 GC
5. **理解 GC 机制**：理解分代回收和增量标记

## 练习

1. **对象池实现**：实现一个通用的对象池，用于复用对象。

2. **内存监控**：使用 Performance API 监控内存使用和垃圾回收。

3. **WeakMap 应用**：使用 WeakMap 实现一个缓存系统，自动清理不需要的缓存。

4. **减少对象创建**：优化一个频繁创建对象的函数，减少垃圾回收压力。

5. **GC 性能分析**：使用 Chrome DevTools 分析垃圾回收对性能的影响。

完成以上练习后，继续学习下一章，了解浏览器性能优化。

## 总结

垃圾回收是 JavaScript 引擎自动管理内存的机制。V8 引擎使用分代垃圾回收，将内存分为新生代和老生代，使用不同的回收算法。通过减少对象创建、使用对象池、避免内存泄漏等方法，可以优化垃圾回收性能。使用性能监控工具可以帮助识别和解决性能问题。

## 相关资源

- [V8 引擎垃圾回收](https://v8.dev/blog/trash-talk)
- [Chrome DevTools Memory 面板](https://developer.chrome.com/docs/devtools/memory-problems/)
