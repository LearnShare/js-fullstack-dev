# 2.5.2 循环结构（for、while、do...while）

## 概述

循环结构用于重复执行代码块。JavaScript 提供了 for、while 和 do...while 循环。本节介绍这些循环的使用方法。

## for 循环

### 基本语法

```js
for (initialization; condition; increment) {
    // 代码块
}
```

### 示例

```js
for (let i = 0; i < 5; i++) {
    console.log(i); // 0, 1, 2, 3, 4
}
```

### 循环步骤

1. 执行初始化（只执行一次）
2. 检查条件
3. 如果条件为真，执行代码块
4. 执行增量
5. 回到步骤 2

### 变体

```js
// 省略初始化
let i = 0;
for (; i < 5; i++) {
    console.log(i);
}

// 省略增量
for (let i = 0; i < 5;) {
    console.log(i);
    i++;
}

// 无限循环
for (;;) {
    // 需要 break 退出
    break;
}
```

## while 循环

### 基本语法

```js
while (condition) {
    // 代码块
}
```

### 示例

```js
let i = 0;
while (i < 5) {
    console.log(i); // 0, 1, 2, 3, 4
    i++;
}
```

### 条件检查

```js
// while 先检查条件，再执行代码
let count = 0;
while (count < 5) {
    console.log(count);
    count++;
}
```

## do...while 循环

### 基本语法

```js
do {
    // 代码块
} while (condition);
```

### 示例

```js
let i = 0;
do {
    console.log(i); // 0, 1, 2, 3, 4
    i++;
} while (i < 5);
```

### 与 while 的区别

```js
// do...while 至少执行一次
let count = 10;
do {
    console.log(count); // 10（会执行一次）
    count++;
} while (count < 5);

// while 可能不执行
let count2 = 10;
while (count2 < 5) {
    console.log(count2); // 不会执行
    count2++;
}
```

## 嵌套循环

### 示例

```js
// 嵌套 for 循环
for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
        console.log(`i=${i}, j=${j}`);
    }
}
```

## 循环控制

### break 语句

```js
// break 退出循环
for (let i = 0; i < 10; i++) {
    if (i === 5) {
        break; // 退出循环
    }
    console.log(i); // 0, 1, 2, 3, 4
}
```

### continue 语句

```js
// continue 跳过当前迭代
for (let i = 0; i < 10; i++) {
    if (i % 2 === 0) {
        continue; // 跳过偶数
    }
    console.log(i); // 1, 3, 5, 7, 9
}
```

## 常见应用

### 遍历数组

```js
let arr = [1, 2, 3, 4, 5];

// for 循环
for (let i = 0; i < arr.length; i++) {
    console.log(arr[i]);
}

// while 循环
let i = 0;
while (i < arr.length) {
    console.log(arr[i]);
    i++;
}
```

### 倒序循环

```js
let arr = [1, 2, 3, 4, 5];

for (let i = arr.length - 1; i >= 0; i--) {
    console.log(arr[i]); // 5, 4, 3, 2, 1
}
```

## 最佳实践

### 1. 选择合适的循环

```js
// 已知次数：使用 for
for (let i = 0; i < 10; i++) { }

// 未知次数：使用 while
while (condition) { }

// 至少执行一次：使用 do...while
do { } while (condition);
```

### 2. 避免无限循环

```js
// 确保循环条件会改变
let i = 0;
while (i < 10) {
    console.log(i);
    i++; // 必须改变条件
}
```

### 3. 使用 break 和 continue

```js
// 使用 break 提前退出
for (let i = 0; i < 100; i++) {
    if (found) {
        break; // 找到后退出
    }
}

// 使用 continue 跳过
for (let i = 0; i < 10; i++) {
    if (shouldSkip(i)) {
        continue; // 跳过当前迭代
    }
    process(i);
}
```

## 练习

1. **for 循环**：使用 for 循环计算 1 到 100 的和。

2. **while 循环**：使用 while 循环实现一个猜数字游戏，直到猜对为止。

3. **do...while 循环**：使用 do...while 循环实现一个菜单系统，至少显示一次菜单。

4. **嵌套循环**：使用嵌套循环打印九九乘法表。

5. **break 和 continue**：在循环中使用 break 和 continue 控制流程，查找数组中的特定值。

完成以上练习后，继续学习下一节，了解迭代器循环。

## 总结

循环结构是重复执行代码的基础。主要要点：

- for：已知次数的循环
- while：条件循环
- do...while：至少执行一次的循环
- break：退出循环
- continue：跳过当前迭代
- 选择合适的循环类型
- 避免无限循环

继续学习下一节，了解迭代器循环。
