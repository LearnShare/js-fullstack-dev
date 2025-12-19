# 2.13.1 原型链机�?

## 概述

JavaScript 使用原型链（Prototype Chain）实现继承。这�?JavaScript 与其他基于类的语言（如 Java、C++）的主要区别。理解原型链是掌�?JavaScript 面向对象编程的关键�?

原型链机制的核心概念�?
- **原型对象（prototype�?*：每个函数都有一�?`prototype` 属性，指向一个对�?
- **实例对象（instance�?*：通过 `new` 关键字创建的对象，有一�?`__proto__` 属性指向构造函数的 `prototype`
- **原型�?*：对象查找属性时，会沿着 `__proto__` 链向上查找，直到找到属性或到达 `null`
- **继承**：通过原型链实现对象之间的继承关系

## 原型对象（prototype�?

### 函数�?prototype 属�?

每个函数都有一�?`prototype` 属性（除了箭头函数和某些内置函数），这个属性指向一个对象，称为原型对象�?

```js
function Person(name) {
    this.name = name;
}

// 每个函数都有一�?prototype 属�?
console.log(typeof Person.prototype); // "object"
console.log(Person.prototype);       // { constructor: ƒ Person(name) }
```

### 原型对象�?constructor 属�?

原型对象默认有一�?`constructor` 属性，指向构造函数本身：

```js
function Person(name) {
    this.name = name;
}

console.log(Person.prototype.constructor === Person); // true
console.log(Person.prototype.constructor);           // ƒ Person(name)
```

### 在原型上添加方法

可以在原型对象上添加方法和属性，这些方法和属性会被所有实例共享：

```js
function Person(name) {
    this.name = name;
}

// 在原型上添加方法
Person.prototype.greet = function() {
    return `Hello, ${this.name}!`;
};

Person.prototype.getAge = function() {
    return this.age || "Unknown";
};

const person1 = new Person("John");
const person2 = new Person("Jane");

// 所有实例都可以访问原型上的方法
console.log(person1.greet()); // "Hello, John!"
console.log(person2.greet()); // "Hello, Jane!"

// 方法在原型上，不在实例上
console.log(person1.hasOwnProperty("greet")); // false
console.log(Person.prototype.hasOwnProperty("greet")); // true
```

## 实例对象�?__proto__

### __proto__ 属�?

通过 `new` 关键字创建的对象，都有一�?`__proto__` 属性（内部属性，不是标准属性），指向构造函数的 `prototype`�?

```js
function Person(name) {
    this.name = name;
}

const person = new Person("John");

// __proto__ 指向构造函数的 prototype
console.log(person.__proto__ === Person.prototype); // true
console.log(person.__proto__);                      // { constructor: ƒ Person(name) }
```

### 访问原型对象

有多种方式访问对象的原型�?

```js
function Person(name) {
    this.name = name;
}

const person = new Person("John");

// 方法 1：使�?__proto__（不推荐，已废弃�?
console.log(person.__proto__ === Person.prototype); // true

// 方法 2：使�?Object.getPrototypeOf()（推荐）
console.log(Object.getPrototypeOf(person) === Person.prototype); // true

// 方法 3：使�?Object.setPrototypeOf() 设置原型
const obj = {};
Object.setPrototypeOf(obj, Person.prototype);
console.log(Object.getPrototypeOf(obj) === Person.prototype); // true
```

## 原型�?

### 属性查找机�?

当访问对象的属性时，JavaScript 会按照以下顺序查找：

1. 首先在对象自身查�?
2. 如果找不到，沿着 `__proto__` 向上查找
3. 继续向上查找，直到找到属性或到达 `null`

```js
function Person(name) {
    this.name = name; // 实例属�?
}

Person.prototype.species = "Homo sapiens"; // 原型属�?

const person = new Person("John");

// 查找 name：在实例上找�?
console.log(person.name); // "John"

// 查找 species：在原型上找�?
console.log(person.species); // "Homo sapiens"

// 查找不存在的属性：沿着原型链查找，最终返�?undefined
console.log(person.nonExistent); // undefined
```

### 原型链的终点

原型链的终点�?`Object.prototype`，它�?`__proto__` �?`null`�?

```js
function Person(name) {
    this.name = name;
}

const person = new Person("John");

// 原型链：person -> Person.prototype -> Object.prototype -> null
console.log(person.__proto__);                    // Person.prototype
console.log(person.__proto__.__proto__);          // Object.prototype
console.log(person.__proto__.__proto__.__proto__); // null

// 可以使用 Object.getPrototypeOf() 遍历原型�?
let proto = person;
while (proto) {
    console.log(proto.constructor.name || "Object");
    proto = Object.getPrototypeOf(proto);
}
// 输出�?
// Person
// Object
```

### 属性遮蔽（Property Shadowing�?

如果实例和原型上都有同名属性，实例属性会遮蔽原型属性：

```js
function Person(name) {
    this.name = name;
}

Person.prototype.name = "Default Name";

const person = new Person("John");

// 实例属性遮蔽原型属�?
console.log(person.name); // "John"（来自实例）

// 删除实例属性后，原型属性可�?
delete person.name;
console.log(person.name); // "Default Name"（来自原型）
```

## 原型链继�?

### 基本继承实现

通过设置子类�?`prototype` 为父类实例，可以实现继承�?

```js
// 父类
function Animal(name) {
    this.name = name;
}

Animal.prototype.eat = function() {
    return `${this.name} is eating`;
};

Animal.prototype.sleep = function() {
    return `${this.name} is sleeping`;
};

// 子类
function Dog(name, breed) {
    // 调用父类构造函�?
    Animal.call(this, name);
    this.breed = breed;
}

// 设置原型链：Dog.prototype -> Animal.prototype -> Object.prototype -> null
Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

// 添加子类方法
Dog.prototype.bark = function() {
    return `${this.name} is barking`;
};

// 重写父类方法
Dog.prototype.eat = function() {
    return `${this.name} is eating dog food`;
};

const dog = new Dog("Buddy", "Golden Retriever");

// 可以访问父类方法
console.log(dog.sleep()); // "Buddy is sleeping"（来�?Animal.prototype�?

// 可以访问子类方法
console.log(dog.bark()); // "Buddy is barking"（来�?Dog.prototype�?

// 重写的方�?
console.log(dog.eat()); // "Buddy is eating dog food"（来�?Dog.prototype，遮蔽了 Animal.prototype.eat�?
```

### Object.create() 的作�?

`Object.create()` 创建一个新对象，并将新对象�?`__proto__` 指向指定的原型对象：

```js
// Object.create(proto) 创建一个新对象，其 __proto__ 指向 proto
const proto = { x: 10 };
const obj = Object.create(proto);

console.log(obj.__proto__ === proto); // true
console.log(obj.x);                   // 10（从原型继承�?

// 等价于（但不推荐）：
const obj2 = {};
obj2.__proto__ = proto; // 不推荐，已废�?
```

### 修复 constructor 属�?

设置 `prototype` 后，需要修�?`constructor` 属性：

```js
function Animal(name) {
    this.name = name;
}

function Dog(name, breed) {
    Animal.call(this, name);
    this.breed = breed;
}

// 设置原型
Dog.prototype = Object.create(Animal.prototype);

// 修复 constructor 属�?
Dog.prototype.constructor = Dog;

console.log(Dog.prototype.constructor === Dog); // true
console.log(new Dog("Buddy", "Golden Retriever").constructor === Dog); // true
```

## 原型链的完整示例

```js
// 完整的原型链继承示例
function Animal(name) {
    this.name = name;
    this.species = "Unknown";
}

Animal.prototype.eat = function() {
    return `${this.name} is eating`;
};

Animal.prototype.sleep = function() {
    return `${this.name} is sleeping`;
};

function Mammal(name) {
    Animal.call(this, name);
    this.species = "Mammal";
    this.warmBlooded = true;
}

Mammal.prototype = Object.create(Animal.prototype);
Mammal.prototype.constructor = Mammal;

Mammal.prototype.giveBirth = function() {
    return `${this.name} gives birth to live young`;
};

function Dog(name, breed) {
    Mammal.call(this, name);
    this.breed = breed;
}

Dog.prototype = Object.create(Mammal.prototype);
Dog.prototype.constructor = Dog;

Dog.prototype.bark = function() {
    return `${this.name} is barking`;
};

Dog.prototype.eat = function() {
    return `${this.name} is eating dog food`;
};

const dog = new Dog("Buddy", "Golden Retriever");

// 原型链：dog -> Dog.prototype -> Mammal.prototype -> Animal.prototype -> Object.prototype -> null

console.log(dog.name);        // "Buddy"（实例属性）
console.log(dog.breed);       // "Golden Retriever"（实例属性）
console.log(dog.species);     // "Mammal"（来�?Mammal�?
console.log(dog.warmBlooded); // true（来�?Mammal�?

console.log(dog.bark());      // "Buddy is barking"（来�?Dog.prototype�?
console.log(dog.giveBirth()); // "Buddy gives birth to live young"（来�?Mammal.prototype�?
console.log(dog.eat());       // "Buddy is eating dog food"（来�?Dog.prototype，遮蔽了 Animal.prototype.eat�?
console.log(dog.sleep());     // "Buddy is sleeping"（来�?Animal.prototype�?

// 检查原型链
console.log(dog instanceof Dog);    // true
console.log(dog instanceof Mammal); // true
console.log(dog instanceof Animal); // true
console.log(dog instanceof Object); // true
```

## instanceof 运算�?

### instanceof 的工作原�?

`instanceof` 运算符检查对象的原型链中是否包含指定构造函数的 `prototype`�?

```js
function Animal(name) {
    this.name = name;
}

function Dog(name) {
    Animal.call(this, name);
}

Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

const dog = new Dog("Buddy");

// instanceof 检查原型链
console.log(dog instanceof Dog);    // true
console.log(dog instanceof Animal); // true
console.log(dog instanceof Object); // true
console.log(dog instanceof Array);  // false
```

### 手动实现 instanceof

```js
function myInstanceof(obj, constructor) {
    let proto = Object.getPrototypeOf(obj);
    const prototype = constructor.prototype;
    
    while (proto !== null) {
        if (proto === prototype) {
            return true;
        }
        proto = Object.getPrototypeOf(proto);
    }
    
    return false;
}

function Animal(name) {
    this.name = name;
}

function Dog(name) {
    Animal.call(this, name);
}

Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

const dog = new Dog("Buddy");

console.log(myInstanceof(dog, Dog));    // true
console.log(myInstanceof(dog, Animal)); // true
console.log(myInstanceof(dog, Object)); // true
```

## 原型链的注意事项

### 1. 修改原型的影�?

修改原型会影响所有实例：

```js
function Person(name) {
    this.name = name;
}

const person1 = new Person("John");
const person2 = new Person("Jane");

// 修改原型
Person.prototype.greet = function() {
    return `Hello, ${this.name}!`;
};

// 所有实例都可以访问新方�?
console.log(person1.greet()); // "Hello, John!"
console.log(person2.greet()); // "Hello, Jane!"
```

### 2. 替换原型的影�?

替换原型不会影响已创建的实例�?

```js
function Person(name) {
    this.name = name;
}

Person.prototype.greet = function() {
    return `Hello, ${this.name}!`;
};

const person = new Person("John");

// 替换原型
Person.prototype = {
    sayHi() {
        return `Hi, ${this.name}!`;
    }
};

// 已创建的实例仍然使用旧原�?
console.log(person.greet()); // "Hello, John!"（仍然可以访问）

// 新创建的实例使用新原�?
const person2 = new Person("Jane");
// console.log(person2.greet()); // TypeError: person2.greet is not a function
console.log(person2.sayHi()); // "Hi, Jane!"
```

### 3. 原型链的性能

原型链查找需要遍历链，性能略低于直接属性访问：

```js
function Person(name) {
    this.name = name; // 实例属性，查找�?
}

Person.prototype.species = "Homo sapiens"; // 原型属性，查找稍慢

const person = new Person("John");

// 实例属性：O(1)
console.log(person.name);

// 原型属性：需要遍历原型链，O(n)（n 是原型链长度�?
console.log(person.species);
```

### 4. 原型链的循环引用

避免创建循环的原型链�?

```js
function A() {}
function B() {}

// 错误：创建循环引�?
A.prototype = new B();
B.prototype = new A();

// 这会导致问题
// const a = new A();
// console.log(a instanceof A); // 可能导致栈溢�?
```

## 常见问题

### 问题 1：如何检查属性是否在对象自身�?

```js
function Person(name) {
    this.name = name;
}

Person.prototype.species = "Homo sapiens";

const person = new Person("John");

// 使用 hasOwnProperty()
console.log(person.hasOwnProperty("name"));   // true（实例属性）
console.log(person.hasOwnProperty("species")); // false（原型属性）

// 使用 Object.hasOwn()（ES2022�?
console.log(Object.hasOwn(person, "name"));   // true
console.log(Object.hasOwn(person, "species")); // false
```

### 问题 2：如何获取对象的所有属性（包括原型）？

```js
function Person(name) {
    this.name = name;
}

Person.prototype.species = "Homo sapiens";

const person = new Person("John");

// 只获取自身属�?
console.log(Object.keys(person)); // ["name"]

// 获取所有可枚举属性（包括原型�?
for (const key in person) {
    console.log(key); // "name", "species"
}

// 获取所有属性（包括不可枚举�?
console.log(Object.getOwnPropertyNames(person)); // ["name"]
```

### 问题 3：如何判断属性是否可枚举�?

```js
function Person(name) {
    this.name = name;
}

Person.prototype.species = "Homo sapiens";

const person = new Person("John");

// 检查自身属性的可枚举�?
console.log(person.propertyIsEnumerable("name")); // true

// 检查原型属性的可枚举�?
console.log(person.propertyIsEnumerable("species")); // true（如果原型属性可枚举�?
```

## 最佳实�?

### 1. 使用 Object.create() 设置原型

```js
// 好的做法：使�?Object.create()
function Animal(name) {
    this.name = name;
}

function Dog(name, breed) {
    Animal.call(this, name);
    this.breed = breed;
}

Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

// 避免：直接赋值（会共享同一个对象）
// Dog.prototype = Animal.prototype; // 错误：修�?Dog.prototype 会影�?Animal.prototype
```

### 2. 修复 constructor 属�?

```js
// 好的做法：设置原型后修复 constructor
Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

// 避免：忘记修�?constructor
// Dog.prototype = Object.create(Animal.prototype);
// console.log(Dog.prototype.constructor); // Animal（错误）
```

### 3. 使用 hasOwnProperty() 检查属�?

```js
// 好的做法：使�?hasOwnProperty() 检查自身属�?
function Person(name) {
    this.name = name;
}

Person.prototype.species = "Homo sapiens";

const person = new Person("John");

for (const key in person) {
    if (person.hasOwnProperty(key)) {
        console.log(key); // 只输�?"name"
    }
}

// 避免：直接遍历（会包括原型属性）
for (const key in person) {
    console.log(key); // 输出 "name", "species"
}
```

### 4. 理解原型链的性能影响

```js
// 好的做法：将常用属性放在实例上
function Person(name) {
    this.name = name; // 实例属性，访问�?
}

// 将方法放在原型上（节省内存）
Person.prototype.greet = function() {
    return `Hello, ${this.name}!`;
};

// 避免：将所有属性放在原型上（查找慢�?
// Person.prototype.name = "Default"; // 所有实例共享，查找需要遍历原型链
```

## 总结

原型链是 JavaScript 的继承机制。主要要点：

- 原型对象：函数的 `prototype` 属性指向原型对�?
- 实例对象：通过 `new` 创建的对象，`__proto__` 指向构造函数的 `prototype`
- 原型链：属性查找沿着 `__proto__` 向上查找
- 继承：通过设置 `prototype` 实现继承
- Object.create()：创建新对象并设置原�?
- instanceof：检查原型链中是否包含指定构造函数的 `prototype`
- 注意原型修改的影响和性能考虑

## 练习

1. **创建原型�?*：创建构造函数和原型，建立简单的原型链关系�?

2. **原型继承**：使�?`Object.create()` 实现原型继承，创建父子类关系�?

3. **修复 constructor**：在设置原型后修�?`constructor` 属性�?

4. **instanceof 检�?*：使�?`instanceof` 运算符检查对象的原型链关系�?

5. **手动实现 instanceof**：手动实�?`instanceof` 的功能，遍历原型链�?

完成以上练习后，继续学习下一节，了解 ES6 Class 语法�?
