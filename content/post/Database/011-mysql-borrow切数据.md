---
title: "01--mysql-borrow切数据"
author: "lucas"
date: 2026-03-11
lastmod: 2026-03-11

tags: ["Mysql"]
categories: ["DataBase"]
keywords: ["Mysql", "borrow"]
---

<div align="center"><font size="35">-mysql-borrow切数据</font></div>


# 1: mysql-borrow切数据
```bash
-- 1. borrow_2026表
CREATE TABLE borrow_2026 LIKE borrow;
INSERT INTO borrow_2026
SELECT * FROM  borrow where tradeDate >= '2026-01-01' ;

-- 2. 创建历史表borrow_2025, 并把历史数据insert,数据太多可以分批插入
CREATE TABLE borrow_2025 LIKE borrow;
INSERT INTO borrow_2025 SELECT * FROM  borrow where tradeDate >= '2025-01-01' and tradeDate < '2025-04-01'; // Q1
INSERT INTO borrow_2025 SELECT * FROM  borrow where tradeDate >= '2025-04-01' and tradeDate < '2025-07-01'; // Q2
INSERT INTO borrow_2025 SELECT * FROM  borrow where tradeDate >= '2025-07-01' and tradeDate < '2025-10-01'; // Q3
INSERT INTO borrow_2025 SELECT * FROM  borrow where tradeDate >= '2025-10-01' and tradeDate < '2026-01-01'; // Q4

-- 3. rename backupdate borrow表
RENAME TABLE borrow TO borrow_2025_backup ;

-- 4. rename borrow_2026表 -> borrow新表
RENAME TABLE borrow_2026 TO borrow;

-- 5. 核对数据

```
