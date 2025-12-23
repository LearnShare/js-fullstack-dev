# 4.12.4 class-validator

## 1. 概述

class-validator 是一个基于装饰器的数据验证库，使用装饰器定义验证规则。class-validator 与 NestJS 集成良好，适合使用类定义数据结构的项目。

## 2. 特性说明

- **装饰器语法**：使用装饰器定义验证规则
- **类验证**：基于类的验证
- **NestJS 集成**：与 NestJS 良好集成
- **TypeScript 支持**：原生支持 TypeScript

## 3. 安装与初始化

### 3.1 安装

```bash
npm install class-validator class-transformer
```

### 3.2 基本使用

```ts
import { IsString, IsEmail, IsInt, Min, Max, IsOptional } from 'class-validator';

class CreateUserDto {
  @IsString()
  @MinLength(1)
  name!: string;

  @IsEmail()
  email!: string;

  @IsInt()
  @Min(0)
  @Max(150)
  @IsOptional()
  age?: number;
}

import { validate } from 'class-validator';
import { plainToInstance } from 'class-transformer';

const data = { name: 'John', email: 'john@example.com', age: 30 };
const dto = plainToInstance(CreateUserDto, data);
const errors = await validate(dto);
```

## 4. 装饰器验证

### 4.1 字符串验证

```ts
import { IsString, MinLength, MaxLength, Matches } from 'class-validator';

class UserDto {
  @IsString()
  @MinLength(1)
  @MaxLength(100)
  name!: string;

  @IsString()
  @Matches(/^[A-Z]/, { message: 'Must start with uppercase' })
  firstName!: string;
}
```

### 4.2 数字验证

```ts
import { IsNumber, IsInt, Min, Max } from 'class-validator';

class UserDto {
  @IsNumber()
  @Min(0)
  @Max(100)
  score!: number;

  @IsInt()
  @Min(0)
  @Max(150)
  age!: number;
}
```

### 4.3 邮箱和 URL 验证

```ts
import { IsEmail, IsUrl } from 'class-validator';

class UserDto {
  @IsEmail()
  email!: string;

  @IsUrl()
  website!: string;
}
```

## 5. 对象验证

### 5.1 嵌套对象

```ts
import { ValidateNested, IsString } from 'class-validator';
import { Type } from 'class-transformer';

class AddressDto {
  @IsString()
  street!: string;

  @IsString()
  city!: string;

  @IsString()
  zipCode!: string;
}

class UserDto {
  @IsString()
  name!: string;

  @ValidateNested()
  @Type(() => AddressDto)
  address!: AddressDto;
}
```

### 5.2 数组验证

```ts
import { IsArray, ArrayMinSize, ArrayMaxSize, ValidateNested } from 'class-validator';
import { Type } from 'class-transformer';

class TagDto {
  @IsString()
  name!: string;
}

class PostDto {
  @IsString()
  title!: string;

  @IsArray()
  @ArrayMinSize(1)
  @ArrayMaxSize(10)
  @ValidateNested({ each: true })
  @Type(() => TagDto)
  tags!: TagDto[];
}
```

## 6. 条件验证

### 6.1 自定义验证

```ts
import { ValidatorConstraint, ValidatorConstraintInterface, ValidationArguments } from 'class-validator';

@ValidatorConstraint({ name: 'isStrongPassword', async: false })
class IsStrongPasswordConstraint implements ValidatorConstraintInterface {
  validate(password: string, args: ValidationArguments): boolean {
    return /[A-Z]/.test(password) && /[a-z]/.test(password) && /[0-9]/.test(password);
  }

  defaultMessage(args: ValidationArguments): string {
    return 'Password must contain uppercase, lowercase, and number';
  }
}

function IsStrongPassword(validationOptions?: ValidationOptions) {
  return function (object: Object, propertyName: string): void {
    registerDecorator({
      target: object.constructor,
      propertyName: propertyName,
      options: validationOptions,
      constraints: [],
      validator: IsStrongPasswordConstraint
    });
  };
}

class UserDto {
  @IsString()
  @IsStrongPassword()
  password!: string;
}
```

## 7. 与 Express 集成

### 7.1 验证中间件

```ts
import { Request, Response, NextFunction } from 'express';
import { validate, ValidationError } from 'class-validator';
import { plainToInstance } from 'class-transformer';

function validateBody(dtoClass: new () => object) {
  return async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    const dto = plainToInstance(dtoClass, req.body);
    const errors: ValidationError[] = await validate(dto);
    
    if (errors.length > 0) {
      const errorMessages = errors.map((error: ValidationError) => ({
        property: error.property,
        constraints: error.constraints
      }));
      
      return res.status(400).json({
        error: 'Validation failed',
        details: errorMessages
      });
    }
    
    req.body = dto;
    next();
  };
}

app.post('/api/users', validateBody(CreateUserDto), (req: Request, res: Response): void => {
  res.json({ message: 'User created' });
});
```

## 8. 与 NestJS 集成

### 8.1 DTO 定义

```ts
// dto/create-user.dto.ts
import { IsString, IsEmail, MinLength } from 'class-validator';

export class CreateUserDto {
  @IsString()
  @MinLength(1)
  name!: string;

  @IsEmail()
  email!: string;
}
```

### 8.2 控制器使用

```ts
// controllers/users.controller.ts
import { Controller, Post, Body } from '@nestjs/common';
import { CreateUserDto } from '../dto/create-user.dto';

@Controller('users')
export class UsersController {
  @Post()
  create(@Body() createUserDto: CreateUserDto): { message: string } {
    // createUserDto 已经验证
    return { message: 'User created' };
  }
}
```

## 9. 最佳实践

### 9.1 DTO 设计

- 为每个端点创建 DTO
- 使用清晰的命名
- 提供验证规则

### 9.2 错误处理

- 提供清晰的错误信息
- 使用自定义消息
- 记录验证失败

### 9.3 性能优化

- 缓存验证元数据
- 优化验证逻辑
- 使用 ValidationPipe

## 10. 注意事项

- **装饰器顺序**：注意装饰器的执行顺序
- **类型转换**：使用 class-transformer 转换类型
- **性能**：注意验证的性能影响
- **可维护性**：保持 DTO 清晰

## 11. 常见问题

### 11.1 如何处理嵌套对象？

使用 `@ValidateNested()` 和 `@Type()` 装饰器。

### 11.2 如何实现自定义验证？

创建自定义验证器类和使用 `registerDecorator`。

### 11.3 如何处理类型转换？

使用 `plainToInstance` 转换普通对象为类实例。

## 12. 实践任务

1. **定义 DTO**：定义用户、文章等数据的 DTO
2. **实现验证中间件**：实现请求体验证中间件
3. **实现自定义验证**：实现自定义验证装饰器
4. **实现错误处理**：实现验证错误处理
5. **优化验证性能**：优化验证逻辑和性能

---

**下一章**：[4.13 错误处理最佳实践](../chapter-13-error-handling/readme.md)
