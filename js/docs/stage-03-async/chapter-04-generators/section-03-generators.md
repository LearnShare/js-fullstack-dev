# 3.4.3 生成器函数

## 概述

生成器函数使用 `function*` 定义，可以暂停和恢复执行。本节详细介绍生成器函数的创建、yield 关键字的使用以及生成器对象的方法。

## 生成器函数的定义

### 函数声明

```js
function* generator() {
    yield 1;
    yield 2;
    yield 3;
}
```

### 函数表达式

```js
const generator = function*() {
    yield 1;
    yield 2;
};
```

### 对象方法

```js
const obj = {
    *generator() {
        yield 1;
        yield 2;
    }
};
```

### 类方法

```js
class MyClass {
    *generator() {
        yield 1;
        yield 2;
    }
}
```

## yield 关键字

### 基本使用

`yield` 用于暂停生成器函数的执行并返回一个值：

```js
function* generator() {
    yield 1;
    yield 2;
    yield 3;
}

const gen = generator();
console.log(gen.next()); // { value: 1, done: false }
console.log(gen.next()); // { value: 2, done: false }
console.log(gen.next()); // { value: 3, done: false }
console.log(gen.next()); // { value: undefined, done: true }
```

### yield 表达式

yield 可以接收值：

```js
function* generator() {
    const value = yield 1;
    console.log(value); // "hello"
}

const gen = generator();
gen.next(); // { value: 1, done: false }
gen.next('hello'); // 传递值给 yield 表达式
```

### yield* 委托

`yield*` 用于委托给另一个可迭代对象：

```js
function* generator1() {
    yield 1;
    yield 2;
}

function* generator2() {
    yield* generator1();
    yield 3;
}

const gen = generator2();
console.log(gen.next()); // { value: 1, done: false }
console.log(gen.next()); // { value: 2, done: false }
console.log(gen.next()); // { value: 3, done: false }
```

## 生成器对象的方法

### next()

调用 `next()` 方法恢复生成器函数的执行：

```js
function* generator() {
    yield 1;
    yield 2;
}

const gen = generator();
console.log(gen.next()); // { value: 1, done: false }
console.log(gen.next()); // { value: 2, done: false }
console.log(gen.next()); // { value: undefined, done: true }
```

### return()

调用 `return()` 方法终止生成器：

```js
function* generator() {
    yield 1;
    yield 2;
    yield 3;
}

const gen = generator();
console.log(gen.next()); // { value: 1, done: false }
console.log(gen.return('结束')); // { value: '结束', done: true }
console.log(gen.next()); // { value: undefined, done: true }
```

### throw()

调用 `throw()` 方法向生成器抛出错误：

```js
function* generator() {
    try {
        yield 1;
        yield 2;
    } catch (error) {
        console.error('捕获错误:', error.message);
    }
}

const gen = generator();
console.log(gen.next()); // { value: 1, done: false }
gen.throw(new Error('错误')); // 捕获错误: 错误
```

## 生成器的应用

### 无限序列

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

### 状态机

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

## 生成器与普通函数的对比

### 主要区别

| 特性           | 生成器函数                     | 普通函数                     |
|:---------------|:-------------------------------|:-----------------------------|
| **定义**       | 使用 `function*` 定义          | 使用 `function` 定义          |
| **执行**       | 可以暂停和恢复执行             | 一次性执行完成               |
| **返回值**     | 返回生成器对象（迭代器）       | 返回函数执行结果              |
| **yield**      | 可以使用 yield 关键字          | 不能使用 yield               |
| **调用方式**   | 调用后返回生成器，需要 next()  | 直接调用，立即返回结果        |
| **状态保持**   | 可以保持执行状态               | 每次调用重新开始              |
| **惰性求值**   | 支持惰性求值                   | 不支持惰性求值               |

### 使用场景对比

**生成器函数适合**：
- 需要暂停和恢复执行的场景
- 生成无限序列
- 实现状态机
- 惰性求值（按需计算）

**普通函数适合**：
- 常规的计算和处理
- 不需要暂停执行的场景
- 简单的数据处理

### 示例对比

```js
// 普通函数：一次性执行
function normalFunction() {
    return [1, 2, 3, 4, 5];
}

const result = normalFunction(); // 立即返回所有值

// 生成器函数：按需生成
function* generatorFunction() {
    yield 1;
    yield 2;
    yield 3;
    yield 4;
    yield 5;
}

const gen = generatorFunction(); // 返回生成器对象
console.log(gen.next().value); // 1（按需生成）
console.log(gen.next().value); // 2
```

## 注意事项

1. **function***：必须使用 function* 定义
2. **yield**：只能在生成器函数中使用 yield
3. **暂停和恢复**：生成器可以在执行过程中暂停和恢复
4. **迭代器协议**：生成器实现了迭代器协议

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

1. **使用生成器**：需要暂停和恢复执行时使用生成器
2. **理解 yield**：理解 yield 的暂停和恢复机制
3. **合理使用**：不要过度使用生成器，普通函数更简单时使用普通函数
4. **性能考虑**：生成器支持惰性求值，适合处理大数据集

## 练习

1. **创建生成器**：创建一个生成器函数，生成数字序列。

2. **使用 yield**：创建生成器，使用 yield 暂停和返回值。

3. **yield***：使用 yield* 委托给另一个生成器。

4. **生成器方法**：使用 next()、return() 和 throw() 方法操作生成器。

5. **实际应用**：实现一个使用生成器的实际场景（如状态机、无限序列等）。

完成以上练习后，继续学习下一节，了解异步生成器的使用。

## 总结

生成器函数提供了暂停和恢复执行的能力。通过 yield 关键字可以暂停函数执行并返回值，通过生成器对象的方法可以控制生成器的执行。生成器在实现自定义迭代、状态管理等方面非常有用。
