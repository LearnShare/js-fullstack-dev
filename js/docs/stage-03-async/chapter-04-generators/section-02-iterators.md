# 3.4.2 迭代器协议

## 概述

迭代器协议定义了迭代器的标准接口。本节详细介绍迭代器协议的定义、实现方法以及如何创建自定义迭代器。

## 迭代器协议

### 协议定义

迭代器协议要求对象实现 `next()` 方法，该方法返回一个对象，包含：

- `value`：当前迭代的值
- `done`：布尔值，表示迭代是否完成

### 基本实现

```js
const iterator = {
    data: [1, 2, 3],
    index: 0,
    
    next() {
        if (this.index < this.data.length) {
            return {
                value: this.data[this.index++],
                done: false
            };
        } else {
            return {
                value: undefined,
                done: true
            };
        }
    }
};

console.log(iterator.next()); // { value: 1, done: false }
console.log(iterator.next()); // { value: 2, done: false }
console.log(iterator.next()); // { value: 3, done: false }
console.log(iterator.next()); // { value: undefined, done: true }
```

## 可迭代对象

### 实现 Symbol.iterator

可迭代对象必须实现 `Symbol.iterator` 方法，该方法返回一个迭代器：

```js
const iterable = {
    data: [1, 2, 3],
    
    [Symbol.iterator]() {
        let index = 0;
        const data = this.data;
        
        return {
            next() {
                if (index < data.length) {
                    return {
                        value: data[index++],
                        done: false
                    };
                } else {
                    return {
                        value: undefined,
                        done: true
                    };
                }
            }
        };
    }
};

// 可以使用 for...of 遍历
for (const value of iterable) {
    console.log(value); // 1, 2, 3
}
```

### 使用生成器实现

使用生成器函数可以更简洁地实现可迭代对象：

```js
const iterable = {
    data: [1, 2, 3],
    
    *[Symbol.iterator]() {
        for (const item of this.data) {
            yield item;
        }
    }
};

for (const value of iterable) {
    console.log(value); // 1, 2, 3
}
```

## 内置可迭代对象

### 数组

数组是可迭代对象：

```js
const arr = [1, 2, 3];
const iterator = arr[Symbol.iterator]();

console.log(iterator.next()); // { value: 1, done: false }
console.log(iterator.next()); // { value: 2, done: false }
console.log(iterator.next()); // { value: 3, done: false }
console.log(iterator.next()); // { value: undefined, done: true }
```

### 字符串

字符串也是可迭代对象：

```js
const str = 'hello';
for (const char of str) {
    console.log(char); // h, e, l, l, o
}
```

### Map 和 Set

Map 和 Set 也是可迭代对象：

```js
const map = new Map([['a', 1], ['b', 2]]);
for (const [key, value] of map) {
    console.log(key, value); // a 1, b 2
}

const set = new Set([1, 2, 3]);
for (const value of set) {
    console.log(value); // 1, 2, 3
}
```

## 自定义迭代器

### 范围迭代器

```js
function createRangeIterator(start, end) {
    let current = start;
    
    return {
        next() {
            if (current < end) {
                return {
                    value: current++,
                    done: false
                };
            } else {
                return {
                    value: undefined,
                    done: true
                };
            }
        }
    };
}

const range = createRangeIterator(1, 4);
console.log(range.next()); // { value: 1, done: false }
console.log(range.next()); // { value: 2, done: false }
console.log(range.next()); // { value: 3, done: false }
console.log(range.next()); // { value: undefined, done: true }
```

### 可迭代的范围对象

```js
class Range {
    constructor(start, end) {
        this.start = start;
        this.end = end;
    }
    
    [Symbol.iterator]() {
        let current = this.start;
        const end = this.end;
        
        return {
            next() {
                if (current < end) {
                    return {
                        value: current++,
                        done: false
                    };
                } else {
                    return {
                        value: undefined,
                        done: true
                    };
                }
            }
        };
    }
}

const range = new Range(1, 4);
for (const value of range) {
    console.log(value); // 1, 2, 3
}
```

## 注意事项

1. **next 方法**：必须返回包含 value 和 done 的对象
2. **done 属性**：当 done 为 true 时，value 可以省略
3. **可迭代对象**：实现 Symbol.iterator 方法返回迭代器
4. **不可重用**：迭代器通常是一次性的，遍历完后不能再次使用

## 常见错误

### 错误 1：next 方法返回值不正确

```js
// 错误：next 方法没有返回正确的对象
const iterator = {
    next() {
        return 1; // 错误，应该返回 { value, done }
    }
};

// 正确：返回包含 value 和 done 的对象
const iterator = {
    next() {
        return {
            value: 1,
            done: false
        };
    }
};
```

### 错误 2：Symbol.iterator 不是方法

```js
// 错误：Symbol.iterator 不是方法
const iterable = {
    Symbol: {
        iterator: function() { }
    }
};

// 正确：使用计算属性名
const iterable = {
    [Symbol.iterator]() {
        // ...
    }
};
```

## 最佳实践

1. **实现协议**：正确实现迭代器协议
2. **使用生成器**：使用生成器函数简化实现
3. **理解机制**：理解迭代器的工作原理
4. **合理使用**：在需要自定义迭代行为时使用

## 练习

1. **创建迭代器**：手动创建一个迭代器，实现 next() 方法。

2. **创建可迭代对象**：创建一个可迭代对象，实现 Symbol.iterator 方法。

3. **范围迭代器**：创建一个范围迭代器，生成指定范围的数字。

4. **自定义类**：创建一个类，实现可迭代接口。

5. **实际应用**：实现一个使用迭代器的实际场景。

完成以上练习后，继续学习下一节，了解生成器函数的详细用法。

## 总结

迭代器协议定义了标准的迭代接口。通过实现 next() 方法可以创建迭代器，通过实现 Symbol.iterator 方法可以创建可迭代对象。理解迭代器协议是掌握生成器和高级迭代特性的基础。
