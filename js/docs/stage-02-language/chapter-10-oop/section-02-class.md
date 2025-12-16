# 2.10.2 ES6 Class 语法

## 概述

ES6 引入了 Class 语法，提供了更清晰的面向对象编程方式。Class 本质上是基于原型链的语法糖，但提供了更接近传统面向对象语言的语法。

Class 语法的主要特点：
- **语法糖**：Class 本质上是构造函数的语法糖
- **更清晰的语法**：比传统的构造函数和原型更易读
- **自动严格模式**：类中的代码自动在严格模式下运行
- **不能提升**：Class 声明不会被提升
- **必须使用 new**：Class 必须使用 `new` 关键字调用

## 类声明

### 基本语法

**语法**：`class ClassName { ... }`

```js
class Person {
    constructor(name) {
        this.name = name;
    }
    
    greet() {
        return `Hello, ${this.name}!`;
    }
}

const person = new Person("John");
console.log(person.greet()); // "Hello, John!"
```

### 类表达式

类也可以使用表达式形式定义：

```js
// 匿名类表达式
const Person = class {
    constructor(name) {
        this.name = name;
    }
};

// 命名类表达式
const Person = class PersonClass {
    constructor(name) {
        this.name = name;
    }
    
    getName() {
        return PersonClass.name; // 可以在类内部使用类名
    }
};
```

### 类不会被提升

与函数声明不同，类声明不会被提升：

```js
// 错误：类不会被提升
// const person = new Person("John"); // ReferenceError: Cannot access 'Person' before initialization

class Person {
    constructor(name) {
        this.name = name;
    }
}

const person = new Person("John"); // 正确
```

## 构造函数

### constructor 方法

`constructor` 是类的特殊方法，用于初始化实例。每个类只能有一个 `constructor` 方法。

**语法**：`constructor([parameters]) { ... }`

**参数**：
- `parameters`（可选）：构造函数的参数

**返回值**：无（隐式返回实例对象）

```js
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
}

const person = new Person("John", 30);
console.log(person.name); // "John"
console.log(person.age);  // 30
```

### 默认构造函数

如果没有定义 `constructor`，JavaScript 会自动提供一个空的构造函数：

```js
class Person {
    // 没有定义 constructor
}

// 等价于
class Person {
    constructor() {
        // 空构造函数
    }
}

const person = new Person();
console.log(person); // Person {}
```

### 构造函数中的 this

在构造函数中，`this` 指向新创建的实例：

```js
class Person {
    constructor(name) {
        this.name = name; // this 指向新创建的实例
    }
}

const person = new Person("John");
console.log(person.name); // "John"
```

## 实例方法

### 方法定义

在类中定义的方法会自动添加到类的 `prototype` 上：

```js
class Person {
    constructor(name) {
        this.name = name;
    }
    
    greet() {
        return `Hello, ${this.name}!`;
    }
    
    getAge() {
        return this.age || "Unknown";
    }
}

const person = new Person("John");
console.log(person.greet()); // "Hello, John!"

// 方法在原型上
console.log(person.hasOwnProperty("greet")); // false
console.log(Person.prototype.hasOwnProperty("greet")); // true
```

### 方法中的 this

在实例方法中，`this` 指向调用该方法的实例：

```js
class Person {
    constructor(name) {
        this.name = name;
    }
    
    greet() {
        return `Hello, ${this.name}!`; // this 指向实例
    }
    
    introduce(other) {
        return `${this.name} meets ${other.name}`;
    }
}

const person1 = new Person("John");
const person2 = new Person("Jane");

console.log(person1.greet());              // "Hello, John!"
console.log(person1.introduce(person2));   // "John meets Jane"
```

### 方法绑定

方法中的 `this` 绑定取决于调用方式：

```js
class Person {
    constructor(name) {
        this.name = name;
    }
    
    greet() {
        return `Hello, ${this.name}!`;
    }
}

const person = new Person("John");

// 直接调用：this 指向实例
console.log(person.greet()); // "Hello, John!"

// 提取方法后调用：this 丢失
const greet = person.greet;
// console.log(greet()); // TypeError: Cannot read property 'name' of undefined

// 使用 bind 绑定 this
const boundGreet = person.greet.bind(person);
console.log(boundGreet()); // "Hello, John!"
```

## Getter 和 Setter

### Getter

Getter 用于获取属性值，使用 `get` 关键字定义：

**语法**：`get propertyName() { ... }`

```js
class Person {
    constructor(firstName, lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }
    
    get fullName() {
        return `${this.firstName} ${this.lastName}`;
    }
}

const person = new Person("John", "Doe");
console.log(person.fullName); // "John Doe"（像属性一样访问，不需要调用）
```

### Setter

Setter 用于设置属性值，使用 `set` 关键字定义：

**语法**：`set propertyName(value) { ... }`

```js
class Person {
    constructor(name) {
        this._name = name; // 使用下划线前缀表示私有（约定）
    }
    
    get name() {
        return this._name;
    }
    
    set name(value) {
        if (typeof value !== "string" || value.length === 0) {
            throw new Error("Name must be a non-empty string");
        }
        this._name = value;
    }
}

const person = new Person("John");
console.log(person.name); // "John"

person.name = "Jane";
console.log(person.name); // "Jane"

// person.name = ""; // Error: Name must be a non-empty string
```

### Getter 和 Setter 的实际应用

```js
class Rectangle {
    constructor(width, height) {
        this._width = width;
        this._height = height;
    }
    
    get width() {
        return this._width;
    }
    
    set width(value) {
        if (value <= 0) {
            throw new Error("Width must be positive");
        }
        this._width = value;
    }
    
    get height() {
        return this._height;
    }
    
    set height(value) {
        if (value <= 0) {
            throw new Error("Height must be positive");
        }
        this._height = value;
    }
    
    get area() {
        return this._width * this._height;
    }
    
    get perimeter() {
        return 2 * (this._width + this._height);
    }
}

const rect = new Rectangle(10, 20);
console.log(rect.area);      // 200
console.log(rect.perimeter); // 60

rect.width = 15;
console.log(rect.area); // 300
```

## 计算属性名

可以使用计算属性名定义方法和属性：

```js
const methodName = "greet";
const propertyName = "fullName";

class Person {
    constructor(name) {
        this.name = name;
    }
    
    [methodName]() {
        return `Hello, ${this.name}!`;
    }
    
    get [propertyName]() {
        return this.name.toUpperCase();
    }
}

const person = new Person("John");
console.log(person.greet());    // "Hello, John!"
console.log(person.fullName);   // "JOHN"
```

## 类字段（Class Fields）

### 公共字段（ES2022）

ES2022 引入了类字段语法，可以在类中直接定义实例属性：

```js
class Person {
    // 公共字段
    name = "Unknown";
    age = 0;
    
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
}

const person = new Person("John", 30);
console.log(person.name); // "John"
console.log(person.age);  // 30
```

### 私有字段（ES2022）

使用 `#` 前缀定义私有字段：

```js
class Person {
    // 私有字段
    #name = "Unknown";
    #age = 0;
    
    constructor(name, age) {
        this.#name = name;
        this.#age = age;
    }
    
    getName() {
        return this.#name; // 只能在类内部访问
    }
    
    getAge() {
        return this.#age;
    }
}

const person = new Person("John", 30);
console.log(person.getName()); // "John"
console.log(person.getAge());  // 30

// 错误：无法从外部访问私有字段
// console.log(person.#name); // SyntaxError: Private field '#name' must be declared in an enclosing class
```

### 静态字段（ES2022）

使用 `static` 关键字定义静态字段：

```js
class Person {
    static count = 0; // 静态字段
    
    constructor(name) {
        this.name = name;
        Person.count++;
    }
}

console.log(Person.count); // 0
new Person("John");
new Person("Jane");
console.log(Person.count); // 2
```

## Class 与构造函数的对比

### 传统构造函数方式

```js
// 传统方式
function Person(name) {
    this.name = name;
}

Person.prototype.greet = function() {
    return `Hello, ${this.name}!`;
};

const person = new Person("John");
```

### Class 方式

```js
// Class 方式
class Person {
    constructor(name) {
        this.name = name;
    }
    
    greet() {
        return `Hello, ${this.name}!`;
    }
}

const person = new Person("John");
```

### 等价性

Class 和构造函数在功能上是等价的：

```js
class Person {
    constructor(name) {
        this.name = name;
    }
    
    greet() {
        return `Hello, ${this.name}!`;
    }
}

// Class 本质上是构造函数的语法糖
console.log(typeof Person);                    // "function"
console.log(Person === Person.prototype.constructor); // true

const person = new Person("John");
console.log(person instanceof Person);        // true
console.log(person.__proto__ === Person.prototype); // true
```

## 完整示例

```js
// 完整的 Class 使用示例
class User {
    // 静态字段
    static userCount = 0;
    
    // 私有字段
    #password = null;
    
    // 公共字段
    role = "user";
    
    constructor(name, email, password) {
        this.name = name;
        this.email = email;
        this.#password = password;
        this.createdAt = new Date();
        User.userCount++;
    }
    
    // Getter
    get password() {
        return "***"; // 不返回真实密码
    }
    
    // Setter
    set password(newPassword) {
        if (newPassword.length < 8) {
            throw new Error("Password must be at least 8 characters");
        }
        this.#password = newPassword;
    }
    
    // 实例方法
    greet() {
        return `Hello, ${this.name}!`;
    }
    
    verifyPassword(password) {
        return this.#password === password;
    }
    
    // 静态方法
    static getCount() {
        return User.userCount;
    }
    
    static createAdmin(name, email, password) {
        const admin = new User(name, email, password);
        admin.role = "admin";
        return admin;
    }
}

// 使用示例
const user1 = new User("John", "john@example.com", "password123");
const user2 = new User("Jane", "jane@example.com", "password456");

console.log(user1.greet());        // "Hello, John!"
console.log(user1.verifyPassword("password123")); // true
console.log(User.getCount());      // 2

const admin = User.createAdmin("Admin", "admin@example.com", "admin123");
console.log(admin.role);           // "admin"
console.log(User.getCount());      // 3
```

## 注意事项

### 1. 必须使用 new 调用

Class 必须使用 `new` 关键字调用，否则会抛出错误：

```js
class Person {
    constructor(name) {
        this.name = name;
    }
}

// 错误：不使用 new
// Person("John"); // TypeError: Class constructor Person cannot be invoked without 'new'

// 正确：使用 new
const person = new Person("John");
```

### 2. 类中的代码自动严格模式

类中的代码自动在严格模式下运行：

```js
class Person {
    constructor(name) {
        // 严格模式：this 为 undefined（如果不用 new）
        this.name = name;
    }
    
    method() {
        // 严格模式：未声明的变量会报错
        // undeclared = "error"; // ReferenceError
    }
}
```

### 3. 类不能提升

类声明不会被提升，必须在声明后使用：

```js
// 错误：类不会被提升
// const person = new Person("John"); // ReferenceError

class Person {
    constructor(name) {
        this.name = name;
    }
}

// 正确：在声明后使用
const person = new Person("John");
```

### 4. 类名不能重复

在同一作用域中，类名不能重复：

```js
class Person {
    constructor(name) {
        this.name = name;
    }
}

// 错误：重复声明
// class Person { } // SyntaxError: Identifier 'Person' has already been declared
```

### 5. 类表达式可以匿名

类表达式可以是匿名的：

```js
const Person = class {
    constructor(name) {
        this.name = name;
    }
};

// 类名只在类内部可用
const Person2 = class PersonClass {
    getName() {
        return PersonClass.name; // "PersonClass"
    }
};

const person = new Person2();
console.log(person.getName()); // "PersonClass"
```

## 常见问题

### 问题 1：如何检查对象是否是类的实例？

```js
class Person {
    constructor(name) {
        this.name = name;
    }
}

const person = new Person("John");

// 使用 instanceof
console.log(person instanceof Person); // true

// 使用 constructor
console.log(person.constructor === Person); // true
```

### 问题 2：如何获取类的名称？

```js
class Person {
    constructor(name) {
        this.name = name;
    }
}

console.log(Person.name); // "Person"

// 在实例方法中获取类名
class Person2 {
    getClassName() {
        return this.constructor.name;
    }
}

const person = new Person2();
console.log(person.getClassName()); // "Person2"
```

### 问题 3：如何在类外部访问私有字段？

私有字段只能在类内部访问，无法从外部访问。如果需要访问，需要提供公共方法：

```js
class Person {
    #name = "Unknown";
    
    getName() {
        return this.#name; // 通过公共方法访问
    }
    
    setName(name) {
        this.#name = name; // 通过公共方法修改
    }
}

const person = new Person();
console.log(person.getName()); // "Unknown"
person.setName("John");
console.log(person.getName()); // "John"
```

## 最佳实践

### 1. 使用 Class 替代构造函数

```js
// 好的做法：使用 Class
class Person {
    constructor(name) {
        this.name = name;
    }
    
    greet() {
        return `Hello, ${this.name}!`;
    }
}

// 避免：使用传统构造函数（除非有特殊需求）
function Person2(name) {
    this.name = name;
}
Person2.prototype.greet = function() {
    return `Hello, ${this.name}!`;
};
```

### 2. 使用私有字段保护数据

```js
// 好的做法：使用私有字段
class BankAccount {
    #balance = 0;
    
    deposit(amount) {
        if (amount > 0) {
            this.#balance += amount;
        }
    }
    
    getBalance() {
        return this.#balance;
    }
}

// 避免：使用公共字段（可能被意外修改）
class BankAccount2 {
    balance = 0; // 可能被外部直接修改
}
```

### 3. 使用 Getter 和 Setter 控制访问

```js
// 好的做法：使用 Getter 和 Setter
class Person {
    constructor(name) {
        this._name = name;
    }
    
    get name() {
        return this._name;
    }
    
    set name(value) {
        if (typeof value === "string" && value.length > 0) {
            this._name = value;
        }
    }
}

// 避免：直接暴露属性
class Person2 {
    constructor(name) {
        this.name = name; // 无法控制访问和修改
    }
}
```

### 4. 使用静态方法组织工具函数

```js
// 好的做法：使用静态方法
class MathUtils {
    static add(a, b) {
        return a + b;
    }
    
    static multiply(a, b) {
        return a * b;
    }
}

console.log(MathUtils.add(5, 3)); // 8

// 避免：使用全局函数
function add(a, b) {
    return a + b;
}
```

## 总结

ES6 Class 语法提供了清晰的面向对象编程方式。主要要点：

- 类声明：使用 `class` 关键字
- 构造函数：`constructor` 方法
- 实例方法：在类中定义的方法
- Getter/Setter：属性访问器
- 类字段：公共字段、私有字段、静态字段
- 必须使用 `new` 调用
- 类中的代码自动严格模式
- 类不会被提升

## 练习

1. **创建类**：使用 class 关键字创建一个类，包含构造函数和实例方法。

2. **Getter 和 Setter**：使用 getter 和 setter 实现属性的访问控制。

3. **私有字段**：使用私有字段（#）实现类的数据封装。

4. **静态方法和字段**：创建静态方法和静态字段，演示类级别的成员。

5. **类字段**：使用类字段语法定义实例属性。

完成以上练习后，继续学习下一节，了解继承和 super。
