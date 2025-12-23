# 7.4.2 Playwright

## 1. 概述

Playwright 是 Microsoft 开发的 E2E 测试框架，支持多浏览器（Chromium、Firefox、WebKit），提供了现代化的 API 和强大的调试功能。

## 2. 特性说明

- **多浏览器**：支持 Chromium、Firefox、WebKit
- **快速执行**：并行执行，速度快
- **现代化 API**：简洁的 API 设计
- **强大调试**：强大的调试和追踪功能

## 3. 安装与配置

### 3.1 安装

```bash
npm install -D @playwright/test
npx playwright install
```

### 3.2 配置文件

```ts
// playwright.config.ts
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests/e2e',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: 'html',
  use: {
    baseURL: 'http://localhost:3000',
    trace: 'on-first-retry'
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] }
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] }
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] }
    }
  ],
  webServer: {
    command: 'npm run dev',
    url: 'http://localhost:3000',
    reuseExistingServer: !process.env.CI
  }
});
```

## 4. 基本使用

### 4.1 测试文件

```ts
// tests/e2e/login.spec.ts
import { test, expect } from '@playwright/test';

test('user can login', async ({ page }): Promise<void> => {
  await page.goto('/login');
  
  await page.fill('#email', 'user@example.com');
  await page.fill('#password', 'password123');
  await page.click('#login-button');
  
  await expect(page).toHaveURL('/dashboard');
  await expect(page.locator('h1')).toContainText('Dashboard');
});
```

### 4.2 运行测试

```bash
# 运行所有测试
npx playwright test

# 运行特定测试
npx playwright test login

# 调试模式
npx playwright test --debug

# UI 模式
npx playwright test --ui
```

## 5. 高级特性

### 5.1 等待机制

```ts
test('should wait for element', async ({ page }): Promise<void> => {
  await page.goto('/');
  
  // 等待元素可见
  await page.waitForSelector('#content', { state: 'visible' });
  
  // 等待网络请求完成
  await page.waitForLoadState('networkidle');
  
  // 等待特定条件
  await page.waitForFunction(() => {
    return document.querySelector('#content')?.textContent?.includes('Loaded');
  });
});
```

### 5.2 页面对象模式

```ts
// pages/LoginPage.ts
export class LoginPage {
  constructor(private page: any) {}
  
  async goto(): Promise<void> {
    await this.page.goto('/login');
  }
  
  async login(email: string, password: string): Promise<void> {
    await this.page.fill('#email', email);
    await this.page.fill('#password', password);
    await this.page.click('#login-button');
  }
  
  async isLoggedIn(): Promise<boolean> {
    return await this.page.locator('#user-menu').isVisible();
  }
}

// 使用
test('user can login', async ({ page }): Promise<void> => {
  const loginPage = new LoginPage(page);
  await loginPage.goto();
  await loginPage.login('user@example.com', 'password123');
  expect(await loginPage.isLoggedIn()).toBe(true);
});
```

### 5.3 截图和视频

```ts
test('should capture screenshot', async ({ page }): Promise<void> => {
  await page.goto('/');
  await page.screenshot({ path: 'screenshot.png', fullPage: true });
});

// 配置自动截图
export default defineConfig({
  use: {
    screenshot: 'only-on-failure',
    video: 'retain-on-failure'
  }
});
```

## 6. 最佳实践

### 6.1 测试组织

- 使用页面对象模式
- 保持测试独立
- 使用描述性名称
- 组织测试结构

### 6.2 稳定性

- 使用等待机制
- 避免硬编码等待
- 处理异步操作
- 使用重试机制

## 7. 注意事项

- **等待机制**：正确使用等待机制
- **测试速度**：优化测试执行速度
- **浏览器支持**：根据需求选择浏览器
- **测试维护**：及时维护测试代码

## 8. 常见问题

### 8.1 如何处理异步操作？

使用 Playwright 的等待机制，如 `waitForSelector`、`waitForLoadState`。

### 8.2 如何调试测试？

使用 `--debug` 模式或 `--ui` 模式进行调试。

### 8.3 如何优化测试速度？

并行执行、使用无头模式、优化等待机制。

## 9. 实践任务

1. **安装配置**：安装和配置 Playwright
2. **编写测试**：编写 E2E 测试
3. **页面对象**：使用页面对象模式
4. **等待机制**：使用等待机制
5. **调试测试**：调试和优化测试

---

**下一节**：[7.4.3 Cypress](section-03-cypress.md)
