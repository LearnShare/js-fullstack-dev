# 3.7.2 爬虫开发

## 1. 概述

网络爬虫是 Node.js 的另一个重要应用领域。通过爬虫，可以自动化地从网页中提取数据、监控网站变化、进行数据分析等。Node.js 的异步特性和丰富的 HTTP 客户端库使其成为构建爬虫的理想选择。

## 2. 特性说明

- **HTTP 请求**：发送 HTTP 请求获取网页内容。
- **HTML 解析**：解析 HTML 文档，提取所需数据。
- **并发控制**：控制并发请求数量，避免过载。
- **数据存储**：将提取的数据保存到文件或数据库。
- **反爬虫应对**：处理验证码、登录、代理等反爬虫机制。

## 3. 主流工具概览

### Cheerio

服务端 jQuery 实现，用于解析 HTML。

**特点**：
- 类似 jQuery 的 API
- 快速且轻量
- 支持 CSS 选择器
- 服务端 DOM 操作

**安装**：
```bash
npm install cheerio
```

**基本用法**：
```ts
// 文件: crawler-cheerio.ts
// 功能: Cheerio 基本用法

import * as cheerio from 'cheerio';

const html = `
<html>
  <body>
    <h1>Title</h1>
    <p class="content">Content here</p>
  </body>
</html>
`;

const $ = cheerio.load(html);
const title = $('h1').text();
const content = $('.content').text();

console.log('Title:', title);
console.log('Content:', content);
```

### Puppeteer

无头浏览器，支持 JavaScript 渲染。

**特点**：
- 完整的浏览器环境
- 支持 JavaScript 渲染
- 可以处理动态内容
- 支持截图和 PDF 生成

**安装**：
```bash
npm install puppeteer
```

**基本用法**：
```ts
// 文件: crawler-puppeteer.ts
// 功能: Puppeteer 基本用法

import puppeteer from 'puppeteer';

async function crawlWithPuppeteer() {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    
    await page.goto('https://example.com');
    
    const title = await page.title();
    const content = await page.$eval('h1', el => el.textContent);
    
    console.log('Title:', title);
    console.log('Content:', content);
    
    await browser.close();
}

crawlWithPuppeteer();
```

### Playwright

现代化的浏览器自动化工具。

**特点**：
- 支持多浏览器（Chromium、Firefox、WebKit）
- 更快的执行速度
- 更好的 API 设计
- 自动等待机制

**安装**：
```bash
npm install playwright
```

**基本用法**：
```ts
// 文件: crawler-playwright.ts
// 功能: Playwright 基本用法

import { chromium } from 'playwright';

async function crawlWithPlaywright() {
    const browser = await chromium.launch();
    const page = await browser.newPage();
    
    await page.goto('https://example.com');
    
    const title = await page.title();
    const content = await page.textContent('h1');
    
    console.log('Title:', title);
    console.log('Content:', content);
    
    await browser.close();
}

crawlWithPlaywright();
```

### Axios / Fetch

HTTP 客户端，用于发送请求。

**特点**：
- 简单易用
- Promise 支持
- 请求拦截和响应拦截
- 自动 JSON 解析

**基本用法**：
```ts
// 文件: crawler-http.ts
// 功能: HTTP 请求基本用法

import axios from 'axios';

async function fetchPage() {
    const response = await axios.get('https://example.com');
    return response.data;
}

// 或使用原生 fetch
async function fetchWithFetch() {
    const response = await fetch('https://example.com');
    return await response.text();
}
```

## 4. 代码示例：完整爬虫示例

以下示例演示了如何构建一个完整的爬虫：

```ts
// 文件: complete-crawler.ts
// 功能: 完整的爬虫示例

import axios from 'axios';
import * as cheerio from 'cheerio';
import fsPromises from 'node:fs/promises';

interface Article {
    title: string;
    link: string;
    summary: string;
}

async function crawlArticles(url: string): Promise<Article[]> {
    // 1. 获取网页内容
    const response = await axios.get(url);
    const html = response.data;
    
    // 2. 解析 HTML
    const $ = cheerio.load(html);
    const articles: Article[] = [];
    
    // 3. 提取数据
    $('.article').each((index, element) => {
        const title = $(element).find('h2').text().trim();
        const link = $(element).find('a').attr('href') || '';
        const summary = $(element).find('.summary').text().trim();
        
        articles.push({ title, link, summary });
    });
    
    return articles;
}

async function saveArticles(articles: Article[], filename: string) {
    const json = JSON.stringify(articles, null, 2);
    await fsPromises.writeFile(filename, json, 'utf8');
}

// 使用
async function main() {
    const articles = await crawlArticles('https://example.com/articles');
    await saveArticles(articles, 'articles.json');
    console.log(`Crawled ${articles.length} articles`);
}

main();
```

## 5. 参数说明：爬虫常用参数

| 参数类型     | 说明                                     | 示例                           |
|:-------------|:-----------------------------------------|:-------------------------------|
| **URL**      | 要爬取的网页地址                          | `'https://example.com'`        |
| **选择器**   | CSS 选择器，用于定位元素                  | `'.article h2'`                |
| **并发数**   | 同时进行的请求数量                        | `5`                            |
| **延迟**     | 请求之间的延迟时间（毫秒）                | `1000`                         |

## 6. 返回值与状态说明

爬虫操作的返回结果：

| 返回类型     | 说明                                     |
|:-------------|:-----------------------------------------|
| **数据数组** | 提取的数据数组                            |
| **HTML 字符串**| 原始 HTML 内容                          |
| **错误对象** | 请求失败时的错误信息                      |

## 7. 输出结果说明

爬虫的输出示例：

```text
Crawled 10 articles
Saved to articles.json
```

**逻辑解析**：
- 发送 HTTP 请求获取网页
- 使用 Cheerio 解析 HTML
- 提取所需数据
- 保存到文件

## 8. 使用场景

### 1. 数据采集

从网站采集数据：

```ts
// 数据采集示例
async function collectData() {
    const data = await crawlArticles('https://example.com');
    await saveToDatabase(data);
}
```

### 2. 内容监控

监控网站内容变化：

```ts
// 内容监控示例
async function monitorContent() {
    const current = await fetchContent();
    const previous = await loadPrevious();
    
    if (current !== previous) {
        await notifyChange();
        await saveCurrent(current);
    }
}
```

### 3. 价格监控

监控商品价格变化：

```ts
// 价格监控示例
async function monitorPrice(url: string) {
    const price = await extractPrice(url);
    const previousPrice = await getPreviousPrice(url);
    
    if (price < previousPrice) {
        await sendPriceAlert(price);
    }
}
```

## 9. 注意事项与常见错误

- **遵守 robots.txt**：遵守网站的爬虫协议
- **请求频率**：控制请求频率，避免对服务器造成压力
- **错误处理**：处理网络错误和解析错误
- **数据验证**：验证提取的数据格式和内容
- **法律合规**：确保爬虫行为符合法律法规

## 10. 常见问题 (FAQ)

**Q: 如何处理需要登录的网站？**
A: 使用 Puppeteer 或 Playwright 模拟登录，或使用 Cookie 和 Session。

**Q: 如何应对反爬虫机制？**
A: 使用代理、设置 User-Agent、添加延迟、使用无头浏览器等。

**Q: 如何提高爬虫效率？**
A: 使用并发请求、合理控制并发数、使用缓存、优化选择器。

## 11. 最佳实践

- **遵守规则**：遵守网站的 robots.txt 和使用条款
- **控制频率**：合理控制请求频率，避免过载
- **错误处理**：完善的错误处理和重试机制
- **数据验证**：验证提取的数据
- **使用缓存**：缓存已爬取的数据，避免重复请求

## 12. 对比分析：爬虫工具选择

| 工具           | 特点                                     | 适用场景                       |
|:---------------|:-----------------------------------------|:-------------------------------|
| **Cheerio**    | 轻量快速，适合静态 HTML                  | 简单网页数据提取                |
| **Puppeteer**  | 完整浏览器环境，支持 JS 渲染              | 动态内容、需要交互的页面        |
| **Playwright** | 多浏览器支持，现代化 API                  | 复杂爬虫、多浏览器测试          |
| **Axios/Fetch**| 简单 HTTP 请求                           | 简单的 API 调用                |

## 13. 练习任务

1. **简单爬虫实践**：
   - 使用 Cheerio 提取网页数据
   - 使用 Axios 发送 HTTP 请求
   - 保存提取的数据

2. **动态内容爬取**：
   - 使用 Puppeteer 爬取动态内容
   - 处理 JavaScript 渲染的页面
   - 实现页面交互

3. **并发控制实践**：
   - 实现并发请求控制
   - 添加请求延迟
   - 处理请求失败和重试

4. **实际应用**：
   - 创建实际的数据采集工具
   - 实现内容监控功能
   - 遵守爬虫最佳实践

完成以上练习后，继续学习下一节：自动化脚本。

## 总结

爬虫开发是 Node.js 的重要应用领域：

- **主流工具**：Cheerio、Puppeteer、Playwright、Axios
- **核心功能**：HTTP 请求、HTML 解析、数据提取、并发控制
- **最佳实践**：遵守规则、控制频率、错误处理、数据验证

掌握爬虫开发有助于进行数据采集和内容监控。

---

**最后更新**：2025-01-XX
