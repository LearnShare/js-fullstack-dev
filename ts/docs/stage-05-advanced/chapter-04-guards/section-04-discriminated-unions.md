# 5.4.4 可辨识联合（Discriminated Unions）

## 概述

可辨识联合是一种类型守卫模式，使用共同的字面量属性来区分联合类型的不同成员。本节介绍可辨识联合的使用。

## 什么是可辨识联合

### 定义

可辨识联合是使用共同的字面量属性（判别式）来区分联合类型不同成员的模式。

### 基本概念

```ts
type Result<T> =
    | { success: true; data: T }
    | { success: false; error: string };

function process<T>(result: Result<T>) {
    if (result.success) {
        // result 的类型是 { success: true; data: T }
        console.log(result.data);
    } else {
        // result 的类型是 { success: false; error: string }
        console.log(result.error);
    }
}
```

## 可辨识联合结构

### 判别式属性

```ts
type Shape =
    | { kind: "circle"; radius: number }
    | { kind: "rectangle"; width: number; height: number }
    | { kind: "triangle"; base: number; height: number };

function getArea(shape: Shape): number {
    switch (shape.kind) {
        case "circle":
            // shape 的类型是 { kind: "circle"; radius: number }
            return Math.PI * shape.radius ** 2;
        case "rectangle":
            // shape 的类型是 { kind: "rectangle"; width: number; height: number }
            return shape.width * shape.height;
        case "triangle":
            // shape 的类型是 { kind: "triangle"; base: number; height: number }
            return (shape.base * shape.height) / 2;
    }
}
```

## 使用场景

### 1. API 响应

```ts
type ApiResponse<T> =
    | { status: "success"; data: T }
    | { status: "error"; message: string };

function handleResponse<T>(response: ApiResponse<T>) {
    if (response.status === "success") {
        return response.data;
    } else {
        throw new Error(response.message);
    }
}
```

### 2. 状态管理

```ts
type State =
    | { type: "idle" }
    | { type: "loading" }
    | { type: "success"; data: any }
    | { type: "error"; error: string };

function handleState(state: State) {
    switch (state.type) {
        case "idle":
            // 处理空闲状态
            break;
        case "loading":
            // 处理加载状态
            break;
        case "success":
            // 处理成功状态
            console.log(state.data);
            break;
        case "error":
            // 处理错误状态
            console.error(state.error);
            break;
    }
}
```

### 3. 事件处理

```ts
type Event =
    | { type: "click"; x: number; y: number }
    | { type: "keypress"; key: string }
    | { type: "scroll"; position: number };

function handleEvent(event: Event) {
    switch (event.type) {
        case "click":
            console.log(`Clicked at (${event.x}, ${event.y})`);
            break;
        case "keypress":
            console.log(`Key pressed: ${event.key}`);
            break;
        case "scroll":
            console.log(`Scrolled to position ${event.position}`);
            break;
    }
}
```

## 类型收窄

### switch 语句

```ts
type Result<T> =
    | { success: true; data: T }
    | { success: false; error: string };

function process<T>(result: Result<T>) {
    switch (result.success) {
        case true:
            // result 的类型是 { success: true; data: T }
            return result.data;
        case false:
            // result 的类型是 { success: false; error: string }
            throw new Error(result.error);
    }
}
```

### if 语句

```ts
function process<T>(result: Result<T>) {
    if (result.success) {
        // result 的类型是 { success: true; data: T }
        return result.data;
    } else {
        // result 的类型是 { success: false; error: string }
        throw new Error(result.error);
    }
}
```

## 常见错误

### 错误 1：缺少判别式

```ts
// 错误：没有共同的判别式属性
type Invalid =
    | { name: string }
    | { age: number };

// 正确：有共同的判别式属性
type Valid =
    | { kind: "name"; name: string }
    | { kind: "age"; age: number };
```

### 错误 2：判别式类型不一致

```ts
// 错误：判别式类型不一致
type Invalid =
    | { kind: "a"; value: string }
    | { kind: 1; value: number };

// 正确：判别式类型一致
type Valid =
    | { kind: "a"; value: string }
    | { kind: "b"; value: number };
```

## 注意事项

1. **判别式属性**：必须有共同的判别式属性
2. **字面量类型**：判别式应该是字面量类型
3. **类型收窄**：使用判别式进行类型收窄
4. **类型安全**：可辨识联合提供类型安全

## 最佳实践

1. **使用可辨识联合**：在需要区分联合类型成员时使用
2. **明确判别式**：使用明确的判别式属性
3. **字面量类型**：判别式使用字面量类型
4. **类型安全**：利用可辨识联合提高类型安全

## 练习

1. **可辨识联合**：定义不同类型的可辨识联合。

2. **类型收窄**：使用可辨识联合进行类型收窄。

3. **实际应用**：在实际场景中应用可辨识联合。

4. **状态管理**：使用可辨识联合管理状态。

完成以上练习后，类型守卫章节学习完成。可以继续学习下一章：类型体操。

## 总结

可辨识联合使用共同的字面量属性来区分联合类型的不同成员。可以使用 switch 或 if 语句进行类型收窄。理解可辨识联合的使用是学习类型守卫的关键。

## 相关资源

- [TypeScript 可辨识联合文档](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#discriminated-unions)
