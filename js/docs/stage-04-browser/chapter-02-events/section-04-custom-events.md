# 4.2.4 自定义事件

## 概述

自定义事件允许你创建和触发自己的事件，用于组件间通信和模块解耦。本节介绍如何创建、触发和监听自定义事件。

## 创建自定义事件

### 使用 Event 构造函数

**语法格式**：`new Event(type[, options])`

**参数说明**：

| 参数名    | 类型   | 说明           | 是否必需 | 默认值 |
|:----------|:-------|:---------------|:---------|:-------|
| `type`    | string | 事件类型名称    | 是       | -      |
| `options` | object | 事件配置对象    | 否       | -      |

**options 对象属性**：

| 属性名      | 类型    | 说明                           | 默认值 |
|:------------|:--------|:-------------------------------|:-------|
| `bubbles`   | boolean | 事件是否冒泡                    | false  |
| `cancelable` | boolean | 事件是否可以取消              | false  |
| `composed`  | boolean | 事件是否可以在 Shadow DOM 边界外触发 | false |

**返回值**：Event 对象

### 基本创建

```js
// 创建简单自定义事件
const event = new Event('customEvent');

// 创建带选项的自定义事件
const eventWithOptions = new Event('customEvent', {
    bubbles: true,
    cancelable: true
});
```

### 使用 CustomEvent 构造函数

**语法格式**：`new CustomEvent(type[, options])`

**参数说明**：

| 参数名    | 类型   | 说明           | 是否必需 | 默认值 |
|:----------|:-------|:---------------|:---------|:-------|
| `type`    | string | 事件类型名称    | 是       | -      |
| `options` | object | 事件配置对象    | 否       | -      |

**options 对象属性**（继承 Event 的所有属性）：

| 属性名      | 类型    | 说明                           | 默认值 |
|:------------|:--------|:-------------------------------|:-------|
| `detail`    | any     | 传递给事件处理函数的数据        | null   |
| `bubbles`   | boolean | 事件是否冒泡                    | false  |
| `cancelable` | boolean | 事件是否可以取消              | false  |
| `composed`  | boolean | 事件是否可以在 Shadow DOM 边界外触发 | false |

**返回值**：CustomEvent 对象

### 基本创建

```js
// 创建带数据的自定义事件
const customEvent = new CustomEvent('userAction', {
    detail: {
        action: 'click',
        timestamp: Date.now()
    },
    bubbles: true,
    cancelable: true
});
```

## 触发自定义事件

### 使用 dispatchEvent()

**语法格式**：`element.dispatchEvent(event)`

**参数说明**：

| 参数名   | 类型  | 说明           | 是否必需 | 默认值 |
|:---------|:------|:---------------|:---------|:-------|
| `event`  | Event | 要触发的事件对象 | 是       | -      |

**返回值**：布尔值，表示事件是否被取消（如果有 cancelable 为 true 的监听器调用了 preventDefault()）

### 基本触发

```js
const element = document.querySelector('div');

// 创建事件
const event = new CustomEvent('customEvent', {
    detail: { message: 'Hello' }
});

// 触发事件
const cancelled = element.dispatchEvent(event);
console.log('事件是否被取消：', cancelled);
```

### 监听自定义事件

```js
const element = document.querySelector('div');

// 监听自定义事件
element.addEventListener('customEvent', (e) => {
    console.log('自定义事件被触发');
    console.log('事件数据：', e.detail);
});

// 触发事件
const event = new CustomEvent('customEvent', {
    detail: { message: 'Hello World' }
});
element.dispatchEvent(event);
```

## 实际应用场景

### 场景 1：组件间通信

```js
// 组件 A：触发事件
class ComponentA {
    constructor(element) {
        this.element = element;
    }
    
    notify(data) {
        const event = new CustomEvent('componentAEvent', {
            detail: data,
            bubbles: true
        });
        this.element.dispatchEvent(event);
    }
}

// 组件 B：监听事件
class ComponentB {
    constructor(element) {
        this.element = element;
        this.element.addEventListener('componentAEvent', (e) => {
            console.log('收到组件 A 的事件：', e.detail);
        });
    }
}

// 使用
const container = document.querySelector('#container');
const compA = new ComponentA(container);
const compB = new ComponentB(container);

compA.notify({ message: 'Hello from A' });
```

### 场景 2：状态变化通知

```js
// 状态管理器
class StateManager {
    constructor(element) {
        this.element = element;
        this.state = {};
    }
    
    setState(newState) {
        const oldState = { ...this.state };
        this.state = { ...this.state, ...newState };
        
        // 触发状态变化事件
        const event = new CustomEvent('stateChange', {
            detail: {
                oldState,
                newState: this.state
            },
            bubbles: true
        });
        this.element.dispatchEvent(event);
    }
}

// 使用
const manager = new StateManager(document.body);
document.body.addEventListener('stateChange', (e) => {
    console.log('状态变化：', e.detail);
});

manager.setState({ count: 1 });
manager.setState({ count: 2 });
```

### 场景 3：插件系统

```js
// 插件系统
class PluginSystem {
    constructor(element) {
        this.element = element;
        this.plugins = [];
    }
    
    register(plugin) {
        this.plugins.push(plugin);
        plugin.init(this.element);
    }
    
    trigger(eventName, data) {
        const event = new CustomEvent(eventName, {
            detail: data,
            bubbles: true
        });
        this.element.dispatchEvent(event);
    }
}

// 插件接口
class Plugin {
    init(element) {
        // 插件初始化
        element.addEventListener('pluginEvent', this.handle.bind(this));
    }
    
    handle(e) {
        console.log('插件处理事件：', e.detail);
    }
}

// 使用
const system = new PluginSystem(document.body);
system.register(new Plugin());
system.trigger('pluginEvent', { data: 'test' });
```

## 事件命名空间

### 使用命名空间避免冲突

```js
// 使用命名空间创建事件
const event = new CustomEvent('myApp:userLogin', {
    detail: { userId: 123 }
});

// 监听命名空间事件
element.addEventListener('myApp:userLogin', (e) => {
    console.log('用户登录：', e.detail);
});
```

## 事件继承

### 继承 Event 类

```js
// 创建自定义事件类
class MyCustomEvent extends Event {
    constructor(type, data, options = {}) {
        super(type, options);
        this.data = data;
    }
}

// 使用
const event = new MyCustomEvent('myEvent', { message: 'Hello' });
element.dispatchEvent(event);
```

## 注意事项

1. **事件命名**：使用清晰的命名，避免与原生事件冲突
2. **事件数据**：使用 detail 属性传递数据
3. **冒泡设置**：根据需求设置 bubbles 选项
4. **性能考虑**：避免频繁触发自定义事件
5. **清理监听器**：及时移除不再需要的监听器

## 常见错误

### 错误 1：忘记传递 detail

```js
// 错误：使用 Event 而不是 CustomEvent
const event = new Event('customEvent');
event.detail = { data: 'test' }; // detail 属性可能不存在

// 正确：使用 CustomEvent
const event = new CustomEvent('customEvent', {
    detail: { data: 'test' }
});
```

### 错误 2：事件不冒泡

```js
// 错误：事件不冒泡，父元素无法监听
const event = new CustomEvent('customEvent', {
    detail: { data: 'test' }
    // 默认 bubbles: false
});

// 正确：需要冒泡时设置 bubbles
const event = new CustomEvent('customEvent', {
    detail: { data: 'test' },
    bubbles: true
});
```

### 错误 3：事件名称冲突

```js
// 错误：使用通用名称可能冲突
const event = new CustomEvent('click', {
    detail: { data: 'test' }
});

// 正确：使用命名空间或特定名称
const event = new CustomEvent('myApp:customClick', {
    detail: { data: 'test' }
});
```

## 最佳实践

1. **使用 CustomEvent**：需要传递数据时使用 CustomEvent
2. **命名规范**：使用清晰的命名，考虑使用命名空间
3. **合理冒泡**：根据需求设置 bubbles 选项
4. **文档说明**：自定义事件应该文档化
5. **测试验证**：确保自定义事件按预期工作

## 练习

1. **基本自定义事件**：创建一个按钮，点击后触发自定义事件，并监听该事件。

2. **组件通信**：创建两个组件，使用自定义事件实现组件间通信。

3. **状态管理**：实现一个简单的状态管理器，状态变化时触发自定义事件。

4. **事件命名空间**：创建一个事件系统，使用命名空间管理不同类型的事件。

5. **事件继承**：创建一个自定义事件类，继承 Event，添加自定义属性和方法。

完成以上练习后，你已经掌握了事件处理的核心技能。

## 总结

自定义事件允许创建和触发自己的事件，用于组件间通信和模块解耦。使用 CustomEvent 构造函数可以创建带数据的自定义事件，使用 dispatchEvent() 方法可以触发事件。自定义事件在组件化开发中非常有用，可以实现松耦合的架构。

## 相关资源

- [MDN：CustomEvent](https://developer.mozilla.org/zh-CN/docs/Web/API/CustomEvent)
- [MDN：Event](https://developer.mozilla.org/zh-CN/docs/Web/API/Event)
- [MDN：dispatchEvent](https://developer.mozilla.org/zh-CN/docs/Web/API/EventTarget/dispatchEvent)
