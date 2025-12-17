# 3.3.4 错误处理与并行执行

## 概述

本节介绍 async/await 的错误处理方法和并行执行优化技巧，包括 try/catch 的使用、Promise.all 的配合使用，以及性能优化的最佳实践。

## 错误处理

### 使用 try/catch

在 async 函数中使用 try/catch 处理错误：

```js
async function fetchData() {
    try {
        const response = await fetch('/api/data');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('获取数据失败:', error);
        throw error;
    }
}
```

### 捕获多个 await

一个 try/catch 可以捕获多个 await 的错误：

```js
async function fetchMultipleData() {
    try {
        const user = await fetchUser();
        const posts = await fetchPosts();
        const comments = await fetchComments();
        return { user, posts, comments };
    } catch (error) {
        console.error('获取数据失败:', error);
        throw error;
    }
}
```

### 分别处理错误

可以分别处理不同操作的错误：

```js
async function fetchData() {
    let user, posts;
    
    try {
        user = await fetchUser();
    } catch (error) {
        console.error('获取用户失败:', error);
        user = getDefaultUser();
    }
    
    try {
        posts = await fetchPosts();
    } catch (error) {
        console.error('获取文章失败:', error);
        posts = [];
    }
    
    return { user, posts };
}
```

## 并行执行

### 串行执行的问题

多个 await 会串行执行，总时间等于所有操作时间之和：

```js
async function fetchData() {
    const data1 = await fetchData1(); // 等待 1 秒
    const data2 = await fetchData2(); // 等待 1 秒
    const data3 = await fetchData3(); // 等待 1 秒
    // 总共等待 3 秒
    return { data1, data2, data3 };
}
```

### 使用 Promise.all 并行执行

使用 Promise.all 可以让多个操作并行执行：

```js
async function fetchData() {
    const [data1, data2, data3] = await Promise.all([
        fetchData1(), // 并行执行
        fetchData2(), // 并行执行
        fetchData3()  // 并行执行
    ]);
    // 总共等待 1 秒（最慢的那个）
    return { data1, data2, data3 };
}
```

### 并行执行示例

```js
async function loadUserPage(userId) {
    const [user, posts, comments] = await Promise.all([
        fetchUser(userId),
        fetchUserPosts(userId),
        fetchUserComments(userId)
    ]);
    
    return { user, posts, comments };
}
```

## 混合执行

### 部分并行

有些操作可以并行，有些需要串行：

```js
async function processData(id) {
    // 并行获取基础数据
    const [user, config] = await Promise.all([
        fetchUser(id),
        fetchConfig()
    ]);
    
    // 串行处理依赖数据
    const posts = await fetchUserPosts(user.id);
    const comments = await fetchUserComments(posts[0].id);
    
    return { user, config, posts, comments };
}
```

### 条件并行

根据条件决定是否并行：

```js
async function fetchData(needPosts) {
    const user = await fetchUser();
    
    let posts;
    if (needPosts) {
        posts = await fetchPosts(user.id);
    }
    
    return { user, posts };
}
```

## 错误处理与并行执行

### Promise.all 的错误处理

Promise.all 中任何一个失败，整个都会失败：

```js
async function fetchData() {
    try {
        const [data1, data2, data3] = await Promise.all([
            fetchData1(),
            fetchData2(),
            fetchData3()
        ]);
        return { data1, data2, data3 };
    } catch (error) {
        console.error('获取数据失败:', error);
        throw error;
    }
}
```

### 使用 Promise.allSettled

如果需要部分失败也能继续：

```js
async function fetchData() {
    const results = await Promise.allSettled([
        fetchData1(),
        fetchData2(),
        fetchData3()
    ]);
    
    return results.map(result => {
        if (result.status === 'fulfilled') {
            return result.value;
        } else {
            console.error('获取数据失败:', result.reason);
            return null;
        }
    });
}
```

## 性能优化技巧

### 1. 尽早启动异步操作

```js
// 不好：串行执行
async function process() {
    const data1 = await fetch1();
    const data2 = await fetch2(); // 等 fetch1 完成才开始
    return { data1, data2 };
}

// 好：并行执行
async function process() {
    const promise1 = fetch1(); // 立即开始
    const promise2 = fetch2(); // 立即开始
    const data1 = await promise1;
    const data2 = await promise2;
    return { data1, data2 };
}
```

### 2. 使用 Promise.all

```js
// 并行执行多个独立操作
const [result1, result2, result3] = await Promise.all([
    operation1(),
    operation2(),
    operation3()
]);
```

### 3. 避免不必要的 await

```js
// 不好：不必要的 await
async function process() {
    const promise = fetchData();
    await promise; // 如果后面不需要立即使用，可以延迟 await
    return promise;
}

// 好：直接返回 Promise
async function process() {
    return fetchData(); // 调用者可以决定何时 await
}
```

## 注意事项

1. **错误处理**：使用 try/catch 处理 await 的错误
2. **性能考虑**：多个独立的 await 考虑使用 Promise.all 并行执行
3. **依赖关系**：有依赖关系的操作需要串行执行
4. **错误传播**：Promise.all 中任何一个失败，整个都会失败

## 常见错误

### 错误 1：不必要的串行执行

```js
// 错误：不必要的串行执行
async function fetchData() {
    const data1 = await fetchData1(); // 等待
    const data2 = await fetchData2(); // 等待（不依赖 data1）
    // 总时间 = 时间1 + 时间2
}

// 正确：并行执行
async function fetchData() {
    const [data1, data2] = await Promise.all([
        fetchData1(),
        fetchData2()
    ]);
    // 总时间 = max(时间1, 时间2)
}
```

### 错误 2：Promise.all 的错误处理不当

```js
// 错误：Promise.all 中一个失败，整个失败
const [data1, data2] = await Promise.all([
    fetchData1(), // 如果失败
    fetchData2()
]); // 这里会抛出错误

// 正确：使用 Promise.allSettled 或单独处理
const results = await Promise.allSettled([
    fetchData1(),
    fetchData2()
]);
```

## 最佳实践

1. **错误处理**：始终使用 try/catch 处理错误
2. **并行优化**：多个独立操作使用 Promise.all 并行执行
3. **理解依赖**：有依赖关系的操作必须串行执行
4. **性能监控**：注意性能影响，合理选择并行或串行

## 练习

1. **错误处理**：创建一个 async 函数，使用 try/catch 处理多个 await 的错误。

2. **并行执行**：将串行执行的多个异步操作改为并行执行，使用 Promise.all。

3. **混合执行**：实现一个既有并行又有串行的异步操作场景。

4. **错误恢复**：使用 Promise.allSettled 处理部分失败的情况，允许部分数据失败。

5. **性能优化**：优化一个实际的异步操作场景，提高执行效率。

完成以上练习后，继续学习下一章，了解生成器与迭代器。

## 总结

async/await 的错误处理使用 try/catch，并行执行可以使用 Promise.all 优化性能。理解错误处理和并行执行的机制，能够编写更高效、更健壮的异步代码。根据实际需求选择合适的执行策略。
