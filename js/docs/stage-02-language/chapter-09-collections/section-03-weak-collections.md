# 2.9.3 WeakSet 与 WeakMap

## 概述

WeakSet 和 WeakMap 是 ES6 引入的弱引用集合类型。它们与 Set 和 Map 的主要区别在于：WeakSet 和 WeakMap 中的键（对于 WeakSet 是值）必须是对象，并且这些对象是弱引用的，不会阻止垃圾回收。

WeakSet 和 WeakMap 的主要特点：
- **弱引用**：不会阻止垃圾回收器回收对象
- **只能存储对象**：键（WeakSet 的值）必须是对象类型
- **不可迭代**：没有 size 属性，不能遍历
- **不可枚举**：没有 keys()、values()、entries() 等方法
- **内存管理**：适合存储对象的元数据，不会造成内存泄漏

## WeakSet

### WeakSet 的特性

WeakSet 是对象的集合，其中每个对象只能出现一次。WeakSet 中的对象是弱引用的，这意味着如果没有其他引用指向这些对象，它们会被垃圾回收。

**主要特点**：
- 只能存储对象（不能存储原始值）
- 弱引用，不会阻止垃圾回收
- 不可迭代，没有 size 属性
- 没有 clear() 方法

### 创建 WeakSet

**语法**：`new WeakSet([iterable])`

**参数**：
- `iterable`（可选）：可迭代对象，每个元素必须是对象

**返回值**：新的 WeakSet 对象

```js
// 创建空 WeakSet
const weakSet = new WeakSet();

// 从可迭代对象创建（每个元素必须是对象）
const obj1 = { id: 1 };
const obj2 = { id: 2 };
const obj3 = { id: 3 };

const weakSet2 = new WeakSet([obj1, obj2, obj3]);
```

### WeakSet 的方法

#### add() 方法

**说明**：向 WeakSet 对象添加一个新对象

**语法**：`weakSet.add(value)`

**参数**：
- `value`（必需）：要添加到 WeakSet 的对象（必须是对象类型）

**返回值**：WeakSet 对象本身（支持链式调用）

```js
const weakSet = new WeakSet();
const obj1 = { id: 1 };
const obj2 = { id: 2 };

weakSet.add(obj1);
weakSet.add(obj2);

// 链式调用
weakSet.add({ id: 3 }).add({ id: 4 });

// 错误：不能添加原始值
// weakSet.add(1);        // TypeError: Invalid value used in weak set
// weakSet.add("hello");  // TypeError: Invalid value used in weak set
// weakSet.add(null);     // TypeError: Invalid value used in weak set
```

#### has() 方法

**说明**：检查 WeakSet 对象中是否包含指定的对象

**语法**：`weakSet.has(value)`

**参数**：
- `value`（必需）：要检查的对象

**返回值**：布尔值，如果 WeakSet 中包含该对象返回 `true`，否则返回 `false`

```js
const weakSet = new WeakSet();
const obj1 = { id: 1 };
const obj2 = { id: 2 };

weakSet.add(obj1);

console.log(weakSet.has(obj1)); // true
console.log(weakSet.has(obj2)); // false

// 注意：对象引用必须相同
const obj3 = { id: 1 }; // 内容相同但引用不同
console.log(weakSet.has(obj3)); // false
```

#### delete() 方法

**说明**：从 WeakSet 对象中删除指定的对象

**语法**：`weakSet.delete(value)`

**参数**：
- `value`（必需）：要删除的对象

**返回值**：布尔值，如果删除成功返回 `true`，如果对象不存在返回 `false`

```js
const weakSet = new WeakSet();
const obj1 = { id: 1 };
const obj2 = { id: 2 };

weakSet.add(obj1);
weakSet.add(obj2);

console.log(weakSet.delete(obj1)); // true（删除成功）
console.log(weakSet.has(obj1));   // false

console.log(weakSet.delete({ id: 3 })); // false（对象不存在）
```

### WeakSet 的使用场景

#### 1. 标记对象

WeakSet 最常见的用途是标记对象，用于跟踪哪些对象已经被处理过：

```js
// 标记已处理的对象
const processed = new WeakSet();

function processObject(obj) {
    // 检查是否已处理
    if (processed.has(obj)) {
        console.log("Object already processed");
        return;
    }
    
    // 处理对象
    console.log("Processing object:", obj);
    
    // 标记为已处理
    processed.add(obj);
}

const obj1 = { id: 1, data: "data1" };
const obj2 = { id: 2, data: "data2" };

processObject(obj1); // Processing object: { id: 1, data: "data1" }
processObject(obj1); // Object already processed
processObject(obj2); // Processing object: { id: 2, data: "data2" }
```

#### 2. 防止循环引用

WeakSet 可以用于检测和防止循环引用：

```js
function deepClone(obj, visited = new WeakSet()) {
    // 检查是否已访问（防止循环引用）
    if (visited.has(obj)) {
        throw new Error("Circular reference detected");
    }
    
    if (typeof obj !== "object" || obj === null) {
        return obj;
    }
    
    visited.add(obj);
    
    if (Array.isArray(obj)) {
        return obj.map(item => deepClone(item, visited));
    }
    
    const cloned = {};
    for (const key in obj) {
        if (obj.hasOwnProperty(key)) {
            cloned[key] = deepClone(obj[key], visited);
        }
    }
    
    return cloned;
}

const obj = { a: 1 };
obj.self = obj; // 创建循环引用

try {
    deepClone(obj);
} catch (error) {
    console.log(error.message); // "Circular reference detected"
}
```

#### 3. DOM 元素标记

WeakSet 可以用于标记 DOM 元素，当元素被移除时，WeakSet 中的引用会自动被垃圾回收：

```js
// 标记已初始化的 DOM 元素
const initializedElements = new WeakSet();

function initializeElement(element) {
    if (initializedElements.has(element)) {
        return; // 已初始化
    }
    
    // 初始化元素
    element.dataset.initialized = "true";
    initializedElements.add(element);
}

const button = document.querySelector("button");
initializeElement(button);

// 当元素从 DOM 中移除时，WeakSet 中的引用会自动被垃圾回收
```

## WeakMap

### WeakMap 的特性

WeakMap 是键值对的集合，其中键必须是对象，值是任意类型。WeakMap 中的键是弱引用的，这意味着如果没有其他引用指向这些键对象，它们会被垃圾回收。

**主要特点**：
- 键必须是对象（不能是原始值）
- 弱引用，不会阻止垃圾回收
- 不可迭代，没有 size 属性
- 没有 clear() 方法
- 没有 keys()、values()、entries() 方法

### 创建 WeakMap

**语法**：`new WeakMap([iterable])`

**参数**：
- `iterable`（可选）：可迭代对象，每个元素应该是 `[key, value]` 形式的数组，其中 key 必须是对象

**返回值**：新的 WeakMap 对象

```js
// 创建空 WeakMap
const weakMap = new WeakMap();

// 从可迭代对象创建
const obj1 = { id: 1 };
const obj2 = { id: 2 };

const weakMap2 = new WeakMap([
    [obj1, "value1"],
    [obj2, "value2"]
]);
```

### WeakMap 的方法

#### set() 方法

**说明**：向 WeakMap 对象添加或更新一个键值对

**语法**：`weakMap.set(key, value)`

**参数**：
- `key`（必需）：要添加的键，必须是对象类型
- `value`（必需）：要添加的值，可以是任何类型

**返回值**：WeakMap 对象本身（支持链式调用）

```js
const weakMap = new WeakMap();
const obj1 = { id: 1 };
const obj2 = { id: 2 };

weakMap.set(obj1, "value1");
weakMap.set(obj2, { name: "John", age: 30 });

// 链式调用
weakMap.set({ id: 3 }, "value3").set({ id: 4 }, "value4");

// 错误：键必须是对象
// weakMap.set("key", "value");    // TypeError: Invalid value used as weak map key
// weakMap.set(1, "value");        // TypeError: Invalid value used as weak map key
// weakMap.set(null, "value");     // TypeError: Invalid value used as weak map key
```

#### get() 方法

**说明**：从 WeakMap 对象中获取指定键对应的值

**语法**：`weakMap.get(key)`

**参数**：
- `key`（必需）：要查找的键

**返回值**：如果键存在，返回对应的值；如果键不存在，返回 `undefined`

```js
const weakMap = new WeakMap();
const obj1 = { id: 1 };
const obj2 = { id: 2 };

weakMap.set(obj1, "value1");
weakMap.set(obj2, { name: "John" });

console.log(weakMap.get(obj1)); // "value1"
console.log(weakMap.get(obj2)); // { name: "John" }
console.log(weakMap.get({ id: 1 })); // undefined（不同的对象引用）
```

#### has() 方法

**说明**：检查 WeakMap 对象中是否包含指定的键

**语法**：`weakMap.has(key)`

**参数**：
- `key`（必需）：要检查的键

**返回值**：布尔值，如果 WeakMap 中包含该键返回 `true`，否则返回 `false`

```js
const weakMap = new WeakMap();
const obj1 = { id: 1 };
const obj2 = { id: 2 };

weakMap.set(obj1, "value1");

console.log(weakMap.has(obj1)); // true
console.log(weakMap.has(obj2)); // false
```

#### delete() 方法

**说明**：从 WeakMap 对象中删除指定的键值对

**语法**：`weakMap.delete(key)`

**参数**：
- `key`（必需）：要删除的键

**返回值**：布尔值，如果删除成功返回 `true`，如果键不存在返回 `false`

```js
const weakMap = new WeakMap();
const obj1 = { id: 1 };
const obj2 = { id: 2 };

weakMap.set(obj1, "value1");
weakMap.set(obj2, "value2");

console.log(weakMap.delete(obj1)); // true（删除成功）
console.log(weakMap.has(obj1));     // false

console.log(weakMap.delete({ id: 3 })); // false（键不存在）
```

### WeakMap 的使用场景

#### 1. 私有数据存储

WeakMap 最常见的用途是存储对象的私有数据，实现真正的私有属性：

```js
// 使用 WeakMap 实现私有属性
const privateData = new WeakMap();

class User {
    constructor(name, email) {
        // 将私有数据存储在 WeakMap 中
        privateData.set(this, {
            name: name,
            email: email,
            password: this.generatePassword()
        });
    }
    
    generatePassword() {
        return Math.random().toString(36).slice(-8);
    }
    
    getName() {
        return privateData.get(this).name;
    }
    
    getEmail() {
        return privateData.get(this).email;
    }
    
    // 无法直接访问 password
    // 当 User 实例被垃圾回收时，WeakMap 中的私有数据也会被自动清理
}

const user = new User("John", "john@example.com");
console.log(user.getName());  // "John"
console.log(user.getEmail()); // "john@example.com"
// console.log(user.password); // undefined（无法访问）

// 私有数据完全隐藏，外部无法访问
console.log(privateData.get(user)); // { name: 'John', email: 'john@example.com', password: '...' }
```

#### 2. DOM 元素元数据

WeakMap 可以用于存储 DOM 元素的元数据，当元素被移除时，元数据会自动被垃圾回收：

```js
// 存储 DOM 元素的元数据
const elementMetadata = new WeakMap();

function attachMetadata(element, metadata) {
    elementMetadata.set(element, metadata);
}

function getMetadata(element) {
    return elementMetadata.get(element);
}

const button = document.querySelector("button");
attachMetadata(button, {
    clickCount: 0,
    lastClicked: null
});

button.addEventListener("click", function() {
    const metadata = getMetadata(this);
    metadata.clickCount++;
    metadata.lastClicked = Date.now();
    console.log(`Button clicked ${metadata.clickCount} times`);
});

// 当按钮从 DOM 中移除时，WeakMap 中的元数据会自动被垃圾回收
```

#### 3. 缓存计算结果

WeakMap 可以用于缓存对象的计算结果，当对象被垃圾回收时，缓存也会自动清理：

```js
// 使用 WeakMap 缓存计算结果
const cache = new WeakMap();

function expensiveComputation(obj) {
    // 检查缓存
    if (cache.has(obj)) {
        console.log("Cache hit");
        return cache.get(obj);
    }
    
    // 执行计算
    console.log("Computing...");
    const result = {
        computed: obj.value * 2,
        timestamp: Date.now()
    };
    
    // 存储到缓存
    cache.set(obj, result);
    
    return result;
}

const obj1 = { value: 10 };
const obj2 = { value: 20 };

console.log(expensiveComputation(obj1)); // Computing... { computed: 20, timestamp: ... }
console.log(expensiveComputation(obj1)); // Cache hit { computed: 20, timestamp: ... }
console.log(expensiveComputation(obj2)); // Computing... { computed: 40, timestamp: ... }

// 当 obj1 和 obj2 被垃圾回收时，缓存也会自动清理
```

#### 4. 对象关联数据

WeakMap 可以用于存储对象之间的关联数据，不会影响对象的垃圾回收：

```js
// 存储对象之间的关联
const associations = new WeakMap();

function associateObjects(obj1, obj2, relationship) {
    if (!associations.has(obj1)) {
        associations.set(obj1, new Map());
    }
    associations.get(obj1).set(obj2, relationship);
}

function getAssociation(obj1, obj2) {
    if (!associations.has(obj1)) {
        return null;
    }
    return associations.get(obj1).get(obj2);
}

const user = { id: 1, name: "John" };
const order = { id: 100, total: 99.99 };

associateObjects(user, order, "owner");
console.log(getAssociation(user, order)); // "owner"
```

## WeakSet vs WeakMap

### 对比

| 特性           | WeakSet                    | WeakMap                    |
| :------------- | :------------------------- | :------------------------- |
| **存储内容**   | 对象集合                   | 键值对（键必须是对象）     |
| **值类型**     | 只能是对象                 | 值可以是任何类型           |
| **使用场景**   | 标记对象、防止循环引用     | 私有数据、元数据、缓存     |
| **方法**       | add、has、delete           | set、get、has、delete      |
| **共同点**     | 弱引用、不可迭代、无 size  | 弱引用、不可迭代、无 size  |

### 选择建议

```js
// 使用 WeakSet：只需要标记对象是否存在
const processed = new WeakSet();
if (!processed.has(obj)) {
    processed.add(obj);
}

// 使用 WeakMap：需要存储对象的关联数据
const metadata = new WeakMap();
metadata.set(obj, { lastProcessed: Date.now() });
```

## 与 Set/Map 的对比

### WeakSet vs Set

| 特性           | WeakSet                    | Set                        |
| :------------- | :------------------------- | :------------------------- |
| **值类型**     | 只能是对象                 | 任何类型                   |
| **弱引用**     | 是                         | 否                         |
| **可迭代**     | 否                         | 是                         |
| **size 属性**  | 否                         | 是                         |
| **clear()**    | 否                         | 是                         |
| **内存管理**   | 自动清理                   | 需要手动清理               |

### WeakMap vs Map

| 特性           | WeakMap                    | Map                        |
| :------------- | :------------------------- | :------------------------- |
| **键类型**     | 只能是对象                 | 任何类型                   |
| **弱引用**     | 是                         | 否                         |
| **可迭代**     | 否                         | 是                         |
| **size 属性**  | 否                         | 是                         |
| **clear()**    | 否                         | 是                         |
| **内存管理**   | 自动清理                   | 需要手动清理               |

## 完整示例

```js
// 完整的 WeakSet 和 WeakMap 使用示例
class WeakCollectionExamples {
    static demonstrateWeakSet() {
        console.log("=== WeakSet 示例 ===");
        const processed = new WeakSet();
        
        const obj1 = { id: 1, name: "Object 1" };
        const obj2 = { id: 2, name: "Object 2" };
        
        function processObject(obj) {
            if (processed.has(obj)) {
                console.log(`${obj.name} already processed`);
                return;
            }
            
            console.log(`Processing ${obj.name}`);
            processed.add(obj);
        }
        
        processObject(obj1); // Processing Object 1
        processObject(obj1); // Object 1 already processed
        processObject(obj2); // Processing Object 2
    }
    
    static demonstrateWeakMap() {
        console.log("\n=== WeakMap 示例 ===");
        const privateData = new WeakMap();
        
        class User {
            constructor(name, email) {
                privateData.set(this, {
                    name: name,
                    email: email,
                    createdAt: Date.now()
                });
            }
            
            getName() {
                return privateData.get(this).name;
            }
            
            getEmail() {
                return privateData.get(this).email;
            }
        }
        
        const user1 = new User("John", "john@example.com");
        const user2 = new User("Jane", "jane@example.com");
        
        console.log(user1.getName());  // "John"
        console.log(user2.getEmail()); // "jane@example.com"
        
        // 私有数据完全隐藏
        // console.log(user1.name); // undefined
    }
    
    static demonstrateDOMUsage() {
        console.log("\n=== DOM 元素使用示例 ===");
        const elementData = new WeakMap();
        
        // 模拟 DOM 元素
        const button = { tagName: "BUTTON", id: "myButton" };
        
        elementData.set(button, {
            clickCount: 0,
            lastClicked: null
        });
        
        // 模拟点击事件
        function handleClick(element) {
            const data = elementData.get(element);
            data.clickCount++;
            data.lastClicked = Date.now();
            console.log(`Button clicked ${data.clickCount} times`);
        }
        
        handleClick(button); // Button clicked 1 times
        handleClick(button); // Button clicked 2 times
        
        // 当元素被移除时，WeakMap 中的数据会自动被垃圾回收
    }
}

WeakCollectionExamples.demonstrateWeakSet();
WeakCollectionExamples.demonstrateWeakMap();
WeakCollectionExamples.demonstrateDOMUsage();
```

## 注意事项

### 1. 只能存储对象

WeakSet 和 WeakMap 只能存储对象，不能存储原始值：

```js
const weakSet = new WeakSet();
const weakMap = new WeakMap();

// 错误：不能存储原始值
// weakSet.add(1);              // TypeError
// weakSet.add("hello");        // TypeError
// weakMap.set("key", "value"); // TypeError
// weakMap.set(1, "value");     // TypeError

// 正确：只能存储对象
const obj = {};
weakSet.add(obj);
weakMap.set(obj, "value");
```

### 2. 不可迭代

WeakSet 和 WeakMap 没有迭代器，不能使用 for...of 循环：

```js
const weakSet = new WeakSet([{}, {}]);
const weakMap = new WeakMap([[{}, "value1"], [{}, "value2"]]);

// 错误：不能迭代
// for (const value of weakSet) { }  // TypeError
// for (const [key, value] of weakMap) { } // TypeError

// 错误：没有 size 属性
// console.log(weakSet.size); // undefined
// console.log(weakMap.size); // undefined

// 错误：没有 keys()、values()、entries() 方法
// weakSet.keys();   // TypeError
// weakMap.keys();   // TypeError
```

### 3. 弱引用的影响

弱引用意味着如果对象没有其他引用，会被垃圾回收：

```js
let obj = { id: 1 };
const weakMap = new WeakMap();

weakMap.set(obj, "value");
console.log(weakMap.has(obj)); // true

// 移除对象的引用
obj = null;

// 对象可能已被垃圾回收
// weakMap 中的条目可能已经不存在
// 注意：垃圾回收的时机不确定，不能立即验证
```

### 4. 没有 clear() 方法

WeakSet 和 WeakMap 没有 clear() 方法，不能一次性清空：

```js
const weakSet = new WeakSet([{}, {}, {}]);
const weakMap = new WeakMap([[{}, "value1"], [{}, "value2"]]);

// 错误：没有 clear() 方法
// weakSet.clear(); // TypeError
// weakMap.clear(); // TypeError

// 如果需要清空，需要重新创建
const newWeakSet = new WeakSet();
const newWeakMap = new WeakMap();
```

### 5. 性能考虑

- **内存管理**：WeakSet 和 WeakMap 的主要优势是自动内存管理
- **查找性能**：has() 和 get() 方法的时间复杂度为 O(1)
- **垃圾回收**：弱引用不会阻止垃圾回收，有助于防止内存泄漏

## 常见问题

### 问题 1：为什么 WeakSet 和 WeakMap 不能迭代？

WeakSet 和 WeakMap 使用弱引用，对象的生命周期不确定。如果允许迭代，可能会在迭代过程中遇到已被垃圾回收的对象，导致不一致的行为。

### 问题 2：如何检查 WeakSet 或 WeakMap 是否为空？

WeakSet 和 WeakMap 没有 size 属性，无法直接检查是否为空。如果需要这个功能，应该使用 Set 或 Map。

### 问题 3：WeakSet 和 WeakMap 适合什么场景？

WeakSet 和 WeakMap 适合以下场景：
- 需要存储对象的元数据，但不希望影响对象的垃圾回收
- 需要标记对象，但标记信息是临时的
- 需要实现真正的私有属性
- 需要存储 DOM 元素的关联数据

### 问题 4：如何清空 WeakSet 或 WeakMap？

WeakSet 和 WeakMap 没有 clear() 方法。如果需要清空，需要重新创建实例，或者让所有键对象失去引用，等待垃圾回收。

## 最佳实践

### 1. 使用 WeakMap 实现私有属性

```js
// 好的做法：使用 WeakMap 实现私有属性
const privateData = new WeakMap();

class User {
    constructor(name) {
        privateData.set(this, { name });
    }
    
    getName() {
        return privateData.get(this).name;
    }
}

// 避免：使用 Symbol（仍然可以访问）
const _name = Symbol("name");
class User2 {
    constructor(name) {
        this[_name] = name; // 仍然可以通过 Object.getOwnPropertySymbols 访问
    }
}
```

### 2. 使用 WeakSet 标记对象

```js
// 好的做法：使用 WeakSet 标记对象
const processed = new WeakSet();

function processObject(obj) {
    if (processed.has(obj)) {
        return;
    }
    processed.add(obj);
    // 处理对象
}

// 避免：使用 Set（会阻止垃圾回收）
const processedSet = new Set();
function processObject2(obj) {
    if (processedSet.has(obj)) {
        return;
    }
    processedSet.add(obj); // 会阻止 obj 被垃圾回收
}
```

### 3. 使用 WeakMap 存储 DOM 元数据

```js
// 好的做法：使用 WeakMap 存储 DOM 元数据
const elementData = new WeakMap();

function attachData(element, data) {
    elementData.set(element, data);
}

// 当元素被移除时，元数据会自动被垃圾回收

// 避免：使用 Map（需要手动清理）
const elementDataMap = new Map();
function attachData2(element, data) {
    elementDataMap.set(element, data);
    // 需要手动监听元素移除事件并清理
}
```

### 4. 理解弱引用的含义

```js
// 弱引用意味着对象可能随时被垃圾回收
let obj = { id: 1 };
const weakMap = new WeakMap();

weakMap.set(obj, "value");

// 移除引用后，对象可能被垃圾回收
obj = null;

// 注意：不能立即验证，因为垃圾回收的时机不确定
// 但可以确定的是，如果没有其他引用，对象会被回收
```

## 练习

1. **WeakSet 标记对象**：使用 WeakSet 实现一个对象处理系统，标记已处理的对象，避免重复处理。

2. **WeakMap 私有属性**：使用 WeakMap 实现一个类，将私有数据存储在 WeakMap 中，实现真正的私有属性。

3. **DOM 元素元数据**：使用 WeakMap 存储 DOM 元素的元数据（如点击次数、最后点击时间等），当元素被移除时自动清理。

4. **缓存系统**：使用 WeakMap 实现一个对象计算结果的缓存系统，当对象被垃圾回收时自动清理缓存。

5. **对象关联**：使用 WeakMap 存储对象之间的关联关系，实现对象之间的弱引用关联。

完成以上练习后，继续学习下一章：面向对象与原型。

## 总结

WeakSet 和 WeakMap 提供了弱引用的集合功能。主要要点：

- WeakSet：对象的弱引用集合，用于标记对象
- WeakMap：键值对的弱引用集合，键必须是对象
- 弱引用：不会阻止垃圾回收，有助于防止内存泄漏
- 不可迭代：没有 size 属性，不能遍历
- 使用场景：私有数据、DOM 元数据、对象标记、缓存
- 只能存储对象：不能存储原始值
- 注意弱引用的影响和不可迭代的限制

完成本章学习后，继续学习下一章：面向对象与原型。
