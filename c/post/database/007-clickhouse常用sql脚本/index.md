
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
DROP  database tick ON CLUSTER <集群名>

-- 显示数据库中的所有表
show tables FROM tick ON CLUSTER <集群名>

-- 手动optimize，合并分区
optimize table tick final;
```

## 3.2 表操作

### 3.2.1 查看表结构

```sql
-- 建表
create table IF NOT EXISTS test.user ON CLUSTER <集群名> (
    `uid` Int32,
    `name` String,
    `age` UInt32,
    `birthday` Date
)ENGINE = MergeTree()
PARTITION BY  (`birthday`)
ORDER BY (uid,birthday);

-- 设置表TTL
--    涉及判断的字段必须是Date或者Datetime类型，推荐使用分区的日期字段：
--      SECOND , MINUTE , HOUR , DAY , WEEK , MONTH , QUARTER , YEAR
Alter table test.user Modify TTL createAt+interval 1 day;


-- 显示表结构
DESCRIBE TABLE test.user;

-- 显示建表语句
SHOW CREATE TABLE test.user;

-- 删除表
DROP table IF EXISTS test.student;

-- 添加字段
alter table product_test add column `test` String DEFAULT '' COMMENT '注释';

--删除字段
alter table product_test drop column `test`;

--修改字段
alter table product_test modify column `test` Nullable(String) DEFAULT NULL COMMENT '注释';

--删除数据
ALTER TABLE db_name.table_name DROP PARTITION '分区(例如：时间20220516)'

-- 删除表中所有数据(清空表)
alter table tableName delete where 1=1;
```

# 四: View 视图

```sql
--ClickHouse支持视图功能，目前一共支持两种视图：普通（Normal）视图和物化（Materialized）视图
--通过DROP TABLE [$db_name.]$view_table_name语句可以直接删除视图，而通过SHOW TABLES可以展示所有的表，视图也会被认为是一种特殊的表一并进行展示

--普通视图
--普通视图不会存储任何数据，它只是一个查询映射，起到了简化查询语义的作用，对查询的性能也不会有任何正负作用


--物化视图
--物化视图支持定义表引擎，因为其数据保存的形式由表引擎决定
--需要定义表引擎，决定数据存储的形式
--物化视图中的数据不支持同步删除，如果源表的数据不存在或者源表被删除了，物化视图的数据依然存在
--物化视图不会随着基础表的变化而变化，所以它也称为快照（snapshot）
--如果要更新数据的话，需要用户手动进行，如周期性执行SQL，或利用触发器等机制
```

# 五: ClickHouse-client

```go
//
clickhouse-client --host localhost --user admin --password admin

// 导出数据
clickhouse-client --query "select * from t_order_mt where create_time='2020-06-01 12:00:00'" --format CSVWithNames> /opt/module/data/rs1.csv

```

# 六: clickhouse-local
