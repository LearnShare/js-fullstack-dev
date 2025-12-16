# 2.7.1 对象创建与操作

## 概述

对象是 JavaScript 中的核心数据结构，用于存储键值对。本节介绍对象的创建、属性访问和方法定义。

## 对象字面量

### 基本语法

```js
const obj = {
    key1: value1,
    key2: value2
};
```

### 示例

```js
const user = {
    name: "John",
    age: 30,
    email: "john@example.com"
};
```

### 简写语法

```js
// 属性简写
const name = "John";
const age = 30;

const user = {
    name,  // 等价于 name: name
    age    // 等价于 age: age
};
```

### 方法简写

```js
const user = {
    name: "John",
    greet() {  // 等价于 greet: function() { }
        return `Hello, ${this.name}!`;
    }
};
```

## 属性访问

### 点号访问

```js
const user = {
    name: "John",
    age: 30
};

console.log(user.name); // "John"
console.log(user.age);  // 30
```

### 方括号访问

```js
const user = {
    name: "John",
    age: 30
};

console.log(user["name"]); // "John"
console.log(user["age"]);  // 30

// 动态属性名
const key = "name";
console.log(user[key]); // "John"
```

### 属性添加和修改

```js
const user = {
    name: "John"
};

// 添加属性
user.age = 30;
user.email = "john@example.com";

// 修改属性
user.name = "Jane";

console.log(user); // { name: "Jane", age: 30, email: "john@example.com" }
```

### 属性删除

```js
const user = {
    name: "John",
    age: 30
};

delete user.age;
console.log(user); // { name: "John" }
```

## 方法定义

### 基本方法

```js
const calculator = {
    add(a, b) {
        return a + b;
    },
    subtract(a, b) {
        return a - b;
    }
};

console.log(calculator.add(5, 3));      // 8
console.log(calculator.subtract(5, 3));  // 2
```

### this 关键字

```js
const user = {
    name: "John",
    greet() {
        return `Hello, ${this.name}!`;
    }
};

console.log(user.greet()); // "Hello, John!"
```

## 对象方法

### Object.keys() 方法

**语法格式**：`Object.keys(obj)`

**参数说明**：

| 参数名   | 类型   | 说明                           | 是否必需 | 默认值 |
|:---------|:-------|:-------------------------------|:---------|:-------|
| `obj`    | Object | 要获取键的对象                 | 是       | -      |

**返回值**：数组，返回对象自身可枚举属性的键名数组

**示例**：

```js
const user = {
    name: "John",
    age: 30,
    email: "john@example.com"
};

const keys = Object.keys(user);
console.log(keys); // ["name", "age", "email"]
```

### Object.values() 方法

**语法格式**：`Object.values(obj)`

**参数说明**：

| 参数名   | 类型   | 说明                           | 是否必需 | 默认值 |
|:---------|:-------|:-------------------------------|:---------|:-------|
| `obj`    | Object | 要获取值的对象                 | 是       | -      |

**返回值**：数组，返回对象自身可枚举属性的值数组

**示例**：

```js
const user = {
    name: "John",
    age: 30,
    email: "john@example.com"
};

const values = Object.values(user);
console.log(values); // ["John", 30, "john@example.com"]
```

### Object.entries() 方法

**语法格式**：`Object.entries(obj)`

**参数说明**：

| 参数名   | 类型   | 说明                           | 是否必需 | 默认值 |
|:---------|:-------|:-------------------------------|:---------|:-------|
| `obj`    | Object | 要获取键值对的对象             | 是       | -      |

**返回值**：数组，返回对象自身可枚举属性的 `[key, value]` 键值对数组

**示例**：

```js
const user = {
    name: "John",
    age: 30,
    email: "john@example.com"
};

const entries = Object.entries(user);
console.log(entries);
// [["name", "John"], ["age", 30], ["email", "john@example.com"]]
```

### Object.assign() 方法

**语法格式**：`Object.assign(target, ...sources)`

**参数说明**：

| 参数名     | 类型   | 说明                           | 是否必需 | 默认值 |
|:-----------|:-------|:-------------------------------|:---------|:-------|
| `target`   | Object | 目标对象，属性将被复制到此对象 | 是       | -      |
| `...sources` | Object | 源对象，属性将被复制到目标对象 | 否       | -      |

**返回值**：对象，返回目标对象（被修改后的 `target`）

**说明**：
- 将源对象的可枚举属性复制到目标对象
- 如果多个源对象有相同属性，后面的会覆盖前面的
- 只复制对象自身的可枚举属性，不复制继承属性

**示例**：

```js
const target = { a: 1 };
const source1 = { b: 2 };
const source2 = { c: 3, a: 4 };

Object.assign(target, source1, source2);
console.log(target); // { a: 4, b: 2, c: 3 }
```

### Object.freeze() 方法

**语法格式**：`Object.freeze(obj)`

**参数说明**：

| 参数名   | 类型   | 说明                           | 是否必需 | 默认值 |
|:---------|:-------|:-------------------------------|:---------|:-------|
| `obj`    | Object | 要冻结的对象                   | 是       | -      |

**返回值**：对象，返回被冻结的对象

**说明**：冻结对象，使其不能添加、删除或修改属性

**示例**：

```js
const obj = { name: "John" };
Object.freeze(obj);
obj.age = 30; // 无效，严格模式下会报错
console.log(obj); // { name: "John" }
```

### Object.seal() 方法

**语法格式**：`Object.seal(obj)`

**参数说明**：

| 参数名   | 类型   | 说明                           | 是否必需 | 默认值 |
|:---------|:-------|:-------------------------------|:---------|:-------|
| `obj`    | Object | 要密封的对象                   | 是       | -      |

**返回值**：对象，返回被密封的对象

**说明**：密封对象，使其不能添加或删除属性，但可以修改现有属性

**示例**：

```js
const obj = { name: "John" };
Object.seal(obj);
obj.name = "Jane"; // 可以修改
obj.age = 30;     // 无效，严格模式下会报错
delete obj.name;   // 无效，严格模式下会报错
console.log(obj); // { name: "Jane" }
```

### Object.create() 方法

**语法格式**：`Object.create(proto[, propertiesObject])`

**参数说明**：

| 参数名            | 类型   | 说明                           | 是否必需 | 默认值 |
|:------------------|:-------|:-------------------------------|:---------|:-------|
| `proto`           | Object\|null | 新对象的原型对象             | 是       | -      |
| `propertiesObject` | Object | 属性描述符对象（可选）       | 否       | -      |

**返回值**：对象，返回新创建的对象

**说明**：使用指定的原型对象创建新对象

**示例**：

```js
const proto = { greet() { return "Hello"; } };
const obj = Object.create(proto);
console.log(obj.greet()); // "Hello"
```

## 注意事项

### 1. 对象引用

对象是引用类型，赋值时传递的是引用：

```js
const obj1 = { name: "John" };
const obj2 = obj1;
obj2.name = "Jane";
console.log(obj1.name); // "Jane"（obj1 也被修改了）
```

### 2. 对象冻结

使用 `Object.freeze()` 冻结对象后，不能修改属性：

```js
const obj = Object.freeze({ name: "John" });
obj.name = "Jane"; // 无效
obj.age = 30;      // 无效
```

### 3. 对象密封

使用 `Object.seal()` 密封对象后，不能添加或删除属性，但可以修改现有属性：

```js
const obj = Object.seal({ name: "John" });
obj.name = "Jane"; // 可以修改
obj.age = 30;      // 无效
```

### 4. 属性枚举

`Object.keys()`、`Object.values()`、`Object.entries()` 只返回对象自身的可枚举属性：

```js
const obj = Object.create({ inherited: "value" });
obj.own = "value";
console.log(Object.keys(obj)); // ["own"]（不包含继承属性）
```

## 常见问题

### 问题 1：如何深拷贝对象？

```js
// 方法 1：使用 JSON（有限制）
const obj1 = { name: "John", age: 30 };
const obj2 = JSON.parse(JSON.stringify(obj1));

// 方法 2：使用展开运算符（浅拷贝）
const obj3 = { ...obj1 };

// 方法 3：使用 Object.assign()（浅拷贝）
const obj4 = Object.assign({}, obj1);
```

### 问题 2：如何检查对象是否为空？

```js
// 方法 1：使用 Object.keys()
function isEmpty(obj) {
    return Object.keys(obj).length === 0;
}

// 方法 2：使用 for...in
function isEmpty2(obj) {
    for (let key in obj) {
        return false;
    }
    return true;
}
```

### 问题 3：如何合并多个对象？

```js
// 使用 Object.assign()
const obj1 = { a: 1 };
const obj2 = { b: 2 };
const obj3 = { c: 3 };
const merged = Object.assign({}, obj1, obj2, obj3);

// 使用展开运算符
const merged2 = { ...obj1, ...obj2, ...obj3 };
```

## 最佳实践

### 1. 使用对象字面量

```js
// 好的做法：使用对象字面量
const user = { name: "John", age: 30 };

// 避免：使用 Object 构造函数
const user2 = new Object();
user2.name = "John";
```

### 2. 使用 Object.keys() 遍历对象

```js
// 好的做法：使用 Object.keys()
for (const key of Object.keys(obj)) {
    console.log(key, obj[key]);
}

// 或使用 Object.entries()
for (const [key, value] of Object.entries(obj)) {
    console.log(key, value);
}
```

### 3. 使用 Object.freeze() 保护对象

```js
// 好的做法：冻结配置对象
const config = Object.freeze({
    apiUrl: "https://api.example.com",
    timeout: 5000
});
```

## 练习

1. **创建用户对象**：创建一个包含 `name`、`age`、`email` 属性的用户对象，并添加一个 `greet()` 方法。

2. **对象属性操作**：编写函数实现对象的属性添加、修改和删除操作。

3. **对象合并**：编写函数合并多个对象，后面的对象属性覆盖前面的。

4. **对象遍历**：使用 `Object.keys()`、`Object.values()`、`Object.entries()` 遍历对象并打印所有属性。

5. **对象冻结**：创建一个配置对象，使用 `Object.freeze()` 冻结它，然后尝试修改属性，观察结果。

6. **对象拷贝**：实现一个函数，使用 `Object.assign()` 或展开运算符创建对象的浅拷贝。

完成以上练习后，继续学习下一节，了解数组的基础操作。

## 总结

对象是 JavaScript 中的核心数据结构。主要要点：

- 对象字面量：使用 {} 创建对象
- 属性访问：点号和方括号
- 方法定义：在对象中定义函数
- this 关键字：指向对象本身
- 对象方法：keys、values、entries、assign、freeze、seal、create

继续学习下一节，了解数组的基础操作。
