# 4.14.2 Postman

## 1. 概述

Postman 是一个功能强大的 API 测试工具，提供了图形化界面、团队协作、测试自动化等功能。Postman 广泛应用于 API 开发、测试和文档生成。

## 2. 特性说明

- **图形化界面**：直观的图形化界面
- **团队协作**：支持团队协作和共享
- **测试自动化**：支持测试脚本和自动化
- **文档生成**：自动生成 API 文档
- **环境管理**：支持多环境配置

## 3. 基本使用

### 3.1 创建请求

```
1. 选择 HTTP 方法（GET、POST 等）
2. 输入 URL
3. 配置请求头
4. 配置请求体（如需要）
5. 发送请求
```

### 3.2 查看响应

```
响应包含：
- 状态码
- 响应头
- 响应体
- 响应时间
```

## 4. 环境变量

### 4.1 创建环境

```
1. 创建新环境
2. 定义环境变量
3. 选择环境
4. 在请求中使用变量
```

### 4.2 使用变量

```http
GET {{baseUrl}}/api/users
Authorization: Bearer {{token}}
```

## 5. 集合和文件夹

### 5.1 创建集合

```
1. 创建新集合
2. 添加请求到集合
3. 使用文件夹组织请求
4. 添加集合描述
```

### 5.2 集合变量

```
集合变量可以在集合内所有请求中使用：
{{collectionVariable}}
```

## 6. 测试脚本

### 6.1 基本测试

```javascript
// 测试响应状态码
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

// 测试响应体
pm.test("Response has users array", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property('users');
    pm.expect(jsonData.users).to.be.an('array');
});
```

### 6.2 高级测试

```javascript
// 测试响应时间
pm.test("Response time is less than 500ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(500);
});

// 测试响应头
pm.test("Content-Type is application/json", function () {
    pm.response.to.have.header("Content-Type", "application/json");
});

// 保存响应数据
pm.test("Save user ID", function () {
    const jsonData = pm.response.json();
    pm.environment.set("userId", jsonData.user.id);
});
```

## 7. 预请求脚本

### 7.1 动态变量

```javascript
// 生成时间戳
pm.environment.set("timestamp", Date.now());

// 生成随机数
pm.environment.set("randomId", Math.floor(Math.random() * 1000));

// 生成签名
const crypto = require('crypto-js');
const signature = crypto.HmacSHA256(data, secret).toString();
pm.environment.set("signature", signature);
```

## 8. 团队协作

### 8.1 共享集合

```
1. 创建团队工作区
2. 共享集合到工作区
3. 团队成员访问集合
4. 协作编辑和测试
```

### 8.2 版本控制

```
1. 创建集合版本
2. 查看版本历史
3. 回滚到旧版本
4. 合并变更
```

## 9. API 文档

### 9.1 自动生成文档

```
1. 为请求添加描述
2. 添加参数说明
3. 添加示例
4. 发布文档
```

### 9.2 文档示例

```markdown
## 获取用户列表

获取系统中的所有用户列表。

### 请求参数

- `page` (可选): 页码，默认为 1
- `limit` (可选): 每页数量，默认为 10

### 响应示例

```json
{
  "users": [],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 0
  }
}
```
```

## 10. 最佳实践

### 10.1 组织管理

- 使用集合组织请求
- 使用文件夹分类
- 添加描述和标签

### 10.2 环境管理

- 为每个环境创建配置
- 使用环境变量
- 保护敏感信息

### 10.3 测试自动化

- 编写测试脚本
- 使用断言验证
- 实现测试报告

## 11. 注意事项

- **安全性**：保护 API 密钥和敏感信息
- **版本控制**：使用版本控制管理集合
- **文档化**：文档化 API 和测试用例
- **维护性**：保持测试用例更新

## 12. 常见问题

### 12.1 如何管理多个环境？

为每个环境创建环境配置，使用环境变量管理不同环境的参数。

### 12.2 如何实现测试自动化？

使用测试脚本和断言，集成到 CI/CD 流程。

### 12.3 如何共享集合？

创建团队工作区，共享集合到工作区。

## 13. 实践任务

1. **创建请求集合**：创建 API 请求集合
2. **配置环境**：配置开发、测试、生产环境
3. **编写测试脚本**：编写 API 测试脚本
4. **实现测试自动化**：实现测试自动化流程
5. **生成 API 文档**：使用 Postman 生成 API 文档

---

**下一节**：[4.14.3 Insomnia](section-03-insomnia.md)
