# 9.5.4 告警系统

## 1. 概述

告警系统是监控系统的重要组成部分，通过及时通知异常情况，可以帮助团队快速响应问题、减少故障时间。有效的告警系统应该避免告警疲劳、提供清晰的告警信息。

## 2. 告警规则

### 2.1 阈值告警

```ts
class AlertManager {
  private rules: AlertRule[] = [];
  
  addRule(rule: AlertRule): void {
    this.rules.push(rule);
  }
  
  async check(metrics: Record<string, number>): Promise<void> {
    for (const rule of this.rules) {
      const value = metrics[rule.metric];
      if (value !== undefined && this.evaluateRule(rule, value)) {
        await this.triggerAlert(rule, value);
      }
    }
  }
  
  private evaluateRule(rule: AlertRule, value: number): boolean {
    switch (rule.operator) {
      case 'gt':
        return value > rule.threshold;
      case 'lt':
        return value < rule.threshold;
      case 'eq':
        return value === rule.threshold;
      default:
        return false;
    }
  }
  
  private async triggerAlert(rule: AlertRule, value: number): Promise<void> {
    const message = `Alert: ${rule.metric} = ${value} (threshold: ${rule.threshold})`;
    await this.sendNotification(rule.channels, message);
  }
  
  private async sendNotification(channels: string[], message: string): Promise<void> {
    for (const channel of channels) {
      switch (channel) {
        case 'email':
          await this.sendEmail(message);
          break;
        case 'slack':
          await this.sendSlack(message);
          break;
        case 'sms':
          await this.sendSMS(message);
          break;
      }
    }
  }
}

interface AlertRule {
  metric: string;
  operator: 'gt' | 'lt' | 'eq';
  threshold: number;
  channels: string[];
  severity: 'low' | 'medium' | 'high' | 'critical';
}
```

## 3. 告警渠道

### 3.1 邮件告警

```ts
import nodemailer from 'nodemailer';

async function sendEmailAlert(message: string): Promise<void> {
  const transporter = nodemailer.createTransport({
    host: process.env.SMTP_HOST,
    port: 587,
    secure: false,
    auth: {
      user: process.env.SMTP_USER,
      pass: process.env.SMTP_PASSWORD
    }
  });
  
  await transporter.sendMail({
    from: process.env.SMTP_FROM,
    to: process.env.ALERT_EMAIL,
    subject: 'System Alert',
    text: message
  });
}
```

### 3.2 Slack 告警

```ts
async function sendSlackAlert(message: string): Promise<void> {
  await fetch(process.env.SLACK_WEBHOOK_URL!, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      text: message,
      channel: '#alerts'
    })
  });
}
```

## 4. 告警分级

### 4.1 分级处理

```ts
enum AlertSeverity {
  LOW = 1,
  MEDIUM = 2,
  HIGH = 3,
  CRITICAL = 4
}

class AlertHandler {
  async handle(alert: Alert): Promise<void> {
    switch (alert.severity) {
      case AlertSeverity.CRITICAL:
        await this.handleCritical(alert);
        break;
      case AlertSeverity.HIGH:
        await this.handleHigh(alert);
        break;
      case AlertSeverity.MEDIUM:
        await this.handleMedium(alert);
        break;
      case AlertSeverity.LOW:
        await this.handleLow(alert);
        break;
    }
  }
  
  private async handleCritical(alert: Alert): Promise<void> {
    // 立即通知所有渠道
    await Promise.all([
      this.sendEmail(alert),
      this.sendSlack(alert),
      this.sendSMS(alert),
      this.sendPagerDuty(alert)
    ]);
  }
}
```

## 5. 告警抑制

### 5.1 防止告警风暴

```ts
class AlertThrottler {
  private lastAlert: Map<string, number> = new Map();
  private cooldown: number = 300000; // 5 分钟
  
  shouldAlert(alertId: string): boolean {
    const lastTime = this.lastAlert.get(alertId) || 0;
    const now = Date.now();
    
    if (now - lastTime > this.cooldown) {
      this.lastAlert.set(alertId, now);
      return true;
    }
    
    return false;
  }
}
```

## 6. 最佳实践

### 6.1 告警设计

- 避免告警疲劳
- 设置合理阈值
- 分级告警
- 及时响应

### 6.2 告警管理

- 告警抑制
- 告警聚合
- 告警升级
- 告警分析

## 7. 注意事项

- **告警疲劳**：避免过多告警
- **阈值设置**：设置合理的阈值
- **响应时间**：及时响应告警
- **告警分析**：定期分析告警

## 8. 常见问题

### 8.1 如何处理告警疲劳？

使用告警抑制、告警聚合、优化告警规则。

### 8.2 如何设置告警阈值？

根据历史数据、SLA、业务需求设置。

### 8.3 如何优化告警系统？

分级告警、告警抑制、告警聚合。

## 9. 实践任务

1. **实现告警**：实现告警系统
2. **告警规则**：配置告警规则
3. **告警渠道**：配置告警渠道
4. **告警分级**：实现告警分级
5. **持续优化**：持续优化告警系统

---

**下一章**：[9.6 API 网关](../chapter-06-api-gateway/readme.md)
