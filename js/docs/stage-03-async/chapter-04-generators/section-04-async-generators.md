# 3.4.4 异步生成器

## 概述

异步生成器结合了生成器和异步编程，可以生成异步序列。本节介绍异步生成器的创建、使用以及与 async/await 的配合使用。

## 异步生成器的定义

### 基本语法

使用 `async function*` 定义异步生成器：

```js
async function* asyncGenerator() {
    yield 1;
    yield 2;
    yield 3;
}
```

### 基本使用

异步生成器返回一个异步迭代器：

```js
async function* asyncGenerator() {
    yield 1;
    yield 2;
    yield 3;
}

(async () => {
    for await (const value of asyncGenerator()) {
        console.log(value); // 1, 2, 3
    }
})();
```

## await 与 yield 结合

### 在异步生成器中使用 await

异步生成器中可以使用 await 等待异步操作：

```js
async function* fetchData() {
    const data1 = await fetch('/api/data1').then(r => r.json());
    yield data1;
    
    const data2 = await fetch('/api/data2').then(r => r.json());
    yield data2;
}

(async () => {
    for await (const data of fetchData()) {
        console.log(data);
    }
})();
```

### 异步序列生成

```js
async function* asyncSequence() {
    for (let i = 0; i < 5; i++) {
        await new Promise(resolve => setTimeout(resolve, 1000));
        yield i;
    }
}

(async () => {
    for await (const value of asyncSequence()) {
        console.log(value); // 每秒输出一个数字
    }
})();
```

## for await...of

### 遍历异步生成器

使用 `for await...of` 遍历异步生成器：

```js
async function* asyncGenerator() {
    yield Promise.resolve(1);
    yield Promise.resolve(2);
    yield Promise.resolve(3);
}

(async () => {
    for await (const value of asyncGenerator()) {
        console.log(value); // 1, 2, 3
    }
})();
```

### 处理异步迭代器

```js
async function processAsyncData() {
    const asyncIterable = {
        async *[Symbol.asyncIterator]() {
            yield 1;
            yield 2;
            yield 3;
        }
    };
    
    for await (const value of asyncIterable) {
        console.log(value); // 1, 2, 3
    }
}

processAsyncData();
```

## 实际应用场景

### 流式数据处理

```js
async function* processStream(stream) {
    for await (const chunk of stream) {
        const processed = await processChunk(chunk);
        yield processed;
    }
}

(async () => {
    for await (const data of processStream(inputStream)) {
        console.log(data);
    }
})();
```

### 分页数据获取

```js
async function* fetchPages(url) {
    let page = 1;
    let hasMore = true;
    
    while (hasMore) {
        const response = await fetch(`${url}?page=${page}`);
        const data = await response.json();
        
        yield data.items;
        
        hasMore = data.hasMore;
        page++;
    }
}

(async () => {
    for await (const items of fetchPages('/api/data')) {
        console.log(items);
    }
})();
```

## 注意事项

1. **async function***：必须使用 async function* 定义
2. **for await...of**：使用 for await...of 遍历异步生成器
3. **异步迭代器**：异步生成器返回异步迭代器
4. **await 支持**：异步生成器中可以使用 await

## 常见错误

### 错误 1：使用 for...of 遍历异步生成器

```js
// 错误：使用 for...of 遍历异步生成器
async function* asyncGenerator() {
    yield 1;
}

for (const value of asyncGenerator()) {
    // 得到 Promise 对象，不是值
}

// 正确：使用 for await...of
for await (const value of asyncGenerator()) {
    // 得到实际值
}
```

### 错误 2：忘记 async 关键字

```js
// 错误：忘记 async，不能在生成器中使用 await
function* generator() {
    await fetch('/api/data'); // SyntaxError
}

// 正确：使用 async function*
async function* generator() {
    await fetch('/api/data');
}
```

## 最佳实践

1. **使用异步生成器**：需要生成异步序列时使用异步生成器
2. **for await...of**：使用 for await...of 遍历异步生成器
3. **理解机制**：理解异步生成器的执行机制
4. **合理使用**：在需要流式处理或分页数据时使用

## 练习

1. **创建异步生成器**：创建一个异步生成器，生成异步序列。

2. **使用 await**：在异步生成器中使用 await 等待异步操作。

3. **for await...of**：使用 for await...of 遍历异步生成器。

4. **实际应用**：实现一个使用异步生成器的实际场景（如流式处理、分页数据等）。

5. **组合使用**：结合 async/await 和异步生成器实现复杂的数据处理流程。

完成以上练习后，阶段三的学习就完成了。

## 总结

异步生成器结合了生成器和异步编程的能力，可以生成异步序列。使用 async function* 定义异步生成器，使用 for await...of 遍历异步生成器。异步生成器在流式处理、分页数据获取等场景中非常有用。

## 相关资源

- [MDN：async function*](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/async_function*)
- [MDN：for await...of](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/for-await...of)
