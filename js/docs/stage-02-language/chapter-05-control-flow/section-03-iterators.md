# 2.5.3 迭代器循环（for...of、for...in）

## 概述

迭代器循环提供了更简洁的方式来遍历数据结构。JavaScript 提供了 for...of 和 for...in 循环。本节介绍它们的区别和使用场景。

## for...of 循环

### 基本语法

```js
for (variable of iterable) {
    // 代码块
}
```

### 遍历数组

```js
let arr = [1, 2, 3, 4, 5];

for (let value of arr) {
    console.log(value); // 1, 2, 3, 4, 5
}
```

### 遍历字符串

```js
let str = "Hello";

for (let char of str) {
    console.log(char); // H, e, l, l, o
}
```

### 遍历 Set

```js
let set = new Set([1, 2, 3]);

for (let value of set) {
    console.log(value); // 1, 2, 3
}
```

### 遍历 Map

```js
let map = new Map([
    ['a', 1],
    ['b', 2],
    ['c', 3]
]);

for (let [key, value] of map) {
    console.log(key, value); // a 1, b 2, c 3
}
```

### 获取索引

```js
let arr = [1, 2, 3];

// 使用 entries() 获取索引
for (let [index, value] of arr.entries()) {
    console.log(index, value); // 0 1, 1 2, 2 3
}
```

## for...in 循环

### 基本语法

```js
for (variable in object) {
    // 代码块
}
```

### 遍历对象属性

```js
let obj = {
    name: "John",
    age: 30,
    city: "New York"
};

for (let key in obj) {
    console.log(key, obj[key]);
    // name John
    // age 30
    // city New York
}
```

### 遍历数组索引

```js
let arr = [1, 2, 3];

for (let index in arr) {
    console.log(index, arr[index]);
    // 0 1
    // 1 2
    // 2 3
}
```

### 继承的属性

```js
// for...in 会遍历继承的属性
let obj = Object.create({ inherited: "value" });
obj.own = "own";

for (let key in obj) {
    console.log(key); // inherited, own
}

// 只遍历自有属性
for (let key in obj) {
    if (obj.hasOwnProperty(key)) {
        console.log(key); // own
    }
}
```

## 区别和使用场景

### for...of vs for...in

```js
let arr = [1, 2, 3];

// for...of：遍历值
for (let value of arr) {
    console.log(value); // 1, 2, 3
}

// for...in：遍历索引/键
for (let index in arr) {
    console.log(index); // 0, 1, 2
}
```

### 使用场景

```js
// for...of：遍历可迭代对象（数组、字符串、Set、Map）
for (let value of array) { }
for (let char of string) { }
for (let item of set) { }
for (let [key, value] of map) { }

// for...in：遍历对象属性
for (let key in object) { }
```

## 最佳实践

### 1. 数组使用 for...of

```js
// 好的做法：使用 for...of
let arr = [1, 2, 3];
for (let value of arr) {
    console.log(value);
}

// 避免：使用 for...in（可能遍历到非数字属性）
for (let index in arr) {
    console.log(arr[index]);
}
```

### 2. 对象使用 for...in

```js
// 好的做法：使用 for...in
let obj = { a: 1, b: 2, c: 3 };
for (let key in obj) {
    if (obj.hasOwnProperty(key)) {
        console.log(key, obj[key]);
    }
}

// 或使用 Object.keys()
for (let key of Object.keys(obj)) {
    console.log(key, obj[key]);
}
```

### 3. 需要索引时使用 entries()

```js
// 使用 entries() 获取索引和值
let arr = [1, 2, 3];
for (let [index, value] of arr.entries()) {
    console.log(index, value);
}
```

## 练习

1. **for...of 遍历数组**：使用 `for...of` 遍历数组，计算数组元素的总和。

2. **for...of 遍历字符串**：使用 `for...of` 遍历字符串，统计每个字符出现的次数。

3. **for...of 遍历 Map**：使用 `for...of` 遍历 Map，打印所有键值对。

4. **for...in 遍历对象**：使用 `for...in` 遍历对象，只遍历自有属性（使用 `hasOwnProperty`）。

5. **获取索引和值**：使用 `entries()` 方法获取数组的索引和值，遍历并打印。

完成以上练习后，继续学习下一节，了解跳转语句。

## 总结

迭代器循环提供了简洁的遍历方式。主要要点：

- for...of：遍历可迭代对象的值
- for...in：遍历对象的属性
- 数组使用 for...of
- 对象使用 for...in（注意继承属性）
- 需要索引时使用 entries()

继续学习下一节，了解跳转语句。
