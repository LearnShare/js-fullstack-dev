# 2.9.2 Map 数据结构

## 概述

Map 是 ES6 引入的数据结构，用于存储键值对的集合。Map 对象允许你使用任何类型的值（包括对象和原始值）作为键，这与普通对象（Object）不同，普通对象的键只能是字符串或 Symbol。

Map 数据结构的主要特点：
- **任意类型键**：Map 的键可以是任何类型的值，包括对象、函数、原始值等
- **插入顺序**：Map 按照插入顺序保存键值对
- **可迭代**：Map 是可迭代对象，可以使用 for...of 循环遍历
- **大小属性**：Map 有 `size` 属性，可以直接获取键值对的数量
- **性能优化**：Map 在频繁添加和删除键值对时性能更好

## Map 的特性

### 键的类型

Map 的键可以是任何类型的值，这是 Map 与 Object 的主要区别之一：

```js
const map = new Map();

// 原始类型作为键
map.set(1, "number");
map.set("hello", "string");
map.set(true, "boolean");
map.set(null, "null");
map.set(undefined, "undefined");

// 对象作为键
const obj = { id: 1 };
map.set(obj, "object");

// 函数作为键
function func() {}
map.set(func, "function");

// 数组作为键
map.set([1, 2, 3], "array");

console.log(map.size); // 9
```

### 插入顺序保证

Map 按照插入顺序保存键值对，遍历时会按照插入顺序返回：

```js
const map = new Map();

map.set("first", 1);
map.set("second", 2);
map.set("third", 3);

// 遍历时按照插入顺序
for (const [key, value] of map) {
    console.log(key, value);
}
// 输出：
// first 1
// second 2
// third 3
```

### 与 Object 的对比

| 特性           | Map                          | Object                      |
| :------------- | :--------------------------- | :-------------------------- |
| **键的类型**   | 任何类型                     | 字符串或 Symbol             |
| **大小**       | `size` 属性                  | 需要手动计算                |
| **默认键**     | 无                           | 有原型链（可能包含继承属性） |
| **迭代**       | 可迭代对象                   | 需要 Object.keys() 等       |
| **性能**       | 频繁增删时性能更好           | 适合静态结构                |
| **序列化**     | 不能直接 JSON.stringify      | 可以直接 JSON.stringify     |
| **使用场景**   | 动态键值对、任意类型键       | 静态结构、JSON 数据         |

## 创建 Map

### 使用构造函数创建空 Map

**语法**：`new Map()`

```js
// 创建空 Map
const emptyMap = new Map();
console.log(emptyMap.size); // 0
console.log(emptyMap);      // Map(0) {}
```

### 使用可迭代对象创建 Map

**语法**：`new Map(iterable)`

**参数**：
- `iterable`（可选）：可迭代对象，每个元素应该是 `[key, value]` 形式的数组

**返回值**：新的 Map 对象

```js
// 从数组创建（数组的每个元素是 [key, value] 对）
const mapFromArray = new Map([
    ['name', 'John'],
    ['age', 30],
    ['city', 'New York']
]);
console.log(mapFromArray); // Map(3) { 'name' => 'John', 'age' => 30, 'city' => 'New York' }

// 从另一个 Map 创建
const originalMap = new Map([['a', 1], ['b', 2]]);
const copiedMap = new Map(originalMap);
console.log(copiedMap); // Map(2) { 'a' => 1, 'b' => 2 }

// 从 Set 创建（需要转换）
const set = new Set([['a', 1], ['b', 2]]);
const mapFromSet = new Map(set);
console.log(mapFromSet); // Map(2) { 'a' => 1, 'b' => 2 }
```

### 动态创建和添加元素

```js
// 先创建空 Map，再逐个添加
const map = new Map();

map.set('name', 'John');
map.set('age', 30);
map.set('email', 'john@example.com');

console.log(map); // Map(3) { 'name' => 'John', 'age' => 30, 'email' => 'john@example.com' }
```

## Map 的方法和属性

### size 属性

**说明**：返回 Map 对象中键值对的数量

**语法**：`map.size`

**返回值**：数字，表示 Map 中键值对的数量

```js
const map = new Map([['a', 1], ['b', 2], ['c', 3]]);
console.log(map.size); // 3

// size 是只读属性
// map.size = 10; // 无效，不会改变 size

// 添加元素后 size 自动更新
map.set('d', 4);
console.log(map.size); // 4

// 删除元素后 size 自动更新
map.delete('a');
console.log(map.size); // 3
```

### set() 方法

**语法格式**：`map.set(key, value)`

**参数说明**：

| 参数名   | 类型 | 说明                           | 是否必需 | 默认值 |
|:---------|:-----|:-------------------------------|:---------|:-------|
| `key`    | any  | 要添加的键，可以是任何类型     | 是       | -      |
| `value`  | any  | 要添加的值，可以是任何类型     | 是       | -      |

**返回值**：Map 对象本身（支持链式调用）

```js
const map = new Map();

// 添加键值对
map.set('name', 'John');
map.set('age', 30);

// 更新已存在的键
map.set('age', 31); // 更新 age 的值

// 链式调用
map.set('email', 'john@example.com')
   .set('city', 'New York')
   .set('country', 'USA');

console.log(map.size); // 5

// 使用对象作为键
const userObj = { id: 1 };
map.set(userObj, { name: 'John', age: 30 });

// 使用函数作为键
function getUserKey() {}
map.set(getUserKey, 'function key');

// 使用原始值作为键
map.set(1, 'number key');
map.set(true, 'boolean key');
map.set(null, 'null key');
```

### get() 方法

**语法格式**：`map.get(key)`

**参数说明**：

| 参数名   | 类型 | 说明       | 是否必需 | 默认值 |
|:---------|:-----|:-----------|:---------|:-------|
| `key`    | any  | 要查找的键 | 是       | -      |

**返回值**：如果键存在，返回对应的值；如果键不存在，返回 `undefined`

```js
const map = new Map([
    ['name', 'John'],
    ['age', 30],
    ['email', 'john@example.com']
]);

console.log(map.get('name'));  // "John"
console.log(map.get('age'));   // 30
console.log(map.get('phone')); // undefined（键不存在）

// 对象作为键的查找
const userObj = { id: 1 };
map.set(userObj, { name: 'John' });
console.log(map.get(userObj)); // { name: 'John' }

// 注意：对象引用必须相同
const anotherObj = { id: 1 }; // 内容相同但引用不同
console.log(map.get(anotherObj)); // undefined（不同的对象引用）
```

### has() 方法

**语法格式**：`map.has(key)`

**参数说明**：

| 参数名   | 类型 | 说明       | 是否必需 | 默认值 |
|:---------|:-----|:-----------|:---------|:-------|
| `key`    | any  | 要检查的键 | 是       | -      |

**返回值**：布尔值，如果 Map 中包含该键返回 `true`，否则返回 `false`

```js
const map = new Map([
    ['name', 'John'],
    ['age', 30]
]);

console.log(map.has('name'));  // true
console.log(map.has('age'));   // true
console.log(map.has('email')); // false

// 对象作为键的检查
const userObj = { id: 1 };
map.set(userObj, 'value');
console.log(map.has(userObj)); // true

const anotherObj = { id: 1 };
console.log(map.has(anotherObj)); // false（不同的对象引用）
```

### delete() 方法

**语法格式**：`map.delete(key)`

**参数说明**：

| 参数名   | 类型 | 说明       | 是否必需 | 默认值 |
|:---------|:-----|:-----------|:---------|:-------|
| `key`    | any  | 要删除的键 | 是       | -      |

**返回值**：布尔值，如果删除成功返回 `true`，如果键不存在返回 `false`

```js
const map = new Map([
    ['name', 'John'],
    ['age', 30],
    ['email', 'john@example.com']
]);

console.log(map.delete('age'));  // true（删除成功）
console.log(map);                // Map(2) { 'name' => 'John', 'email' => 'john@example.com' }

console.log(map.delete('phone')); // false（键不存在）
console.log(map.size);            // 2（未改变）
```

### clear() 方法

**语法格式**：`map.clear()`

**参数说明**：无参数

**返回值**：`undefined`

```js
const map = new Map([
    ['name', 'John'],
    ['age', 30],
    ['email', 'john@example.com']
]);

console.log(map.size); // 3

map.clear();

console.log(map.size); // 0
console.log(map);      // Map(0) {}
```

## Map 的遍历

### for...of 循环

```js
const map = new Map([
    ['name', 'John'],
    ['age', 30],
    ['email', 'john@example.com']
]);

// 遍历键值对
for (const [key, value] of map) {
    console.log(key, value);
}
// 输出：
// name John
// age 30
// email john@example.com

// 只遍历键
for (const key of map.keys()) {
    console.log(key);
}

// 只遍历值
for (const value of map.values()) {
    console.log(value);
}
```

### forEach() 方法

**语法格式**：`map.forEach(callbackFn[, thisArg])`

**参数说明**：

| 参数名        | 类型     | 说明                           | 是否必需 | 默认值 |
|:--------------|:---------|:-------------------------------|:---------|:-------|
| `callbackFn`  | Function | 为每个键值对执行的函数，接收三个参数：<br>- `value`：当前元素的值<br>- `key`：当前元素的键<br>- `map`：正在遍历的 Map 对象 | 是       | -      |
| `thisArg`     | any      | 执行 `callbackFn` 时使用的 `this` 值 | 否       | -      |

**返回值**：`undefined`

```js
const map = new Map([
    ['name', 'John'],
    ['age', 30],
    ['email', 'john@example.com']
]);

// 基本用法
map.forEach((value, key) => {
    console.log(key, value);
});

// 使用所有参数
map.forEach((value, key, map) => {
    console.log(`Key: ${key}, Value: ${value}, Map size: ${map.size}`);
});

// 使用 thisArg
const obj = {
    prefix: "User:",
    process(key, value) {
        console.log(`${this.prefix} ${key} = ${value}`);
    }
};

map.forEach(obj.process, obj);
```

### keys() 方法

**说明**：返回一个新的迭代器对象，包含 Map 对象中的所有键

**语法**：`map.keys()`

**返回值**：新的 Map 迭代器对象

```js
const map = new Map([
    ['name', 'John'],
    ['age', 30],
    ['email', 'john@example.com']
]);

const keysIterator = map.keys();

console.log(keysIterator.next().value); // "name"
console.log(keysIterator.next().value); // "age"
console.log(keysIterator.next().value); // "email"
console.log(keysIterator.next().done);  // true

// 使用 for...of 遍历迭代器
for (const key of map.keys()) {
    console.log(key);
}
```

### values() 方法

**说明**：返回一个新的迭代器对象，包含 Map 对象中的所有值

**语法**：`map.values()`

**返回值**：新的 Map 迭代器对象

```js
const map = new Map([
    ['name', 'John'],
    ['age', 30],
    ['email', 'john@example.com']
]);

const valuesIterator = map.values();

console.log(valuesIterator.next().value); // "John"
console.log(valuesIterator.next().value); // 30
console.log(valuesIterator.next().value); // "john@example.com"

// 使用 for...of 遍历
for (const value of map.values()) {
    console.log(value);
}
```

### entries() 方法

**说明**：返回一个新的迭代器对象，包含 `[key, value]` 形式的数组

**语法**：`map.entries()`

**返回值**：新的 Map 迭代器对象

```js
const map = new Map([
    ['name', 'John'],
    ['age', 30],
    ['email', 'john@example.com']
]);

const entriesIterator = map.entries();

console.log(entriesIterator.next().value); // ['name', 'John']
console.log(entriesIterator.next().value); // ['age', 30]
console.log(entriesIterator.next().value); // ['email', 'john@example.com']

// 使用 for...of 遍历
for (const [key, value] of map.entries()) {
    console.log(key, value);
}

// entries() 是默认迭代器，可以直接遍历 Map
for (const [key, value] of map) {
    console.log(key, value);
}
```

## Map 与 Object 的转换

### 从 Object 创建 Map

```js
// 从普通对象创建 Map
const obj = {
    name: 'John',
    age: 30,
    email: 'john@example.com'
};

const map = new Map(Object.entries(obj));
console.log(map); // Map(3) { 'name' => 'John', 'age' => 30, 'email' => 'john@example.com' }
```

### 从 Map 转换为 Object

```js
const map = new Map([
    ['name', 'John'],
    ['age', 30],
    ['email', 'john@example.com']
]);

// 使用 Object.fromEntries()
const obj = Object.fromEntries(map);
console.log(obj); // { name: 'John', age: 30, email: 'john@example.com' }

// 手动转换
const obj2 = {};
for (const [key, value] of map) {
    obj2[key] = value;
}
console.log(obj2); // { name: 'John', age: 30, email: 'john@example.com' }
```

### 注意事项

```js
// 注意：对象作为键时，转换会丢失
const map = new Map();
const objKey = { id: 1 };
map.set(objKey, 'value');

const obj = Object.fromEntries(map);
// objKey 会被转换为字符串 "[object Object]"
console.log(obj); // { '[object Object]': 'value' }
```

## Map 的实际应用场景

### 1. 使用对象作为键

```js
// 存储对象相关的元数据
const userMetadata = new Map();

const user1 = { id: 1, name: 'John' };
const user2 = { id: 2, name: 'Jane' };

userMetadata.set(user1, { lastLogin: '2024-01-01', role: 'admin' });
userMetadata.set(user2, { lastLogin: '2024-01-02', role: 'user' });

console.log(userMetadata.get(user1)); // { lastLogin: '2024-01-01', role: 'admin' }
```

### 2. 缓存系统

```js
// 使用 Map 实现缓存
class Cache {
    constructor() {
        this.cache = new Map();
    }
    
    set(key, value, ttl = 0) {
        this.cache.set(key, {
            value,
            expires: ttl > 0 ? Date.now() + ttl : null
        });
    }
    
    get(key) {
        const item = this.cache.get(key);
        if (!item) return null;
        
        if (item.expires && Date.now() > item.expires) {
            this.cache.delete(key);
            return null;
        }
        
        return item.value;
    }
    
    clear() {
        this.cache.clear();
    }
}

const cache = new Cache();
cache.set('user:1', { name: 'John' }, 60000); // 60秒过期
console.log(cache.get('user:1')); // { name: 'John' }
```

### 3. 计数器

```js
// 使用 Map 实现计数器
function countOccurrences(arr) {
    const counts = new Map();
    
    for (const item of arr) {
        counts.set(item, (counts.get(item) || 0) + 1);
    }
    
    return counts;
}

const fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple'];
const counts = countOccurrences(fruits);
console.log(counts.get('apple'));  // 3
console.log(counts.get('banana')); // 2
console.log(counts.get('orange')); // 1
```

### 4. 数据分组

```js
// 使用 Map 进行数据分组
function groupBy(array, keyFn) {
    const groups = new Map();
    
    for (const item of array) {
        const key = keyFn(item);
        if (!groups.has(key)) {
            groups.set(key, []);
        }
        groups.get(key).push(item);
    }
    
    return groups;
}

const users = [
    { id: 1, name: 'John', role: 'admin' },
    { id: 2, name: 'Jane', role: 'user' },
    { id: 3, name: 'Bob', role: 'admin' },
    { id: 4, name: 'Alice', role: 'user' }
];

const grouped = groupBy(users, user => user.role);
console.log(grouped.get('admin')); // [{ id: 1, name: 'John', role: 'admin' }, { id: 3, name: 'Bob', role: 'admin' }]
console.log(grouped.get('user'));  // [{ id: 2, name: 'Jane', role: 'user' }, { id: 4, name: 'Alice', role: 'user' }]
```

### 5. 关联数据存储

```js
// 存储关联数据
const userSessions = new Map();

function createSession(userId, sessionData) {
    userSessions.set(userId, {
        ...sessionData,
        createdAt: Date.now()
    });
}

function getSession(userId) {
    return userSessions.get(userId);
}

function removeSession(userId) {
    userSessions.delete(userId);
}

createSession(1, { token: 'abc123', ip: '192.168.1.1' });
console.log(getSession(1)); // { token: 'abc123', ip: '192.168.1.1', createdAt: ... }
```

## 完整示例

```js
// 完整的 Map 使用示例
class MapExamples {
    static demonstrate() {
        console.log("=== 创建 Map ===");
        const map1 = new Map([
            ['name', 'John'],
            ['age', 30],
            ['email', 'john@example.com']
        ]);
        const map2 = new Map();
        map2.set('city', 'New York');
        map2.set('country', 'USA');
        
        console.log("Map 1:", map1);
        console.log("Map 2:", map2);
        console.log("Map 1 size:", map1.size);
        
        console.log("\n=== 访问和修改 ===");
        console.log("map1.get('name'):", map1.get('name'));
        console.log("map1.has('age'):", map1.has('age'));
        
        map1.set('age', 31);
        console.log("更新 age 后:", map1.get('age'));
        
        console.log("\n=== 遍历 Map ===");
        console.log("使用 for...of:");
        for (const [key, value] of map1) {
            console.log(`${key}: ${value}`);
        }
        
        console.log("\n使用 forEach:");
        map1.forEach((value, key) => {
            console.log(`${key}: ${value}`);
        });
        
        console.log("\n=== 对象作为键 ===");
        const userObj = { id: 1, name: 'John' };
        const metadata = new Map();
        metadata.set(userObj, { lastLogin: '2024-01-01', role: 'admin' });
        console.log("metadata.get(userObj):", metadata.get(userObj));
        
        console.log("\n=== 集合运算 ===");
        const mapA = new Map([['a', 1], ['b', 2], ['c', 3]]);
        const mapB = new Map([['b', 20], ['c', 30], ['d', 4]]);
        
        // 合并 Map
        const merged = new Map([...mapA, ...mapB]);
        console.log("合并后的 Map:", [...merged]);
        
        console.log("\n=== 转换为对象 ===");
        const obj = Object.fromEntries(map1);
        console.log("转换为对象:", obj);
    }
}

MapExamples.demonstrate();
```

## 注意事项

### 1. 对象引用的唯一性

Map 使用引用比较对象键，内容相同的不同对象被视为不同的键：

```js
const map = new Map();
const obj1 = { id: 1, name: "John" };
const obj2 = { id: 1, name: "John" };

map.set(obj1, "value1");
map.set(obj2, "value2");

console.log(map.size); // 2（两个不同的对象）
console.log(map.get(obj1)); // "value1"
console.log(map.get(obj2)); // "value2"
```

### 2. NaN 的特殊处理

NaN 在 Map 中被视为相等：

```js
const map = new Map();
map.set(NaN, "not a number");
console.log(map.has(NaN)); // true
console.log(map.get(NaN)); // "not a number"

map.set(NaN, "updated");
console.log(map.size); // 1（NaN 被视为相等）
```

### 3. +0 和 -0 的处理

+0 和 -0 在 Map 中被视为相等：

```js
const map = new Map();
map.set(+0, "positive zero");
map.set(-0, "negative zero");
console.log(map.size); // 1（+0 和 -0 被视为相等）
```

### 4. 性能考虑

- **查找性能**：Map 的 `get()` 和 `has()` 方法平均时间复杂度为 O(1)
- **插入性能**：Map 的 `set()` 方法平均时间复杂度为 O(1)
- **删除性能**：Map 的 `delete()` 方法平均时间复杂度为 O(1)
- **内存使用**：Map 使用哈希表实现，内存使用略高于对象

### 5. 序列化限制

Map 不能直接使用 `JSON.stringify()` 序列化：

```js
const map = new Map([['name', 'John'], ['age', 30]]);

// JSON.stringify(map) 返回 "{}"（空对象）

// 需要先转换为数组
const serialized = JSON.stringify([...map]);
console.log(serialized); // '[["name","John"],["age",30]]'

// 反序列化
const deserialized = new Map(JSON.parse(serialized));
console.log(deserialized); // Map(2) { 'name' => 'John', 'age' => 30 }
```

## 常见问题

### 问题 1：如何检查 Map 是否为空？

```js
const map = new Map();

// 方法 1：使用 size 属性
if (map.size === 0) {
    console.log("Map is empty");
}

// 方法 2：转换为布尔值
if (!map.size) {
    console.log("Map is empty");
}
```

### 问题 2：如何获取 Map 中的第一个键值对？

```js
const map = new Map([['a', 1], ['b', 2], ['c', 3]]);

// 方法 1：使用迭代器
const firstEntry = map.entries().next().value;
console.log(firstEntry); // ['a', 1]

// 方法 2：转换为数组
const firstEntry2 = [...map][0];
console.log(firstEntry2); // ['a', 1]
```

### 问题 3：如何合并多个 Map？

```js
const map1 = new Map([['a', 1], ['b', 2]]);
const map2 = new Map([['c', 3], ['d', 4]]);
const map3 = new Map([['e', 5], ['f', 6]]);

// 方法 1：使用展开运算符
const merged = new Map([...map1, ...map2, ...map3]);
console.log([...merged]); // [['a', 1], ['b', 2], ['c', 3], ['d', 4], ['e', 5], ['f', 6]]

// 方法 2：逐个添加
const merged2 = new Map(map1);
map2.forEach((value, key) => merged2.set(key, value));
map3.forEach((value, key) => merged2.set(key, value));
```

### 问题 4：如何对 Map 进行排序？

```js
const map = new Map([
    ['c', 3],
    ['a', 1],
    ['b', 2],
    ['d', 4]
]);

// 按键排序
const sortedByKey = new Map([...map].sort((a, b) => a[0].localeCompare(b[0])));
console.log([...sortedByKey]); // [['a', 1], ['b', 2], ['c', 3], ['d', 4]]

// 按值排序
const sortedByValue = new Map([...map].sort((a, b) => a[1] - b[1]));
console.log([...sortedByValue]); // [['a', 1], ['b', 2], ['c', 3], ['d', 4]]
```

### 问题 5：如何过滤 Map？

```js
const map = new Map([
    ['a', 1],
    ['b', 2],
    ['c', 3],
    ['d', 4]
]);

// 过滤值大于 2 的项
const filtered = new Map([...map].filter(([key, value]) => value > 2));
console.log([...filtered]); // [['c', 3], ['d', 4]]
```

## 最佳实践

### 1. 使用 Map 存储动态键值对

```js
// 好的做法：使用 Map 存储动态键值对
const dynamicData = new Map();

function addData(key, value) {
    dynamicData.set(key, value);
}

// 避免：使用 Object 存储动态键（可能遇到原型链问题）
const dynamicDataObj = {};
function addDataObj(key, value) {
    dynamicDataObj[key] = value; // 可能覆盖原型属性
}
```

### 2. 使用 Map 进行快速查找

```js
// 好的做法：使用 Map 进行快速查找
const lookup = new Map([
    [1, 'one'],
    [2, 'two'],
    [3, 'three']
]);

if (lookup.has(userId)) {
    const value = lookup.get(userId);
}

// 避免：使用数组进行查找（性能较差）
const lookupArray = [[1, 'one'], [2, 'two'], [3, 'three']];
const found = lookupArray.find(([key]) => key === userId);
```

### 3. 使用对象作为键

```js
// 好的做法：使用 Map 存储对象相关的数据
const userMetadata = new Map();
const user = { id: 1 };
userMetadata.set(user, { lastLogin: Date.now() });

// 避免：使用 WeakMap（如果需要遍历）
// WeakMap 不能遍历，如果需要遍历应使用 Map
```

### 4. 选择合适的数据结构

```js
// 使用 Map 的场景：
// - 需要任意类型键
// - 频繁添加和删除
// - 需要保持插入顺序
// - 需要 size 属性

// 使用 Object 的场景：
// - 静态结构
// - 需要 JSON 序列化
// - 需要原型链
// - 简单的键值对存储
```

## 练习

1. **创建 Map**：创建一个 Map 存储用户信息（name、age、email），并添加、获取、删除操作。

2. **对象作为键**：使用对象作为 Map 的键，存储对象相关的元数据。

3. **计数器实现**：使用 Map 实现一个计数器，统计数组中每个元素出现的次数。

4. **数据分组**：使用 Map 实现数据分组功能，将数组按某个属性分组。

5. **缓存系统**：使用 Map 实现一个简单的缓存系统，支持设置、获取和过期时间。

6. **Map 与 Object 转换**：实现 Map 和 Object 之间的相互转换函数。

完成以上练习后，继续学习下一节，了解 WeakSet 和 WeakMap。

## 总结

Map 提供了强大的键值对存储能力。主要要点：

- Map 存储键值对，键可以是任何类型
- 提供 set、get、has、delete、clear 等方法
- 支持多种遍历方式
- 与 Object 相比，支持任意类型键，性能更好
- 适合动态键值对、缓存、计数器等场景
- 注意对象引用的唯一性和序列化限制

继续学习下一节，了解 WeakSet 和 WeakMap。
