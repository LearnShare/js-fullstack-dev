# 2.5.2 EventEmitter 基础

## 1. 概述

EventEmitter 是 Node.js 事件系统的核心类，提供了事件监听和触发的功能。理解 EventEmitter 的使用是掌握 Node.js 事件系统的基础。许多 Node.js 内置模块都继承自 EventEmitter，如 HTTP 服务器、Stream 等。

## 2. 特性说明

- **事件监听**：可以监听多个事件，支持多个监听器。
- **事件触发**：可以触发事件，调用所有注册的监听器。
- **链式调用**：支持链式调用，提高代码可读性。
- **错误处理**：支持 error 事件，处理错误情况。
- **监听器管理**：可以添加、移除、查询监听器。

## 3. 语法与定义

### 创建 EventEmitter

```ts
import { EventEmitter } from 'node:events';

const emitter = new EventEmitter();
```

### 继承 EventEmitter

```ts
import { EventEmitter } from 'node:events';

class MyClass extends EventEmitter {
    // 类定义
}
```

## 4. 基本用法

### 示例 1：基本事件监听和触发

```ts
// 文件: eventemitter-basic.ts
// 功能: EventEmitter 基本用法

import { EventEmitter } from 'node:events';

const emitter = new EventEmitter();

// 注册事件监听器
emitter.on('data', (data: string) => {
    console.log('Received data:', data);
});

// 触发事件
emitter.emit('data', 'Hello, World!');
emitter.emit('data', 'Node.js');
```

### 示例 2：多个监听器

```ts
// 文件: eventemitter-multiple.ts
// 功能: 多个事件监听器

import { EventEmitter } from 'node:events';

const emitter = new EventEmitter();

// 注册多个监听器
emitter.on('event', () => console.log('Listener 1'));
emitter.on('event', () => console.log('Listener 2'));
emitter.on('event', () => console.log('Listener 3'));

// 触发事件，所有监听器都会执行
emitter.emit('event');
```

### 示例 3：继承 EventEmitter

```ts
// 文件: eventemitter-inherit.ts
// 功能: 继承 EventEmitter

import { EventEmitter } from 'node:events';

class UserService extends EventEmitter {
    private users: any[] = [];
    
    addUser(user: any) {
        this.users.push(user);
        this.emit('user:added', user);
    }
    
    removeUser(id: number) {
        const user = this.users.find(u => u.id === id);
        if (user) {
            this.users = this.users.filter(u => u.id !== id);
            this.emit('user:removed', user);
        }
    }
}

const userService = new UserService();

userService.on('user:added', (user) => {
    console.log('User added:', user);
});

userService.on('user:removed', (user) => {
    console.log('User removed:', user);
});

userService.addUser({ id: 1, name: 'Alice' });
userService.removeUser(1);
```

## 5. 参数说明：EventEmitter 常用方法

### on 方法

| 参数名     | 类型     | 说明                                     | 示例                           |
|:-----------|:---------|:-----------------------------------------|:-------------------------------|
| **eventName**| String | 事件名称                                 | `'data'`                       |
| **listener** | Function | 事件监听器函数                           | `(data) => {}`                 |

### emit 方法

| 参数名     | 类型     | 说明                                     | 示例                           |
|:-----------|:---------|:-----------------------------------------|:-------------------------------|
| **eventName**| String | 事件名称                                 | `'data'`                       |
| **...args** | Any      | 传递给监听器的参数（可变参数）           | `'data', 123, { key: 'value' }`|

## 6. 返回值与状态说明

### on 方法返回值

| 返回类型     | 说明                                     |
|:-------------|:-----------------------------------------|
| **EventEmitter**| 返回 EventEmitter 实例，支持链式调用   |

### emit 方法返回值

| 返回类型 | 说明                                     |
|:---------|:-----------------------------------------|
| **Boolean**| 如果有监听器处理了该事件返回 true，否则返回 false|

## 7. 代码示例：完整的 EventEmitter 使用

以下示例演示了 EventEmitter 的完整使用：

```ts
// 文件: eventemitter-complete.ts
// 功能: EventEmitter 完整使用示例

import { EventEmitter } from 'node:events';

class DataProcessor extends EventEmitter {
    process(data: string) {
        this.emit('start');
        
        try {
            const processed = data.toUpperCase();
            this.emit('data', processed);
            this.emit('end');
        } catch (error) {
            this.emit('error', error);
        }
    }
}

const processor = new DataProcessor();

// 注册多个事件监听器
processor.on('start', () => {
    console.log('Processing started');
});

processor.on('data', (data: string) => {
    console.log('Processed data:', data);
});

processor.on('end', () => {
    console.log('Processing completed');
});

processor.on('error', (error: Error) => {
    console.error('Error:', error);
});

// 处理数据
processor.process('hello, world');
```

## 8. 输出结果说明

事件触发的输出结果：

```text
Processing started
Processed data: HELLO, WORLD
Processing completed
```

**逻辑解析**：
- `start` 事件在开始处理时触发
- `data` 事件在处理完成后触发，传递处理后的数据
- `end` 事件在处理结束时触发
- 如果发生错误，触发 `error` 事件

## 9. 使用场景

### 1. 自定义类事件

为自定义类添加事件支持：

```ts
// 自定义类事件示例
class FileWatcher extends EventEmitter {
    watch(filePath: string) {
        // 监听文件变化
        this.emit('change', filePath);
    }
}
```

### 2. 状态机

实现状态机：

```ts
// 状态机示例
class StateMachine extends EventEmitter {
    private state: string = 'idle';
    
    transition(newState: string) {
        const oldState = this.state;
        this.state = newState;
        this.emit('state:changed', { from: oldState, to: newState });
    }
}
```

### 3. 异步操作通知

通知异步操作完成：

```ts
// 异步操作通知示例
class AsyncOperation extends EventEmitter {
    async execute() {
        this.emit('start');
        try {
            const result = await someAsyncOperation();
            this.emit('success', result);
        } catch (error) {
            this.emit('error', error);
        }
    }
}
```

## 10. 注意事项与常见错误

- **错误事件**：必须监听 `error` 事件，否则会抛出未捕获的异常
- **内存泄漏**：及时移除不再需要的监听器
- **监听器顺序**：监听器按注册顺序执行
- **同步执行**：事件监听器是同步执行的
- **监听器数量**：默认最多 10 个监听器，超过会警告

## 11. 常见问题 (FAQ)

**Q: 如何移除事件监听器？**
A: 使用 `off()` 或 `removeListener()` 方法，需要传入相同的函数引用。

**Q: 如何只执行一次的事件监听器？**
A: 使用 `once()` 方法注册监听器，执行一次后自动移除。

**Q: 如何获取所有事件名称？**
A: 使用 `eventNames()` 方法获取所有已注册的事件名称。

## 12. 最佳实践

- **错误处理**：始终监听 `error` 事件
- **内存管理**：及时移除不再需要的监听器
- **事件命名**：使用清晰的命名规范（如 `user:created`）
- **链式调用**：利用链式调用提高代码可读性
- **文档说明**：为自定义事件提供文档说明

## 13. 对比分析：on vs once

| 维度             | on()                                      | once()                                    |
|:-----------------|:------------------------------------------|:------------------------------------------|
| **执行次数**     | 每次触发都执行                            | 只执行一次，然后自动移除                  |
| **自动移除**     | 需要手动移除                               | 自动移除                                  |
| **适用场景**     | 需要持续监听的事件                         | 只需要执行一次的事件                      |

## 14. 练习任务

1. **EventEmitter 基础实践**：
   - 创建 EventEmitter 实例
   - 注册和触发事件
   - 理解事件的基本流程

2. **继承实践**：
   - 创建继承 EventEmitter 的类
   - 实现自定义事件
   - 处理事件错误

3. **监听器管理实践**：
   - 添加和移除监听器
   - 使用 `once()` 注册一次性监听器
   - 查询监听器数量

4. **实际应用**：
   - 在实际项目中应用 EventEmitter
   - 实现自定义事件系统
   - 处理复杂的事件流程

完成以上练习后，继续学习下一节：事件监听与触发。

## 总结

EventEmitter 是 Node.js 事件系统的基础：

- **核心类**：提供事件监听和触发功能
- **继承支持**：可以继承 EventEmitter 创建自定义类
- **链式调用**：支持链式调用，提高代码可读性
- **错误处理**：必须处理 error 事件

掌握 EventEmitter 有助于理解 Node.js 的事件驱动模型。

---

**最后更新**：2025-01-XX
