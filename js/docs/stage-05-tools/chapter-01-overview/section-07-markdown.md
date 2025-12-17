# 5.1.7 Markdown 处理

## 概述

Markdown 是一种轻量级标记语言，广泛用于文档编写。本节介绍常用的 Markdown 处理库和工具。

## marked

### 简介

marked 是一个快速、轻量级的 Markdown 解析器和编译器，支持 GFM（GitHub Flavored Markdown）。

### 安装

```bash
npm install marked
```

### 基本使用

```js
import { marked } from 'marked';

// 解析 Markdown
const html = marked('# Hello World');
console.log(html); // <h1>Hello World</h1>

// 解析 Markdown 字符串
const markdown = `
# 标题

这是一段文本。

- 列表项 1
- 列表项 2
`;

const result = marked(markdown);
console.log(result);
```

### 配置选项

```js
import { marked } from 'marked';

// 配置选项
marked.setOptions({
    breaks: true,        // 支持换行
    gfm: true,          // 支持 GFM
    headerIds: false,   // 不生成 header ID
    mangle: false,      // 不混淆邮箱
});
```

### 自定义渲染器

```js
import { marked } from 'marked';

// 自定义渲染器
const renderer = new marked.Renderer();

renderer.heading = function(text, level) {
    return `<h${level} class="custom-heading">${text}</h${level}>`;
};

marked.setOptions({ renderer });

const html = marked('# Hello');
// <h1 class="custom-heading">Hello</h1>
```

## markdown-it

### 简介

markdown-it 是一个功能强大的 Markdown 解析器，可配置性强，支持插件扩展。

### 安装

```bash
npm install markdown-it
```

### 基本使用

```js
import MarkdownIt from 'markdown-it';

const md = new MarkdownIt();

// 解析 Markdown
const html = md.render('# Hello World');
console.log(html); // <h1>Hello World</h1>
```

### 配置选项

```js
import MarkdownIt from 'markdown-it';

const md = new MarkdownIt({
    html: true,        // 允许 HTML 标签
    breaks: true,      // 支持换行
    linkify: true,     // 自动识别链接
});
```

### 使用插件

```bash
npm install markdown-it-anchor markdown-it-table-of-contents
```

```js
import MarkdownIt from 'markdown-it';
import anchor from 'markdown-it-anchor';
import toc from 'markdown-it-table-of-contents';

const md = new MarkdownIt()
    .use(anchor)
    .use(toc);

const html = md.render(markdown);
```

## remark

### 简介

remark 是一个基于 AST（抽象语法树）的 Markdown 处理工具，属于 unified 生态系统。

### 安装

```bash
npm install remark
```

### 基本使用

```js
import { remark } from 'remark';
import remarkHtml from 'remark-html';

// 处理 Markdown
const file = await remark()
    .use(remarkHtml)
    .process('# Hello World');

console.log(String(file)); // <h1>Hello World</h1>
```

### 使用插件

```js
import { remark } from 'remark';
import remarkGfm from 'remark-gfm';
import remarkHtml from 'remark-html';

const file = await remark()
    .use(remarkGfm)  // 支持 GFM
    .use(remarkHtml)
    .process(markdown);
```

## 库对比

| 特性          | marked      | markdown-it | remark      |
|:--------------|:------------|:------------|:------------|
| 速度          | 快          | 中等        | 中等        |
| 体积          | 小          | 中等        | 中等        |
| 可配置性      | 中等        | 高          | 高          |
| 插件生态      | 较少        | 丰富        | 丰富        |
| AST 支持      | 不支持      | 不支持      | 支持        |
| 学习曲线      | 平缓        | 中等        | 较陡        |

## 使用场景

### marked

- 简单快速的 Markdown 解析
- 不需要复杂配置
- 体积敏感的场景

### markdown-it

- 需要丰富的插件
- 需要自定义渲染
- 需要灵活配置

### remark

- 需要 AST 处理
- 需要复杂的转换
- unified 生态系统

## 注意事项

1. **安全性**：解析用户输入的 Markdown 时注意 XSS 防护
2. **性能**：大量 Markdown 处理时注意性能
3. **配置**：根据需求配置选项和插件
4. **输出格式**：注意输出的 HTML 格式和样式

## 最佳实践

1. **选择合适工具**：根据需求选择合适的工具
2. **安全处理**：使用 DOMPurify 等工具清理 HTML
3. **插件管理**：合理使用插件，避免过度依赖
4. **性能优化**：大量处理时考虑缓存和优化

## 练习

1. **marked 基础**：使用 marked 解析 Markdown 并渲染为 HTML。

2. **markdown-it 插件**：使用 markdown-it 和插件实现表格、代码高亮等功能。

3. **remark 处理**：使用 remark 处理 Markdown，实现自定义转换。

4. **安全处理**：实现安全的 Markdown 渲染，防止 XSS 攻击。

5. **Markdown 编辑器**：创建一个简单的 Markdown 编辑器，实时预览。

完成以上练习后，你已经了解了常用的工具与库概览。

## 总结

marked、markdown-it、remark 是常用的 Markdown 处理工具。marked 快速轻量，markdown-it 功能丰富，remark 基于 AST。根据项目需求选择合适的工具，注意安全性和性能优化。

## 相关资源

- [marked 官网](https://marked.js.org/)
- [markdown-it 官网](https://github.com/markdown-it/markdown-it)
- [remark 官网](https://remark.js.org/)
