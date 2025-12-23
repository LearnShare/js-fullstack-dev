# 7.7.2 BDD 工具（Cucumber、Jest-Cucumber）

## 1. 概述

BDD 工具用于将自然语言场景转化为可执行的测试。Cucumber 和 Jest-Cucumber 是常用的 BDD 工具，支持 Gherkin 语法。

## 2. Cucumber

### 2.1 安装

```bash
npm install -D @cucumber/cucumber
```

### 2.2 特性文件

```gherkin
# features/login.feature
Feature: 用户登录
  作为用户
  我想要登录系统
  以便访问我的账户

  Scenario: 成功登录
    Given 用户已注册，邮箱为 "user@example.com"
    When 用户输入邮箱 "user@example.com" 和密码 "password123"
    And 点击登录按钮
    Then 用户应该成功登录
    And 应该跳转到 "/dashboard" 页面
```

### 2.3 步骤定义

```ts
// features/step_definitions/login.steps.ts
import { Given, When, Then } from '@cucumber/cucumber';
import { expect } from 'chai';
import { page } from '../support/page';

Given('用户已注册，邮箱为 {string}', async (email: string): Promise<void> => {
  // 准备测试数据
  await createTestUser({ email, password: 'password123' });
});

When('用户输入邮箱 {string} 和密码 {string}', async (email: string, password: string): Promise<void> => {
  await page.fill('#email', email);
  await page.fill('#password', password);
});

When('点击登录按钮', async (): Promise<void> => {
  await page.click('#login-button');
});

Then('用户应该成功登录', async (): Promise<void> => {
  await page.waitForURL('**/dashboard');
  const isLoggedIn = await page.locator('#user-menu').isVisible();
  expect(isLoggedIn).to.be.true;
});

Then('应该跳转到 {string} 页面', async (path: string): Promise<void> => {
  await expect(page).toHaveURL(new RegExp(path));
});
```

### 2.4 运行测试

```bash
npx cucumber-js
```

## 3. Jest-Cucumber

### 3.1 安装

```bash
npm install -D jest-cucumber
```

### 3.2 特性文件

```gherkin
# features/login.feature
Feature: 用户登录

  Scenario: 成功登录
    Given 用户已注册
    When 用户输入正确的邮箱和密码
    Then 用户应该成功登录
```

### 3.3 步骤定义

```ts
// features/login.steps.ts
import { loadFeature, defineFeature, DefineStepFunction } from 'jest-cucumber';
import { UserService } from '../src/user-service';

const feature = loadFeature('./features/login.feature');

defineFeature(feature, (test) => {
  let userService: UserService;
  let result: any;
  
  test('成功登录', ({ given, when, then }: { given: DefineStepFunction; when: DefineStepFunction; then: DefineStepFunction }) => {
    given('用户已注册', () => {
      userService = new UserService();
      userService.createUser({ email: 'user@example.com', password: 'password123' });
    });
    
    when('用户输入正确的邮箱和密码', async () => {
      result = await userService.login('user@example.com', 'password123');
    });
    
    then('用户应该成功登录', () => {
      expect(result.success).toBe(true);
      expect(result.user).toBeDefined();
    });
  });
});
```

## 4. 最佳实践

### 4.1 场景编写

- 使用自然语言
- 描述业务行为
- 保持场景简单
- 使用 Given-When-Then

### 4.2 步骤实现

- 实现步骤定义
- 保持步骤可复用
- 使用页面对象
- 组织步骤代码

## 5. 注意事项

- **业务导向**：关注业务价值
- **自然语言**：使用自然语言
- **场景简单**：保持场景简单
- **工具选择**：根据项目需求选择工具

## 6. 常见问题

### 6.1 如何选择 BDD 工具？

根据项目需求、团队经验、工具特性选择。

### 6.2 如何处理复杂场景？

将复杂场景分解为简单场景，逐步实现。

### 6.3 如何保持场景可读性？

使用自然语言，避免技术术语，保持场景简单。

## 7. 实践任务

1. **安装工具**：安装 BDD 工具
2. **编写场景**：编写 Gherkin 场景
3. **实现步骤**：实现步骤定义
4. **运行测试**：运行 BDD 测试
5. **最佳实践**：遵循 BDD 最佳实践

---

**下一节**：[7.7.3 BDD 实践](section-03-practice.md)
