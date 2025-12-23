# 8.2.2 算法优化

## 1. 概述

算法优化是提高代码性能的核心方法，通过选择更高效的算法和数据结构，可以显著提高应用性能。理解算法复杂度对于优化至关重要。

## 2. 时间复杂度优化

### 2.1 选择合适算法

```ts
// O(n²) - 不优化
function findDuplicates(arr: number[]): number[] {
  const duplicates: number[] = [];
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] === arr[j] && !duplicates.includes(arr[i])) {
        duplicates.push(arr[i]);
      }
    }
  }
  return duplicates;
}

// O(n) - 优化
function findDuplicatesOptimized(arr: number[]): number[] {
  const seen = new Set<number>();
  const duplicates = new Set<number>();
  
  for (const num of arr) {
    if (seen.has(num)) {
      duplicates.add(num);
    } else {
      seen.add(num);
    }
  }
  
  return Array.from(duplicates);
}
```

### 2.2 缓存结果

```ts
// 不优化：重复计算
function fibonacci(n: number): number {
  if (n <= 1) return n;
  return fibonacci(n - 1) + fibonacci(n - 2);
}

// 优化：使用缓存
const fibCache = new Map<number, number>();

function fibonacciOptimized(n: number): number {
  if (n <= 1) return n;
  
  if (fibCache.has(n)) {
    return fibCache.get(n)!;
  }
  
  const result = fibonacciOptimized(n - 1) + fibonacciOptimized(n - 2);
  fibCache.set(n, result);
  return result;
}
```

## 3. 数据结构优化

### 3.1 使用 Map/Set

```ts
// 不优化：使用数组查找 O(n)
function hasUser(users: User[], id: number): boolean {
  return users.some(user => user.id === id);
}

// 优化：使用 Set O(1)
class UserSet {
  private ids: Set<number> = new Set();
  
  add(user: User): void {
    this.ids.add(user.id);
  }
  
  has(id: number): boolean {
    return this.ids.has(id);
  }
}
```

### 3.2 使用索引

```ts
// 不优化：线性查找
function getUserByEmail(users: User[], email: string): User | undefined {
  return users.find(user => user.email === email);
}

// 优化：使用索引
class UserIndex {
  private byEmail: Map<string, User> = new Map();
  
  constructor(users: User[]) {
    for (const user of users) {
      this.byEmail.set(user.email, user);
    }
  }
  
  getByEmail(email: string): User | undefined {
    return this.byEmail.get(email);
  }
}
```

## 4. 循环优化

### 4.1 减少循环次数

```ts
// 不优化：嵌套循环
function findPairs(arr: number[], target: number): [number, number][] {
  const pairs: [number, number][] = [];
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] + arr[j] === target) {
        pairs.push([arr[i], arr[j]]);
      }
    }
  }
  return pairs;
}

// 优化：使用 Map O(n)
function findPairsOptimized(arr: number[], target: number): [number, number][] {
  const pairs: [number, number][] = [];
  const seen = new Map<number, number>();
  
  for (let i = 0; i < arr.length; i++) {
    const complement = target - arr[i];
    if (seen.has(complement)) {
      pairs.push([complement, arr[i]]);
    }
    seen.set(arr[i], i);
  }
  
  return pairs;
}
```

### 4.2 提前退出

```ts
// 不优化：遍历全部
function hasEven(arr: number[]): boolean {
  let hasEven = false;
  for (const num of arr) {
    if (num % 2 === 0) {
      hasEven = true;
    }
  }
  return hasEven;
}

// 优化：提前退出
function hasEvenOptimized(arr: number[]): boolean {
  for (const num of arr) {
    if (num % 2 === 0) {
      return true; // 找到就退出
    }
  }
  return false;
}
```

## 5. 排序优化

### 5.1 选择合适的排序算法

```ts
// 小数组：使用插入排序
function insertionSort(arr: number[]): number[] {
  for (let i = 1; i < arr.length; i++) {
    const key = arr[i];
    let j = i - 1;
    while (j >= 0 && arr[j] > key) {
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = key;
  }
  return arr;
}

// 大数组：使用快速排序
function quickSort(arr: number[]): number[] {
  if (arr.length <= 1) return arr;
  
  const pivot = arr[Math.floor(arr.length / 2)];
  const left = arr.filter(x => x < pivot);
  const middle = arr.filter(x => x === pivot);
  const right = arr.filter(x => x > pivot);
  
  return [...quickSort(left), ...middle, ...quickSort(right)];
}
```

## 6. 最佳实践

### 6.1 算法选择

- 理解算法复杂度
- 选择合适的数据结构
- 使用缓存避免重复计算
- 优化循环和递归

### 6.2 性能测试

- 编写性能测试
- 对比不同算法
- 测量实际性能
- 验证优化效果

## 7. 注意事项

- **复杂度分析**：理解算法复杂度
- **实际性能**：理论复杂度不等于实际性能
- **数据规模**：根据数据规模选择算法
- **可读性**：保持代码可读性

## 8. 常见问题

### 8.1 如何选择算法？

根据数据规模、操作类型、性能要求选择。

### 8.2 何时使用缓存？

对于重复计算、昂贵操作、稳定结果使用缓存。

### 8.3 如何优化递归？

使用尾递归、记忆化、迭代替代。

## 9. 实践任务

1. **算法分析**：分析算法复杂度
2. **算法优化**：优化算法实现
3. **数据结构**：选择合适的数据结构
4. **性能测试**：编写性能测试
5. **持续优化**：持续优化算法

---

**下一节**：[8.2.3 内存管理](section-03-memory.md)
