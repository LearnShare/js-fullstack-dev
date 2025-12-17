# 2.11.1 Proxy 与 Reflect 概述

## 概述

Proxy 和 Reflect 是 ES6 引入的元编程特性，它们提供了对对象操作进行拦截和自定义的能力。Proxy 可以拦截并自定义对象的操作，而 Reflect 提供了一组操作对象的静态方法，与 Proxy 配合使用。

## 什么是 Proxy

Proxy 用于创建一个对象的代理，可以拦截并重新定义对象的基本操作（如属性查找、赋值、枚举、函数调用等）。

### 基本概念

Proxy 是一个包装器（wrapper），它包装目标对象，并拦截对目标对象的操作：

```js
// 创建一个简单的代理
const target = { name: 'JavaScript' };
const proxy = new Proxy(target, {
    get(target, prop) {
        console.log(`获取属性: ${prop}`);
        return target[prop];
    }
});

console.log(proxy.name); // "获取属性: name" 然后输出 "JavaScript"
```

### Proxy 的作用

1. **拦截操作**：可以拦截对象的属性访问、赋值、删除等操作
2. **自定义行为**：可以自定义这些操作的默认行为
3. **元编程**：提供了强大的元编程能力，可以实现数据绑定、观察者模式等功能

## 什么是 Reflect

Reflect 是一个内置对象，提供了一组操作对象的静态方法，这些方法与 Proxy 的拦截器方法一一对应。

### 基本概念

Reflect 的方法与 Proxy 的 handler 方法同名，且行为一致：

```js
// 使用 Reflect
const obj = { name: 'JavaScript' };
console.log(Reflect.get(obj, 'name')); // "JavaScript"
Reflect.set(obj, 'age', 25);
console.log(obj.age); // 25
```

### Reflect 的作用

1. **统一 API**：提供统一的对象操作 API
2. **返回值改进**：操作失败时返回 false 而不是抛出异常
3. **函数式风格**：提供函数式编程风格的对象操作
4. **与 Proxy 配合**：与 Proxy 配合使用，简化拦截器的实现

## Proxy 和 Reflect 的关系

Proxy 和 Reflect 是配合使用的：

```js
const target = { name: 'JavaScript' };
const proxy = new Proxy(target, {
    get(target, prop, receiver) {
        // 使用 Reflect 调用原始行为
        return Reflect.get(target, prop, receiver);
    },
    set(target, prop, value, receiver) {
        // 使用 Reflect 调用原始行为
        return Reflect.set(target, prop, value, receiver);
    }
});
```

## 应用场景

### 1. 数据验证

```js
// 使用 Proxy 实现数据验证
const validator = {
    set(target, prop, value) {
        if (prop === 'age' && (typeof value !== 'number' || value < 0)) {
            throw new TypeError('年龄必须是正数');
        }
        return Reflect.set(target, prop, value);
    }
};

const person = new Proxy({}, validator);
person.age = 25; // 成功
// person.age = -5; // 抛出错误
```

### 2. 属性访问日志

```js
// 记录属性访问
const logger = {
    get(target, prop) {
        console.log(`访问属性: ${prop}`);
        return Reflect.get(target, prop);
    }
};

const obj = new Proxy({ name: 'test' }, logger);
obj.name; // 输出: "访问属性: name"
```

### 3. 默认值处理

```js
// 为不存在的属性提供默认值
const withDefaults = (target, defaults) => {
    return new Proxy(target, {
        get(target, prop) {
            return prop in target ? Reflect.get(target, prop) : defaults[prop];
        }
    });
};

const obj = withDefaults({ name: 'test' }, { name: 'default', age: 0 });
console.log(obj.name); // "test"
console.log(obj.age);  // 0（默认值）
```

### 4. 观察者模式

```js
// 实现观察者模式
function observable(target) {
    const observers = [];
    
    return new Proxy(target, {
        set(target, prop, value) {
            const oldValue = target[prop];
            const result = Reflect.set(target, prop, value);
            if (result && oldValue !== value) {
                observers.forEach(fn => fn(prop, value, oldValue));
            }
            return result;
        }
    });
}

const obj = observable({ name: 'test' });
obj.observe = (fn) => observers.push(fn);
```

## 注意事项

1. **兼容性**：Proxy 和 Reflect 是 ES6 特性，需要现代浏览器支持
2. **性能**：Proxy 的拦截会有一定的性能开销，不应过度使用
3. **透明性**：Proxy 对目标对象是透明的，某些操作可能无法被拦截
4. **this 绑定**：在 Proxy 中需要注意 this 的绑定问题

## 常见错误

### 错误 1：直接操作目标对象

```js
const target = { name: 'test' };
const proxy = new Proxy(target, {
    get(target, prop) {
        return target[prop].toUpperCase();
    }
});

// 错误：直接操作目标对象，绕过了代理
console.log(target.name); // "test"（没有被拦截）

// 正确：使用代理
console.log(proxy.name); // "TEST"
```

### 错误 2：忘记使用 Reflect

```js
// 错误：直接操作 target，可能破坏代理的语义
const badProxy = new Proxy({}, {
    get(target, prop) {
        return target[prop]; // 应该使用 Reflect.get
    }
});

// 正确：使用 Reflect
const goodProxy = new Proxy({}, {
    get(target, prop, receiver) {
        return Reflect.get(target, prop, receiver);
    }
});
```

## 最佳实践

1. **使用 Reflect**：在 Proxy 的拦截器中使用 Reflect 方法，保持语义一致性
2. **性能考虑**：只在必要时使用 Proxy，避免过度拦截
3. **清晰文档**：使用 Proxy 时，应该清楚地文档化拦截的行为
4. **测试覆盖**：对 Proxy 的行为进行充分测试

## 练习

1. **基础代理**：创建一个 Proxy，拦截对象的属性访问并记录日志。

2. **数据验证**：创建一个 Proxy，验证对象的属性值（如年龄必须是正数）。

3. **默认值**：创建一个 Proxy，为不存在的属性提供默认值。

4. **观察者模式**：使用 Proxy 实现一个简单的观察者模式，当对象属性改变时通知观察者。

5. **属性保护**：创建一个 Proxy，保护某些属性不被修改或删除。

完成以上练习后，继续学习下一节，了解 Proxy 的详细用法。

## 总结

Proxy 和 Reflect 是 ES6 引入的元编程特性，提供了强大的对象操作拦截和自定义能力。Proxy 可以拦截对象的操作，而 Reflect 提供了一组操作对象的静态方法。两者配合使用，可以实现数据验证、观察者模式、属性访问日志等功能。

## 相关资源

- [MDN：Proxy](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Proxy)
- [MDN：Reflect](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Reflect)
