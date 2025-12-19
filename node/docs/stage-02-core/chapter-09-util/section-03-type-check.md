# 2.9.3 类型检查与调试工具

## 1. 概述

util 模块提供了类型检查和调试工具函数，用于在运行时进行类型检查和格式化输出。虽然 TypeScript 提供了编译时类型检查，但运行时类型检查在某些场景下仍然有用，特别是在处理动态数据、API 响应等场景中。

## 2. 特性说明

- **类型检查**：提供多种类型检查函数。
- **调试输出**：提供格式化的调试输出工具。
- **对象检查**：深度检查对象结构。
- **格式化输出**：格式化字符串和对象输出。
- **自定义检查**：支持自定义类型检查逻辑。

## 3. 语法与定义

### 类型检查

```ts
// 类型检查函数
util.types.isDate(value: any): boolean
util.types.isPromise(value: any): boolean
util.types.isRegExp(value: any): boolean
util.types.isArrayBuffer(value: any): boolean
// ... 更多类型检查函数
```

### 调试工具

```ts
// 对象检查
util.inspect(object: any, options?: object): string

// 格式化字符串
util.format(format: string, ...args: any[]): string

// 调试日志
util.debuglog(section: string): Function
```

## 4. 基本用法

### 示例 1：类型检查

```ts
// 文件: util-type-check.ts
// 功能: 类型检查

import util from 'node:util';

function validateInput(input: any) {
    // 检查类型
    if (!util.types.isString(input)) {
        throw new Error('Input must be a string');
    }
    
    if (util.types.isDate(input)) {
        console.log('Input is a Date');
    }
    
    if (util.types.isPromise(input)) {
        console.log('Input is a Promise');
    }
    
    if (util.types.isRegExp(input)) {
        console.log('Input is a RegExp');
    }
}

// 使用
validateInput('Hello');
validateInput(new Date());
validateInput(Promise.resolve());
```

### 示例 2：对象检查

```ts
// 文件: util-inspect.ts
// 功能: 对象检查

import util from 'node:util';

const obj = {
    name: 'Alice',
    age: 25,
    nested: {
        key: 'value',
        array: [1, 2, 3],
        func: () => {}
    }
};

// 格式化输出
const formatted = util.inspect(obj, {
    depth: null,        // 无限深度
    colors: true,       // 彩色输出
    compact: false,     // 不紧凑
    showHidden: true   // 显示隐藏属性
});

console.log(formatted);
```

### 示例 3：格式化字符串

```ts
// 文件: util-format.ts
// 功能: 格式化字符串

import util from 'node:util';

// 格式化字符串（类似 printf）
const formatted = util.format('User: %s, Age: %d, Active: %s', 'Alice', 25, true);
console.log(formatted);
// User: Alice, Age: 25, Active: true

// 对象格式化
const objFormatted = util.format('Object: %j', { name: 'Alice', age: 25 });
console.log(objFormatted);
// Object: {"name":"Alice","age":25}
```

### 示例 4：调试日志

```ts
// 文件: util-debuglog.ts
// 功能: 调试日志

import util from 'node:util';

// 创建调试日志函数
const debug = util.debuglog('myapp');

// 只有在 NODE_DEBUG=myapp 时才会输出
debug('This is a debug message');

// 使用
// NODE_DEBUG=myapp node script.js
```

## 5. 参数说明：类型检查和调试工具参数

### inspect 参数

| 参数名       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **object**   | Any      | 要检查的对象                             | `{ name: 'Alice' }`            |
| **options**  | Object   | 选项对象                                 | `{ depth: 2, colors: true }`  |
| **depth**    | Number   | 检查深度（null 表示无限）                | `2` 或 `null`                  |
| **colors**   | Boolean  | 是否使用颜色                             | `true`                         |
| **compact**  | Boolean  | 是否紧凑输出                             | `false`                        |

### format 参数

| 参数名       | 类型     | 说明                                     | 示例                           |
|:-------------|:---------|:-----------------------------------------|:-------------------------------|
| **format**   | String   | 格式化字符串（支持 %s, %d, %j 等）       | `'Hello, %s!'`                 |
| **...args**  | Any      | 要格式化的参数（可变参数）               | `'Alice'`, `25`                |

## 6. 返回值与状态说明

类型检查和调试工具的返回结果：

| 操作类型     | 返回类型     | 说明                                     |
|:-------------|:-------------|:-----------------------------------------|
| **类型检查** | Boolean      | 返回是否为指定类型                       |
| **inspect**  | String       | 返回格式化的字符串表示                   |
| **format**   | String       | 返回格式化后的字符串                     |

## 7. 代码示例：完整的类型检查和调试工具

以下示例演示了如何构建完整的类型检查和调试工具：

```ts
// 文件: util-tools-complete.ts
// 功能: 完整的类型检查和调试工具

import util from 'node:util';

class TypeChecker {
    static isString(value: any): value is string {
        return util.types.isString(value);
    }
    
    static isNumber(value: any): value is number {
        return util.types.isNumber(value);
    }
    
    static isObject(value: any): value is object {
        return util.types.isObject(value) && !util.types.isArray(value);
    }
    
    static isArray(value: any): value is any[] {
        return Array.isArray(value);
    }
    
    static isDate(value: any): value is Date {
        return util.types.isDate(value);
    }
    
    static isPromise(value: any): value is Promise<any> {
        return util.types.isPromise(value);
    }
}

class Debugger {
    static log(obj: any, options?: { depth?: number; colors?: boolean }) {
        console.log(util.inspect(obj, {
            depth: options?.depth ?? 2,
            colors: options?.colors ?? true,
            ...options
        }));
    }
    
    static format(format: string, ...args: any[]) {
        return util.format(format, ...args);
    }
    
    static createDebugLog(section: string) {
        return util.debuglog(section);
    }
}

// 使用
const data: any = {
    name: 'Alice',
    age: 25,
    tags: ['js', 'ts']
};

if (TypeChecker.isString(data.name)) {
    console.log('Name is string:', data.name.toUpperCase());
}

Debugger.log(data, { depth: null });
```

## 8. 输出结果说明

类型检查和调试工具的输出结果：

```text
Name is string: ALICE
{
  name: 'Alice',
  age: 25,
  tags: [ 'js', 'ts' ]
}
```

**逻辑解析**：
- 类型检查用于运行时验证数据类型
- `inspect()` 格式化对象，便于调试
- 类型守卫（Type Guard）提供类型安全

## 9. 使用场景

### 1. API 响应验证

验证 API 响应的数据结构：

```ts
// API 响应验证示例
import util from 'node:util';

function validateAPIResponse(response: any) {
    if (!util.types.isObject(response)) {
        throw new Error('Response must be an object');
    }
    
    if (!util.types.isString(response.name)) {
        throw new Error('Response.name must be a string');
    }
    
    if (!util.types.isNumber(response.age)) {
        throw new Error('Response.age must be a number');
    }
}
```

### 2. 调试输出

格式化调试输出：

```ts
// 调试输出示例
import util from 'node:util';

function debugObject(obj: any, label?: string) {
    if (label) {
        console.log(`${label}:`);
    }
    console.log(util.inspect(obj, { depth: null, colors: true }));
}
```

### 3. 类型守卫

实现类型守卫：

```ts
// 类型守卫示例
import util from 'node:util';

function isUserData(data: any): data is { name: string; age: number } {
    return util.types.isObject(data) &&
           util.types.isString(data.name) &&
           util.types.isNumber(data.age);
}

function processUser(data: any) {
    if (isUserData(data)) {
        // TypeScript 知道 data 的类型
        console.log(data.name, data.age);
    }
}
```

## 10. 注意事项与常见错误

- **类型检查限制**：运行时类型检查不如 TypeScript 编译时检查准确
- **性能考虑**：类型检查可能有性能开销
- **深度检查**：`inspect()` 的深度设置影响输出
- **颜色输出**：颜色输出只在支持颜色的终端中显示
- **现代替代**：优先使用 TypeScript 进行类型检查

## 11. 常见问题 (FAQ)

**Q: 类型检查和 TypeScript 有什么区别？**
A: TypeScript 是编译时类型检查，util.types 是运行时类型检查。两者可以配合使用。

**Q: inspect 和 JSON.stringify 有什么区别？**
A: `inspect()` 更适合调试，支持循环引用、函数等；`JSON.stringify()` 只处理 JSON 兼容的数据。

**Q: 什么时候使用运行时类型检查？**
A: 处理动态数据、API 响应、用户输入等不确定类型的场景。

## 12. 最佳实践

- **配合 TypeScript**：运行时类型检查配合 TypeScript 使用
- **类型守卫**：使用类型守卫提供类型安全
- **调试工具**：使用 `inspect()` 进行调试输出
- **性能考虑**：注意类型检查的性能开销
- **错误处理**：类型检查失败时提供清晰的错误信息

## 13. 对比分析：运行时 vs 编译时类型检查

| 维度             | 运行时类型检查（util.types）              | 编译时类型检查（TypeScript）              |
|:-----------------|:------------------------------------------|:------------------------------------------|
| **检查时机**     | 运行时                                    | 编译时                                    |
| **准确性**       | 较准确                                    | 非常准确                                  |
| **性能影响**     | 有运行时开销                              | 无运行时开销                              |
| **适用场景**     | 动态数据、API 响应                        | 静态代码分析                              |
| **推荐使用**     | 配合 TypeScript 使用                      | 主要类型检查方式                           |

## 14. 练习任务

1. **类型检查实践**：
   - 使用不同的类型检查函数
   - 实现类型守卫
   - 验证 API 响应

2. **调试工具实践**：
   - 使用 inspect 格式化输出
   - 使用 format 格式化字符串
   - 创建调试工具函数

3. **实际应用**：
   - 在实际项目中应用类型检查
   - 实现 API 响应验证
   - 实现调试工具

完成以上练习后，继续学习下一节：其他工具函数。

## 总结

类型检查与调试工具是 util 模块的重要功能：

- **类型检查**：运行时验证数据类型
- **调试工具**：格式化输出，便于调试
- **最佳实践**：配合 TypeScript 使用，注意性能

掌握类型检查与调试工具有助于编写更健壮的代码。

---

**最后更新**：2025-01-XX
