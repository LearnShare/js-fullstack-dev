# Node.js 全栈开发指南 (TypeScript First)

**适用对象**：已掌握 JavaScript 和 TypeScript 基础，希望从零开始掌握 Node.js 全栈开发的开发者。  
**目标**：从 Node.js 运行时架构出发，掌握后端开发、数据库操作、API 设计、安全、性能优化和部署，最终具备独立设计与开发企业级全栈应用的能力。  
**版本**：2025 版  
**适用 Node.js 版本**：Node.js 22+  
**代码语言**：TypeScript（优先）

---

## 文档说明

本指南采用分阶段、分章节的结构，每个阶段和章节都是独立的文档文件，便于学习和查阅。所有内容面向已掌握 JavaScript/TypeScript 基础的开发者设计，提供详细的概念解释、语法说明、参数列表、完整示例代码和练习任务。**所有代码示例优先使用 TypeScript 编写**。

---

## 目录结构

### 阶段一：Node.js 运行时与架构（基础）

- [阶段一总览](docs/stage-01-foundation/README.md)
- [1.0 Node.js 发展史](docs/stage-01-foundation/chapter-01-history/README.md)
  - [1.0.1 Node.js 起源与发展历程](docs/stage-01-foundation/chapter-01-history/section-01-history.md)
  - [1.0.2 Node.js 版本演进（0.x - 22.x）](docs/stage-01-foundation/chapter-01-history/section-02-version-evolution.md)
  - [1.0.3 Node.js 生态系统](docs/stage-01-foundation/chapter-01-history/section-03-ecosystem.md)
- [1.1 Node.js 运行时架构](docs/stage-01-foundation/chapter-02-runtime/README.md)
  - [1.1.1 Node.js 运行时架构概述](docs/stage-01-foundation/chapter-02-runtime/section-01-overview.md)
  - [1.1.2 V8 引擎](docs/stage-01-foundation/chapter-02-runtime/section-02-v8.md)
  - [1.1.3 Libuv 与事件循环](docs/stage-01-foundation/chapter-02-runtime/section-03-libuv.md)
  - [1.1.4 单线程模型与事件驱动](docs/stage-01-foundation/chapter-02-runtime/section-04-event-driven.md)
  - [1.1.5 Worker Threads（多线程）](docs/stage-01-foundation/chapter-02-runtime/section-05-worker-threads.md)
- [1.2 Node.js 安装与版本管理](docs/stage-01-foundation/chapter-03-installation/README.md)
  - [1.2.1 Node.js 安装](docs/stage-01-foundation/chapter-03-installation/section-01-installation.md)
  - [1.2.2 版本管理工具（nvm、fnm）](docs/stage-01-foundation/chapter-03-installation/section-02-version-managers.md)
  - [1.2.3 验证与测试](docs/stage-01-foundation/chapter-03-installation/section-03-verification.md)
- [1.3 TypeScript 项目初始化](docs/stage-01-foundation/chapter-04-typescript-setup/README.md)
  - [1.3.1 TypeScript 项目初始化](docs/stage-01-foundation/chapter-04-typescript-setup/section-01-init.md)
  - [1.3.2 tsconfig.json 配置](docs/stage-01-foundation/chapter-04-typescript-setup/section-02-tsconfig.md)
  - [1.3.3 ts-node 与 tsx](docs/stage-01-foundation/chapter-04-typescript-setup/section-03-ts-node-tsx.md)
  - [1.3.4 构建与运行](docs/stage-01-foundation/chapter-04-typescript-setup/section-04-build-run.md)

### 阶段二：核心模块与基础 API（核心能力）

- [阶段二总览](docs/stage-02-core/README.md)
- [2.1 模块系统](docs/stage-02-core/chapter-01-modules/README.md)
  - [2.1.1 模块系统概述](docs/stage-02-core/chapter-01-modules/section-01-overview.md)
  - [2.1.2 CommonJS 模块](docs/stage-02-core/chapter-01-modules/section-02-commonjs.md)
  - [2.1.3 ES Modules (ESM)](docs/stage-02-core/chapter-01-modules/section-03-esm.md)
  - [2.1.4 模块解析与加载](docs/stage-02-core/chapter-01-modules/section-04-resolution.md)
- [2.2 文件系统（fs）](docs/stage-02-core/chapter-02-fs/README.md)
  - [2.2.1 文件系统概述](docs/stage-02-core/chapter-02-fs/section-01-overview.md)
  - [2.2.2 文件读写（同步与异步）](docs/stage-02-core/chapter-02-fs/section-02-read-write.md)
  - [2.2.3 Promise 版本（fs/promises）](docs/stage-02-core/chapter-02-fs/section-03-promises.md)
  - [2.2.4 目录操作](docs/stage-02-core/chapter-02-fs/section-04-directories.md)
  - [2.2.5 文件监听（watch）](docs/stage-02-core/chapter-02-fs/section-05-watch.md)
- [2.3 路径处理（path）](docs/stage-02-core/chapter-03-path/README.md)
  - [2.3.1 路径拼接与解析](docs/stage-02-core/chapter-03-path/section-01-join-resolve.md)
  - [2.3.2 路径信息获取](docs/stage-02-core/chapter-03-path/section-02-info.md)
  - [2.3.3 跨平台兼容性](docs/stage-02-core/chapter-03-path/section-03-cross-platform.md)
- [2.4 HTTP 模块](docs/stage-02-core/chapter-04-http/README.md)
  - [2.4.1 HTTP 模块概述](docs/stage-02-core/chapter-04-http/section-01-overview.md)
  - [2.4.2 创建 HTTP 服务器](docs/stage-02-core/chapter-04-http/section-02-server.md)
  - [2.4.3 处理请求与响应](docs/stage-02-core/chapter-04-http/section-03-request-response.md)
  - [2.4.4 HTTP 客户端](docs/stage-02-core/chapter-04-http/section-04-client.md)
- [2.5 事件系统（events）](docs/stage-02-core/chapter-05-events/README.md)
  - [2.5.1 事件系统概述](docs/stage-02-core/chapter-05-events/section-01-overview.md)
  - [2.5.2 EventEmitter 基础](docs/stage-02-core/chapter-05-events/section-02-eventemitter.md)
  - [2.5.3 事件监听与触发](docs/stage-02-core/chapter-05-events/section-03-listen-emit.md)
  - [2.5.4 自定义事件](docs/stage-02-core/chapter-05-events/section-04-custom-events.md)
- [2.6 加密与安全（crypto）](docs/stage-02-core/chapter-06-crypto/README.md)
  - [2.6.1 加密与安全概述](docs/stage-02-core/chapter-06-crypto/section-01-overview.md)
  - [2.6.2 哈希算法](docs/stage-02-core/chapter-06-crypto/section-02-hash.md)
  - [2.6.3 加密与解密](docs/stage-02-core/chapter-06-crypto/section-03-encryption.md)
  - [2.6.4 数字签名](docs/stage-02-core/chapter-06-crypto/section-04-signature.md)
- [2.7 Buffer 与 Stream](docs/stage-02-core/chapter-07-buffer-stream/README.md)
  - [2.7.1 Buffer 与 Stream 概述](docs/stage-02-core/chapter-07-buffer-stream/section-01-overview.md)
  - [2.7.2 Buffer 基础](docs/stage-02-core/chapter-07-buffer-stream/section-02-buffer.md)
  - [2.7.3 Stream 基础](docs/stage-02-core/chapter-07-buffer-stream/section-03-stream.md)
  - [2.7.4 可读流、可写流、双工流](docs/stage-02-core/chapter-07-buffer-stream/section-04-stream-types.md)
  - [2.7.5 管道（pipe）与背压（backpressure）](docs/stage-02-core/chapter-07-buffer-stream/section-05-pipe-backpressure.md)

### 阶段三：包管理与工具链（工程化）

- [阶段三总览](docs/stage-03-toolchain/README.md)
- [3.1 包管理器](docs/stage-03-toolchain/chapter-01-package-managers/README.md)
  - [3.1.1 包管理器概述](docs/stage-03-toolchain/chapter-01-package-managers/section-01-overview.md)
  - [3.1.2 npm 基础](docs/stage-03-toolchain/chapter-01-package-managers/section-02-npm.md)
  - [3.1.3 pnpm（现代包管理器）](docs/stage-03-toolchain/chapter-01-package-managers/section-03-pnpm.md)
  - [3.1.4 yarn（经典包管理器）](docs/stage-03-toolchain/chapter-01-package-managers/section-04-yarn.md)
  - [3.1.5 package.json 详解](docs/stage-03-toolchain/chapter-01-package-managers/section-05-package-json.md)
- [3.2 构建工具](docs/stage-03-toolchain/chapter-02-build-tools/README.md)
  - [3.2.1 构建工具概述](docs/stage-03-toolchain/chapter-02-build-tools/section-01-overview.md)
  - [3.2.2 Vite（现代构建工具）](docs/stage-03-toolchain/chapter-02-build-tools/section-02-vite.md)
  - [3.2.3 Turbopack（Next.js 构建工具）](docs/stage-03-toolchain/chapter-02-build-tools/section-03-turbopack.md)
  - [3.2.4 Webpack（传统构建工具）](docs/stage-03-toolchain/chapter-02-build-tools/section-04-webpack.md)
- [3.3 代码质量工具](docs/stage-03-toolchain/chapter-03-quality/README.md)
  - [3.3.1 代码质量工具概述](docs/stage-03-toolchain/chapter-03-quality/section-01-overview.md)
  - [3.3.2 ESLint 配置](docs/stage-03-toolchain/chapter-03-quality/section-02-eslint.md)
  - [3.3.3 Prettier 配置](docs/stage-03-toolchain/chapter-03-quality/section-03-prettier.md)
  - [3.3.4 TypeScript 类型检查](docs/stage-03-toolchain/chapter-03-quality/section-04-typescript.md)
- [3.4 Monorepo 管理](docs/stage-03-toolchain/chapter-04-monorepo/README.md)
  - [3.4.1 Monorepo 概述](docs/stage-03-toolchain/chapter-04-monorepo/section-01-overview.md)
  - [3.4.2 Turborepo](docs/stage-03-toolchain/chapter-04-monorepo/section-02-turborepo.md)
  - [3.4.3 Nx](docs/stage-03-toolchain/chapter-04-monorepo/section-03-nx.md)
  - [3.4.4 pnpm Workspaces](docs/stage-03-toolchain/chapter-04-monorepo/section-04-pnpm-workspaces.md)
- [3.5 任务运行器](docs/stage-03-toolchain/chapter-05-task-runners/README.md)
  - [3.5.1 任务运行器概述](docs/stage-03-toolchain/chapter-05-task-runners/section-01-overview.md)
  - [3.5.2 Grunt](docs/stage-03-toolchain/chapter-05-task-runners/section-02-grunt.md)
  - [3.5.3 Gulp](docs/stage-03-toolchain/chapter-05-task-runners/section-03-gulp.md)
  - [3.5.4 现代替代方案](docs/stage-03-toolchain/chapter-05-task-runners/section-04-modern-alternatives.md)
- [3.6 Node.js 生态流行库概览](docs/stage-03-toolchain/chapter-06-popular-libs/README.md)
  - [3.6.1 HTTP 客户端库](docs/stage-03-toolchain/chapter-06-popular-libs/section-01-http-clients.md)
  - [3.6.2 工具函数库](docs/stage-03-toolchain/chapter-06-popular-libs/section-02-utility-libs.md)
  - [3.6.3 日期时间库](docs/stage-03-toolchain/chapter-06-popular-libs/section-03-datetime-libs.md)
  - [3.6.4 验证库](docs/stage-03-toolchain/chapter-06-popular-libs/section-04-validation-libs.md)
  - [3.6.5 Markdown 处理库](docs/stage-03-toolchain/chapter-06-popular-libs/section-05-markdown.md)
  - [3.6.6 其他常用库](docs/stage-03-toolchain/chapter-06-popular-libs/section-06-other-libs.md)

### 阶段四：Web 框架与 API 开发（核心技能）

- [阶段四总览](docs/stage-04-web/README.md)
- [4.1 HTTP 协议与 API 设计](docs/stage-04-web/chapter-01-http-api/README.md)
  - [4.1.1 HTTP 协议与 API 设计概述](docs/stage-04-web/chapter-01-http-api/section-01-overview.md)
  - [4.1.2 HTTP 协议详解](docs/stage-04-web/chapter-01-http-api/section-02-http-protocol.md)
  - [4.1.3 RESTful API 设计原则](docs/stage-04-web/chapter-01-http-api/section-03-restful.md)
  - [4.1.4 API 版本控制](docs/stage-04-web/chapter-01-http-api/section-04-versioning.md)
  - [4.1.5 API 文档（OpenAPI/Swagger）](docs/stage-04-web/chapter-01-http-api/section-05-documentation.md)
- [4.2 Web 框架概览](docs/stage-04-web/chapter-02-frameworks/README.md)
  - [4.2.1 Web 框架概述](docs/stage-04-web/chapter-02-frameworks/section-01-overview.md)
  - [4.2.2 Express.js 简介](docs/stage-04-web/chapter-02-frameworks/section-02-express.md)
  - [4.2.3 Fastify 简介](docs/stage-04-web/chapter-02-frameworks/section-03-fastify.md)
  - [4.2.4 NestJS 简介](docs/stage-04-web/chapter-02-frameworks/section-04-nestjs.md)
  - [4.2.5 Hono 简介](docs/stage-04-web/chapter-02-frameworks/section-05-hono.md)
  - [4.2.6 Elysia 简介](docs/stage-04-web/chapter-02-frameworks/section-06-elysia.md)
  - [4.2.7 其他 Web 框架](docs/stage-04-web/chapter-02-frameworks/section-07-other-frameworks.md)
- [4.3 API 设计范式](docs/stage-04-web/chapter-03-api-paradigms/README.md)
  - [4.3.1 API 设计范式概述](docs/stage-04-web/chapter-03-api-paradigms/section-01-overview.md)
  - [4.3.2 RESTful API](docs/stage-04-web/chapter-03-api-paradigms/section-02-restful.md)
  - [4.3.3 GraphQL API](docs/stage-04-web/chapter-03-api-paradigms/section-03-graphql.md)
  - [4.3.4 tRPC](docs/stage-04-web/chapter-03-api-paradigms/section-04-trpc.md)
  - [4.3.5 gRPC](docs/stage-04-web/chapter-03-api-paradigms/section-05-grpc.md)
- [4.4 全栈框架概览](docs/stage-04-web/chapter-04-fullstack/README.md)
  - [4.4.1 Next.js 简介](docs/stage-04-web/chapter-04-fullstack/section-01-nextjs.md)
  - [4.4.2 Nuxt.js 简介](docs/stage-04-web/chapter-04-fullstack/section-02-nuxtjs.md)
  - [4.4.3 Remix 简介](docs/stage-04-web/chapter-04-fullstack/section-03-remix.md)
  - [4.4.4 其他全栈框架](docs/stage-04-web/chapter-04-fullstack/section-04-other-frameworks.md)
- [4.5 JAMstack 架构](docs/stage-04-web/chapter-05-jamstack/README.md)
  - [4.5.1 JAMstack 概念与原理](docs/stage-04-web/chapter-05-jamstack/section-01-concept.md)
  - [4.5.2 静态站点生成器](docs/stage-04-web/chapter-05-jamstack/section-02-ssg.md)
  - [4.5.3 Headless CMS](docs/stage-04-web/chapter-05-jamstack/section-03-headless-cms.md)
  - [4.5.4 CDN 与边缘计算](docs/stage-04-web/chapter-05-jamstack/section-04-cdn-edge.md)
- [4.6 WebSocket 服务器](docs/stage-04-web/chapter-06-websocket/README.md)
  - [4.6.1 WebSocket 概述](docs/stage-04-web/chapter-06-websocket/section-01-overview.md)
  - [4.6.2 Socket.io](docs/stage-04-web/chapter-06-websocket/section-02-socketio.md)
  - [4.6.3 ws（原生 WebSocket）](docs/stage-04-web/chapter-06-websocket/section-03-ws.md)
  - [4.6.4 WebSocket 最佳实践](docs/stage-04-web/chapter-06-websocket/section-04-best-practices.md)
- [4.7 文件上传处理](docs/stage-04-web/chapter-07-file-upload/README.md)
  - [4.7.1 文件上传概述](docs/stage-04-web/chapter-07-file-upload/section-01-overview.md)
  - [4.7.2 multer](docs/stage-04-web/chapter-07-file-upload/section-02-multer.md)
  - [4.7.3 formidable](docs/stage-04-web/chapter-07-file-upload/section-03-formidable.md)
  - [4.7.4 文件验证与存储](docs/stage-04-web/chapter-07-file-upload/section-04-validation-storage.md)
- [4.8 API 限流](docs/stage-04-web/chapter-08-rate-limiting/README.md)
  - [4.8.1 API 限流概述](docs/stage-04-web/chapter-08-rate-limiting/section-01-overview.md)
  - [4.8.2 express-rate-limit](docs/stage-04-web/chapter-08-rate-limiting/section-02-express-rate-limit.md)
  - [4.8.3 bottleneck](docs/stage-04-web/chapter-08-rate-limiting/section-03-bottleneck.md)
  - [4.8.4 限流策略](docs/stage-04-web/chapter-08-rate-limiting/section-04-strategies.md)
- [4.9 配置管理](docs/stage-04-web/chapter-09-config/README.md)
  - [4.9.1 配置管理概述](docs/stage-04-web/chapter-09-config/section-01-overview.md)
  - [4.9.2 node-config](docs/stage-04-web/chapter-09-config/section-02-node-config.md)
  - [4.9.3 convict](docs/stage-04-web/chapter-09-config/section-03-convict.md)
  - [4.9.4 环境变量管理](docs/stage-04-web/chapter-09-config/section-04-env-vars.md)
- [4.10 模板引擎概览](docs/stage-04-web/chapter-10-templates/README.md)
- [4.11 健康检查](docs/stage-04-web/chapter-11-health/README.md)
  - [4.11.1 健康检查端点](docs/stage-04-web/chapter-11-health/section-01-endpoints.md)
  - [4.11.2 就绪检查（Readiness）](docs/stage-04-web/chapter-11-health/section-02-readiness.md)
  - [4.11.3 存活检查（Liveness）](docs/stage-04-web/chapter-11-health/section-03-liveness.md)

### 阶段五：数据持久化与数据库（数据层）

- [阶段五总览](docs/stage-05-database/README.md)
- [5.1 数据库设计基础](docs/stage-05-database/chapter-01-design/README.md)
  - [5.1.1 数据库设计原则](docs/stage-05-database/chapter-01-design/section-01-principles.md)
  - [5.1.2 范式与反范式](docs/stage-05-database/chapter-01-design/section-02-normalization.md)
  - [5.1.3 索引设计](docs/stage-05-database/chapter-01-design/section-03-indexes.md)
- [5.2 关系型数据库（SQL）](docs/stage-05-database/chapter-02-sql/README.md)
  - [5.2.1 关系型数据库概述](docs/stage-05-database/chapter-02-sql/section-01-overview.md)
  - [5.2.2 PostgreSQL（推荐）](docs/stage-05-database/chapter-02-sql/section-02-postgresql.md)
  - [5.2.3 MySQL](docs/stage-05-database/chapter-02-sql/section-03-mysql.md)
  - [5.2.4 SQLite](docs/stage-05-database/chapter-02-sql/section-04-sqlite.md)
- [5.3 ORM 框架概览](docs/stage-05-database/chapter-03-orm/README.md)
  - [5.3.1 ORM 框架概述](docs/stage-05-database/chapter-03-orm/section-01-overview.md)
  - [5.3.2 Prisma 简介](docs/stage-05-database/chapter-03-orm/section-02-prisma.md)
  - [5.3.3 Drizzle ORM 简介](docs/stage-05-database/chapter-03-orm/section-03-drizzle.md)
  - [5.3.4 TypeORM 简介](docs/stage-05-database/chapter-03-orm/section-04-typeorm.md)
  - [5.3.5 Sequelize 简介](docs/stage-05-database/chapter-03-orm/section-05-sequelize.md)
  - [5.3.6 其他 ORM 框架](docs/stage-05-database/chapter-03-orm/section-06-other-orms.md)
- [5.4 数据库迁移](docs/stage-05-database/chapter-04-migrations/README.md)
  - [5.4.1 数据库迁移概述](docs/stage-05-database/chapter-04-migrations/section-01-overview.md)
  - [5.4.2 Prisma Migrate](docs/stage-05-database/chapter-04-migrations/section-02-prisma-migrate.md)
  - [5.4.3 TypeORM Migrations](docs/stage-05-database/chapter-04-migrations/section-03-typeorm-migrations.md)
  - [5.4.4 迁移最佳实践](docs/stage-05-database/chapter-04-migrations/section-04-best-practices.md)
- [5.5 事务处理](docs/stage-05-database/chapter-05-transactions/README.md)
  - [5.5.1 事务处理概述](docs/stage-05-database/chapter-05-transactions/section-01-overview.md)
  - [5.5.2 事务基础](docs/stage-05-database/chapter-05-transactions/section-02-basics.md)
  - [5.5.3 ACID 特性](docs/stage-05-database/chapter-05-transactions/section-03-acid.md)
  - [5.5.4 隔离级别](docs/stage-05-database/chapter-05-transactions/section-04-isolation-levels.md)
- [5.6 NoSQL 数据库](docs/stage-05-database/chapter-06-nosql/README.md)
  - [5.6.1 NoSQL 数据库概述](docs/stage-05-database/chapter-06-nosql/section-01-overview.md)
  - [5.6.2 MongoDB](docs/stage-05-database/chapter-06-nosql/section-02-mongodb.md)
  - [5.6.3 Mongoose ODM](docs/stage-05-database/chapter-06-nosql/section-03-mongoose.md)
- [5.7 Redis 缓存](docs/stage-05-database/chapter-07-redis/README.md)
  - [5.7.1 Redis 缓存概述](docs/stage-05-database/chapter-07-redis/section-01-overview.md)
  - [5.7.2 Redis 基础](docs/stage-05-database/chapter-07-redis/section-02-basics.md)
  - [5.7.3 缓存策略](docs/stage-05-database/chapter-07-redis/section-03-strategies.md)
  - [5.7.4 ioredis 客户端](docs/stage-05-database/chapter-07-redis/section-04-ioredis.md)
- [5.8 消息队列](docs/stage-05-database/chapter-08-queue/README.md)
  - [5.8.1 消息队列概述](docs/stage-05-database/chapter-08-queue/section-01-overview.md)
  - [5.8.2 RabbitMQ](docs/stage-05-database/chapter-08-queue/section-02-rabbitmq.md)
  - [5.8.3 Bull/BullMQ（Redis 队列）](docs/stage-05-database/chapter-08-queue/section-03-bull.md)
  - [5.8.4 任务调度（node-cron、agenda）](docs/stage-05-database/chapter-08-queue/section-04-scheduling.md)

### 阶段六：认证、授权与安全（安全层）

- [阶段六总览](docs/stage-06-security/README.md)
- [6.1 身份认证（Authentication）](docs/stage-06-security/chapter-01-auth/README.md)
  - [6.1.1 身份认证概述](docs/stage-06-security/chapter-01-auth/section-01-overview.md)
  - [6.1.2 Session + Cookie](docs/stage-06-security/chapter-01-auth/section-02-session-cookie.md)
  - [6.1.3 JWT（JSON Web Token）](docs/stage-06-security/chapter-01-auth/section-03-jwt.md)
  - [6.1.4 OAuth 2.0 与 OIDC](docs/stage-06-security/chapter-01-auth/section-04-oauth2.md)
  - [6.1.5 Passport.js](docs/stage-06-security/chapter-01-auth/section-05-passport.md)
- [6.2 授权（Authorization）](docs/stage-06-security/chapter-02-authorization/README.md)
  - [6.2.1 授权概述](docs/stage-06-security/chapter-02-authorization/section-01-overview.md)
  - [6.2.2 RBAC（基于角色的访问控制）](docs/stage-06-security/chapter-02-authorization/section-02-rbac.md)
  - [6.2.3 ABAC（基于属性的访问控制）](docs/stage-06-security/chapter-02-authorization/section-03-abac.md)
  - [6.2.4 权限中间件实现](docs/stage-06-security/chapter-02-authorization/section-04-middleware.md)
- [6.3 Web 安全](docs/stage-06-security/chapter-03-web-security/README.md)
  - [6.3.1 Web 安全概述](docs/stage-06-security/chapter-03-web-security/section-01-overview.md)
  - [6.3.2 OWASP Top 10（2025）](docs/stage-06-security/chapter-03-web-security/section-02-owasp.md)
  - [6.3.3 XSS 防护](docs/stage-06-security/chapter-03-web-security/section-03-xss.md)
  - [6.3.4 CSRF 防护](docs/stage-06-security/chapter-03-web-security/section-04-csrf.md)
  - [6.3.5 SQL 注入防护](docs/stage-06-security/chapter-03-web-security/section-05-sql-injection.md)
  - [6.3.6 Helmet.js 安全头](docs/stage-06-security/chapter-03-web-security/section-06-helmet.md)
- [6.4 数据加密](docs/stage-06-security/chapter-04-encryption/README.md)
  - [6.4.1 数据加密概述](docs/stage-06-security/chapter-04-encryption/section-01-overview.md)
  - [6.4.2 密码加密（bcrypt、argon2）](docs/stage-06-security/chapter-04-encryption/section-02-password.md)
  - [6.4.3 数据加密](docs/stage-06-security/chapter-04-encryption/section-03-data-encryption.md)
  - [6.4.4 HTTPS/TLS](docs/stage-06-security/chapter-04-encryption/section-04-https-tls.md)

### 阶段七：测试与质量保证（质量层）

- [阶段七总览](docs/stage-07-testing/README.md)
- [7.1 测试基础](docs/stage-07-testing/chapter-01-basics/README.md)
  - [7.1.1 测试金字塔](docs/stage-07-testing/chapter-01-basics/section-01-testing-pyramid.md)
  - [7.1.2 测试类型（单元、集成、E2E）](docs/stage-07-testing/chapter-01-basics/section-02-test-types.md)
- [7.2 单元测试](docs/stage-07-testing/chapter-02-unit/README.md)
  - [7.2.1 单元测试概述](docs/stage-07-testing/chapter-02-unit/section-01-overview.md)
  - [7.2.2 Vitest（现代测试框架）](docs/stage-07-testing/chapter-02-unit/section-02-vitest.md)
  - [7.2.3 Jest（传统测试框架）](docs/stage-07-testing/chapter-02-unit/section-03-jest.md)
  - [7.2.4 测试覆盖率](docs/stage-07-testing/chapter-02-unit/section-04-coverage.md)
- [7.3 集成测试](docs/stage-07-testing/chapter-03-integration/README.md)
  - [7.3.1 集成测试概述](docs/stage-07-testing/chapter-03-integration/section-01-overview.md)
  - [7.3.2 API 集成测试](docs/stage-07-testing/chapter-03-integration/section-02-api-tests.md)
  - [7.3.3 数据库集成测试](docs/stage-07-testing/chapter-03-integration/section-03-database-tests.md)
- [7.4 E2E 测试](docs/stage-07-testing/chapter-04-e2e/README.md)
  - [7.4.1 E2E 测试概述](docs/stage-07-testing/chapter-04-e2e/section-01-overview.md)
  - [7.4.2 Playwright](docs/stage-07-testing/chapter-04-e2e/section-02-playwright.md)
  - [7.4.3 Cypress](docs/stage-07-testing/chapter-04-e2e/section-03-cypress.md)
  - [7.4.4 Puppeteer](docs/stage-07-testing/chapter-04-e2e/section-04-puppeteer.md)
- [7.5 Mock 与 Stub](docs/stage-07-testing/chapter-05-mocking/README.md)
  - [7.5.1 Mock 与 Stub 概述](docs/stage-07-testing/chapter-05-mocking/section-01-overview.md)
  - [7.5.2 Mock 基础](docs/stage-07-testing/chapter-05-mocking/section-02-basics.md)
  - [7.5.3 Sinon.js](docs/stage-07-testing/chapter-05-mocking/section-03-sinon.md)
  - [7.5.4 MSW（Mock Service Worker）](docs/stage-07-testing/chapter-05-mocking/section-04-msw.md)

### 阶段八：性能优化与可观测性（性能层）

- [阶段八总览](docs/stage-08-performance/README.md)
- [8.1 性能优化基础](docs/stage-08-performance/chapter-01-basics/README.md)
  - [8.1.1 性能指标](docs/stage-08-performance/chapter-01-basics/section-01-metrics.md)
  - [8.1.2 性能分析工具](docs/stage-08-performance/chapter-01-basics/section-02-profiling.md)
- [8.2 代码优化](docs/stage-08-performance/chapter-02-code/README.md)
  - [8.2.1 代码优化概述](docs/stage-08-performance/chapter-02-code/section-01-overview.md)
  - [8.2.2 算法优化](docs/stage-08-performance/chapter-02-code/section-02-algorithms.md)
  - [8.2.3 内存管理](docs/stage-08-performance/chapter-02-code/section-03-memory.md)
  - [8.2.4 异步优化](docs/stage-08-performance/chapter-02-code/section-04-async.md)
- [8.3 数据库优化](docs/stage-08-performance/chapter-03-database/README.md)
  - [8.3.1 数据库优化概述](docs/stage-08-performance/chapter-03-database/section-01-overview.md)
  - [8.3.2 查询优化](docs/stage-08-performance/chapter-03-database/section-02-query.md)
  - [8.3.3 索引优化](docs/stage-08-performance/chapter-03-database/section-03-indexes.md)
  - [8.3.4 连接池优化](docs/stage-08-performance/chapter-03-database/section-04-connection-pool.md)
- [8.4 缓存策略](docs/stage-08-performance/chapter-04-caching/README.md)
  - [8.4.1 缓存策略概述](docs/stage-08-performance/chapter-04-caching/section-01-overview.md)
  - [8.4.2 缓存模式（Cache-Aside、Write-Through）](docs/stage-08-performance/chapter-04-caching/section-02-patterns.md)
  - [8.4.3 Redis 缓存实现](docs/stage-08-performance/chapter-04-caching/section-03-redis.md)
  - [8.4.4 CDN 与静态资源缓存](docs/stage-08-performance/chapter-04-caching/section-04-cdn.md)
- [8.5 可观测性](docs/stage-08-performance/chapter-05-observability/README.md)
  - [8.5.1 可观测性概述](docs/stage-08-performance/chapter-05-observability/section-01-overview.md)
  - [8.5.2 日志系统（Winston、Pino）](docs/stage-08-performance/chapter-05-observability/section-02-logging.md)
  - [8.5.3 日志轮转](docs/stage-08-performance/chapter-05-observability/section-03-log-rotation.md)
  - [8.5.4 指标监控（Prometheus）](docs/stage-08-performance/chapter-05-observability/section-04-metrics.md)
  - [8.5.5 链路追踪（OpenTelemetry）](docs/stage-08-performance/chapter-05-observability/section-05-tracing.md)
  - [8.5.6 错误追踪（Sentry）](docs/stage-08-performance/chapter-05-observability/section-06-error-tracking.md)

### 阶段九：部署与 DevOps（运维层）

- [阶段九总览](docs/stage-09-deployment/README.md)
- [9.1 容器化](docs/stage-09-deployment/chapter-01-containerization/README.md)
  - [9.1.1 容器化概述](docs/stage-09-deployment/chapter-01-containerization/section-01-overview.md)
  - [9.1.2 Docker 基础](docs/stage-09-deployment/chapter-01-containerization/section-02-docker.md)
  - [9.1.3 Dockerfile 编写](docs/stage-09-deployment/chapter-01-containerization/section-03-dockerfile.md)
  - [9.1.4 Docker Compose](docs/stage-09-deployment/chapter-01-containerization/section-04-docker-compose.md)
- [9.2 CI/CD](docs/stage-09-deployment/chapter-02-cicd/README.md)
  - [9.2.1 CI/CD 概述](docs/stage-09-deployment/chapter-02-cicd/section-01-overview.md)
  - [9.2.2 GitHub Actions](docs/stage-09-deployment/chapter-02-cicd/section-02-github-actions.md)
  - [9.2.3 GitLab CI](docs/stage-09-deployment/chapter-02-cicd/section-03-gitlab-ci.md)
  - [9.2.4 自动化测试与部署](docs/stage-09-deployment/chapter-02-cicd/section-04-automation.md)
- [9.3 部署平台](docs/stage-09-deployment/chapter-03-platforms/README.md)
  - [9.3.1 部署平台概述](docs/stage-09-deployment/chapter-03-platforms/section-01-overview.md)
  - [9.3.2 PaaS（Vercel、Railway、Render）](docs/stage-09-deployment/chapter-03-platforms/section-02-paas.md)
  - [9.3.3 Serverless（AWS Lambda、Cloudflare Workers）](docs/stage-09-deployment/chapter-03-platforms/section-03-serverless.md)
  - [9.3.4 IaaS（AWS EC2、DigitalOcean）](docs/stage-09-deployment/chapter-03-platforms/section-04-iaas.md)
- [9.4 进程管理](docs/stage-09-deployment/chapter-04-process/README.md)
  - [9.4.1 进程管理概述](docs/stage-09-deployment/chapter-04-process/section-01-overview.md)
  - [9.4.2 PM2](docs/stage-09-deployment/chapter-04-process/section-02-pm2.md)
  - [9.4.3 systemd](docs/stage-09-deployment/chapter-04-process/section-03-systemd.md)
- [9.5 监控与告警](docs/stage-09-deployment/chapter-05-monitoring/README.md)
  - [9.5.1 监控与告警概述](docs/stage-09-deployment/chapter-05-monitoring/section-01-overview.md)
  - [9.5.2 应用监控](docs/stage-09-deployment/chapter-05-monitoring/section-02-application.md)
  - [9.5.3 基础设施监控](docs/stage-09-deployment/chapter-05-monitoring/section-03-infrastructure.md)
  - [9.5.4 告警系统](docs/stage-09-deployment/chapter-05-monitoring/section-04-alerts.md)
- [9.6 API 网关](docs/stage-09-deployment/chapter-06-api-gateway/README.md)
  - [9.6.1 API 网关概述](docs/stage-09-deployment/chapter-06-api-gateway/section-01-overview.md)
  - [9.6.2 Kong](docs/stage-09-deployment/chapter-06-api-gateway/section-02-kong.md)
  - [9.6.3 Traefik](docs/stage-09-deployment/chapter-06-api-gateway/section-03-traefik.md)

### 阶段十：现代运行时与新兴技术（前沿）

- [阶段十总览](docs/stage-10-modern/README.md)
- [10.1 Deno](docs/stage-10-modern/chapter-01-deno/README.md)
  - [10.1.1 Deno 概述](docs/stage-10-modern/chapter-01-deno/section-01-overview.md)
  - [10.1.2 Deno 基础](docs/stage-10-modern/chapter-01-deno/section-02-basics.md)
  - [10.1.3 Deno 与 Node.js 对比](docs/stage-10-modern/chapter-01-deno/section-03-comparison.md)
- [10.2 Bun](docs/stage-10-modern/chapter-02-bun/README.md)
  - [10.2.1 Bun 概述](docs/stage-10-modern/chapter-02-bun/section-01-overview.md)
  - [10.2.2 Bun 基础](docs/stage-10-modern/chapter-02-bun/section-02-basics.md)
  - [10.2.3 Bun 运行时特性](docs/stage-10-modern/chapter-02-bun/section-03-features.md)
- [10.3 边缘计算](docs/stage-10-modern/chapter-03-edge/README.md)
  - [10.3.1 边缘计算概述](docs/stage-10-modern/chapter-03-edge/section-01-overview.md)
  - [10.3.2 Cloudflare Workers](docs/stage-10-modern/chapter-03-edge/section-02-cloudflare.md)
  - [10.3.3 Vercel Edge Functions](docs/stage-10-modern/chapter-03-edge/section-03-vercel.md)
  - [10.3.4 Hono 边缘部署](docs/stage-10-modern/chapter-03-edge/section-04-hono-edge.md)

---

## 学习路径建议

### 初学者路径

1. **阶段一**：搭建 Node.js 和 TypeScript 环境
2. **阶段二**：掌握核心模块与基础 API
3. **阶段三**：学习包管理与工具链
4. **阶段四**：学习 Web 框架与 API 开发（了解框架生态）
5. **阶段五**：掌握数据持久化与数据库
6. **阶段六**：学习认证、授权与安全
7. **阶段七**：掌握测试与质量保证
8. **阶段八**：学习性能优化与可观测性
9. **阶段九**：掌握部署与 DevOps
10. **阶段十**：了解现代运行时与新兴技术

### 有经验开发者路径

- 可直接跳转到感兴趣的阶段
- 建议重点学习阶段四（Web 框架）、阶段六（安全）、阶段八（性能优化）、阶段九（部署）

---

## 文档特点

- **面向有 JS/TS 基础的开发者**：假设已掌握 JavaScript 和 TypeScript 基础
- **TypeScript First**：所有代码示例优先使用 TypeScript 编写
- **内容详实**：提供完整的语法、参数说明和使用示例
- **示例丰富**：每个知识点都配有完整的代码示例
- **实践导向**：每章都包含练习任务，帮助巩固学习
- **结构清晰**：按阶段、章节、小节分层组织，便于查阅
- **技术前沿**：反映 2025 年最新的 Node.js 技术和工具生态
- **全栈覆盖**：涵盖后端开发、数据库、安全、测试、部署等全栈技能

---

## 版本信息

- **版本**：2025.1
- **创建日期**：2025-12-11
- **适用 Node.js 版本**：Node.js 22+
- **代码语言**：TypeScript（优先）
- **最后更新**：2025-12-11
