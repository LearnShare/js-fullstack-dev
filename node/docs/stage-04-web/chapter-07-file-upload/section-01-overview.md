# 4.7.1 文件上传概述

## 1. 概述

文件上传是 Web 应用中常见的功能，允许用户将文件从客户端上传到服务器。文件上传需要处理文件接收、验证、存储等操作，涉及安全性、性能、存储等多个方面。

## 2. 核心概念

### 2.1 文件上传方式

**multipart/form-data**：
- 使用 `multipart/form-data` 编码
- 支持文件和其他表单数据
- 最常用的文件上传方式

**Base64 编码**：
- 将文件编码为 Base64 字符串
- 通过 JSON 传输
- 适合小文件

**二进制流**：
- 直接传输二进制数据
- 使用 `application/octet-stream`
- 适合大文件

### 2.2 文件上传流程

```
客户端 → 选择文件 → 编码 → HTTP 请求 → 服务器接收 → 验证 → 存储 → 响应
```

## 3. Content-Type

### 3.1 multipart/form-data

```http
POST /upload HTTP/1.1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="file"; filename="example.jpg"
Content-Type: image/jpeg

[文件二进制数据]
------WebKitFormBoundary7MA4YWxkTrZu0gW--
```

### 3.2 application/octet-stream

```http
POST /upload HTTP/1.1
Content-Type: application/octet-stream
Content-Length: 1024

[文件二进制数据]
```

## 4. 文件上传库

### 4.1 multer

**特点**：
- Express 中间件
- 支持多文件上传
- 内存和磁盘存储
- 文件过滤

**适用场景**：
- Express 应用
- 需要中间件集成
- 多文件上传

### 4.2 formidable

**特点**：
- 独立库
- 支持流式处理
- 灵活配置
- 框架无关

**适用场景**：
- 需要流式处理
- 框架无关的应用
- 大文件上传

### 4.3 busboy

**特点**：
- 底层解析库
- 高性能
- 流式处理
- 框架无关

**适用场景**：
- 需要底层控制
- 高性能要求
- 自定义实现

## 5. 文件验证

### 5.1 文件类型验证

```ts
const allowedTypes = ['image/jpeg', 'image/png', 'image/gif'];

function isValidFileType(mimetype: string): boolean {
  return allowedTypes.includes(mimetype);
}
```

### 5.2 文件大小验证

```ts
const MAX_FILE_SIZE = 5 * 1024 * 1024; // 5MB

function isValidFileSize(size: number): boolean {
  return size <= MAX_FILE_SIZE;
}
```

### 5.3 文件扩展名验证

```ts
const allowedExtensions = ['.jpg', '.jpeg', '.png', '.gif'];

function isValidExtension(filename: string): boolean {
  const ext = filename.toLowerCase().substring(filename.lastIndexOf('.'));
  return allowedExtensions.includes(ext);
}
```

## 6. 文件存储

### 6.1 本地存储

```ts
import { writeFile } from 'node:fs/promises';
import { join } from 'node:path';

async function saveFile(file: Buffer, filename: string): Promise<string> {
  const filePath = join(process.cwd(), 'uploads', filename);
  await writeFile(filePath, file);
  return filePath;
}
```

### 6.2 云存储

```ts
// AWS S3
import { S3Client, PutObjectCommand } from '@aws-sdk/client-s3';

const s3Client = new S3Client({ region: 'us-east-1' });

async function uploadToS3(file: Buffer, filename: string): Promise<string> {
  const command = new PutObjectCommand({
    Bucket: 'my-bucket',
    Key: filename,
    Body: file
  });
  
  await s3Client.send(command);
  return `https://my-bucket.s3.amazonaws.com/${filename}`;
}
```

## 7. 安全性考虑

### 7.1 文件类型验证

- 验证 MIME 类型
- 验证文件扩展名
- 验证文件内容

### 7.2 文件大小限制

- 限制单个文件大小
- 限制总上传大小
- 限制上传频率

### 7.3 文件名处理

- 生成唯一文件名
- 清理文件名
- 防止路径遍历

## 8. 性能优化

### 8.1 流式处理

- 使用流式处理大文件
- 避免将整个文件加载到内存
- 实现进度跟踪

### 8.2 分块上传

- 将大文件分块上传
- 实现断点续传
- 减少内存使用

### 8.3 异步处理

- 异步保存文件
- 使用消息队列
- 后台处理

## 9. 注意事项

- **安全性**：实现完善的验证机制
- **性能**：优化大文件上传性能
- **存储**：选择合适的存储方案
- **错误处理**：实现完善的错误处理

## 10. 常见问题

### 10.1 如何处理大文件上传？

使用流式处理、分块上传或断点续传。

### 10.2 如何验证文件类型？

验证 MIME 类型、文件扩展名和文件内容。

### 10.3 如何存储上传的文件？

使用本地存储、云存储或对象存储服务。

## 11. 相关资源

- [multer 文档](https://github.com/expressjs/multer)
- [formidable 文档](https://github.com/node-formidable/formidable)
- [文件上传安全指南](https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload)

---

**下一节**：[4.7.2 multer](section-02-multer.md)
