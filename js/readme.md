# JavaScript 深度编程指南 (Modern ES6+)

**适用对象**：具备通用编程概念（变量、循环、函数），但从未系统学习过 JavaScript 的开发者。
**目标**：从零掌握 JavaScript 独特的动态类型、原型链、事件循环机制，能够编写高质量的异步代码，并熟悉浏览器与 Node.js 的核心 API。  
**版本**：2025 版  
**适用 JavaScript 版本**：ES2022+ (ES13+)

---

## 文档说明

本指南采用分阶段、分章节的结构，每个阶段和章节都是独立的文档文件，便于学习和查阅。所有内容面向零基础学员设计，提供详细的概念解释、语法说明、参数列表、完整示例代码和练习任务。

---

## 目录结构

### 阶段一：环境、运行时与工具链（基础设施）

- [阶段一总览](docs/stage-01-foundation/readme.md)
- [1.0 JavaScript 发展史](docs/stage-01-foundation/chapter-01-history/readme.md)
  - [1.0.1 JavaScript 起源与发展历程](docs/stage-01-foundation/chapter-01-history/section-01-history.md)
  - [1.0.2 ECMAScript 标准演进](docs/stage-01-foundation/chapter-01-history/section-02-ecmascript-evolution.md)
  - [1.0.3 JavaScript 生态系统](docs/stage-01-foundation/chapter-01-history/section-03-ecosystem.md)
- [1.1 JavaScript 运行环境](docs/stage-01-foundation/chapter-02-runtime/readme.md)
  - [1.1.1 JavaScript 运行环境概述](docs/stage-01-foundation/chapter-02-runtime/section-01-overview.md)
  - [1.1.2 浏览器环境与 V8 引擎](docs/stage-01-foundation/chapter-02-runtime/section-02-browser-v8.md)
  - [1.1.3 Node.js 环境](docs/stage-01-foundation/chapter-02-runtime/section-03-nodejs.md)
  - [1.1.4 其他运行时（Deno、Bun）](docs/stage-01-foundation/chapter-02-runtime/section-04-other-runtimes.md)
- [1.2 开发工具链](docs/stage-01-foundation/chapter-03-toolchain/readme.md)
  - [1.2.1 开发工具链概述](docs/stage-01-foundation/chapter-03-toolchain/section-01-overview.md)
  - [1.2.2 代码编辑器与 IDE 配置](docs/stage-01-foundation/chapter-03-toolchain/section-02-editor-ide.md)
  - [1.2.3 包管理器（npm、pnpm、yarn）](docs/stage-01-foundation/chapter-03-toolchain/section-03-package-managers.md)
  - [1.2.4 构建工具（Vite、Webpack、Turbopack）](docs/stage-01-foundation/chapter-03-toolchain/section-04-build-tools.md)
  - [1.2.5 代码质量工具（ESLint、Prettier）](docs/stage-01-foundation/chapter-03-toolchain/section-05-code-quality.md)
  - [1.2.6 调试工具与技巧](docs/stage-01-foundation/chapter-03-toolchain/section-06-debugging.md)
- [1.3 模块化与包管理](docs/stage-01-foundation/chapter-04-modules/readme.md)
  - [1.3.1 模块化与包管理概述](docs/stage-01-foundation/chapter-04-modules/section-01-overview.md)
  - [1.3.2 ES Modules (ESM)](docs/stage-01-foundation/chapter-04-modules/section-02-esm.md)
  - [1.3.3 CommonJS](docs/stage-01-foundation/chapter-04-modules/section-03-commonjs.md)
  - [1.3.4 模块打包与 Tree Shaking](docs/stage-01-foundation/chapter-04-modules/section-04-bundling.md)

### 阶段二：JavaScript 基础语法（语言精通）

- [阶段二总览](docs/stage-02-language/readme.md)
- [2.1 第一个 JavaScript 程序](docs/stage-02-language/chapter-01-hello-world/readme.md)
  - [2.1.1 Hello World 程序](docs/stage-02-language/chapter-01-hello-world/section-01-hello-world.md)
  - [2.1.2 文件结构与编码](docs/stage-02-language/chapter-01-hello-world/section-02-file-structure.md)
  - [2.1.3 语句与注释](docs/stage-02-language/chapter-01-hello-world/section-03-statements-comments.md)
  - [2.1.4 执行方式（浏览器、Node.js、REPL）](docs/stage-02-language/chapter-01-hello-world/section-04-execution.md)
- [2.2 变量与常量](docs/stage-02-language/chapter-02-variables/readme.md)
  - [2.2.1 变量声明（let、const）](docs/stage-02-language/chapter-02-variables/section-01-declarations.md)
  - [2.2.2 var 的问题与暂时性死区（TDZ）](docs/stage-02-language/chapter-02-variables/section-02-var-tdz.md)
  - [2.2.3 常量与引用类型](docs/stage-02-language/chapter-02-variables/section-03-constants.md)
  - [2.2.4 作用域（全局、函数、块级）](docs/stage-02-language/chapter-02-variables/section-04-scope.md)
- [2.3 数据类型](docs/stage-02-language/chapter-03-types/readme.md)
  - [2.3.1 原始类型（Primitives）](docs/stage-02-language/chapter-03-types/section-01-primitives.md)
  - [2.3.2 引用类型（Objects）](docs/stage-02-language/chapter-03-types/section-02-objects.md)
  - [2.3.3 类型检测（typeof、instanceof）](docs/stage-02-language/chapter-03-types/section-03-type-detection.md)
  - [2.3.4 类型转换（隐式与显式）](docs/stage-02-language/chapter-03-types/section-04-type-conversion.md)
- [2.4 运算符与表达式](docs/stage-02-language/chapter-04-operators/readme.md)
  - [2.4.1 算术运算符](docs/stage-02-language/chapter-04-operators/section-01-arithmetic.md)
  - [2.4.2 比较运算符（=== vs ==）](docs/stage-02-language/chapter-04-operators/section-02-comparison.md)
  - [2.4.3 逻辑运算符（&&、||、!）](docs/stage-02-language/chapter-04-operators/section-03-logical.md)
  - [2.4.4 现代运算符（??、?.、??=）](docs/stage-02-language/chapter-04-operators/section-04-modern-operators.md)
  - [2.4.5 运算符优先级](docs/stage-02-language/chapter-04-operators/section-05-precedence.md)
- [2.5 控制结构](docs/stage-02-language/chapter-05-control-flow/readme.md)
  - [2.5.1 条件语句（if、else、switch）](docs/stage-02-language/chapter-05-control-flow/section-01-conditionals.md)
  - [2.5.2 循环结构（for、while、do...while）](docs/stage-02-language/chapter-05-control-flow/section-02-loops.md)
  - [2.5.3 迭代器循环（for...of、for...in）](docs/stage-02-language/chapter-05-control-flow/section-03-iterators.md)
  - [2.5.4 跳转语句（break、continue、return）](docs/stage-02-language/chapter-05-control-flow/section-04-jump-statements.md)
- [2.6 函数](docs/stage-02-language/chapter-06-functions/readme.md)
  - [2.6.1 函数声明与表达式](docs/stage-02-language/chapter-06-functions/section-01-declarations.md)
  - [2.6.2 箭头函数](docs/stage-02-language/chapter-06-functions/section-02-arrow-functions.md)
  - [2.6.3 参数（默认参数、剩余参数）](docs/stage-02-language/chapter-06-functions/section-03-parameters.md)
  - [2.6.4 作用域与闭包](docs/stage-02-language/chapter-06-functions/section-04-scope-closures.md)
  - [2.6.5 高阶函数](docs/stage-02-language/chapter-06-functions/section-05-higher-order.md)
- [2.7 对象与数组](docs/stage-02-language/chapter-07-objects-arrays/readme.md)
  - [2.7.1 对象创建与操作](docs/stage-02-language/chapter-07-objects-arrays/section-01-objects.md)
  - [2.7.2 数组基础与操作](docs/stage-02-language/chapter-07-objects-arrays/section-02-arrays.md)
  - [2.7.3 数组方法（map、filter、reduce）](docs/stage-02-language/chapter-07-objects-arrays/section-03-array-methods.md)
  - [2.7.4 解构赋值](docs/stage-02-language/chapter-07-objects-arrays/section-04-destructuring.md)
  - [2.7.5 展开运算符](docs/stage-02-language/chapter-07-objects-arrays/section-05-spread.md)
- [2.8 字符串操作](docs/stage-02-language/chapter-08-strings/readme.md)
  - [2.8.1 字符串创建与模板字符串](docs/stage-02-language/chapter-08-strings/section-01-creation.md)
  - [2.8.2 字符串方法](docs/stage-02-language/chapter-08-strings/section-02-methods.md)
  - [2.8.3 正则表达式基础](docs/stage-02-language/chapter-08-strings/section-03-regex.md)
  - [2.8.4 正则表达式高级用法](docs/stage-02-language/chapter-08-strings/section-04-regex-advanced.md)
  - [2.8.5 常见正则模式](docs/stage-02-language/chapter-08-strings/section-05-regex-patterns.md)
  - [2.8.6 正则表达式性能优化](docs/stage-02-language/chapter-08-strings/section-06-regex-performance.md)
- [2.9 Set 与 Map](docs/stage-02-language/chapter-09-collections/readme.md)
  - [2.9.1 Set 数据结构](docs/stage-02-language/chapter-09-collections/section-01-set.md)
  - [2.9.2 Map 数据结构](docs/stage-02-language/chapter-09-collections/section-02-map.md)
  - [2.9.3 WeakSet 与 WeakMap](docs/stage-02-language/chapter-09-collections/section-03-weak-collections.md)
- [2.10 面向对象与原型](docs/stage-02-language/chapter-10-oop/readme.md)
  - [2.10.1 原型链机制](docs/stage-02-language/chapter-10-oop/section-01-prototype-chain.md)
  - [2.10.2 ES6 Class 语法](docs/stage-02-language/chapter-10-oop/section-02-class.md)
  - [2.10.3 继承与 super](docs/stage-02-language/chapter-10-oop/section-03-inheritance.md)
  - [2.10.4 this 关键字](docs/stage-02-language/chapter-10-oop/section-04-this.md)
  - [2.10.5 静态方法与属性](docs/stage-02-language/chapter-10-oop/section-05-static.md)
- [2.11 Proxy 与 Reflect](docs/stage-02-language/chapter-11-proxy-reflect/readme.md)
  - [2.11.1 Proxy 与 Reflect 概述](docs/stage-02-language/chapter-11-proxy-reflect/section-01-overview.md)
  - [2.11.2 Proxy 基础](docs/stage-02-language/chapter-11-proxy-reflect/section-02-proxy-basics.md)
  - [2.11.3 Proxy 高级用法](docs/stage-02-language/chapter-11-proxy-reflect/section-03-proxy-advanced.md)
  - [2.11.4 Reflect API](docs/stage-02-language/chapter-11-proxy-reflect/section-04-reflect.md)
  - [2.11.5 元编程实践](docs/stage-02-language/chapter-11-proxy-reflect/section-05-metaprogramming.md)
- [2.12 错误与异常处理](docs/stage-02-language/chapter-12-errors/readme.md)
  - [2.12.1 错误类型](docs/stage-02-language/chapter-12-errors/section-01-error-types.md)
  - [2.12.2 try...catch...finally](docs/stage-02-language/chapter-12-errors/section-02-try-catch.md)
  - [2.12.3 自定义错误](docs/stage-02-language/chapter-12-errors/section-03-custom-errors.md)
- [2.13 JavaScript 版本新特性](docs/stage-02-language/chapter-13-versions/readme.md)
  - [2.13.1 ES2020 新特性](docs/stage-02-language/chapter-13-versions/section-01-es2020.md)
  - [2.13.2 ES2021 新特性](docs/stage-02-language/chapter-13-versions/section-02-es2021.md)
  - [2.13.3 ES2022 新特性](docs/stage-02-language/chapter-13-versions/section-03-es2022.md)
  - [2.13.4 ES2023 新特性](docs/stage-02-language/chapter-13-versions/section-04-es2023.md)
  - [2.13.5 ES2024 新特性](docs/stage-02-language/chapter-13-versions/section-05-es2024.md)
- [2.14 代码规范与最佳实践](docs/stage-02-language/chapter-14-standards/readme.md)
  - [2.14.1 JavaScript 语法指南](docs/stage-02-language/chapter-14-standards/section-01-syntax-guide.md)
  - [2.14.2 命名规范（变量、函数、类）](docs/stage-02-language/chapter-14-standards/section-02-naming-conventions.md)
  - [2.14.3 注释规范（JSDoc）](docs/stage-02-language/chapter-14-standards/section-03-comments.md)
  - [2.14.4 代码风格指南（Airbnb、Google、Standard）](docs/stage-02-language/chapter-14-standards/section-04-style-guides.md)
  - [2.14.5 最佳实践与反模式](docs/stage-02-language/chapter-14-standards/section-05-best-practices.md)

### 阶段三：异步编程（核心能力）

- [阶段三总览](docs/stage-03-async/readme.md)
- [3.1 事件循环机制](docs/stage-03-async/chapter-01-event-loop/readme.md)
  - [3.1.1 事件循环机制概述](docs/stage-03-async/chapter-01-event-loop/section-01-overview.md)
  - [3.1.2 调用栈与任务队列](docs/stage-03-async/chapter-01-event-loop/section-02-call-stack.md)
  - [3.1.3 宏任务与微任务](docs/stage-03-async/chapter-01-event-loop/section-03-macro-micro.md)
  - [3.1.4 浏览器与 Node.js 的事件循环差异](docs/stage-03-async/chapter-01-event-loop/section-04-differences.md)
- [3.2 Promise](docs/stage-03-async/chapter-02-promise/readme.md)
  - [3.2.1 Promise 概述](docs/stage-03-async/chapter-02-promise/section-01-overview.md)
  - [3.2.2 Promise 基础](docs/stage-03-async/chapter-02-promise/section-02-basics.md)
  - [3.2.3 Promise 链式调用](docs/stage-03-async/chapter-02-promise/section-03-chaining.md)
  - [3.2.4 Promise 组合方法（all、race、allSettled）](docs/stage-03-async/chapter-02-promise/section-04-composition.md)
  - [3.2.5 Promise 错误处理](docs/stage-03-async/chapter-02-promise/section-05-error-handling.md)
- [3.3 async/await](docs/stage-03-async/chapter-03-async-await/readme.md)
  - [3.3.1 async/await 概述](docs/stage-03-async/chapter-03-async-await/section-01-overview.md)
  - [3.3.2 async 函数](docs/stage-03-async/chapter-03-async-await/section-02-async-functions.md)
  - [3.3.3 await 表达式](docs/stage-03-async/chapter-03-async-await/section-03-await.md)
  - [3.3.4 错误处理与并行执行](docs/stage-03-async/chapter-03-async-await/section-04-error-parallel.md)
- [3.4 生成器与迭代器](docs/stage-03-async/chapter-04-generators/readme.md)
  - [3.4.1 生成器与迭代器概述](docs/stage-03-async/chapter-04-generators/section-01-overview.md)
  - [3.4.2 迭代器协议](docs/stage-03-async/chapter-04-generators/section-02-iterators.md)
  - [3.4.3 生成器函数](docs/stage-03-async/chapter-04-generators/section-03-generators.md)
  - [3.4.4 异步生成器](docs/stage-03-async/chapter-04-generators/section-04-async-generators.md)

### 阶段四：浏览器环境与 DOM（前端基础）

- [阶段四总览](docs/stage-04-browser/readme.md)
- [4.1 DOM 操作](docs/stage-04-browser/chapter-01-dom/readme.md)
  - [4.1.1 DOM 树结构](docs/stage-04-browser/chapter-01-dom/section-01-tree.md)
  - [4.1.2 元素选择与操作](docs/stage-04-browser/chapter-01-dom/section-02-selection.md)
  - [4.1.3 元素创建与删除](docs/stage-04-browser/chapter-01-dom/section-03-creation.md)
  - [4.1.4 属性与样式操作](docs/stage-04-browser/chapter-01-dom/section-04-attributes.md)
- [4.2 事件处理](docs/stage-04-browser/chapter-02-events/readme.md)
  - [4.2.1 事件模型（捕获、冒泡、委托）](docs/stage-04-browser/chapter-02-events/section-01-event-model.md)
  - [4.2.2 事件监听与移除](docs/stage-04-browser/chapter-02-events/section-02-listeners.md)
  - [4.2.3 常见事件类型](docs/stage-04-browser/chapter-02-events/section-03-event-types.md)
  - [4.2.4 自定义事件](docs/stage-04-browser/chapter-02-events/section-04-custom-events.md)
- [4.3 DOM 库概览](docs/stage-04-browser/chapter-03-dom-libs/readme.md)
  - [4.3.1 DOM 库概述](docs/stage-04-browser/chapter-03-dom-libs/section-01-overview.md)
  - [4.3.2 jQuery 简介](docs/stage-04-browser/chapter-03-dom-libs/section-02-jquery.md)
  - [4.3.3 现代 DOM 库（Zepto、Cash）](docs/stage-04-browser/chapter-03-dom-libs/section-03-modern-libs.md)
  - [4.3.4 原生 DOM API vs DOM 库](docs/stage-04-browser/chapter-03-dom-libs/section-04-native-vs-libs.md)
- [4.4 浏览器 API](docs/stage-04-browser/chapter-04-apis/readme.md)
  - [4.4.1 浏览器 API 概述](docs/stage-04-browser/chapter-04-apis/section-01-overview.md)
  - [4.4.2 Fetch API](docs/stage-04-browser/chapter-04-apis/section-02-fetch.md)
  - [4.4.3 数据存储 API（localStorage、sessionStorage、IndexedDB、Cache API）](docs/stage-04-browser/chapter-04-apis/section-03-storage.md)
  - [4.4.4 定时器 API](docs/stage-04-browser/chapter-04-apis/section-04-timers.md)
  - [4.4.5 WebSocket API](docs/stage-04-browser/chapter-04-apis/section-05-websocket.md)
  - [4.4.6 媒体 API（MediaDevices、MediaRecorder、Audio/Video API）](docs/stage-04-browser/chapter-04-apis/section-06-media.md)
  - [4.4.7 Canvas API](docs/stage-04-browser/chapter-04-apis/section-07-canvas.md)
  - [4.4.8 WebGL API](docs/stage-04-browser/chapter-04-apis/section-08-webgl.md)
  - [4.4.9 Web Workers](docs/stage-04-browser/chapter-04-apis/section-09-workers.md)
  - [4.4.10 Service Workers](docs/stage-04-browser/chapter-04-apis/section-10-service-workers.md)
  - [4.4.11 Observer API（Intersection、Resize、Mutation）](docs/stage-04-browser/chapter-04-apis/section-11-observer.md)
  - [4.4.12 Performance API](docs/stage-04-browser/chapter-04-apis/section-12-performance.md)
  - [4.4.13 国际化 API（Intl）](docs/stage-04-browser/chapter-04-apis/section-13-intl.md)
  - [4.4.14 其他现代 API（Geolocation、Notification、Clipboard、File API、Drag & Drop）](docs/stage-04-browser/chapter-04-apis/section-14-other-apis.md)
- [4.5 Web Components](docs/stage-04-browser/chapter-05-web-components/readme.md)
  - [4.5.1 Web Components 概述](docs/stage-04-browser/chapter-05-web-components/section-01-overview.md)
  - [4.5.2 自定义元素（Custom Elements）](docs/stage-04-browser/chapter-05-web-components/section-02-custom-elements.md)
  - [4.5.3 Shadow DOM](docs/stage-04-browser/chapter-05-web-components/section-03-shadow-dom.md)
  - [4.5.4 HTML 模板（Template）](docs/stage-04-browser/chapter-05-web-components/section-04-template.md)
  - [4.5.5 Web Components 最佳实践](docs/stage-04-browser/chapter-05-web-components/section-05-best-practices.md)
- [4.6 WebAssembly（WASM）](docs/stage-04-browser/chapter-06-wasm/readme.md)
  - [4.6.1 WebAssembly 概述](docs/stage-04-browser/chapter-06-wasm/section-01-overview.md)
  - [4.6.2 WebAssembly 基础](docs/stage-04-browser/chapter-06-wasm/section-02-basics.md)
  - [4.6.3 WebAssembly 与 JavaScript 互操作](docs/stage-04-browser/chapter-06-wasm/section-03-interop.md)
  - [4.6.4 WebAssembly 使用场景](docs/stage-04-browser/chapter-06-wasm/section-04-use-cases.md)
- [4.7 BOM（浏览器对象模型）](docs/stage-04-browser/chapter-07-bom/readme.md)
  - [4.7.1 BOM 概述](docs/stage-04-browser/chapter-07-bom/section-01-overview.md)
  - [4.7.2 window 对象](docs/stage-04-browser/chapter-07-bom/section-02-window.md)
  - [4.7.3 location 对象](docs/stage-04-browser/chapter-07-bom/section-03-location.md)
  - [4.7.4 history 对象](docs/stage-04-browser/chapter-07-bom/section-04-history.md)
  - [4.7.5 navigator 对象](docs/stage-04-browser/chapter-07-bom/section-05-navigator.md)

### 阶段五：现代工具与库（工程化）

- [阶段五总览](docs/stage-05-tools/readme.md)
- [5.1 常用工具与库概览](docs/stage-05-tools/chapter-01-overview/readme.md)
  - [5.1.1 日期时间处理库](docs/stage-05-tools/chapter-01-overview/section-01-datetime.md)
  - [5.1.2 工具函数库](docs/stage-05-tools/chapter-01-overview/section-02-utils.md)
  - [5.1.3 HTTP 客户端库](docs/stage-05-tools/chapter-01-overview/section-03-http-clients.md)
  - [5.1.4 测试框架](docs/stage-05-tools/chapter-01-overview/section-04-testing.md)
  - [5.1.5 代码质量工具](docs/stage-05-tools/chapter-01-overview/section-05-quality.md)
  - [5.1.6 历史技术与库](docs/stage-05-tools/chapter-01-overview/section-06-legacy.md)
  - [5.1.7 Markdown 处理](docs/stage-05-tools/chapter-01-overview/section-07-markdown.md)

### 阶段六：前端框架与库概览（框架生态）

- [阶段六总览](docs/stage-06-frameworks/readme.md)
- [6.1 JSX 语法](docs/stage-06-frameworks/chapter-01-jsx/readme.md)
  - [6.1.1 JSX 基础与语法](docs/stage-06-frameworks/chapter-01-jsx/section-01-basics.md)
  - [6.1.2 JSX 表达式与属性](docs/stage-06-frameworks/chapter-01-jsx/section-02-expressions-props.md)
  - [6.1.3 JSX 条件渲染与列表](docs/stage-06-frameworks/chapter-01-jsx/section-03-conditional-lists.md)
  - [6.1.4 JSX 编译原理](docs/stage-06-frameworks/chapter-01-jsx/section-04-compilation.md)
- [6.2 前端框架概览](docs/stage-06-frameworks/chapter-02-overview/readme.md)
  - [6.2.1 React 框架简介](docs/stage-06-frameworks/chapter-02-overview/section-01-react.md)
  - [6.2.2 Vue 框架简介](docs/stage-06-frameworks/chapter-02-overview/section-02-vue.md)
  - [6.2.3 Angular 框架简介](docs/stage-06-frameworks/chapter-02-overview/section-03-angular.md)
  - [6.2.4 其他前端框架](docs/stage-06-frameworks/chapter-02-overview/section-04-other-frameworks.md)
- [6.3 全栈框架概览](docs/stage-06-frameworks/chapter-03-fullstack/readme.md)
  - [6.3.1 Next.js 简介](docs/stage-06-frameworks/chapter-03-fullstack/section-01-nextjs.md)
  - [6.3.2 Nuxt.js 简介](docs/stage-06-frameworks/chapter-03-fullstack/section-02-nuxtjs.md)
  - [6.3.3 Remix 简介](docs/stage-06-frameworks/chapter-03-fullstack/section-03-remix.md)
  - [6.3.4 其他全栈框架](docs/stage-06-frameworks/chapter-03-fullstack/section-04-other-frameworks.md)
- [6.4 JAMstack 架构](docs/stage-06-frameworks/chapter-04-jamstack/readme.md)
  - [6.4.1 JAMstack 概念与原理](docs/stage-06-frameworks/chapter-04-jamstack/section-01-concept.md)
  - [6.4.2 静态站点生成器](docs/stage-06-frameworks/chapter-04-jamstack/section-02-ssg.md)
  - [6.4.3 Headless CMS](docs/stage-06-frameworks/chapter-04-jamstack/section-03-headless-cms.md)
  - [6.4.4 CDN 与边缘计算](docs/stage-06-frameworks/chapter-04-jamstack/section-04-cdn-edge.md)

### 阶段七：性能优化与最佳实践（生产级）

- [阶段七总览](docs/stage-07-performance/readme.md)
- [7.1 代码优化](docs/stage-07-performance/chapter-01-code/readme.md)
  - [7.1.1 算法优化](docs/stage-07-performance/chapter-01-code/section-01-algorithms.md)
  - [7.1.2 内存管理](docs/stage-07-performance/chapter-01-code/section-02-memory.md)
  - [7.1.3 垃圾回收机制](docs/stage-07-performance/chapter-01-code/section-03-gc.md)
- [7.2 浏览器性能优化](docs/stage-07-performance/chapter-02-browser/readme.md)
  - [7.2.1 渲染性能优化](docs/stage-07-performance/chapter-02-browser/section-01-rendering.md)
  - [7.2.2 网络性能优化](docs/stage-07-performance/chapter-02-browser/section-02-network.md)
  - [7.2.3 代码分割与懒加载](docs/stage-07-performance/chapter-02-browser/section-03-code-splitting.md)
- [7.3 调试与性能分析](docs/stage-07-performance/chapter-03-debugging/readme.md)
  - [7.3.1 Chrome DevTools 使用](docs/stage-07-performance/chapter-03-debugging/section-01-devtools.md)
  - [7.3.2 性能分析工具](docs/stage-07-performance/chapter-03-debugging/section-02-profiling.md)
  - [7.3.3 常见错误与解决方案](docs/stage-07-performance/chapter-03-debugging/section-03-common-errors.md)

---

## 学习路径建议

### 初学者路径

1. **阶段一**：搭建开发环境，掌握基础工具
2. **阶段二**：系统学习 JavaScript 语言基础（包括代码规范）
3. **阶段三**：深入理解异步编程机制
4. **阶段四**：学习浏览器环境与 DOM 操作
5. **阶段五**：了解常用工具与库
6. **阶段六**：了解前端框架与全栈框架生态
7. **阶段七**：了解性能优化与最佳实践

### 有经验开发者路径

- 可直接跳转到感兴趣的阶段
- 建议重点学习阶段三（异步编程）、阶段四（浏览器 API）、阶段七（性能优化）

---

## 文档特点

- **面向零基础**：所有内容从基础概念开始，循序渐进
- **内容详实**：提供完整的语法、参数说明和使用示例
- **示例丰富**：每个知识点都配有完整的代码示例
- **实践导向**：每章都包含练习任务，帮助巩固学习
- **结构清晰**：按阶段、章节、小节分层组织，便于查阅
- **技术前沿**：反映 2025 年最新的 JavaScript 技术和工具生态

---

## 版本信息

- **版本**：2025.1
- **创建日期**：2025-12-11
- **适用 JavaScript 版本**：ES2022+ (ES13+)
- **最后更新**：2025-12-11
