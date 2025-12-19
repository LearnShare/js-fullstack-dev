# 2.14.2 Proxy 基础

## 概述

本节详细介绍 Proxy 的创建、基本拦截器（handler）的使用，包�?get、set、has、deleteProperty 等常用拦截器�?
## 创建 Proxy

### 基本语法

**语法格式**：`new Proxy(target, handler)`

**参数说明**�?
| 参数�?   | 类型   | 说明                           | 是否必需 | 默认�?|
|:----------|:-------|:-------------------------------|:---------|:-------|
| `target`  | object | 要代理的目标对象                | �?      | -      |
| `handler` | object | 拦截器对象，定义拦截行为        | �?      | -      |

**返回�?*：一个新�?Proxy 对象

### 基本创建

```js
const target = { name: 'JavaScript' };
const handler = {};
const proxy = new Proxy(target, handler);

console.log(proxy.name); // "JavaScript"
```

### �?handler

如果 handler 是空对象，Proxy 的行为与目标对象相同�?
```js
const target = { name: 'test' };
const proxy = new Proxy(target, {});

// 行为与直接访�?target 相同
console.log(proxy.name); // "test"
proxy.age = 25;
console.log(target.age); // 25
```

## get 拦截�?
### 基本语法

**语法格式**：`get(target, property, receiver)`

**参数说明**�?
| 参数�?     | 类型   | 说明                           | 是否必需 | 默认�?|
|:------------|:-------|:-------------------------------|:---------|:-------|
| `target`    | object | 目标对象                        | �?      | -      |
| `property`  | string | 要访问的属性名                  | �?      | -      |
| `receiver`  | object | Proxy 对象本身                  | �?      | -      |

**返回�?*：属性值（可以是任何类型）

### 基本使用

```js
const target = { name: 'JavaScript', age: 25 };
const proxy = new Proxy(target, {
    get(target, prop) {
        console.log(`访问属�? ${prop}`);
        return target[prop];
    }
});

console.log(proxy.name); // "访问属�? name" 然后输出 "JavaScript"
console.log(proxy.age);  // "访问属�? age" 然后输出 25
```

### 返回默认�?
```js
const target = { name: 'test' };
const proxy = new Proxy(target, {
    get(target, prop) {
        if (prop in target) {
            return target[prop];
        }
        return `属�?${prop} 不存在，返回默认值`;
    }
});

console.log(proxy.name); // "test"
console.log(proxy.age);  // "属�?age 不存在，返回默认�?
```

### 使用 Reflect.get

```js
const target = { name: 'test' };
const proxy = new Proxy(target, {
    get(target, prop, receiver) {
        console.log(`访问属�? ${prop}`);
        return Reflect.get(target, prop, receiver);
    }
});
```

## set 拦截�?
### 基本语法

**语法格式**：`set(target, property, value, receiver)`

**参数说明**�?
| 参数�?     | 类型   | 说明                           | 是否必需 | 默认�?|
|:------------|:-------|:-------------------------------|:---------|:-------|
| `target`    | object | 目标对象                        | �?      | -      |
| `property`  | string | 要设置的属性名                  | �?      | -      |
| `value`     | any    | 要设置的�?                     | �?      | -      |
| `receiver`  | object | Proxy 对象本身                  | �?      | -      |

**返回�?*：布尔值，表示设置是否成功

### 基本使用

```js
const target = {};
const proxy = new Proxy(target, {
    set(target, prop, value) {
        console.log(`设置属�? ${prop} = ${value}`);
        target[prop] = value;
        return true; // 表示设置成功
    }
});

proxy.name = 'JavaScript'; // "设置属�? name = JavaScript"
console.log(target.name); // "JavaScript"
```

### 数据验证

```js
const target = {};
const proxy = new Proxy(target, {
    set(target, prop, value) {
        if (prop === 'age') {
            if (typeof value !== 'number' || value < 0) {
                throw new TypeError('年龄必须是正�?);
            }
        }
        target[prop] = value;
        return true;
    }
});

proxy.age = 25; // 成功
// proxy.age = -5; // 抛出错误
```

### 使用 Reflect.set

```js
const target = {};
const proxy = new Proxy(target, {
    set(target, prop, value, receiver) {
        console.log(`设置属�? ${prop} = ${value}`);
        return Reflect.set(target, prop, value, receiver);
    }
});
```

## has 拦截�?
### 基本语法

**语法格式**：`has(target, property)`

**参数说明**�?
| 参数�?     | 类型   | 说明           | 是否必需 | 默认�?|
|:------------|:-------|:---------------|:---------|:-------|
| `target`    | object | 目标对象        | �?      | -      |
| `property`  | string | 要检查的属性名  | �?      | -      |

**返回�?*：布尔值，表示属性是否存�?
### 基本使用

```js
const target = { name: 'test', age: 25 };
const proxy = new Proxy(target, {
    has(target, prop) {
        console.log(`检查属�? ${prop}`);
        return prop in target;
    }
});

console.log('name' in proxy); // "检查属�? name" 然后输出 true
console.log('email' in proxy); // "检查属�? email" 然后输出 false
```

### 隐藏某些属�?
```js
const target = { name: 'test', password: 'secret' };
const proxy = new Proxy(target, {
    has(target, prop) {
        if (prop === 'password') {
            return false; // 隐藏 password 属�?        }
        return prop in target;
    }
});

console.log('name' in proxy);     // true
console.log('password' in proxy); // false（被隐藏�?```

## deleteProperty 拦截�?
### 基本语法

**语法格式**：`deleteProperty(target, property)`

**参数说明**�?
| 参数�?     | 类型   | 说明           | 是否必需 | 默认�?|
|:------------|:-------|:---------------|:---------|:-------|
| `target`    | object | 目标对象        | �?      | -      |
| `property`  | string | 要删除的属性名  | �?      | -      |

**返回�?*：布尔值，表示删除是否成功

### 基本使用

```js
const target = { name: 'test', age: 25 };
const proxy = new Proxy(target, {
    deleteProperty(target, prop) {
        console.log(`删除属�? ${prop}`);
        return delete target[prop];
    }
});

delete proxy.age; // "删除属�? age"
console.log('age' in target); // false
```

### 保护某些属�?
```js
const target = { name: 'test', id: 123 };
const proxy = new Proxy(target, {
    deleteProperty(target, prop) {
        if (prop === 'id') {
            throw new Error('不能删除 id 属�?);
        }
        return delete target[prop];
    }
});

delete proxy.name; // 成功
// delete proxy.id; // 抛出错误
```

## ownKeys 拦截�?
### 基本语法

**语法格式**：`ownKeys(target)`

**参数说明**�?
| 参数�?  | 类型   | 说明    | 是否必需 | 默认�?|
|:---------|:-------|:--------|:---------|:-------|
| `target` | object | 目标对象 | �?      | -      |

**返回�?*：属性名数组

### 基本使用

```js
const target = { name: 'test', age: 25, email: 'test@example.com' };
const proxy = new Proxy(target, {
    ownKeys(target) {
        console.log('获取所有属性名');
        return Reflect.ownKeys(target);
    }
});

console.log(Object.keys(proxy)); // "获取所有属性名" 然后输出 ["name", "age", "email"]
```

### 过滤属�?
```js
const target = { name: 'test', password: 'secret', age: 25 };
const proxy = new Proxy(target, {
    ownKeys(target) {
        return Object.keys(target).filter(key => key !== 'password');
    }
});

console.log(Object.keys(proxy)); // ["name", "age"]（password 被过滤）
```

## defineProperty 拦截�?
### 基本语法

**语法格式**：`defineProperty(target, property, descriptor)`

**参数说明**�?
| 参数�?      | 类型   | 说明           | 是否必需 | 默认�?|
|:-------------|:-------|:---------------|:---------|:-------|
| `target`     | object | 目标对象        | �?      | -      |
| `property`   | string | 要定义的属性名  | �?      | -      |
| `descriptor` | object | 属性描述符      | �?      | -      |

**返回�?*：布尔值，表示定义是否成功

### 基本使用

```js
const target = {};
const proxy = new Proxy(target, {
    defineProperty(target, prop, descriptor) {
        console.log(`定义属�? ${prop}`);
        return Reflect.defineProperty(target, prop, descriptor);
    }
});

Object.defineProperty(proxy, 'name', {
    value: 'test',
    writable: true,
    enumerable: true,
    configurable: true
});
```

## getOwnPropertyDescriptor 拦截�?
### 基本语法

**语法格式**：`getOwnPropertyDescriptor(target, property)`

**参数说明**�?
| 参数�?     | 类型   | 说明           | 是否必需 | 默认�?|
|:------------|:-------|:---------------|:---------|:-------|
| `target`    | object | 目标对象        | �?      | -      |
| `property`  | string | 要获取的属性名  | �?      | -      |

**返回�?*：属性描述符对象�?undefined

### 基本使用

```js
const target = { name: 'test' };
const proxy = new Proxy(target, {
    getOwnPropertyDescriptor(target, prop) {
        console.log(`获取属性描述符: ${prop}`);
        return Reflect.getOwnPropertyDescriptor(target, prop);
    }
});

console.log(Object.getOwnPropertyDescriptor(proxy, 'name'));
```

## 注意事项

1. **必须返回正确�?*：拦截器必须返回符合预期的值，否则可能导致错误
2. **使用 Reflect**：在拦截器中使用 Reflect 方法，保持语义一致�?3. **this 绑定**：注意在拦截器中�?this 绑定问题
4. **性能考虑**：Proxy 的拦截会有性能开销，不应过度使�?5. **不可拦截的操�?*：某些操作无法被拦截（如 `Object.keys()` 在某些情况下�?
## 常见错误

### 错误 1：忘记返�?true

```js
// 错误：set 拦截器没有返�?true
const badProxy = new Proxy({}, {
    set(target, prop, value) {
        target[prop] = value;
        // 忘记返回 true
    }
});

// 正确：返�?true 表示设置成功
const goodProxy = new Proxy({}, {
    set(target, prop, value) {
        target[prop] = value;
        return true;
    }
});
```

### 错误 2：直接操�?target

```js
// 错误：在拦截器中直接操作 target，可能破坏代理语�?const badProxy = new Proxy({}, {
    get(target, prop) {
        return target[prop]; // 应该使用 Reflect.get
    }
});

// 正确：使�?Reflect
const goodProxy = new Proxy({}, {
    get(target, prop, receiver) {
        return Reflect.get(target, prop, receiver);
    }
});
```

### 错误 3：拦截器参数错误

```js
// 错误：拦截器参数不完�?const badProxy = new Proxy({}, {
    get(target, prop) {
        // 缺少 receiver 参数
        return target[prop];
    }
});

// 正确：包含所有参�?const goodProxy = new Proxy({}, {
    get(target, prop, receiver) {
        return Reflect.get(target, prop, receiver);
    }
});
```

## 最佳实�?
1. **使用 Reflect**：在拦截器中使用 Reflect 方法，保持语义一致�?2. **返回正确�?*：确保拦截器返回符合预期的�?3. **错误处理**：在拦截器中添加适当的错误处�?4. **性能考虑**：避免在拦截器中执行耗时操作
5. **文档说明**：清楚文档化代理的行�?
## 练习

1. **基础代理**：创建一�?Proxy，拦截对象的属性访问并记录日志�?
2. **数据验证**：创建一�?Proxy，验证对象的属性值（如年龄必须是正数，邮箱必须是有效格式）�?
3. **属性保�?*：创建一�?Proxy，保护某些属性不被修改或删除�?
4. **属性隐�?*：创建一�?Proxy，隐藏某些属性（如密码），使其在 `in` 操作�?`Object.keys()` 中不可见�?
5. **默认值处�?*：创建一�?Proxy，为不存在的属性提供默认值�?
完成以上练习后，继续学习下一节，了解 Proxy 的高级用法�?
## 总结

Proxy 提供了强大的对象操作拦截能力，通过 get、set、has、deleteProperty 等拦截器，可以自定义对象的行为。在拦截器中使用 Reflect 方法可以保持语义一致性，并简化代码实现�?
## 相关资源

- [MDN：Proxy](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Proxy)
- [MDN：Proxy handler](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy)
