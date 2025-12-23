# 4.7.3 formidable

## 1. 概述

formidable 是一个用于解析表单数据的 Node.js 库，支持文件上传和流式处理。formidable 框架无关，可以在任何 Node.js 环境中使用，提供了灵活的文件上传处理能力。

## 2. 特性说明

- **框架无关**：不依赖特定框架
- **流式处理**：支持流式文件处理
- **灵活配置**：提供丰富的配置选项
- **多文件支持**：支持多文件上传
- **TypeScript 支持**：提供类型定义

## 3. 安装与初始化

### 3.1 安装

```bash
npm install formidable
npm install @types/formidable -D
```

### 3.2 基本使用

```ts
import { IncomingMessage } from 'node:http';
import formidable, { File, Fields, Files } from 'formidable';
import { createServer } from 'node:http';

const server = createServer(async (req: IncomingMessage, res: ServerResponse): Promise<void> => {
  if (req.method === 'POST' && req.url === '/upload') {
    const form = formidable({
      uploadDir: 'uploads/',
      keepExtensions: true
    });

    const [fields, files] = await form.parse(req);

    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ fields, files }));
  } else {
    res.writeHead(404);
    res.end('Not Found');
  }
});

server.listen(3000, (): void => {
  console.log('Server running on port 3000');
});
```

## 4. 配置选项

### 4.1 基本配置

```ts
const form = formidable({
  uploadDir: 'uploads/',
  keepExtensions: true,
  maxFileSize: 5 * 1024 * 1024, // 5MB
  maxFields: 1000,
  maxFieldsSize: 2 * 1024 * 1024, // 2MB
  multiples: true // 支持多文件
});
```

### 4.2 高级配置

```ts
const form = formidable({
  uploadDir: 'uploads/',
  keepExtensions: true,
  allowEmptyFiles: false,
  minFileSize: 1,
  maxFileSize: 10 * 1024 * 1024,
  filter: (part: Part): boolean => {
    return part.mimetype?.startsWith('image/') || false;
  }
});
```

## 5. 文件处理

### 5.1 单文件上传

```ts
const form = formidable({
  uploadDir: 'uploads/',
  keepExtensions: true
});

const [fields, files] = await form.parse(req);

const file = Array.isArray(files.file) ? files.file[0] : files.file;
if (file) {
  console.log('File uploaded:', file.originalFilename);
  console.log('File path:', file.filepath);
  console.log('File size:', file.size);
}
```

### 5.2 多文件上传

```ts
const form = formidable({
  uploadDir: 'uploads/',
  keepExtensions: true,
  multiples: true
});

const [fields, files] = await form.parse(req);

const uploadedFiles = Array.isArray(files.files) ? files.files : [files.files];
uploadedFiles.forEach((file: File): void => {
  console.log('File:', file.originalFilename);
});
```

## 6. 事件处理

### 6.1 文件接收事件

```ts
const form = formidable({
  uploadDir: 'uploads/'
});

form.on('fileBegin', (name: string, file: File): void => {
  console.log('File upload started:', name);
});

form.on('file', (name: string, file: File): void => {
  console.log('File uploaded:', name, file.originalFilename);
});

form.on('progress', (bytesReceived: number, bytesExpected: number): void => {
  const percent = (bytesReceived / bytesExpected * 100).toFixed(2);
  console.log(`Upload progress: ${percent}%`);
});

form.on('error', (error: Error): void => {
  console.error('Upload error:', error);
});

form.on('end', (): void => {
  console.log('Upload completed');
});
```

## 7. 与 Express 集成

### 7.1 Express 集成

```ts
import express, { Express, Request, Response } from 'express';
import formidable, { File, Fields, Files } from 'formidable';

const app: Express = express();

app.post('/upload', async (req: Request, res: Response): Promise<void> => {
  const form = formidable({
    uploadDir: 'uploads/',
    keepExtensions: true
  });

  try {
    const [fields, files] = await form.parse(req);
    res.json({ fields, files });
  } catch (error) {
    res.status(500).json({ error: 'Upload failed' });
  }
});

app.listen(3000, (): void => {
  console.log('Server running on port 3000');
});
```

### 7.2 中间件封装

```ts
import { Request, Response, NextFunction } from 'express';
import formidable, { File, Fields, Files } from 'formidable';

interface RequestWithFiles extends Request {
  files?: Files;
  fields?: Fields;
}

function formidableMiddleware(options?: formidable.Options) {
  return async (req: RequestWithFiles, res: Response, next: NextFunction): Promise<void> => {
    if (!req.headers['content-type']?.includes('multipart/form-data')) {
      return next();
    }

    const form = formidable(options);

    try {
      const [fields, files] = await form.parse(req);
      req.fields = fields;
      req.files = files;
      next();
    } catch (error) {
      next(error);
    }
  };
}

app.post('/upload', formidableMiddleware({ uploadDir: 'uploads/' }), (req: RequestWithFiles, res: Response): void => {
  res.json({ fields: req.fields, files: req.files });
});
```

## 8. 流式处理

### 8.1 流式上传

```ts
import { createWriteStream } from 'node:fs';
import { join } from 'node:path';

const form = formidable({
  fileWriteStreamHandler: (file: File): NodeJS.WritableStream => {
    const filepath = join('uploads/', file.originalFilename || 'file');
    return createWriteStream(filepath);
  }
});

form.on('file', (name: string, file: File): void => {
  console.log('File streamed:', file.originalFilename);
});
```

## 9. 文件验证

### 9.1 文件类型验证

```ts
const form = formidable({
  uploadDir: 'uploads/',
  filter: (part: Part): boolean => {
    const allowedTypes = ['image/jpeg', 'image/png', 'image/gif'];
    return part.mimetype ? allowedTypes.includes(part.mimetype) : false;
  }
});
```

### 9.2 文件大小验证

```ts
const form = formidable({
  uploadDir: 'uploads/',
  maxFileSize: 5 * 1024 * 1024, // 5MB
  maxFieldsSize: 2 * 1024 * 1024 // 2MB
});

form.on('error', (error: Error): void => {
  if (error.message.includes('maxFileSize')) {
    console.error('File too large');
  }
});
```

## 10. 最佳实践

### 10.1 错误处理

- 实现完善的错误处理
- 处理文件大小限制
- 处理文件类型限制

### 10.2 性能优化

- 使用流式处理
- 限制文件大小
- 异步处理

### 10.3 安全性

- 验证文件类型
- 验证文件大小
- 生成唯一文件名

## 11. 注意事项

- **内存使用**：大文件使用流式处理
- **错误处理**：实现完善的错误处理
- **文件清理**：及时清理临时文件
- **安全性**：实现文件验证

## 12. 常见问题

### 12.1 formidable 和 multer 的区别？

formidable 框架无关，支持流式处理；multer 专为 Express 设计。

### 12.2 如何处理大文件？

使用流式处理和 fileWriteStreamHandler。

### 12.3 如何实现进度跟踪？

使用 progress 事件监听上传进度。

## 13. 实践任务

1. **实现文件上传**：使用 formidable 实现文件上传功能
2. **实现流式处理**：实现流式文件处理
3. **实现文件验证**：实现文件类型和大小验证
4. **实现进度跟踪**：实现上传进度跟踪
5. **实现错误处理**：实现完善的错误处理机制

---

**下一节**：[4.7.4 文件验证与存储](section-04-validation-storage.md)
