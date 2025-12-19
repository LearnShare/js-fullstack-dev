# 2.5.4 自定义事件

## 1. 概述

自定义事件是 EventEmitter 的高级用法，允许开发者创建自己的事件系统。通过继承 EventEmitter 或使用 EventEmitter 实例，可以定义符合业务需求的自定义事件。理解自定义事件有助于构建灵活、解耦的应用架构。

## 2. 特性说明

- **继承支持**：可以继承 EventEmitter 创建自定义类。
- **事件命名**：可以使用命名空间组织事件（如 `user:created`）。
- **事件数据**：可以传递复杂的数据结构。
- **事件链**：可以创建事件链，一个事件触发另一个事件。
- **事件过滤**：可以实现事件过滤和条件触发。

## 3. 语法与定义

### 继承 EventEmitter

```ts
import { EventEmitter } from 'node:events';

class CustomClass extends EventEmitter {
    // 自定义方法
    customMethod() {
        this.emit('custom:event', data);
    }
}
```

### 使用 EventEmitter 实例

```ts
import { EventEmitter } from 'node:events';

const eventBus = new EventEmitter();

// 作为事件总线使用
eventBus.emit('global:event', data);
```

## 4. 基本用法

### 示例 1：继承 EventEmitter

```ts
// 文件: custom-events-inherit.ts
// 功能: 继承 EventEmitter 创建自定义事件

import { EventEmitter } from 'node:events';

class UserManager extends EventEmitter {
    private users: Map<number, any> = new Map();
    
    createUser(userData: any) {
        const user = {
            id: Date.now(),
            ...userData,
            createdAt: new Date()
        };
        
        this.users.set(user.id, user);
        this.emit('user:created', user);
        return user;
    }
    
    updateUser(id: number, updates: any) {
        const user = this.users.get(id);
        if (user) {
            const updated = { ...user, ...updates, updatedAt: new Date() };
            this.users.set(id, updated);
            this.emit('user:updated', { old: user, new: updated });
            return updated;
        }
        this.emit('user:notfound', id);
    }
    
    deleteUser(id: number) {
        const user = this.users.get(id);
        if (user) {
            this.users.delete(id);
            this.emit('user:deleted', user);
        }
    }
}

const userManager = new UserManager();

// 监听自定义事件
userManager.on('user:created', (user) => {
    console.log('User created:', user);
});

userManager.on('user:updated', ({ old, new: updated }) => {
    console.log('User updated:', { from: old, to: updated });
});

userManager.on('user:deleted', (user) => {
    console.log('User deleted:', user);
});

// 使用
userManager.createUser({ name: 'Alice', email: 'alice@example.com' });
```

### 示例 2：事件总线模式

```ts
// 文件: custom-events-bus.ts
// 功能: 事件总线模式

import { EventEmitter } from 'node:events';

// 创建全局事件总线
class EventBus extends EventEmitter {
    private static instance: EventBus;
    
    static getInstance(): EventBus {
        if (!EventBus.instance) {
            EventBus.instance = new EventBus();
        }
        return EventBus.instance;
    }
}

const eventBus = EventBus.getInstance();

// 模块 A
eventBus.on('data:updated', (data) => {
    console.log('Module A received:', data);
});

// 模块 B
eventBus.on('data:updated', (data) => {
    console.log('Module B received:', data);
});

// 触发事件
eventBus.emit('data:updated', { id: 1, value: 'new data' });
```

### 示例 3：事件链

```ts
// 文件: custom-events-chain.ts
// 功能: 事件链示例

import { EventEmitter } from 'node:events';

class Workflow extends EventEmitter {
    step1() {
        console.log('Step 1');
        this.emit('step:1:completed');
    }
    
    step2() {
        console.log('Step 2');
        this.emit('step:2:completed');
    }
    
    step3() {
        console.log('Step 3');
        this.emit('workflow:completed');
    }
}

const workflow = new Workflow();

// 创建事件链
workflow.on('step:1:completed', () => {
    workflow.step2();
});

workflow.on('step:2:completed', () => {
    workflow.step3();
});

workflow.on('workflow:completed', () => {
    console.log('All steps completed');
});

// 启动工作流
workflow.step1();
```

## 5. 参数说明：自定义事件参数

| 参数类型     | 说明                                     | 示例                           |
|:-------------|:-----------------------------------------|:-------------------------------|
| **事件名称** | 自定义事件名称，建议使用命名空间          | `'user:created'`               |
| **事件数据** | 传递给监听器的数据，可以是任意类型       | `{ id: 1, name: 'Alice' }`     |
| **选项对象** | 事件选项（如 `once`、`prependListener`）| `{ once: true }`               |

## 6. 返回值与状态说明

自定义事件的返回值：

| 返回类型 | 说明                                     |
|:---------|:-----------------------------------------|
| **Boolean**| `emit()` 返回是否有监听器处理了事件     |
| **EventEmitter**| 监听方法返回 EventEmitter 实例          |

## 7. 代码示例：完整的自定义事件系统

以下示例演示了如何构建完整的自定义事件系统：

```ts
// 文件: custom-events-complete.ts
// 功能: 完整的自定义事件系统

import { EventEmitter } from 'node:events';

interface EventData {
    timestamp: number;
    source: string;
    data: any;
}

class EventSystem extends EventEmitter {
    private eventHistory: EventData[] = [];
    
    emitWithHistory(eventName: string, data: any) {
        const eventData: EventData = {
            timestamp: Date.now(),
            source: eventName,
            data
        };
        
        this.eventHistory.push(eventData);
        this.emit(eventName, eventData);
        this.emit('*', eventData); // 通配符事件
    }
    
    getHistory(): EventData[] {
        return [...this.eventHistory];
    }
    
    getHistoryByEvent(eventName: string): EventData[] {
        return this.eventHistory.filter(e => e.source === eventName);
    }
}

const eventSystem = new EventSystem();

// 监听特定事件
eventSystem.on('user:created', (eventData: EventData) => {
    console.log('User created:', eventData);
});

// 监听所有事件
eventSystem.on('*', (eventData: EventData) => {
    console.log('Any event:', eventData.source);
});

// 使用
eventSystem.emitWithHistory('user:created', { id: 1, name: 'Alice' });
eventSystem.emitWithHistory('user:updated', { id: 1, name: 'Bob' });

console.log('History:', eventSystem.getHistory());
```

## 8. 输出结果说明

自定义事件的输出结果：

```text
Any event: user:created
User created: { timestamp: 1234567890, source: 'user:created', data: { id: 1, name: 'Alice' } }
Any event: user:updated
History: [ { timestamp: 1234567890, source: 'user:created', ... }, ... ]
```

**逻辑解析**：
- 自定义事件系统记录所有事件历史
- 支持通配符事件监听所有事件
- 可以查询特定事件的历史记录

## 9. 使用场景

### 1. 业务事件系统

实现业务领域的事件系统：

```ts
// 业务事件系统示例
class OrderService extends EventEmitter {
    createOrder(orderData: any) {
        const order = { ...orderData, status: 'pending' };
        this.emit('order:created', order);
        return order;
    }
    
    processOrder(orderId: number) {
        this.emit('order:processing', orderId);
        // 处理逻辑
        this.emit('order:processed', orderId);
    }
}
```

### 2. 插件系统

实现插件系统：

```ts
// 插件系统示例
class PluginManager extends EventEmitter {
    private plugins: Map<string, any> = new Map();
    
    register(name: string, plugin: any) {
        this.plugins.set(name, plugin);
        this.emit('plugin:registered', { name, plugin });
    }
    
    execute(name: string, data: any) {
        const plugin = this.plugins.get(name);
        if (plugin) {
            this.emit('plugin:executing', { name, data });
            const result = plugin.execute(data);
            this.emit('plugin:executed', { name, result });
            return result;
        }
    }
}
```

### 3. 状态管理

实现状态管理：

```ts
// 状态管理示例
class StateStore extends EventEmitter {
    private state: any = {};
    
    setState(key: string, value: any) {
        const oldValue = this.state[key];
        this.state[key] = value;
        this.emit('state:changed', { key, oldValue, newValue: value });
    }
    
    getState(key: string) {
        return this.state[key];
    }
}
```

## 10. 注意事项与常见错误

- **事件命名**：使用清晰的命名规范，建议使用命名空间
- **内存管理**：及时移除不再需要的监听器，避免内存泄漏
- **错误处理**：处理事件监听器中的错误
- **事件数据**：确保事件数据的结构清晰和文档化
- **性能考虑**：避免在事件监听器中执行耗时操作

## 11. 常见问题 (FAQ)

**Q: 如何实现事件过滤？**
A: 在监听器中添加条件判断，或使用中间件模式过滤事件。

**Q: 如何实现事件优先级？**
A: 使用 `prependListener()` 将高优先级监听器前置，或使用自定义优先级系统。

**Q: 如何实现事件中间件？**
A: 在 `emit()` 前添加中间件处理逻辑，或使用装饰器模式。

## 12. 最佳实践

- **命名规范**：使用命名空间组织事件（如 `module:action`）
- **文档说明**：为自定义事件提供文档说明
- **类型安全**：使用 TypeScript 定义事件数据类型
- **错误处理**：完善的错误处理和日志记录
- **测试覆盖**：为自定义事件编写测试

## 13. 对比分析：不同事件模式

| 模式           | 特点                                     | 适用场景                       |
|:---------------|:-----------------------------------------|:-------------------------------|
| **继承模式**   | 类继承 EventEmitter                      | 需要封装业务逻辑的类           |
| **组合模式**   | 类包含 EventEmitter 实例                 | 需要更灵活的控制               |
| **事件总线**   | 全局 EventEmitter 实例                   | 跨模块通信                     |
| **事件链**     | 事件触发其他事件                          | 工作流、状态机                 |

## 14. 练习任务

1. **继承实践**：
   - 创建继承 EventEmitter 的类
   - 实现自定义事件
   - 处理事件错误

2. **事件总线实践**：
   - 实现全局事件总线
   - 实现跨模块通信
   - 管理事件订阅

3. **事件链实践**：
   - 实现事件链
   - 处理事件依赖
   - 实现工作流

4. **实际应用**：
   - 在实际项目中应用自定义事件
   - 实现业务事件系统
   - 添加事件日志和监控

完成以上练习后，继续学习下一章：加密与安全（crypto）。

## 总结

自定义事件是 EventEmitter 的高级用法：

- **继承支持**：可以继承 EventEmitter 创建自定义类
- **事件命名**：使用命名空间组织事件
- **灵活应用**：支持多种事件模式（继承、组合、事件总线等）
- **最佳实践**：命名规范、文档说明、类型安全、错误处理

掌握自定义事件有助于构建灵活、解耦的应用架构。

---

**最后更新**：2025-01-XX
