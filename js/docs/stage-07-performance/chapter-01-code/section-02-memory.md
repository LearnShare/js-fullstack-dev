# 7.1.2 内存管理

## 概述

内存管理是 JavaScript 性能优化的重要方面。本节介绍内存分配、内存泄漏的识别和预防，以及内存优化的方法。

## 内存生命周期

### 分配

JavaScript 引擎自动分配内存：

```js
// 变量声明时分配内存
const number = 123;
const string = 'text';
const object = { name: 'test' };
const array = [1, 2, 3];
```

### 使用

分配的内存被读取和写入：

```js
const obj = { name: 'test' };
obj.name = 'new name'; // 写入
console.log(obj.name); // 读取
```

### 释放

当内存不再需要时，垃圾回收器自动释放：

```js
let obj = { name: 'test' };
obj = null; // 对象可以被垃圾回收
```

## 内存泄漏

### 什么是内存泄漏

内存泄漏是指不再使用的内存没有被释放，导致内存占用持续增长。

### 常见的内存泄漏场景

#### 1. 全局变量

```js
// 错误：意外创建全局变量
function leak() {
    name = 'test'; // 没有 var/let/const，成为全局变量
}

// 正确：使用局部变量
function noLeak() {
    const name = 'test';
}
```

#### 2. 闭包

```js
// 错误：闭包持有大量数据
function createLeak() {
    const largeData = new Array(1000000).fill(0);
    return function() {
        console.log('closure'); // 闭包持有 largeData
    };
}

// 正确：只保留需要的数据
function createNoLeak() {
    const largeData = new Array(1000000).fill(0);
    const neededData = largeData.length; // 只保留需要的数据
    return function() {
        console.log(neededData);
    };
}
```

#### 3. 事件监听器未移除

```js
// 错误：事件监听器未移除
function addListener() {
    const button = document.getElementById('button');
    button.addEventListener('click', handleClick);
    // 如果元素被移除，监听器仍然存在
}

// 正确：移除事件监听器
function addListenerCorrect() {
    const button = document.getElementById('button');
    button.addEventListener('click', handleClick);
    
    // 在适当时机移除
    button.removeEventListener('click', handleClick);
}
```

#### 4. 定时器未清除

```js
// 错误：定时器未清除
function startTimer() {
    setInterval(() => {
        console.log('tick');
    }, 1000);
    // 定时器会一直运行
}

// 正确：清除定时器
function startTimerCorrect() {
    const timerId = setInterval(() => {
        console.log('tick');
    }, 1000);
    
    // 在适当时机清除
    clearInterval(timerId);
}
```

#### 5. DOM 引用

```js
// 错误：保留 DOM 引用
const elements = [];
function addElement() {
    const div = document.createElement('div');
    document.body.appendChild(div);
    elements.push(div); // 即使从 DOM 移除，仍然保留引用
}

// 正确：移除引用
function addElementCorrect() {
    const div = document.createElement('div');
    document.body.appendChild(div);
    // 不需要时移除引用
    // elements = elements.filter(el => el !== div);
}
```

## 内存优化方法

### 1. 及时释放引用

```js
// 使用完毕后设置为 null
let largeData = new Array(1000000).fill(0);
// 使用 largeData
largeData = null; // 释放引用
```

### 2. 使用 WeakMap/WeakSet

```js
// WeakMap 的键是弱引用，不会阻止垃圾回收
const weakMap = new WeakMap();
const obj = { data: 'test' };
weakMap.set(obj, 'value');
// 当 obj 被回收时，WeakMap 中的条目也会被自动移除
```

### 3. 避免循环引用

```js
// 错误：循环引用
let obj1 = { name: 'obj1' };
let obj2 = { name: 'obj2' };
obj1.ref = obj2;
obj2.ref = obj1; // 循环引用

// 正确：使用 WeakMap 或单向引用
const weakMap = new WeakMap();
weakMap.set(obj1, obj2);
```

### 4. 分批处理大数据

```js
// 错误：一次性处理大量数据
function processLargeArray(arr) {
    return arr.map(item => expensiveOperation(item));
}

// 正确：分批处理
async function processLargeArrayOptimized(arr, batchSize = 1000) {
    const results = [];
    for (let i = 0; i < arr.length; i += batchSize) {
        const batch = arr.slice(i, i + batchSize);
        const batchResults = batch.map(item => expensiveOperation(item));
        results.push(...batchResults);
        // 让浏览器有机会处理其他任务
        await new Promise(resolve => setTimeout(resolve, 0));
    }
    return results;
}
```

### 5. 对象池模式

```js
// 对象池：复用对象，减少内存分配
class ObjectPool {
    constructor(createFn, resetFn) {
        this.createFn = createFn;
        this.resetFn = resetFn;
        this.pool = [];
    }
    
    acquire() {
        return this.pool.length > 0
            ? this.pool.pop()
            : this.createFn();
    }
    
    release(obj) {
        this.resetFn(obj);
        this.pool.push(obj);
    }
}

// 使用
const pool = new ObjectPool(
    () => ({ x: 0, y: 0 }),
    obj => { obj.x = 0; obj.y = 0; }
);

const obj = pool.acquire();
// 使用 obj
pool.release(obj);
```

## 内存分析工具

### Chrome DevTools Memory 面板

1. 打开 Chrome DevTools
2. 切换到 Memory 标签
3. 选择 Heap Snapshot
4. 点击 Take snapshot 拍摄快照
5. 对比多个快照，找出内存泄漏

### Performance Monitor

```js
// 使用 Performance API 监控内存
if ('memory' in performance) {
    setInterval(() => {
        const memory = performance.memory;
        console.log({
            used: (memory.usedJSHeapSize / 1048576).toFixed(2) + ' MB',
            total: (memory.totalJSHeapSize / 1048576).toFixed(2) + ' MB',
            limit: (memory.jsHeapSizeLimit / 1048576).toFixed(2) + ' MB'
        });
    }, 1000);
}
```

## 注意事项

1. **及时清理**：使用完毕后及时清理引用和监听器
2. **避免全局变量**：避免意外创建全局变量
3. **使用弱引用**：在适当场景使用 WeakMap/WeakSet
4. **监控内存**：使用工具监控内存使用情况
5. **测试验证**：在真实场景中测试内存使用

## 常见错误

### 错误 1：忘记移除事件监听器

```js
// 错误：元素移除后监听器仍然存在
function createElement() {
    const div = document.createElement('div');
    div.addEventListener('click', handleClick);
    document.body.appendChild(div);
    // 移除元素但未移除监听器
    document.body.removeChild(div);
}

// 正确：移除监听器
function createElementCorrect() {
    const div = document.createElement('div');
    const handler = () => handleClick();
    div.addEventListener('click', handler);
    document.body.appendChild(div);
    // 移除时同时移除监听器
    div.removeEventListener('click', handler);
    document.body.removeChild(div);
}
```

### 错误 2：闭包持有大量数据

```js
// 错误：闭包持有不需要的数据
function createHandler() {
    const largeData = new Array(1000000).fill(0);
    return function(event) {
        console.log(event.type); // 不需要 largeData
    };
}

// 正确：只保留需要的数据
function createHandlerCorrect() {
    return function(event) {
        console.log(event.type);
    };
}
```

## 最佳实践

1. **及时清理**：使用完毕后及时清理引用、监听器和定时器
2. **避免全局变量**：使用 let/const 声明变量
3. **使用弱引用**：在适当场景使用 WeakMap/WeakSet
4. **监控内存**：使用工具监控内存使用情况
5. **测试验证**：在真实场景中测试内存使用

## 练习

1. **内存泄漏检测**：编写代码检测常见的内存泄漏场景。

2. **事件监听器清理**：实现一个事件管理器，自动清理事件监听器。

3. **对象池实现**：实现一个对象池，用于复用对象减少内存分配。

4. **内存监控**：使用 Performance API 监控内存使用情况。

5. **大数据处理**：实现一个分批处理大数据的函数，避免内存溢出。

完成以上练习后，继续学习下一节，了解垃圾回收机制。

## 总结

内存管理是 JavaScript 性能优化的重要方面。通过识别和预防内存泄漏，及时释放引用，使用弱引用和对象池等技术，可以有效优化内存使用。使用内存分析工具可以帮助识别和解决内存问题。

## 相关资源

- [MDN：内存管理](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Memory_Management)
- [Chrome DevTools Memory 面板](https://developer.chrome.com/docs/devtools/memory-problems/)
