# 7.1.1 算法优化

## 概述

算法优化是提升 JavaScript 性能的基础。本节介绍算法的时间复杂度、空间复杂度，以及常见算法的优化方法和技巧。

## 时间复杂度

### 基本概念

时间复杂度描述算法执行时间随输入规模增长的趋势：

```js
// O(1) - 常数时间复杂度
function getFirst(arr) {
    return arr[0]; // 无论数组多大，都是常数时间
}

// O(n) - 线性时间复杂度
function findItem(arr, item) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === item) return i;
    }
    return -1;
}

// O(n²) - 平方时间复杂度
function bubbleSort(arr) {
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr.length - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
            }
        }
    }
}
```

### 常见时间复杂度

| 复杂度     | 说明           | 示例                     |
|:-----------|:---------------|:-------------------------|
| O(1)       | 常数时间       | 数组索引访问             |
| O(log n)   | 对数时间       | 二分查找                 |
| O(n)       | 线性时间       | 遍历数组                 |
| O(n log n) | 线性对数时间   | 快速排序、归并排序        |
| O(n²)      | 平方时间       | 嵌套循环、冒泡排序        |
| O(2ⁿ)      | 指数时间       | 递归斐波那契（未优化）    |

## 空间复杂度

### 基本概念

空间复杂度描述算法使用的内存空间随输入规模增长的趋势：

```js
// O(1) - 常数空间复杂度
function sum(arr) {
    let total = 0;
    for (let i = 0; i < arr.length; i++) {
        total += arr[i];
    }
    return total; // 只使用固定数量的变量
}

// O(n) - 线性空间复杂度
function copyArray(arr) {
    const newArr = [];
    for (let i = 0; i < arr.length; i++) {
        newArr.push(arr[i]);
    }
    return newArr; // 创建了与输入相同大小的新数组
}
```

## 数组操作优化

### 避免不必要的循环

```js
// 错误：多次遍历
function badExample(arr) {
    const doubled = arr.map(x => x * 2);
    const filtered = doubled.filter(x => x > 10);
    const sum = filtered.reduce((a, b) => a + b, 0);
    return sum;
}

// 正确：一次遍历
function goodExample(arr) {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
        const doubled = arr[i] * 2;
        if (doubled > 10) {
            sum += doubled;
        }
    }
    return sum;
}
```

### 使用 Set 优化查找

```js
// 错误：O(n) 查找
function hasItem(arr, item) {
    return arr.includes(item); // O(n)
}

// 正确：O(1) 查找
function hasItemOptimized(arr, item) {
    const set = new Set(arr);
    return set.has(item); // O(1)
}
```

### 数组方法选择

```js
// 根据需求选择合适的方法
const arr = [1, 2, 3, 4, 5];

// 只需要检查存在性，使用 some（可能提前退出）
const hasEven = arr.some(x => x % 2 === 0); // 找到第一个就停止

// 需要所有结果，使用 filter
const evens = arr.filter(x => x % 2 === 0);

// 需要转换，使用 map
const doubled = arr.map(x => x * 2);

// 需要累积，使用 reduce
const sum = arr.reduce((a, b) => a + b, 0);
```

## 对象操作优化

### 避免频繁的属性访问

```js
// 错误：频繁访问对象属性
function badExample(obj) {
    for (let i = 0; i < 1000; i++) {
        console.log(obj.name, obj.age, obj.email);
    }
}

// 正确：缓存属性值
function goodExample(obj) {
    const { name, age, email } = obj;
    for (let i = 0; i < 1000; i++) {
        console.log(name, age, email);
    }
}
```

### 使用 Map 替代对象

```js
// 对象：键必须是字符串
const obj = {};
obj[1] = 'one'; // 键被转换为字符串 "1"

// Map：键可以是任何类型
const map = new Map();
map.set(1, 'one'); // 键保持为数字 1

// Map 在频繁增删时性能更好
```

## 循环优化

### 减少循环次数

```js
// 错误：嵌套循环
function findCommon(arr1, arr2) {
    const common = [];
    for (let i = 0; i < arr1.length; i++) {
        for (let j = 0; j < arr2.length; j++) {
            if (arr1[i] === arr2[j]) {
                common.push(arr1[i]);
            }
        }
    }
    return common; // O(n * m)
}

// 正确：使用 Set
function findCommonOptimized(arr1, arr2) {
    const set = new Set(arr2);
    return arr1.filter(x => set.has(x)); // O(n + m)
}
```

### 提前退出

```js
// 错误：总是遍历完整数组
function hasLargeNumber(arr) {
    let found = false;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > 1000) {
            found = true;
        }
    }
    return found;
}

// 正确：找到就退出
function hasLargeNumberOptimized(arr) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > 1000) {
            return true; // 提前退出
        }
    }
    return false;
}
```

## 递归优化

### 尾递归优化

```js
// 错误：非尾递归
function factorial(n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1); // 需要保存调用栈
}

// 正确：尾递归（但 JavaScript 引擎可能不支持优化）
function factorialTail(n, acc = 1) {
    if (n <= 1) return acc;
    return factorialTail(n - 1, n * acc);
}
```

### 记忆化（Memoization）

```js
// 优化递归：使用记忆化
function fibonacci(n, memo = {}) {
    if (n in memo) return memo[n];
    if (n <= 1) return n;
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo);
    return memo[n];
}

// 未优化：O(2ⁿ)
// 优化后：O(n)
```

## 字符串操作优化

### 使用数组拼接

```js
// 错误：字符串拼接（每次创建新字符串）
function badConcat(arr) {
    let result = '';
    for (let i = 0; i < arr.length; i++) {
        result += arr[i]; // O(n²)
    }
    return result;
}

// 正确：使用数组 join
function goodConcat(arr) {
    const parts = [];
    for (let i = 0; i < arr.length; i++) {
        parts.push(arr[i]);
    }
    return parts.join(''); // O(n)
}
```

### 使用模板字符串

```js
// 错误：字符串拼接
const message = 'Hello, ' + name + '! You are ' + age + ' years old.';

// 正确：模板字符串（更清晰，性能也更好）
const message = `Hello, ${name}! You are ${age} years old.`;
```

## 注意事项

1. **过早优化**：不要过早优化，先确保功能正确
2. **可读性优先**：在性能和可读性之间找到平衡
3. **实际测试**：在真实数据上测试性能，不要假设
4. **复杂度分析**：理解算法复杂度，选择合适算法
5. **工具辅助**：使用性能分析工具识别瓶颈

## 常见错误

### 错误 1：忽略时间复杂度

```js
// 错误：在循环中使用 includes（O(n²)）
function hasDuplicates(arr) {
    for (let i = 0; i < arr.length; i++) {
        if (arr.includes(arr[i], i + 1)) { // O(n)
            return true;
        }
    }
    return false;
}

// 正确：使用 Set（O(n)）
function hasDuplicatesOptimized(arr) {
    const seen = new Set();
    for (let i = 0; i < arr.length; i++) {
        if (seen.has(arr[i])) return true;
        seen.add(arr[i]);
    }
    return false;
}
```

### 错误 2：不必要的数组创建

```js
// 错误：创建不必要的中间数组
function processData(arr) {
    const doubled = arr.map(x => x * 2);
    const filtered = doubled.filter(x => x > 10);
    return filtered.reduce((a, b) => a + b, 0);
}

// 正确：一次遍历
function processDataOptimized(arr) {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
        const doubled = arr[i] * 2;
        if (doubled > 10) {
            sum += doubled;
        }
    }
    return sum;
}
```

## 最佳实践

1. **选择合适的数据结构**：根据操作选择数组、Set、Map 等
2. **减少循环次数**：合并循环，使用 Set/Map 优化查找
3. **提前退出**：找到结果后立即返回
4. **缓存计算结果**：使用记忆化避免重复计算
5. **性能测试**：使用性能分析工具验证优化效果

## 练习

1. **数组去重优化**：实现一个高效的数组去重函数，比较不同方法的性能。

2. **查找优化**：实现一个函数，在大量数据中查找元素，使用 Set 优化性能。

3. **循环合并**：将多个数组操作合并为一次循环，减少遍历次数。

4. **递归优化**：使用记忆化优化递归函数（如斐波那契数列）。

5. **字符串拼接**：对比字符串拼接和数组 join 的性能差异。

完成以上练习后，继续学习下一节，了解内存管理。

## 总结

算法优化是提升 JavaScript 性能的基础。通过理解时间复杂度和空间复杂度，选择合适的数据结构和算法，可以减少代码执行时间和内存使用。在实际开发中，应该平衡性能和可读性，使用性能分析工具验证优化效果。

## 相关资源

- [算法复杂度分析](https://www.bigocheatsheet.com/)
- [JavaScript 性能优化指南](https://developer.mozilla.org/zh-CN/docs/Web/Performance)
