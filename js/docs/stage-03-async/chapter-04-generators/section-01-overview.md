# 3.4.1 生成器与迭代器概述

## 概述

生成器和迭代器是 JavaScript 中强大的特性，它们提供了自定义迭代行为的能力。本节介绍迭代器协议、可迭代对象和生成器的基本概念。

## 什么是迭代器

### 定义

迭代器是一个对象，它提供了一种标准的方式来遍历数据集合。迭代器必须实现 `next()` 方法。

### 迭代器协议

迭代器协议定义了迭代器必须实现的方法：

- `next()` 方法：返回一个对象，包含 `value` 和 `done` 属性
  - `value`：当前迭代的值
  - `done`：布尔值，表示迭代是否完成

```js
const iterator = {
    next() {
        return {
            value: 1,
            done: false
        };
    }
};
```

## 什么是可迭代对象

### 定义

可迭代对象是实现了 `Symbol.iterator` 方法的对象，该方法返回一个迭代器。

### 可迭代对象示例

JavaScript 中的数组、字符串、Map、Set 等都是可迭代对象：

```js
const arr = [1, 2, 3];
const iterator = arr[Symbol.iterator]();

console.log(iterator.next()); // { value: 1, done: false }
console.log(iterator.next()); // { value: 2, done: false }
console.log(iterator.next()); // { value: 3, done: false }
console.log(iterator.next()); // { value: undefined, done: true }
```

### 使用 for...of 遍历

可迭代对象可以使用 `for...of` 循环遍历：

```js
const arr = [1, 2, 3];

for (const value of arr) {
    console.log(value); // 1, 2, 3
}
```

## 什么是生成器

### 定义

生成器是使用 `function*` 定义的函数，它可以暂停和恢复执行。生成器函数返回一个生成器对象，该对象实现了迭代器协议。

### 生成器函数示例

```js
function* numberGenerator() {
    yield 1;
    yield 2;
    yield 3;
}

const generator = numberGenerator();

console.log(generator.next()); // { value: 1, done: false }
console.log(generator.next()); // { value: 2, done: false }
console.log(generator.next()); // { value: 3, done: false }
console.log(generator.next()); // { value: undefined, done: true }
```

### 使用 for...of 遍历生成器

生成器是可迭代对象，可以使用 `for...of` 遍历：

```js
function* numberGenerator() {
    yield 1;
    yield 2;
    yield 3;
}

for (const value of numberGenerator()) {
    console.log(value); // 1, 2, 3
}
```

## 生成器的特性

### 暂停和恢复

生成器函数可以在执行过程中暂停，然后在需要时恢复：

```js
function* generator() {
    console.log('开始');
    yield 1;
    console.log('中间');
    yield 2;
    console.log('结束');
}

const gen = generator();
gen.next(); // 输出 "开始"，返回 { value: 1, done: false }
gen.next(); // 输出 "中间"，返回 { value: 2, done: false }
gen.next(); // 输出 "结束"，返回 { value: undefined, done: true }
```

### 惰性求值

生成器支持惰性求值，只有在需要时才计算值：

```js
function* infiniteNumbers() {
    let i = 0;
    while (true) {
        yield i++;
    }
}

const numbers = infiniteNumbers();
console.log(numbers.next().value); // 0
console.log(numbers.next().value); // 1
console.log(numbers.next().value); // 2
// 可以无限生成，但不会一次性计算所有值
```

## 生成器的应用场景

### 1. 自定义迭代

```js
function* range(start, end) {
    for (let i = start; i < end; i++) {
        yield i;
    }
}

for (const num of range(1, 5)) {
    console.log(num); // 1, 2, 3, 4
}
```

### 2. 惰性序列

```js
function* fibonacci() {
    let [prev, curr] = [0, 1];
    while (true) {
        yield curr;
        [prev, curr] = [curr, prev + curr];
    }
}

const fib = fibonacci();
console.log(fib.next().value); // 1
console.log(fib.next().value); // 1
console.log(fib.next().value); // 2
console.log(fib.next().value); // 3
```

### 3. 状态管理

```js
function* stateMachine() {
    let state = 'start';
    
    while (true) {
        const input = yield state;
        
        if (input === 'next') {
            state = state === 'start' ? 'middle' : 'end';
        } else if (input === 'reset') {
            state = 'start';
        }
    }
}

const sm = stateMachine();
console.log(sm.next().value); // "start"
console.log(sm.next('next').value); // "middle"
console.log(sm.next('next').value); // "end"
```

## 注意事项

1. **生成器函数**：使用 `function*` 定义
2. **yield 关键字**：用于暂停和返回值
3. **迭代器协议**：生成器实现了迭代器协议
4. **可迭代对象**：生成器是可迭代对象

## 常见错误

### 错误 1：忘记星号

```js
// 错误：忘记 function* 中的星号
function generator() {
    yield 1; // SyntaxError
}

// 正确：使用 function*
function* generator() {
    yield 1;
}
```

### 错误 2：在普通函数中使用 yield

```js
// 错误：在普通函数中使用 yield
function normalFunction() {
    yield 1; // SyntaxError
}

// 正确：使用生成器函数
function* generator() {
    yield 1;
}
```

## 最佳实践

1. **使用生成器**：需要自定义迭代行为时使用生成器
2. **理解协议**：理解迭代器协议的工作原理
3. **合理使用**：不要过度使用生成器，普通函数更简单时使用普通函数
4. **性能考虑**：生成器支持惰性求值，适合处理大数据集

## 练习

1. **创建迭代器**：手动创建一个迭代器对象，实现 next() 方法。

2. **创建可迭代对象**：创建一个可迭代对象，实现 Symbol.iterator 方法。

3. **创建生成器**：创建一个生成器函数，生成数字序列。

4. **遍历生成器**：使用 for...of 遍历生成器生成的值。

5. **实际应用**：实现一个使用生成器的实际场景（如生成序列、状态机等）。

完成以上练习后，继续学习下一节，了解迭代器协议的详细机制。

## 总结

迭代器和生成器提供了自定义迭代行为的能力。迭代器协议定义了标准的迭代方式，生成器函数提供了创建迭代器的简洁方法。理解迭代器协议和生成器的基本概念，是掌握 JavaScript 高级特性的基础。

## 相关资源

- [MDN：迭代器协议](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Iteration_protocols)
- [MDN：生成器函数](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/function*)
