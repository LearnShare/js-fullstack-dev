# 5.10.3 恢复操作

## 1. 概述

数据库恢复是在数据丢失或损坏时，从备份中恢复数据的过程。恢复操作需要快速、准确、可靠，以最小化业务中断时间。

## 2. 恢复类型

### 2.1 全量恢复

**场景**：
- 数据库完全损坏
- 数据完全丢失
- 系统重建

**流程**：
```ts
async function fullRestore(backupFile: string): Promise<void> {
  // 1. 停止应用
  await stopApplication();
  
  // 2. 备份当前数据（如需要）
  await backupCurrentData();
  
  // 3. 恢复数据库
  await execAsync(`pg_restore -h localhost -U postgres -d mydb -c ${backupFile}`);
  
  // 4. 验证恢复
  await verifyRestore();
  
  // 5. 启动应用
  await startApplication();
}
```

### 2.2 部分恢复

**场景**：
- 部分数据损坏
- 误删除数据
- 数据修复

**流程**：
```ts
async function partialRestore(table: string, backupFile: string): Promise<void> {
  // 恢复特定表
  await execAsync(
    `pg_restore -h localhost -U postgres -d mydb -t ${table} ${backupFile}`
  );
}
```

### 2.3 时间点恢复

**场景**：
- 恢复到特定时间点
- 事务日志恢复
- 精确恢复

**流程**：
```ts
async function pointInTimeRestore(targetTime: Date): Promise<void> {
  // 1. 恢复全量备份
  await fullRestore('full-backup.sql');
  
  // 2. 应用事务日志到目标时间
  await applyTransactionLogs(targetTime);
}
```

## 3. 恢复实现

### 3.1 PostgreSQL 恢复

```ts
async function restorePostgreSQL(backupFile: string): Promise<void> {
  // 删除现有数据库
  await execAsync('dropdb -h localhost -U postgres mydb');
  
  // 创建新数据库
  await execAsync('createdb -h localhost -U postgres mydb');
  
  // 恢复备份
  await execAsync(`pg_restore -h localhost -U postgres -d mydb ${backupFile}`);
}
```

### 3.2 MySQL 恢复

```ts
async function restoreMySQL(backupFile: string): Promise<void> {
  await execAsync(`mysql -h localhost -u root -p mydb < ${backupFile}`);
}
```

### 3.3 MongoDB 恢复

```ts
async function restoreMongoDB(backupDir: string): Promise<void> {
  await execAsync(`mongorestore --host localhost --db mydb ${backupDir}`);
}
```

## 4. 恢复验证

### 4.1 数据完整性检查

```ts
async function verifyRestore(): Promise<boolean> {
  // 检查表数量
  const tableCount = await db.query('SELECT COUNT(*) FROM information_schema.tables');
  
  // 检查数据量
  const userCount = await db.query('SELECT COUNT(*) FROM users');
  
  // 检查关键数据
  const adminUser = await db.query('SELECT * FROM users WHERE role = "admin"');
  
  return tableCount > 0 && userCount > 0 && adminUser.length > 0;
}
```

## 5. 恢复测试

### 5.1 定期测试

```ts
async function testRestore(): Promise<void> {
  // 1. 创建测试环境
  const testDb = 'test_restore';
  await createTestDatabase(testDb);
  
  // 2. 恢复备份
  await restorePostgreSQL('latest-backup.sql');
  
  // 3. 验证恢复
  const isValid = await verifyRestore();
  
  if (!isValid) {
    throw new Error('Restore test failed');
  }
  
  // 4. 清理测试环境
  await dropTestDatabase(testDb);
}
```

## 6. 最佳实践

### 6.1 恢复流程

- 制定恢复流程文档
- 定期测试恢复流程
- 准备恢复脚本
- 培训恢复人员

### 6.2 恢复优化

- 优化恢复速度
- 减少恢复时间
- 自动化恢复流程
- 监控恢复过程

## 7. 注意事项

- **数据安全**：恢复前备份当前数据
- **恢复验证**：恢复后验证数据完整性
- **业务影响**：最小化业务中断时间
- **恢复测试**：定期测试恢复流程

## 8. 常见问题

### 8.1 如何快速恢复？

使用物理备份、优化恢复流程、准备恢复脚本。

### 8.2 如何验证恢复？

检查数据完整性、关键数据验证、业务功能测试。

### 8.3 如何减少恢复时间？

使用增量备份、优化恢复流程、自动化恢复。

## 9. 实践任务

1. **实现恢复**：实现数据库恢复功能
2. **恢复验证**：实现恢复验证功能
3. **恢复测试**：定期测试恢复流程
4. **恢复优化**：优化恢复速度和流程
5. **文档化**：文档化恢复流程和步骤

---

**下一章**：[5.11 数据库性能监控](../chapter-11-monitoring/readme.md)
