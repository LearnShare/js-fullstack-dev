# 2.11.3 Proxy 高级用法

## 概述

本节介绍 Proxy 的高级应用，包括可撤销代理、代理链、函数代理、数组代理、类代理等高级用法。

## 可撤销代理

### Proxy.revocable()

**语法格式**：`Proxy.revocable(target, handler)`

**参数说明**：

| 参数名    | 类型   | 说明                    | 是否必需 | 默认值 |
|:----------|:-------|:------------------------|:---------|:-------|
| `target`  | object | 要代理的目标对象         | 是       | -      |
| `handler` | object | 拦截器对象               | 是       | -      |

**返回值**：包含 `proxy` 和 `revoke` 方法的对象

### 基本使用

```js
const target = { name: 'test' };
const { proxy, revoke } = Proxy.revocable(target, {
    get(target, prop) {
        return target[prop];
    }
});

console.log(proxy.name); // "test"
revoke(); // 撤销代理
// console.log(proxy.name); // TypeError: Cannot perform 'get' on a proxy that has been revoked
```

### 应用场景

```js
// 临时访问控制
function createTemporaryAccess(obj, duration) {
    const { proxy, revoke } = Proxy.revocable(obj, {
        get(target, prop) {
            return target[prop];
        }
    });
    
    setTimeout(revoke, duration);
    return proxy;
}

const obj = { data: 'secret' };
const tempProxy = createTemporaryAccess(obj, 5000);
// 5 秒后代理自动撤销
```

## 代理链

### 多层代理

可以创建多个代理，形成代理链：

```js
const target = { name: 'test' };

// 第一层代理：日志记录
const proxy1 = new Proxy(target, {
    get(target, prop) {
        console.log(`[日志] 访问: ${prop}`);
        return target[prop];
    }
});

// 第二层代理：验证
const proxy2 = new Proxy(proxy1, {
    get(target, prop) {
        console.log(`[验证] 访问: ${prop}`);
        return Reflect.get(target, prop);
    }
});

console.log(proxy2.name);
// 输出：
// [验证] 访问: name
// [日志] 访问: name
// "test"
```

## 函数代理

### 拦截函数调用

使用 `apply` 拦截器拦截函数调用：

**语法格式**：`apply(target, thisArg, argumentsList)`

**参数说明**：

| 参数名          | 类型   | 说明           | 是否必需 | 默认值 |
|:----------------|:-------|:---------------|:---------|:-------|
| `target`        | function | 目标函数      | 是       | -      |
| `thisArg`       | any    | 函数调用时的 this | 是       | -      |
| `argumentsList` | array  | 函数参数数组    | 是       | -      |

**返回值**：函数调用的返回值

### 基本使用

```js
function sum(a, b) {
    return a + b;
}

const proxy = new Proxy(sum, {
    apply(target, thisArg, args) {
        console.log(`调用函数，参数: ${args.join(', ')}`);
        const result = Reflect.apply(target, thisArg, args);
        console.log(`返回值: ${result}`);
        return result;
    }
});

console.log(proxy(1, 2));
// 输出：
// 调用函数，参数: 1, 2
// 返回值: 3
// 3
```

### 函数参数验证

```js
function divide(a, b) {
    return a / b;
}

const safeDivide = new Proxy(divide, {
    apply(target, thisArg, args) {
        const [a, b] = args;
        if (b === 0) {
            throw new Error('除数不能为 0');
        }
        return Reflect.apply(target, thisArg, args);
    }
});

console.log(safeDivide(10, 2)); // 5
// console.log(safeDivide(10, 0)); // 抛出错误
```

## 数组代理

### 拦截数组操作

```js
const target = [1, 2, 3];
const proxy = new Proxy(target, {
    get(target, prop) {
        if (prop === 'length') {
            console.log('访问数组长度');
        }
        return Reflect.get(target, prop);
    },
    set(target, prop, value) {
        console.log(`设置数组[${prop}] = ${value}`);
        return Reflect.set(target, prop, value);
    }
});

proxy.push(4); // "设置数组[3] = 4" 和 "设置数组[length] = 4"
console.log(proxy.length); // "访问数组长度" 然后输出 4
```

### 负索引支持

```js
// 使用 Proxy 实现负索引
function createNegativeIndexArray(arr) {
    return new Proxy(arr, {
        get(target, prop) {
            const index = parseInt(prop);
            if (index < 0) {
                return target[target.length + index];
            }
            return Reflect.get(target, prop);
        }
    });
}

const arr = createNegativeIndexArray([1, 2, 3, 4, 5]);
console.log(arr[-1]); // 5（最后一个元素）
console.log(arr[-2]); // 4（倒数第二个元素）
```

## 类代理

### 代理类构造函数

```js
class Person {
    constructor(name) {
        this.name = name;
    }
    
    greet() {
        return `Hello, ${this.name}!`;
    }
}

const ProxiedPerson = new Proxy(Person, {
    construct(target, args) {
        console.log(`创建 ${target.name} 实例，参数: ${args.join(', ')}`);
        return Reflect.construct(target, args);
    }
});

const person = new ProxiedPerson('John');
// 输出：创建 Person 实例，参数: John
```

### construct 拦截器

**语法格式**：`construct(target, argumentsList, newTarget)`

**参数说明**：

| 参数名          | 类型     | 说明           | 是否必需 | 默认值 |
|:----------------|:---------|:---------------|:---------|:-------|
| `target`        | function | 目标构造函数    | 是       | -      |
| `argumentsList` | array    | 构造函数参数    | 是       | -      |
| `newTarget`     | function | 实际被调用的构造函数 | 是       | -      |

**返回值**：构造的实例对象

## 属性描述符拦截

### getPrototypeOf 拦截器

```js
const target = {};
const proxy = new Proxy(target, {
    getPrototypeOf(target) {
        console.log('获取原型');
        return Reflect.getPrototypeOf(target);
    }
});

console.log(Object.getPrototypeOf(proxy));
```

### setPrototypeOf 拦截器

```js
const target = {};
const proxy = new Proxy(target, {
    setPrototypeOf(target, proto) {
        console.log('设置原型');
        return Reflect.setPrototypeOf(target, proto);
    }
});

Object.setPrototypeOf(proxy, {});
```

### isExtensible 拦截器

```js
const target = {};
const proxy = new Proxy(target, {
    isExtensible(target) {
        console.log('检查是否可扩展');
        return Reflect.isExtensible(target);
    }
});

console.log(Object.isExtensible(proxy));
```

### preventExtensions 拦截器

```js
const target = {};
const proxy = new Proxy(target, {
    preventExtensions(target) {
        console.log('阻止扩展');
        return Reflect.preventExtensions(target);
    }
});

Object.preventExtensions(proxy);
```

## 实际应用案例

### 案例 1：响应式数据

```js
// 简单的响应式系统
function reactive(target) {
    const handlers = [];
    
    const proxy = new Proxy(target, {
        set(target, prop, value) {
            const oldValue = target[prop];
            const result = Reflect.set(target, prop, value);
            if (result && oldValue !== value) {
                handlers.forEach(handler => handler(prop, value, oldValue));
            }
            return result;
        }
    });
    
    proxy.onChange = (handler) => {
        handlers.push(handler);
    };
    
    return proxy;
}

const data = reactive({ name: 'test' });
data.onChange((prop, newVal, oldVal) => {
    console.log(`${prop} 从 ${oldVal} 变为 ${newVal}`);
});

data.name = 'new name'; // 输出: name 从 test 变为 new name
```

### 案例 2：API 客户端

```js
// 使用 Proxy 创建 API 客户端
function createAPIClient(baseURL) {
    return new Proxy({}, {
        get(target, prop) {
            return async (...args) => {
                const url = `${baseURL}/${prop}`;
                const response = await fetch(url, ...args);
                return response.json();
            };
        }
    });
}

const api = createAPIClient('https://api.example.com');
// api.users() 会请求 https://api.example.com/users
```

### 案例 3：属性别名

```js
// 为属性创建别名
function createAlias(target, aliases) {
    return new Proxy(target, {
        get(target, prop) {
            if (prop in aliases) {
                return target[aliases[prop]];
            }
            return Reflect.get(target, prop);
        }
    });
}

const obj = createAlias({ firstName: 'John', lastName: 'Doe' }, {
    first: 'firstName',
    last: 'lastName'
});

console.log(obj.first);  // "John"
console.log(obj.last);   // "Doe"
```

## 注意事项

1. **性能开销**：多层代理会增加性能开销
2. **可撤销代理**：撤销后无法恢复，需要谨慎使用
3. **this 绑定**：在拦截器中注意 this 的绑定
4. **不可拦截的操作**：某些操作无法被拦截
5. **调试困难**：复杂的代理可能使调试变得困难

## 常见错误

### 错误 1：忘记撤销代理

```js
// 错误：创建了可撤销代理但忘记撤销
const { proxy } = Proxy.revocable({}, {});
// 代理一直存在，可能导致内存泄漏

// 正确：在适当时机撤销
const { proxy, revoke } = Proxy.revocable({}, {});
// 使用完毕后撤销
revoke();
```

### 错误 2：代理链过深

```js
// 错误：创建过深的代理链
let proxy = target;
for (let i = 0; i < 100; i++) {
    proxy = new Proxy(proxy, {});
}
// 性能会严重下降

// 正确：合并多个拦截器到一个 handler
const handler = {
    get(target, prop) {
        // 合并多个逻辑
    }
};
const proxy = new Proxy(target, handler);
```

## 最佳实践

1. **合并拦截器**：将多个拦截逻辑合并到一个 handler，而不是创建多层代理
2. **及时撤销**：使用可撤销代理时，在适当时机撤销
3. **性能测试**：对代理的性能进行测试，确保可接受
4. **文档说明**：清楚文档化代理的行为和用途
5. **错误处理**：在拦截器中添加适当的错误处理

## 练习

1. **可撤销代理**：创建一个可撤销代理，在 5 秒后自动撤销。

2. **函数代理**：创建一个函数代理，记录函数调用的参数和返回值。

3. **数组负索引**：使用 Proxy 实现数组的负索引支持（如 `arr[-1]` 访问最后一个元素）。

4. **响应式数据**：使用 Proxy 实现一个简单的响应式数据系统，当数据改变时触发回调。

5. **API 客户端**：使用 Proxy 创建一个动态的 API 客户端，可以根据属性名自动构建请求 URL。

完成以上练习后，继续学习下一节，了解 Reflect API。

## 总结

Proxy 的高级用法包括可撤销代理、代理链、函数代理、数组代理等。这些高级特性可以让我们实现更强大的功能，如响应式系统、API 客户端等。在使用时要注意性能开销和调试难度。

## 相关资源

- [MDN：Proxy.revocable](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Proxy/revocable)
- [MDN：Proxy handler](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy)
