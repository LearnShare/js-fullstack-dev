# 2.6.5 高阶函数

## 概述

高阶函数是接受函数作为参数或返回函数的函数。高阶函数是函数式编程的基础。本节介绍高阶函数的概念和应用。

## 函数作为参数

### 回调函数

```js
function processArray(arr, callback) {
    const result = [];
    for (let item of arr) {
        result.push(callback(item));
    }
    return result;
}

const numbers = [1, 2, 3, 4, 5];
const doubled = processArray(numbers, x => x * 2);
console.log(doubled); // [2, 4, 6, 8, 10]
```

### 数组方法

```js
const numbers = [1, 2, 3, 4, 5];

// map：转换每个元素
const doubled = numbers.map(x => x * 2);

// filter：过滤元素
const evens = numbers.filter(x => x % 2 === 0);

// reduce：归约数组
const sum = numbers.reduce((acc, x) => acc + x, 0);

// forEach：遍历数组
numbers.forEach(x => console.log(x));
```

## 函数作为返回值

### 函数工厂

```js
function createMultiplier(factor) {
    return function(x) {
        return x * factor;
    };
}

const double = createMultiplier(2);
const triple = createMultiplier(3);

console.log(double(5));  // 10
console.log(triple(5));  // 15
```

### 函数组合

```js
function compose(f, g) {
    return function(x) {
        return f(g(x));
    };
}

const addOne = x => x + 1;
const multiplyTwo = x => x * 2;

const addThenMultiply = compose(multiplyTwo, addOne);
console.log(addThenMultiply(5)); // 12
```

## 实际应用

### 1. 事件处理

```js
function createEventHandler(eventType) {
    return function(callback) {
        document.addEventListener(eventType, callback);
    };
}

const onClick = createEventHandler("click");
onClick(() => console.log("Clicked"));
```

### 2. 数据验证

```js
function createValidator(rules) {
    return function(data) {
        for (let rule of rules) {
            if (!rule(data)) {
                return false;
            }
        }
        return true;
    };
}

const validateUser = createValidator([
    data => data.name && data.name.length > 0,
    data => data.email && data.email.includes("@")
]);

console.log(validateUser({ name: "John", email: "john@example.com" })); // true
```

### 3. 缓存函数

```js
function memoize(fn) {
    const cache = {};
    return function(...args) {
        const key = JSON.stringify(args);
        if (cache[key]) {
            return cache[key];
        }
        const result = fn(...args);
        cache[key] = result;
        return result;
    };
}

const expensiveFunction = memoize(function(n) {
    // 昂贵的计算
    return n * n;
});
```

## 函数式编程

### 纯函数

```js
// 纯函数：相同输入总是产生相同输出，无副作用
function add(a, b) {
    return a + b;
}

// 非纯函数：有副作用
let counter = 0;
function increment() {
    counter++;
    return counter;
}
```

### 不可变性

```js
// 函数式编程：不修改原数据
function addItem(arr, item) {
    return [...arr, item]; // 返回新数组
}

const numbers = [1, 2, 3];
const newNumbers = addItem(numbers, 4);
console.log(numbers);     // [1, 2, 3]（未改变）
console.log(newNumbers);   // [1, 2, 3, 4]
```

## 最佳实践

### 1. 使用高阶函数简化代码

```js
// 好的做法：使用高阶函数
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(x => x * 2);

// 避免：手动循环
const doubled2 = [];
for (let i = 0; i < numbers.length; i++) {
    doubled2.push(numbers[i] * 2);
}
```

### 2. 组合小函数

```js
// 组合小函数创建复杂功能
const process = numbers
    .filter(x => x > 0)
    .map(x => x * 2)
    .reduce((acc, x) => acc + x, 0);
```

## 总结

高阶函数是函数式编程的基础。主要要点：

- 函数可以作为参数传递
- 函数可以作为返回值
## 练习

1. **函数作为参数**：编写一个高阶函数，接受一个函数作为参数，并在特定条件下调用它。

2. **函数作为返回值**：编写一个函数，返回另一个函数，实现函数工厂模式。

3. **数组高阶函数**：使用 `map`、`filter`、`reduce` 等高阶函数处理数组数据。

4. **函数组合**：编写函数组合工具，将多个函数组合成一个新函数。

5. **纯函数**：编写纯函数，确保函数没有副作用，相同输入总是产生相同输出。

完成以上练习后，继续学习下一章：对象与数组。

## 总结

高阶函数是函数式编程的核心。主要要点：

- 高阶函数：接受函数作为参数或返回函数
- 函数作为值：函数是一等公民
- 常用高阶函数：map、filter、reduce、forEach
- 使用高阶函数简化代码
- 函数式编程：纯函数、不可变性
- 组合小函数创建复杂功能

完成本章学习后，继续学习下一章：对象与数组。
