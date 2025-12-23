# 7.7.3 BDD 实践

## 1. 概述

BDD 实践包括在实际项目中应用 BDD 方法，编写可执行的业务规范，促进业务和技术团队协作。

## 2. 实践场景

### 2.1 用户注册

```gherkin
Feature: 用户注册
  作为新用户
  我想要注册账户
  以便使用系统功能

  Scenario: 成功注册
    Given 用户访问注册页面
    When 用户输入有效的注册信息
      | 字段 | 值 |
      | 姓名 | John |
      | 邮箱 | john@example.com |
      | 密码 | password123 |
    And 点击注册按钮
    Then 用户应该成功注册
    And 应该收到确认邮件
    And 应该跳转到登录页面

  Scenario: 注册失败 - 邮箱已存在
    Given 用户 "john@example.com" 已注册
    When 用户尝试使用相同邮箱注册
    Then 应该显示错误消息 "邮箱已存在"
    And 用户应该停留在注册页面
```

### 2.2 步骤实现

```ts
import { Given, When, Then } from '@cucumber/cucumber';
import { page } from '../support/page';
import { db } from '../support/db';

Given('用户访问注册页面', async (): Promise<void> => {
  await page.goto('/register');
});

When('用户输入有效的注册信息', async (dataTable: any): Promise<void> => {
  const data = dataTable.hashes()[0];
  await page.fill('#name', data.姓名);
  await page.fill('#email', data.邮箱);
  await page.fill('#password', data.密码);
});

When('点击注册按钮', async (): Promise<void> => {
  await page.click('#register-button');
});

Then('用户应该成功注册', async (): Promise<void> => {
  await page.waitForURL('**/login');
  const user = await db.query('SELECT * FROM users WHERE email = $1', ['john@example.com']);
  expect(user.rows).toHaveLength(1);
});

Then('应该收到确认邮件', async (): Promise<void> => {
  // 验证邮件发送
  const emails = await getSentEmails();
  expect(emails).toContainEqual(
    expect.objectContaining({ to: 'john@example.com', subject: 'Welcome' })
  );
});
```

## 3. 数据驱动测试

### 3.1 场景大纲

```gherkin
Feature: 密码验证

  Scenario Outline: 密码强度验证
    Given 用户在注册页面
    When 用户输入密码 "<password>"
    Then 验证结果应该是 "<result>"

    Examples:
      | password      | result |
      | password123   | 通过   |
      | 123456        | 失败   |
      | abc           | 失败   |
      | Password123!  | 通过   |
```

### 3.2 步骤实现

```ts
When('用户输入密码 {string}', async (password: string): Promise<void> => {
  await page.fill('#password', password);
});

Then('验证结果应该是 {string}', async (expectedResult: string): Promise<void> => {
  const isValid = await page.locator('#password').evaluate((el: HTMLInputElement) => {
    return el.validity.valid;
  });
  
  if (expectedResult === '通过') {
    expect(isValid).toBe(true);
  } else {
    expect(isValid).toBe(false);
  }
});
```

## 4. 最佳实践

### 4.1 场景编写

- 使用自然语言
- 描述业务行为
- 保持场景简单
- 使用数据表格

### 4.2 步骤实现

- 实现步骤定义
- 保持步骤可复用
- 使用页面对象
- 组织步骤代码

### 4.3 团队协作

- 业务参与编写
- 统一语言
- 定期审查
- 持续改进

## 5. 注意事项

- **业务导向**：关注业务价值
- **自然语言**：使用自然语言
- **场景简单**：保持场景简单
- **团队协作**：促进团队协作

## 6. 常见问题

### 6.1 如何处理复杂业务规则？

将复杂规则分解为简单场景，使用场景大纲。

### 6.2 如何保持场景可维护？

使用页面对象，保持步骤可复用，定期重构。

### 6.3 如何促进业务参与？

使用自然语言，组织协作会议，提供培训。

## 7. 实践任务

1. **编写场景**：编写业务场景
2. **实现步骤**：实现步骤定义
3. **数据驱动**：使用数据驱动测试
4. **团队协作**：促进团队协作
5. **持续改进**：持续改进 BDD 实践

---

**下一章**：[7.8 性能测试](../chapter-08-performance/readme.md)
