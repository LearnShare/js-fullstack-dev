# 4.7.4 文件验证与存储

## 1. 概述

文件验证和存储是文件上传功能的关键部分。文件验证确保上传文件的安全性和合法性，文件存储需要选择合适的存储方案和实现高效的存储逻辑。

## 2. 文件验证

### 2.1 文件类型验证

```ts
import { readFile } from 'node:fs/promises';

interface FileType {
  mime: string;
  extension: string;
}

async function validateFileType(filepath: string, expectedType: string): Promise<boolean> {
  // 读取文件头
  const buffer = await readFile(filepath);
  const header = buffer.slice(0, 4);

  // 检查文件签名
  const signatures: Record<string, number[]> = {
    'image/jpeg': [0xFF, 0xD8, 0xFF],
    'image/png': [0x89, 0x50, 0x4E, 0x47],
    'image/gif': [0x47, 0x49, 0x46, 0x38]
  };

  const signature = signatures[expectedType];
  if (!signature) return false;

  return signature.every((byte: number, index: number): boolean => header[index] === byte);
}
```

### 2.2 文件大小验证

```ts
const MAX_FILE_SIZE = 5 * 1024 * 1024; // 5MB

function validateFileSize(size: number): boolean {
  return size > 0 && size <= MAX_FILE_SIZE;
}
```

### 2.3 文件名验证

```ts
function sanitizeFilename(filename: string): string {
  // 移除路径分隔符
  let sanitized = filename.replace(/[\/\\]/g, '');
  
  // 移除特殊字符
  sanitized = sanitized.replace(/[^a-zA-Z0-9._-]/g, '');
  
  // 限制长度
  if (sanitized.length > 255) {
    const ext = sanitized.substring(sanitized.lastIndexOf('.'));
    sanitized = sanitized.substring(0, 255 - ext.length) + ext;
  }
  
  return sanitized;
}
```

### 2.4 综合验证

```ts
interface ValidationResult {
  valid: boolean;
  errors: string[];
}

async function validateFile(file: Express.Multer.File): Promise<ValidationResult> {
  const errors: string[] = [];

  // 验证文件类型
  const allowedTypes = ['image/jpeg', 'image/png', 'image/gif'];
  if (!allowedTypes.includes(file.mimetype)) {
    errors.push('Invalid file type');
  }

  // 验证文件大小
  if (!validateFileSize(file.size)) {
    errors.push('File size exceeds limit');
  }

  // 验证文件内容
  const isValidContent = await validateFileType(file.path, file.mimetype);
  if (!isValidContent) {
    errors.push('File content does not match type');
  }

  return {
    valid: errors.length === 0,
    errors
  };
}
```

## 3. 文件存储

### 3.1 本地存储

```ts
import { writeFile, mkdir } from 'node:fs/promises';
import { join, dirname } from 'node:path';
import { existsSync } from 'node:fs';

async function saveFileLocally(file: Buffer, filename: string, baseDir: string = 'uploads'): Promise<string> {
  // 创建目录
  const dir = join(process.cwd(), baseDir);
  if (!existsSync(dir)) {
    await mkdir(dir, { recursive: true });
  }

  // 生成唯一文件名
  const uniqueFilename = generateUniqueFilename(filename);
  const filepath = join(dir, uniqueFilename);

  // 保存文件
  await writeFile(filepath, file);

  return filepath;
}

function generateUniqueFilename(originalFilename: string): string {
  const timestamp = Date.now();
  const random = Math.round(Math.random() * 1E9);
  const ext = originalFilename.substring(originalFilename.lastIndexOf('.'));
  return `${timestamp}-${random}${ext}`;
}
```

### 3.2 云存储（AWS S3）

```ts
import { S3Client, PutObjectCommand, GetObjectCommand } from '@aws-sdk/client-s3';
import { getSignedUrl } from '@aws-sdk/s3-request-presigner';

const s3Client = new S3Client({ region: 'us-east-1' });
const BUCKET_NAME = 'my-bucket';

async function uploadToS3(file: Buffer, filename: string, contentType: string): Promise<string> {
  const key = `uploads/${Date.now()}-${filename}`;
  
  const command = new PutObjectCommand({
    Bucket: BUCKET_NAME,
    Key: key,
    Body: file,
    ContentType: contentType
  });

  await s3Client.send(command);
  return `https://${BUCKET_NAME}.s3.amazonaws.com/${key}`;
}

async function getSignedUrl(key: string, expiresIn: number = 3600): Promise<string> {
  const command = new GetObjectCommand({
    Bucket: BUCKET_NAME,
    Key: key
  });

  return await getSignedUrl(s3Client, command, { expiresIn });
}
```

### 3.3 云存储（Cloudinary）

```ts
import { v2 as cloudinary } from 'cloudinary';

cloudinary.config({
  cloud_name: process.env.CLOUDINARY_CLOUD_NAME!,
  api_key: process.env.CLOUDINARY_API_KEY!,
  api_secret: process.env.CLOUDINARY_API_SECRET!
});

async function uploadToCloudinary(file: Buffer, filename: string): Promise<string> {
  return new Promise((resolve, reject): void => {
    const uploadStream = cloudinary.uploader.upload_stream(
      {
        folder: 'uploads',
        public_id: filename.replace(/\.[^/.]+$/, ''),
        resource_type: 'auto'
      },
      (error, result) => {
        if (error) {
          reject(error);
        } else {
          resolve(result!.secure_url);
        }
      }
    );

    uploadStream.end(file);
  });
}
```

## 4. 存储策略

### 4.1 存储选择

```ts
enum StorageType {
  LOCAL = 'local',
  S3 = 's3',
  CLOUDINARY = 'cloudinary'
}

async function saveFile(
  file: Buffer,
  filename: string,
  storageType: StorageType = StorageType.LOCAL
): Promise<string> {
  switch (storageType) {
    case StorageType.LOCAL:
      return await saveFileLocally(file, filename);
    case StorageType.S3:
      return await uploadToS3(file, filename, 'application/octet-stream');
    case StorageType.CLOUDINARY:
      return await uploadToCloudinary(file, filename);
    default:
      throw new Error('Invalid storage type');
  }
}
```

### 4.2 文件清理

```ts
import { unlink, readdir } from 'node:fs/promises';
import { join } from 'node:path';

async function cleanupOldFiles(directory: string, maxAge: number): Promise<void> {
  const files = await readdir(directory);
  const now = Date.now();

  for (const file of files) {
    const filepath = join(directory, file);
    const stats = await stat(filepath);
    const age = now - stats.mtime.getTime();

    if (age > maxAge) {
      await unlink(filepath);
      console.log(`Deleted old file: ${file}`);
    }
  }
}

// 定期清理
setInterval(async (): Promise<void> => {
  await cleanupOldFiles('uploads/', 7 * 24 * 60 * 60 * 1000); // 7 天
}, 24 * 60 * 60 * 1000); // 每天执行一次
```

## 5. 完整示例

### 5.1 Express + multer + 验证 + 存储

```ts
import express, { Express, Request, Response } from 'express';
import multer, { Multer } from 'multer';
import { diskStorage } from 'multer';
import { validateFile, saveFile, StorageType } from './file-utils';

const app: Express = express();

const storage = diskStorage({
  destination: 'temp/',
  filename: (req: Request, file: Express.Multer.File, cb: (error: Error | null, filename: string) => void): void => {
    const uniqueSuffix = Date.now() + '-' + Math.round(Math.random() * 1E9);
    const ext = file.originalname.substring(file.originalname.lastIndexOf('.'));
    cb(null, uniqueSuffix + ext);
  }
});

const upload: Multer = multer({
  storage,
  limits: {
    fileSize: 5 * 1024 * 1024 // 5MB
  },
  fileFilter: (req: Request, file: Express.Multer.File, cb: multer.FileFilterCallback): void => {
    const allowedTypes = ['image/jpeg', 'image/png', 'image/gif'];
    if (allowedTypes.includes(file.mimetype)) {
      cb(null, true);
    } else {
      cb(new Error('Invalid file type'));
    }
  }
});

app.post('/upload', upload.single('file'), async (req: Request, res: Response): Promise<void> => {
  if (!req.file) {
    return res.status(400).json({ error: 'No file uploaded' });
  }

  // 验证文件
  const validation = await validateFile(req.file);
  if (!validation.valid) {
    return res.status(400).json({ errors: validation.errors });
  }

  // 读取文件
  const fileBuffer = await readFile(req.file.path);

  // 保存文件
  const fileUrl = await saveFile(fileBuffer, req.file.originalname, StorageType.S3);

  // 删除临时文件
  await unlink(req.file.path);

  res.json({
    message: 'File uploaded successfully',
    url: fileUrl
  });
});

app.listen(3000, (): void => {
  console.log('Server running on port 3000');
});
```

## 6. 最佳实践

### 6.1 验证策略

- 验证文件类型（MIME 类型和文件内容）
- 验证文件大小
- 验证文件名
- 扫描恶意文件

### 6.2 存储策略

- 选择合适的存储方案
- 实现文件清理机制
- 使用 CDN 加速
- 实现备份机制

### 6.3 安全性

- 生成唯一文件名
- 限制文件访问
- 实现访问控制
- 记录文件操作

## 7. 注意事项

- **安全性**：实现完善的验证机制
- **性能**：优化文件存储性能
- **存储成本**：考虑存储成本
- **可扩展性**：考虑存储扩展性

## 8. 常见问题

### 8.1 如何选择存储方案？

根据文件大小、访问频率、成本等因素选择。小文件用本地存储，大文件用云存储。

### 8.2 如何实现文件清理？

实现定期清理机制，删除过期文件。

### 8.3 如何实现文件访问控制？

使用签名 URL 或访问令牌控制文件访问。

## 9. 实践任务

1. **实现文件验证**：实现完整的文件验证机制
2. **实现本地存储**：实现本地文件存储功能
3. **实现云存储**：集成云存储服务
4. **实现文件清理**：实现文件清理机制
5. **实现访问控制**：实现文件访问控制

---

**下一章**：[4.8 API 限流](../chapter-08-rate-limiting/readme.md)
