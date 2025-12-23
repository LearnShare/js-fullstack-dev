# 4.2.4 NestJS 简介

## 1. 概述

NestJS 是一个用于构建高效、可扩展的 Node.js 服务器端应用的框架。NestJS 采用模块化架构，基于 TypeScript，借鉴了 Angular 的设计理念，提供了依赖注入、装饰器、模块系统等企业级特性。NestJS 适合构建大型、复杂的应用程序。

## 2. 特性说明

- **模块化架构**：基于模块的架构设计，便于组织代码
- **依赖注入**：强大的依赖注入系统
- **TypeScript 优先**：原生支持 TypeScript，提供完整的类型安全
- **装饰器支持**：使用装饰器简化代码
- **企业级特性**：提供完整的架构和最佳实践
- **丰富的生态**：支持多种数据库、消息队列、缓存等

## 3. 安装与初始化

### 3.1 安装 CLI

```bash
npm install -g @nestjs/cli
```

### 3.2 创建项目

```bash
nest new my-project
```

### 3.3 基本结构

```
src/
├── app.module.ts      # 根模块
├── app.controller.ts  # 控制器
├── app.service.ts     # 服务
└── main.ts            # 入口文件
```

## 4. 核心概念

### 4.1 模块（Module）

模块是 NestJS 的基本组织单位：

```ts
// app.module.ts
import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';

@Module({
  imports: [],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
```

### 4.2 控制器（Controller）

控制器处理 HTTP 请求：

```ts
// app.controller.ts
import { Controller, Get, Post, Body, Param } from '@nestjs/common';
import { AppService } from './app.service';

@Controller('users')
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  findAll() {
    return this.appService.findAll();
  }

  @Get(':id')
  findOne(@Param('id') id: string) {
    return this.appService.findOne(id);
  }

  @Post()
  create(@Body() createUserDto: CreateUserDto) {
    return this.appService.create(createUserDto);
  }
}
```

### 4.3 服务（Service）

服务包含业务逻辑：

```ts
// app.service.ts
import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  findAll() {
    return { users: [] };
  }

  findOne(id: string) {
    return { id, name: 'John' };
  }

  create(createUserDto: CreateUserDto) {
    return { id: 1, ...createUserDto };
  }
}
```

### 4.4 DTO（Data Transfer Object）

DTO 用于数据传输和验证：

```ts
// dto/create-user.dto.ts
import { IsString, IsEmail, MinLength } from 'class-validator';

export class CreateUserDto {
  @IsString()
  @MinLength(1)
  name: string;

  @IsEmail()
  email: string;
}
```

## 5. 依赖注入

### 5.1 基本使用

```ts
@Injectable()
export class UserService {
  findAll() {
    return { users: [] };
  }
}

@Controller('users')
export class UserController {
  constructor(private readonly userService: UserService) {}

  @Get()
  findAll() {
    return this.userService.findAll();
  }
}
```

### 5.2 模块注入

```ts
@Module({
  imports: [HttpModule],
  controllers: [UserController],
  providers: [UserService],
})
export class UserModule {}
```

## 6. 中间件

### 6.1 类中间件

```ts
// middleware/logger.middleware.ts
import { Injectable, NestMiddleware } from '@nestjs/common';
import { Request, Response, NextFunction } from 'express';

@Injectable()
export class LoggerMiddleware implements NestMiddleware {
  use(req: Request, res: Response, next: NextFunction) {
    console.log(`${req.method} ${req.url}`);
    next();
  }
}
```

### 6.2 使用中间件

```ts
export class AppModule implements NestModule {
  configure(consumer: MiddlewareConsumer) {
    consumer
      .apply(LoggerMiddleware)
      .forRoutes('*');
  }
}
```

## 7. 守卫（Guards）

守卫用于实现认证和授权：

```ts
// guards/auth.guard.ts
import { Injectable, CanActivate, ExecutionContext } from '@nestjs/common';

@Injectable()
export class AuthGuard implements CanActivate {
  canActivate(context: ExecutionContext): boolean {
    const request = context.switchToHttp().getRequest();
    const token = request.headers.authorization;
    return !!token;
  }
}
```

### 7.1 使用守卫

```ts
@Controller('users')
@UseGuards(AuthGuard)
export class UserController {
  // ...
}
```

## 8. 拦截器（Interceptors）

拦截器用于在请求处理前后执行逻辑：

```ts
// interceptors/logging.interceptor.ts
import { Injectable, NestInterceptor, ExecutionContext, CallHandler } from '@nestjs/common';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';

@Injectable()
export class LoggingInterceptor implements NestInterceptor {
  intercept(context: ExecutionContext, next: CallHandler): Observable<any> {
    const now = Date.now();
    return next
      .handle()
      .pipe(
        tap(() => console.log(`After... ${Date.now() - now}ms`))
      );
  }
}
```

## 9. 管道（Pipes）

管道用于数据转换和验证：

```ts
// pipes/validation.pipe.ts
import { PipeTransform, Injectable, ArgumentMetadata, BadRequestException } from '@nestjs/common';
import { validate } from 'class-validator';
import { plainToInstance } from 'class-transformer';

@Injectable()
export class ValidationPipe implements PipeTransform<any> {
  async transform(value: any, { metatype }: ArgumentMetadata) {
    if (!metatype || !this.toValidate(metatype)) {
      return value;
    }
    const object = plainToInstance(metatype, value);
    const errors = await validate(object);
    if (errors.length > 0) {
      throw new BadRequestException('Validation failed');
    }
    return value;
  }

  private toValidate(metatype: Function): boolean {
    const types: Function[] = [String, Boolean, Number, Array, Object];
    return !types.includes(metatype);
  }
}
```

## 10. 完整示例

```ts
// main.ts
import { NestFactory } from '@nestjs/core';
import { ValidationPipe } from '@nestjs/common';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  
  app.useGlobalPipes(new ValidationPipe());
  app.enableCors();
  
  await app.listen(3000);
  console.log('Server running on http://localhost:3000');
}

bootstrap();

// users.module.ts
import { Module } from '@nestjs/common';
import { UsersController } from './users.controller';
import { UsersService } from './users.service';

@Module({
  controllers: [UsersController],
  providers: [UsersService],
})
export class UsersModule {}

// users.controller.ts
import { Controller, Get, Post, Body, Param, UseGuards } from '@nestjs/common';
import { UsersService } from './users.service';
import { CreateUserDto } from './dto/create-user.dto';
import { AuthGuard } from '../guards/auth.guard';

@Controller('users')
@UseGuards(AuthGuard)
export class UsersController {
  constructor(private readonly usersService: UsersService) {}

  @Get()
  findAll() {
    return this.usersService.findAll();
  }

  @Get(':id')
  findOne(@Param('id') id: string) {
    return this.usersService.findOne(id);
  }

  @Post()
  create(@Body() createUserDto: CreateUserDto) {
    return this.usersService.create(createUserDto);
  }
}

// users.service.ts
import { Injectable } from '@nestjs/common';
import { CreateUserDto } from './dto/create-user.dto';

@Injectable()
export class UsersService {
  private users = [];

  findAll() {
    return { data: this.users };
  }

  findOne(id: string) {
    return this.users.find(user => user.id === id);
  }

  create(createUserDto: CreateUserDto) {
    const user = { id: Date.now(), ...createUserDto };
    this.users.push(user);
    return user;
  }
}
```

## 11. 最佳实践

### 11.1 项目结构

```
src/
├── modules/
│   ├── users/
│   │   ├── users.module.ts
│   │   ├── users.controller.ts
│   │   ├── users.service.ts
│   │   └── dto/
│   │       └── create-user.dto.ts
│   └── posts/
├── common/
│   ├── guards/
│   ├── interceptors/
│   ├── pipes/
│   └── filters/
└── main.ts
```

### 11.2 代码组织

- **模块化**：按功能组织模块
- **单一职责**：每个类只负责一个功能
- **依赖注入**：充分利用依赖注入
- **类型安全**：充分利用 TypeScript 类型系统

## 12. 注意事项

- **学习曲线**：NestJS 学习曲线较陡，需要理解其架构理念
- **性能考虑**：相比轻量框架，NestJS 有一定开销
- **项目规模**：适合大型、复杂的应用程序
- **团队协作**：需要团队熟悉 NestJS 的架构模式

## 13. 常见问题

### 13.1 如何处理异步操作？

使用 async/await：

```ts
@Get()
async findAll() {
  const users = await this.usersService.findAll();
  return { data: users };
}
```

### 13.2 如何实现文件上传？

使用 `@nestjs/platform-express` 和 `multer`：

```ts
import { UseInterceptors, UploadedFile } from '@nestjs/common';
import { FileInterceptor } from '@nestjs/platform-express';

@Post('upload')
@UseInterceptors(FileInterceptor('file'))
uploadFile(@UploadedFile() file: Express.Multer.File) {
  return { filename: file.filename };
}
```

---

**下一节**：[4.2.5 Hono 简介](section-05-hono.md)
