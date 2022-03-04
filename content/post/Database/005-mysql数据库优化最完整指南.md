---
title: "01-mysql数据库优化最完整指南"
author: "lucas"
date: 2021-06-11
lastmod: 2021-06-1

tags: ["Mysql"]
categories: ["DataBase"]
keywords: ["Mysql", "sql", "sql优化"]
---

- [阶段一: 数据库表设计](#阶段一-数据库表设计)
- [阶段二: 数据库部署](#阶段二-数据库部署)
- [阶段三: 数据库性能优化](#阶段三-数据库性能优化)
  - [3.1 硬件配置](#31-硬件配置)
  - [3.2 数据库配置优化](#32-数据库配置优化)
  - [3.3 系统内核参数优化](#33-系统内核参数优化)
- [阶段四: SQL 语句优化](#阶段四-sql-语句优化)
- [阶段五: 数据库架构扩展](#阶段五-数据库架构扩展)
  - [5.1 增加 cache 缓存](#51-增加-cache-缓存)
  - [5.2 Master/Slave 复制和读写分离](#52-masterslave-复制和读写分离)
  - [5.3 分库](#53-分库)
  - [5.4 分表](#54-分表)
  - [5.5 分区](#55-分区)
- [阶段六: 数据库维护](#阶段六-数据库维护)
  - [6.1 性能状态关键指标 quota](#61-性能状态关键指标-quota)
    - [6.1.1 QPS](#611-qps)
    - [6.1.2 TPS](#612-tps)
  - [6.2 开启慢查询日志](#62-开启慢查询日志)
  - [6.3 数据库备份](#63-数据库备份)
  - [6.4 数据库修复](#64-数据库修复)
  - [6.5 mysql 服务器性能分析](#65-mysql-服务器性能分析)
- [阶段七: 其他](#阶段七-其他)

# 阶段一: 数据库表设计

- 表结构设计

# 阶段二: 数据库部署

- 主从复制
- 集群
- 主从复制+Keepalived 实现双机热备份

> 主流的 HA 软件有: Keepalived,Heartbeat

# 阶段三: 数据库性能优化

## 3.1 硬件配置

## 3.2 数据库配置优化

MySQL 应用最广泛的有两种存储引擎：一个是 MyISAM，不支持事务处理，读性能处理快，表级别锁。另一个是 InnoDB，支持事务处理（ACID 属性），设计目标是为大数据处理，行级别锁。
表锁：开销小，锁定粒度大，发生死锁概率高，相对并发也低。
行锁：开销大，锁定粒度小，发生死锁概率低，相对并发也高。
为什么会出现表锁和行锁呢？主要为保证数据完整性。举个例子，一个用户在操作一张表，其他用户也想操作这张表，那么就要等第一个用户操作完，其他用户才能操作，表锁和行锁就是这个作用。否则多个用户同时操作一张表，肯定会数据产生冲突或者异常。
根据这些方面看，使用 InnoDB 存储引擎是最好的选择，也是 MySQL5.5+版本默认存储引擎。每个存储引擎相关运行参数比较多，以下列出可能影响数据库性能的参数。
**公共参数默认值:**

```bash
max_connections = 151
# 同时处理最大连接数，建议设置最大连接数是上限连接数的80%左右
sort_buffer_size = 2M
# 查询排序时缓冲区大小，只对order by和group by起作用，建议增大为16M
open_files_limit = 1024
# 打开文件数限制，如果show global status like 'open_files'查看的值等于或者大于open_files_limit值时，程序会无法连接数据库或卡死
```

**MyISAM 参数默认值:**

```bash
key_buffer_size = 16M
# 索引缓存区大小，一般设置物理内存的30-40%
read_buffer_size = 128K
# 读操作缓冲区大小，建议设置16M或32M
query_cache_type = ON
# 打开查询缓存功能
query_cache_limit = 1M
# 查询缓存限制，只有1M以下查询结果才会被缓存，以免结果数据较大把缓存池覆盖
query_cache_size = 16M
# 查看缓冲区大小，用于缓存SELECT查询结果，下一次有同样SELECT查询将直接从缓存池返回结果，可适当成倍增加此值
```

**InnoDB 参数默认值：**

```bash
innodb_buffer_pool_size = 128M
# 索引和数据缓冲区大小，建议设置物理内存的70%左右
innodb_buffer_pool_instances = 1
# 缓冲池实例个数，推荐设置4个或8个
innodb_flush_log_at_trx_commit = 1
# 关键参数，0代表大约每秒写入到日志并同步到磁盘，数据库故障会丢失1秒左右事务数据。1为每执行一条SQL后写入到日志并同步到磁盘，I/O开销大，执行完SQL要等待日志读写，效率低。2代表只把日志写入到系统缓存区，再每秒同步到磁盘，效率很高，如果服务器故障，才会丢失事务数据。对数据安全性要求不是很高的推荐设置2，性能高，修改后效果明显。
innodb_file_per_table = OFF
# 是否共享表空间，5.7+版本默认ON，共享表空间idbdata文件不断增大，影响一定的I/O性能。建议开启独立表空间模式，每个表的索引和数据都存在自己独立的表空间中，可以实现单表在不同数据库中移动。
innodb_log_buffer_size = 8M
# 日志缓冲区大小，由于日志最长每秒钟刷新一次，所以一般不用超过16M
```

## 3.3 系统内核参数优化

```bash
net.ipv4.tcp_fin_timeout = 30
# TIME_WAIT超时时间，默认是60s
net.ipv4.tcp_tw_reuse = 1
# 1表示开启复用，允许TIME_WAIT socket重新用于新的TCP连接，0表示关闭
net.ipv4.tcp_tw_recycle = 1
# 1表示开启TIME_WAIT socket快速回收，0表示关闭
net.ipv4.tcp_max_tw_buckets = 4096
# 系统保持TIME_WAIT socket最大数量，如果超出这个数，系统将随机清除一些TIME_WAIT并打印警告信息
net.ipv4.tcp_max_syn_backlog = 4096
# 进入SYN队列最大长度，加大队列长度可容纳更多的等待连接
在Linux系统中，如果进程打开的文件句柄数量超过系统默认值1024，就会提示“too many files open”信息，所以要调整打开文件句柄限制。
重启永久生效：
# vi /etc/security/limits.conf
* soft nofile 65535
* hard nofile 65535
当前用户立即生效：
# ulimit -SHn 65535
```

# 阶段四: SQL 语句优化

# 阶段五: 数据库架构扩展

- 随着业务量越来越大，单台数据库服务器性能已无法满足业务需求，该考虑增加服务器扩展架构了。主要思想是分解单台数据库负载，突破磁盘 I/O 性能，热数据存放缓存中，降低磁盘 I/O 访问频率。

## 5.1 增加 cache 缓存

![](https://i0.hdslb.com/bfs/album/7de207d35e8684ebf4ed66a38bda44a8d45f670b.png)

```go
1: 本地缓存: 把热数据存储到内存中或者本地文件中，比如bigcache,gcache等
https://www.jianshu.com/p/0ff2e8c61c9c?tdsourcetag=s_pctim_aiomsg


2: 分布式缓存: Redis,Memecached

```

## 5.2 Master/Slave 复制和读写分离

在生产环境中，业务系统通常读多写少，可部署一主多从架构，主数据库负责写操作，并做双机热备，多台从数据库做负载均衡，负责读操作。**主流的负载均衡器：LVS、HAProxy、Nginx**。
怎么来实现读写分离呢？大多数企业是在代码层面实现读写分离，效率高。另一个种方式通过代理程序实现读写分离，企业中应用较少，会增加中间件消耗。主流中间件代理系统有 MyCat、Atlas 等。
在这种 MySQL 主从复制拓扑架构中，分散单台负载，大大提高数据库并发能力。如果一台从服务器能处理 1500 QPS，那么 3 台就能处理 4500 QPS，而且容易横向扩展。
有时，面对大量写操作的应用时，单台写性能达不到业务需求。就可以做双向复制（双主），但有个问题得注意：两台主服务器如果都对外提供读写操作，就可能遇到数据不一致现象，产生这个原因是程序有同时操作两台数据库几率，同时的更新操作会造成两台数据库数据发生冲突或者不一致。
可设置每个表 ID 字段自增唯一：auto_increment_increment 和 auto_increment_offset，也可以写算法生成随机唯一。
官方近两年推出的 MGR（多主复制）集群也可以考虑下。

## 5.3 分库

分库是根据业务将数据库中相关的表分离到不同的数据库中，例如 web、bbs、blog 等库。如果业务量很大，还可将分离后的数据库做主从复制架构，进一步避免单库压力过大。

## 5.4 分表

数据量的日剧增加，数据库中某个表有几百万条数据，导致查询和插入耗时太长，怎么能解决单表压力呢？你应该考虑把这个表拆分成多个小表，来减轻单个表的压力，提高处理效率，此方式称为分表。
分表技术比较麻烦，要修改程序代码里的 SQL 语句，还要手动去创建其他表，也可以用` merge 存储引擎实现分表`，相对简单许多。分表后，程序是对一个总表进行操作，这个总表不存放数据，只有一些分表的关系，以及更新数据的方式，总表会根据不同的查询，将压力分到不同的小表上，因此提高并发能力和磁盘 I/O 性能。
分表分为垂直拆分和水平拆分：
**垂直拆分：** 把原来的一个很多字段的表拆分多个表，解决表的宽度问题。你可以把不常用的字段单独放到一个表中，也可以把大字段独立放一个表中，或者把关联密切的字段放一个表中。
**水平拆分：** 把原来一个表拆分成多个表，每个表的结构都一样，解决单表数据量大的问题。

## 5.5 分区

分区就是把一张表的数据根据表结构中的字段（如 range、list、hash 等）分成多个区块，这些区块可以在一个磁盘上，也可以在不同的磁盘上，分区后，表面上还是一张表，但数据散列在多个位置，这样一来，多块硬盘同时处理不同的请求，从而提高磁盘 I/O 读写性能。

# 阶段六: 数据库维护

## 6.1 性能状态关键指标 quota

其中有几个值帮可以我们计算出 QPS 和 TPS，如下:

```go
Uptime：服务器已经运行的实际，单位秒
Questions：已经发送给数据库查询数
Com_select：查询次数，实际操作数据库的
Com_insert：插入次数
Com_delete：删除次数
Com_update：更新次数
Com_commit：事务次数
Com_rollback：回滚次数
```

### 6.1.1 QPS

```go
// 1: 基于Questions计算出QPS
mysql> show global status like 'Questions';
mysql> show global status like 'Uptime';
QPS = Questions / Uptime

// 2: 基于Com_select、Com_insert、Com_delete、Com_update计算出QPS：
mysql> show global status where Variable_name in('com_select','com_insert','com_delete','com_update');
等待1秒再执行，获取间隔差值，第二次每个变量值减去第一次对应的变量值，就是QPS。

waitfor delay '00:00:01' // 延迟多长时间执行

// 3：比较
当数据库中myisam表比较多时，使用Questions计算比较准确。当数据库中innodb表比较多时，则以Com_*计算比较准确.
```

### 6.1.2 TPS

```go
// 1: 基于Com_commit和Com_rollback计算出TPS：
mysql> show global status like 'Com_commit';
mysql> show global status like 'Com_rollback';
mysql> show global status like 'Uptime';
TPS = (Com_commit + Com_rollback) / Uptime

// 2:
// 计算TPS，就不算查询操作了，计算出插入、删除、更新四个值即可
mysql> show global status where Variable_name in('com_insert','com_delete','com_update');
```

## 6.2 开启慢查询日志

- MySQL 开启慢查询日志，分析出哪条 SQL 语句比较慢，支持动态开启：

```bash
mysql> set global slow-query-log=on
# 开启慢查询日志
mysql> set global slow_query_log_file='/var/log/mysql/mysql-slow.log';
# 指定慢查询日志文件位置
mysql> set global log_queries_not_using_indexes=on;
# 记录没有使用索引的查询
mysql> set global long_query_time=1;
# 只记录处理时间1s以上的慢查询
分析慢查询日志，可以使用MySQL自带的mysqldumpslow工具，分析的日志较为简单。
mysqldumpslow -t 3 /var/log/mysql/mysql-slow.log
# 查看最慢的前三个查询
也可以使用percona公司的pt-query-digest工具，日志分析功能全面，可分析slow log、binlog、general log。
分析慢查询日志：pt-query-digest /var/log/mysql/mysql-slow.log
分析binlog日志：mysqlbinlog mysql-bin.000001 >mysql-bin.000001.sql
pt-query-digest --type=binlog mysql-bin.000001.sql
分析普通日志：pt-query-digest --type=genlog localhost.log
```

## 6.3 数据库备份

- 数据库大小在 2G 以内，建议使用官方的逻辑备份工具**mysqldump**
- 超过 2G 以上，建议使用 percona 公司的物理备份工具**xtrabackup**
- 两个工具都支持 InnoDB 存储引擎下热备，不影响业务读写操作。

## 6.4 数据库修复

## 6.5 mysql 服务器性能分析

```bash
$ vmstat 1 3
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 4568784 559828 2865040    0    0     9    15   34   49  1  2 97  0  0
 1  0      0 4568736 559828 2865040    0    0     0    32 2531 9745  1  2 98  0  0
 2  0      0 4568776 559828 2865040    0    0     0    28 2172 8694  2  1 97  0  0
```

# 阶段七: 其他

文章摘李振良老师的文章。
