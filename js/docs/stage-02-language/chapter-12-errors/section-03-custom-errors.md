# 2.12.3 自定义错�?

## 概述

自定义错误让业务语义更清晰，便于分类处理、日志筛选与用户提示。常见场景：校验失败、权限不足、外部服务异常、限流、超时。通过继承 `Error`（或子类）并添加字段（code、status、field、cause）可构建可观测、可恢复的错误体系�?

## 基本语法

```js
class CustomError extends Error {
  constructor(message, code) {
    super(message);
    this.name = 'CustomError';
    this.code = code;
  }
}

throw new CustomError('Custom error message', 'CUSTOM_CODE');
```

- 继承链：`CustomError` �?`Error`
- `name`：便于日志过�?
- `code`：机器可读的错误�?

## 结构化错误：常用字段

- `name`：错误名�?
- `message`：人类可�?
- `code`：业�?系统错误码（�?`VALIDATION_ERROR`、`AUTH_DENIED`�?
- `status`：HTTP 状态码（如 400/401/429/500�?
- `field`：校验相关字�?
- `cause`：根因（ES2022 原生支持�?

### 使用 cause

```js
try {
  await callApi();
} catch (err) {
  throw new Error('Service failed', { cause: err });
}
```

## 业务错误示例

### ValidationError
```js
class ValidationError extends Error {
  constructor(field, message) {
    super(`Invalid ${field}: ${message}`);
    this.name = 'ValidationError';
    this.code = 'VALIDATION_ERROR';
    this.field = field;
  }
}

function validateUser(user) {
  if (!user.name) throw new ValidationError('name', 'required');
  if (!user.email) throw new ValidationError('email', 'required');
}
```

### AuthError
```js
class AuthError extends Error {
  constructor(message = 'Unauthorized') {
    super(message);
    this.name = 'AuthError';
    this.code = 'AUTH_DENIED';
    this.status = 401;
  }
}
```

### RateLimitError
```js
class RateLimitError extends Error {
  constructor(limit, resetAt) {
    super(`Rate limit exceeded: ${limit}`);
    this.name = 'RateLimitError';
    this.code = 'RATE_LIMIT';
    this.status = 429;
    this.limit = limit;
    this.resetAt = resetAt;
  }
}
```

## 前端应用中的自定义错�?

### 区分可提示与需上报
```js
class UserFriendlyError extends Error {
  constructor(message, options = {}) {
    super(message);
    this.name = 'UserFriendlyError';
    this.userMessage = options.userMessage || '操作失败，请稍后重试';
    this.report = options.report ?? true; // 是否上报
  }
}

function showError(err) {
  alert(err.userMessage || '出错�?);
  if (err.report !== false) report(err);
}
```

### 包装外部服务错误
```js
class ApiError extends Error {
  constructor(message, status, response, cause) {
    super(message, { cause });
    this.name = 'ApiError';
    this.status = status;
    this.response = response;
  }
}

async function fetchJson(url) {
  const res = await fetch(url);
  if (!res.ok) {
    const body = await res.text().catch(() => '');
    throw new ApiError(`Request failed: ${res.status}`, res.status, body);
  }
  return res.json();
}
```

## �?Promise/async 搭配

```js
async function loadProfile() {
  try {
    return await fetchJson('/api/profile');
  } catch (err) {
    if (err instanceof ApiError && err.status === 401) {
      throw new AuthError('登录已过�?);
    }
    throw err; // 未知错误上抛
  }
}
```

## 日志与监�?

- 记录 `name`、`code`、`status`、`message`、`stack`、`cause`�?
- 避免向用户泄露敏感栈信息；仅上报到监控平台（Sentry/自建）�?
- 结合 Source Map 还原压缩代码栈�?

## 序列化与传输

原生 Error 不可直接 JSON 序列化，需自定�?toJSON�?

```js
class SerializableError extends Error {
  constructor(message, code) {
    super(message);
    this.name = 'SerializableError';
    this.code = code;
  }
  toJSON() {
    return { name: this.name, message: this.message, code: this.code };
  }
}
```

## 常见陷阱

- 继承 Error 时忘�?`super(message)`，导�?message/stack 丢失�? 
- 覆盖 `name` 但未设置 `this.name`，影响日志筛选�? 
- 重新抛出时丢失原始错误：可用 `cause` 或自定义 `originalError`�? 
- 直接向用户暴露后端栈信息：注意脱敏与友好提示�? 

## 最佳实�?

1) 为可预期的业务场景定义语义化错误类（验证/权限/限流/超时）�? 
2) 添加结构化字段（code/status/field/cause），方便监控和分流处理�? 
3) �?`cause` 传递根因，保留完整链路�? 
4) 前端提示与日志上报分离：对用户友好提示，对监控保留详情�? 
5) 序列化前显式挑选字段，避免敏感信息泄露�? 
6) 在测试中断言错误类型�?code，确保行为稳定�? 

## 练习

1. 定义 `ValidationError`、`AuthError`，在表单与鉴权流程中抛出并分类处理�? 
2. �?API 调用封装 `ApiError`，包�?status、响应体、cause，并在上层转换为用户友好提示�? 
3. 实现 `SerializableError` �?`toJSON`，并在前后端通信中传递�? 
4. 将底层第三方库错误包装为业务错误，同时保留原�?`cause`�? 
5. 在测试中模拟抛出自定义错误，断言 `name/code/status`，确保契约不破坏�? 

## 小结

- 自定义错误通过继承 Error 并添加结构化字段，使错误语义清晰、可观测、可分流�? 
- 使用 `cause` 保留根因；用 `code/status` 支撑自动化处理；�?`userMessage` 支撑友好提示�? 
- 结合监控上报与测试断言，构建稳健的错误处理体系�? 

完成本章学习后，继续学习下一章：JavaScript 版本新特性�?
