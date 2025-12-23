# 6.2.3 ABAC（基于属性的访问控制）

## 1. 概述

ABAC（Attribute-Based Access Control）是基于属性的访问控制模型，通过用户属性、资源属性、环境属性等判断权限。ABAC 灵活强大，适合复杂的权限控制场景。

## 2. ABAC 模型

### 2.1 核心概念

- **主体属性（Subject Attributes）**：用户属性（角色、部门、级别等）
- **资源属性（Resource Attributes）**：资源属性（类型、所有者、敏感度等）
- **环境属性（Environment Attributes）**：环境属性（时间、地点、IP 等）
- **操作（Action）**：要执行的操作

### 2.2 决策模型

```
IF (主体属性 AND 资源属性 AND 环境属性) THEN 允许/拒绝
```

## 3. 策略定义

### 3.1 策略示例

```ts
interface Policy {
  id: string;
  name: string;
  effect: 'allow' | 'deny';
  conditions: Condition[];
}

interface Condition {
  attribute: string;
  operator: 'equals' | 'contains' | 'greaterThan' | 'lessThan';
  value: any;
}

const policies: Policy[] = [
  {
    id: '1',
    name: '部门管理员可以访问本部门文档',
    effect: 'allow',
    conditions: [
      { attribute: 'user.role', operator: 'equals', value: 'department_admin' },
      { attribute: 'resource.department', operator: 'equals', value: 'user.department' }
    ]
  },
  {
    id: '2',
    name: '工作时间外禁止访问敏感资源',
    effect: 'deny',
    conditions: [
      { attribute: 'resource.sensitivity', operator: 'equals', value: 'high' },
      { attribute: 'environment.hour', operator: 'lessThan', value: 9 }
    ]
  }
];
```

## 4. Node.js 实现

### 4.1 策略评估引擎

```ts
interface Context {
  user: {
    id: number;
    role: string;
    department: string;
    level: number;
  };
  resource: {
    id: number;
    type: string;
    owner: number;
    department: string;
    sensitivity: string;
  };
  environment: {
    time: Date;
    ip: string;
    location: string;
  };
  action: string;
}

function evaluateCondition(condition: Condition, context: Context): boolean {
  const { attribute, operator, value } = condition;
  const attributeValue = getAttributeValue(attribute, context);
  
  switch (operator) {
    case 'equals':
      return attributeValue === value;
    case 'contains':
      return Array.isArray(attributeValue) && attributeValue.includes(value);
    case 'greaterThan':
      return attributeValue > value;
    case 'lessThan':
      return attributeValue < value;
    default:
      return false;
  }
}

function getAttributeValue(path: string, context: Context): any {
  const parts = path.split('.');
  let value: any = context;
  
  for (const part of parts) {
    value = value[part];
    if (value === undefined) {
      return undefined;
    }
  }
  
  return value;
}

function evaluatePolicy(policy: Policy, context: Context): boolean {
  const allConditionsMet = policy.conditions.every((condition: Condition) => 
    evaluateCondition(condition, context)
  );
  
  if (allConditionsMet) {
    return policy.effect === 'allow';
  }
  
  return false;
}

async function checkAccess(context: Context): Promise<boolean> {
  for (const policy of policies) {
    if (evaluatePolicy(policy, context)) {
      return policy.effect === 'allow';
    }
  }
  
  return false; // 默认拒绝
}
```

### 4.2 权限中间件

```ts
function requireABAC(resourceType: string, action: string) {
  return async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    const user = (req as any).user;
    const resourceId = req.params.id;
    
    const resource = await getResource(resourceId);
    const context: Context = {
      user: {
        id: user.id,
        role: user.role,
        department: user.department,
        level: user.level
      },
      resource: {
        id: resource.id,
        type: resourceType,
        owner: resource.ownerId,
        department: resource.department,
        sensitivity: resource.sensitivity
      },
      environment: {
        time: new Date(),
        ip: req.ip,
        location: req.headers['x-location'] as string || ''
      },
      action
    };
    
    const hasAccess = await checkAccess(context);
    if (!hasAccess) {
      res.status(403).json({ message: 'Forbidden' });
      return;
    }
    
    next();
  };
}

// 使用
app.delete('/documents/:id', requireABAC('document', 'delete'), (req: Request, res: Response): void => {
  // 删除文档
});
```

## 5. 策略管理

### 5.1 策略存储

```ts
interface PolicyStore {
  save(policy: Policy): Promise<void>;
  findById(id: string): Promise<Policy | null>;
  findAll(): Promise<Policy[]>;
  delete(id: string): Promise<void>;
}

class DatabasePolicyStore implements PolicyStore {
  async save(policy: Policy): Promise<void> {
    await db.query(
      'INSERT INTO policies (id, name, effect, conditions) VALUES ($1, $2, $3, $4)',
      [policy.id, policy.name, policy.effect, JSON.stringify(policy.conditions)]
    );
  }
  
  async findById(id: string): Promise<Policy | null> {
    const result = await db.query('SELECT * FROM policies WHERE id = $1', [id]);
    if (result.length === 0) {
      return null;
    }
    return {
      id: result[0].id,
      name: result[0].name,
      effect: result[0].effect,
      conditions: JSON.parse(result[0].conditions)
    };
  }
  
  async findAll(): Promise<Policy[]> {
    const results = await db.query('SELECT * FROM policies');
    return results.map((row: any) => ({
      id: row.id,
      name: row.name,
      effect: row.effect,
      conditions: JSON.parse(row.conditions)
    }));
  }
  
  async delete(id: string): Promise<void> {
    await db.query('DELETE FROM policies WHERE id = $1', [id]);
  }
}
```

## 6. 最佳实践

### 6.1 策略设计

- 策略清晰明确
- 避免策略冲突
- 策略可测试
- 策略可审计

### 6.2 性能优化

- 缓存策略评估结果
- 优化策略匹配算法
- 使用策略索引
- 批量评估策略

## 7. 注意事项

- **策略复杂度**：避免策略过于复杂
- **性能影响**：注意策略评估的性能
- **策略冲突**：处理策略冲突
- **策略测试**：充分测试策略

## 8. 常见问题

### 8.1 如何选择 RBAC 还是 ABAC？

简单场景用 RBAC，复杂场景用 ABAC。

### 8.2 如何处理策略冲突？

定义策略优先级，按优先级评估策略。

### 8.3 如何优化策略性能？

缓存策略评估结果，优化策略匹配算法。

## 9. 实践任务

1. **设计策略**：设计 ABAC 策略模型
2. **实现引擎**：实现策略评估引擎
3. **权限中间件**：实现 ABAC 权限中间件
4. **策略管理**：实现策略管理功能
5. **性能优化**：优化策略评估性能

---

**下一节**：[6.2.4 权限中间件实现](section-04-middleware.md)
