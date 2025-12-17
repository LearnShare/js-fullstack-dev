# 2.11.2 try...catch...finally

## 概述

`try...catch...finally` 提供同步/异步（结合 async/await）异常捕获能力。合理使用能防止程序崩溃，提供优雅的降级与清理。本节涵盖语法、error 对象、常见模式、异步场景、重新抛出、资源清理与最佳实践。

## 基本语法

### try...catch

```js
try {
  // 可能出错的代码
  riskyOperation();
} catch (error) {
  console.error('Error:', error.message);
}
```

### try...catch...finally

```js
try {
  riskyOperation();
} catch (error) {
  console.error('Error:', error.message);
} finally {
  cleanup(); // 无论是否出错都会执行
}
```

### catch 省略 error 绑定（ES2019）
```js
try {
  riskyOperation();
} catch {
  console.error('Error occurred');
}
```

## error 对象

- `name`：错误名称（TypeError/ReferenceError/自定义）
- `message`：错误信息
- `stack`：堆栈（实现相关）
- 自定义字段：可在业务错误中添加 `code`、`status`、`field` 等。

```js
try {
  throw new Error('Something went wrong');
} catch (error) {
  console.log(error.name);    // Error
  console.log(error.message); // Something went wrong
  console.log(error.stack);   // 调用栈
}
```

## 异步中的异常处理

### Promise 链
```js
doAsync()
  .then(handleResult)
  .catch(err => {
    console.error(err);
  });
```

### async/await + try...catch
```js
async function load() {
  try {
    const data = await fetchData();
    return data;
  } catch (err) {
    console.error('fetch failed', err);
    return null; // 降级返回
  }
}
```

### 并行 Promise 处理
```js
async function loadAll() {
  try {
    const [a, b] = await Promise.all([fetchA(), fetchB()]);
    return { a, b };
  } catch (err) {
    // 任一失败都会进入这里
    console.error('one failed', err);
    throw err;
  }
}
```

### Promise.any/AggregateError
```js
try {
  const val = await Promise.any([p1, p2]);
  console.log(val);
} catch (err) {
  if (err instanceof AggregateError) {
    err.errors.forEach(e => console.error(e.message));
  }
}
```

## 重新抛出与错误封装

### 重新抛出（保留语义）
```js
try {
  doWork();
} catch (err) {
  log(err);
  throw err; // 让上层感知
}
```

### 包装为业务错误
```js
class ServiceError extends Error {
  constructor(message, cause) {
    super(message);
    this.name = 'ServiceError';
    this.cause = cause;
  }
}

try {
  await callApi();
} catch (err) {
  throw new ServiceError('API failed', err);
}
```

## 资源清理与 finally

- 用于关闭连接、释放锁、恢复状态、清理定时器。
- 在 async 函数中，`finally` 同样适用。

```js
async function withConn() {
  const conn = await openConnection();
  try {
    return await conn.query('SELECT 1');
  } finally {
    conn.close(); // 确保被执行
  }
}
```

## 常见模式

### 1) 防御性解析
```js
function safeParse(json) {
  try { return JSON.parse(json); }
  catch { return null; }
}
```

### 2) 降级返回
```js
async function getProfile() {
  try {
    return await fetchProfile();
  } catch (err) {
    return { name: 'Guest' }; // 合理的降级
  }
}
```

### 3) 兜底日志 + 报警
```js
try {
  risky();
} catch (err) {
  console.error(err);
  report(err); // 上报监控
}
```

### 4) 边界校验
```js
function divide(a, b) {
  if (b === 0) throw new RangeError('b cannot be 0');
  return a / b;
}
```

### 5) 分支捕获
```js
try {
  task();
} catch (err) {
  if (err instanceof ValidationError) handleValidation(err);
  else if (err instanceof TypeError) handleType(err);
  else throw err; // 未知错误向上抛
}
``}

## 常见陷阱

- **吞掉错误不处理**：空 catch 导致问题被隐藏。应记录或重新抛出。  
- **Promise 未处理拒绝**：缺少 `.catch` 或 try...catch；Node 会产生 UnhandledRejection。  
- **finally 覆盖返回值**：`finally` 返回值会覆盖 try/catch 的返回，谨慎使用。  
- **同步/异步混用**：`try...catch` 只能捕获同步和 await 的异常，不能捕获未 await 的异步错误。  

示例——finally 覆盖返回：
```js
function demo() {
  try { return 1; }
  finally { return 2; } // 覆盖为 2，通常不建议
}
```

## 最佳实践

1) 只捕获可恢复或需要降级的错误；未知错误让上层或全局处理。  
2) catch 中区分错误类型，给出针对性恢复或提示。  
3) 记录上下文：输入参数、用户信息、环境、traceId，便于排查。  
4) async/await 保持对称的 try...catch；并行任务用 Promise.all/any 包裹整体。  
5) finally 做幂等的清理操作，避免改变主逻辑返回值。  
6) 与监控平台结合（Sentry/自建），配合 Source Map。  

## 练习

1. 写一个 `safeFetch(url)`：失败时返回 `{ ok:false, error }`，成功返回 `{ ok:true, data }`。  
2. 用 `Promise.any` + try...catch 处理全部失败的情况，打印 AggregateError 中的所有 message。  
3. 演示 finally 覆盖返回值的例子，并改写为不覆盖的写法。  
4. 编写一个带 `cause` 的业务错误包装器，并在 catch 中重新抛出。  
5. 在 async 函数中忘记 await 一个 Promise，观察 try...catch 是否捕获，解释原因。  

## 小结

- `try...catch...finally` 是同步与 async/await 异步的核心错误处理手段。  
- catch 中应分类处理、记录上下文，必要时重新抛出或包装。  
- finally 负责清理且应避免篡改主逻辑返回值。  
- 异步链路确保每个 Promise 有对应的错误处理，避免未处理拒绝。  

继续学习下一节，了解自定义错误的定义与使用。
