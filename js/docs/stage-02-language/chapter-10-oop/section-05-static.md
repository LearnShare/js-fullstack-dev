# 2.10.5 静态方法与属性

## 概述

静态成员（static）属于类本身，而非实例。常用于：工具函数、工厂方法、计数器、缓存、常量配置。ES2022 引入了公共/私有静态字段与静态初始化块，为类级逻辑提供更强能力。本节覆盖语法、参数/返回值、访问规则、继承、常见陷阱、最佳实践。

## 静态方法

### 基本语法

```js
class MathUtils {
  static add(a, b) { return a + b; }
  static subtract(a, b) { return a - b; }
}

console.log(MathUtils.add(5, 3));      // 8
console.log(MathUtils.subtract(5, 3)); // 2
```

- 访问方式：`ClassName.method()`；实例不可直接访问。
- 调用时 `this` 指向类本身（除非被 `call` 改变）。

### 参数与返回值说明（示例）

- 语法：`static add(a: number, b: number): number`
- 参数：
  - `a` (number) 必填，加数
  - `b` (number) 必填，被加数
- 返回值：`number`，两数之和

## 静态属性（公共）

ES2022 允许在类体内直接声明静态字段。

```js
class User {
  static count = 0;
  static defaultRole = 'user';

  constructor(name) {
    this.name = name;
    User.count++;
  }
}

console.log(User.count); // 0
new User('John');
console.log(User.count); // 1
```

## 私有静态字段与方法

使用 `#` 声明私有静态成员，仅在类内部可见。

```js
class Config {
  static #secret = 'token';
  static #getSecret() { return this.#secret; }

  static expose(mask = true) {
    return mask ? '***' : this.#getSecret();
  }
}

console.log(Config.expose());   // ***
// Config.#secret; // SyntaxError: 私有字段不可访问
```

## 静态块（static initialization block）

用于类级初始化逻辑，可访问私有静态字段。

```js
class Logger {
  static #initialized = false;
  static level;

  static {
    this.level = process.env.LOG_LEVEL || 'info';
    this.#initialized = true;
  }
}
```

## 继承中的静态成员

- 静态成员会被子类继承，可通过 `super` 访问父类静态方法。
- `this` 在静态方法中指向当前类（子类调用时指向子类）。

```js
class Base {
  static type = 'base';
  static getType() { return this.type; }
}

class Sub extends Base {
  static type = 'sub';
}

console.log(Sub.getType()); // 'sub'，this 指向 Sub
console.log(Base.getType()); // 'base'
```

## 常见使用模式

### 1) 工具/纯函数集合
```js
class DateUtils {
  static toISO(date = new Date()) { return date.toISOString(); }
  static addDays(date, days) {
    const d = new Date(date);
    d.setDate(d.getDate() + days);
    return d;
  }
}
```

### 2) 工厂方法
```js
class User {
  constructor(name, role) { this.name = name; this.role = role; }
  static createAdmin(name) { return new User(name, 'admin'); }
}

const admin = User.createAdmin('Alice');
```

### 3) 单例/缓存
```js
class Db {
  static #instance = null;
  static getInstance() {
    if (!this.#instance) this.#instance = new Db();
    return this.#instance;
  }
}
```

### 4) 计数器/统计
```js
class Counter {
  static total = 0;
  constructor() { Counter.total++; }
}
```

### 5) 常量与配置
```js
class HttpStatus {
  static OK = 200;
  static NOT_FOUND = 404;
}
```

## 与实例成员的区别

| 对比项       | 静态成员（static）      | 实例成员（非 static）     |
| :----------- | :---------------------- | :------------------------ |
| 归属         | 类本身                  | 实例对象                  |
| 访问方式     | `ClassName.member`      | `instance.member`         |
| 内存占用     | 共享一份               | 每个实例一份              |
| 适用场景     | 工具、常量、工厂、缓存  | 与具体实例状态相关的行为  |

## this 在静态方法中的指向

在静态方法内，默认 `this` 为类本身：

```js
class Demo {
  static who() { return this.name; } // 类名
}
console.log(Demo.who()); // 'Demo'
```

子类调用时 `this` 指向子类，有助于复用：
```js
class A {
  static hello() { return this.id; }
}
class B extends A {}
B.id = 'B';
console.log(B.hello()); // 'B'
```

## 常见陷阱

- **用实例访问静态成员**：`instance.method` 不可访问静态方法；需用类名。  
- **重新绑定 this**：用 `call/apply` 改变静态方法 this 可能造成混淆，不推荐除非有意为之。  
- **滥用静态存状态**：在前端会共享跨页面逻辑，可能导致数据泄漏或测试污染。  
- **私有静态访问错误**：`Class.#field` 只能在类内部；子类也无法直接访问父类私有静态。  
- **循环依赖**：静态初始化块/字段若依赖其它未加载完成的模块，可能出现 undefined。  

## 最佳实践

1. 将“与实例无关”的工具、工厂、常量放入静态成员，避免占用实例内存。  
2. 需要复用且允许子类覆写时，静态方法内部使用 `this` 而非硬编码类名，方便继承扩展。  
3. 避免在静态成员中存放可变全局状态；如需缓存，提供清理方法或使用弱引用/依赖注入。  
4. 对外暴露常量时使用全大写或语义清晰的命名，避免魔法数字。  
5. 使用私有静态字段保护敏感数据或内部缓存，实现类级封装。  
6. 编写测试时清理静态可变数据，防止测试间污染。  

## 练习

1. 编写一个静态工具类，实现字符串裁剪、去重、大小写转换。  
2. 使用私有静态字段实现单例模式，并提供 `reset` 用于测试清理。  
3. 为一个 `Shape` 基类添加 `fromJSON` 静态工厂，返回不同子类实例。  
4. 编写一个 `RateLimiter` 静态类，维护全局配额计数，并演示多实例共享限制。  
5. 在继承层次中演示静态方法使用 `this` 以支持多态（父类返回 `this.type`，子类覆写）。  

## 小结

- 静态成员属于类本身，适合工具、常量、工厂、共享缓存/统计。  
- ES2022 支持公共/私有静态字段与静态初始化块，便于类级封装。  
- 继承时静态成员会被子类继承，`this` 指向当前类，可实现类级多态。  
- 谨慎存放可变全局状态，注意测试隔离与安全性。  

完成本章学习后，继续学习下一章：错误与异常处理。
