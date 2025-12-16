# 2.10.4 this 关键字

## 概述

`this` 表示函数运行时的上下文对象。它的指向不取决于定义位置，而取决于“调用方式”。掌握 `this` 对象能避免常见 Bug（丢失上下文、事件回调指向错误），也是理解面向对象与异步回调的重要基础。本节系统讲解 `this` 的绑定规则、各场景示例、常见陷阱与最佳实践。

## this 绑定的四条核心规则

> 决定 `this` 的是“调用点”，而非“定义点”。按照优先级从高到低：
> 1) new 绑定 2) 显式绑定 3) 隐式绑定 4) 默认绑定；箭头函数不适用这四条，会继承外层 `this`（词法绑定）。

## 1. 默认绑定

非严格模式下，独立函数调用 `this` 指向全局对象（浏览器为 `window`，Node 为 `global`）；严格模式下为 `undefined`。

```js
function greet() {
  console.log(this);
}

greet(); // 非严格模式：window / global；严格模式：undefined
```

严格模式示例：
```js
'use strict';
function demo() {
  console.log(this); // undefined
}
demo();
```

## 2. 隐式绑定

当函数作为对象的方法被调用时，`this` 指向该对象。

```js
const user = {
  name: 'Alice',
  greet() {
    console.log(this.name);
  }
};

user.greet(); // Alice
```

#### 隐式丢失

方法“脱离”所属对象后调用，会退化为默认绑定。

```js
const obj = { name: 'Bob', say() { console.log(this.name); } };
const fn = obj.say;
fn(); // 非严格：window/global；严格：undefined
```

解决方案：`bind` 固定、或在调用处保持对象调用。

## 3. 显式绑定：call/apply/bind

显式指定 `this`。

**call**：按参数列表传递；**apply**：参数数组；**bind**：返回绑定了 `this` 的新函数。

```js
function show(lang) {
  console.log(lang, this.name);
}
const obj = { name: 'Carol' };

show.call(obj, 'en');       // en Carol
show.apply(obj, ['en']);    // en Carol
const bound = show.bind(obj, 'en');
bound();                    // en Carol
```

## 4. new 绑定

用 `new` 调用函数会创建新对象，并将 `this` 绑定到该实例。

```js
function Person(name) {
  this.name = name;
}
const p = new Person('Dave');
console.log(p.name); // Dave
```

new 优先级最高，会覆盖显式/隐式绑定：
```js
function User(name) { this.name = name; }
const obj = { name: 'X', User };
const u = new obj.User('Tom'); // this -> 新实例
```

## 5. 箭头函数的词法绑定

箭头函数没有自己的 `this`，会捕获定义时所在词法作用域的 `this`。

### 示例：保持外层 this
```js
const obj = {
  name: 'Eve',
  greet() {
    setTimeout(() => {
      console.log(this.name); // Eve，继承 obj 的 this
    }, 10);
  }
};
obj.greet();
```

### 误用：对象方法声明箭头函数
```js
const obj = {
  name: 'Foo',
  greet: () => console.log(this.name) // this 来自外层（通常是全局/undefined）
};
obj.greet(); // 非预期：undefined
```
对象方法应使用普通函数，箭头函数更适合回调/内层函数。

## 6. this 绑定优先级总结

1. `new` 绑定
2. 显式绑定（call/apply/bind）
3. 隐式绑定（对象调用）
4. 默认绑定（独立调用）
箭头函数：不参与上述规则，直接继承外层 `this`。

## 特殊场景与案例

### DOM 事件处理中的 this
```js
button.addEventListener('click', function() {
  console.log(this === button); // true，指向触发事件的元素
});

button.addEventListener('click', () => {
  console.log(this); // 继承外层（若在模块顶层为 undefined）
});
```
在 class 组件/对象方法中，为避免丢失上下文，常用 `bind` 或箭头函数封装回调。

### class 方法与 this
```js
class Counter {
  count = 0;
  inc() { this.count += 1; }
  incAsync() {
    setTimeout(this.inc, 0); // this 丢失 -> NaN
  }
}
```
解决：`this.inc = this.inc.bind(this)`，或在调用处 `setTimeout(() => this.inc(), 0)`，或定义为箭头函数字段：
```js
class Counter {
  count = 0;
  inc = () => { this.count += 1; }; // 字段箭头函数，绑定外层 this（实例）
}
```

### 回调中的 this 丢失
```js
const obj = {
  name: 'Job',
  run(cb) { cb(); }
};
function say() { console.log(this.name); }
obj.run(say); // this 丢失
obj.run(say.bind(obj)); // Job
```

### 数组方法回调中的 thisArg
大多数数组方法（map/filter/forEach）可传递 `thisArg` 作为回调的 `this`。
```js
const obj = { factor: 2 };
const doubled = [1, 2, 3].map(function(x) { return x * this.factor; }, obj);
console.log(doubled); // [2, 4, 6]
```

### 立即调用的函数表达式 (IIFE)
```js
(function() {
  console.log(this); // 非严格：window/global；严格：undefined
})();
```

### 闭包与 this
闭包保存变量，不保存 `this`。若需要外层 `this`，可使用：
- 箭头函数（推荐）
- `const self = this;`（旧写法）
- `bind`

## this 与严格模式

- 默认绑定：严格模式下 `this` 为 `undefined`，有助于发现错误。
- 其他绑定方式行为一致（new/显式/隐式）。

启用严格模式的好处：防止无意中将属性挂到全局对象。

## 常见错误与排查

- **症状**：`Cannot read properties of undefined` / `this is undefined`  
  **原因**：this 丢失（隐式丢失、回调丢失）。  
  **修正**：在调用处用 `bind`、箭头函数，或确保对象点调用。

- **症状**：事件回调中 this 非预期  
  **原因**：箭头函数继承外层，或回调被传递后上下文丢失。  
  **修正**：用普通函数作为事件回调，或在回调内使用已绑定函数。

- **症状**：类方法作为回调丢失 this  
  **原因**：`setTimeout(this.method)`、`Promise.then(this.method)`。  
  **修正**：`this.method = this.method.bind(this)`，或 `() => this.method()`。

## 最佳实践

1) 对象方法用普通函数；内部回调用箭头函数保持外层 `this`。  
2) 类方法若会被当作回调传递，构造函数里 `bind`，或声明为箭头函数字段。  
3) 事件监听使用普通函数获取目标元素的 `this`；需要闭包时用箭头函数或捕获参数。  
4) 在严格模式/ESM 下编写，避免默认绑定落到全局。  
5) 避免在模块顶层依赖 `this`（ESM 顶层 this 为 `undefined`）。  
6) 需要动态上下文时优先使用 `call`/`apply`/`bind`，避免隐式丢失。  

## 练习

1. 编写一个对象方法，演示隐式绑定与隐式丢失，并用 `bind` 修正。  
2. 将类方法传入 `setTimeout`，分别展示未绑定与使用箭头函数/`bind` 的差异。  
3. 在数组 `map` 中传入 `thisArg`，实现带权重的运算。  
4. 用事件监听分别尝试普通函数与箭头函数，观察 `this` 指向的不同。  
5. 编写一个高阶函数，返回绑定特定上下文的函数，并验证 `call`/`apply` 的效果。  

## 小结

- 决定 `this` 的是调用方式：new > 显式 > 隐式 > 默认；箭头函数继承外层。  
- 严格模式/ESM 下默认绑定为 `undefined`，减少意外挂载到全局。  
- 回调、事件、类方法传递时最易丢失 `this`，使用 `bind` 或箭头函数封装。  
- 充分理解并按场景选用绑定方式，可显著降低上下文相关 Bug。  

继续学习下一节，了解静态方法和属性。
