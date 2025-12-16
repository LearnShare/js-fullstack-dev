# 2.6.2 箭头函数

## 概述

箭头函数是 ES6 引入的简洁函数语法，具有更短的语法和特殊的 this 绑定。本节介绍箭头函数的语法、特性和使用场景。

## 基本语法

### 完整语法

```js
const functionName = (parameters) => {
    // 函数体
    return value;
};
```

### 单参数

```js
// 单参数可以省略括号
const greet = name => {
    return `Hello, ${name}!`;
};
```

### 无参数

```js
// 无参数必须使用括号
const sayHello = () => {
    return "Hello";
};
```

### 单表达式

```js
// 单表达式可以省略花括号和 return
const add = (a, b) => a + b;

const greet = name => `Hello, ${name}!`;
```

### 返回对象

```js
// 返回对象需要使用括号
const createUser = (name, age) => ({
    name: name,
    age: age
});
```

## 箭头函数与普通函数的对比

### 主要区别

| 特性           | 箭头函数                     | 普通函数                     |
|:---------------|:-----------------------------|:-----------------------------|
| **this 绑定**  | 不绑定 this，继承外层作用域  | 绑定 this，取决于调用方式    |
| **arguments**  | 不绑定 arguments             | 绑定 arguments               |
| **构造函数**   | 不能作为构造函数             | 可以作为构造函数             |
| **prototype**  | 没有 prototype 属性          | 有 prototype 属性            |
| **语法**       | 更简洁                       | 传统语法                     |
| **提升**       | 不提升                       | 函数声明提升                 |
| **yield**      | 不能用作生成器函数           | 可以用作生成器函数           |

### 使用场景对比

**箭头函数适合**：
- 回调函数（如 `map`、`filter`、`forEach`）
- 需要保持外层 `this` 的场景
- 简短的函数表达式

**普通函数适合**：
- 对象方法
- 需要 `this` 动态绑定的场景
- 构造函数
- 需要 `arguments` 的场景
- 生成器函数

## this 绑定

### 普通函数的 this

```js
const obj = {
    name: "John",
    greet: function() {
        console.log(this.name); // "John"
    }
};

obj.greet();
```

### 箭头函数的 this

```js
const obj = {
    name: "John",
    greet: () => {
        console.log(this.name); // undefined（this 指向外层作用域）
    }
};

obj.greet();
```

### 实际应用

```js
// 在回调中使用箭头函数保持 this
class Button {
    constructor() {
        this.text = "Click me";
    }
    
    handleClick() {
        // 箭头函数保持 this
        setTimeout(() => {
            console.log(this.text); // "Click me"
        }, 100);
    }
}
```

## 不能使用箭头函数的场景

### 1. 作为方法

```js
// 不好的做法：箭头函数作为方法
const obj = {
    name: "John",
    greet: () => {
        console.log(this.name); // undefined
    }
};

// 好的做法：普通函数
const obj2 = {
    name: "John",
    greet: function() {
        console.log(this.name); // "John"
    }
};
```

### 2. 构造函数

```js
// 箭头函数不能作为构造函数
// const User = (name) => {
//     this.name = name; // TypeError
// };

// 使用普通函数
function User(name) {
    this.name = name;
}
```

### 3. 需要 arguments 对象

```js
// 箭头函数没有 arguments 对象
const func = () => {
    // console.log(arguments); // ReferenceError
};

// 使用剩余参数
const func2 = (...args) => {
    console.log(args);
};
```

## 使用场景

### 1. 回调函数

```js
// 数组方法
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(n => n * 2);
const evens = numbers.filter(n => n % 2 === 0);
const sum = numbers.reduce((acc, n) => acc + n, 0);
```

### 2. 事件处理

```js
// 在类方法中使用箭头函数
class Component {
    handleClick = () => {
        console.log("Clicked");
    }
}
```

### 3. 函数式编程

```js
// 函数式编程风格
const operations = {
    add: (a, b) => a + b,
    subtract: (a, b) => a - b,
    multiply: (a, b) => a * b
};
```

## 最佳实践

### 1. 在回调中使用箭头函数

```js
// 好的做法：在回调中使用箭头函数
const numbers = [1, 2, 3];
numbers.forEach(n => console.log(n));

// 避免：在方法中使用箭头函数
const obj = {
    name: "John",
    greet: () => console.log(this.name) // this 不正确
};
```

### 2. 保持简洁

```js
// 好的做法：简洁的箭头函数
const add = (a, b) => a + b;

// 避免：复杂的箭头函数（使用普通函数）
const complexFunction = (a, b) => {
    // 大量代码
    // ...
    return result;
};
```

## 注意事项

### 1. 不能作为构造函数

```js
// 箭头函数不能作为构造函数
const Arrow = () => {};
// new Arrow(); // TypeError: Arrow is not a constructor
```

### 2. 没有 arguments

```js
// 箭头函数没有 arguments
const arrow = () => {
    // console.log(arguments); // ReferenceError
};

// 使用剩余参数代替
const arrow2 = (...args) => {
    console.log(args);
};
```

### 3. 不能用作生成器

```js
// 箭头函数不能用作生成器
// const gen = *() => {}; // SyntaxError

// 使用普通函数
function* gen() {
    yield 1;
}
```

## 练习

1. **箭头函数转换**：将以下普通函数转换为箭头函数：
   ```js
   function add(a, b) {
       return a + b;
   }
   
   function greet(name) {
       return `Hello, ${name}!`;
   }
   ```

2. **this 绑定对比**：创建一个对象，分别使用普通函数和箭头函数作为方法，观察 `this` 的差异。

3. **回调函数**：使用箭头函数作为 `map`、`filter`、`reduce` 的回调函数。

4. **事件处理**：在类中使用箭头函数作为事件处理函数，保持 `this` 绑定。

5. **函数式编程**：使用箭头函数编写函数式编程风格的代码，如管道、组合等。

完成以上练习后，继续学习下一节，了解函数参数。

## 总结

箭头函数提供了简洁的函数语法。主要要点：

- 简洁的语法：单参数、单表达式可以简化
- this 绑定：箭头函数不绑定 this，继承外层作用域
- 不能作为构造函数：没有 prototype 属性
- 适合回调函数和函数式编程
- 不适合作为对象方法（需要 this 绑定时）
- 与普通函数的主要区别：this 绑定、arguments、构造函数等

继续学习下一节，了解函数参数。
