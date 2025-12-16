# 2.3.2 引用类型（Objects）

## 概述

引用类型（Objects）是 JavaScript 中的复合数据类型，包括对象、数组、函数、日期、正则表达式等。引用类型的值是可变的，通过引用传递。

## 对象（Object）

### 对象创建

```js
// 对象字面量
let obj = {
    name: "John",
    age: 30
};

// 使用 new Object()
let obj2 = new Object();
obj2.name = "John";

// 使用 Object.create()
let obj3 = Object.create(null);
obj3.name = "John";
```

### 对象属性

```js
let obj = {
    name: "John",
    age: 30
};

// 访问属性
console.log(obj.name);      // "John"
console.log(obj["age"]);    // 30

// 添加属性
obj.email = "john@example.com";

// 删除属性
delete obj.age;
```

## 数组（Array）

### 数组创建

```js
// 数组字面量
let arr = [1, 2, 3];

// 使用 new Array()
let arr2 = new Array(1, 2, 3);

// 空数组
let arr3 = [];
```

### 数组特性

```js
let arr = [1, 2, 3];

// 长度
console.log(arr.length); // 3

// 索引访问
console.log(arr[0]); // 1

// 修改元素
arr[0] = 10;
console.log(arr); // [10, 2, 3]
```

## 函数（Function）

### 函数是对象

```js
function greet() {
    return "Hello";
}

// 函数是对象
console.log(typeof greet); // "function"
console.log(greet.name);   // "greet"
```

### 函数属性

```js
function greet(name) {
    return `Hello, ${name}!`;
}

greet.customProperty = "custom";
console.log(greet.customProperty); // "custom"
```

## 日期（Date）

### 日期创建

```js
// 当前时间
let now = new Date();

// 指定时间
let date = new Date(2024, 0, 1); // 2024年1月1日
let date2 = new Date("2024-01-01");
```

### 日期方法

```js
let date = new Date();

console.log(date.getFullYear()); // 2024
console.log(date.getMonth());    // 0-11
console.log(date.getDate());     // 1-31
console.log(date.getDay());      // 0-6
```

## 正则表达式（RegExp）

### 正则创建

```js
// 字面量
let regex = /pattern/;

// 构造函数
let regex2 = new RegExp("pattern");
```

### 正则方法

```js
let regex = /hello/;

console.log(regex.test("hello world")); // true
console.log(regex.exec("hello world")); // ["hello"]
```

## 引用类型的特性

### 可变性

```js
// 对象是可变的
let obj = { name: "John" };
obj.name = "Jane";
console.log(obj); // { name: "Jane" }

// 数组是可变的
let arr = [1, 2, 3];
arr.push(4);
console.log(arr); // [1, 2, 3, 4]
```

### 引用传递

```js
// 引用类型按引用传递
let obj1 = { value: 10 };
let obj2 = obj1;
obj2.value = 20;
console.log(obj1.value); // 20（obj1 也被修改）

// 数组也是引用传递
let arr1 = [1, 2, 3];
let arr2 = arr1;
arr2.push(4);
console.log(arr1); // [1, 2, 3, 4]
```

### 引用比较

```js
// 引用类型按引用比较
let obj1 = { value: 10 };
let obj2 = { value: 10 };
console.log(obj1 === obj2); // false（不同的引用）

let obj3 = obj1;
console.log(obj1 === obj3); // true（相同的引用）
```

## 类型检测

```js
// typeof 检测
typeof {};        // "object"
typeof [];        // "object"
typeof null;      // "object"（bug）
typeof function(){}; // "function"

// instanceof 检测
[] instanceof Array;        // true
{} instanceof Object;       // true
new Date() instanceof Date; // true
```

## 练习

1. **对象创建**：创建不同类型的对象（普通对象、数组、函数、日期、正则表达式）。

2. **对象修改**：修改对象的属性，演示引用类型的可变性。

3. **引用比较**：比较对象引用，理解引用类型按引用比较的特性。

4. **对象拷贝**：实现对象的浅拷贝和深拷贝，理解引用传递的影响。

5. **类型检测**：使用 `typeof` 和 `instanceof` 检测不同类型的对象。

完成以上练习后，继续学习下一节，了解类型检测方法。

## 总结

引用类型是 JavaScript 中的复合数据类型，具有可变性和引用传递的特性。主要要点：

- 对象：键值对的集合
- 数组：有序的元素集合
- 函数：可调用的对象
- 日期：日期和时间对象
- 正则表达式：模式匹配对象
- 引用类型是可变的
- 引用类型按引用传递和比较

继续学习下一节，了解类型检测方法。
