
<div align="center"><font size="35">ClickHouse常用sql脚本</font></div>

# 一: ClickHouse 介绍

- ClickHouse 是一个用于联机分析(OLAP)的列式数据库管理系统(DBMS).
- https://clickhouse.com/docs/zh/
- 数据文件路径： /var/lib/clickhouse/
- 日志文件路径：/var/log/clickhouse-server/clickhouse-server.log

# 二: Clickhouse 连接

- https://clickhouse.com/docs/zh/interfaces/third-party/gui

# 三: ClickHouse Database

## 3.1 数据库操作

- ClickHouse 严格区分大小写

```sql
-- 显示所有数据库
SHOW database

-- 显示当前使用的数据库
select currentDatabase();

-- 创建数据库
CREATE database if not exists tick

-- 删除数据库
DROP  database tick

-- 显示数据库中的所有表
show tables FROM tick


```

## 3.2 表操作

### 3.2.1 查看表结构

```sql
-- 建表
create table IF NOT EXISTS test.user(
    `uid` Int32,
    `name` String,
    `age` UInt32,
    `birthday` Date
)ENGINE = MergeTree()
PARTITION BY  (`birthday`)
ORDER BY (uid,birthday);

-- 设置表TTL
Alter table test.user Modify TTL createAt+interval 1 day;

-- 显示表结构
DESCRIBE TABLE test.user;

-- 显示建表语句
SHOW CREATE TABLE test.user;

-- 删除表
DROP table IF EXISTS test.student;
--
--
--


```

# 四: ClickHouse-client

```go
clickhouse-client --host localhost --user admin --password admin
```
