# 4.7.2 multer

## 1. 概述

multer 是一个用于处理 `multipart/form-data` 的 Express 中间件，主要用于文件上传。multer 支持单文件和多文件上传，提供内存存储和磁盘存储两种方式。

## 2. 特性说明

- **Express 中间件**：专为 Express 设计
- **多文件支持**：支持单文件和多文件上传
- **存储选项**：内存存储和磁盘存储
- **文件过滤**：支持文件类型和大小过滤
- **TypeScript 支持**：提供类型定义

## 3. 安装与初始化

### 3.1 安装

```bash
npm install multer
npm install @types/multer -D
```

### 3.2 基本使用

```ts
import express, { Express, Request, Response } from 'express';
import multer, { Multer } from 'multer';

const app: Express = express();
const upload: Multer = multer({ dest: 'uploads/' });

app.post('/upload', upload.single('file'), (req: Request, res: Response): void => {
  if (!req.file) {
    return res.status(400).json({ error: 'No file uploaded' });
  }

  res.json({
    filename: req.file.filename,
    originalname: req.file.originalname,
    size: req.file.size
  });
});

app.listen(3000, (): void => {
  console.log('Server running on port 3000');
});
```

## 4. 存储配置

### 4.1 磁盘存储

```ts
import { diskStorage } from 'multer';
import { join } from 'node:path';

const storage = diskStorage({
  destination: (req: Request, file: Express.Multer.File, cb: (error: Error | null, destination: string) => void): void => {
    cb(null, 'uploads/');
  },
  filename: (req: Request, file: Express.Multer.File, cb: (error: Error | null, filename: string) => void): void => {
    const uniqueSuffix = Date.now() + '-' + Math.round(Math.random() * 1E9);
    const ext = file.originalname.substring(file.originalname.lastIndexOf('.'));
    cb(null, file.fieldname + '-' + uniqueSuffix + ext);
  }
});

const upload = multer({ storage });
```

### 4.2 内存存储

```ts
import { memoryStorage } from 'multer';

const storage = memoryStorage();
const upload = multer({ storage });

app.post('/upload', upload.single('file'), async (req: Request, res: Response): Promise<void> => {
  if (!req.file) {
    return res.status(400).json({ error: 'No file uploaded' });
  }

  // 文件在 req.file.buffer 中
  const fileBuffer: Buffer = req.file.buffer;
  
  // 保存到云存储或处理文件
  const fileUrl = await uploadToCloudStorage(fileBuffer, req.file.originalname);
  
  res.json({ url: fileUrl });
});
```

## 5. 文件过滤

### 5.1 文件类型过滤

```ts
const fileFilter = (req: Request, file: Express.Multer.File, cb: multer.FileFilterCallback): void => {
  const allowedTypes = ['image/jpeg', 'image/png', 'image/gif'];
  
  if (allowedTypes.includes(file.mimetype)) {
    cb(null, true);
  } else {
    cb(new Error('Invalid file type'));
  }
};

const upload = multer({
  storage: diskStorage({ destination: 'uploads/' }),
  fileFilter
});
```

### 5.2 文件大小限制

```ts
const upload = multer({
  storage: diskStorage({ destination: 'uploads/' }),
  limits: {
    fileSize: 5 * 1024 * 1024, // 5MB
    files: 5, // 最多 5 个文件
    fieldSize: 1024 * 1024 // 1MB
  }
});
```

## 6. 单文件上传

### 6.1 基本单文件上传

```ts
app.post('/upload', upload.single('file'), (req: Request, res: Response): void => {
  if (!req.file) {
    return res.status(400).json({ error: 'No file uploaded' });
  }

  res.json({
    message: 'File uploaded successfully',
    file: {
      filename: req.file.filename,
      originalname: req.file.originalname,
      mimetype: req.file.mimetype,
      size: req.file.size
    }
  });
});
```

### 6.2 带表单数据的单文件上传

```ts
app.post('/upload', upload.single('file'), (req: Request, res: Response): void => {
  const { title, description } = req.body;
  const file = req.file;

  if (!file) {
    return res.status(400).json({ error: 'No file uploaded' });
  }

  res.json({
    message: 'File uploaded successfully',
    data: {
      title,
      description,
      file: {
        filename: file.filename,
        originalname: file.originalname
      }
    }
  });
});
```

## 7. 多文件上传

### 7.1 多个字段

```ts
app.post('/upload', upload.fields([
  { name: 'avatar', maxCount: 1 },
  { name: 'gallery', maxCount: 5 }
]), (req: Request, res: Response): void => {
  const files = req.files as { [fieldname: string]: Express.Multer.File[] };
  
  const avatar = files.avatar?.[0];
  const gallery = files.gallery || [];

  res.json({
    avatar: avatar ? {
      filename: avatar.filename,
      originalname: avatar.originalname
    } : null,
    gallery: gallery.map((file: Express.Multer.File) => ({
      filename: file.filename,
      originalname: file.originalname
    }))
  });
});
```

### 7.2 同一字段多个文件

```ts
app.post('/upload', upload.array('files', 10), (req: Request, res: Response): void => {
  const files = req.files as Express.Multer.File[];

  res.json({
    message: `${files.length} files uploaded successfully`,
    files: files.map((file: Express.Multer.File) => ({
      filename: file.filename,
      originalname: file.originalname,
      size: file.size
    }))
  });
});
```

## 8. 自定义存储

### 8.1 云存储集成

```ts
import { S3Client, PutObjectCommand } from '@aws-sdk/client-s3';

const s3Client = new S3Client({ region: 'us-east-1' });

const storage = diskStorage({
  destination: async (req: Request, file: Express.Multer.File, cb: (error: Error | null, destination: string) => void): Promise<void> => {
    // 先保存到临时目录
    cb(null, 'temp/');
  },
  filename: (req: Request, file: Express.Multer.File, cb: (error: Error | null, filename: string) => void): void => {
    const uniqueSuffix = Date.now() + '-' + Math.round(Math.random() * 1E9);
    const ext = file.originalname.substring(file.originalname.lastIndexOf('.'));
    cb(null, uniqueSuffix + ext);
  }
});

const upload = multer({ storage });

app.post('/upload', upload.single('file'), async (req: Request, res: Response): Promise<void> => {
  if (!req.file) {
    return res.status(400).json({ error: 'No file uploaded' });
  }

  // 读取文件并上传到 S3
  const fileBuffer = await readFile(req.file.path);
  const command = new PutObjectCommand({
    Bucket: 'my-bucket',
    Key: req.file.filename,
    Body: fileBuffer
  });

  await s3Client.send(command);
  
  // 删除临时文件
  await unlink(req.file.path);

  res.json({ url: `https://my-bucket.s3.amazonaws.com/${req.file.filename}` });
});
```

## 9. 错误处理

### 9.1 错误处理中间件

```ts
app.post('/upload', upload.single('file'), (req: Request, res: Response): void => {
  // 处理上传
}, (error: Error, req: Request, res: Response, next: express.NextFunction): void => {
  if (error instanceof multer.MulterError) {
    if (error.code === 'LIMIT_FILE_SIZE') {
      return res.status(400).json({ error: 'File too large' });
    }
    if (error.code === 'LIMIT_FILE_COUNT') {
      return res.status(400).json({ error: 'Too many files' });
    }
  }

  res.status(500).json({ error: 'Upload failed' });
});
```

## 10. 最佳实践

### 10.1 文件验证

- 验证文件类型
- 验证文件大小
- 验证文件内容

### 10.2 存储管理

- 使用唯一文件名
- 清理临时文件
- 实现文件清理机制

### 10.3 安全性

- 限制文件类型
- 限制文件大小
- 防止路径遍历

## 11. 注意事项

- **内存使用**：大文件使用磁盘存储
- **文件清理**：及时清理临时文件
- **错误处理**：实现完善的错误处理
- **安全性**：实现文件验证

## 12. 常见问题

### 12.1 如何处理大文件？

使用磁盘存储和流式处理。

### 12.2 如何验证文件类型？

使用 fileFilter 和文件内容验证。

### 12.3 如何实现进度跟踪？

使用自定义存储引擎或客户端进度跟踪。

## 13. 实践任务

1. **实现单文件上传**：实现基本的单文件上传功能
2. **实现多文件上传**：实现多文件上传功能
3. **实现文件验证**：实现文件类型和大小验证
4. **实现云存储**：集成云存储服务
5. **实现错误处理**：实现完善的错误处理机制

---

**下一节**：[4.7.3 formidable](section-03-formidable.md)
