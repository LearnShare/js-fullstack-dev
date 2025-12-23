# 9.2.3 GitLab CI

## 1. 概述

GitLab CI 是 GitLab 提供的 CI/CD 平台，通过 `.gitlab-ci.yml` 文件配置自动化流水线。GitLab CI 提供了强大的 CI/CD 功能和灵活的配置方式。

## 2. 基本配置

### 2.1 .gitlab-ci.yml

```yaml
# .gitlab-ci.yml
stages:
  - test
  - build
  - deploy

variables:
  NODE_VERSION: "18"

test:
  stage: test
  image: node:${NODE_VERSION}-alpine
  script:
    - npm ci
    - npm test
    - npm run lint
  only:
    - merge_requests
    - main

build:
  stage: build
  image: node:${NODE_VERSION}-alpine
  script:
    - npm ci
    - npm run build
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
  only:
    - main

deploy:
  stage: deploy
  image: alpine:latest
  script:
    - echo "Deploying to production"
    - # 部署命令
  only:
    - main
  when: manual
```

## 3. 阶段和作业

### 3.1 阶段定义

```yaml
stages:
  - build
  - test
  - deploy
```

### 3.2 作业配置

```yaml
test:
  stage: test
  script:
    - npm test
  artifacts:
    reports:
      junit: junit.xml
    paths:
      - coverage/
    expire_in: 1 week
```

## 4. 环境变量

### 4.1 变量定义

```yaml
variables:
  NODE_ENV: "production"
  DATABASE_URL: "postgresql://user:password@db:5432/mydb"

test:
  variables:
    NODE_ENV: "test"
  script:
    - npm test
```

### 4.2 密钥变量

```yaml
# 在 GitLab 项目设置中配置
# Settings > CI/CD > Variables

deploy:
  script:
    - echo $DEPLOY_KEY
    - echo $API_TOKEN
```

## 5. Docker 集成

### 5.1 Docker 构建

```yaml
build:
  stage: build
  services:
    - docker:dind
  script:
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
```

### 5.2 Docker Compose

```yaml
test:
  services:
    - postgres:15-alpine
    - redis:7-alpine
  variables:
    POSTGRES_DB: test_db
    POSTGRES_USER: test_user
    POSTGRES_PASSWORD: test_password
  script:
    - npm ci
    - npm test
```

## 6. 部署配置

### 6.1 环境部署

```yaml
deploy_staging:
  stage: deploy
  environment:
    name: staging
    url: https://staging.example.com
  script:
    - ./deploy.sh staging
  only:
    - develop

deploy_production:
  stage: deploy
  environment:
    name: production
    url: https://example.com
  script:
    - ./deploy.sh production
  only:
    - main
  when: manual
```

## 7. 最佳实践

### 7.1 流水线设计

- 快速反馈
- 并行执行
- 使用缓存
- 失败快速修复

### 7.2 安全实践

- 使用 CI/CD 变量管理密钥
- 最小权限原则
- 定期更新镜像
- 审查配置

## 8. 注意事项

- **安全性**：保护 CI/CD 变量
- **性能**：优化流水线性能
- **成本**：控制运行时间
- **维护**：定期更新配置

## 9. 常见问题

### 9.1 如何管理环境变量？

使用 CI/CD 变量，按环境分离。

### 9.2 如何优化流水线性能？

使用缓存、并行执行、优化步骤。

### 9.3 如何处理部署失败？

实现自动回滚、健康检查、通知机制。

## 10. 实践任务

1. **配置流水线**：配置 GitLab CI 流水线
2. **实现 CI**：实现持续集成
3. **实现 CD**：实现持续部署
4. **安全加固**：实现安全最佳实践
5. **持续优化**：持续优化流水线

---

**下一节**：[9.2.4 自动化测试与部署](section-04-automation.md)
