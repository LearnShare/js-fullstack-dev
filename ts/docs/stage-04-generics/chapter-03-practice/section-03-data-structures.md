# 4.3.3 数据结构类型化

## 概述

使用泛型类型化数据结构，提供类型安全的数据结构。本节介绍如何使用泛型类型化数据结构。

## 栈（Stack）

### 定义

```ts
class Stack<T> {
    private items: T[] = [];

    push(item: T): void {
        this.items.push(item);
    }

    pop(): T | undefined {
        return this.items.pop();
    }

    peek(): T | undefined {
        return this.items[this.items.length - 1];
    }

    isEmpty(): boolean {
        return this.items.length === 0;
    }

    size(): number {
        return this.items.length;
    }
}

// 使用
let numberStack = new Stack<number>();
numberStack.push(1);
numberStack.push(2);
let top = numberStack.pop(); // 类型为 number | undefined
```

## 队列（Queue）

### 定义

```ts
class Queue<T> {
    private items: T[] = [];

    enqueue(item: T): void {
        this.items.push(item);
    }

    dequeue(): T | undefined {
        return this.items.shift();
    }

    front(): T | undefined {
        return this.items[0];
    }

    isEmpty(): boolean {
        return this.items.length === 0;
    }

    size(): number {
        return this.items.length;
    }
}

// 使用
let stringQueue = new Queue<string>();
stringQueue.enqueue("first");
stringQueue.enqueue("second");
let first = stringQueue.dequeue(); // 类型为 string | undefined
```

## 链表（LinkedList）

### 定义

```ts
class ListNode<T> {
    value: T;
    next: ListNode<T> | null = null;

    constructor(value: T) {
        this.value = value;
    }
}

class LinkedList<T> {
    private head: ListNode<T> | null = null;

    append(value: T): void {
        const newNode = new ListNode(value);
        if (!this.head) {
            this.head = newNode;
            return;
        }
        let current = this.head;
        while (current.next) {
            current = current.next;
        }
        current.next = newNode;
    }

    find(value: T): ListNode<T> | null {
        let current = this.head;
        while (current) {
            if (current.value === value) {
                return current;
            }
            current = current.next;
        }
        return null;
    }
}
```

## 映射（Map）

### 定义

```ts
class TypedMap<K, V> {
    private data: Map<K, V> = new Map();

    set(key: K, value: V): void {
        this.data.set(key, value);
    }

    get(key: K): V | undefined {
        return this.data.get(key);
    }

    has(key: K): boolean {
        return this.data.has(key);
    }

    delete(key: K): boolean {
        return this.data.delete(key);
    }

    size(): number {
        return this.data.size;
    }
}

// 使用
let userMap = new TypedMap<number, { name: string }>();
userMap.set(1, { name: "John" });
let user = userMap.get(1); // 类型为 { name: string } | undefined
```

## 缓存（Cache）

### 定义

```ts
class Cache<T> {
    private data: Map<string, { value: T; expires: number }> = new Map();
    private defaultTTL: number;

    constructor(defaultTTL: number = 60000) {
        this.defaultTTL = defaultTTL;
    }

    set(key: string, value: T, ttl?: number): void {
        const expires = Date.now() + (ttl || this.defaultTTL);
        this.data.set(key, { value, expires });
    }

    get(key: string): T | undefined {
        const item = this.data.get(key);
        if (!item) {
            return undefined;
        }
        if (Date.now() > item.expires) {
            this.data.delete(key);
            return undefined;
        }
        return item.value;
    }
}
```

## 使用场景

### 1. 数据存储

```ts
class Storage<T> {
    private data: T[] = [];

    add(item: T): void {
        this.data.push(item);
    }

    getAll(): T[] {
        return [...this.data];
    }
}
```

### 2. 事件系统

```ts
class EventEmitter<T extends Record<string, any[]>> {
    private listeners: Map<keyof T, Array<(...args: any[]) => void>> = new Map();

    on<K extends keyof T>(event: K, listener: (...args: T[K]) => void): void {
        if (!this.listeners.has(event)) {
            this.listeners.set(event, []);
        }
        this.listeners.get(event)!.push(listener);
    }

    emit<K extends keyof T>(event: K, ...args: T[K]): void {
        const listeners = this.listeners.get(event);
        if (listeners) {
            listeners.forEach(listener => listener(...args));
        }
    }
}
```

## 常见错误

### 错误 1：类型参数使用错误

```ts
// 错误：类型参数应该在类名后
class Stack {
    items: T[];
}

// 正确
class Stack<T> {
    items: T[];
}
```

### 错误 2：类型不匹配

```ts
let stack = new Stack<number>();
// stack.push("string"); // 错误：类型不匹配
```

## 注意事项

1. **类型参数**：为数据结构提供明确的类型参数
2. **类型安全**：利用泛型提高类型安全
3. **代码复用**：使用泛型封装通用数据结构
4. **性能考虑**：考虑数据结构的性能影响

## 最佳实践

1. **明确类型**：为数据结构提供明确的类型
2. **类型安全**：利用泛型提高类型安全
3. **代码复用**：使用泛型封装通用数据结构
4. **合理设计**：合理设计数据结构的接口

## 练习

1. **栈和队列**：实现泛型的栈和队列数据结构。

2. **链表**：实现泛型的链表数据结构。

3. **映射和缓存**：实现泛型的映射和缓存数据结构。

4. **实际应用**：在实际项目中应用数据结构类型化。

完成以上练习后，泛型实战章节学习完成。阶段四学习完成，可以继续学习阶段五：高级类型系统。

## 总结

使用泛型类型化数据结构可以提供类型安全的数据结构。可以定义栈、队列、链表、映射、缓存等数据结构。理解数据结构类型化是学习 TypeScript 泛型实战的关键。

## 相关资源

- [TypeScript 泛型文档](https://www.typescriptlang.org/docs/handbook/2/generics.html)
