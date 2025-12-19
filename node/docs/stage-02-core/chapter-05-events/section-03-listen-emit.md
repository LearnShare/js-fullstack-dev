# 2.5.3 事件监听与触发

## 1. 概述

事件监听和触发是 EventEmitter 的核心功能。通过 `on()`、`once()` 等方法注册事件监听器，通过 `emit()` 方法触发事件。理解事件监听和触发的机制对于掌握 Node.js 事件系统至关重要。

## 2. 特性说明

- **多种监听方式**：支持 `on()`、`once()`、`prependListener()` 等。
- **参数传递**：支持向监听器传递多个参数。
- **同步执行**：事件监听器是同步执行的。
- **返回值**：`emit()` 返回是否有监听器处理了事件。
- **监听器顺序**：监听器按注册顺序执行。

## 3. 语法与定义

### 事件监听

```ts
// 注册事件监听器
emitter.on(eventName: string, listener: Function): EventEmitter

// 注册一次性监听器
emitter.once(eventName: string, listener: Function): EventEmitter

// 前置监听器（优先执行）
emitter.prependListener(eventName: string, listener: Function): EventEmitter
```

### 事件触发

```ts
// 触发事件
emitter.emit(eventName: string, ...args: any[]): boolean
```

## 4. 基本用法

### 示例 1：基本监听和触发

```ts
// 文件: events-listen-emit.ts
// 功能: 基本事件监听和触发

import { EventEmitter } from 'node:events';

const emitter = new EventEmitter();

// 注册监听器
emitter.on('data', (data: string, timestamp: number) => {
    console.log(`[${timestamp}] Data:`, data);
});

// 触发事件，传递参数
emitter.emit('data', 'Hello', Date.now());
emitter.emit('data', 'World', Date.now());
```

### 示例 2：once 一次性监听器

```ts
// 文件: events-once.ts
// 功能: 一次性事件监听器

import { EventEmitter } from 'node:events';

const emitter = new EventEmitter();

// 注册一次性监听器
emitter.once('connect', () => {
    console.log('Connected (only once)');
});

// 多次触发，但只执行一次
emitter.emit('connect');
emitter.emit('connect');
emitter.emit('connect');
```

### 示例 3：监听器执行顺序

```ts
// 文件: events-order.ts
// 功能: 监听器执行顺序

import { EventEmitter } from 'node:events';

const emitter = new EventEmitter();

// 按顺序注册监听器
emitter.on('event', () => console.log('Listener 1'));
emitter.on('event', () => console.log('Listener 2'));

// 前置监听器（优先执行）
emitter.prependListener('event', () => console.log('Listener 0'));

// 触发事件
emitter.emit('event');
```

## 5. 参数说明：监听和触发方法

### on/once 参数

| 参数名       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **eventName**| String   | 事件名称                                 | `'data'`                       |
| **listener** | Function | 事件监听器函数                           | `(data) => {}`                 |

### emit 参数

| 参数名       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **eventName**| String   | 事件名称                                 | `'data'`                       |
| **...args**  | Any      | 传递给监听器的参数（可变参数）           | `'data', 123`                  |

## 6. 返回值与状态说明

### on/once 返回值

| 返回类型     | 说明                                     |
|:-------------|:-----------------------------------------|
| **EventEmitter**| 返回 EventEmitter 实例，支持链式调用   |

### emit 返回值

| 返回类型 | 说明                                     |
|:---------|:-----------------------------------------|
| **Boolean**| 如果有监听器返回 true，否则返回 false    |

## 7. 代码示例：完整的事件处理

以下示例演示了完整的事件监听和触发：

```ts
// 文件: events-complete.ts
// 功能: 完整的事件处理示例

import { EventEmitter } from 'node:events';

class TaskManager extends EventEmitter {
    private tasks: string[] = [];
    
    addTask(task: string) {
        this.tasks.push(task);
        this.emit('task:added', task, this.tasks.length);
    }
    
    completeTask(index: number) {
        if (index >= 0 && index < this.tasks.length) {
            const task = this.tasks[index];
            this.tasks.splice(index, 1);
            this.emit('task:completed', task, this.tasks.length);
        }
    }
    
    getTasks() {
        return [...this.tasks];
    }
}

const taskManager = new TaskManager();

// 注册多个监听器
taskManager.on('task:added', (task: string, total: number) => {
    console.log(`Task added: ${task} (Total: ${total})`);
});

taskManager.on('task:completed', (task: string, remaining: number) => {
    console.log(`Task completed: ${task} (Remaining: ${remaining})`);
});

// 一次性监听器
taskManager.once('task:added', () => {
    console.log('First task added!');
});

// 使用
taskManager.addTask('Learn Node.js');
taskManager.addTask('Build API');
taskManager.completeTask(0);
```

## 8. 输出结果说明

事件触发的输出结果：

```text
First task added!
Task added: Learn Node.js (Total: 1)
Task added: Build API (Total: 2)
Task completed: Learn Node.js (Remaining: 1)
```

**逻辑解析**：
- `once()` 监听器只执行一次
- `on()` 监听器每次都会执行
- 监听器按注册顺序执行
- 可以传递多个参数给监听器

## 9. 使用场景

### 1. 异步操作通知

通知异步操作完成：

```ts
// 异步操作通知示例
class AsyncTask extends EventEmitter {
    async execute() {
        this.emit('start');
        try {
            const result = await someAsyncOperation();
            this.emit('success', result);
        } catch (error) {
            this.emit('error', error);
        } finally {
            this.emit('end');
        }
    }
}
```

### 2. 状态变化通知

通知状态变化：

```ts
// 状态变化通知示例
class StateManager extends EventEmitter {
    private state: any = {};
    
    setState(key: string, value: any) {
        const oldValue = this.state[key];
        this.state[key] = value;
        this.emit('state:changed', { key, oldValue, newValue: value });
    }
}
```

### 3. 数据流处理

处理数据流：

```ts
// 数据流处理示例
class DataStream extends EventEmitter {
    process(data: string) {
        this.emit('data', data);
        if (data.includes('end')) {
            this.emit('end');
        }
    }
}
```

## 10. 注意事项与常见错误

- **函数引用**：移除监听器时需要相同的函数引用
- **同步执行**：事件监听器是同步执行的，注意性能
- **错误处理**：监听器中的错误需要处理，否则会中断执行
- **内存泄漏**：及时移除不再需要的监听器
- **参数传递**：注意参数的类型和数量

## 11. 常见问题 (FAQ)

**Q: 如何移除匿名函数监听器？**
A: 无法直接移除匿名函数，需要保存函数引用或使用命名函数。

**Q: 事件监听器是同步还是异步执行？**
A: 事件监听器是同步执行的，但可以通过 `setImmediate` 实现异步。

**Q: 如何获取事件的所有监听器？**
A: 使用 `listeners(eventName)` 方法获取指定事件的所有监听器。

## 12. 最佳实践

- **命名函数**：使用命名函数而非匿名函数，便于移除
- **错误处理**：在监听器中处理错误，避免影响其他监听器
- **参数验证**：验证传递给监听器的参数
- **性能考虑**：避免在监听器中执行耗时操作
- **文档说明**：为事件和参数提供文档说明

## 13. 对比分析：on vs once vs prependListener

| 维度             | on()                                      | once()                                    | prependListener()                         |
|:-----------------|:------------------------------------------|:------------------------------------------|:------------------------------------------|
| **执行次数**     | 每次触发都执行                            | 只执行一次                                | 每次触发都执行                            |
| **执行顺序**     | 按注册顺序执行                            | 按注册顺序执行                            | 优先执行（在其他监听器之前）              |
| **自动移除**     | 需要手动移除                               | 自动移除                                  | 需要手动移除                              |

## 14. 练习任务

1. **事件监听实践**：
   - 使用 `on()` 注册监听器
   - 使用 `once()` 注册一次性监听器
   - 理解监听器的执行顺序

2. **事件触发实践**：
   - 使用 `emit()` 触发事件
   - 传递多个参数给监听器
   - 理解 `emit()` 的返回值

3. **监听器管理实践**：
   - 添加和移除监听器
   - 使用 `prependListener()` 前置监听器
   - 查询监听器信息

4. **实际应用**：
   - 在实际项目中应用事件监听和触发
   - 实现复杂的事件流程
   - 处理事件错误

完成以上练习后，继续学习下一节：自定义事件。

## 总结

事件监听和触发是 EventEmitter 的核心功能：

- **监听方法**：`on()`、`once()`、`prependListener()` 等
- **触发方法**：`emit()` 触发事件并传递参数
- **执行顺序**：监听器按注册顺序执行
- **最佳实践**：使用命名函数、错误处理、参数验证

掌握事件监听和触发有助于构建事件驱动的应用。

---

**最后更新**：2025-01-XX
