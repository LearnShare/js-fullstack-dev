# 2.11.5 元编程实践

## 概述

本节通过实际案例展示 Proxy 和 Reflect 在实际开发中的应用，包括数据绑定、观察者模式、属性验证、API 封装等实际场景。

## 数据验证框架

### 实现思路

使用 Proxy 拦截属性设置，进行数据验证：

```js
function createValidator(target, rules) {
    return new Proxy(target, {
        set(target, prop, value) {
            const rule = rules[prop];
            if (rule && !rule(value)) {
                throw new Error(`属性 ${prop} 验证失败`);
            }
            return Reflect.set(target, prop, value);
        }
    });
}

// 使用
const rules = {
    age: (value) => typeof value === 'number' && value >= 0 && value <= 150,
    email: (value) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)
};

const user = createValidator({}, rules);
user.age = 25;        // 成功
user.email = 'test@example.com'; // 成功
// user.age = -5;     // 抛出错误
```

### 完整实现

```js
class Validator {
    constructor(rules = {}) {
        this.rules = rules;
    }
    
    validate(prop, value) {
        const rule = this.rules[prop];
        if (rule) {
            if (typeof rule === 'function') {
                return rule(value);
            }
            if (rule.validator && typeof rule.validator === 'function') {
                return rule.validator(value);
            }
        }
        return true;
    }
    
    createProxy(target) {
        return new Proxy(target, {
            set: (target, prop, value) => {
                if (!this.validate(prop, value)) {
                    const rule = this.rules[prop];
                    const message = rule?.message || `属性 ${prop} 验证失败`;
                    throw new Error(message);
                }
                return Reflect.set(target, prop, value);
            }
        });
    }
}

// 使用
const validator = new Validator({
    age: {
        validator: (value) => typeof value === 'number' && value >= 0,
        message: '年龄必须是正数'
    },
    email: {
        validator: (value) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value),
        message: '邮箱格式不正确'
    }
});

const user = validator.createProxy({});
user.age = 25;
user.email = 'test@example.com';
```

## 观察者模式实现

### 基础实现

```js
function observable(target) {
    const observers = [];
    
    const proxy = new Proxy(target, {
        set(target, prop, value) {
            const oldValue = target[prop];
            const result = Reflect.set(target, prop, value);
            if (result && oldValue !== value) {
                observers.forEach(observer => {
                    observer(prop, value, oldValue);
                });
            }
            return result;
        }
    });
    
    proxy.observe = (callback) => {
        observers.push(callback);
        return () => {
            const index = observers.indexOf(callback);
            if (index > -1) {
                observers.splice(index, 1);
            }
        };
    };
    
    return proxy;
}

// 使用
const data = observable({ name: 'test' });
const unsubscribe = data.observe((prop, newVal, oldVal) => {
    console.log(`${prop} 从 ${oldVal} 变为 ${newVal}`);
});

data.name = 'new name'; // 输出: name 从 test 变为 new name
unsubscribe();
data.name = 'another'; // 不会触发回调
```

### 深度观察

```js
function deepObservable(target) {
    const observers = [];
    
    // 递归代理所有对象属性
    function makeObservable(obj) {
        if (typeof obj !== 'object' || obj === null) {
            return obj;
        }
        
        for (const key in obj) {
            if (typeof obj[key] === 'object' && obj[key] !== null) {
                obj[key] = makeObservable(obj[key]);
            }
        }
        
        return new Proxy(obj, {
            set(target, prop, value) {
                const oldValue = target[prop];
                if (typeof value === 'object' && value !== null) {
                    value = makeObservable(value);
                }
                const result = Reflect.set(target, prop, value);
                if (result && oldValue !== value) {
                    observers.forEach(observer => {
                        observer(prop, value, oldValue);
                    });
                }
                return result;
            }
        });
    }
    
    const proxy = makeObservable(target);
    proxy.observe = (callback) => {
        observers.push(callback);
    };
    
    return proxy;
}
```

## 属性访问控制

### 私有属性模拟

```js
function createPrivateObject(target, privateKeys) {
    const privateProps = new Set(privateKeys);
    
    return new Proxy(target, {
        get(target, prop) {
            if (privateProps.has(prop)) {
                throw new Error(`属性 ${prop} 是私有的，无法访问`);
            }
            return Reflect.get(target, prop);
        },
        has(target, prop) {
            if (privateProps.has(prop)) {
                return false; // 隐藏私有属性
            }
            return Reflect.has(target, prop);
        },
        ownKeys(target) {
            return Reflect.ownKeys(target).filter(key => !privateProps.has(key));
        }
    });
}

// 使用
const obj = createPrivateObject({ name: 'test', password: 'secret' }, ['password']);
console.log(obj.name);     // "test"
// console.log(obj.password); // 抛出错误
console.log('password' in obj); // false
```

## API 客户端封装

### 动态 API 调用

```js
function createAPIClient(baseURL) {
    return new Proxy({}, {
        get(target, prop) {
            return async (params = {}) => {
                const url = `${baseURL}/${prop}`;
                const response = await fetch(url, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(params)
                });
                return response.json();
            };
        }
    });
}

// 使用
const api = createAPIClient('https://api.example.com');
const users = await api.users({ page: 1 });
const posts = await api.posts({ limit: 10 });
```

### RESTful API 封装

```js
function createRESTClient(baseURL) {
    const methods = ['get', 'post', 'put', 'delete'];
    
    return new Proxy({}, {
        get(target, resource) {
            const client = {};
            
            methods.forEach(method => {
                client[method] = async (id, data) => {
                    let url = `${baseURL}/${resource}`;
                    if (id) url += `/${id}`;
                    
                    const options = {
                        method: method.toUpperCase(),
                        headers: { 'Content-Type': 'application/json' }
                    };
                    
                    if (data && (method === 'post' || method === 'put')) {
                        options.body = JSON.stringify(data);
                    }
                    
                    const response = await fetch(url, options);
                    return response.json();
                };
            });
            
            return client;
        }
    });
}

// 使用
const api = createRESTClient('https://api.example.com');
const users = await api.users.get();
const user = await api.users.get(1);
const newUser = await api.users.post({ name: 'John' });
```

## 缓存代理

### 函数结果缓存

```js
function createCacheProxy(fn) {
    const cache = new Map();
    
    return new Proxy(fn, {
        apply(target, thisArg, args) {
            const key = JSON.stringify(args);
            if (cache.has(key)) {
                console.log('从缓存获取');
                return cache.get(key);
            }
            console.log('计算结果');
            const result = Reflect.apply(target, thisArg, args);
            cache.set(key, result);
            return result;
        }
    });
}

// 使用
function expensiveOperation(n) {
    // 模拟耗时操作
    let sum = 0;
    for (let i = 0; i < n; i++) {
        sum += i;
    }
    return sum;
}

const cachedFn = createCacheProxy(expensiveOperation);
console.log(cachedFn(1000000)); // 计算结果
console.log(cachedFn(1000000)); // 从缓存获取
```

## 属性别名系统

### 多语言属性支持

```js
function createI18nObject(target, translations) {
    return new Proxy(target, {
        get(target, prop) {
            // 先尝试直接访问
            if (prop in target) {
                return Reflect.get(target, prop);
            }
            // 尝试通过翻译访问
            for (const [lang, map] of Object.entries(translations)) {
                if (prop in map) {
                    const originalKey = map[prop];
                    return Reflect.get(target, originalKey);
                }
            }
            return undefined;
        },
        has(target, prop) {
            if (prop in target) return true;
            for (const map of Object.values(translations)) {
                if (prop in map) return true;
            }
            return false;
        }
    });
}

// 使用
const obj = { name: 'test', age: 25 };
const i18nObj = createI18nObject(obj, {
    zh: { 姓名: 'name', 年龄: 'age' },
    en: { name: 'name', age: 'age' }
});

console.log(i18nObj.姓名); // "test"
console.log(i18nObj.name); // "test"
```

## 注意事项

1. **性能考虑**：Proxy 的拦截会有性能开销，在性能敏感的场景需要谨慎使用
2. **调试困难**：复杂的代理可能使调试变得困难，需要添加适当的日志
3. **兼容性**：Proxy 和 Reflect 需要现代浏览器支持
4. **语义清晰**：使用 Proxy 时，应该清楚地文档化拦截的行为
5. **测试覆盖**：对 Proxy 的行为进行充分测试

## 常见错误

### 错误 1：过度使用 Proxy

```js
// 错误：在不需要的地方使用 Proxy
const simpleObj = new Proxy({ name: 'test' }, {
    get(target, prop) {
        return target[prop]; // 没有实际作用
    }
});

// 正确：只在需要拦截时使用
const obj = { name: 'test' };
```

### 错误 2：忽略性能影响

```js
// 错误：在性能敏感的场景使用复杂的代理
function processLargeArray(arr) {
    const proxy = new Proxy(arr, {
        get(target, prop) {
            // 复杂的拦截逻辑
        }
    });
    // 处理大量数据
}

// 正确：在必要时使用，或优化拦截逻辑
```

## 最佳实践

1. **明确目的**：只在需要拦截操作时使用 Proxy
2. **性能测试**：对 Proxy 的性能进行测试，确保可接受
3. **文档说明**：清楚文档化代理的行为和用途
4. **错误处理**：在拦截器中添加适当的错误处理
5. **测试覆盖**：对 Proxy 的行为进行充分测试

## 练习

1. **数据验证框架**：实现一个完整的数据验证框架，支持多种验证规则。

2. **观察者模式**：实现一个深度观察的对象，当嵌套属性改变时也能触发回调。

3. **API 客户端**：使用 Proxy 创建一个动态的 RESTful API 客户端。

4. **缓存代理**：实现一个函数结果缓存代理，支持缓存过期时间。

5. **属性访问控制**：实现一个属性访问控制系统，支持只读、隐藏等权限控制。

完成以上练习后，继续学习下一章：错误与异常处理。

## 总结

Proxy 和 Reflect 在实际开发中有很多应用场景，包括数据验证、观察者模式、API 封装、缓存代理等。通过合理使用这些元编程特性，可以编写更灵活、更强大的代码。在使用时要注意性能开销和调试难度，确保代码的可维护性。

## 相关资源

- [MDN：Proxy](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Proxy)
- [MDN：Reflect](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Reflect)
- [JavaScript 元编程指南](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Meta_programming)
