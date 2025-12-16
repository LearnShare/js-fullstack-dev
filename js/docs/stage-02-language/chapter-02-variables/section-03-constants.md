# 2.2.3 常量与引用类型

## 概述

`const` 声明的常量不能重新赋值，但对于引用类型（对象、数组等），常量本身不可变，但对象的内容可以修改。本节介绍常量的特性、引用类型的行为和不可变性的概念。

## const 的基本特性

### 不能重新赋值

```js
// const 声明的常量不能重新赋值
const PI = 3.14159;
// PI = 3.14; // TypeError: Assignment to constant variable

const MAX_SIZE = 100;
// MAX_SIZE = 200; // TypeError
```

### 必须初始化

```js
// const 声明时必须初始化
// const x; // SyntaxError: Missing initializer in const declaration

const y = 10; // 正确
```

### 块级作用域

```js
{
    const x = 10;
    console.log(x); // 10
}
// console.log(x); // ReferenceError: x is not defined
```

## 常量与原始类型

### 原始类型不可变

```js
// 原始类型（字符串、数字、布尔值）是不可变的
const str = "Hello";
// str[0] = "h"; // 无效，字符串不可变

const num = 10;
// num = 20; // TypeError: Assignment to constant variable

const bool = true;
// bool = false; // TypeError
```

## 常量与引用类型

### 对象内容可以修改

```js
// const 声明的对象，对象本身不可变，但内容可以修改
const user = {
    name: "John",
    age: 30
};

// 可以修改对象属性
user.name = "Jane";
user.age = 25;
console.log(user); // { name: "Jane", age: 25 }

// 可以添加新属性
user.email = "jane@example.com";
console.log(user); // { name: "Jane", age: 25, email: "jane@example.com" }

// 但不能重新赋值整个对象
// user = {}; // TypeError: Assignment to constant variable
```

### 数组内容可以修改

```js
// const 声明的数组，数组本身不可变，但内容可以修改
const numbers = [1, 2, 3];

// 可以修改数组元素
numbers[0] = 10;
console.log(numbers); // [10, 2, 3]

// 可以添加元素
numbers.push(4);
console.log(numbers); // [10, 2, 3, 4]

// 可以删除元素
numbers.pop();
console.log(numbers); // [10, 2, 3]

// 但不能重新赋值整个数组
// numbers = []; // TypeError: Assignment to constant variable
```

## 理解引用类型

### 引用 vs 值

```js
// 原始类型：值传递
let x = 10;
let y = x;
y = 20;
console.log(x); // 10（x 不变）

// 引用类型：引用传递
const obj1 = { value: 10 };
const obj2 = obj1;
obj2.value = 20;
console.log(obj1.value); // 20（obj1 也被修改）
```

### const 保护的是引用

```js
// const 保护的是变量对对象的引用，而不是对象本身
const user = { name: "John" };

// 可以修改对象内容
user.name = "Jane"; // 允许

// 不能改变引用
// user = { name: "Bob" }; // TypeError
```

## 创建真正的不可变对象

### Object.freeze()

```js
// 使用 Object.freeze() 冻结对象
const user = Object.freeze({
    name: "John",
    age: 30
});

// 尝试修改属性（在严格模式下会报错）
user.name = "Jane"; // 无效（非严格模式下静默失败）
console.log(user.name); // "John"（未改变）

// 注意：Object.freeze() 是浅冻结
const nested = Object.freeze({
    name: "John",
    address: {
        city: "New York"
    }
});

nested.address.city = "Boston"; // 可以修改嵌套对象
console.log(nested.address.city); // "Boston"
```

### 深冻结

```js
// 深冻结函数
function deepFreeze(obj) {
    Object.freeze(obj);
    Object.keys(obj).forEach(key => {
        if (typeof obj[key] === 'object' && obj[key] !== null) {
            deepFreeze(obj[key]);
        }
    });
    return obj;
}

const user = deepFreeze({
    name: "John",
    address: {
        city: "New York"
    }
});

// user.address.city = "Boston"; // 无效
```

## 最佳实践

### 1. 使用 const 声明对象和数组

```js
// 好的做法：使用 const 声明对象和数组
const user = {
    name: "John",
    age: 30
};

const numbers = [1, 2, 3];

// 只有在需要重新赋值整个对象/数组时才使用 let
let user = { name: "John" };
user = { name: "Jane" }; // 需要重新赋值
```

### 2. 理解 const 的行为

```js
// const 保护的是引用，不是内容
const arr = [1, 2, 3];
arr.push(4); // 允许：修改数组内容
// arr = []; // 不允许：重新赋值引用
```

### 3. 需要真正的不可变性时使用 Object.freeze()

```js
// 需要真正的不可变对象时
const config = Object.freeze({
    apiUrl: "https://api.example.com",
    timeout: 5000
});
```

### 4. 使用函数式编程风格

```js
// 函数式编程：创建新对象而不是修改原对象
const user = { name: "John", age: 30 };

// 不好的做法：修改原对象
// user.age = 31;

// 好的做法：创建新对象
const updatedUser = { ...user, age: 31 };
console.log(user);      // { name: "John", age: 30 }
console.log(updatedUser); // { name: "John", age: 31 }
```

## 常见误解

### 误解 1：const 使对象不可变

```js
// 误解：const 使对象不可变
const obj = { x: 1 };
obj.x = 2; // 实际上可以修改

// 正确理解：const 使引用不可变
const obj = { x: 1 };
// obj = { x: 2 }; // 不能重新赋值引用
```

### 误解 2：const 数组不能修改

```js
// 误解：const 数组不能修改
const arr = [1, 2, 3];
arr.push(4); // 实际上可以修改

// 正确理解：const 数组的引用不可变
const arr = [1, 2, 3];
// arr = []; // 不能重新赋值引用
```

## 练习

1. **const 基本使用**：使用 const 声明原始类型常量，尝试修改观察结果。

2. **const 与对象**：使用 const 声明对象，修改对象属性，理解引用的概念。

3. **const 与数组**：使用 const 声明数组，使用数组方法修改数组，理解引用的概念。

4. **Object.freeze()**：使用 Object.freeze() 冻结对象，尝试修改观察结果。

5. **深冻结**：实现深冻结函数，冻结嵌套对象。

完成以上练习后，继续学习下一节，了解作用域的概念。

## 总结

理解常量与引用类型的关系，有助于正确使用 `const`。主要要点：

- `const` 声明的常量不能重新赋值
- 对于引用类型，`const` 保护的是引用，不是内容
- 对象和数组的内容可以修改
- 需要真正的不可变性时使用 `Object.freeze()`
- 优先使用 `const` 声明对象和数组

继续学习下一节，了解作用域的概念。
