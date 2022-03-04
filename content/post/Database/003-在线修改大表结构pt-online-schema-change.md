---
title: "03-在线修改大表结构pt-online-schema-change"
author: "lucas" # 文章作者
description: "在线更新Mysql大表表结构的工具..."
date: 2021-04-15
lastmod: 2021-04-15

tags: # 文章所属标签
  ["DataBase", "Mysql"]
categories: # 文章所属目录
  ["DataBase"]
keywords: # 文章关键词
  ["DataBase", "Mysql", "tool"]
# prev: ./20210415-02.md # 上一篇博客地址
# next: ./20210415-04.md # 下一篇博客地址
---

- [1: 使用场景 Scenario](#1-使用场景-scenario)
- [2: 在线修改大表的可能影响](#2-在线修改大表的可能影响)
- [3: pt\-online\-schema\-change 介绍](#3-pt-online-schema-change-介绍)
- [4: 解决了什么问题](#4-解决了什么问题)
- [5: pt\-online\-schema\-change 安装](#5-pt-online-schema-change-安装)
- [6: pt\-online\-schema\-change 使用](#6-pt-online-schema-change-使用)
  - [6\.1 参数](#61-参数)
  - [6\.2 为避免每次都要输入一堆参数，写个脚本复用一下，pt\.sh](#62-为避免每次都要输入一堆参数写个脚本复用一下ptsh)
  - [6\.3 添加表字段](#63-添加表字段)
  - [6\.4 修改表字段](#64-修改表字段)
  - [6\.4 添加索引](#64-添加索引)
- [7： Others](#7-others)

# 1: 使用场景 Scenario

在线数据库的维护中，总会涉及到研发修改表结构的情况，修改一些小表影响很小，而修改大表时，往往影响业务的正常运转，如表数据量超过 500W，1000W，甚至过亿时.

# 2: 在线修改大表的可能影响

1. 在线修改大表的表结构执行时间往往不可预估，一般时间较长
2. 由于修改表结构是表级锁，因此在修改表结构时，影响表写入操作
3. 如果长时间的修改表结构，中途修改失败，由于修改表结构是一个事务，因此失败后会还原表结构，在这个过程中表都是锁着不可写入,严重影响业务
4. 修改大表结构容易导致数据库 CPU、IO 等性能消耗，使 MySQL 服务器性能降低
5. 在线修改大表结构容易导致主从延时，从而影响业务读取

# 3: pt-online-schema-change 介绍

pt-online-schema-change 是 percona 公司开发的一个工具，在 percona-toolkit 包里面可以找到这个功能，它可以在线修改表结构

**原理:**

```go
1: 首先它会新建一张一模一样的表，表名一般是\_new 后缀
2: 然后在这个新表执行更改字段操作
3: 然后在原表上加三个触发器，DELETE/UPDATE/INSERT，将原表中要执行的语句也在新表中执行
4: 最后将原表的数据拷贝到新表中，然后替换掉原表
```

# 4: 解决了什么问题

1. 降低 Master/Slave 延时
2. 减少对业务的影响
3. 降低对服务器资源的消耗

# 5: pt-online-schema-change 安装

去官网下载对应的版本，官网下载地址:https://www.percona.com/downloads/percona-toolkit/LATEST/

安装依赖包

```shell
yum install perl-DBI
yum install perl-DBD-MySQL
yum install perl-Time-HiRes
yum install perl-IO-Socket-SSL
```

# 6: pt-online-schema-change 使用

## 6.1 参数

./bin/pt-online-schema-change --help 可以查看参数的使用，我们只是要修改个表结构，只需要知道几个简单的参数就可以了

```shell
--user=        连接mysql的用户名
--password=    连接mysql的密码
--host=        连接mysql的地址
P=3306         连接mysql的端口号
D=             连接mysql的库名
t=             连接mysql的表名
--alter        修改表结构的语句
--execute      执行修改表结构
--charset=utf8 使用utf8编码，避免中文乱码
--no-version-check  不检查版本，在阿里云服务器中一般加入此参数，否则会报错

```

## 6.2 为避免每次都要输入一堆参数，写个脚本复用一下，pt.sh

```shell
#!/bin/bash
table=$1
alter_conment=$2

cnn_host='127.0.0.1'
cnn_user='user'
cnn_pwd='password'
cnn_db='database_name'

echo "$table"
echo "$alter_conment"
/root/percona-toolkit-2.2.19/bin/pt-online-schema-change --charset=utf8 --no-version-check --user=${cnn_user} --password=${cnn_pwd} --host=${cnn_host}  P=3306,D=${cnn_db},t=$table --alter
"${alter_conment}" --execute
```

## 6.3 添加表字段

```sql
-- 如添加表字段 SQL 语句为:
ALTER TABLE tb_test ADD COLUMN column1 tinyint(4) DEFAULT NULL;

-- 那么使用 pt-online-schema-change 则可以这样写:
sh pt.sh tb_test "ADD COLUMN column1 tinyint(4) DEFAULT NULL"
```

## 6.4 修改表字段

```sql
-- 修改表字段sql
ALTER TABLE tb_test CHANGE COLUMN age adress varchar(30);
-- pt-online-schema-change工具:
sh pt.sh tb_test "CHANGE COLUMN age address varchar(30)";
```

## 6.4 添加索引

```sql
-- SQL语句
ALTER TABLE tb_test ADD INDEX idx_address(address);

-- pt-online-schema-change工具:
sh pt.sh tb_test "ADD INDEX idx_address(address)"
```

# 7： Others

1. pt-online-schema-change 工具还有很多其他的参数，可以有很多限制，比如限制 CPU、线程数量、从库状态等等，不过我做过一个超过 6000W 表的结构修改，发现几乎不影响性能，很稳定很流畅的就修改了表结构，所以，对以上常规参数的使用基本能满足业务

2. 一定要在业务低峰期做，这样才能确保万无一失
