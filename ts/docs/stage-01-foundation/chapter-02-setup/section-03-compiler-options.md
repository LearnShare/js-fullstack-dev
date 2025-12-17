# 1.1.3 编译器选项

## 概述

TypeScript 编译器提供了丰富的选项来控制编译行为。本节介绍常用的编译器选项及其作用。

## 类型检查选项

### strict

启用所有严格类型检查选项。

**默认值**：`false`

```json
{
  "compilerOptions": {
    "strict": true
  }
}
```

启用 `strict` 会同时启用以下选项：
- `strictNullChecks`
- `strictFunctionTypes`
- `strictBindCallApply`
- `strictPropertyInitialization`
- `noImplicitThis`
- `alwaysStrict`

### strictNullChecks

启用严格的 null 检查。

**默认值**：`false`（如果 `strict: true` 则为 `true`）

```json
{
  "compilerOptions": {
    "strictNullChecks": true
  }
}
```

启用后，`null` 和 `undefined` 需要明确处理。

```ts
// strictNullChecks: false（默认）
let value: string = null; // 允许

// strictNullChecks: true
let value: string = null; // 错误
let value: string | null = null; // 正确
```

### noImplicitAny

不允许隐式 any 类型。

**默认值**：`false`（如果 `strict: true` 则为 `true`）

```json
{
  "compilerOptions": {
    "noImplicitAny": true
  }
}
```

```ts
// noImplicitAny: false（默认）
function fn(param) { // param 的类型是 any
  return param;
}

// noImplicitAny: true
function fn(param) { // 错误：参数有隐式 any 类型
  return param;
}
function fn(param: string) { // 正确
  return param;
}
```

### strictFunctionTypes

对函数类型进行更严格的检查。

**默认值**：`false`（如果 `strict: true` 则为 `true`）

### strictBindCallApply

对 `bind`、`call`、`apply` 进行严格检查。

**默认值**：`false`（如果 `strict: true` 则为 `true`）

### strictPropertyInitialization

要求类属性必须在构造函数中初始化。

**默认值**：`false`（如果 `strict: true` 则为 `true`）

```ts
// strictPropertyInitialization: true
class User {
  name: string; // 错误：属性未初始化
}

class User {
  name: string;
  constructor(name: string) {
    this.name = name; // 正确
  }
}
```

### noImplicitThis

不允许隐式 this。

**默认值**：`false`（如果 `strict: true` 则为 `true`）

## 模块选项

### target

编译目标 ECMAScript 版本。

**默认值**：`ES3`

```json
{
  "compilerOptions": {
    "target": "ES2020"
  }
}
```

可选值：`ES3`、`ES5`、`ES2015`、`ES2016`、`ES2017`、`ES2018`、`ES2019`、`ES2020`、`ES2021`、`ES2022`、`ESNext`

### module

指定模块系统。

**默认值**：根据 `target` 自动选择

```json
{
  "compilerOptions": {
    "module": "commonjs"
  }
}
```

常用值：`commonjs`、`ES2015`、`ES2020`、`ESNext`、`Node16`、`NodeNext`、`bundler`

### moduleResolution

指定模块解析策略。

**默认值**：根据 `module` 自动选择

```json
{
  "compilerOptions": {
    "moduleResolution": "node"
  }
}
```

可选值：`node`、`classic`、`bundler`、`node16`、`nodenext`

### esModuleInterop

启用 ES 模块互操作性。

**默认值**：`false`

```json
{
  "compilerOptions": {
    "esModuleInterop": true
  }
}
```

### allowSyntheticDefaultImports

允许从没有默认导出的模块中导入默认值。

**默认值**：`false`（如果 `esModuleInterop: true` 则为 `true`）

## 输出选项

### outDir

指定输出目录。

```json
{
  "compilerOptions": {
    "outDir": "./dist"
  }
}
```

### outFile

将所有文件合并为一个输出文件（仅当 `module` 为 `amd` 或 `system` 时可用）。

```json
{
  "compilerOptions": {
    "outFile": "./dist/bundle.js",
    "module": "amd"
  }
}
```

### rootDir

指定根目录。

```json
{
  "compilerOptions": {
    "rootDir": "./src"
  }
}
```

### declaration

生成声明文件（.d.ts）。

**默认值**：`false`

```json
{
  "compilerOptions": {
    "declaration": true
  }
}
```

### declarationMap

为声明文件生成 source map。

**默认值**：`false`

### sourceMap

生成 source map 文件。

**默认值**：`false`

```json
{
  "compilerOptions": {
    "sourceMap": true
  }
}
```

### removeComments

移除注释。

**默认值**：`false`

## JavaScript 支持

### allowJs

允许编译 JavaScript 文件。

**默认值**：`false`

```json
{
  "compilerOptions": {
    "allowJs": true
  }
}
```

### checkJs

在 JavaScript 文件中进行类型检查（需要 `allowJs: true`）。

**默认值**：`false`

```json
{
  "compilerOptions": {
    "allowJs": true,
    "checkJs": true
  }
}
```

## 其他选项

### lib

指定要包含的类型定义库。

```json
{
  "compilerOptions": {
    "lib": ["ES2020", "DOM", "DOM.Iterable"]
  }
}
```

### skipLibCheck

跳过声明文件的类型检查。

**默认值**：`false`

```json
{
  "compilerOptions": {
    "skipLibCheck": true
  }
}
```

### forceConsistentCasingInFileNames

强制文件名大小写一致。

**默认值**：`false`

### resolveJsonModule

允许导入 JSON 文件。

**默认值**：`false`

```json
{
  "compilerOptions": {
    "resolveJsonModule": true
  }
}
```

```ts
import data from './data.json';
```

### isolatedModules

确保每个文件都可以独立编译。

**默认值**：`false`

### noEmit

不生成输出文件，仅进行类型检查。

**默认值**：`false`

```json
{
  "compilerOptions": {
    "noEmit": true
  }
}
```

### incremental

启用增量编译。

**默认值**：`false`

```json
{
  "compilerOptions": {
    "incremental": true
  }
}
```

### composite

启用项目引用。

**默认值**：`false`

```json
{
  "compilerOptions": {
    "composite": true
  }
}
```

## 配置建议

### 推荐配置（严格模式）

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "lib": ["ES2020"],
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true
  }
}
```

### 浏览器项目配置

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx"
  }
}
```

## 注意事项

1. **strict 模式**：建议启用 strict 模式，获得更好的类型安全
2. **target 选择**：根据运行环境选择合适的 target
3. **模块系统**：根据项目需求选择合适的模块系统
4. **性能考虑**：某些选项可能影响编译性能

## 最佳实践

1. **启用 strict**：始终启用 strict 模式
2. **明确配置**：明确配置所有必要的选项
3. **环境适配**：根据运行环境选择合适的配置
4. **性能优化**：使用增量编译和项目引用提升性能

## 练习

1. **配置实践**：创建 tsconfig.json，配置不同的编译器选项。

2. **strict 模式**：启用 strict 模式，体验类型检查的严格性。

3. **模块配置**：尝试不同的 module 和 moduleResolution 配置。

4. **输出配置**：配置 outDir、declaration、sourceMap 等输出选项。

5. **配置对比**：对比不同配置的效果和差异。

完成以上练习后，继续学习下一节，了解 IDE 配置。

## 总结

TypeScript 编译器提供了丰富的选项来控制编译行为。理解这些选项的作用和影响是配置 TypeScript 项目的关键。建议启用 strict 模式，获得更好的类型安全和开发体验。

## 相关资源

- [TypeScript 编译器选项文档](https://www.typescriptlang.org/tsconfig#compilerOptions)
