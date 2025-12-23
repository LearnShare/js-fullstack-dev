# 9.9.3 备份与恢复流程

## 1. 概述

备份与恢复是数据保护的基础，通过定期备份数据和应用，可以在故障时快速恢复。本章介绍备份策略、备份实现和恢复流程。

## 2. 备份策略

### 2.1 备份类型

- **全量备份**：备份所有数据
- **增量备份**：备份变更的数据
- **差异备份**：备份上次全量备份后的变更

### 2.2 备份频率

```ts
interface BackupSchedule {
  full: string;      // 全量备份频率
  incremental: string; // 增量备份频率
  retention: number;  // 保留天数
}

const schedule: BackupSchedule = {
  full: '0 2 * * 0',      // 每周日凌晨 2 点
  incremental: '0 2 * * *', // 每天凌晨 2 点
  retention: 30            // 保留 30 天
};
```

## 3. 数据库备份

### 3.1 PostgreSQL 备份

```ts
import { exec } from 'node:child_process';
import { promisify } from 'node:util';
import { writeFile } from 'node:fs/promises';

const execAsync = promisify(exec);

async function backupPostgreSQL(): Promise<string> {
  const timestamp = new Date().toISOString().replace(/:/g, '-');
  const backupFile = `/backups/postgres-${timestamp}.sql`;
  
  // 执行备份
  await execAsync(
    `pg_dump -h localhost -U postgres -d mydb > ${backupFile}`
  );
  
  // 压缩备份
  await execAsync(`gzip ${backupFile}`);
  
  return `${backupFile}.gz`;
}
```

### 3.2 MySQL 备份

```ts
async function backupMySQL(): Promise<string> {
  const timestamp = new Date().toISOString().replace(/:/g, '-');
  const backupFile = `/backups/mysql-${timestamp}.sql`;
  
  await execAsync(
    `mysqldump -h localhost -u root -p mydb > ${backupFile}`
  );
  
  await execAsync(`gzip ${backupFile}`);
  
  return `${backupFile}.gz`;
}
```

## 4. 文件备份

### 4.1 应用文件备份

```ts
import { createReadStream, createWriteStream } from 'node:fs';
import { pipeline } from 'node:stream/promises';
import { createGzip } from 'node:zlib';
import { archiver } from 'archiver';

async function backupFiles(sourceDir: string, backupFile: string): Promise<void> {
  const output = createWriteStream(backupFile);
  const archive = archiver('zip', { zlib: { level: 9 } });
  
  archive.pipe(output);
  archive.directory(sourceDir, false);
  await archive.finalize();
}
```

## 5. 自动化备份

### 5.1 定时备份

```ts
import cron from 'node-cron';

// 每天凌晨 2 点备份
cron.schedule('0 2 * * *', async (): Promise<void> => {
  console.log('Starting backup...');
  
  try {
    // 备份数据库
    const dbBackup = await backupPostgreSQL();
    
    // 备份文件
    const fileBackup = await backupFiles('/app/data', '/backups/files.zip');
    
    // 上传到云存储
    await uploadToCloud(dbBackup);
    await uploadToCloud(fileBackup);
    
    // 清理旧备份
    await cleanupOldBackups(30);
    
    console.log('Backup completed');
  } catch (error) {
    console.error('Backup failed:', error);
    await sendAlert('Backup failed', error);
  }
});
```

## 6. 恢复流程

### 6.1 数据库恢复

```ts
async function restorePostgreSQL(backupFile: string): Promise<void> {
  console.log(`Restoring from ${backupFile}...`);
  
  // 1. 停止应用
  await stopApplication();
  
  // 2. 解压备份
  await execAsync(`gunzip ${backupFile}`);
  const sqlFile = backupFile.replace('.gz', '');
  
  // 3. 恢复数据库
  await execAsync(
    `psql -h localhost -U postgres -d mydb < ${sqlFile}`
  );
  
  // 4. 验证恢复
  await verifyDatabase();
  
  // 5. 启动应用
  await startApplication();
  
  console.log('Restore completed');
}
```

### 6.2 文件恢复

```ts
import { extract } from 'unzipper';

async function restoreFiles(backupFile: string, targetDir: string): Promise<void> {
  console.log(`Restoring files from ${backupFile}...`);
  
  // 1. 停止应用
  await stopApplication();
  
  // 2. 备份当前文件
  await backupFiles(targetDir, `${targetDir}.backup`);
  
  // 3. 恢复文件
  await extract(backupFile, { dir: targetDir });
  
  // 4. 验证恢复
  await verifyFiles(targetDir);
  
  // 5. 启动应用
  await startApplication();
  
  console.log('File restore completed');
}
```

## 7. 备份验证

### 7.1 验证备份

```ts
async function verifyBackup(backupFile: string): Promise<boolean> {
  try {
    // 检查文件完整性
    const stats = await stat(backupFile);
    if (stats.size === 0) {
      return false;
    }
    
    // 测试恢复（可选）
    // 在测试环境恢复并验证
    
    return true;
  } catch {
    return false;
  }
}
```

## 8. 最佳实践

### 8.1 备份策略

- 定期备份
- 多地点备份
- 加密备份
- 验证备份

### 8.2 恢复流程

- 自动化恢复
- 测试恢复
- 文档化流程
- 定期演练

## 9. 注意事项

- **备份验证**：定期验证备份
- **备份加密**：加密敏感数据
- **备份存储**：安全存储备份
- **恢复测试**：定期测试恢复

## 10. 常见问题

### 10.1 如何选择备份频率？

根据数据重要性、变更频率、RPO 要求选择。

### 10.2 如何验证备份？

检查文件完整性、测试恢复、定期演练。

### 10.3 如何优化备份性能？

使用增量备份、并行备份、压缩备份。

## 11. 实践任务

1. **实现备份**：实现自动化备份
2. **备份策略**：设计备份策略
3. **恢复流程**：实现恢复流程
4. **备份验证**：验证备份完整性
5. **持续优化**：持续优化备份恢复

---

**阶段九完成**：恭喜完成阶段九的学习！可以继续学习阶段十：现代运行时与新兴技术。
