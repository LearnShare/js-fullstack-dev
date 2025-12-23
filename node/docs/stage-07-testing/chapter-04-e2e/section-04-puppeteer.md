# 7.4.4 Puppeteer

## 1. 概述

Puppeteer 是 Google 开发的 Node.js 库，用于控制 Chrome 或 Chromium 浏览器。Puppeteer 提供了强大的浏览器控制能力，适合自动化测试和爬虫。

## 2. 特性说明

- **Chrome 专用**：支持 Chrome/Chromium
- **强大控制**：强大的浏览器控制能力
- **适合自动化**：适合自动化任务
- **性能优秀**：执行性能优秀

## 3. 安装与配置

### 3.1 安装

```bash
npm install puppeteer
npm install -D @types/puppeteer
```

### 3.2 基本使用

```ts
import puppeteer, { Browser, Page } from 'puppeteer';

async function runTest(): Promise<void> {
  const browser: Browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  
  const page: Page = await browser.newPage();
  await page.goto('http://localhost:3000');
  
  // 测试操作
  await page.click('#login-button');
  
  await browser.close();
}
```

## 4. 基本操作

### 4.1 页面导航

```ts
const page: Page = await browser.newPage();

// 访问页面
await page.goto('http://localhost:3000');

// 等待导航
await page.goto('http://localhost:3000', { waitUntil: 'networkidle0' });

// 返回上一页
await page.goBack();

// 前进下一页
await page.goForward();
```

### 4.2 元素操作

```ts
// 点击元素
await page.click('#button');

// 输入文本
await page.type('#input', 'text');

// 选择选项
await page.select('#select', 'option-value');

// 上传文件
const input = await page.$('input[type="file"]');
if (input) {
  await input.uploadFile('/path/to/file');
}
```

### 4.3 等待机制

```ts
// 等待元素出现
await page.waitForSelector('#content');

// 等待函数返回 true
await page.waitForFunction(() => {
  return document.querySelector('#content')?.textContent?.includes('Loaded');
});

// 等待网络请求
await page.waitForResponse(response => response.url().includes('/api/users'));

// 等待导航
await page.waitForNavigation();
```

## 5. 测试示例

### 5.1 登录测试

```ts
import { describe, it, expect, beforeAll, afterAll } from 'vitest';
import puppeteer, { Browser, Page } from 'puppeteer';

describe('Login E2E', () => {
  let browser: Browser;
  let page: Page;
  
  beforeAll(async (): Promise<void> => {
    browser = await puppeteer.launch({ headless: true });
    page = await browser.newPage();
  });
  
  afterAll(async (): Promise<void> => {
    await browser.close();
  });
  
  it('should login successfully', async (): Promise<void> => {
    await page.goto('http://localhost:3000/login');
    
    await page.type('#email', 'user@example.com');
    await page.type('#password', 'password123');
    await page.click('#login-button');
    
    await page.waitForNavigation();
    
    const url = page.url();
    expect(url).toContain('/dashboard');
    
    const heading = await page.$eval('h1', (el: HTMLElement) => el.textContent);
    expect(heading).toContain('Dashboard');
  });
});
```

### 5.2 截图和 PDF

```ts
// 截图
await page.screenshot({ path: 'screenshot.png', fullPage: true });

// PDF
await page.pdf({ path: 'page.pdf', format: 'A4' });
```

### 5.3 网络拦截

```ts
await page.setRequestInterception(true);

page.on('request', (request) => {
  if (request.url().includes('/api/users')) {
    request.respond({
      status: 200,
      contentType: 'application/json',
      body: JSON.stringify([{ id: 1, name: 'John' }])
    });
  } else {
    request.continue();
  }
});
```

## 6. 最佳实践

### 6.1 测试组织

- 使用测试框架集成
- 保持测试独立
- 使用页面对象模式
- 组织测试结构

### 6.2 性能优化

- 使用无头模式
- 复用浏览器实例
- 优化等待机制
- 并行执行

## 7. 注意事项

- **浏览器版本**：注意 Puppeteer 和 Chrome 版本匹配
- **等待机制**：正确使用等待机制
- **资源管理**：及时关闭浏览器和页面
- **测试维护**：及时维护测试代码

## 8. 常见问题

### 8.1 如何处理异步操作？

使用 Puppeteer 的等待机制，如 `waitForSelector`、`waitForFunction`。

### 8.2 如何调试测试？

使用 `headless: false` 查看浏览器操作。

### 8.3 如何优化测试速度？

使用无头模式、复用浏览器实例、优化等待机制。

## 9. 实践任务

1. **安装配置**：安装和配置 Puppeteer
2. **编写测试**：编写 E2E 测试
3. **页面操作**：进行页面操作
4. **等待机制**：使用等待机制
5. **性能优化**：优化测试性能

---

**下一章**：[7.5 Mock 与 Stub](../chapter-05-mocking/readme.md)
