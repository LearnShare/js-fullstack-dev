# 2.5.4 跳转语句（break、continue、return）

## 概述

跳转语句用于控制程序的执行流程。JavaScript 提供了 break、continue 和 return 语句。本节介绍这些语句的使用方法。

## break 语句

### 在循环中使用

```js
// break 退出循环
for (let i = 0; i < 10; i++) {
    if (i === 5) {
        break; // 退出循环
    }
    console.log(i); // 0, 1, 2, 3, 4
}
```

### 在 switch 中使用

```js
let day = 1;

switch (day) {
    case 1:
        console.log("星期一");
        break; // 退出 switch
    case 2:
        console.log("星期二");
        break;
}
```

### 标签 break

```js
// 使用标签退出外层循环
outer: for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
        if (i === 1 && j === 1) {
            break outer; // 退出外层循环
        }
        console.log(i, j);
    }
}
```

## continue 语句

### 在循环中使用

```js
// continue 跳过当前迭代
for (let i = 0; i < 10; i++) {
    if (i % 2 === 0) {
        continue; // 跳过偶数
    }
    console.log(i); // 1, 3, 5, 7, 9
}
```

### 标签 continue

```js
// 使用标签跳过外层循环的当前迭代
outer: for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
        if (j === 1) {
            continue outer; // 跳过外层循环的当前迭代
        }
        console.log(i, j);
    }
}
```

## return 语句

### 在函数中使用

```js
// return 返回值并退出函数
function add(a, b) {
    return a + b; // 返回值并退出
}

let result = add(1, 2); // 3
```

### 提前返回

```js
// 使用 return 提前退出
function processUser(user) {
    if (!user) {
        return; // 提前退出
    }
    if (!user.name) {
        return; // 提前退出
    }
    
    // 处理用户
    console.log(user.name);
}
```

### 返回值

```js
// 返回单个值
function getValue() {
    return 10;
}

// 返回对象
function getUser() {
    return {
        name: "John",
        age: 30
    };
}

// 返回数组
function getNumbers() {
    return [1, 2, 3];
}
```

## 最佳实践

### 1. 使用 break 提前退出

```js
// 好的做法：使用 break 提前退出
for (let i = 0; i < 100; i++) {
    if (found) {
        break; // 找到后退出
    }
    search(i);
}
```

### 2. 使用 continue 跳过

```js
// 好的做法：使用 continue 跳过
for (let i = 0; i < 10; i++) {
    if (shouldSkip(i)) {
        continue; // 跳过当前迭代
    }
    process(i);
}
```

### 3. 使用 return 早期返回

```js
// 好的做法：使用 return 早期返回
function process(data) {
    if (!data) return;
    if (!data.valid) return;
    
    // 处理数据
}
```

## 练习

1. **break 语句**：在循环中使用 break 语句，找到第一个满足条件的元素后退出循环。

2. **continue 语句**：在循环中使用 continue 语句，跳过不满足条件的元素。

3. **标签 break**：使用标签 break 退出外层循环，处理嵌套循环的情况。

4. **return 语句**：编写函数使用 return 语句实现早期返回，减少嵌套。

5. **综合应用**：结合使用 break、continue 和 return，实现复杂的控制流程。

完成以上练习后，继续学习下一章：函数。

## 总结

跳转语句控制程序执行流程。主要要点：

- break：退出循环或 switch
- continue：跳过当前迭代
- return：返回值并退出函数
- 使用标签控制外层循环
- 使用早期返回减少嵌套

完成本章学习后，继续学习下一章：函数。
