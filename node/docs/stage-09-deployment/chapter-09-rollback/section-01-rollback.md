# 9.9.1 回滚策略

## 1. 概述

回滚策略是在部署失败或新版本出现问题时，快速恢复到稳定版本的机制。有效的回滚策略可以最小化故障影响、保证服务可用性。

## 2. 回滚类型

### 2.1 自动回滚

**触发条件**：
- 健康检查失败
- 错误率超过阈值
- 性能指标异常
- 部署脚本失败

**实现**：
```ts
async function deployWithAutoRollback(version: string): Promise<void> {
  try {
    // 1. 部署新版本
    await deploy(version);
    
    // 2. 健康检查
    const healthy = await healthCheck(300); // 检查 5 分钟
    if (!healthy) {
      throw new Error('Health check failed');
    }
    
    // 3. 监控指标
    const metrics = await monitorMetrics(600); // 监控 10 分钟
    if (metrics.errorRate > 0.05) {
      throw new Error('Error rate too high');
    }
    
    console.log('Deployment successful');
  } catch (error) {
    console.error('Deployment failed, rolling back...');
    await rollback();
    throw error;
  }
}
```

### 2.2 手动回滚

**触发条件**：
- 业务问题
- 性能问题
- 安全问题
- 用户反馈

**实现**：
```ts
async function rollbackToVersion(version: string): Promise<void> {
  console.log(`Rolling back to version ${version}...`);
  
  // 1. 停止当前版本
  await stopCurrentVersion();
  
  // 2. 启动目标版本
  await startVersion(version);
  
  // 3. 验证回滚
  await healthCheck(60);
  
  console.log('Rollback completed');
}
```

## 3. 版本管理

### 3.1 版本标记

```ts
class VersionManager {
  private versions: Map<string, string> = new Map();
  
  tagVersion(version: string, image: string): void {
    this.versions.set(version, image);
  }
  
  getVersionImage(version: string): string | undefined {
    return this.versions.get(version);
  }
  
  getLatestVersion(): string {
    const versions = Array.from(this.versions.keys()).sort().reverse();
    return versions[0];
  }
  
  getPreviousVersion(current: string): string | undefined {
    const versions = Array.from(this.versions.keys()).sort().reverse();
    const index = versions.indexOf(current);
    return index > 0 ? versions[index - 1] : undefined;
  }
}
```

### 3.2 版本历史

```ts
interface DeploymentHistory {
  version: string;
  timestamp: Date;
  status: 'success' | 'failed' | 'rolled_back';
  deployedBy: string;
}

class DeploymentTracker {
  private history: DeploymentHistory[] = [];
  
  recordDeployment(version: string, status: string, user: string): void {
    this.history.push({
      version,
      timestamp: new Date(),
      status: status as any,
      deployedBy: user
    });
  }
  
  getRollbackCandidates(): string[] {
    return this.history
      .filter(h => h.status === 'success')
      .map(h => h.version)
      .reverse();
  }
}
```

## 4. 回滚实现

### 4.1 Kubernetes 回滚

```bash
# 查看部署历史
kubectl rollout history deployment/my-app

# 回滚到上一个版本
kubectl rollout undo deployment/my-app

# 回滚到特定版本
kubectl rollout undo deployment/my-app --to-revision=2

# 查看回滚状态
kubectl rollout status deployment/my-app
```

### 4.2 Docker 回滚

```bash
# 停止当前容器
docker stop my-app

# 启动旧版本
docker run -d --name my-app my-app:v1.0

# 或使用 Docker Compose
docker-compose -f docker-compose.previous.yml up -d
```

## 5. 数据库回滚

### 5.1 迁移回滚

```ts
async function rollbackDatabase(version: string): Promise<void> {
  // 执行反向迁移
  await db.migrate.rollback({
    to: version
  });
}
```

## 6. 最佳实践

### 6.1 回滚设计

- 快速回滚
- 自动化回滚
- 版本管理
- 数据一致性

### 6.2 回滚测试

- 定期测试回滚
- 验证回滚流程
- 记录回滚时间
- 优化回滚速度

## 7. 注意事项

- **数据一致性**：保证数据一致性
- **回滚速度**：快速回滚
- **版本管理**：管理版本历史
- **测试验证**：定期测试回滚

## 8. 常见问题

### 8.1 如何处理数据库迁移回滚？

使用迁移工具的回滚功能、版本兼容、数据备份。

### 8.2 如何实现快速回滚？

保留旧版本、使用蓝绿部署、自动化回滚。

### 8.3 如何验证回滚成功？

健康检查、功能测试、监控指标。

## 9. 实践任务

1. **实现回滚**：实现回滚机制
2. **版本管理**：管理版本历史
3. **自动化回滚**：实现自动回滚
4. **回滚测试**：测试回滚流程
5. **持续优化**：持续优化回滚策略

---

**下一节**：[9.9.2 灾难恢复](section-02-disaster-recovery.md)
