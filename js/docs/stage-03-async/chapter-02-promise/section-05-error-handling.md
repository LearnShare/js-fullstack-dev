# 3.2.5 Promise 错误处理

## 概述

Promise 的错误处理是异步编程中的重要部分。本节详细介绍 Promise 的错误处理机制，包括错误捕获、错误传播、错误恢复和最佳实践。

## 错误捕获

### 使用 catch()

`catch()` 方法用于捕获 Promise 链中的错误：

```js
Promise.reject('错误')
    .catch(error => {
        console.error(error); // "错误"
    });
```

### catch 的位置

`catch` 可以放在链的任何位置：

```js
Promise.resolve(1)
    .then(value => {
        throw new Error('错误1');
    })
    .catch(error => {
        console.error('捕获错误1:', error.message);
        throw new Error('错误2');
    })
    .catch(error => {
        console.error('捕获错误2:', error.message);
    });
```

### 链式调用中的错误

错误会在 Promise 链中向下传播：

```js
Promise.resolve(1)
    .then(value => {
        throw new Error('错误');
    })
    .then(value => {
        // 不会执行
    })
    .then(value => {
        // 不会执行
    })
    .catch(error => {
        console.error(error.message); // "错误"
    });
```

## 错误类型

### 普通错误

```js
Promise.reject('字符串错误')
    .catch(error => {
        console.error(error); // "字符串错误"
    });
```

### Error 对象

```js
Promise.reject(new Error('错误信息'))
    .catch(error => {
        console.error(error.message); // "错误信息"
        console.error(error.stack); // 错误堆栈
    });
```

### 自定义错误

```js
class CustomError extends Error {
    constructor(message, code) {
        super(message);
        this.code = code;
        this.name = 'CustomError';
    }
}

Promise.reject(new CustomError('自定义错误', 404))
    .catch(error => {
        if (error instanceof CustomError) {
            console.error(`错误代码: ${error.code}, 信息: ${error.message}`);
        }
    });
```

## 错误传播

### 错误在链中传播

错误会沿着 Promise 链向下传播，直到遇到 `catch`：

```js
Promise.resolve(1)
    .then(value => {
        throw new Error('错误1');
    })
    .then(value => {
        // 跳过
    })
    .then(value => {
        // 跳过
    })
    .catch(error => {
        // 捕获所有错误
        console.error(error.message); // "错误1"
    });
```

### 在 catch 中重新抛出

`catch` 中可以重新抛出错误，让错误继续传播：

```js
Promise.resolve(1)
    .then(value => {
        throw new Error('错误1');
    })
    .catch(error => {
        console.error('捕获:', error.message);
        throw new Error('错误2'); // 重新抛出
    })
    .catch(error => {
        console.error('最终捕获:', error.message); // "错误2"
    });
```

### 在 catch 中返回正常值

`catch` 中可以返回正常值，让 Promise 链继续：

```js
Promise.reject('错误')
    .catch(error => {
        console.error(error);
        return '默认值'; // 返回正常值
    })
    .then(value => {
        console.log(value); // "默认值"
    });
```

## 错误恢复

### 使用默认值

```js
fetchUserData(userId)
    .catch(error => {
        console.error('获取用户数据失败:', error);
        return getDefaultUserData(); // 返回默认数据
    })
    .then(userData => {
        // 使用用户数据或默认数据
        renderUser(userData);
    });
```

### 重试机制

```js
function fetchWithRetry(url, retries = 3) {
    return fetch(url)
        .catch(error => {
            if (retries > 0) {
                console.log(`重试中，剩余 ${retries} 次`);
                return fetchWithRetry(url, retries - 1);
            } else {
                throw error;
            }
        });
}

fetchWithRetry('/api/data')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('最终失败:', error));
```

### 降级方案

```js
Promise.all([
    fetchPrimaryData(),
    fetchBackupData()
])
    .then(([primary, backup]) => primary) // 优先使用主要数据
    .catch(() => fetchBackupData()) // 失败时使用备用数据
    .then(data => {
        // 使用主要数据或备用数据
        processData(data);
    });
```

## 未捕获的错误

### 全局错误处理

Promise 中的未捕获错误会导致警告：

```js
// 浏览器环境
window.addEventListener('unhandledrejection', event => {
    console.error('未捕获的 Promise 错误:', event.reason);
    event.preventDefault(); // 阻止默认行为
});

// Node.js 环境
process.on('unhandledRejection', (reason, promise) => {
    console.error('未捕获的 Promise 错误:', reason);
});
```

### 避免未捕获的错误

始终为 Promise 添加错误处理：

```js
// 错误：没有错误处理
Promise.reject('错误');
// 会导致未捕获的错误警告

// 正确：添加错误处理
Promise.reject('错误')
    .catch(error => {
        console.error(error);
    });
```

## finally 中的错误处理

### finally 中的错误

`finally` 中的错误会覆盖原来的错误：

```js
Promise.resolve('成功')
    .then(value => {
        throw new Error('原始错误');
    })
    .finally(() => {
        throw new Error('finally 中的错误');
    })
    .catch(error => {
        console.error(error.message); // "finally 中的错误"
    });
```

### 在 finally 中避免抛出错误

```js
Promise.resolve('成功')
    .then(value => {
        throw new Error('原始错误');
    })
    .finally(() => {
        try {
            // 清理操作
        } catch (error) {
            console.error('清理失败:', error);
            // 不要重新抛出，避免覆盖原始错误
        }
    })
    .catch(error => {
        console.error(error.message); // "原始错误"
    });
```

## 最佳实践

### 1. 始终处理错误

```js
// 总是为 Promise 添加 catch
promise
    .then(value => processValue(value))
    .catch(error => handleError(error));
```

### 2. 在链的末尾统一处理

```js
// 在链的末尾统一处理错误
fetchData()
    .then(data => processData(data))
    .then(result => saveResult(result))
    .catch(error => {
        // 统一处理所有错误
        logError(error);
        showErrorMessage(error);
    });
```

### 3. 区分错误类型

```js
fetchData()
    .catch(error => {
        if (error instanceof NetworkError) {
            // 网络错误
            showNetworkError();
        } else if (error instanceof ValidationError) {
            // 验证错误
            showValidationError(error);
        } else {
            // 其他错误
            showGenericError();
        }
    });
```

### 4. 记录错误信息

```js
fetchData()
    .catch(error => {
        // 记录错误信息
        console.error('错误详情:', {
            message: error.message,
            stack: error.stack,
            timestamp: new Date().toISOString()
        });
        throw error; // 重新抛出，让上层处理
    });
```

## 常见错误

### 错误 1：忘记处理错误

```js
// 错误：没有错误处理
Promise.reject('错误');
// 会导致未捕获的错误警告

// 正确：添加错误处理
Promise.reject('错误')
    .catch(error => console.error(error));
```

### 错误 2：在 catch 中忘记处理

```js
// 错误：catch 中抛出错误但没有处理
promise
    .catch(error => {
        throw new Error('新错误');
    }); // 新错误没有被处理

// 正确：继续处理错误
promise
    .catch(error => {
        throw new Error('新错误');
    })
    .catch(error => {
        console.error(error);
    });
```

### 错误 3：在 finally 中抛出错误

```js
// 错误：finally 中抛出错误会覆盖原始错误
promise
    .then(value => {
        throw new Error('原始错误');
    })
    .finally(() => {
        throw new Error('finally 错误'); // 会覆盖原始错误
    })
    .catch(error => {
        // 只能捕获 finally 中的错误
    });
```

## 练习

1. **错误捕获**：创建一个 Promise 链，在中间抛出错误，使用 catch 捕获并处理错误。

2. **错误恢复**：创建一个 Promise，失败时返回默认值，让 Promise 链继续执行。

3. **重试机制**：实现一个带重试功能的 fetch 函数，失败时自动重试最多 3 次。

4. **错误分类**：创建不同类型的错误（网络错误、验证错误等），在 catch 中根据错误类型进行不同处理。

5. **全局错误处理**：设置全局的 Promise 错误处理，捕获所有未处理的 Promise 错误。

完成以上练习后，继续学习下一章，了解 async/await 的使用。

## 总结

Promise 的错误处理是异步编程的重要部分。通过 catch 方法可以捕获错误，错误会在链中向下传播，可以在 catch 中恢复或重新抛出错误。始终为 Promise 添加错误处理，避免未捕获的错误。根据实际需求选择合适的错误处理策略。

## 相关资源

- [MDN：Promise.catch()](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch)
- [JavaScript.info：Promise 错误处理](https://zh.javascript.info/promise-error-handling)
