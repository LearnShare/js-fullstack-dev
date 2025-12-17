# 2.11.4 Reflect API

## 概述

Reflect 是一个内置对象，提供了一组操作对象的静态方法。这些方法与 Proxy 的拦截器方法一一对应，提供了统一的对象操作 API。

## Reflect 的作用

### 为什么需要 Reflect

1. **统一 API**：提供统一的对象操作 API
2. **返回值改进**：操作失败时返回 false 而不是抛出异常
3. **函数式风格**：提供函数式编程风格的对象操作
4. **与 Proxy 配合**：与 Proxy 配合使用，简化拦截器的实现

### 与 Object 方法的对比

```js
// Object 方法：失败时抛出异常
try {
    Object.defineProperty(obj, 'prop', { value: 1 });
} catch (e) {
    // 处理错误
}

// Reflect 方法：失败时返回 false
if (Reflect.defineProperty(obj, 'prop', { value: 1 })) {
    // 成功
} else {
    // 失败
}
```

## Reflect.get()

### 基本语法

**语法格式**：`Reflect.get(target, propertyKey[, receiver])`

**参数说明**：

| 参数名        | 类型   | 说明                           | 是否必需 | 默认值 |
|:--------------|:-------|:-------------------------------|:---------|:-------|
| `target`      | object | 目标对象                        | 是       | -      |
| `propertyKey`  | string | 属性名                          | 是       | -      |
| `receiver`    | object | 如果属性是 getter，this 指向此对象 | 否       | target |

**返回值**：属性值

### 基本使用

```js
const obj = { name: 'test', age: 25 };
console.log(Reflect.get(obj, 'name')); // "test"
console.log(Reflect.get(obj, 'age'));  // 25
```

### 与 getter 配合

```js
const obj = {
    _value: 10,
    get value() {
        return this._value;
    }
};

const receiver = { _value: 20 };
console.log(Reflect.get(obj, 'value'));        // 10
console.log(Reflect.get(obj, 'value', receiver)); // 20（this 指向 receiver）
```

## Reflect.set()

### 基本语法

**语法格式**：`Reflect.set(target, propertyKey, value[, receiver])`

**参数说明**：

| 参数名        | 类型   | 说明                           | 是否必需 | 默认值 |
|:--------------|:-------|:-------------------------------|:---------|:-------|
| `target`      | object | 目标对象                        | 是       | -      |
| `propertyKey`  | string | 属性名                          | 是       | -      |
| `value`       | any    | 要设置的值                      | 是       | -      |
| `receiver`    | object | 如果属性是 setter，this 指向此对象 | 否       | target |

**返回值**：布尔值，表示设置是否成功

### 基本使用

```js
const obj = {};
Reflect.set(obj, 'name', 'test');
console.log(obj.name); // "test"
```

### 返回值处理

```js
const obj = {};
const result = Reflect.set(obj, 'name', 'test');
if (result) {
    console.log('设置成功');
} else {
    console.log('设置失败');
}
```

## Reflect.has()

### 基本语法

**语法格式**：`Reflect.has(target, propertyKey)`

**参数说明**：

| 参数名        | 类型   | 说明           | 是否必需 | 默认值 |
|:--------------|:-------|:---------------|:---------|:-------|
| `target`      | object | 目标对象        | 是       | -      |
| `propertyKey`  | string | 属性名          | 是       | -      |

**返回值**：布尔值，表示属性是否存在

### 基本使用

```js
const obj = { name: 'test' };
console.log(Reflect.has(obj, 'name'));  // true
console.log(Reflect.has(obj, 'age'));   // false
```

## Reflect.deleteProperty()

### 基本语法

**语法格式**：`Reflect.deleteProperty(target, propertyKey)`

**参数说明**：

| 参数名        | 类型   | 说明           | 是否必需 | 默认值 |
|:--------------|:-------|:---------------|:---------|:-------|
| `target`      | object | 目标对象        | 是       | -      |
| `propertyKey`  | string | 要删除的属性名  | 是       | -      |

**返回值**：布尔值，表示删除是否成功

### 基本使用

```js
const obj = { name: 'test', age: 25 };
Reflect.deleteProperty(obj, 'age');
console.log('age' in obj); // false
```

## Reflect.ownKeys()

### 基本语法

**语法格式**：`Reflect.ownKeys(target)`

**参数说明**：

| 参数名   | 类型   | 说明    | 是否必需 | 默认值 |
|:---------|:-------|:--------|:---------|:-------|
| `target` | object | 目标对象 | 是       | -      |

**返回值**：属性名数组

### 基本使用

```js
const obj = { name: 'test', age: 25 };
const symbol = Symbol('id');
obj[symbol] = 123;

console.log(Reflect.ownKeys(obj)); // ["name", "age", Symbol(id)]
```

## Reflect.defineProperty()

### 基本语法

**语法格式**：`Reflect.defineProperty(target, propertyKey, attributes)`

**参数说明**：

| 参数名        | 类型   | 说明           | 是否必需 | 默认值 |
|:--------------|:-------|:---------------|:---------|:-------|
| `target`      | object | 目标对象        | 是       | -      |
| `propertyKey`  | string | 属性名          | 是       | -      |
| `attributes`  | object | 属性描述符      | 是       | -      |

**返回值**：布尔值，表示定义是否成功

### 基本使用

```js
const obj = {};
const result = Reflect.defineProperty(obj, 'name', {
    value: 'test',
    writable: true,
    enumerable: true,
    configurable: true
});

if (result) {
    console.log(obj.name); // "test"
}
```

## Reflect.getOwnPropertyDescriptor()

### 基本语法

**语法格式**：`Reflect.getOwnPropertyDescriptor(target, propertyKey)`

**参数说明**：

| 参数名        | 类型   | 说明           | 是否必需 | 默认值 |
|:--------------|:-------|:---------------|:---------|:-------|
| `target`      | object | 目标对象        | 是       | -      |
| `propertyKey`  | string | 属性名          | 是       | -      |

**返回值**：属性描述符对象或 undefined

### 基本使用

```js
const obj = { name: 'test' };
const descriptor = Reflect.getOwnPropertyDescriptor(obj, 'name');
console.log(descriptor);
// { value: 'test', writable: true, enumerable: true, configurable: true }
```

## Reflect.getPrototypeOf()

### 基本语法

**语法格式**：`Reflect.getPrototypeOf(target)`

**参数说明**：

| 参数名   | 类型   | 说明    | 是否必需 | 默认值 |
|:---------|:-------|:--------|:---------|:-------|
| `target` | object | 目标对象 | 是       | -      |

**返回值**：原型对象或 null

### 基本使用

```js
const obj = {};
const proto = Reflect.getPrototypeOf(obj);
console.log(proto === Object.prototype); // true
```

## Reflect.setPrototypeOf()

### 基本语法

**语法格式**：`Reflect.setPrototypeOf(target, prototype)`

**参数说明**：

| 参数名      | 类型   | 说明    | 是否必需 | 默认值 |
|:------------|:-------|:--------|:---------|:-------|
| `target`    | object | 目标对象 | 是       | -      |
| `prototype` | object | 新原型  | 是       | -      |

**返回值**：布尔值，表示设置是否成功

### 基本使用

```js
const obj = {};
const newProto = { method() { return 'test'; } };
const result = Reflect.setPrototypeOf(obj, newProto);
if (result) {
    console.log(obj.method()); // "test"
}
```

## Reflect.isExtensible()

### 基本语法

**语法格式**：`Reflect.isExtensible(target)`

**参数说明**：

| 参数名   | 类型   | 说明    | 是否必需 | 默认值 |
|:---------|:-------|:--------|:---------|:-------|
| `target` | object | 目标对象 | 是       | -      |

**返回值**：布尔值，表示对象是否可扩展

### 基本使用

```js
const obj = {};
console.log(Reflect.isExtensible(obj)); // true

Object.freeze(obj);
console.log(Reflect.isExtensible(obj)); // false
```

## Reflect.preventExtensions()

### 基本语法

**语法格式**：`Reflect.preventExtensions(target)`

**参数说明**：

| 参数名   | 类型   | 说明    | 是否必需 | 默认值 |
|:---------|:-------|:--------|:---------|:-------|
| `target` | object | 目标对象 | 是       | -      |

**返回值**：布尔值，表示操作是否成功

### 基本使用

```js
const obj = { name: 'test' };
Reflect.preventExtensions(obj);
// obj.age = 25; // 在严格模式下会抛出错误
```

## Reflect.apply()

### 基本语法

**语法格式**：`Reflect.apply(target, thisArgument, argumentsList)`

**参数说明**：

| 参数名          | 类型   | 说明           | 是否必需 | 默认值 |
|:----------------|:-------|:---------------|:---------|:-------|
| `target`        | function | 目标函数      | 是       | -      |
| `thisArgument`  | any    | 函数调用时的 this | 是       | -      |
| `argumentsList` | array  | 函数参数数组    | 是       | -      |

**返回值**：函数调用的返回值

### 基本使用

```js
function greet(name, age) {
    return `Hello, ${name}! You are ${age} years old.`;
}

const result = Reflect.apply(greet, null, ['John', 30]);
console.log(result); // "Hello, John! You are 30 years old."
```

### 与 Function.prototype.apply 对比

```js
// 使用 Function.prototype.apply
const result1 = greet.apply(null, ['John', 30]);

// 使用 Reflect.apply（更清晰）
const result2 = Reflect.apply(greet, null, ['John', 30]);
```

## Reflect.construct()

### 基本语法

**语法格式**：`Reflect.construct(target, argumentsList[, newTarget])`

**参数说明**：

| 参数名          | 类型     | 说明           | 是否必需 | 默认值 |
|:----------------|:---------|:---------------|:---------|:-------|
| `target`        | function | 目标构造函数    | 是       | -      |
| `argumentsList` | array    | 构造函数参数    | 是       | -      |
| `newTarget`     | function | 实际被调用的构造函数 | 否       | target |

**返回值**：构造的实例对象

### 基本使用

```js
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
}

const person = Reflect.construct(Person, ['John', 30]);
console.log(person.name); // "John"
console.log(person.age);  // 30
```

## Reflect 与 Proxy 配合使用

### 在 Proxy 中使用 Reflect

```js
const target = { name: 'test' };
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

### 保持语义一致性

```js
// 使用 Reflect 可以保持正确的 this 绑定和原型链
const target = {
    get value() {
        return this._value;
    }
};

const proxy = new Proxy(target, {
    get(target, prop, receiver) {
        // 使用 Reflect.get 可以正确传递 receiver
        return Reflect.get(target, prop, receiver);
    }
});

const obj = Object.create(proxy);
obj._value = 10;
console.log(obj.value); // 10（this 正确指向 obj）
```

## 注意事项

1. **返回值**：Reflect 方法失败时返回 false，而不是抛出异常
2. **this 绑定**：使用 Reflect 方法可以正确传递 this 和 receiver
3. **与 Proxy 配合**：在 Proxy 拦截器中使用 Reflect 方法，保持语义一致性
4. **函数式风格**：Reflect 提供函数式编程风格的对象操作
5. **统一 API**：Reflect 提供统一的对象操作 API

## 常见错误

### 错误 1：忽略返回值

```js
// 错误：忽略 Reflect 方法的返回值
Reflect.set(obj, 'name', 'test');
// 不知道是否设置成功

// 正确：检查返回值
if (Reflect.set(obj, 'name', 'test')) {
    console.log('设置成功');
}
```

### 错误 2：不使用 receiver 参数

```js
// 错误：在 Proxy 中不使用 receiver
const badProxy = new Proxy({}, {
    get(target, prop) {
        return target[prop]; // 应该使用 Reflect.get(target, prop, receiver)
    }
});

// 正确：使用 receiver
const goodProxy = new Proxy({}, {
    get(target, prop, receiver) {
        return Reflect.get(target, prop, receiver);
    }
});
```

## 最佳实践

1. **在 Proxy 中使用 Reflect**：在 Proxy 拦截器中使用 Reflect 方法，保持语义一致性
2. **检查返回值**：检查 Reflect 方法的返回值，处理失败情况
3. **传递 receiver**：在需要时传递 receiver 参数，确保正确的 this 绑定
4. **统一 API**：使用 Reflect 提供统一的对象操作 API
5. **函数式风格**：利用 Reflect 的函数式编程风格

## 练习

1. **基础 Reflect 操作**：使用 Reflect.get、Reflect.set、Reflect.has 等方法操作对象。

2. **Reflect 与 Proxy 配合**：在 Proxy 的拦截器中使用 Reflect 方法，实现属性访问日志。

3. **函数调用**：使用 Reflect.apply 和 Reflect.construct 调用函数和构造函数。

4. **属性描述符**：使用 Reflect.defineProperty 和 Reflect.getOwnPropertyDescriptor 操作属性描述符。

5. **原型操作**：使用 Reflect.getPrototypeOf 和 Reflect.setPrototypeOf 操作对象原型。

完成以上练习后，继续学习下一节，了解元编程实践。

## 总结

Reflect 提供了一组操作对象的静态方法，这些方法与 Proxy 的拦截器方法一一对应。Reflect 方法失败时返回 false 而不是抛出异常，提供了统一的对象操作 API。在 Proxy 拦截器中使用 Reflect 方法可以保持语义一致性和正确的 this 绑定。

## 相关资源

- [MDN：Reflect](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Reflect)
- [MDN：Reflect 方法列表](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Reflect#methods)
