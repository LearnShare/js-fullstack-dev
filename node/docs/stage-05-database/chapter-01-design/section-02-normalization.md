# 5.1.2 范式与反范式

## 1. 概述

数据库范式是数据库设计的重要理论，通过范式化可以减少数据冗余、提高数据一致性。但在某些场景下，适度的反范式化可以提高查询性能。

## 2. 范式理论

### 2.1 第一范式（1NF）

**定义**：每个字段都是原子值，不可再分

**示例**：
```sql
-- 不符合 1NF
CREATE TABLE users (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  address VARCHAR(200)  -- 包含省、市、区
);

-- 符合 1NF
CREATE TABLE users (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  province VARCHAR(50),
  city VARCHAR(50),
  district VARCHAR(50)
);
```

### 2.2 第二范式（2NF）

**定义**：在 1NF 基础上，非主键字段完全依赖于主键

**示例**：
```sql
-- 不符合 2NF
CREATE TABLE orders (
  order_id INT,
  product_id INT,
  product_name VARCHAR(100),  -- 部分依赖于 product_id
  quantity INT,
  PRIMARY KEY (order_id, product_id)
);

-- 符合 2NF
CREATE TABLE orders (
  order_id INT,
  product_id INT,
  quantity INT,
  PRIMARY KEY (order_id, product_id),
  FOREIGN KEY (product_id) REFERENCES products(id)
);

CREATE TABLE products (
  id INT PRIMARY KEY,
  name VARCHAR(100)
);
```

### 2.3 第三范式（3NF）

**定义**：在 2NF 基础上，非主键字段不依赖于其他非主键字段

**示例**：
```sql
-- 不符合 3NF
CREATE TABLE orders (
  id INT PRIMARY KEY,
  customer_id INT,
  customer_name VARCHAR(100),  -- 依赖于 customer_id
  order_date DATE
);

-- 符合 3NF
CREATE TABLE orders (
  id INT PRIMARY KEY,
  customer_id INT,
  order_date DATE,
  FOREIGN KEY (customer_id) REFERENCES customers(id)
);

CREATE TABLE customers (
  id INT PRIMARY KEY,
  name VARCHAR(100)
);
```

## 3. 反范式化

### 3.1 反范式化的原因

- **性能优化**：减少 JOIN 操作
- **查询简化**：简化复杂查询
- **读取优化**：优化读取性能

### 3.2 反范式化策略

**冗余字段**：
```sql
-- 范式化设计
CREATE TABLE orders (
  id INT PRIMARY KEY,
  customer_id INT,
  FOREIGN KEY (customer_id) REFERENCES customers(id)
);

-- 反范式化：添加冗余字段
CREATE TABLE orders (
  id INT PRIMARY KEY,
  customer_id INT,
  customer_name VARCHAR(100),  -- 冗余字段
  FOREIGN KEY (customer_id) REFERENCES customers(id)
);
```

**汇总表**：
```sql
-- 创建汇总表避免实时计算
CREATE TABLE user_stats (
  user_id INT PRIMARY KEY,
  total_orders INT,
  total_amount DECIMAL(10, 2),
  last_order_date DATE
);
```

## 4. 范式化 vs 反范式化

### 4.1 范式化优势

- 减少数据冗余
- 提高数据一致性
- 节省存储空间
- 易于维护

### 4.2 反范式化优势

- 提高查询性能
- 减少 JOIN 操作
- 简化查询逻辑
- 优化读取性能

### 4.3 选择原则

- **读取为主**：适度反范式化
- **写入为主**：保持范式化
- **平衡考虑**：根据业务场景选择

## 5. 最佳实践

### 5.1 设计策略

- 先范式化设计
- 根据性能需求反范式化
- 保持数据一致性
- 定期审查设计

### 5.2 性能优化

- 识别热点查询
- 适度反范式化
- 使用缓存
- 优化索引

## 6. 注意事项

- **数据一致性**：反范式化需要维护数据一致性
- **更新成本**：反范式化增加更新成本
- **存储空间**：反范式化增加存储空间
- **维护复杂度**：反范式化增加维护复杂度

## 7. 常见问题

### 7.1 应该范式化到第几范式？

通常范式化到第三范式，根据性能需求适度反范式化。

### 7.2 何时使用反范式化？

读取频繁、JOIN 操作多、性能要求高的场景。

### 7.3 如何维护反范式化数据？

使用触发器、应用层逻辑或定期同步维护。

## 8. 实践任务

1. **范式化设计**：将数据库设计范式化到第三范式
2. **反范式化优化**：根据性能需求适度反范式化
3. **性能测试**：测试范式化和反范式化的性能差异
4. **数据一致性**：实现反范式化数据的一致性维护
5. **设计审查**：定期审查和优化数据库设计

---

**下一节**：[5.1.3 索引设计](section-03-indexes.md)
