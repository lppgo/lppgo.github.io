---
title: "01-005-lppKDB脚本"
author: "lucas"
description: "..."
date: 2025-10-24
lastmod: 2025-10-24

tags: ["DB", "KDB"]
categories: ["DB"]
keywords: ["DB", "KDB"]
---

- [1：简介](#1简介)
- [2：Linux 安装多个版本 python](#2linux-安装多个版本-python)
  - [2.1 下载 python 安装包](#21-下载-python-安装包)
  - [2.2 update-alternative 管理多版本 python](#22-update-alternative-管理多版本-python)
- [3: pip 源设置](#3-pip-源设置)

# 1：KDB 简介

# 2：KDB 安装

# 3：KDB+/Q 脚本

```sql
 wans//utf-8 ------------kdb+ Common Statments ---kdb+常用语句----------

// kdb+ tutorials https://www.timestored.com/kdb-guides/?utm_source=qstudio&utm_medium=app&utm_campaign=qstudio
// kdb+ keywords  https://www.timestored.com/kdb-guides/kdb-keyword-reference

// list
y:(`cpp;`python;`go;`java) // list of four symbols, y is variable name
y

y:(`cpp`python`go`java) // list of four symbols, Note not semicolon
y

y2:("symbol may have interior blanks") // string
y2
type y2

// string convert symbol  将字符串转换为符号
s: "hello world"
symbolList: `$(" " vs s) // use vs 函数 ; $ 是类型转换操作符
symbolList
symbolList[1]

// table  https://www.wenjiangs.com/doc/p4btamfe
// 创建表
userTable:([]name:(`cpp`go`python);[]amount:(100,200,300);[]price:(10.5,95.5,60.5))
// 获取表信息
cols userTable
userTable.name
meta userTable // 展示table meta信息: 列名， 列类型，其他信息

val:flip`name`id!(`John`Jenny`Jonathan;9 18 27) // flip 将list转为列，也就是list转为table

val:flip`name`id!(`John`Jenny`Jonathan;9 18 27)
idTable:flip (enlist`eid)!enlist 99 198 297
newTable: idTable ! val //
// select
select from responsev4 where sym like "*zjzg_test_1*", qid like "*6dc47d9e-b6bd-47e5-aa59-8ac4dc701776*",entrustno=100016,status=1

select count qid from responsev4  where sym like "*zjzg_test_1*"

select from responsev4 where sym like "*zjzg_test_1*",securityID like "*600570*"

select from responsev4 where qid like "*b9edeee9-88e3-4b45-8231-da6d1136a34d*", entrustno = 10009,status = 2

select from responsev4 where sym like "*zjzg_test_1*", entrustno = 10003

select count qid from responsev4 where sym like "*zjzg_test_1*"

0!select sym,qid,entrustno from responsev4Qid where sym like "*zjzg_test_1*", entrustno = 10001

`open xdesc select from tableB // by open filed sort

`resptime xdesc (select  from responsev4Qid where sym like "*2668i*") // sort xasc, xdesc

// 查询聚合语句
select count(qid) from responsev4 where sym like "*9878*"   , status in(2,3);
select sum(cumqty) from responsev4 where sym like "*9878*"   , status in(2,3);

// delete
delete columns from table  / delete columns
delete from table where clause
delete from `responsev4Qid where qid like "delete_test_1"
delete from `assetTab  where i>=0  // 清空表
drop `Stu    // 删除表

// insert
`trade insert (`hsbc`apple;302.0 730.40;3020 3012;09:30:17.00409:15:00.000)
insert[`cancelTab;enlist `sym`qid`entrustno


// update 更新语句
update entrustno: 10005 from (0!select from responsev4Qid where qid like "*c3c63d45-4c9c-4de6-8276-86b9a516c924*")
upd0['responsev4;update status:5i, cumqty:0i, avgpx:0.0f, note: `DFD from ( 0!select from responsev4Qid where sym like "*guangda test*")]


// insert 插入语句
insert[`cancelTab;enlist `sym`qid`entrustno!(`zjzg_test_1,`t7912h9sh3, 10004)];

// 发布数据.u.pub
u.pub[`cancelTab;enlist`sym`qid`entrustno!(`zjzg_test_1 ,`t7912h9sh3, 10003)];


// kdb 撤单指令
cancelReq:{[q] t:select sym, qid, entrustno from (select from responsev4Qid where qid = q); upd0[`cancelTab;t];}
cancelReq[`$"a3dcb0ea-d26a-40d6-87b6-98a6b705fc4e"]

//  time
select from responsev4Qid where resptime.time>09:40:00 ,status=6, note like "*ACK*"

// group

// cancel order

cancelReq:{[q] t:select sym, qid, entrustno from (select from responsev4Qid where  qid like "*dca382c8*"  ); upd0[`cancelTab;t];}

cancelReq[`$"527ed110-6e4a-11ef-8997-00163e313bec"]


// limit stat
select count qid by `second$time from request where sym like "*1099*"
select count qid by `second$resptime  from responsev4Qid

// not sym like "*gs2828i*"

//
(1) 查看状态不正常的订单，比如status=0，3
(2) qmt查看账户交易是否正常，GT停用启用该账户:
(3) 重启下游交易程序，并查看订单状态是否正常回报;
(4) 没回报的话，手动修改订单状态
(5) 没有报出去order,状态为3，置为5
(6) qmt成交，cim丢失了，先把该账户对应订单置为0，重启客户端，停用启用,在重启下游交易程序


//  统计
r: select sym,qid,time from request where sym=`mshw_ubs26_03
v: select  sym,qid,resptime,status from responsev4 where status=1, sym in (`mshw_ubs26_03), not null resptime
v_unkeyed: select  sym,qid,resptime,status from responsev4 where status=1, sym in (`mshw_ubs26_03)
v_keyed: `qid xkey v_unkeyed // 将右表 v_unkeyed 转换为以 qid 为键的键控表
jt: r ij v_keyed // lj, ij
select from jt  where not null resptime
select sym,qid,time,latency: resptime - time  from jt  where not null resptime
select sym,qid,time,latency_ms: 0.001 * (resptime - time)    from jt  where not null resptime

select sym,qid,time,latency: 1000000*(resptime - time) from jt  where not null resptime ,qid=`$"3fcac912-b078-11f0-b812-00163e313bec" //含有-, `$"string" 先转字符串再转 symbol

```
