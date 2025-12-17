# 8.5.1 tsd 类型测试

## 概述

tsd 是一个类型测试工具，可以验证类型定义的正确性。本节介绍 tsd 的使用。

## 安装

```bash
npm install --save-dev tsd
```

## 基本使用

### 1. 创建测试文件

创建 `.test-d.ts` 文件：

```ts
// types.test-d.ts
import { expectType } from "tsd";
import { User } from "./types";

expectType<string>(new User("John").name);
```

### 2. 运行测试

```bash
npx tsd
```

## 使用场景

### 1. 类型定义测试

测试类型定义：

```ts
import { expectType } from "tsd";
import { User } from "./types";

expectType<string>(new User("John").name);
expectType<number>(new User("John", 30).age);
```

### 2. 工具类型测试

测试工具类型：

```ts
import { expectType } from "tsd";
import { Partial } from "./utils";

type User = { name: string; age: number };
expectType<{ name?: string; age?: number }>({} as Partial<User>);
```

## 注意事项

1. **测试文件**：使用 `.test-d.ts` 扩展名
2. **导入工具**：导入 `expectType` 等工具
3. **类型验证**：验证类型定义的正确性

## 最佳实践

1. **使用 tsd**：使用 tsd 进行类型测试
2. **测试类型**：测试重要的类型定义
3. **持续测试**：持续进行类型测试

## 练习

1. **tsd 测试**：使用 tsd 进行类型测试。

2. **类型验证**：验证类型定义的正确性。

3. **实际应用**：在实际项目中使用 tsd。

完成以上练习后，继续学习下一节，了解 dtslint 类型测试。

## 总结

tsd 是一个类型测试工具，可以验证类型定义的正确性。创建 `.test-d.ts` 文件，使用 `expectType` 等工具进行类型测试。理解 tsd 的使用是学习类型测试的关键。

## 相关资源

- [tsd GitHub](https://github.com/SamVerschueren/tsd)
