# 3.2.3 Promise 链式调用

## 概述

Promise 链式调用是 Promise 的核心特性之一，它允许将多个异步操作串联起来，形成清晰的处理流程。本节详细介绍 Promise 链式调用的机制、返回值处理和错误传播。

## 链式调用的基本概念

### 什么是链式调用

链式调用是指在一个 Promise 上连续调用 `then` 方法，每个 `then` 返回一个新的 Promise，可以继续调用下一个 `then`。

```js
Promise.resolve(1)
    .then(value => value + 1)      // 2
    .then(value => value * 2)      // 4
    .then(value => console.log(value)); // 4
```

### 链式调用的优势

链式调用的优势：

1. **代码清晰**：避免了回调嵌套
2. **易于维护**：每个步骤都很清晰
3. **错误处理**：统一的错误处理机制
4. **可组合性**：可以轻松组合多个异步操作

## 返回值处理

### 返回普通值

如果 `then` 的回调函数返回普通值，该值会成为下一个 `then` 的参数：

```js
Promise.resolve(1)
    .then(value => {
        return value + 1; // 返回 2
    })
    .then(value => {
        console.log(value); // 2
        return value * 2; // 返回 4
    })
    .then(value => {
        console.log(value); // 4
    });
```

### 返回 Promise

如果 `then` 的回调函数返回 Promise，下一个 `then` 会等待这个 Promise 完成：

```js
Promise.resolve(1)
    .then(value => {
        return Promise.resolve(value + 1); // 返回 Promise
    })
    .then(value => {
        console.log(value); // 2（等待上面的 Promise 完成）
    });
```

### 不返回任何值

如果 `then` 的回调函数没有返回值，下一个 `then` 会接收 `undefined`：

```js
Promise.resolve(1)
    .then(value => {
        console.log(value); // 1
        // 没有返回值
    })
    .then(value => {
        console.log(value); // undefined
    });
```

### 返回 thenable 对象

返回一个具有 `then` 方法的对象（thenable），会被当作 Promise 处理：

```js
Promise.resolve(1)
    .then(value => {
        return {
            then: function(resolve) {
                resolve(value + 1);
            }
        };
    })
    .then(value => {
        console.log(value); // 2
    });
```

## 错误传播

### 错误在链中传播

Promise 链中的错误会向下传播，直到遇到 `catch`：

```js
Promise.resolve(1)
    .then(value => {
        throw new Error('错误');
    })
    .then(value => {
        // 不会执行
    })
    .catch(error => {
        console.error(error.message); // "错误"
    });
```

### 在 catch 中恢复

`catch` 可以返回一个值，让 Promise 链继续：

```js
Promise.resolve(1)
    .then(value => {
        throw new Error('错误');
    })
    .catch(error => {
        console.error(error.message); // "错误"
        return 0; // 返回默认值，让链继续
    })
    .then(value => {
        console.log(value); // 0
    });
```

### 多个 catch

可以在链的不同位置使用多个 `catch`：

```js
Promise.resolve(1)
    .then(value => {
        throw new Error('错误1');
    })
    .catch(error => {
        console.error('捕获错误1:', error.message);
        throw new Error('错误2'); // 继续抛出错误
    })
    .catch(error => {
        console.error('捕获错误2:', error.message);
    });
```

## 实际应用场景

### 数据转换链

```js
// 数据处理链
fetchUserData(userId)
    .then(user => user.name)              // 提取用户名
    .then(name => name.toUpperCase())      // 转换为大写
    .then(upperName => `Hello, ${upperName}`) // 格式化
    .then(greeting => console.log(greeting))
    .catch(error => console.error('处理失败:', error));
```

### 异步操作链

```js
// 多个异步操作串联
login(user, password)
    .then(token => fetchUserProfile(token))
    .then(profile => updateUserPreferences(profile))
    .then(result => console.log('更新成功:', result))
    .catch(error => console.error('操作失败:', error));
```

### 条件分支

```js
// 在链中进行条件判断
fetchData()
    .then(data => {
        if (data.needUpdate) {
            return updateData(data);
        } else {
            return data;
        }
    })
    .then(result => processResult(result))
    .catch(error => handleError(error));
```

## 链式调用的注意事项

### 避免嵌套 then

```js
// 错误：嵌套 then
promise.then(value => {
    anotherPromise(value).then(result => {
        // 嵌套过深
    });
});

// 正确：返回 Promise，继续链式调用
promise
    .then(value => anotherPromise(value))
    .then(result => {
        // 继续处理
    });
```

### 处理异步 then 回调

```js
// 如果 then 回调本身是异步的，需要返回 Promise
promise
    .then(value => {
        return new Promise(resolve => {
            setTimeout(() => {
                resolve(value + 1);
            }, 1000);
        });
    })
    .then(value => {
        console.log(value); // 等待 1 秒后输出
    });
```

### 使用 async/await 简化

在支持 async/await 的环境中，可以使用 async/await 简化链式调用：

```js
// 使用 Promise 链
fetchData()
    .then(data => processData(data))
    .then(result => saveResult(result))
    .then(() => console.log('完成'))
    .catch(error => console.error(error));

// 使用 async/await（更清晰）
try {
    const data = await fetchData();
    const result = await processData(data);
    await saveResult(result);
    console.log('完成');
} catch (error) {
    console.error(error);
}
```

## 注意事项

1. **返回值**：then 回调的返回值会成为下一个 then 的参数
2. **Promise 返回**：返回 Promise 会让下一个 then 等待
3. **错误传播**：错误会向下传播直到遇到 catch
4. **避免嵌套**：不要嵌套 then 回调，使用链式调用

## 常见错误

### 错误 1：忘记返回 Promise

```js
// 错误：没有返回 Promise
promise
    .then(value => {
        anotherAsyncOperation(value); // 没有 return
    })
    .then(result => {
        // result 是 undefined，不是异步操作的结果
    });

// 正确：返回 Promise
promise
    .then(value => {
        return anotherAsyncOperation(value);
    })
    .then(result => {
        // result 是异步操作的结果
    });
```

### 错误 2：在 then 中抛出错误但没有 catch

```js
// 错误：抛出错误但没有 catch
promise
    .then(value => {
        throw new Error('错误');
    })
    .then(value => {
        // 不会执行，但错误没有被处理
    });
```

### 错误 3：嵌套 then

```js
// 错误：嵌套 then
promise.then(value => {
    anotherPromise(value).then(result => {
        // 嵌套过深，失去了链式调用的优势
    });
});

// 正确：使用链式调用
promise
    .then(value => anotherPromise(value))
    .then(result => {
        // 继续处理
    });
```

## 最佳实践

1. **返回 Promise**：在 then 中执行异步操作时，返回 Promise
2. **统一错误处理**：在链的末尾使用 catch 统一处理错误
3. **避免嵌套**：使用链式调用而不是嵌套 then
4. **使用 async/await**：在支持的环境中，使用 async/await 简化代码

## 练习

1. **基础链式调用**：创建一个 Promise 链，依次执行三个异步操作，每个操作处理前一个操作的结果。

2. **错误处理**：创建一个 Promise 链，在中间抛出错误，使用 catch 处理错误并恢复执行。

3. **条件分支**：创建一个 Promise 链，根据某个条件决定执行不同的异步操作。

4. **数据转换**：创建一个 Promise 链，对数据进行多次转换（如：获取数据 → 过滤 → 排序 → 格式化）。

5. **实际场景**：实现一个完整的用户登录流程（登录 → 获取用户信息 → 更新最后登录时间 → 返回结果），使用 Promise 链式调用。

完成以上练习后，继续学习下一节，了解 Promise 组合方法的使用。

## 总结

Promise 链式调用是处理多个异步操作的重要方式。通过链式调用，可以避免回调嵌套，使代码更加清晰易读。理解返回值处理和错误传播机制，是掌握 Promise 链式调用的关键。

## 相关资源

- [MDN：Promise.then()](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/then)
- [JavaScript.info：Promise 链](https://zh.javascript.info/promise-chaining)
