
- [一: mysql 命令行连接](#一-mysql-命令行连接)
  - [二：常见的问题及处理](#二常见的问题及处理)
  - [三: 库操作](#三-库操作)
    - [3.1 创建数据库](#31-创建数据库)
    - [3.2 显示所有的数据库](#32-显示所有的数据库)
    - [3.3 删除数据库](#33-删除数据库)
    - [3.4 连接数据库](#34-连接数据库)
    - [3.5 查看当前使用的数据库](#35-查看当前使用的数据库)
    - [3.6 当前数据库包含的表信息：](#36-当前数据库包含的表信息)
  - [四: Table 表操作](#四-table-表操作)
    - [4.1 create table xxx 建表](#41-create-table-xxx-建表)
    - [4.2 desc xxx 获取表结构](#42-desc-xxx-获取表结构)
    - [4.3 删除/清空表](#43-删除清空表)
    - [4.4 insert into table xxx 给表插入数据](#44-insert-into-table-xxx-给表插入数据)
    - [4.5 查询表中的数据](#45-查询表中的数据)
    - [4.6 删除表中的数据](#46-删除表中的数据)
    - [4.7 修改表中数据](#47-修改表中数据)
    - [4.8 在表中增加字段](#48-在表中增加字段)
    - [4.9 更改表名和字段名](#49-更改表名和字段名)
    - [4.10 导入数据库表](#410-导入数据库表)
    - [4.11 修改数据库](#411-修改数据库)
    - [4.12 mysql 数据库的授权](#412-mysql-数据库的授权)
  - [五: DDL 操作](#五-ddl-操作)

# 一: mysql 命令行连接

- 安装并启动 mysql 服务;
- 在命令行连接 mysql: `mysql -hlocalhost -uroot -p`
  - -h: host
  - -u: username
  - -p: password
- `show databases; //显示存在的数据库`;
- `use test; //test为相对应的数据库名称，表示使用某个数据库`;
- `show tables; //显示此数据库的所有表`;
- `DESCRIBE MYTABLE; //显示表结构 `
- `desc book; //book为对应的表名称，此命令为展示表的字段详情`;
- `create database test; //建数据库。名字为test`;
- `create table user(id int(4) not null primary key auto_increment,username char(20)not null,password char(20) not null); // 创建表`;
- `insert into user (1,‘duoduo’,‘921012’); //插入一条数据`;
- `select * from user; //查询所有的信息`;
- 退出 MySQL：quit 或 exit ;

- 导入.sql 文件
  - `mysql>use database`;
  - `mysql>source d:/mysql.sql; `;

# 二：常见的问题及处理

- [关于 ubuntu 下 mysql 插入中文字符为？？？的情况解决方法](https://www.cnblogs.com/fangyh/p/6286699.html)
- [mysql 修改数据库表和表中的字段的编码格式的修改](https://blog.csdn.net/luo4105/article/details/50804148)
- [ubuntu 上修改 mysql 默认字符编码出现的 Job failed to start 解决方法](https://blog.csdn.net/leroy008/article/details/15816391)

# 三: 库操作

## 3.1 创建数据库

```sql
命令：create database <数据库名>
例如：建立一个名为sqlroad的数据库
mysql> create database sqlroad;
```

## 3.2 显示所有的数据库

```sql
命令：show databases （注意：最后有个 s）
mysql> show databases;
```

## 3.3 删除数据库

```sql
命令：drop database <数据库名>
例如：删除名为 sqlroad 的数据库
mysql> drop database sqlroad;

```

## 3.4 连接数据库

```sql
命令：use <数据库名>
例如：如果 sqlroad 数据库存在，尝试存取它：
mysql> use sqlroad;
屏幕提示：Database changed
```

## 3.5 查看当前使用的数据库

```sql
mysql> select database();
```

## 3.6 当前数据库包含的表信息：

```sql
mysql> show tables; （注意：最后有个 s）
```

# 四: Table 表操作

- 表操作，操作之前应连接某个数据库；

## 4.1 create table xxx 建表

```sql
-- 命令：create table <表名> ( <字段名> <类型> [,..<字段名n> <类型n>]);

mysql> create table MyClass(
> id int(4) not null primary key auto_increment,
> name char(20) not null,
> sex int(4) not null default ’′,
> degree double(16,2));
```

## 4.2 desc xxx 获取表结构

```sql
-- 命令：desc 表名，或者show columns from 表名

mysql>DESCRIBE MyClass
mysql> desc MyClass;
mysql> show columns from MyClass;
```

## 4.3 删除/清空表

```sql
-- 删除表
-- 命令：drop table <表名>

-- 例如：删除表名为 MyClass 的表
mysql> drop table MyClass;


-- 清空表
mysql> delete from MYTABLE;
```

## 4.4 insert into table xxx 给表插入数据

```sql
-- 命令：insert into <表名> [( <字段名>[,..<字段名n> ])] values ( 值 )[, ( 值n )]

mysql> insert into MyClass values(1,’Tom’,96.45),(2,’Joan’,82.99), (2,’Wang’, 96.59);
```

## 4.5 查询表中的数据

```sql
-- 命令：select <字段，字段，...> from < 表名 > where < 表达式 >

select * from table ...
```

## 4.6 删除表中的数据

```sql
-- 命令：delete from 表名 where 表达式
delete from MyClass where id=1;
```

## 4.7 修改表中数据

```sql
-- 命令：update 表名 set 字段=新值,…where 条件
update MyClass set name=’Mary’where id=1;
```

## 4.8 在表中增加字段

```sql
-- 命令：alter table 表名 add字段 类型 其他;
-- 例如：在表MyClass中添加了一个字段passtest，类型为int(4)，默认值为
alter table MyClass add passtest int(4) default ’′
```

## 4.9 更改表名和字段名

```sql
-- 命令：rename table 原表名 to 新表名;
mysql> rename table MyClass to YouClass;

更新字段内容
update 表名 set 字段名 = 新内容
update 表名 set 字段名 = replace(字段名,’旧内容’, 新内容’)
```

## 4.10 导入数据库表

```sql
创建.sql文件

先产生一个库如auction
mysqladmin -u root -p create auction，会提示输入密码，然后成功创建。

导入auction.sql文件
mysql -u root -p auction < auction.sql。
通过以上操作，就可以创建了一个数据库auction以及其中的一个表auction。
```

## 4.11 修改数据库

```sql
在mysql的表中增加字段：

alter table dbname add column userid int(11) not null primary key auto_increment;

这样，就在表dbname中添加了一个字段userid，类型为int(11)。
```

## 4.12 mysql 数据库的授权

```sql
mysql>grant select,insert,delete,create,drop on *.* (或test.*/user.*/..) to 用户名@localhost  identified by ‘密码’；

-- 如：新建一个用户帐号以便可以访问数据库，需要进行如下操作：
mysql> grant usage
　　-> ON test.*
　　-> TO testuser@localhost;
　　Query OK, 0 rows affected (0.15 sec)

-- 此后就创建了一个新用户叫：testuser，这个用户只能从localhost连接到数据库并可以连接到test 数据库。下一步，我们必须指定testuser这个用户可以执行哪些操作：

mysql> GRANT select, insert, delete,update
　　-> ON test.*
　　-> TO testuser@localhost;
　　Query OK, 0 rows affected (0.00 sec)

-- 此操作使testuser能够在每一个test数据库中的表执行SELECT，INSERT和DELETE以及UPDATE查询操作。现在我们结束操作并退出MySQL客户程序：

mysql> exit
```

# 五: DDL 操作
