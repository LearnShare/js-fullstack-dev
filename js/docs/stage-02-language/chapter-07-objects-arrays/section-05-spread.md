# 2.7.5 展开运算符

## 概述

展开运算符（`...`）是 ES2015 引入的语法特性，用于展开可迭代对象（如数组、字符串）或对象。展开运算符提供了简洁、优雅的方式来操作数组和对象。

展开运算符的主要特点：

- **简洁性**：比传统方法更简洁
- **不可变性**：创建新数组或对象，不修改原数据
- **灵活性**：可以在多个位置使用
- **性能**：现代 JavaScript 引擎已优化

## 语法格式

展开运算符使用三个点（`...`）表示：

```js
...iterable  // 数组、字符串等可迭代对象
...object    // 对象（ES2018+）
```

## 数组展开

### 基本用法

**说明**：展开数组会将数组的所有元素展开为独立的元素。

```js
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const combined = [...arr1, ...arr2];
console.log(combined); // [1, 2, 3, 4, 5, 6]
```

**输出说明**：展开运算符将两个数组合并为一个新数组。

### 复制数组

**说明**：展开运算符可以创建数组的浅拷贝。

```js
const original = [1, 2, 3];
const copy = [...original];
console.log(copy); // [1, 2, 3]

// 修改拷贝不影响原数组
copy.push(4);
console.log(original); // [1, 2, 3]
console.log(copy);     // [1, 2, 3, 4]
```

**输出说明**：展开运算符创建新数组，修改拷贝不影响原数组。

**注意事项**：这是浅拷贝，嵌套数组或对象仍会共享引用。

### 添加元素

**说明**：可以在展开数组的同时添加新元素。

```js
const arr = [1, 2, 3];
const newArr = [0, ...arr, 4];
console.log(newArr); // [0, 1, 2, 3, 4]
```

**输出说明**：可以在数组开头、中间或末尾添加元素。

### 展开字符串

**说明**：字符串是可迭代对象，可以使用展开运算符。

```js
const str = 'hello';
const chars = [...str];
console.log(chars); // ['h', 'e', 'l', 'l', 'o']
```

**输出说明**：展开字符串会将每个字符作为数组元素。

## 对象展开

### 基本用法

**说明**：对象展开（ES2018+）可以将对象的属性展开到新对象中。

```js
const obj1 = { a: 1, b: 2 };
const obj2 = { c: 3, d: 4 };
const combined = { ...obj1, ...obj2 };
console.log(combined); // { a: 1, b: 2, c: 3, d: 4 }
```

**输出说明**：展开运算符将两个对象合并为一个新对象。

### 复制对象

**说明**：展开运算符可以创建对象的浅拷贝。

```js
const original = { name: "John", age: 30 };
const copy = { ...original };
console.log(copy); // { name: "John", age: 30 }

// 修改拷贝不影响原对象
copy.age = 31;
console.log(original.age); // 30
console.log(copy.age);     // 31
```

**输出说明**：展开运算符创建新对象，修改拷贝不影响原对象。

**注意事项**：这是浅拷贝，嵌套对象仍会共享引用。

### 覆盖属性

**说明**：后面的属性会覆盖前面的同名属性。

```js
const user = { name: "John", age: 30 };
const updated = { ...user, age: 31 };
console.log(updated); // { name: "John", age: 31 }
```

**输出说明**：后面的 `age: 31` 覆盖了前面的 `age: 30`。

### 添加新属性

**说明**：可以在展开对象的同时添加新属性。

```js
const user = { name: "John", age: 30 };
const extended = { ...user, city: "NYC", country: "USA" };
console.log(extended);
// { name: "John", age: 30, city: "NYC", country: "USA" }
```

**输出说明**：可以在展开对象的同时添加新属性。

## 函数参数展开

### 传递参数

**说明**：展开运算符可以将数组展开为函数参数。

```js
function sum(a, b, c) {
  return a + b + c;
}

const numbers = [1, 2, 3];
console.log(sum(...numbers)); // 6
```

**输出说明**：`...numbers` 将数组 `[1, 2, 3]` 展开为三个独立参数。

### 与剩余参数结合

**说明**：展开运算符可以与剩余参数结合使用。

```js
function process(first, ...rest) {
  console.log(first, rest);
}

const arr = [1, 2, 3, 4, 5];
process(...arr); // 1 [2, 3, 4, 5]
```

**输出说明**：第一个参数被赋值给 `first`，其余参数被收集到 `rest` 数组中。

### 与 apply() 的对比

**说明**：展开运算符可以替代 `Function.prototype.apply()`。

```js
const numbers = [1, 2, 3];

// 旧方式：使用 apply()
Math.max.apply(null, numbers); // 3

// 新方式：使用展开运算符
Math.max(...numbers); // 3
```

**输出说明**：展开运算符更简洁、可读。

## 深度说明

### 浅拷贝特性

**说明**：展开运算符创建的是浅拷贝，嵌套对象或数组仍会共享引用。

```js
const original = {
  name: "John",
  address: { city: "NYC", country: "USA" }
};

const copy = { ...original };

// 修改嵌套对象会影响原对象
copy.address.city = "LA";
console.log(original.address.city); // "LA"
console.log(copy.address.city);     // "LA"
```

**输出说明**：嵌套对象 `address` 仍共享引用，修改会影响原对象。

**解决方案**：需要深拷贝时使用 `JSON.parse(JSON.stringify())` 或深拷贝库。

### 不可迭代对象的错误

**说明**：展开运算符只能用于可迭代对象，不可迭代对象会抛出错误。

```js
// 数组：可迭代，可以展开
const arr = [1, 2, 3];
console.log(...arr); // 1 2 3

// 普通对象：不可迭代（在函数参数中）
// 错误：Uncaught TypeError: ... is not iterable
// const obj = { a: 1, b: 2 };
// console.log(...obj); // 错误！
```

**注意事项**：对象展开（`{...obj}`）是 ES2018+ 特性，与数组展开不同。

### 属性覆盖优先级

**说明**：后面的属性会覆盖前面的同名属性。

```js
const obj1 = { a: 1, b: 2 };
const obj2 = { b: 3, c: 4 };
const combined = { ...obj1, ...obj2 };
console.log(combined); // { a: 1, b: 3, c: 4 }
```

**输出说明**：`obj2` 的 `b: 3` 覆盖了 `obj1` 的 `b: 2`。

### 性能考虑

**说明**：展开运算符的性能取决于数据大小。

- **小数组/对象**：性能良好
- **大数组/对象**：可能影响性能，考虑使用其他方法

```js
// 小数组：性能良好
const small = [1, 2, 3];
const copy = [...small];

// 大数组：可能影响性能
const large = new Array(1000000).fill(0);
const copy2 = [...large]; // 可能较慢
```

## 对比说明

### 与 Object.assign() 的对比

| 特性              | 展开运算符                    | `Object.assign()`            |
|:------------------|:------------------------------|:-----------------------------|
| **语法**          | `{...obj1, ...obj2}`          | `Object.assign({}, obj1, obj2)` |
| **可读性**        | 更简洁、直观                  | 较冗长                       |
| **性能**          | 略快（现代引擎优化）          | 略慢                         |
| **兼容性**        | ES2018+                       | ES2015+                      |
| **嵌套对象**      | 浅拷贝                        | 浅拷贝                       |

**示例**：

```js
const obj1 = { a: 1 };
const obj2 = { b: 2 };

// 展开运算符
const result1 = { ...obj1, ...obj2 };

// Object.assign()
const result2 = Object.assign({}, obj1, obj2);

console.log(result1); // { a: 1, b: 2 }
console.log(result2); // { a: 1, b: 2 }
```

**建议**：优先使用展开运算符，更简洁、可读。

### 与剩余参数的对比

| 特性              | 展开运算符                    | 剩余参数                     |
|:------------------|:------------------------------|:-----------------------------|
| **位置**          | 函数调用时                    | 函数定义时                   |
| **作用**          | 展开数组为参数                 | 收集参数为数组               |
| **语法**          | `func(...arr)`                | `function(...args)`          |

**示例**：

```js
// 展开运算符：展开数组为参数
const numbers = [1, 2, 3];
Math.max(...numbers); // 3

// 剩余参数：收集参数为数组
function sum(...args) {
  return args.reduce((a, b) => a + b, 0);
}
sum(1, 2, 3); // 6
```

**说明**：展开运算符和剩余参数使用相同的语法（`...`），但作用相反。

## 注意事项

### 1. 浅拷贝限制

展开运算符创建的是浅拷贝，嵌套对象或数组仍会共享引用：

```js
const original = {
  items: [1, 2, 3]
};

const copy = { ...original };
copy.items.push(4);

console.log(original.items); // [1, 2, 3, 4]（原对象也被修改）
```

**解决方案**：需要深拷贝时使用深拷贝方法。

### 2. 不可迭代对象错误

在函数参数中使用展开运算符时，只能展开可迭代对象：

```js
// 正确：数组是可迭代的
const arr = [1, 2, 3];
console.log(...arr); // 1 2 3

// 错误：对象在函数参数中不可迭代
// const obj = { a: 1 };
// console.log(...obj); // TypeError
```

### 3. 属性覆盖顺序

后面的属性会覆盖前面的同名属性：

```js
const obj1 = { a: 1, b: 2 };
const obj2 = { b: 3 };
const result = { ...obj1, ...obj2 }; // { a: 1, b: 3 }
```

### 4. 性能考虑

对于大数组或大对象，展开运算符可能影响性能：

```js
// 小数据：性能良好
const small = [1, 2, 3];
const copy = [...small];

// 大数据：可能较慢
const large = new Array(1000000).fill(0);
const copy2 = [...large]; // 考虑使用其他方法
```

## 常见错误

### 错误 1：在不可迭代对象上使用展开运算符

```js
// 错误：对象在函数参数中不可迭代
const obj = { a: 1, b: 2 };
// console.log(...obj); // TypeError

// 正确：对象展开（ES2018+）
const copy = { ...obj }; // { a: 1, b: 2 }
```

### 错误 2：混淆浅拷贝和深拷贝

```js
// 错误：认为展开运算符是深拷贝
const original = { nested: { value: 1 } };
const copy = { ...original };
copy.nested.value = 2;
console.log(original.nested.value); // 2（原对象也被修改）

// 正确：需要深拷贝时使用深拷贝方法
const deepCopy = JSON.parse(JSON.stringify(original));
```

## 最佳实践

1. **优先使用展开运算符**：比 `Object.assign()` 更简洁
2. **注意浅拷贝**：嵌套对象或数组仍会共享引用
3. **性能考虑**：大数据时考虑使用其他方法
4. **属性覆盖**：注意属性覆盖的顺序和优先级
5. **可读性**：展开运算符通常比传统方法更可读

## 实际应用

### 1. 合并数组

```js
const arr1 = [1, 2];
const arr2 = [3, 4];
const merged = [...arr1, ...arr2]; // [1, 2, 3, 4]
```

### 2. 更新对象

```js
const user = { name: "John", age: 30 };
const updated = { ...user, age: 31, city: "NYC" };
// { name: "John", age: 31, city: "NYC" }
```

### 3. 函数调用

```js
const numbers = [1, 2, 3];
Math.max(...numbers); // 3
```

### 4. 复制数据

```js
// 复制数组
const arr = [1, 2, 3];
const copy = [...arr];

// 复制对象
const obj = { a: 1, b: 2 };
const copy2 = { ...obj };
```

## 练习

1. **数组操作**：
   - 使用展开运算符合并三个数组
   - 使用展开运算符在数组中间插入元素

2. **对象操作**：
   - 使用展开运算符创建对象的浅拷贝
   - 使用展开运算符更新对象的多个属性

3. **函数参数**：
   - 使用展开运算符调用 `Math.max()` 和 `Math.min()`
   - 编写函数，使用展开运算符和剩余参数处理参数

4. **对比实践**：
   - 使用展开运算符和 `Object.assign()` 实现相同的对象合并
   - 比较两种方法的性能和可读性

5. **实际应用**：
   - 实现一个函数，使用展开运算符合并多个配置对象
   - 实现一个函数，使用展开运算符处理数组数据

## 总结

展开运算符提供了简洁、优雅的数据操作方式：

- **数组展开**：展开数组元素，合并、复制数组
- **对象展开**：展开对象属性，合并、复制对象
- **函数参数**：展开参数列表，替代 `apply()`
- **浅拷贝**：创建数组或对象的浅拷贝
- **属性覆盖**：后面的属性覆盖前面的同名属性

掌握展开运算符是编写现代 JavaScript 代码的基础。

继续学习下一章：字符串操作。

---

**最后更新**：2025-12-16
