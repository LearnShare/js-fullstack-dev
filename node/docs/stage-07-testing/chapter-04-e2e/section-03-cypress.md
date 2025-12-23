# 7.4.3 Cypress

## 1. 概述

Cypress 是一个现代化的 E2E 测试框架，提供了开发者友好的 API、实时预览、时间旅行等特性。Cypress 适合前端应用的 E2E 测试。

## 2. 特性说明

- **开发者友好**：简洁的 API
- **实时预览**：实时查看测试执行
- **时间旅行**：查看测试历史状态
- **强大调试**：强大的调试功能

## 3. 安装与配置

### 3.1 安装

```bash
npm install -D cypress
```

### 3.2 配置文件

```ts
// cypress.config.ts
import { defineConfig } from 'cypress';

export default defineConfig({
  e2e: {
    baseUrl: 'http://localhost:3000',
    setupNodeEvents(on, config) {
      // 配置插件
    },
    specPattern: 'cypress/e2e/**/*.cy.{js,jsx,ts,tsx}',
    supportFile: 'cypress/support/e2e.ts'
  },
  component: {
    devServer: {
      framework: 'react',
      bundler: 'vite'
    }
  }
});
```

### 3.3 package.json

```json
{
  "scripts": {
    "cypress:open": "cypress open",
    "cypress:run": "cypress run",
    "cypress:headless": "cypress run --headless"
  }
}
```

## 4. 基本使用

### 4.1 测试文件

```ts
// cypress/e2e/login.cy.ts
describe('Login', () => {
  beforeEach(() => {
    cy.visit('/login');
  });
  
  it('should login successfully', () => {
    cy.get('#email').type('user@example.com');
    cy.get('#password').type('password123');
    cy.get('#login-button').click();
    
    cy.url().should('include', '/dashboard');
    cy.get('h1').should('contain', 'Dashboard');
  });
  
  it('should show error for invalid credentials', () => {
    cy.get('#email').type('user@example.com');
    cy.get('#password').type('wrongpassword');
    cy.get('#login-button').click();
    
    cy.get('.error-message').should('be.visible');
    cy.get('.error-message').should('contain', 'Invalid credentials');
  });
});
```

### 4.2 运行测试

```bash
# 打开 Cypress UI
npm run cypress:open

# 无头模式运行
npm run cypress:run

# 运行特定测试
npx cypress run --spec "cypress/e2e/login.cy.ts"
```

## 5. 高级特性

### 5.1 自定义命令

```ts
// cypress/support/commands.ts
declare global {
  namespace Cypress {
    interface Chainable {
      login(email: string, password: string): Chainable<void>;
      logout(): Chainable<void>;
    }
  }
}

Cypress.Commands.add('login', (email: string, password: string): void => {
  cy.visit('/login');
  cy.get('#email').type(email);
  cy.get('#password').type(password);
  cy.get('#login-button').click();
});

Cypress.Commands.add('logout', (): void => {
  cy.get('#user-menu').click();
  cy.get('#logout-button').click();
});

// 使用
cy.login('user@example.com', 'password123');
cy.logout();
```

### 5.2 拦截请求

```ts
describe('API Tests', () => {
  it('should intercept API request', () => {
    cy.intercept('GET', '/api/users', { fixture: 'users.json' }).as('getUsers');
    
    cy.visit('/users');
    cy.wait('@getUsers');
    
    cy.get('.user-list').should('have.length', 3);
  });
});
```

### 5.3 组件测试

```ts
// cypress/component/Button.cy.tsx
import Button from './Button';

describe('Button', () => {
  it('should render button', () => {
    cy.mount(<Button>Click me</Button>);
    cy.get('button').should('contain', 'Click me');
  });
  
  it('should handle click', () => {
    const onClick = cy.stub();
    cy.mount(<Button onClick={onClick}>Click me</Button>);
    cy.get('button').click();
    cy.wrap(onClick).should('have.been.called');
  });
});
```

## 6. 最佳实践

### 6.1 测试组织

- 使用自定义命令
- 保持测试独立
- 使用描述性名称
- 组织测试结构

### 6.2 稳定性

- 使用等待机制
- 避免硬编码等待
- 处理异步操作
- 使用重试机制

## 7. 注意事项

- **等待机制**：Cypress 自动等待，但需注意异步操作
- **测试速度**：优化测试执行速度
- **浏览器支持**：主要支持 Chromium
- **测试维护**：及时维护测试代码

## 8. 常见问题

### 8.1 如何处理异步操作？

Cypress 自动等待 DOM 操作，但需要手动处理网络请求。

### 8.2 如何调试测试？

使用 Cypress UI 的实时预览和时间旅行功能。

### 8.3 如何优化测试速度？

并行执行、使用无头模式、优化等待机制。

## 9. 实践任务

1. **安装配置**：安装和配置 Cypress
2. **编写测试**：编写 E2E 测试
3. **自定义命令**：创建自定义命令
4. **拦截请求**：使用请求拦截
5. **组件测试**：进行组件测试

---

**下一节**：[7.4.4 Puppeteer](section-04-puppeteer.md)
