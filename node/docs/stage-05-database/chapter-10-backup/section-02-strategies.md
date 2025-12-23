# 5.10.2 备份策略

## 1. 概述

备份策略决定了何时备份、如何备份、备份保留多长时间等。合理的备份策略可以平衡数据安全、存储成本和恢复时间。

## 2. 备份策略类型

### 2.1 3-2-1 策略

**原则**：
- 3 份数据副本
- 2 种不同介质
- 1 份异地备份

**实现**：
```ts
// 本地备份
await backupToLocal();

// 云存储备份
await backupToCloud();

// 异地备份
await backupToRemote();
```

### 2.2 全量+增量策略

**原则**：
- 定期全量备份
- 频繁增量备份
- 快速恢复

**实现**：
```ts
// 每周全量备份
if (isWeeklyBackup()) {
  await fullBackup();
}

// 每日增量备份
await incrementalBackup();
```

## 3. 备份实现

### 3.1 PostgreSQL 备份

```ts
import { exec } from 'node:child_process';
import { promisify } from 'node:util';

const execAsync = promisify(exec);

async function backupPostgreSQL(): Promise<void> {
  const timestamp = new Date().toISOString().replace(/:/g, '-');
  const backupFile = `backup-${timestamp}.sql`;
  
  await execAsync(
    `pg_dump -h localhost -U postgres -d mydb -F c -f ${backupFile}`
  );
  
  console.log(`Backup created: ${backupFile}`);
}
```

### 3.2 MySQL 备份

```ts
async function backupMySQL(): Promise<void> {
  const timestamp = new Date().toISOString().replace(/:/g, '-');
  const backupFile = `backup-${timestamp}.sql`;
  
  await execAsync(
    `mysqldump -h localhost -u root -p mydb > ${backupFile}`
  );
  
  console.log(`Backup created: ${backupFile}`);
}
```

### 3.3 MongoDB 备份

```ts
async function backupMongoDB(): Promise<void> {
  const timestamp = new Date().toISOString().replace(/:/g, '-');
  const backupDir = `backup-${timestamp}`;
  
  await execAsync(
    `mongodump --host localhost --db mydb --out ${backupDir}`
  );
  
  console.log(`Backup created: ${backupDir}`);
}
```

## 4. 自动化备份

### 4.1 定时备份

```ts
import cron from 'node-cron';

// 每天凌晨备份
cron.schedule('0 0 * * *', async (): Promise<void> => {
  await backupPostgreSQL();
});

// 每周全量备份
cron.schedule('0 0 * * 0', async (): Promise<void> => {
  await fullBackup();
});
```

### 4.2 备份清理

```ts
import { readdir, unlink, stat } from 'node:fs/promises';
import { join } from 'node:path';

async function cleanupOldBackups(backupDir: string, maxAge: number): Promise<void> {
  const files = await readdir(backupDir);
  const now = Date.now();
  
  for (const file of files) {
    const filePath = join(backupDir, file);
    const stats = await stat(filePath);
    const age = now - stats.mtime.getTime();
    
    if (age > maxAge) {
      await unlink(filePath);
      console.log(`Deleted old backup: ${file}`);
    }
  }
}
```

## 5. 备份验证

### 5.1 备份完整性检查

```ts
async function verifyBackup(backupFile: string): Promise<boolean> {
  try {
    // 检查文件大小
    const stats = await stat(backupFile);
    if (stats.size === 0) {
      return false;
    }
    
    // 检查文件格式
    // 根据备份类型进行验证
    
    return true;
  } catch (error) {
    console.error('Backup verification failed:', error);
    return false;
  }
}
```

## 6. 最佳实践

### 6.1 策略设计

- 根据业务需求设计策略
- 平衡安全性和成本
- 定期审查和调整
- 文档化备份流程

### 6.2 自动化

- 自动化备份流程
- 自动化备份清理
- 自动化备份验证
- 自动化告警

## 7. 注意事项

- **备份验证**：定期验证备份完整性
- **存储安全**：保护备份数据安全
- **恢复测试**：定期测试恢复流程
- **监控告警**：监控备份执行状态

## 8. 常见问题

### 8.1 如何设计备份策略？

根据数据重要性、变更频率、恢复需求设计。

### 8.2 备份保留多长时间？

根据业务需求、合规要求、存储成本确定。

### 8.3 如何自动化备份？

使用定时任务、脚本、备份工具实现自动化。

## 9. 实践任务

1. **设计策略**：设计数据库备份策略
2. **实现备份**：实现数据库备份功能
3. **自动化**：实现自动化备份流程
4. **备份验证**：实现备份验证功能
5. **备份清理**：实现备份清理功能

---

**下一节**：[5.10.3 恢复操作](section-03-restore.md)
