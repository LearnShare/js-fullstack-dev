# 2.13.3 继承�?super

## 概述

类可以通过 `extends` 关键字实现继承。继承允许子类继承父类的属性和方法，并可以添加或重写自己的属性和方法。`super` 关键字用于调用父类的构造函数和方法�?

继承的主要特点：
- **代码复用**：子类可以复用父类的代码
- **方法重写**：子类可以重写父类的方法
- **扩展功能**：子类可以添加新的属性和方法
- **多态�?*：子类对象可以替代父类对象使�?

## 类继�?

### extends 关键�?

使用 `extends` 关键字实现类继承�?

**语法**：`class ChildClass extends ParentClass { ... }`

```js
// 父类
class Animal {
    constructor(name) {
        this.name = name;
        this.species = "Unknown";
    }
    
    eat() {
        return `${this.name} is eating`;
    }
    
    sleep() {
        return `${this.name} is sleeping`;
    }
}

// 子类
class Dog extends Animal {
    constructor(name, breed) {
        super(name); // 必须调用 super
        this.breed = breed;
    }
    
    bark() {
        return `${this.name} is barking`;
    }
}

const dog = new Dog("Buddy", "Golden Retriever");
console.log(dog.name);      // "Buddy"
console.log(dog.breed);     // "Golden Retriever"
console.log(dog.eat());     // "Buddy is eating"（继承自 Animal�?
console.log(dog.bark());    // "Buddy is barking"（Dog 自己的方法）
```

### 继承�?

继承可以形成链式结构�?

```js
class Animal {
    constructor(name) {
        this.name = name;
    }
    
    eat() {
        return `${this.name} is eating`;
    }
}

class Mammal extends Animal {
    constructor(name) {
        super(name);
        this.warmBlooded = true;
    }
    
    giveBirth() {
        return `${this.name} gives birth to live young`;
    }
}

class Dog extends Mammal {
    constructor(name, breed) {
        super(name);
        this.breed = breed;
    }
    
    bark() {
        return `${this.name} is barking`;
    }
}

const dog = new Dog("Buddy", "Golden Retriever");

// 原型链：dog -> Dog.prototype -> Mammal.prototype -> Animal.prototype -> Object.prototype -> null

console.log(dog instanceof Dog);    // true
console.log(dog instanceof Mammal); // true
console.log(dog instanceof Animal); // true
console.log(dog instanceof Object); // true
```

## super 关键�?

### 调用父类构造函�?

在子类的构造函数中，必须在使用 `this` 之前调用 `super()`�?

**语法**：`super([arguments])`

**参数**�?
- `arguments`（可选）：传递给父类构造函数的参数

**返回�?*：父类构造函数的返回值（通常�?`undefined`�?

```js
class Animal {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
}

class Dog extends Animal {
    constructor(name, age, breed) {
        // 必须在使�?this 之前调用 super
        super(name, age); // 调用父类构造函�?
        this.breed = breed; // 现在可以使用 this
    }
}

const dog = new Dog("Buddy", 3, "Golden Retriever");
console.log(dog.name);  // "Buddy"（来�?Animal�?
console.log(dog.age);   // 3（来�?Animal�?
console.log(dog.breed); // "Golden Retriever"（来�?Dog�?
```

### super() 必须�?this 之前调用

```js
class Animal {
    constructor(name) {
        this.name = name;
    }
}

class Dog extends Animal {
    constructor(name, breed) {
        // 错误：在使用 this 之前没有调用 super
        // this.breed = breed; // ReferenceError: Must call super constructor in derived class before accessing 'this'
        
        // 正确：先调用 super
        super(name);
        this.breed = breed;
    }
}
```

### 调用父类方法

使用 `super` 可以调用父类的方法：

**语法**：`super.methodName([arguments])`

```js
class Animal {
    eat() {
        return `${this.name} is eating`;
    }
    
    sleep() {
        return `${this.name} is sleeping`;
    }
}

class Dog extends Animal {
    eat() {
        // 调用父类方法并扩�?
        return super.eat() + " dog food";
    }
    
    bark() {
        return `${this.name} is barking`;
    }
}

const dog = new Dog("Buddy");
dog.name = "Buddy"; // 设置 name

console.log(dog.eat());  // "Buddy is eating dog food"（调用了父类方法并扩展）
console.log(dog.sleep()); // "Buddy is sleeping"（继承自父类�?
console.log(dog.bark());  // "Buddy is barking"（子类自己的方法�?
```

### super 在静态方法中

在静态方法中，`super` 指向父类的静态方法：

```js
class Animal {
    static getSpecies() {
        return "Animal";
    }
    
    static create(name) {
        return new Animal(name);
    }
}

class Dog extends Animal {
    static getSpecies() {
        return super.getSpecies() + " - Dog";
    }
    
    static create(name, breed) {
        const dog = super.create(name);
        dog.breed = breed;
        return dog;
    }
}

console.log(Dog.getSpecies()); // "Animal - Dog"
const dog = Dog.create("Buddy", "Golden Retriever");
console.log(dog); // Animal { name: 'Buddy', breed: 'Golden Retriever' }
```

## 方法重写

### 基本重写

子类可以重写父类的方法：

```js
class Animal {
    makeSound() {
        return "Some sound";
    }
    
    move() {
        return `${this.name} is moving`;
    }
}

class Dog extends Animal {
    // 重写父类方法
    makeSound() {
        return "Woof!";
    }
    
    // 添加新方�?
    fetch() {
        return `${this.name} is fetching`;
    }
}

const dog = new Dog("Buddy");
dog.name = "Buddy";

console.log(dog.makeSound()); // "Woof!"（重写的方法�?
console.log(dog.move());      // "Buddy is moving"（继承的方法�?
console.log(dog.fetch());     // "Buddy is fetching"（新方法�?
```

### 使用 super 扩展父类方法

可以使用 `super` 调用父类方法并扩展：

```js
class Animal {
    eat() {
        return `${this.name} is eating`;
    }
}

class Dog extends Animal {
    eat() {
        // 调用父类方法并添加额外行�?
        const baseResult = super.eat();
        return `${baseResult} and wagging tail`;
    }
}

const dog = new Dog("Buddy");
dog.name = "Buddy";

console.log(dog.eat()); // "Buddy is eating and wagging tail"
```

### 完全重写

也可以完全重写父类方法，不调�?`super`�?

```js
class Animal {
    makeSound() {
        return "Some sound";
    }
}

class Dog extends Animal {
    // 完全重写，不调用 super
    makeSound() {
        return "Woof!";
    }
}

const dog = new Dog("Buddy");
console.log(dog.makeSound()); // "Woof!"
```

## 继承的实际应�?

### 1. 图形类继�?

```js
class Shape {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
    
    move(dx, dy) {
        this.x += dx;
        this.y += dy;
    }
    
    getPosition() {
        return { x: this.x, y: this.y };
    }
}

class Circle extends Shape {
    constructor(x, y, radius) {
        super(x, y);
        this.radius = radius;
    }
    
    getArea() {
        return Math.PI * this.radius ** 2;
    }
    
    getPerimeter() {
        return 2 * Math.PI * this.radius;
    }
}

class Rectangle extends Shape {
    constructor(x, y, width, height) {
        super(x, y);
        this.width = width;
        this.height = height;
    }
    
    getArea() {
        return this.width * this.height;
    }
    
    getPerimeter() {
        return 2 * (this.width + this.height);
    }
}

const circle = new Circle(10, 20, 5);
const rect = new Rectangle(0, 0, 10, 20);

console.log(circle.getArea());        // 78.53981633974483
console.log(rect.getArea());          // 200
console.log(circle.getPosition());    // { x: 10, y: 20 }
circle.move(5, 5);
console.log(circle.getPosition());    // { x: 15, y: 25 }
```

### 2. 用户权限系统

```js
class User {
    constructor(name, email) {
        this.name = name;
        this.email = email;
        this.role = "user";
    }
    
    login() {
        return `${this.name} logged in`;
    }
    
    logout() {
        return `${this.name} logged out`;
    }
    
    canAccess(resource) {
        return false; // 默认无权�?
    }
}

class Admin extends User {
    constructor(name, email) {
        super(name, email);
        this.role = "admin";
    }
    
    canAccess(resource) {
        return true; // 管理员有所有权�?
    }
    
    deleteUser(userId) {
        return `User ${userId} deleted`;
    }
}

class Moderator extends User {
    constructor(name, email) {
        super(name, email);
        this.role = "moderator";
    }
    
    canAccess(resource) {
        return resource === "posts" || resource === "comments";
    }
    
    moderatePost(postId) {
        return `Post ${postId} moderated`;
    }
}

const user = new User("John", "john@example.com");
const admin = new Admin("Admin", "admin@example.com");
const moderator = new Moderator("Mod", "mod@example.com");

console.log(user.canAccess("posts"));      // false
console.log(admin.canAccess("posts"));     // true
console.log(moderator.canAccess("posts")); // true
console.log(moderator.canAccess("users")); // false
```

### 3. 交通工具继�?

```js
class Vehicle {
    constructor(brand, model, year) {
        this.brand = brand;
        this.model = model;
        this.year = year;
        this.speed = 0;
    }
    
    start() {
        return `${this.brand} ${this.model} started`;
    }
    
    stop() {
        this.speed = 0;
        return `${this.brand} ${this.model} stopped`;
    }
    
    accelerate(amount) {
        this.speed += amount;
        return `Speed: ${this.speed} km/h`;
    }
}

class Car extends Vehicle {
    constructor(brand, model, year, doors) {
        super(brand, model, year);
        this.doors = doors;
        this.type = "car";
    }
    
    honk() {
        return "Beep beep!";
    }
}

class Motorcycle extends Vehicle {
    constructor(brand, model, year) {
        super(brand, model, year);
        this.type = "motorcycle";
    }
    
    wheelie() {
        return "Doing a wheelie!";
    }
}

const car = new Car("Toyota", "Camry", 2023, 4);
const bike = new Motorcycle("Honda", "CBR", 2023);

console.log(car.start());      // "Toyota Camry started"
console.log(car.honk());       // "Beep beep!"
console.log(bike.start());     // "Honda CBR started"
console.log(bike.wheelie());   // "Doing a wheelie!"
```

## 完整示例

```js
// 完整的继承示�?
class Animal {
    constructor(name, age) {
        this.name = name;
        this.age = age;
        this.species = "Unknown";
    }
    
    eat() {
        return `${this.name} is eating`;
    }
    
    sleep() {
        return `${this.name} is sleeping`;
    }
    
    makeSound() {
        return `${this.name} makes a sound`;
    }
    
    getInfo() {
        return `${this.name} is a ${this.species}, age ${this.age}`;
    }
}

class Mammal extends Animal {
    constructor(name, age) {
        super(name, age);
        this.species = "Mammal";
        this.warmBlooded = true;
    }
    
    giveBirth() {
        return `${this.name} gives birth to live young`;
    }
    
    makeSound() {
        return super.makeSound() + " (mammal sound)";
    }
}

class Dog extends Mammal {
    constructor(name, age, breed) {
        super(name, age);
        this.breed = breed;
    }
    
    bark() {
        return `${this.name} is barking: Woof! Woof!`;
    }
    
    makeSound() {
        return this.bark();
    }
    
    fetch() {
        return `${this.name} is fetching the ball`;
    }
}

class Cat extends Mammal {
    constructor(name, age, color) {
        super(name, age);
        this.color = color;
    }
    
    meow() {
        return `${this.name} is meowing: Meow!`;
    }
    
    makeSound() {
        return this.meow();
    }
    
    purr() {
        return `${this.name} is purring`;
    }
}

// 使用示例
const dog = new Dog("Buddy", 3, "Golden Retriever");
const cat = new Cat("Whiskers", 2, "Orange");

console.log("=== Dog ===");
console.log(dog.getInfo());     // "Buddy is a Mammal, age 3"
console.log(dog.eat());         // "Buddy is eating"（来�?Animal�?
console.log(dog.sleep());       // "Buddy is sleeping"（来�?Animal�?
console.log(dog.giveBirth());   // "Buddy gives birth to live young"（来�?Mammal�?
console.log(dog.bark());        // "Buddy is barking: Woof! Woof!"（来�?Dog�?
console.log(dog.makeSound());   // "Buddy is barking: Woof! Woof!"（重写的方法�?
console.log(dog.fetch());       // "Buddy is fetching the ball"（Dog 的方法）

console.log("\n=== Cat ===");
console.log(cat.getInfo());     // "Whiskers is a Mammal, age 2"
console.log(cat.eat());         // "Whiskers is eating"（来�?Animal�?
console.log(cat.meow());        // "Whiskers is meowing: Meow!"（来�?Cat�?
console.log(cat.makeSound());   // "Whiskers is meowing: Meow!"（重写的方法�?
console.log(cat.purr());        // "Whiskers is purring"（Cat 的方法）

// 多态性：可以使用父类类型引用子类对象
const animals = [dog, cat];
animals.forEach(animal => {
    console.log(animal.makeSound()); // 每个动物发出不同的声�?
});
```

## 注意事项

### 1. 必须调用 super()

在子类构造函数中，如果使用了 `this`，必须先调用 `super()`�?

```js
class Animal {
    constructor(name) {
        this.name = name;
    }
}

class Dog extends Animal {
    constructor(name, breed) {
        // 错误：在使用 this 之前没有调用 super
        // this.breed = breed; // ReferenceError
        
        // 正确
        super(name);
        this.breed = breed;
    }
}
```

### 2. super 只能在子类中使用

`super` 只能在子类中使用�?

```js
class Animal {
    constructor(name) {
        // 错误：super 不能在非子类中使�?
        // super(); // SyntaxError: 'super' keyword unexpected here
        this.name = name;
    }
}
```

### 3. 不能继承多个�?

JavaScript 不支持多重继承，一个类只能继承一个父类：

```js
class A {}
class B {}
class C {}

// 错误：不能继承多个类
// class D extends A, B, C { } // SyntaxError

// 正确：只能继承一个类
class D extends A {}
```

### 4. 可以继承内置�?

可以继承 JavaScript 的内置类�?

```js
class MyArray extends Array {
    first() {
        return this[0];
    }
    
    last() {
        return this[this.length - 1];
    }
}

const arr = new MyArray(1, 2, 3, 4, 5);
console.log(arr.first()); // 1
console.log(arr.last());  // 5
console.log(arr.length);  // 5（继承自 Array�?
```

### 5. 静态方法的继承

静态方法也会被继承�?

```js
class Animal {
    static getSpecies() {
        return "Animal";
    }
}

class Dog extends Animal {
    static getBreed() {
        return "Dog";
    }
}

console.log(Dog.getSpecies()); // "Animal"（继承的静态方法）
console.log(Dog.getBreed());   // "Dog"（自己的静态方法）
```

## 常见问题

### 问题 1：如何检查类之间的继承关系？

```js
class Animal {}
class Dog extends Animal {}
class Cat extends Animal {}

const dog = new Dog();

// 使用 instanceof
console.log(dog instanceof Dog);    // true
console.log(dog instanceof Animal); // true

// 使用 Object.getPrototypeOf()
console.log(Object.getPrototypeOf(Dog.prototype) === Animal.prototype); // true
```

### 问题 2：如何调用父类的私有方法�?

私有方法无法从子类访问，即使是使�?`super`�?

```js
class Animal {
    #privateMethod() {
        return "private";
    }
    
    publicMethod() {
        return this.#privateMethod();
    }
}

class Dog extends Animal {
    // 无法访问父类的私有方�?
    // callPrivate() {
    //     return super.#privateMethod(); // SyntaxError
    // }
    
    // 可以通过公共方法间接访问
    callPrivate() {
        return super.publicMethod();
    }
}
```

### 问题 3：如何实现多重继承？

JavaScript 不支持多重继承，但可以使�?Mixin 模式模拟�?

```js
// Mixin 模式
const CanFly = {
    fly() {
        return `${this.name} is flying`;
    }
};

const CanSwim = {
    swim() {
        return `${this.name} is swimming`;
    }
};

class Animal {
    constructor(name) {
        this.name = name;
    }
}

class Duck extends Animal {
    constructor(name) {
        super(name);
        Object.assign(this, CanFly, CanSwim);
    }
}

const duck = new Duck("Donald");
console.log(duck.fly());  // "Donald is flying"
console.log(duck.swim()); // "Donald is swimming"
```

## 最佳实�?

### 1. 总是调用 super()

```js
// 好的做法：总是调用 super()
class Dog extends Animal {
    constructor(name, breed) {
        super(name);
        this.breed = breed;
    }
}

// 避免：忘记调�?super（如果父类需要初始化�?
class Dog2 extends Animal {
    constructor(name, breed) {
        // 如果父类构造函数需要参数，必须调用 super
        this.breed = breed; // 错误
    }
}
```

### 2. 使用 super 扩展而不是替�?

```js
// 好的做法：使�?super 扩展父类方法
class Dog extends Animal {
    eat() {
        return super.eat() + " dog food";
    }
}

// 避免：完全替换（除非必要�?
class Dog2 extends Animal {
    eat() {
        return "Eating"; // 丢失了父类的实现
    }
}
```

### 3. 合理使用继承层次

```js
// 好的做法：合理的继承层次
class Animal {}
class Mammal extends Animal {}
class Dog extends Mammal {}

// 避免：过深的继承层次
class A {}
class B extends A {}
class C extends B {}
class D extends C {}
class E extends D {} // 继承层次过深，难以维�?
```

### 4. 使用组合替代继承（当合适时�?

```js
// 好的做法：使用组�?
class Engine {
    start() {
        return "Engine started";
    }
}

class Car {
    constructor() {
        this.engine = new Engine();
    }
    
    start() {
        return this.engine.start();
    }
}

// 避免：不必要的继�?
// class Car extends Engine { } // 汽车不是引擎
```

## 总结

继承提供了代码复用的机制。主要要点：

- `extends`：实现类继承
- `super`：调用父类构造函数和方法
- 方法重写：子类可以重写父类方�?
- 必须在使�?`this` 之前调用 `super()`
- 不支持多重继�?
- 可以使用 Mixin 模式模拟多重继承
- 合理使用继承，避免过深的继承层次

## 练习

1. **类继�?*：使�?`extends` 关键字实现类继承，创建子类�?

2. **super 调用**：在子类构造函数中使用 `super()` 调用父类构造函数�?

3. **方法重写**：在子类中重写父类方法，使用 `super` 调用父类方法�?

4. **多级继承**：创建多级继承关系，演示继承链�?

5. **Mixin 模式**：使�?Mixin 模式实现多重继承的功能�?

完成以上练习后，继续学习下一节，了解 this 关键字�?
