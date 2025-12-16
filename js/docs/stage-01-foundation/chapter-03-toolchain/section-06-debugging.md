# 1.2.6 调试工具与技巧

## 概述

调试是保障代码质量和稳定性的关键步骤。现代调试不仅包含断点与日志，还涉及网络、性能、内存、Source Map、远程调试、移动端与 Node.js 服务器调试。本节覆盖浏览器、VS Code、Node Inspector 的高频操作、常见陷阱与最佳实践，并提供可直接复用的配置与检查清单。

## 浏览器调试（以 Chrome DevTools 为例）

### 打开方式
- `F12` / `Ctrl+Shift+I`（macOS: `Cmd+Opt+I`）
- 右键页面 → 检查
- `chrome://inspect`（远程/Node）

### 主要面板与用途
- **Elements**：DOM/CSS 查看与实时修改；强制状态（:hover、:focus）；布局/Box Model。
- **Console**：日志、表达式求值、`$0`/`$_` 临时变量、`console.table`/`group`/`time`。
- **Sources**：断点（行/条件/事件/XHR/DOM 变动）、调用栈、Scope/Watch、Step Over/Into/Out、黑箱脚本。
- **Network**：请求瀑布、状态码、缓存命中、CORS、重定向、Cookies、阻塞原因，导出 cURL。
- **Performance**：记录主线程、帧率、长任务、布局/绘制耗时，定位卡顿点。
- **Application**：localStorage、sessionStorage、IndexedDB、Cache、Service Worker、Manifest。
- **Memory**：堆快照、分配检测、泄漏定位（Detached DOM、未释放监听）。
- **Lighthouse**：自动化性能与可访问性评估。

### 断点与高级用法
- 行/条件断点：右键行号添加条件，如 `count > 10`。
- XHR/Fetch 断点：按 URL 关键字拦截请求。
- 事件监听器断点：click、input、DOMSubtreeModified 等。
- DOM 断点：属性/子树修改时中断。
- 黑箱脚本：忽略第三方/框架代码，聚焦业务。
- Watch 与 Scope：减少反复 `console.log`，实时观察变量。

### 日志技巧

#### console.log()

**语法格式**：`console.log(...data)`

**参数说明**：

| 参数名   | 类型 | 说明                           | 是否必需 | 默认值 |
|:---------|:-----|:-------------------------------|:---------|:-------|
| `...data` | any  | 要输出的数据（可多个）         | 是       | -      |

**返回值**：`undefined`

**说明**：最常用的日志方法，可以输出多个值

```js
console.log('Hello', 'World', 123);
console.log({ name: 'John', age: 30 });
```

#### console.table()

**语法格式**：`console.table(data[, columns])`

**参数说明**：

| 参数名     | 类型           | 说明                           | 是否必需 | 默认值 |
|:-----------|:---------------|:-------------------------------|:---------|:-------|
| `data`     | Array\|Object  | 要显示为表格的数据             | 是       | -      |
| `columns`  | Array          | 要显示的列（仅数组时有效）     | 否       | -      |

**返回值**：`undefined`

**说明**：以表格形式显示数组或对象，便于查看结构化数据

```js
const users = [
  { name: 'John', age: 30 },
  { name: 'Jane', age: 25 }
];
console.table(users);

// 只显示指定列
console.table(users, ['name']);
```

#### console.time() 和 console.timeEnd()

**语法格式**：`console.time(label)` / `console.timeEnd(label)`

**参数说明**：

| 参数名   | 类型   | 说明                           | 是否必需 | 默认值 |
|:---------|:-------|:-------------------------------|:---------|:-------|
| `label`  | string | 计时器标签                     | 是       | -      |

**返回值**：`undefined`

**说明**：测量代码执行时间，`time()` 开始计时，`timeEnd()` 结束并输出

```js
console.time('calc');
// 执行一些操作
for (let i = 0; i < 1000000; i++) {
  // ...
}
console.timeEnd('calc'); // calc: 123.456ms
```

#### console.group() 和 console.groupEnd()

**语法格式**：`console.group([label])` / `console.groupEnd()`

**参数说明**：

| 参数名   | 类型   | 说明                           | 是否必需 | 默认值 |
|:---------|:-------|:-------------------------------|:---------|:-------|
| `label`  | string | 分组标签                       | 否       | -      |

**返回值**：`undefined`

**说明**：创建日志分组，便于组织相关日志

```js
console.group('Task');
console.log('Step 1');
console.log('Step 2');
console.groupEnd();
```

#### console.assert()

**语法格式**：`console.assert(condition, ...data)`

**参数说明**：

| 参数名       | 类型    | 说明                           | 是否必需 | 默认值 |
|:-------------|:--------|:-------------------------------|:---------|:-------|
| `condition`  | boolean | 断言条件                       | 是       | -      |
| `...data`    | any     | 条件为 false 时输出的数据      | 否       | -      |

**返回值**：`undefined`

**说明**：如果条件为 `false`，输出错误信息

```js
const value = null;
console.assert(value !== null, 'value should not be null', { value });
// 输出：Assertion failed: value should not be null { value: null }
```

#### 其他常用 console 方法

**console.error()**：输出错误信息（红色）

```js
console.error('Error:', error);
```

**console.warn()**：输出警告信息（黄色）

```js
console.warn('Warning: This is deprecated');
```

**console.trace()**：输出调用栈

```js
function a() {
  b();
}
function b() {
  console.trace('Trace');
}
a();
// 输出调用栈
```

### 性能与网络排查
- Performance 录制查找 Long Task（>50ms）、频繁布局/样式抖动、JS 热点。
- Network 查看缓存状态（Memory/Disk）、阻塞、重试、CORS、请求体大小。
- 覆盖（Overrides）：本地文件替换远端资源（Application -> Overrides）。
- Source Map：确保构建产物携带 map，并在 DevTools 启用 JS/CSS source maps。

## Node.js 调试

### VS Code 调试（推荐）

**配置说明**：创建 `.vscode/launch.json` 文件

**参数说明**：

| 参数名         | 类型   | 说明                           | 是否必需 | 默认值 |
|:---------------|:-------|:-------------------------------|:---------|:-------|
| `type`         | string | 调试器类型（"node"）           | 是       | -      |
| `request`       | string | 请求类型（"launch" 或 "attach"）| 是       | -      |
| `name`          | string | 配置名称                       | 是       | -      |
| `program`       | string | 要调试的文件路径               | 是       | -      |
| `console`       | string | 控制台类型                     | 否       | "internalConsole" |
| `skipFiles`     | Array  | 要跳过的文件模式               | 否       | -      |
| `env`           | Object | 环境变量                       | 否       | -      |

**示例配置**：

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "Launch Node.js",
      "program": "${workspaceFolder}/index.js",
      "console": "integratedTerminal",
      "skipFiles": ["<node_internals>/**", "**/node_modules/**"],
      "env": { "NODE_ENV": "development" }
    }
  ]
}
```

**使用步骤**：
1. 在代码中设置断点（点击行号左侧）
2. 按 `F5` 启动调试
3. 观察变量、调用栈、Watch 表达式
4. 使用调试工具栏控制执行流程

### Node Inspector
```bash
node --inspect=9229 index.js
# Chrome 访问 chrome://inspect，或通过 SSH 隧道远程调试
```

### 常见场景
- **异步/Promise**：在 async 函数中断点，查看 Microtask 队列；捕获未处理拒绝。
- **内存泄漏**：`--inspect` + Memory 快照，查找长时间存活对象、未清理监听/定时器。
- **性能热点**：`--inspect` + Performance/CPU Profile，识别阻塞事件循环的同步任务。

## 远程与移动端调试
- Chrome 远程设备：`chrome://inspect/#devices`，Android USB 调试。
- Safari Web Inspector：调试 iOS WebView/移动 Safari。
- 抓包：Charles/Fiddler/Proxyman；处理 HTTPS 需安装信任证书。
- 小程序/Hybrid：使用平台提供的开发者工具或内置调试面板。

## Source Map 策略
- 开发：`inline-source-map` 或高质量 map，便于断点与快速定位。
- 生产：`hidden-source-map` / `nosources-source-map`，避免源码暴露；上传 map 至监控平台（如 Sentry），勿直接对公网开放。
- 校验 map：行号错位常因版本不匹配或 map 路径错误。

## 常见问题与排查
- **断点不命中**：确认 map 生效、脚本未被黑箱、路径一致；检查是否是构建后文件。
- **this/作用域异常**：查看 Call Stack 与 Scope，检查箭头函数/绑定。
- **性能卡顿**：录制 Performance，查长任务、频繁回流、JS 热点；避免大 JSON 同步解析。
- **网络失败**：看 CORS、状态码、缓存、重试策略；必要时抓包。
- **内存增长**：拍多份堆快照对比，关注 Detached DOM、全局缓存、未清理监听。

## 最佳实践清单
1) Dev 环境开启高质量 Source Map；Prod 使用 hidden/nosources 并上传到监控。  
2) 多用条件/XHR/事件断点，减少刷日志。  
3) 黑箱第三方脚本，聚焦业务代码；Node 调试跳过 node_modules。  
4) 日志分组与分级，必要时 `console.assert/trace/table/time`。  
5) 性能问题先录制再优化，定位长任务和布局抖动；内存问题用快照对比。  
6) 远程/移动端问题用 chrome://inspect、Web Inspector 或抓包工具复现。  
7) 断点 + Watch 替代无序打印；调试结束后清理临时代码。  
8) 避免在生产暴露 Source Map；错误还原走监控平台。  

## 练习
1. 在 DevTools 为特定 URL 的 XHR 设置断点，打印调用栈并查看请求头。  
2. 为 Node 项目创建 VS Code 调试配置，支持环境变量、跳过 node_modules、断点调试。  
3. 录制 Performance，定位最长的 Long Task，并给出优化思路。  
4. 构造一个未清理事件监听导致的内存泄漏，使用内存快照定位并修复。  
5. 生成生产构建的 hidden Source Map，上传到监控平台还原压缩栈信息。  

## 小结

- DevTools/VS Code/Inspector 是主力调试阵地，熟练断点、Network、Performance、Memory 能显著提效。  
- Source Map 是跨环境定位的关键，生产需兼顾安全与可观测性。  
- 远程、移动端、Node 环境均可通过 inspect/抓包/平台工具完成调试。  
- 性能与内存问题以录制与数据为先导，避免盲目猜测。  

完成本节后，可将调试技巧与后续性能优化、异步编程章节结合，形成系统的排查能力。
